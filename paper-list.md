# Paper list: 12 influential LLM safety benchmarks (2020–2026)

Status: working draft, 2026-10-13. Scope is LLM safety evaluation and benchmarking (safety-specific only; no general-capability benchmarks). Evidence comes from the notes in `years/` and the checks in `verification/`. Fields marked (unverified) were not confirmed against a primary source.

Citation counts are Semantic Scholar, checked 2026-10-13, unless noted. Where a count is missing, the API was rate-limited.

| # | Benchmark | Year | Venue | Citations | Verified lab or government use | Open data? |
|---|---|---|---|---|---|---|
| 1 | RealToxicityPrompts | 2020 | Findings of EMNLP 2020 | not retrieved | GPT-4 technical report (0.73% toxic generations vs 6.48% for GPT-3.5); HELM; lm-eval-harness | Yes (99,442 rows on Hugging Face) |
| 2 | TruthfulQA | 2021 | ACL 2022 | 4,093 | Llama 2 paper; Inspect Evals; lm-eval-harness; HELM | Yes (817 questions; revised Jan 2025) |
| 3 | DecodingTrust | 2023 | NeurIPS 2023 D&B (Outstanding Paper) | 724 | None found | Yes |
| 4 | XSTest | 2023 (arXiv) | NAACL 2024 Main | 590 | Inspect Evals | Yes (250 safe + 200 unsafe prompts) |
| 5 | HarmBench | 2024 | ICML 2024 | 1,676 | HELM Safety; FLI AI Safety Index | Yes |
| 6 | JailbreakBench | 2024 | NeurIPS 2024 D&B | 704 | None found (academic reuse only) | Yes |
| 7 | StrongREJECT | 2024 | NeurIPS 2024 D&B | 433 | OpenAI o1 card; Claude 4 card (Sec. 2.7); Inspect Evals. OpenAI later replaced it with a harder multiturn jailbreak evaluation. | Yes (313 prompts) |
| 8 | WMDP | 2024 | ICML 2024 | 582 | xAI Grok 4 card (Table 3); Gemini 2.5 technical report (WMDP Bio and Chem); Inspect Evals | Yes |
| 9 | AgentDojo | 2024 | NeurIPS 2024 D&B | 152 (likely an undercount) | NIST CAISI; UK AISI Inspect Evals; Meta Muse Spark report | Yes |
| 10 | Virology Capabilities Test (VCT) | 2025 | arXiv-only | 43 | GPT-5 card (Table 15: 41.4 ± 1.7%); Anthropic, xAI and Meta documents | No (withheld; vetted organizations only) |
| 11 | MASK | 2025 | arXiv-only | not retrieved | Grok 4 card; Anthropic Sonnet 5 and Opus 5 cards; Meta Muse Spark report; Scale leaderboard | Partly (1,000 public examples, 500 private holdout) |
| 12 | IPI Arena (Gray Swan) | 2026 | arXiv-only | not retrieved | Anthropic Sonnet 5, Opus 5 and Sonnet 5.5 cards; OpenAI GPT-6 Astra page; Google Gemini 4 Argon blog | Partly (evaluation kit is open; attack strings mostly withheld) |

## Entries

### 1. RealToxicityPrompts (2020)
- **Paper:** RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models
- **Authors:** Gehman et al.
- **Link:** arXiv 2009.11462
- **Measures:** how often a model continues a prompt with toxic text (about 100K prompts, scored by the Perspective API).
- **Limits:** labels come only from the Perspective API, which Google says ends 2026-12-31, so the metric will stop being reproducible.

### 2. TruthfulQA (2021)
- **Paper:** TruthfulQA: Measuring How Models Mimic Human Falsehoods
- **Authors:** Lin, Hilton, Evans
- **Link:** arXiv 2109.07958
- **Measures:** whether a model repeats common falsehoods (817 questions, 38 categories).
- **Limits:** revised by the authors in Jan 2025 (typos fixed, questions dropped, binary format added). Saturation claims come from weak sources.

### 3. DecodingTrust (2023)
- **Paper:** DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models
- **Authors:** Wang, Chen, Pei et al. (19 authors)
- **Link:** arXiv 2306.11698
- **Measures:** eight trust axes (toxicity, stereotype bias, adversarial and out-of-distribution robustness, adversarial demonstrations, privacy, machine ethics, fairness).
- **Limits:** the stereotype and fairness axes are borderline for a safety survey. No model card or leaderboard use found.

### 4. XSTest (2023)
- **Paper:** XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models
- **Authors:** Röttger, Kirk, Vidgen, Attanasio, Bianchi, Hovy
- **Link:** arXiv 2308.01263
- **Measures:** over-refusal. 250 safe prompts that look unsafe, plus 200 unsafe contrast prompts.
- **Limits:** the Claude 3 XSTest figure seen in notes comes from a secondary blog and was not checked against the model card.

