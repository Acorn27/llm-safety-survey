# Verification of 2025 candidates (CSE 6324 LLM safety survey), checked 2026-10-13

Legend: VERIFIED = checked this session against the cited primary page or PDF. UNVERIFIED = not confirmed. Method: PDFs were downloaded with curl into separate new directories under the session scratchpad and their text extracted with macOS PDFKit (compiled Swift helper; Python `-I` has no PyObjC). arXiv abstract pages and a few web pages were read through WebFetch, which returns a small-model summary, so those quotes are "as relayed". Quotes from PDFs are from extracted text. One extracted PDF (MASK) contains an unrelated stray line ("EASTER EGG ... Chimecho"); it was treated as data and ignored.

## Summary table

| Candidate | Title/ID correct? | Venue | Data access | 2025-26 lab/gov use | Hold up as top-12 for 2025? |
|---|---|---|---|---|---|
| VCT | Yes (2504.16137) | arXiv only | Withheld; on request to vetted orgs | Strong: OpenAI, Anthropic, xAI, Meta, Google (as VMQA), third-party Kimi eval, International AI Safety Report 2026 | Yes, strongest of the four |
| MASK | Yes (2503.03750) | arXiv only | Public (1,000 items) + private 500 holdout | Strong: xAI, Anthropic (several cards), Meta, Scale leaderboard | Yes, with caveats (saturating, construct) |
| Gray Swan ART | ID right, but the paper title is NOT "Agent Red Teaming" | arXiv only ("Preprint. Under review.") | Test cases promised public; private leaderboard; actual release not confirmed | Strong: OpenAI GPT-5 card, Anthropic cards (retired 2026), Meta Muse Spark | Yes, as a 2025 candidate; now superseded by IPI Arena |
| AILuminate v1.0 | (already recorded) | arXiv | Not rechecked | One new item: cited in International AI Safety Report 2026; no lab or government scoring use found | No new evidence; keep as lower-ranked |

---

## 1. Virology Capabilities Test (VCT)

