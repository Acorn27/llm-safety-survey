# 2025 wider search: safety benchmarks first released in 2025

Run date: 2026-10-13. Scope: safety-specific benchmarks first released in 2025. Excluded as already handled elsewhere: VCT, MASK, Gray Swan ART/IPI. Excluded as 2024 releases: AILuminate, SORRY-Bench, AIR-Bench, AgentHarm, ASB.

Labels: VERIFIED means I opened the primary document (PDF/arXiv/venue page) and saw the fact. UNVERIFIED means a search snippet, a secondary source, or not checked.

## Bottom line

No 2025-released safety benchmark has strong, multi-lab adoption evidence. What exists is single-lab evidence: SHADE-Arena in Anthropic's Claude Opus 4.5 card, the Phuong et al. stealth/situational-awareness suite in Google DeepMind's Gemini 3 Pro FSF report, and Apollo's 26-eval scheming suite in OpenAI's GPT-5 card. In each case the benchmark is first-party or a close collaborator of the lab that reports it. I found no 2025 static prompt-set safety benchmark (jailbreak, refusal, multilingual, over-refusal) cited in the frontier cards I opened. Those cards still lean on 2021-2024 sets (StrongREJECT, BBQ, LAB-Bench, Cybench).

## Ranking of the strongest 2025 candidates

1. SHADE-Arena (best evidence, but Anthropic-internal usage and only partly public)
2. Phuong et al., stealth and situational awareness evals (DeepMind-internal, no public data link found)
3. Apollo scheming evaluation suite as used in GPT-5 / anti-scheming paper (strong use, but not a released benchmark)
4. CyberGym (used in Opus 4.5 card, but a capability benchmark, so borderline for "safety")
5. OS-Harm (clean NeurIPS 2025 D&B paper and public data, no frontier-card use found)
6. CVE-Bench (ICML 2025, cyber capability, borderline)
7. FORTRESS (public data, over-refusal pairing, little verified adoption)
8. PropensityBench (arXiv Nov 2025, no adoption evidence)

## Detailed records

### 1. SHADE-Arena
- Title: SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents (VERIFIED, arXiv abstract page via search and Opus 4.5 card footnote 34)
- Authors: Jonathan Kutasov and 11 co-authors (VERIFIED: "Kutasov, J., et al." in the Opus 4.5 card; first author and co-author count from the arXiv listing in search results). Full list not captured.
- Venue/year: arXiv only, first submitted 17 Jun 2025, v2 8 Jul 2025 (VERIFIED). No peer-reviewed venue found; Semantic Scholar lists "arXiv.org".
- PDF: https://arxiv.org/pdf/2506.15740
- Dataset/code: https://github.com/safety-research/SHADE-Arena. VERIFIED by fetch: this repo is marked DEPRECATED and points to https://github.com/jkutaso/SHADE-Arena as the current public split (MIT license). I did not open the second repo. The paper says 5 of 17 task pairs are public, the rest on request (VERIFIED from search-result summary of the paper).
- Measures: pairs of a benign long-horizon agentic main task and a harmful hidden side task; the agent must complete the side task without an LLM monitor flagging it. Also measures monitor quality. 17 task pairs. Headline: best sabotage agents 27% (Claude 3.7 Sonnet) and 15% (Gemini 2.5 Pro); best monitor Gemini 2.5 Pro AUC 0.87 (UNVERIFIED beyond the abstract summary).
- Citations: 69 (Semantic Scholar API, queried 2026-10-13).
- Evidence of use: Claude Opus 4.5 system card, Section 6.11.1 "SHADE-Arena" (VERIFIED, opened the PDF and read the text): https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf . The card describes tasks as "a long-horizon agentic main task that is paired with a harmful side task", with Claude Sonnet 3.7 as monitor calibrated to flag about 1% of benign transcripts. Not found in the Claude Opus 4 / Sonnet 4 card (May 2025, predates the paper) or in the GPT-5 card. Not listed in the UK AISI Inspect Evals index per my fetch. I did not open the Opus 4.1 card.
- Limitations: Anthropic authored the benchmark and reports it, so independence is low. The public split is small and the repo layout is in flux. Measures capability to sabotage with a weak monitor, not propensity. Results depend on the monitor model and a hidden scratchpad. Contamination risk is the stated reason for withholding tasks.

