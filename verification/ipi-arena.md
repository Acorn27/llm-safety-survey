# Verification: Gray Swan IPI Arena (arXiv 2603.15714), checked 2026-10-13

Legend: VERIFIED = checked against the cited primary page this session. UNVERIFIED = not confirmed or secondary only.
Method caveat: web pages were read through WebFetch, which returns a small-model summary of the page, so wording marked "quote" is as relayed by that tool. The three Anthropic system cards were downloaded and their text extracted directly (pypdf), so those quotes are from the PDFs themselves.

## 1. Paper metadata

| Field | Status | Value / source |
|---|---|---|
| Exact title | VERIFIED | "How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition" (https://arxiv.org/abs/2603.15714). The benchmark/arena is called "IPI Arena" (Gray Swan blog, repo, OpenAI page); the paper title does not contain that name. |
| Authors (31) | VERIFIED | Mateusz Dziemian, Maxwell Lin, Xiaohan Fu, Micha Nowak, Nick Winter, Eliot Jones, Andy Zou, Lama Ahmad, Kamalika Chaudhuri, Sahana Chennabasappa, Xander Davies, Lauren Deason, Benjamin L. Edelman, Tanner Emek, Ivan Evtimov, Jim Gust, Maia Hamin, Kat He, Klaudia Krawiecka, Riccardo Patana, Neil Perry, Troy Peterson, Xiangyu Qi, Javier Rando, Zifan Wang, Zihan Wang, Spencer Whitman, Eric Winsor, Arman Zharmagambetov, Matt Fredrikson, Zico Kolter. (Source: arXiv abs page.) |
| Affiliations | UNVERIFIED (summary only) | HTML page reportedly lists Gray Swan AI plus researchers from OpenAI, Meta, Anthropic, US CAISI, UK AISI, with a CMU / Center for AI Safety footnote. Not checked author by author. |
| Venue / year | VERIFIED: arXiv only | cs.CR (cross-list cs.AI). Submitted 16 Mar 2026, v1 only, no later version listed. Comments: "38 pages, 16 figures. Newer version to cover Q1 competition results on latest models in progress." No journal/conference listed. No peer-reviewed venue found. |
| PDF | VERIFIED | https://arxiv.org/pdf/2603.15714 (HTML: https://arxiv.org/html/2603.15714v1) |
| Citation count | UNVERIFIED | Semantic Scholar API returned HTTP 429 on every attempt (6+ tries, incl. via WebFetch). OpenAlex returned cited_by_count = 0 for the arXiv record, which is unusable (OpenAlex undercounts arXiv-only works; see agents-2025-2026.md). Google Scholar not reachable. Do not cite a number. Indirect evidence of uptake: it is footnoted as ref. 3 in three Anthropic cards (below) and cited by at least arXiv 2606.10525 (search result, approving mention; not opened). |

## 2. Data availability: PARTLY PUBLIC (kit open, most attacks withheld)

- VERIFIED (paper, via HTML page): "We open source the full evaluation kit except for attack strings." A subset of attacks against open-weight models is on HF; the full benchmark is available "upon request." Model-specific attack data went to the respective labs; the full dataset went to UK AISI and US CAISI.
- VERIFIED (repo https://github.com/grayswansecurity/ipi_arena_os, MIT, 62 stars / 14 forks at fetch, 2 commits): Python package `ipi-arena-bench`, 41 behaviors (tool 18, coding 15, browser 8). Attack strings are not in the repo; 95 attacks covering 28 of the 41 behaviors are on HF. The other 13 behaviors have no released attacks; users must supply their own. Running needs an OpenRouter key; browser behaviors need Playwright.
- VERIFIED (HF https://huggingface.co/datasets/sureheremarv/ipi_arena_attacks): 95 rows, MIT, ungated, columns behavior_id / attack. These are attacks generated against Qwen3-VL-235B that succeeded on open models but did not transfer to closed ones, i.e. the least dangerous slice. Owner account is a personal-looking name with "Gray Swan" shown beside it.
- VERIFIED (Gray Swan blog https://www.grayswan.ai/blog/your-ai-agent-can-be-compromised-youd-never-know): UK AISI and US CAISI "receive the full competition dataset, enabling them to run the complete benchmark independently"; labs get attack data for defense training; a held-out portion is kept "to preserve benchmark integrity."
- Consequence: the benchmark labs report on (1,130 or 1,810 curated attacks, see below) is NOT public and cannot be independently re-run by outside academics. The arena/competition itself is hosted by Gray Swan (https://app.grayswan.ai/arena/challenge/...), with Q1 and Q2 2026 challenge pages seen in search results (not opened).

## 3. What it measures

All VERIFIED from the paper HTML unless noted.
- Threat: indirect prompt injection (attacker controls part of an external data source the agent reads). Single-turn attacks only.
- Settings: 41 scenarios ("behaviors") = tool use 18, coding 15, computer use 8 (the repo calls the last "browser").
- Dual objective: an attack counts only if (a) the agent executes the harmful action AND (b) it passes scenario-specific criteria on the final response, always including concealment of the injection and harmful action from the visible response. This concealment requirement is the paper's claimed novelty (Table 1: no prior benchmark covers concealment).
- Scoring: a "tool judge" checks programmatically that the harmful action happened; a "prompt judge" scores the final response 0-10 and the attack passes if all criteria exceed 7. The paper says the threshold "was not empirically tuned on this dataset."
- Competition: 13 frontier models, 464 participants, ~272K attempts (HTML intro also says 240K+), 8,648 successful attacks, $40k prize pool. Wave 0 excluded. Duration is inconsistent inside the paper ("two-week period" in Sec. 3.3 vs "three-week competition" in intro).
- Headline results: all 13 models were vulnerable; ASR 0.5% (Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro); capability and robustness weakly correlated; attacks on robust models transfer to weaker ones; "universal" attack templates (Gray Swan blog: one template worked on 21 of 41 scenarios and 9 models).
- Benchmark set size: paper = 2,679 attacks over 41 behaviors (up to 9 per model-behavior pair; 2,449 for four models without vision). Lab-used curated sets differ: Anthropic cards = 28 scenarios, 1,130 transferable attacks after dedup; OpenAI = 1,810 curated attacks from Q1+Q2 (April) 2026 arenas. The 28-vs-41 and 1,130/1,810/2,679 figures are different subsets/quarters and are NOT reconciled in any source I read. Cite the number with its source.
- Metric used by labs: probability an attacker finds a successful attack within k=1, 10 or 15 attempts.
- Static Table 1 includes an "updates" column: the authors commit to "quarterly updates through continued red teaming competitions."

## 4. Lineage

- Predecessor ART (Gray Swan Arena agent red-teaming; "Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition", arXiv 2507.20526, Zou et al. 2025). Paper cites it as zou2025security and says its findings are in line with ART (VERIFIED, HTML). The ID 2507.20526 itself did not appear in the text I read (UNVERIFIED there; it is taken from agents-2025-2026.md). The Sonnet 5 card (VERIFIED, PDF p.57-58) says ART was developed by Gray Swan "in collaboration with the UK AI Security Institute", is on 19 scenarios, k=1/10/100, and that Claude models "have been near maximum performance on ART for several releases"; IPI replaces it ("Similar to ART, we organized a competition...", "Unlike ART, they also span coding and computer use, not just tool use").
- AgentDojo: paper's Table 1 marks it indirect-injection + tool use, no concealment, no code/computer-use (VERIFIED). AgentHarm: direct misuse, not indirect injection, no concealment (VERIFIED). Both are cited as contrast, not as bases. Note shared authors with AgentHarm: Dziemian, Davies, Winsor, Zou, Fredrikson and Kolter appear on both author lists (compared against the AgentHarm list in agents-2025-2026.md) - the same Gray Swan / CMU / UK AISI circle. That is an institutional lineage observation, not a stated dataset lineage.
- It is a prompt-injection / agent-hijacking benchmark, not a general harmful-content benchmark.

## 5. Adopters: document-by-document

### Anthropic - VERIFIED (PDF text extracted)
- Claude Sonnet 5 System Card (30 Jun 2026), https://www-cdn.anthropic.com/9e6a1044980d8c4ed85669faf9c2a8342e2e9f1e/Claude%20Sonnet%205%20System%20Card.pdf, p.53/57-59. Quote: "we supplemented the ART prompt injection benchmark—which recent Claude models have nearly saturated—with a new Gray Swan indirect prompt injection (IPI) benchmark that spans coding, computer use, and tool use tasks." And: "Going forward, we will report results on a new Indirect Prompt Injection benchmark [fn 3], built in partnership with Gray Swan, the UK AI Security Institute, the US Center for AI Standards and Innovation, and other model developers... 28 different attack scenarios... After deduplication, we selected 1,130 attacks that showed high transferability across target models." Footnote 3 = Dziemian et al., arXiv:2603.15714. Fig 5.2.1.B (Q1 2026) notes Sonnet 4.6 and Gemini 3.1 Pro "are not directly comparable as these were included in the red-teaming competition used to source attacks"; GPT-5.5 and Gemini 3.5 Flash were not, so are "directly comparable evaluations of attack transfer."
- Claude Opus 5 System Card (24 Jul 2026), https://www-cdn.anthropic.com/ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf, p.73-74. Quote: "we have retired the Agent Red Teaming (ART) benchmark and will no longer report it... We now report the Indirect Prompt Injection (IPI) benchmark in its place." Result (p.74): Opus 5 2.0% at k=15 (5.5% for Opus 4.8), 0.2% at k=1; Sonnet 5 5.9%, Mythos 5 2.6%; best non-Claude Muse Spark 16.5%; GPT 5.6 Sol 20.0%, Terra 30.4%, Luna 43.9%; GPT 5.5 20.8%. Same footnote 3. (This also gives the 2.0% figure directly from the PDF; agents-2025-2026.md only had it secondhand.)
- Claude Sonnet 5.5 System Card (28 Sep 2026), https://www-cdn.anthropic.com/870c8f525702625d2c62fc6dd04c857e3250bec1/Claude%20Sonnet%205.5%20System%20Card.pdf, p.49-50. Quote: "We evaluate our models using the Indirect Prompt Injection (IPI) benchmark created by Gray Swan in partnership with the UK AI Security Institute, the US Center for AI Standards and Innovation, and model developers." Figure uses Q1+Q2 2026. Footnote cites arXiv:2603.15714. (Card refers readers to an "Opus 5.5 System Card" for methodology; I did not open that.)
- Anthropic cards also use other Gray Swan products (live bug bounty, Shade) - not the IPI benchmark itself. The Opus 5 card concedes "Claude models have saturated most public benchmarks."
- Claude Opus 4.8 card (28 May 2026) referenced as the first bug-bounty card; not opened (UNVERIFIED).

### OpenAI - VERIFIED (web page, first 100k of 216k chars read)
- GPT-6 Astra prompt-injection page, https://deploymentsafety.openai.com/gpt-6-astra/prompt-injection (3 Sep 2026). Quotes: "We also ran robustness evaluations in collaboration with Gray Swan." "On a benchmark of 1,810 curated attacks from Gray Swan's IPI Arena," Astra's safeguards-enabled checkpoint "showed improved robustness relative to GPT-5.6 Sol." "The estimated attack success rate across 15 attempts per scenario was 8.5%, compared with 27.0% for GPT-5.6 Sol." Fig 5 caption: "Indirect prompt injection robustness on the Gray Swan IPI benchmark... 1,810 curated attacks from the Q1 and Q2 (April) 2026 arenas." The page links the IPI Arena to arXiv. A search summary says OpenAI deprecated its older internal prompt-injection evals as saturated (UNVERIFIED; from https://deploymentsafety.openai.com/gpt-6-astra/capability-threshold-critical search snippet, not opened).
- Note a cross-card inconsistency: Anthropic's Opus 5 card reports GPT 5.6 Sol at 20.0% (k=15) while OpenAI reports 27.0% for GPT-5.6 Sol (different attack set/quarters/settings). Do not compare numbers across cards.
- The GPT-5.6 card (https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf): earlier note found no Gray Swan IPI hits; not rechecked.

### Google - VERIFIED (blog, single sentence)
- "Developing Gemini 4 Argon responsibly and safely", 13 Oct 2026, https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/. Quote (as relayed): "Through built-in adversarial training and real-time security checks, Argon leads in prompt injection robustness on Gray Swan's Indirect Prompt Injection (IPI) benchmark, cutting attack success across 15 adaptive attempts to 0.7%." The only sentence naming the benchmark; no paper link, no comparison table, no method details. It is a blog, not a model card. Aggregators (benchlm.ai, benchmarklist.com) tag the Argon 0.7% as self-reported; their pages are unreliable (see below).
- Gemini 3.7 Flash model card: no external benchmarks (from earlier note, not rechecked).

### NIST CAISI - VERIFIED, but participation, not benchmark scoring
- Blog "Insights from AI agent security large-scale red-teaming competition" (23 Mar 2026), https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition. Quotes (as relayed): "CAISI recently partnered with Gray Swan, the UK AI Security Institute (UK AISI), and several frontier AI labs"; CAISI "contributed to the analysis methodology for this work", will receive the competition data including attack strategies, and plans to use it "to refine future red-teaming competition designs" and "to improve our own AI security measurements going forward." It reports "at least one successful attack was found against all of the target frontier models" and "certain families of 'universal' attacks." It does not name the arXiv ID in the relayed text.
- So CAISI is a co-developer/data recipient, not an independent adopter publishing scores on it. I did not find a CAISI evaluation report that runs the benchmark. CAISI's DeepSeek Sept 2025 evaluation used AgentDojo, not this (see agents-2025-2026.md).

### Others
- Meta: Gray Swan's blog names Meta among collaborating labs ("OpenAI, Anthropic, and Meta"; quote as relayed). A Meta author is on the paper (summary-level). Muse Spark appears as the best non-Claude model on IPI in Anthropic's Opus 5 card (16.5% at k=15), but the Meta Muse Spark report (arXiv 2606.12429) HTML grep for "Gray Swan"/"IPI Arena"/"2603.15714" returned no hits - Meta does not appear to report it itself (grep on the downloaded HTML; not conclusive).
- UK AISI: co-designer per Anthropic cards and Gray Swan blog; receives full dataset. No UK AISI report running it found.
- xAI, Mistral, DeepSeek: nothing found.
- Third-party research: arXiv 2606.10525 cites it approvingly (search summary; not opened). Many 2026 prompt-injection papers surfaced in search (e.g. 2608.28411 LongPIBench, 2604.08499 PIArena) but I did not open them to confirm they cite it.
- Aggregators (UNVERIFIED/unreliable): benchlm.ai/benchmarks/gray-swan-ipi, benchmarklist.com (self-reported scores; a search summary flagged inconsistent model names and a Gray Swan leaderboard page with odd labels).

## 6. Limitations and criticisms

- Authors' own caveats (VERIFIED, paper HTML): threat model "more permissive than typical real-world conditions", so results are "an upper bound on single-turn agent vulnerability"; single-turn only; effort non-uniform and a few participants contributed disproportionately; participants could copy strategies across models, which "may inflate transferability observations"; most models were tested with thinking disabled; judge threshold not tuned. No explicit conflict-of-interest or funding statement found.
- Closed data / reproducibility (VERIFIED facts above): full benchmark by request; only 95 attacks for 28 of 41 behaviors public; outsiders cannot reproduce lab-reported numbers.
- Vendor / evaluator conflict of interest (analysis, not a published critique): Gray Swan builds the benchmark, runs the competitions, sells red-teaming/Shade to labs, and co-authored with the labs whose models are scored; competition was sponsored by UK AISI and frontier labs (paper). Labs report their own model's score on it, and Google's 0.7% is a self-reported blog figure. Anthropic's cards add comparability caveats: models included in the competition that sourced the attacks (Sonnet 4.6, Gemini 3.1 Pro) are "not directly comparable"; Claude is run "without additional safeguards" while other models use public endpoints that may include safeguards.
- Saturation / aging: authors plan quarterly updates because of saturation; Opus 5 at 2.0% (k=15) and Gemini 4 Argon at 0.7% suggest it is approaching the floor for the best models. Anthropic's own Sonnet 5 card argues fixed attack sets "can provide a false sense of security" (citing Nasr et al., arXiv 2510.09023, "The attacker moves second") and pairs IPI with adaptive evaluations (bug bounty, Shade). Because the lab benchmark is a fixed, transfer-selected attack set, it is a static benchmark in that sense.
- Construct validity: dual objective (action + concealment) is judged by a prompt judge (LLM) with an untuned threshold; coding scenarios "used authentic agent transcripts, which may resemble safety training data" and the capability-vs-robustness correlation was "weak and not statistically significant (r = -0.31, p = 0.3)" - both per Ilya Kabanov's post (below), relaying paper content. Mismatched scenario counts across sources (41 / 28) and attack counts (2,679 / 1,130 / 1,810).
- Independent critique: none found. The 2026 validity audit arXiv 2607.28685 covers R-Judge, InjecAgent, AgentHarm and AgentDojo only, not IPI Arena. A search specifically for criticism of the paper returned no critical analysis.

## 7. Discussion by researchers / blogs

- VERIFIED: Ilya Kabanov, The Weather Report, 23 Mar 2026, https://theweatherreport.ai/posts/ipi-arena-benchmark/ - a summary with a "My take" section (concealment should be part of safety evals; test the strongest model first; safety is a design choice). Independent blogger of unknown standing; not a reputable-researcher endorsement.
- VERIFIED: Gray Swan's own blog (vendor) and NIST CAISI blog (government).
- Secondary news: cybersecuritynews.com (10 Aug 2026) on Opus 5 numbers, taken from the system card.
- Not found: Simon Willison, Carlini, Invariant Labs, or academic-blog commentary specific to this paper (unsearched or unfound, not absent).

## 8. Assessment for the survey

- Strong on adoption: three consecutive Anthropic cards (Sonnet 5, Opus 5, Sonnet 5.5) replaced ART with it and footnote the paper; OpenAI's GPT-6 Astra page reports a headline number; Google's Gemini 4 Argon blog reports one (today's date, 13 Oct 2026); CAISI and UK AISI co-developed it. This is the best-documented 2026 lab adoption found.
- Weak on academic validation: arXiv-only, no venue, no citation count retrievable, no independent critique, partly closed data, and the evaluator is also the benchmark vendor. Recommended phrasing: "adopted de facto by frontier-lab system cards in 2026; not peer-reviewed; benchmark data largely withheld."
- Caveat on the claim "cited by Google": it is a single sentence in a launch blog, not a model card or paper. Caveat on "cited by NIST CAISI": CAISI is a partner/data recipient, no CAISI-run scores found.

## Open items
- Citation count (Semantic Scholar 429; retry later with API key). Google Scholar.
- Full GPT-6 Astra page beyond 100k chars and the Astra PDF; Opus 4.8 and "Opus 5.5" cards; Gemini 4 Argon model card (if any); xAI.
- Whether arXiv 2606.10525 and other citing papers actually cite it in the way search summaries claim.
- Full author affiliations; a published peer-reviewed version (comments say a newer arXiv version with Q1 results is in progress).
