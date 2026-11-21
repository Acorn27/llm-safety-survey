#!/usr/bin/env python3
"""Generate the static figures for docs/index.html.

Every number below comes from the notes in this repo (paper-list.md, years/*.md,
verification/*.md). Each data block names its source. Run:

    python3 figures/build_figures.py

The script rewrites the regions of docs/index.html delimited by
<!--FIG:name--> ... <!--/FIG:name--> and touches nothing else. Output is plain
HTML and inline SVG (no JavaScript, no external libraries), colored with the
page's CSS variables so light and dark mode both work.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "docs" / "index.html"


def esc(s):
    return html.escape(str(s), quote=True)


# Entry numbers on the page (also the reference numbers [1]-[15]).
NUM = {"RealToxicityPrompts": 1, "TruthfulQA": 2, "Anthropic red team": 3, "AdvBench": 4, "DecodingTrust": 5,
       "XSTest": 6, "HarmBench": 7, "JailbreakBench": 8, "StrongREJECT": 9, "WMDP": 10, "AgentDojo": 11,
       "VCT": 12, "MASK": 13, "ART": 14, "IPI Arena": 15}


def nl(name):
    return f"{NUM[name]} · {name}"


# --------------------------------------------------------------------------
# Figure 2: life-cycle timeline
# Event types: R release, A adoption evidence (primary document), S saturated /
# replaced / retired, F fragile dependency, U dataset update.
# Dates are from the verification notes. approx=True means the month or the
# exact position is not stated in our sources, so the marker is hollow.
# --------------------------------------------------------------------------
NOW = 2026 + (10 + 21 / 30) / 12  # 2026-11-21, the date of this build
LIFECYCLE = [
    ("RealToxicityPrompts", [
        ("R", 2020, 9, "arXiv, Sep 2020", False),
        ("A", 2023, 3, "GPT-4 technical report: 0.73% toxic generations", False),
        ("F", 2026, 12, "Perspective API scheduled to end 31 Dec 2026", False)]),
    ("TruthfulQA", [
        ("R", 2021, 9, "arXiv, Sep 2021", False),
        ("A", 2023, 3, "GPT-4 technical report cites it", False),
        ("A", 2023, 7, "Llama 2 paper reports it", False),
        ("U", 2025, 1, "Authors revise the dataset (Jan 2025)", False)]),
    ("Anthropic red team", [
        ("R", 2022, 8, "arXiv, 23 Aug 2022", False),
        ("A", 2024, 11, "HELM Safety v1.0 (8 Nov 2024) includes it", False)]),
    ("DecodingTrust", [
        ("R", 2023, 6, "arXiv, Jun 2023", False)]),
    ("AdvBench", [
        ("R", 2023, 7, "arXiv, 27 Jul 2023", False),
        ("A", 2024, 2, "Reused by HarmBench (arXiv, 6 Feb 2024)", False),
        ("A", 2024, 3, "Reused by JailbreakBench (arXiv, 28 Mar 2024)", False)]),
    ("XSTest", [
        ("R", 2023, 8, "arXiv, Aug 2023", False),
        ("A", 2024, 11, "HELM Safety v1.0 (8 Nov 2024) includes it", False)]),
    ("HarmBench", [
        ("R", 2024, 2, "arXiv, 6 Feb 2024", False),
        ("A", 2024, 11, "HELM Safety v1.0 (8 Nov 2024)", False),
        ("A", 2025, 7, "FLI AI Safety Index, Summer 2025 (month approximate)", True),
        ("A", 2025, 9, "NIST CAISI DeepSeek evaluation samples HarmBench queries", False)]),
    ("StrongREJECT", [
        ("R", 2024, 2, "arXiv, 15 Feb 2024", False),
        ("A", 2024, 12, "OpenAI o1 system card", False),
        ("A", 2025, 5, "Claude 4 system card, Sec. 2.7", False),
        ("A", 2025, 9, "GPT-5-Codex addendum, 15 Sep 2025", False),
        ("S", 2026, 1, "OpenAI replaces its StrongReject-based benchmark ahead of GPT-5.4 (date not stated; position approximate)", True)]),
    ("WMDP", [
        ("R", 2024, 3, "arXiv, 5 Mar 2024", False),
        ("S", 2025, 6, "Epoch AI (13 Jun 2025): WMDP-style bio evaluations largely saturated", False),
        ("A", 2025, 7, "Gemini 2.5 technical report (Bio and Chem)", False),
        ("A", 2025, 8, "xAI Grok 4 card (20 Aug 2025)", False)]),
    ("JailbreakBench", [
        ("R", 2024, 3, "arXiv, 28 Mar 2024", False)]),
    ("AgentDojo", [
        ("R", 2024, 6, "arXiv, Jun 2024", False),
        ("A", 2025, 1, "NIST CAISI agent-hijacking evaluation", False),
        ("A", 2025, 9, "NIST CAISI DeepSeek evaluation", False),
        ("A", 2026, 5, "Meta Muse Spark report", False)]),
    ("MASK", [
        ("R", 2025, 3, "arXiv, 5 Mar 2025", False),
        ("A", 2025, 8, "xAI Grok 4 card (20 Aug 2025)", False),
        ("A", 2026, 5, "Meta Muse Spark report", False),
        ("S", 2026, 6, "Anthropic Sonnet 5 card: 3.1% lying; Scale leaderboard top about 96% honest (near ceiling)", False)]),
    ("VCT", [
        ("R", 2025, 4, "arXiv, 21 Apr 2025", False),
        ("S", 2025, 5, "Anthropic Claude 4 card: \"we consider this evaluation to have saturated\"", False),
        ("A", 2025, 8, "xAI Grok 4 card (20 Aug 2025)", False),
        ("A", 2026, 5, "Meta Muse Spark report", False),
        ("A", 2026, 7, "Anthropic Opus 5 card still reports it (0.59)", False)]),
    ("ART", [
        ("R", 2025, 7, "arXiv, 28 Jul 2025", False),
        ("A", 2026, 2, "Anthropic Opus 4.6 card", False),
        ("A", 2026, 5, "Meta Muse Spark report", False),
        ("S", 2026, 7, "Anthropic Opus 5 card: ART retired (24 Jul 2026)", False)]),
    ("IPI Arena", [
        ("R", 2026, 3, "arXiv, 16 Mar 2026", False),
        ("A", 2026, 6, "Anthropic Sonnet 5 card (30 Jun 2026)", False),
        ("A", 2026, 9, "OpenAI GPT-6 Astra page (3 Sep 2026)", False),
        ("A", 2026, 10, "Google Gemini 4 Argon blog (13 Oct 2026)", False)]),
]


def marker(kind, x, y, approx):
    st = ' style="fill:var(--bg)"' if approx else ""
    if kind == "R":
        return f'<circle cx="{x:.1f}" cy="{y}" r="5" class="mk-r"{st}/>'
    if kind == "A":
        d = 5.5
        pts = f"{x:.1f},{y-d} {x+d:.1f},{y} {x:.1f},{y+d} {x-d:.1f},{y}"
        return f'<polygon points="{pts}" class="mk-a"{st}/>'
    if kind == "S":
        d = 6
        pts = f"{x:.1f},{y-d} {x+d:.1f},{y+d-1} {x-d:.1f},{y+d-1}"
        return f'<polygon points="{pts}" class="mk-s"{st}/>'
    if kind == "F":
        d = 4.5
        return f'<path d="M{x-d:.1f},{y-d} L{x+d:.1f},{y+d} M{x+d:.1f},{y-d} L{x-d:.1f},{y+d}" class="mk-f"/>'
    if kind == "U":
        d = 3.5
        return f'<rect x="{x-d:.1f}" y="{y-d}" width="{2*d}" height="{2*d}" class="mk-u"/>'
    raise ValueError(kind)


def fig_lifecycle():
    W, left, right = 900, 150, 880
    y0, y1 = 2020.0, 2027.05
    top, rh = 44, 27
    H = top + rh * len(LIFECYCLE) + 74

    def X(year):
        return left + (year - y0) / (y1 - y0) * (right - left)

    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-labelledby="lc-t lc-d" class="fig">',
           '<title id="lc-t">Life cycle of 15 safety benchmarks, 2020 to 2026</title>',
           '<desc id="lc-d">Each row is a benchmark. A circle marks release, diamonds mark documented use, '
           'triangles mark saturation, replacement or retirement, an X marks a fragile dependency.</desc>']
    # year grid
    for yr in range(2020, 2028):
        x = X(yr)
        out.append(f'<line x1="{x:.1f}" y1="{top-8}" x2="{x:.1f}" y2="{top+rh*len(LIFECYCLE)}" class="grid"/>')
        if yr < 2027:
            out.append(f'<text x="{(x+X(yr+1))/2:.1f}" y="{top-16}" text-anchor="middle" class="ax">{yr}</text>')
    # now line
    xn = X(NOW)
    out.append(f'<line x1="{xn:.1f}" y1="{top-8}" x2="{xn:.1f}" y2="{top+rh*len(LIFECYCLE)}" class="now"/>')
    out.append(f'<text x="{xn-4:.1f}" y="{top+rh*len(LIFECYCLE)+14}" text-anchor="end" class="ax">now (Nov 2026)</text>')
    for i, (name, events) in enumerate(LIFECYCLE):
        cy = top + rh * i + rh / 2
        if i % 2 == 0:
            out.append(f'<rect x="0" y="{top+rh*i}" width="{W}" height="{rh}" class="band"/>')
        out.append(f'<text x="{left-12}" y="{cy+4:.1f}" text-anchor="end" class="rowlab">{esc(nl(name))}</text>')
        xs = [X(ev[1] + (ev[2] - 0.5) / 12) for ev in events]
        out.append(f'<line x1="{xs[0]:.1f}" y1="{cy}" x2="{max(xn, xs[-1]):.1f}" y2="{cy}" class="life"/>')
        for ev, x in zip(events, xs):
            kind, _, _, label, approx = ev
            out.append(f'<g>{marker(kind, x, cy, approx)}<title>{esc(label)}</title></g>')
    # legend (two rows)
    rows = [[("R", "release"), ("A", "documented use (lab card, harness, government evaluation, or reuse by a later benchmark)")],
            [("S", "called saturated, replaced or retired"), ("F", "dependency being withdrawn"), ("U", "dataset revised")]]
    for ri, row in enumerate(rows):
        ly = H - 36 + ri * 20
        lx = 14
        for kind, lab in row:
            out.append(marker(kind, lx + 6, ly - 4, False))
            out.append(f'<text x="{lx+18}" y="{ly}" class="lg">{esc(lab)}</text>')
            lx += 18 + 6.4 * len(lab) + 24
    out.append('</svg>')
    svg = "\n".join(out)
    return f"""<figure>
    <figcaption><strong>Figure 2.</strong> Life cycle of each benchmark, in order of release; the number before each name is its entry number. Hollow markers have an approximate position because the month is not stated in our sources. Only events with a source and a stated date are plotted, so absence of a marker does not mean absence of use. Hover a marker for its source. Data: release dates from the papers; adoption and replacement events from the system cards, blog posts, evaluations and later benchmarks listed in References (this script, <code>figures/build_figures.py</code>, holds each date and source).</figcaption>
    <div class="sr-only">Text description of Figure 2: fifteen rows, one per benchmark, on a 2020 to 2026 time axis. Older benchmarks such as RealToxicityPrompts and TruthfulQA show use in 2023 reports and little after. StrongREJECT, WMDP, VCT, MASK and ART each show a saturation, replacement or retirement marker within one to two years of first lab use. IPI Arena, released in March 2026, shows three lab uses by October 2026 and no saturation marker yet.</div>
    <div class="scroll-x"><div style="min-width:760px">{svg}</div></div>
  </figure>"""


# --------------------------------------------------------------------------
# Figure 5: adoption matrix. y = primary document found, p = indirect or weaker
# evidence, n = searched, not found. Tips are the evidence behind each cell.
# Sources: verification/*.md (system-card-recheck, agents-2025-2026, ipi-arena,
# 2025-candidates, 2024, early-2020-2022, 2023).
# --------------------------------------------------------------------------
COLS = ["OpenAI", "Anthropic", "xAI", "Google", "Meta", "UK AISI / US CAISI", "Harness or leaderboard"]
MATRIX = [
    ("RealToxicityPrompts", [("y", "GPT-4 technical report (2023)"), "n", "n", "n", "n", "n", ("y", "HELM, lm-evaluation-harness")]),
    ("TruthfulQA", [("y", "GPT-4 technical report (2023)"), "n", "n", "n", ("y", "Llama 2 paper (2023)"), "n", ("y", "Inspect Evals, lm-evaluation-harness, HELM")]),
    ("Anthropic red team", ["n", ("n", "Built by Anthropic; no later Anthropic card found citing it"), "n", "n", "n", "n", ("y", "HELM Safety v1.0 (AnthropicRedTeam scenario)")]),
    ("AdvBench", ["n", "n", "n", "n", "n", "n", ("n", "Reused by HarmBench and JailbreakBench, which are benchmarks, not harnesses; not in the Inspect Evals listing")]),
    ("DecodingTrust", ["n", "n", "n", "n", "n", "n", ("n", "not in the Inspect Evals directory listing")]),
    ("XSTest", ["n", ("p", "A Claude 3 figure appears only in a secondary blog"), "n", "n", "n", "n", ("y", "Inspect Evals, HELM Safety v1.0")]),
    ("HarmBench", ["n", "n", "n", "n", "n", ("y", "NIST CAISI DeepSeek evaluation (Sep 2025) sampled HarmBench queries"), ("y", "HELM Safety v1.0, FLI AI Safety Index")]),
    ("JailbreakBench", ["n", "n", "n", "n", "n", "n", ("n", "own leaderboard only; not in the Inspect Evals listing we read")]),
    ("StrongREJECT", [("y", "o1 card and GPT-5 family cards"), ("y", "Claude 4 card, Sec. 2.7"), "n", "n", ("p", "Cited in the Muse Spark report's reference list"), ("y", "NIST CAISI DeepSeek evaluation sampled StrongREJECT queries"), ("y", "Inspect Evals")]),
    ("WMDP", [("n", "o1 card mentions WMDP only as an unreported contextual evaluation"), "n", ("y", "Grok 4 card, Table 3"), ("y", "Gemini 2.5 technical report (Bio and Chem)"), ("p", "Cited in the Muse Spark report's reference list"), "n", ("y", "Inspect Evals")]),
    ("AgentDojo", ["n", "n", "n", "n", ("y", "Muse Spark report"), ("y", "NIST CAISI; UK AISI Inspect Evals; International Network joint testing"), ("y", "Inspect Evals; agentdojo.spylab.ai results")]),
    ("VCT", [("y", "GPT-5 card, Table 15 (run by SecureBio)"), ("y", "Claude 4, Sonnet 4.5, Sonnet 5 and Opus 5 cards"), ("y", "Grok 4 card (text-only portion)"), ("p", "Gemini 2.5 report lists \"SecureBio VMQA\"; that this is VCT is our inference"), ("y", "Muse Spark report"), ("n", "none found in UK AISI or CAISI reports we read"), "n"]),
    ("MASK", ["n", ("y", "Sonnet 5 and Opus 5 cards"), ("y", "Grok 4 card"), "n", ("y", "Muse Spark report"), "n", ("y", "Scale leaderboard (run by an author organization)")]),
    ("ART", [("y", "GPT-5 card (Figure 8)"), ("y", "Claude cards through Sonnet 4.5 and Opus 4.6; retired in the Opus 5 card"), "n", "n", ("y", "Muse Spark report"), ("p", "co-developed by UK AISI; no scores run by them found"), ("n", "private leaderboard by design")]),
    ("IPI Arena", [("y", "GPT-6 Astra page"), ("y", "Sonnet 5, Opus 5 and Sonnet 5.5 cards"), "n", ("p", "one sentence in the Gemini 4 Argon blog"), ("n", "Meta co-authored; its report does not appear to cite it (search not conclusive)"), ("p", "co-developed by UK AISI and CAISI; no scores run by them found"), "n"]),
]

SYM = {"y": "●", "p": "◐", "n": "○"}
SYMTXT = {"y": "primary document found", "p": "indirect or weaker evidence", "n": "not found"}


def fig_matrix():
    rows = []
    for name, cells in MATRIX:
        tds = []
        for col, c in zip(COLS, cells):
            st, tip = (c, "") if isinstance(c, str) else c
            title = f'{nl(name)}, {col}: {SYMTXT[st]}' + (f'. {tip}' if tip else "")
            tds.append(f'<td class="am {st}" title="{esc(title)}"><span aria-hidden="true">{SYM[st]}</span><span class="sr-only">{esc(SYMTXT[st])}</span></td>')
        rows.append(f'<tr><th scope="row">{esc(nl(name))}</th>{"".join(tds)}</tr>')
    head = "".join(f'<th scope="col">{esc(c)}</th>' for c in COLS)
    return f"""<figure>
    <figcaption><strong>Figure 5.</strong> Where each benchmark has been used, by adopter, at any date. <span class="am-key y">●</span> primary document found; <span class="am-key p">◐</span> indirect or weaker evidence (secondary source, reference-list citation only, co-developer, single blog sentence, or our inference); <span class="am-key n">○</span> searched and not found. Hover a cell for its evidence. "Not found" is weaker than "does not use": several card PDFs were read through text extraction and the Gemini 2.5 Pro card was not accessible. Source: verification notes in this repository, checked 2026-10-13.</figcaption>
    <div class="scroll-x"><table class="am-table"><thead><tr><th></th>{head}</tr></thead><tbody>
{chr(10).join(rows)}
</tbody></table></div>
  </figure>"""


# --------------------------------------------------------------------------
# Figure 6: citations vs frontier-lab use.
# Citations: Semantic Scholar, 2026-10-13 (paper-list.md). None = not retrieved.
# in_card: reported in a frontier-lab system card or report dated 2025-26.
# --------------------------------------------------------------------------
CITES = [
    ("TruthfulQA", 4093, False, "Used in 2023 reports (GPT-4, Llama 2); no 2025-26 card found"),
    ("HarmBench", 1676, False, "No frontier card found; used by HELM Safety, FLI index, NIST CAISI"),
    ("Anthropic red team", 904, False, "HELM Safety v1.0; no 2025-26 frontier card found"),
    ("DecodingTrust", 724, False, "No lab or leaderboard use found"),
    ("JailbreakBench", 704, False, "Academic reuse only"),
    ("XSTest", 590, False, "Inspect Evals and HELM Safety; no frontier card found"),
    ("WMDP", 582, True, "xAI Grok 4 card; Gemini 2.5 technical report (2025)"),
    ("StrongREJECT", 433, True, "Claude 4 card and GPT-5 family cards (2025), then replaced at OpenAI"),
    ("AgentDojo", 152, True, "Meta Muse Spark report (2026). Count likely an undercount"),
    ("VCT", 43, True, "OpenAI, Anthropic, xAI and Meta cards"),
    ("RealToxicityPrompts", None, False, "Used in the 2023 GPT-4 report; no 2025-26 card found"),
    ("AdvBench", None, False, "Reused by HarmBench and JailbreakBench; no lab use found"),
    ("MASK", None, True, "Grok 4, Anthropic and Meta documents"),
    ("ART", None, True, "GPT-5 card, Anthropic cards through Opus 4.6, Meta report (2025-26); retired in 2026"),
    ("IPI Arena", None, True, "Anthropic and OpenAI cards; Google blog"),
]

def fig_cites():
    W, left, maxw = 900, 170, 460
    rh = 28
    top = 38
    H = top + rh * len(CITES) + 48
    mx = max(c[1] for c in CITES if c[1])
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-labelledby="ct-t ct-d" class="fig">',
           '<title id="ct-t">Citations versus frontier-lab use</title>',
           '<desc id="ct-d">Horizontal bars of citation counts for ten benchmarks, with a marker showing whether each appears in a 2025 or 2026 frontier-lab card.</desc>',
           f'<text x="{left+maxw+70}" y="{top-14}" class="ax" text-anchor="start">in a 2025–26 frontier card?</text>',
           f'<text x="{left}" y="{top-14}" class="ax">Semantic Scholar citations</text>']
    for i, (name, n, card, tip) in enumerate(CITES):
        y = top + rh * i
        cy = y + rh / 2
        if i % 2 == 0:
            out.append(f'<rect x="0" y="{y}" width="{W}" height="{rh}" class="band"/>')
        out.append(f'<text x="{left-10}" y="{cy+4:.1f}" text-anchor="end" class="rowlab">{esc(nl(name))}</text>')
        if n:
            w = max(2, n / mx * maxw)
            out.append(f'<rect x="{left}" y="{y+6}" width="{w:.1f}" height="{rh-12}" class="bar"><title>{esc(nl(name))}: {n:,} citations</title></rect>')
            out.append(f'<text x="{left+w+6:.1f}" y="{cy+4:.1f}" class="val">{n:,}</text>')
        else:
            out.append(f'<text x="{left+6}" y="{cy+4:.1f}" class="val muted">not retrieved</text>')
        mxp = left + maxw + 70
        if card:
            out.append(f'<circle cx="{mxp+8}" cy="{cy}" r="6" class="yes"><title>{esc(tip)}</title></circle>')
            out.append(f'<text x="{mxp+22}" y="{cy+4:.1f}" class="val">yes</text>')
        else:
            out.append(f'<circle cx="{mxp+8}" cy="{cy}" r="6" class="no"><title>{esc(tip)}</title></circle>')
            out.append(f'<text x="{mxp+22}" y="{cy+4:.1f}" class="val muted">none found</text>')
    out.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+rh*len(CITES)}" class="grid"/>')
    out.append('</svg>')
    svg = "\n".join(out)
    return f"""<figure>
    <figcaption><strong>Figure 6.</strong> Citations and use in 2025–26 frontier cards disagree. Bars: Semantic Scholar citation counts, checked 2026-10-13, linear scale from zero. Right: whether the benchmark appears in a frontier-lab system card or report dated 2025–26. Citation counts favour older papers, so age is a confounder, and AgentDojo's count is likely an undercount. Counts for five benchmarks could not be retrieved (rate limiting) and are shown without bars. "None found" is weaker than "none exists".</figcaption>
    <div class="sr-only">Text description of Figure 6: TruthfulQA has the most citations (4,093), followed by HarmBench (1,676) and the Anthropic red-team dataset (904). All three, and DecodingTrust (724), JailbreakBench (704) and XSTest (590), have no 2025 to 2026 frontier card use found. WMDP (582), StrongREJECT (433), AgentDojo (152) and VCT (43) each appear in at least one frontier document. Five benchmarks have no retrieved count: RealToxicityPrompts and AdvBench with no frontier card use found, and MASK, ART and IPI Arena with use in frontier documents. VCT has the fewest retrieved citations but appears in the most cards.</div>
    <div class="scroll-x"><div style="min-width:720px">{svg}</div></div>
  </figure>"""


# --------------------------------------------------------------------------
# Figure 3: why 2024 needed standardization.
# (a) AdvBench: 520 rows in the released CSV; 58 unique behaviors after HarmBench's
#     manual and automated semantic deduplication (verification/2023.md).
# (b) Average agreement with human labels, HarmBench paper Table 3: AdvBench-style
#     substring matching 69.93, GPT-4 88.37, HarmBench classifier 93.19
#     (verification/2023.md and 2024.md).
# --------------------------------------------------------------------------
def fig_standardization():
    W, H = 900, 262
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-labelledby="st-t st-d" class="fig">',
           '<title id="st-t">Why 2024 needed standardization</title>',
           '<desc id="st-d">Panel a: AdvBench has 520 rows but 58 unique behaviors. Panel b: agreement with human labels for three ways of judging jailbreaks.</desc>']
    # panel a
    out.append('<text x="10" y="22" class="ptitle">(a) AdvBench: rows vs. unique behaviors</text>')
    left, maxw = 14, 360
    for i, (lab, n, cls) in enumerate([("Rows in the released CSV", 520, "bar"), ("Unique behaviors after semantic deduplication", 58, "bar hi")]):
        y = 56 + i * 70
        out.append(f'<text x="{left}" y="{y-8}" class="val">{esc(lab)}</text>')
        w = n / 520 * maxw
        out.append(f'<rect x="{left}" y="{y}" width="{w:.1f}" height="28" class="{cls}"><title>{esc(lab)}: {n}</title></rect>')
        out.append(f'<text x="{left+w+8:.1f}" y="{y+19}" class="val">{n}</text>')
    for j, line in enumerate(["About 89% fewer (our arithmetic: 1 − 58/520).", "HarmBench also found 50% of 20 sampled behaviors", "findable by a 10-minute web search (one author,", "small sample)."]):
        out.append(f'<text x="{left}" y="{56+70+56+j*16}" class="note-s">{esc(line)}</text>')
    # panel b
    px, pw = 470, 400
    out.append(f'<text x="{px}" y="22" class="ptitle">(b) Agreement with human labels (%)</text>')
    items = [("Substring matching (AdvBench-style)", 69.93, "bar"), ("GPT-4 as judge", 88.37, "bar"), ("HarmBench classifier", 93.19, "bar hi")]
    for i, (lab, v, cls) in enumerate(items):
        y = 56 + i * 52
        out.append(f'<text x="{px}" y="{y-8}" class="val">{esc(lab)}</text>')
        w = v / 100 * pw
        out.append(f'<rect x="{px}" y="{y}" width="{w:.1f}" height="26" class="{cls}"><title>{esc(lab)}: {v}</title></rect>')
        out.append(f'<text x="{px+w+8:.1f}" y="{y+18}" class="val">{v}</text>')
    out.append(f'<line x1="{px}" y1="44" x2="{px}" y2="{56+52*3-18}" class="grid"/>')
    out.append(f'<line x1="{px+pw}" y1="44" x2="{px+pw}" y2="{56+52*3-18}" class="grid dash"/>')
    out.append(f'<text x="{px+pw}" y="{56+52*3-4}" text-anchor="end" class="ax">100</text><text x="{px}" y="{56+52*3-4}" class="ax">0</text>')
    out.append('</svg>')
    svg = "\n".join(out)
    return f"""<figure>
    <figcaption><strong>Figure 3.</strong> Two measurement flaws behind the 2024 standardization wave. (a) AdvBench's released file has 520 rows, but HarmBench's manual and automated semantic deduplication leaves 58 unique behaviors. (b) Average agreement with human labels from HarmBench's classifier comparison (its Table 3): refusal-string matching, the AdvBench-style metric, agrees least. Axis starts at zero. Both panels are HarmBench's measurements, not ours, on its own data, so the numbers show that benchmark's case and are not a neutral head-to-head. Sources: [4], [7].</figcaption>
    <div class="sr-only">Text description of Figure 3: Panel a shows a long bar of 520 and a short bar of 58 for AdvBench rows against unique behaviors. Panel b shows agreement with human labels rising from 69.93 percent for substring matching, to 88.37 for GPT-4, to 93.19 for the HarmBench classifier.</div>
    <div class="scroll-x"><div style="min-width:760px">{svg}</div></div>
  </figure>"""


# --------------------------------------------------------------------------
# Figure 4: IPI Arena attack success at k=15 attempts (lower is better).
# Anthropic Opus 5 card, p.74 (verification/ipi-arena.md): all models in the
# same card and attack set. Other sources are plotted separately and hatched
# because their attack sets, quarters and settings differ.
# --------------------------------------------------------------------------
IPI_CARD = [("Claude Opus 5", 2.0), ("Claude Mythos 5", 2.6), ("Claude Opus 4.8", 5.5), ("Claude Sonnet 5", 5.9),
            ("Muse Spark (Meta)", 16.5), ("GPT 5.6 Sol", 20.0), ("GPT 5.5", 20.8), ("GPT 5.6 Terra", 30.4), ("GPT 5.6 Luna", 43.9)]
IPI_OTHER = [("GPT 5.6 Sol (OpenAI's own report)", 27.0, "OpenAI GPT-6 Astra page: 1,810 curated attacks from Q1 and Q2 2026"),
             ("GPT-6 Astra (OpenAI)", 8.5, "OpenAI GPT-6 Astra page: 15 attempts per scenario"),
             ("Gemini 4 Argon (Google blog)", 0.7, "Google blog, 13 Oct 2026: one sentence, self-reported")]


def fig_ipi():
    W, left, maxw = 900, 250, 460
    rh = 26
    top = 40
    n1, n2 = len(IPI_CARD), len(IPI_OTHER)
    H = top + rh * n1 + 84 + rh * n2 + 20
    scale = maxw / 50.0
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-labelledby="ip-t ip-d" class="fig">',
           '<title id="ip-t">IPI Arena attack success within 15 attempts</title>',
           '<desc id="ip-d">Bars of attack success rate at 15 attempts. Nine models from Anthropic\'s Opus 5 card, then three values from other sources shown hatched because they are not comparable.</desc>',
           '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" class="hatch-bg"/><line x1="0" y1="0" x2="0" y2="6" class="hatch-ln"/></pattern></defs>',
           f'<text x="10" y="{top-16}" class="ptitle">Same card and attack set (Anthropic Opus 5 card, k = 15)</text>']
    ycoord = {}
    for i, (name, v) in enumerate(IPI_CARD):
        y = top + rh * i
        cy = y + rh / 2
        ycoord[name] = cy
        out.append(f'<text x="{left-10}" y="{cy+4:.1f}" text-anchor="end" class="rowlab">{esc(name)}</text>')
        out.append(f'<rect x="{left}" y="{y+5}" width="{v*scale:.1f}" height="{rh-10}" class="bar{" hi" if name.startswith("Claude") else ""}"><title>{esc(name)}: {v}%</title></rect>')
        out.append(f'<text x="{left+v*scale+6:.1f}" y="{cy+4:.1f}" class="val">{v}%</text>')
    y2 = top + rh * n1 + 66
    out.append(f'<text x="10" y="{y2-14}" class="ptitle">Other sources: different attack sets and settings, not comparable with the bars above</text>')
    for i, (name, v, tip) in enumerate(IPI_OTHER):
        y = y2 + rh * i
        cy = y + rh / 2
        ycoord[name] = cy
        out.append(f'<text x="{left-10}" y="{cy+4:.1f}" text-anchor="end" class="rowlab">{esc(name)}</text>')
        out.append(f'<rect x="{left}" y="{y+5}" width="{v*scale:.1f}" height="{rh-10}" class="bar-h"><title>{esc(tip)}</title></rect>')
        out.append(f'<text x="{left+v*scale+6:.1f}" y="{cy+4:.1f}" class="val">{v}%</text>')
    # discrepancy callout: to the right of every bar label, so nothing is overdrawn
    xs = left + 50 * scale - 6
    ya, yb = ycoord["GPT 5.6 Sol"], ycoord["GPT 5.6 Sol (OpenAI's own report)"]
    out.append(f'<path d="M{left+20.0*scale+46:.1f},{ya} H{xs:.1f} V{yb} H{left+27.0*scale+46:.1f}" class="callout"/>')
    out.append(f'<text x="{xs+8:.1f}" y="{yb-4:.1f}" class="note-s">Same model, two cards:</text>')
    out.append(f'<text x="{xs+8:.1f}" y="{yb+12:.1f}" class="note-s">20.0% vs 27.0%</text>')
    # axis
    ay = top + rh * n1 + 6
    for t in (0, 10, 20, 30, 40, 50):
        x = left + t * scale
        out.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{ay-2}" class="grid"/>')
        out.append(f'<text x="{x:.1f}" y="{ay+12}" text-anchor="middle" class="ax">{t}%</text>')
    out.append('</svg>')
    svg = "\n".join(out)
    return f"""<figure>
    <figcaption><strong>Figure 4.</strong> Probability that an attacker finds a successful indirect prompt injection within 15 attempts on IPI Arena (lower is better), as reported in vendor documents. Solid bars: nine models from the same Anthropic card, attack set and settings (Opus 5 card, p. 74; Claude models are run without additional safeguards while other models use public endpoints that may include them). Hatched bars: values from other sources with different attack sets, quarters or settings, which should not be ranked against the solid bars. The 20.0% versus 27.0% pair for one model shows why cross-card comparison is unsafe. Axis starts at zero. No uncertainty intervals were reported in the sources we read. Sources: [26], [30], [31].</figcaption>
    <div class="sr-only">Text description of Figure 4: Within Anthropic's card, attack success at 15 attempts runs from 2.0 percent for Claude Opus 5 up to 43.9 percent for GPT 5.6 Luna, with Meta's Muse Spark at 16.5 and GPT 5.6 Sol at 20.0. Separate hatched bars show OpenAI reporting 27.0 percent for GPT 5.6 Sol, 8.5 for GPT-6 Astra, and a Google blog reporting 0.7 for Gemini 4 Argon.</div>
    <div class="scroll-x"><div style="min-width:760px">{svg}</div></div>
  </figure>"""


FIGS = {
    "lifecycle": fig_lifecycle,
    "standardization": fig_standardization,
    "ipi": fig_ipi,
    "matrix": fig_matrix,
    "cites": fig_cites,
}


def main():
    s = PAGE.read_text(encoding="utf-8")
    for name, fn in FIGS.items():
        pat = re.compile(rf"(<!--FIG:{name}-->).*?(<!--/FIG:{name}-->)", re.S)
        if not pat.search(s):
            raise SystemExit(f"marker for {name} not found in {PAGE}")
        s = pat.sub(lambda m: f"{m.group(1)}\n  {fn()}\n  {m.group(2)}", s, count=1)
    PAGE.write_text(s, encoding="utf-8")
    print("figures written:", ", ".join(FIGS))


if __name__ == "__main__":
    main()