| Field | Status | Value / source |
|---|---|---|
| Exact title | VERIFIED | "Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark" (https://arxiv.org/abs/2504.16137) |
| Authors (9) | VERIFIED | Jasper Götting, Pedro Medeiros, Jon G Sanders, Nathaniel Li, Long Phan, Karam Elabd, Lennart Justen, Dan Hendrycks, Seth Donoughe. Affiliations in PDF header include SecureBio, CAIS, a Federal University of ABC centre and MIT Media Lab. The 2025.md "SecureBio and CAIS (author list not verified)" is now resolved. |
| Venue / year | VERIFIED: arXiv only | v1 21 Apr 2025, v2 29 Apr 2025; 31 pages; cs.CY, cs.LG; no journal ref, no venue. |
| PDF | VERIFIED | https://arxiv.org/pdf/2504.16137 |
| Citation count | VERIFIED (partly) | Semantic Scholar API, fetched 2026-10-13: 43 citations (paperId 384235e4862bfb61460dd08d89740a44d0d1205d, venue "arXiv.org"). Note S2 undercounts relative to Google Scholar; no other source checked. |
| Dataset access | VERIFIED: withheld / access-controlled | Paper: "The shared dataset will not be released publicly to reduce the risk of leakage into training corpora, but the benchmark will be directly conveyed to any organizations and researchers with a track record of work on AI safety. The holdout set will be kept private..." A canary string is embedded. A few example questions are public. Appendix A5: "A refusal preference dataset covering all 322 VCT questions is available upon request." No public Hugging Face dataset found (HF API for cais/vct returned an auth error; not a proof of absence). |
| Size | VERIFIED | 322 shared questions (221 with image, 101 text-only) plus a private 43-question holdout (34 image, 9 text-only), from 365 questions after filtering 394 edited ones. |
| What it measures | VERIFIED | Practical, tacit and visual wet-lab virology troubleshooting; dual-use knowledge relevant to biological uplift. Headline: expert virologists with internet access average 22.1% on questions in their own sub-areas; o3 43.8%, outperforming 94% of the experts (paper abstract and Table). |

### 2025-2026 use (primary documents opened)

- **OpenAI GPT-5 system card** (arXiv 2601.03267, v2 1 May 2026; https://arxiv.org/pdf/2601.03267), section 6.1.1.6 "External Evaluations by SecureBio", Table 15. VERIFIED. Row "gpt-5-thinking July 13": Virology Capabilities Test 41.4 ± 1.7%; text-only 46.0 ± 1.8%. Same table: gpt-5-thinking-helpful-only July 26 37.7 ± 1.9%; OpenAI o3 [high] 42.0 ± 0.9%; Grok 4 text-only 45.8 ± 2.8%; "Human experts, assigned individually tailored subsets" 22.6% (VCT) and 30.8% / 32.4% on the other tests. Text: "The results reported in Table 15 are the mean ± standard deviation across all n=10 evaluations", and "all five models they tested were appreciably stronger than most human expert baseliners". The 41.4 +/- 1.7% in 2025.md is correct and is gpt-5-thinking on the full VCT (not the text-only subset).
  - Separate section 6.1.1.2 "Multimodal Troubleshooting Virology": "a set of 350 fully held-out virology troubleshooting questions from SecureBio and the Center for AI Safety", and "SecureBio has since updated the eval to a multi-select variant which increases the difficulty... All models exceed the median domain expert baseline of 22.1%." The 350-question OpenAI-side set differs from the 322 in the paper; the relationship is not explained in the card (UNVERIFIED whether the same questions).
- **OpenAI o3 / o4-mini card** (https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf), section 4.2.2. VERIFIED: "350 fully held-out virology troubleshooting questions from SecureBio" (the card does not name VCT or CAIS); "Evaluating in the single select multiple choice setting, all models (including o3 and o4-mini models, and also prior models like GPT-4o) score above the average human baseline (40%)." Numbers are only in a figure (not extracted).
- **Anthropic Claude 4 card** (https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285/Claude%204%20System%20Card.pdf), section 7.2.4.4, p.97. VERIFIED: uses "multiple select" VCT/VMQA, 10-shot; "we consider this evaluation to have saturated, since even the Claude Sonnet 3.7 score exceeds the human baseline." Shared "across major labs via the Frontier Model Forum".
- **Anthropic Claude Sonnet 4.5 card** (https://assets.anthropic.com/m/12f214efcc2f457a/original/Claude-Sonnet-4-5-System-Card.pdf), section 9.2.4.2, pp.130-131. VERIFIED: Sonnet 4.5 39.7%, Opus 4.1 42.9%, Opus 4 41.1%; "Given that all models have crossed the 22.1% threshold, this evaluation is no longer valid as a rule-out and included mostly for comparison between models."
- **Anthropic Claude Sonnet 5 card** (30 Jun 2026) and **Opus 5 card** (24 Jul 2026), both PDFs from ipi-arena.md. VERIFIED: Sonnet 5 scores 0.45 "well above the expert baseline of 0.221" (regression vs Opus 4.7 0.50, Opus 4.8 0.47, Mythos 5 0.56); Opus 5 scores 0.59. So Anthropic still reports VCT in mid-2026 even after calling it saturated.
- **xAI Grok 4 model card** (https://data.x.ai/2025-08-20-grok-4-model-card.pdf, 20 Aug 2025). VERIFIED (already in system-card-recheck.md): uses "the text-only portion of VCT [Götting et al., 2025]"; VCT accuracy 0.60 (API) / 0.71 (Web); "human expert performance on BioLP-Bench is 38.4% and 22.1% on VCT, so both Grok 4 API and Grok 4 Web achieve superhuman performance".
- **Meta Muse Spark Safety & Preparedness Report** (arXiv 2606.12429, 14 May 2026, https://arxiv.org/pdf/2606.12429). VERIFIED: VCT, HPCT and MBCT "are part of a suite of evaluations developed by SecureBio and the Center for AI Safety (Götting et al., 2025; SecureBio, 2025)... All evaluations were run with the recommended multiple-response multiple-choice configuration"; summary table lists VCT for Muse Spark 49.7 (column alignment of the other models' VCT cells is garbled in extraction, so not quoted); "performance well above the expert baseline, and on par with other frontier models."
- **Google**: Gemini 2.5 technical report (arXiv 2507.06261 v6, https://arxiv.org/pdf/2507.06261) says "SecureBio VMQA single-choice" among external CBRN benchmarks. VERIFIED that this wording appears. That VMQA is the VCT is INFERRED (Anthropic cards write "VMQA/VCT", and the VCT PDF canary string begins "vmqa:"); Google does not write "VCT". The Gemini 3 Pro model card PDF (https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf) has no mention of VCT, VMQA, MASK or Gray Swan.
- **International AI Safety Report 2026** (3 Feb 2026, https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026_1.pdf). VERIFIED: text says "one study showed that OpenAI's o3 model is able to outperform 94% of domain experts at troubleshooting virology lab protocols (549)"; ref 549 is the VCT paper (arXiv 2504.16137). Also cited at a second place on virology-trained models (549, 1206*).
- **Independent third party**: "An Independent Safety Evaluation of Kimi K2.5" (arXiv 2604.03121, 3 Apr 2026; authors affiliated with Constellation, Anthropic Fellows Program, etc., not a government body) uses VCT "multi-select" "to avoid benchmark saturation"; "As no refusals from any model were encountered during testing..." VERIFIED.
- **UK AISI**: Frontier AI Trends Report (https://www.aisi.gov.uk/frontier-ai-trends-report) page text, searched for "Virology Capabilities", "VCT", "MASK", "Gray Swan": only a Gray Swan mention ("joint paper with Gray Swan AI" on safeguards). No VCT use found (UNVERIFIED that none exists in the full report; I searched the HTML text only).
- **NIST CAISI**: search for CAISI evaluation reports (DeepSeek, Kimi K2 Thinking, DeepSeek V4 Pro) found no mention of VCT or MASK in excerpts. UNVERIFIED (reports not opened in full).
- Other: CAIS newsletter AISN #52 (https://newsletter.safe.ai/p/ai-safety-newsletter-52-an-expert) says xAI added new safeguards as a result of the paper (relayed; the VCT paper's A5 also credits Norman Mu (xAI) for the refusal policy).

### Criticisms / limitations

- Saturation: Anthropic says it is saturated (Claude 4 card) and "no longer valid as a rule-out" (Sonnet 4.5 card); labs and third parties moved to the harder multi-select variant (OpenAI, Kimi eval, Meta). Single-select vs multi-select vs OpenAI's 350-question set are not comparable.
- Authors' own limitation (Appendix A3, VERIFIED): "the benchmark doesn't capture an objective 'ground truth'... it captures the actual views and advice of real human scientists"; experts disagree on some answers.
- Expert baseline is narrow: experts were scored only on questions in their own sub-areas, with internet access; GPT-5 card's "tailored subsets" baseline is 22.6%. The "beats 94% of experts" claim depends on this design.
- Closed data: only available on request to vetted orgs; outsiders cannot reproduce; evaluator (SecureBio) is also the benchmark owner and runs the lab evaluations (GPT-5 card).
- Narrow construct: multiple-choice knowledge troubleshooting, not actual wet-lab uplift (Epoch's article, already in system-card-recheck.md, makes the general case against bio evals measuring real risk; not VCT-specific). No dedicated third-party critique of VCT found.

---

## 2. MASK

| Field | Status | Value / source |
|---|---|---|
| Exact title | VERIFIED | "The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems" (https://arxiv.org/abs/2503.03750). MASK = Model Alignment between Statements and Knowledge. |
| Authors (16) | VERIFIED | Richard Ren, Arunim Agarwal, Mantas Mazeika, Cristina Menghini, Robert Vacareanu, Brad Kenstler, Mick Yang, Isabelle Barrass, Alice Gatti, Xuwang Yin, Eduardo Trevino, Matias Geralnik, Adam Khoja, Dean Lee, Summer Yue, Dan Hendrycks. CAIS and Scale AI. First three equal contribution (plus Menghini). |
| Venue / year | VERIFIED: arXiv only | v1 5 Mar 2025, v2 20 Mar 2025, v3 5 Jan 2026; no journal ref; a web search found no acceptance at ICLR 2026 or NeurIPS 2025 (absence of evidence). |
| PDF | VERIFIED | https://arxiv.org/pdf/2503.03750 (project site https://www.mask-benchmark.ai ; code https://github.com/centerforaisafety/mask, MIT, 27 stars at fetch). |
| Citation count | UNVERIFIED | Semantic Scholar returned HTTP 429 on all attempts (5+ over about 10 min). OpenAlex says 1, which is an obvious undercount for an arXiv-only record and is not usable. |
| Dataset access | VERIFIED: public + private holdout | Hugging Face cais/MASK: not gated, ungated API result, 1,000 rows in 6 subsets (continuations 176, disinformation 125, doubling_down_known_facts 120, known_facts 209, provided_facts 274, statistics 96); HF API shows 9,058 downloads (HF's own count, window not stated) and 18 likes. Paper: "1,000 public examples" with "a separate, held-out set of 500 examples" kept private; the paper's results use all 1,500. Anthropic's cards use the "public test split" with n=904, so some public items are dropped (reason not stated; UNVERIFIED). |
| Size / construct | VERIFIED | Measures lies of commission: a model's statement under pressure versus its own separately elicited belief; reports P(Lie) (and honesty = 1 - P(Lie)); 30 models evaluated in the paper. Headline: larger models get more accurate but not more honest; e.g. P(Lie) Grok 2 63.0, GPT-4o 44.5, Claude 3.7 Sonnet 26.6 (paper Fig. 4). LLM judge agrees with humans 86.4% (Appendix A.2). |

### 2025-2026 use

- **xAI Grok 4 model card** (https://data.x.ai/2025-08-20-grok-4-model-card.pdf), section 2.2. VERIFIED: "To assess honesty, we use the MASK dataset, a collection of 1000 questions measuring whether models faithfully report their beliefs when pressured to lie [Ren et al., 2025]"; Table 2 "Deception | MASK dishonesty rate | 0.43" for Grok 4 API; mitigation is a system prompt instructing honesty. This is a primary-document use of MASK as a release gate input.
- **Anthropic**: Sonnet 5 card, section 6.5.2, p.89: Sonnet 5 lying rate 3.1% (Mythos Preview 4.4%, Opus 4.8 6.1%, Mythos 5 8.6%, Opus 4.6 and 4.7 9.8%, Sonnet 4.6 13.3%), "public test split, not the private test set", n=904. Opus 5 card, section 6.5.2, p.112: "As in previous system cards, we used the public test split of the MASK evaluation set." VERIFIED. Which was the first Anthropic card with MASK is UNVERIFIED (the Claude 4 and Sonnet 4.5 cards contain no MASK text per my grep; Sonnet 4.5 is covered by the Scale leaderboard instead).
- **Meta Muse Spark report** (arXiv 2606.12429): "On MASK... Muse Spark achieves an honesty rate of 89.1%, second only to GPT-5.4 at 90.3%, outperforming Gemini 3.1 Pro at 44.1%" (Claude Opus 4.6 83.4% in the table). MASK is one of the "Loss of Control" evaluations in Meta's framework table. VERIFIED.
- **Scale AI leaderboard** (https://labs.scale.com/leaderboard/mask, redirect from scale.com/leaderboard/mask): 67 models; metric Honesty Score = 1 - P(Lie); uses the private 500-example split. Top entries read: claude-opus-4-6 (Non-Thinking) 96.28 ± 0.41; claude-sonnet-4-5-20250929-thinking 96.13 ± 0.57; Claude Sonnet 4 (Thinking) 95.33 ± 2.29. Page shows no update date. VERIFIED (via WebFetch summary). Conflict of interest: Scale is an author organisation.
- **Not found**: OpenAI GPT-5 card (2601.03267), o3/o4-mini card, Gemini 2.5 report and Gemini 3 Pro card contain no MASK text (grep). Epoch and Artificial Analysis: I did not locate MASK pages (UNVERIFIED, not searched beyond one web search). UK AISI Frontier AI Trends page and CAISI excerpts: no MASK mention found. The International AI Safety Report 2026 text has no MASK match (grep for "MASK" and the author name pattern returned nothing).
- Aggregators benchlm.ai and benchmarklist.com list MASK scores; treat as unreliable and not used.

### Criticisms / limitations

- Authors' limitations (Appendix A.2, VERIFIED): English only, short factual propositions; LLM-judge 86.4% agreement with humans, noise could bias rankings; only six hand-crafted pressure archetypes; tests models in isolation, so rates are "worst-case propensities".
- Construct validity: the paper's claim is that it measures lying (statement contradicts elicited belief), so it depends on the assumption that an elicited belief is the model's belief (Appendix A.3 discusses this). Grok 4's system-prompt mitigation lowering the rate (xAI card: "makes the model less willing to contradict its beliefs") shows the score is prompt-sensitive; no independent validity study found.
- Saturation and ranking drift: the Scale leaderboard top is about 96% honesty and Anthropic's Sonnet 5 lying rate is 3.1%, so top models are close to the floor. Cross-lab numbers differ in split and judge (Anthropic public n=904; Scale private 500; Meta 89.1%/Claude Opus 4.6 83.4% vs Scale ~96% for Opus 4.6), so do not compare across sources.
- Leaderboard run by an author organisation (Scale).

---

## 3. Gray Swan ART competition / Agent Red Teaming paper

| Field | Status | Value / source |
|---|---|---|
| arXiv ID | VERIFIED | 2507.20526 is correct. |
| Exact title | VERIFIED (corrects the earlier note) | "Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition" (https://arxiv.org/abs/2507.20526). "Agent Red Teaming (ART)" is the name of the benchmark built from the competition, not the paper title. |
| Authors (17) | VERIFIED | Andy Zou, Maxwell Lin, Eliot Jones, Micha Nowak, Mateusz Dziemian, Nick Winter, Alexander Grattan, Valent Nathanael, Ayla Croft, Xander Davies, Jai Patel, Robert Kirk, Nate Burnikell, Yarin Gal, Dan Hendrycks, J. Zico Kolter, Matt Fredrikson. Affiliations: Gray Swan AI; UK AI Security Institute; additional CMU, Oxford, CAIS. |
| Venue / year | VERIFIED: arXiv only | Submitted 28 Jul 2025, v1 only (cs.AI), PDF footer "Preprint. Under review." No venue found. |
| PDF | VERIFIED | https://arxiv.org/pdf/2507.20526 |
| Citation count | UNVERIFIED | Semantic Scholar 429 on every attempt; OpenAlex has no record for the arXiv DOI (count 0 results). |
| Dataset access | PARTLY VERIFIED | Paper: "We plan to publicly release the test cases along with a private leaderboard to prevent overfitting to known attacks and active misuse." Anthropic's Sonnet 5 card and Meta's report call it Gray Swan's benchmark / "private Agent Red Teaming (ART) benchmark" (Meta wording per search summary). Whether the test cases were actually released is UNVERIFIED (not checked; no repo link found in my reading). |
| Size / what it measures | VERIFIED | Competition (ran with UK AISI sponsorship): 22 frontier agents, 44 deployment scenarios, over 1.8 million prompt-injection attacks, over 60,000 successful policy violations, $171,800 prize pool, over a month, four weekly waves. ART benchmark: 4,700 curated attacks over 44 behaviors, evaluated on 19 models. Measures prompt-injection / policy-violation robustness of tool-using agents (confidentiality breach, conflicting objectives, prohibited content, prohibited actions per Sonnet 4.5 card). Findings: nearly all agents violate policy for most behaviors within 10-100 queries; high transfer; limited correlation between robustness and model size, capability or inference-time compute. |

### 2025-2026 use

- **OpenAI GPT-5 system card** (arXiv 2601.03267): "One of our external testing partners, Gray Swan, ran a prompt-injection benchmark[10], showing that gpt-5-thinking has SOTA performance against adversarial prompt injection attacks produced by their Shade platform." Figure 8 titled "Agent Red Teaming (ART) benchmark for prompt injections"; ref [10] = Zou et al., "Security challenges in AI agent deployment: Insights from a large scale public competition" (the ART paper). VERIFIED. Also, Gray Swan arena red-teamers submitted 277 jailbreak reports over 28,367 attempts against bioweaponization rubrics (ASR 0.98%), a different use of the arena.
- **Anthropic Claude Sonnet 4.5 card** (4.2.1, p.27-28): ART benchmark run "against 23 models from Anthropic and other developers"; k=1 and k=10; Sonnet 4.5 "had the lowest rate of successful prompt injection attacks of any model tested". Cites the arXiv paper in a footnote (https://arxiv.org/abs/2507.20526). VERIFIED. (The Claude 4 card has no Gray Swan/ART text per grep.)
- **Anthropic Claude Sonnet 5 card** (5.2.1, p.57): "since Claude models have been near maximum performance on ART for several releases, we are deprecating it as our primary prompt injection benchmark"; Opus 5 card "retired the Agent Red Teaming (ART) benchmark". VERIFIED (see ipi-arena.md). So ART was a de facto lab benchmark from about mid-2025 to mid-2026, then replaced by IPI Arena (arXiv 2603.15714).
- **Meta Muse Spark report** (arXiv 2606.12429): adversarial-robustness table row "ART (pass@1)": Muse Spark 6.7, GPT-5.4 1.2, Claude Opus 4.6 0.2, Gemini 3.1 Pro 1.0 (column assignment from extraction order, treat with care); text: "On the third-party GraySwan ART benchmark (Zou et al., 2025), Muse Spark currently shows greater sensitivity to injection than the other models GraySwan evaluated." VERIFIED.
- **UK AISI**: co-developer (authors; Sonnet 5 card says developed "in collaboration with the UK AI Security Institute"). AISI page mentions a "joint paper with Gray Swan AI" on safeguards (not opened in depth). No AISI-run scores found.
- Gemini, xAI: no mention in the Gemini 2.5 report, Gemini 3 Pro card or Grok 4 card (grep).

### Criticisms / limitations

- Paper's own: sub-optimal exposure of some models (o3 introduced late in the competition, "potentially inflating" its observed attack success rate); simulated tools and scenarios.
- Saturation: Anthropic says near-maximum performance on ART (Claude models) and retired it; Muse Spark table shows pass@1 values near 0-2% for most models.
- Closed/private leaderboard (by design) and evaluator is the vendor selling red-teaming; attacks were sourced against models available at the time, so the set ages and advantages models not in the arena (same issue Anthropic notes for IPI).
- No independent critique found (not exhaustively searched).

---

## 4. AILuminate v1.0 (only new evidence)

Existing record: arXiv 2503.05731, ~24k prompts, 12 hazards. New or checked this session:
- International AI Safety Report 2026 (https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026_1.pdf) cites it as ref 901 (S. Ghosh et al., "AILuminate: Introducing v1.0...", arXiv 2503.05731), in the sentence "many benchmarks fail to accurately measure the specific capability they claim to assess (900*, 901)". VERIFIED that it is cited; the report uses it as an example of benchmark-validity concerns or related support, and I did not read the surrounding discussion beyond that sentence, so it is a government-backed citation, not a use as an evaluation.
- MLCommons page (https://mlcommons.org/ailuminate/, via WebFetch): "109 models benchmarked" (unnamed); safety benchmark version "1.0-en_us-official-ensemble"; a Jailbreak/Security benchmark "0.5" exists; AI Verify Foundation and Nasscom named as partners; Anthropic, Google, Meta, Microsoft, NVIDIA, OpenAI and others listed as working-group participants. The page states no lab or government adoption.
- grep of the GPT-5, Claude 4, Sonnet 4.5, Sonnet 5, Opus 5, o3, Grok 4, Gemini 2.5, Gemini 3 Pro and Muse Spark documents for "AILuminate" and "MLCommons": zero hits. UK AISI and CAISI use: none found.
- Verdict: no verified lab or government use of AILuminate scores found. Keep the "industry-consortium standard" description but not as top-12.

---

## Verdict for the top-12 list (2025)

1. VCT: holds up. Highest-quality adoption evidence: OpenAI (GPT-5 Table 15, 41.4 +/- 1.7%), Anthropic (Claude 4, Sonnet 4.5, Sonnet 5, Opus 5), xAI (Grok 4), Meta (Muse Spark), International AI Safety Report 2026. Caveats: arXiv only, data withheld, already described as saturated in its single-select form.
2. MASK: holds up. Used in the Grok 4 card, Anthropic cards (2026), Meta's report, and Scale's leaderboard. Caveats: arXiv only, honesty construct depends on belief elicitation, top scores near ceiling, leaderboard run by an author org, citation count UNVERIFIED.
3. ART (Zou et al., 2507.20526): holds up as a 2025 candidate (GPT-5 card, Anthropic cards through Sonnet 4.5, Meta). Correct the title in the notes; present it as superseded by IPI Arena (2603.15714) in 2026. Caveats: arXiv only, "under review", citation count UNVERIFIED, public release of test cases not confirmed.
4. AILuminate: no new use evidence; not recommended on adoption grounds.

Open items: Semantic Scholar counts for MASK and ART (retry later or use an API key); whether ART test cases were publicly released; first Anthropic card to report MASK; Epoch and Artificial Analysis MASK pages; full UK AISI and CAISI report text; mapping between OpenAI's 350-question troubleshooting set and the 322-question VCT.