### 5. HarmBench (2024)
- **Paper:** HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal
- **Authors:** Mazeika, Phan, Yin, Zou, Wang et al.
- **Link:** arXiv 2402.04249
- **Measures:** standardized automated red teaming (18 attack methods against 33 target models and defenses).
- **Limits:** a June 2026 preprint finds its classifier over-flags (precision 0.835, recall 0.974).

### 6. JailbreakBench (2024)
- **Paper:** JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models
- **Authors:** Chao, Debenedetti, Robey, Andriushchenko et al.
- **Link:** arXiv 2404.01318
- **Measures:** 100 misuse behaviors plus 100 matched benign behaviors, with a public leaderboard and a standardized threat model and judge.
- **Limits:** modest size. No lab, UK AISI or CAISI use found.

### 7. StrongREJECT (2024)
- **Paper:** A StrongREJECT for Empty Jailbreaks
- **Authors:** Souly, Lu, Bowen, Trinh et al.
- **Link:** arXiv 2402.10260
- **Measures:** a forbidden-prompt set with a rubric-based autograder that scores how useful a harmful response is.
- **Limits:** OpenAI cited grader issues. The prompt count is 313 per the paper (the 324 in Inspect Evals is probably a file line count).

### 8. WMDP (2024)
- **Paper:** The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning
- **Authors:** Li, Pan, Gopal et al. (56 authors)
- **Link:** arXiv 2403.03218
- **Measures:** 3,668 multiple-choice questions that proxy hazardous knowledge (bio, cyber, chem).
- **Limits:** Epoch calls WMDP-style biosecurity evaluations largely saturated and says it tests textbook-like knowledge, not uplift.

### 9. AgentDojo (2024)
- **Paper:** AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents
- **Authors:** Debenedetti, Zhang, Balunovic, Beurer-Kellner, Fischer, Tramèr
- **Link:** arXiv 2406.13352
- **Measures:** prompt injection against tool-using agents (97 tasks, 629 security test cases).
- **Limits:** a July 2026 validity audit (arXiv 2607.28685, not read) questions whether agent-safety benchmarks separate safety from capability.

### 10. Virology Capabilities Test (2025)
- **Paper:** Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark
- **Authors:** SecureBio and CAIS (9 authors)
- **Link:** arXiv 2504.16137
- **Measures:** 322 multimodal questions on tacit wet-lab virology troubleshooting (dual-use bio uplift).
- **Limits:** data is withheld. The Claude 4 and Sonnet 4.5 cards call it saturated or no longer valid as a rule-out.

### 11. MASK (2025)
- **Paper:** The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems
- **Authors:** Ren, Agarwal, Mazeika et al. (16 authors; CAIS and Scale AI)
- **Link:** arXiv 2503.03750
- **Measures:** whether a model lies under pressure, compared with its own elicited beliefs.
- **Limits:** the Scale leaderboard tops out near 96% honesty, so it is close to ceiling. Scale is an author organization.

### 12. IPI Arena (2026)
- **Paper:** How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition
- **Authors:** Dziemian et al. (31 authors; Gray Swan)
- **Link:** arXiv 2603.15714
- **Measures:** indirect prompt injection against agents in 41 scenarios. An attack counts only if the agent runs the harmful action and hides it from the user. The competition had 464 participants, about 272K attempts and 13 models.
- **Limits:** not peer-reviewed. Gray Swan builds, hosts and sells to the labs it scores (analysis, not a sourced fact). Anthropic's scenario and attack counts (28 and 1,130) do not match the paper's (41 and 2,679). Cross-card numbers disagree for GPT-5.6 Sol (20.0% in Anthropic's card, 27.0% in OpenAI's).

## Referenced in the story but not numbered
- **AdvBench** (arXiv 2307.15043): arXiv-only. HarmBench finds 58 unique behaviors after deduplication. No 2025–26 lab use found.
- **Anthropic red-team dataset** (arXiv 2209.07858): arXiv-only. 38,961 attacks, distributed inside HH-RLHF.
- **AgentHarm** (arXiv 2410.09024): ICLR 2025. Only a subset of the data is public (44 of 66 test behaviors).
- **Agent Red Teaming (ART)** (arXiv 2507.20526): predecessor of IPI Arena. Anthropic retired it in 2026.
- **SHADE-Arena** (arXiv 2506.15740) and **Apollo's scheming evaluations** (arXiv 2509.15541): cited in Opus 4.5 and GPT-5 cards, but built in-house and mostly closed.
- **AILuminate** (arXiv 2503.05731): standards-body weight, no verified lab use.

## Open items
- Re-read the GPT-5.5 page directly before quoting the StrongREJECT replacement sentence (it was read through a summarizing tool).
- The Gemini 2.5 Pro model card PDF could not be opened (AccessDenied). The WMDP link there rests on Epoch's chart caption plus the Gemini 2.5 technical report.
- Citation counts missing for RealToxicityPrompts, MASK and IPI Arena.
- Later xAI cards, GPT-5.2 and the Sonnet 4.5 "saturated" claim were not rechecked.
