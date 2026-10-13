# System-card recheck (CSE 6324 LLM safety survey)

Checked 2026-10-13. Method: PDFs downloaded with curl into separate empty directories and text extracted with macOS PDFKit (no poppler/mutool installed). Statuses: CONFIRMED / CONTRADICTED / STILL UNREADABLE. Quotes are from extracted text; table cells were read in row order. Page numbers are the printed page numbers where I could see them.

## Claims from 2024.md and early-2020-2022.md tagged (snippet) or UNVERIFIED about lab adoption

1. Claude Opus 4 / Sonnet 4 card has a StrongREJECT section; figures conflicted between secondary sources. (2024.md section 4)
2. OpenAI o1 card uses StrongREJECT with goodness@0.1 (snippet).
3. OpenAI GPT-5 family (GPT-5-Codex addendum, GPT-5 Instant addendum, GPT-5 main card) use StrongReject (snippet); values 0.992-0.997 from search summaries only.
4. GPT-5.5 page: StrongReject-based benchmark replaced by a multiturn jailbreak eval (marked VERIFIED, rechecked for exact quote).
5. xAI Grok 4 card reports WMDP (API Bio 0.87, Chem 0.83, Cyber 0.79) (snippet). Later xAI cards (Grok 4.1, 4.5, 4.7) (snippet).
6. Gemini 2.5 Pro card uses WMDP (only via Epoch; card not opened).
7. GPT-4 technical report 0.73% RealToxicityPrompts (snippet, early-2020-2022.md) and its TruthfulQA claim (unreadable).
8. Llama 2 uses TruthfulQA and ToxiGen (figures from ar5iv).
9. StrongREJECT prompt count 313 (secondary) vs 324 (Inspect Evals).
10. Sonnet 4.5 card calls single-turn sets saturated (snippet); Grok 4.1/4.5/4.7 WMDP; Cisco/DeepSeek HarmBench; AgentHarm on Princeton HAL (from the task brief).
Not rechecked here: item 10 except AgentHarm/HAL; GPT-5 Instant "sensitive conversations" addendum (27 Oct 2025); the "A Safety Report on GPT-5.2..." paper; Grok 4.1 and later xAI cards.

---

## (a) Anthropic Claude 4 system card: StrongREJECT. CONFIRMED (figures now read)

- URL: https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285/Claude%204%20System%20Card.pdf
- Section 2.7 "StrongREJECT for jailbreak resistance", printed pp. 18-19.
- Quote: "We ran the StrongREJECT evaluation, a benchmark (Souly et al 2024) for evaluating the model's robustness against jailbreaks. ... StrongREJECT was intentionally run without ASL-3 protections and was not specifically focused on jailbreaks around potentially dangerous CBRN information."
- Quote: "In this evaluation, an 'attacker' model (in this case, a version of Claude Sonnet 3.5 (new) without safety training) was used to generate jailbreaks for a series of prompts using various jailbreak techniques. We report the 'Best Score,' which is the percentage of cases where at least one jailbreak succeeded for a given prompt, as well as the 'Top 3 Average Score' which shows the averaged jailbreak success rate for the top 3 jailbreak techniques per prompt."
- Table 2.7.A (lower is better). Columns: Best score standard thinking / Top-3 average standard / Best score extended thinking / Top-3 average extended:
  - Claude Opus 4: 18.21% / 7.14% / 2.24% / 1.17%
  - Claude Sonnet 4: 6.71% / 2.66% / 2.24% / 1.38%
  - Claude Sonnet 3.7: 31.95% / 8.09% / 10.22% / 4.05%
