# Story plan: how LLM safety evaluation developed, 2020–2026

Status: plan only, 2026-10-13. The narrative itself is not written yet. It will be built from `years/` (per-year notes), `verification/` (checked evidence) and `paper-list.md` (the 12 benchmarks).

## Thesis
Safety benchmarks do not stay useful for long. Each generation measures the risks of its moment, gets adopted, saturates or is replaced, and by 2025–26 the evaluations that frontier labs actually report are increasingly the ones they build and control themselves.

## Recurring themes to carry across years
1. **Lifecycle:** release, adoption, saturation, replacement. Examples: StrongREJECT replaced by OpenAI with a harder multiturn jailbreak evaluation; VCT called saturated or no longer valid as a rule-out in Anthropic's Claude 4 and Sonnet 4.5 cards; MASK near ceiling on Scale's leaderboard; Epoch calls WMDP-style bio evaluations largely saturated.
2. **Fragile foundations:** RealToxicityPrompts depends on the Perspective API, which Google says ends 2026-12-31.
3. **Measurement quality:** small and duplicated test sets (AdvBench has 58 unique behaviors after deduplication, per HarmBench), judge reliability (HarmBench classifier over-flags; MLCommons jailbreak judge error rates), and construct validity (the July 2026 audit of agent-safety benchmarks).
4. **Open vs. closed:** from open academic sets to withheld data (VCT, IPI Arena attack strings) and in-house lab evaluations (SHADE-Arena, Apollo scheming suite).
5. **Adoption signal:** model and system cards, government evaluations and leaderboards. This lags academic influence, so citation counts and lab use will disagree.

## Year by year
Each year gets: what was new, the state of development, gaps, and what it set up for the next year.

### 2020 (thin year)
- **Benchmarks:** RealToxicityPrompts.
- **Story:** safety evaluation is toxicity measurement for GPT-2-era models. Bias sets (CrowS-Pairs, StereoSet) exist but are out of scope.
- **Gaps:** one automated label source (Perspective), no notion of adversarial users.
- **Sets up:** truthfulness and harder harms.

### 2021
- **Benchmarks:** TruthfulQA.
- **Story:** the first benchmark that shows bigger models can be worse (they mimic falsehoods). Agenda papers outnumber benchmarks ("Unsolved Problems in ML Safety", Anthropic's HHH, DeepMind's risks taxonomy).
- **Gaps:** English, static, no jailbreaks, dangerous capabilities or agents.
- **Sets up:** red teaming as a method.

### 2022
- **Benchmarks:** Anthropic red-team dataset (milestone, not numbered); ToxiGen, HELM and PromptInject as context.
- **Story:** the shift from fixed prompt lists to adversarial red teaming, after ChatGPT and RLHF.
- **Gaps:** red-team data is a collection of attacks, not a fixed benchmark. Everything English-only.
- **Sets up:** jailbreaks as an attack field.
- **Known weakness:** this year's notes were the thinnest on security venues and model-card adoption.

### 2023
- **Benchmarks:** DecodingTrust, XSTest; AdvBench as the flawed predecessor.
- **Story:** the field becomes its own field. Multi-axis suites, jailbreak sets (GCG, DAN study), over-refusal as a new axis, early agent and cyber evaluations. Llama 2 reports TruthfulQA, ToxiGen and BOLD. Policy (US EO 14110, Bletchley, Anthropic RSP) frames evaluation of extreme risks without naming benchmarks.
- **Gaps:** no standard attack or judge protocol, small sets, GPT-4 as judge.
- **Sets up:** standardization.

### 2024
- **Benchmarks:** HarmBench, JailbreakBench, StrongREJECT, WMDP, AgentDojo; AgentHarm as companion.
- **Story:** standardization. Fixed threat models, judges and leaderboards. Dangerous-capability proxies with unlearning (WMDP). Agent safety begins (AgentDojo, AgentHarm). Government pre-deployment testing starts (US/UK AISI on Claude 3.5 Sonnet). StrongREJECT reaches the OpenAI o1 card.
- **Gaps:** judge reliability, English-centric single-turn prompts, saturation and contamination, WMDP is knowledge not uplift.
- **Sets up:** reporting in system cards, agent security.

### 2025 (consolidation year)
- **Benchmarks:** VCT, MASK; ART as predecessor; SHADE-Arena and Apollo scheming suite as the in-house trend.
- **Story:** no 2025-released open benchmark shows strong multi-lab adoption. Static refusal and jailbreak sets in the cards are still 2021–2024 ones. Several 2024 preprints gain ICLR 2025 venue status (SORRY-Bench, AgentHarm, AIR-Bench, Agent Security Bench). New 2025 evaluations target frontier risks (bio uplift, honesty, scheming, sabotage), and the ones that reach system cards are mostly lab-built and partly closed.
- **Gaps:** closed data, saturation, near-ceiling honesty scores, thin evidence of real-world transfer.
- **Sets up:** agent-security evaluation at scale.
- **Known weakness:** security-venue and blog coverage for 2025 was not exhaustive.

### 2026 (current)
- **Benchmarks:** IPI Arena (adopted de facto in frontier cards; not peer-reviewed; data largely withheld).
- **Story:** text jailbreak sets give way to agent evaluations scored on what the agent actually did. Anthropic retires ART for IPI Arena. The International AI Safety Report 2026 warns that benchmarks predict real-world risk poorly. MLCommons posts a jailbreak benchmark (arXiv 2610.02827); its judge error rates are verified but the paper does not say what data they were computed on.
- **Gaps:** vendor conflict of interest, cross-card comparability (GPT-5.6 Sol is 20.0% in Anthropic's card and 27.0% in OpenAI's), judge reliability, benchmarks too new to have a track record.
- **Future directions:** renewable and adaptive benchmarks, independent (non-vendor) agent evaluations, validity audits, multi-turn and multilingual coverage.

## Closing section: what the labs actually use
- **Verified in cards:** StrongREJECT (o1, Claude 4), WMDP (Grok 4), VCT (GPT-5 and others), MASK (Grok 4 and others), IPI Arena (Anthropic, OpenAI, Google), TruthfulQA and RealToxicityPrompts (older cards, Llama 2 and GPT-4).
- **Not found in 2026 Anthropic or OpenAI cards:** AgentHarm, AgentDojo, AILuminate, StrongREJECT (full-text search by the verification agent).
- **Academic influence without lab use:** DecodingTrust, JailbreakBench.

## Evidence caveats to keep on the slides
- VCT, MASK and IPI Arena are arXiv-only.
- VCT and IPI Arena data are largely withheld.
- Several lab-card figures were read from documents; others (Gemini 2.5 Pro model card) could not be opened.
- Clearly distinguish claims made by the papers and cards from our own interpretation (course requirement).
- AI use must be disclosed on the website and slides: AI agents did the literature search and verification; we verified key claims against primary documents as recorded in `verification/`.

## Next steps
1. Re-read the unverified items listed at the bottom of `paper-list.md`.
2. Fill the remaining citation counts.
3. Write the narrative from this plan.
4. Decide the website structure (separate task; not started).