### 2. Evaluating Frontier Models for Stealth and Situational Awareness
- Title: Evaluating Frontier Models for Stealth and Situational Awareness (VERIFIED, arXiv abs page fetched)
- Authors: Mary Phuong, Roland S. Zimmermann, Ziyue Wang, David Lindner, Victoria Krakovna, Sarah Cogan, Allan Dafoe, Lewis Ho, Rohin Shah (VERIFIED)
- Venue/year: arXiv 2 May 2025 (v4 3 Jul 2025). Semantic Scholar lists "Proceedings of IASEAI Conference" 2025; I did not confirm this on the conference site (UNVERIFIED).
- PDF: https://arxiv.org/pdf/2505.01420
- Dataset: none linked on the arXiv page (VERIFIED absence on that page). Inspect Evals index lists "GDM Dangerous Capabilities: Stealth" (per WebFetch summary of https://ukgovernmentbeis.github.io/inspect_evals/; the summary was internally inconsistent in its counts, so treat as moderate confidence).
- Measures: 5 stealth evaluations (getting around oversight) and 11 situational-awareness evaluations, framed as prerequisites for scheming in a safety case. Frontier models showed no concerning levels (VERIFIED, abstract).
- Citations: 30 (Semantic Scholar, 2026-10-13).
- Evidence of use: Gemini 3 Pro Frontier Safety Framework Report (Nov 2025) runs stealth and situational-awareness challenges and cites "Phuong et al. (2025)" for task descriptions (VERIFIED, opened PDF text): https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf . It reports the final model did not show a material capability there.
- Limitations: Authors and user are the same lab. No public dataset located. Capability-only; the paper itself notes current models score low.

### 3. Apollo Research scheming evaluation suite (26 evals) / Stress Testing Deliberative Alignment for Anti-Scheming Training
- Title: Stress Testing Deliberative Alignment for Anti-Scheming Training (VERIFIED, arXiv abs fetched)
- Authors: Bronson Schoen, Evgenia Nitishinskaya, Mikita Balesni, Axel Hojmark, and 15 more (19 total; VERIFIED count). Apollo Research with OpenAI per search coverage.
- Venue/year: arXiv, 19 Sep 2025. No venue found.
- PDF: https://arxiv.org/pdf/2509.15541
- Dataset: none released (VERIFIED absence on arXiv page).
- Measures: covert-action rates across 26 out-of-distribution evaluations (180+ environments).
- Citations: 78 (Semantic Scholar, 2026-10-13). For reference, the 2024 precursor "Frontier Models are Capable of In-context Scheming" (arXiv 2412.04984) has 333; it is a 2024 release and out of scope.
- Evidence of use: GPT-5 system card (arXiv 2601.03267), Section 6.2.1 (VERIFIED, opened PDF): "Apollo Research evaluated gpt-5-thinking on a range of 26 evaluations (>180 environments, >4600 samples)"; covert action rate 3.97% vs 8.24% for o3 and 28.36% for helpful-only. Also noted in Gemini 3 and Claude materials as an external evaluator (Apollo named for Gemini 3 per secondary source, UNVERIFIED; Claude Opus 4 card section 4.1.1.4 VERIFIED cites Apollo scenario evaluations following their earlier work).
- Limitations: Not a downloadable benchmark, so poor fit for a "datasets" survey. Evaluation awareness confounds results (the GPT-5 card says the model sometimes reasons it is being evaluated). Evaluations were designed to elicit deception, so rates do not map to deployment.

### 4. CyberGym
- Title: CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities at Scale (Semantic Scholar title; the Opus 4.5 card gives a slightly different title). arXiv 2506.02548.
- Authors: "Wang, Z., et al." only (VERIFIED from the card's reference); full list not captured.
- Venue/year: arXiv Jun 2025; Semantic Scholar venue field is empty (no venue confirmed).
- PDF: https://arxiv.org/abs/2506.02548 . Dataset link: not checked (UNVERIFIED).
- Measures: finding previously known vulnerabilities from a description and discovering new ones in real open-source projects; 1,505 tasks (VERIFIED from card text).
- Citations: 86 (Semantic Scholar, 2026-10-13).
- Evidence of use: Claude Opus 4.5 system card Section 2.14 (VERIFIED). Listed in Inspect Evals (per WebFetch summary, moderate confidence).
- Limitations: Framed as a capability benchmark, reported in the card's capabilities section, not its safety sections. Borderline for "safety-specific".

### 5. OS-Harm
- Title: OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents (VERIFIED)
- Authors: Kuntz, Duzan, Zhao, Croce, Kolter, Flammarion, Andriushchenko (from search summary of the NeurIPS/arXiv pages; first names not captured).
- Venue/year: NeurIPS 2025 Datasets and Benchmarks Track (VERIFIED, papers.neurips.cc page returned by search); arXiv 2506.14866, Jun 2025.
- PDF: https://arxiv.org/pdf/2506.14866 . NeurIPS page: https://papers.neurips.cc/paper_files/paper/2025/hash/4009bff0cd87ba2203c8e3a2f082aaec-Abstract-Datasets_and_Benchmarks_Track.html
- Dataset/code: https://github.com/tml-epfl/os-harm (VERIFIED by fetch: 3 task lists, Apache-2.0, LLM judge, traces on Google Drive, 78 stars at fetch time).
- Measures: 150 tasks on OSWorld across deliberate misuse, prompt injection and model misbehavior (50 each); LLM judge with F1 0.76 (accuracy) and 0.79 (safety) vs humans. Models tested included o4-mini, Claude 3.7 Sonnet, Gemini 2.5 Pro.
- Citations: 122 (Semantic Scholar, 2026-10-13).
- Evidence of use: no frontier-card use found (searched; Opus 4.5 and GPT-5 cards contain no OS-Harm string; "not in Inspect Evals" per fetch). Evidence is academic citations only.
- Limitations: small (150 tasks), judge error rate, OSWorld-only.

### 6. CVE-Bench
- Title: CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities (Semantic Scholar title, truncated in my output). arXiv 2503.17332.
- Venue: ICML 2025 per Semantic Scholar (UNVERIFIED on the ICML site). Authors not captured.
- Citations: 129 (Semantic Scholar, 2026-10-13). Listed in Inspect Evals (moderate confidence). Frontier-card use not found.
- Limitations: cyber capability benchmark; borderline.

### 7. FORTRESS
- Title: FORTRESS: Frontier Risk Evaluation for National Security and Public Safety (VERIFIED)
- Authors: Christina Q. Knight, Kaustubh Deshpande, Ved Sirdeshmukh, Meher Mankikar, Scale Red Team, SEAL Research Team, Julian Michael (VERIFIED)
- Venue/year: arXiv only, 17 Jun 2025 (v2 24 Jun). PDF: https://arxiv.org/pdf/2506.14922 . Dataset: https://huggingface.co/datasets/ScaleAI/fortress_public
- Measures: 500 expert-written adversarial prompts with 4-7 binary rubric questions each, three domains (CBRNE; political violence and terrorism; criminal and financial), 10 subcategories, plus a benign twin of each prompt for over-refusal.
- Citations: 19 (Semantic Scholar, 2026-10-13). Evidence of use: listed in Inspect Evals (moderate confidence); a third-party aggregator attributes it to a July 2026 model card from another lab, which I could not verify (UNVERIFIED). No card I opened uses it.
- Limitations: judged by LLM against rubrics; unclassified-information scope only.

### 8. PropensityBench
- arXiv 2511.20703 (Nov 2025), Scale Labs; per search summary 5,874 scenarios, 6,648 tools, four domains (cyber, self-proliferation, bio, chem). Citation count UNVERIFIED (API rate-limited). No adoption evidence found.

## Other 2025 items seen but not ranked
- Petri (Anthropic, Oct 2025): open-source automated auditing tool, https://github.com/safety-research/petri . A tool, not a dataset. VERIFIED that the Opus 4.5 card Sections 6.2 and 6.2.4 discuss it and report Petri comparisons across developers.
- JBDistill, "Jailbreak Distillation: Renewable Safety Benchmarking": listed at Findings of EMNLP 2025 (ACL Anthology preview) and a NeurIPS 2025 D&B page. The previous year file says NeurIPS; the venue question is open (UNVERIFIED which is correct). Adoption: none found.
- Automating Deception: Scalable Multi-Turn LLM Jailbreaks (NeurIPS 2025, https://neurips.cc/virtual/2025/127999): 1,500 scenarios, per search summary only (UNVERIFIED; authors not captured).
- SafeArena (arXiv 2503.04957, Mar 2025, 250 safe + 250 harmful web-agent tasks), PolyGuard (arXiv 2506.19054), FalseReject (arXiv 2505.08054, 59 citations), OS-adjacent BountyBench (NeurIPS 2025, 49 citations): seen, not examined in depth.
- CyberSOCEval (arXiv 2509.20166) and AutoPatchBench (Meta, Apr 2025, within CyberSecEval 4): defensive-cyber capability; borderline, not examined in depth.
- ACL 2025: SafeLawBench, LongSafety, Chinese SafetyQA; EMNLP 2025: MemeSafetyBench, SafeToolBench (Findings). Seen via search results only (UNVERIFIED details). No outstanding/best paper award for a safety benchmark was found at ACL or EMNLP 2025.
- Excluded as capability benchmarks: HealthBench, AbstentionBench, PaperBench (cited in the GPT-5 card, VERIFIED, but not safety-specific).
- Post-2025 (out of scope): MultiBreak (arXiv 2605.01687), TeleAI-Safety (Dec 2025 arXiv, borderline date; not examined), LITMUS and ClawSafety (2026).
- Bias/fairness framed as harm evaluation: none surfaced; nothing to flag as borderline.

## Coverage gaps (what I did not do)
- USENIX Security / IEEE S&P / ACM CCS / NDSS 2025: two searches returned no confirmed benchmark paper (only TwinBreak, an attack paper). Not exhaustive; accepted-paper lists were not browsed. Treat as unexplored, not as negative.
- Not searched: ICLR 2026 submissions, Lilian Weng and Nicholas Carlini posts, METR and Epoch pages, International AI Safety Report text (only the Oct 2025 Key Update press coverage was seen, which names no specific benchmarks).
- Opened for system-card evidence: GPT-5 card (full text), Claude Opus 4.5 card (full text), Claude Opus 4 / Sonnet 4 card (grep only), Gemini 3 Pro FSF report (full text). Not opened: Claude Opus 4.1 card, Gemini 3 model card text, GPT-5 system-card successors.
- Semantic Scholar rate-limited me; counts for PropensityBench, SafeArena, PolyGuard, CyberSOCEval are UNVERIFIED. All counts shown above are from the 2026-10-13 API run.
- Inspect Evals "listed" claims come from a small-model summary of the docs page, which contradicted itself on counts once; re-check by hand before citing.