- Resolves the conflict in 2024.md: both secondary sources were partly right, because the numbers come from different columns. 31.95% is Sonnet 3.7 best score (standard thinking) and 10.22% is Sonnet 3.7 best score (extended thinking). 18.21% is Opus 4 best score (standard). 2.24% is the best score with extended thinking for BOTH Opus 4 and Sonnet 4. The "31.95% to 18.21% to 2.24%" chain is a cross-model comparison, not one model's trajectory.
- Caveat: the PDF's table was extracted as plain text; the column order is inferred from the header order. The row values follow the card's text order.
- Not rechecked: the Sonnet 4.5 card "saturated" claim (https://www.anthropic.com/claude-sonnet-4-5-system-card). Status stays (snippet).

## (b) OpenAI cards

**o1 system card. CONFIRMED.** https://cdn.openai.com/o1-system-card-20241205.pdf, section 4.1.2 "Jailbreak Evaluations" and Table 23 (printed p. 45).
- "StrongReject [16]: An academic jailbreak benchmark that tests a model's resistance against common attacks from the literature. Following [16], we calculate goodness@0.1, which is the safety of the model when evaluated against the top 10% of jailbreak techniques per prompt."
- "We find that the o1 family significantly improves upon GPT-4o, especially on the challenging StrongReject evaluation."
- Table 23 row: "StrongReject [16] goodness@0.1 0.22 0.66 0.72 0.83" for columns GPT-4o, o1-preview, o1, o1-mini.
- It is one of four jailbreak evals (with Production jailbreaks, Jailbreak augmented examples, Human sourced jailbreaks). Same card also says "We also ran contextual evaluations not included here, including on GPQA biology, WMDP biology..." (so o1 mentions WMDP, but only as unreported contextual evals).

**GPT-5-Codex addendum (15 Sep 2025). CONFIRMED.** https://cdn.openai.com/pdf/97cc5669-7a25-4e63-b15f-5fd5bdc4d149/gpt-5-codex-system-card.pdf, section 1.2 Jailbreaks, Table 2.
- "We evaluate the model using StrongReject [1], an academic jailbreak benchmark."
- Rows (gpt-5-codex / gpt-5-thinking / OpenAI o3): illicit/non-violent-crime prompts 0.992 / 0.995 / 0.985; violence prompts 0.997 / 0.999 / 0.992; abuse/disinformation/hate prompts 0.993 / 0.999 / 0.995; sexual-content prompts 0.995 / 0.995 / 0.991. The earlier "0.992-0.997 for gpt-5-codex" is correct (range across rows is 0.992-0.997).

**GPT-5 system card (main). CONFIRMED.** arXiv 2601.03267 ("OpenAI GPT-5 System Card", v1 19 Dec 2025, v2 1 May 2026; https://arxiv.org/abs/2601.03267, PDF https://arxiv.org/pdf/2601.03267). This resolves the "link not checked" note.
- Section 3.4 Jailbreaks: "StrongReject [1]: inserts a known jailbreak into an example from the above safety refusal eval. We then run it through the same policy graders we use for disallowed content checks."
- Table 25 (gpt-5-thinking-mini / gpt-5-thinking-nano / OpenAI o4-mini / gpt-5-main-mini): illicit/non-violent-crime 0.994 / 0.997 / 0.968 / 0.940; violence 0.996 / 0.996 / 0.972 / 0.949; abuse/disinformation/hate 0.973 / 0.997 / 0.973 / 0.971; sexual-content 0.994 / 0.996 / 0.970 / 0.953.
- Note the metric here is not_unsafe per policy grader, not the goodness@0.1 used in the o1 card. Do not compare across cards.

**GPT-5.5 "replaced" sentence. CONFIRMED (exact quote).** https://deploymentsafety.openai.com/gpt-5-5, section "4. Robustness Evaluations", "4.1 Jailbreaks". StrongReject appears once on the page.
- "Ahead of the GPT-5.4 launch, we replaced our previous StrongReject-based benchmark with a more challenging multiturn jailbreak evaluation derived from red-teaming exercises."
- Next sentence: "The updated evaluation tests models on realistic scenarios using sophisticated attacker strategies that can probe, adapt, and escalate over the course of a conversation."
- Correction: the jailbreak section does NOT use the word "saturated". The word appears elsewhere on the page in section 3.1.1 about disallowed-content evals: "our earlier Standard evaluations for these categories had become relatively saturated." Do not attribute saturation to the StrongReject replacement from this page. (Quotes via WebFetch's summarizer, which returned them verbatim in short segments; re-read the page before final citation.) The 2024.md "Corrections" 10 and the "saturation" gloss in section 4 are therefore an inference, not a statement on the page. The GPT-5.2 "filtered to remove saturated examples" claim was not re-opened.
- Not rechecked: GPT-5.2 page (https://deploymentsafety.openai.com/gpt-5-2) and the GPT-5 Instant addendum.

## (c) xAI Grok 4 model card: WMDP. CONFIRMED

- URL: https://data.x.ai/2025-08-20-grok-4-model-card.pdf. Header says "Last updated: August 20, 2025". Section 2.3.1/2.3.2, Table 3.
- "To measure dual-use weapons development capabilities, we assess performance on WMDP [Li et al., 2024], the text-only portion of VCT [Götting et al., 2025], and BioLP-Bench [Ivanov, 2024]."
- Table 3 "Dual-use capabilities evaluations" (Grok 4 API / Grok 4 Web): "WMDP Bio accuracy 0.87 0.88"; "Chemistry WMDP Chem accuracy 0.83 0.85"; "Cybersecurity WMDP Cyber accuracy 0.79 -". Also BioLP-Bench 0.47 / 0.44, VCT 0.60 / 0.71, CyBench unguided 0.43, MakeMeSay 0.12.
- The snippet values (API Bio 0.87, Chem 0.83, Cyber 0.79) are exactly right.
- Later xAI cards (Grok 4.1, 4.5, 4.7): NOT rechecked; remain (snippet).

## (d) Gemini 2.5 Pro: WMDP

- Epoch claim. CONFIRMED. https://epoch.ai/gradient-updates/do-the-biorisk-evaluations-of-ai-labs-actually-measure-the-risk-of-developing-bioweapons. Figure 1 caption: "Data on WMDP-Bio were taken from Justen 2025, the Gemini 2.5 Pro Preview Model Card, and Dev et al. 2025" and "Data on WMDP-Chem were taken from Dev et al. 2025 and the Gemini 2.5 Pro Preview Model Card." The article body does not say which labs report WMDP; the caption is the only link. (Caption quotes via WebFetch summarizer.)
- Gemini 2.5 Pro model card PDF itself: STILL UNREADABLE. https://storage.googleapis.com/model-cards/documents/gemini-2.5-pro.pdf returns AccessDenied to anonymous callers (checked by curl); modelcards.withgoogle.com redirects to a listing; https://deepmind.google/models/model-cards/gemini-2-5-pro/ returns 404.
- Closest primary evidence: the Gemini 2.5 technical report, arXiv 2507.06261 v6 (19 Dec 2025), https://arxiv.org/pdf/2507.06261, Frontier Safety, CBRN: "Examples of model performance on three external benchmarks are shown in Figure 9: i) SecureBio VMQA single-choice; ii) FutureHouse LAB-Bench presented as three subsets (ProtocolQA, Cloning Scenarios, SeqQA) (Laurent et al., 2024); and iii) Weapons of Mass Destruction Proxy (WMDP) presented as the biology and chemistry data sets (Li et al., 2024)." Followed by "Results: We observe a general trend of increasing scores, with Gemini 2.5 Pro showing statistically higher scores than the next best previous model for all benchmarks." So Google does use WMDP (Bio, Chem) in the technical report. The model-card claim itself rests on Epoch's caption.

## (e) GPT-4 technical report: 0.73% RealToxicityPrompts. CONFIRMED

- URL: https://arxiv.org/pdf/2303.08774. Main report, printed p. 13 (Section 6 Risks & mitigations): "On the RealToxicityPrompts dataset [73], GPT-4 produces toxic generations only 0.73% of the time, while GPT-3.5 generates toxic content 6.48% of time."
- System Card appendix repeats it (printed p. 62): "On the RealToxicityPrompts dataset, GPT-4 produces toxic generations 0.73% of the time while GPT-3.5..." (the sentence continues past the extracted line; the main-report sentence gives the GPT-3.5 figure).
- TruthfulQA: also CONFIRMED in the same report, Section 6: "GPT-4 makes progress on public benchmarks like TruthfulQA [66], which tests the model's ability to separate fact from an adversarially-selected set of incorrect statements (Figure 7)." It adds "The GPT-4 base model is only slightly better at this task than GPT-3.5; however, after RLHF post-training we observe large improvements over GPT-3.5." The report gives results in Figure 7 (mc1 accuracy), not a number in text that I extracted. Footnote 9: "We did not check the RLHF post-training data for contamination with TruthfulQA."
- This is a 2023 report; it supports GPT-4 adoption only, not 2025-26.

## (f) Llama 2 paper: TruthfulQA / ToxiGen. CONFIRMED

- URL: https://arxiv.org/pdf/2307.09288, Section 4.1 (safety evaluation of pretrained models), Table 11, printed p. 22. Table 14 (fine-tuned models), printed p. 31.
- "We evaluate the safety capabilities of Llama 2 on three popular automatic benchmarks, pertaining to three key dimensions of LM safety." The three are TruthfulQA (truthfulness), ToxiGen (toxicity) and BOLD (bias). The earlier note omitted BOLD.
- Table 11 (TruthfulQA up / ToxiGen down): Llama 2 7B 33.29 / 21.25; 13B 41.86 / 26.10; 34B 43.45 / 21.19; 70B 50.18 / 24.60. Llama 1 65B 48.71 / 21.77. MPT 7B 29.13 / 22.32; Falcon 40B 40.39 / 23.44. The earlier TruthfulQA values in early-2020-2022.md are right.
- Metrics: "For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher, the better). For ToxiGen, we present the percentage of generations that are deemed toxic by the metric (the lower, the better)."
- Table 14 (fine-tuned): ChatGPT 78.46 / 0.20; Llama 2-Chat 7B 57.04 / 0.00; 13B 62.18 / 0.00; 34B 67.20 / 0.02; 70B 64.14 / 0.01. So Llama 2-Chat is ~0% on ToxiGen, which supports the saturation observation (now VERIFIED from the paper, not from a mirrored table). Paper's own claim: "Llama 2 does not outperform other models on toxicity metrics" for base models.
- Appendix A.4.7: TruthfulQA "consists of 817 questions distributed across 38 categories"; ToxiGen uses "a revised version of the dataset from Hosseini et al. (2023) that reduces noise by filtering out prompts for which annotators disagree on the target demographic group", with the default ToxiGen classifier tuned on RoBERTa.
- Note: Llama 2 uses a HateBERT classifier fine-tuned on ToxiGen only in pretraining-data analysis (Section 4.1 text line); the evaluation classifier is the RoBERTa one.

## (g) StrongREJECT prompt count (313 vs 324). RESOLVED: the paper and the dataset say 313

- Paper (https://arxiv.org/pdf/2402.10260 v2, 27 Aug 2024), Section 2.1: "In total, the StrongREJECT dataset offers 313 high-quality forbidden prompts, with at least 50 forbidden prompts in each category. Out of these, 70% are our own novel prompts, 10% each are from DAN [31] and AdvBench [44], and the rest are from other prior work and OpenAI's system card." Section 3 also refers to the "full dataset of 313 forbidden prompts".
- Dataset file, https://raw.githubusercontent.com/alexandrasouly/strongreject/main/strongreject_dataset/strongreject_dataset.csv: parsed with Python csv, it has 313 rows. Categories: Non-violent crimes 59, Violence 54, Disinformation and deception 50, Hate/harassment/discrimination 50, Illegal goods and services 50, Sexual content 50. Sources: custom 221, DAN 35, AdvBench 25, MaliciousInstruct 12, HarmfulQ 11, three at 3 each. This matches "70% novel" (221/313 = 70.6%).
- Where 324 comes from: `wc -l` on that file gives 324 lines, because some prompts contain embedded newlines (313 parsed rows plus a header plus multi-line cells). The Inspect Evals README says "consists of a set of 324 'forbidden' prompts" (https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/strong_reject) while linking to `strongreject_small_dataset.csv` at a pinned commit. The current small CSV on main has 60 rows (10 per category, all custom). So the Inspect figure of 324 is inconsistent with both files as they stand on main. My explanation (a line count mistaken for a row count) is an inference, not confirmed. CONTRADICTED: "324 samples" as the StrongREJECT dataset size. Cite 313 from the paper; if citing Inspect, say "Inspect Evals documents 324 and uses a pinned copy of the small dataset".
- The Inspect listing page (ukgovernmentbeis.github.io/inspect_evals/...) returned only a redirect for the sub-page; the 324 figure on the main listing was not re-read.

## (h) AgentHarm and the "Princeton HAL leaderboard". UNCONFIRMED / STILL UNREADABLE

- AgentHarm itself: arXiv 2410.09024, "AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents", authors Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian, Derek Duenas, Maxwell Lin, Justin Wang, Dan Hendrycks, Andy Zou, Zico Kolter, Matt Fredrikson, Eric Winsor, Jerome Wynne, Yarin Gal, Xander Davies; comment "Accepted at ICLR 2025"; v1 11 Oct 2024, v3 18 Apr 2025. The arXiv page does not mention HAL, a leaderboard or Princeton.
- Search results (web search tool) list https://hal.cs.princeton.edu/agentharm titled "AgentHarm Benchmark", with a description of harm score, refusal rates and cost, and early entries Meta-Llama-3.1-405B-Instruct-Turbo and claude-3-5-sonnet-20241022. That is search-snippet evidence only.
- Direct fetch of https://hal.cs.princeton.edu/agentharm returns HTTP 404 (WebFetch and curl, 13 Oct 2026). The HAL home page https://hal.cs.princeton.edu/ lists 9 benchmarks (AssistantBench, CORE-Bench Hard, GAIA, Online Mind2Web, Scicode, ScienceAgentBench, SWE-bench Verified Mini, TAU-bench Airline, USACO), does not mention AgentHarm, and states: "We have paused updating HAL leaderboard with new models and are currently focusing on measuring reliability in AI agents." The HAL paper (arXiv 2510.11977, ICLR 2026) text has no occurrence of "agentharm".
- Verdict: a HAL AgentHarm page seems to have existed (snippets), but it is not currently reachable and is not part of HAL's current nine benchmarks or its paper. Do not state that AgentHarm is on the HAL leaderboard as a current fact. Say "a HAL page for AgentHarm appeared in search results but returns 404 now".

---

## Other facts to fix in the notes

- 2024.md section 4: replace the Claude 4 sentence "Secondary sources conflict on numbers" with the Table 2.7.A figures above, and note the attacker model was a Sonnet 3.5 (new) without safety training.
- 2024.md section 4 / correction 10: do not say the GPT-5.5 page calls StrongReject "saturated". It says "replaced ... with a more challenging multiturn jailbreak evaluation derived from red-teaming exercises".
- 2024.md section 3 (WMDP): the Grok 4 values are now verified from the card; Gemini 2.5 Pro use of WMDP is confirmed in the tech report (arXiv 2507.06261), not in the card PDF, which was inaccessible. Also note o1 lists WMDP biology only as an unreported contextual eval.
- early-2020-2022.md: GPT-4 0.73% (and GPT-3.5 6.48%) and the TruthfulQA claim are now verified. Llama 2 chat ToxiGen near-zero is verified from the paper.
- StrongREJECT count: use 313.
- Metric differences: o1 uses goodness@0.1; GPT-5 and GPT-5-Codex tables use not_unsafe; Anthropic uses attacker-generated "Best score" and "Top 3 average" attack success (lower is better). These are not comparable.
