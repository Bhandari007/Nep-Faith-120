# Domain Glossary: NepFaith-120

This glossary defines canonical terms and conventions for the NepFaith-120 research project investigating cross-lingual faithfulness scoring failure on Nepali → English RAG.

---

## Core Quantities & Hypotheses

- **$\Delta_{MT}$ (Machine Translation Gap)**:
  $$\Delta_{MT} = A(C3) - A(C2)$$
  The performance penalty attributable strictly to machine translation quality. Measures evaluator accuracy under human post-edited translation minus accuracy under raw machine translation.
- **$\Delta_{XL}$ (Cross-Lingual Gap)**:
  $$\Delta_{XL} = A(C3) - A(C1)$$
  The performance penalty attributable strictly to evaluating cross-lingually rather than monolingually on clean translations.
- **H1 (Primary Hypothesis)**:
  $\Delta_{XL} > \Delta_{MT}$ — The primary bottleneck in cross-lingual RAG evaluation is the cross-lingual evaluator's inability to judge cross-lingual entailment, not errors introduced by machine translation.
- **H2 (Claim-Type Survival)**:
  Certain claim types (e.g. attribution, honorifics/register, numbers) will show differential survival rates across MT vs cross-lingual scoring.

---

## Context Conditions

- **C1 (Cross-Lingual Evaluation)**: Original Nepali context evaluated cross-lingually against the English answer.
- **C2 (Machine Translation)**: Nepali context translated to English via machine translation (IndicTrans2) and evaluated monolingually against the English answer.
- **C3 (Post-Edited MT Ceiling)**: Machine translation from C2 post-edited by a human translator to correct MT errors and evaluated monolingually against the English answer. **Crucial:** C3 is human *post-edited* MT, *not* from-scratch human translation.

---

## Annotation & Unit of Evaluation

- **Claim-Level Unit**: The atomic, primary unit of faithfulness scoring. RAGAS-style decomposition splits generated answers into individual claims.
- **Claim Labels**:
  - `Supported`: The claim is directly entailed by the reference context.
  - `Contradicted`: The claim directly asserts a fact that conflicts with the reference context.
  - `Not-in-context`: The reference context neither confirms nor contradicts the claim.
  > [!IMPORTANT]
  > `Contradicted` $\ne$ `Not-in-context`. Confabulations that add external facts must not be conflated with assertions that actively conflict with the context.
- **Derived Item Label**: The overall faithfulness judgment of an answer item derived from its constituent claim labels. An item is marked faithful if all its claims are supported.
- **Critical-Claim Override**: If any critical claim is contradicted or not-in-context, the entire item is deemed unfaithful, regardless of the proportion of non-critical supported claims.
- **Human–Human Ceiling**: The inter-annotator agreement (Krippendorff's $\alpha$) between trained human annotators prior to adjudication, representing the realistic upper bound of scorer performance.

---

## Corpus & Sampling

- **Provenance**:
  - `Natural`: Naturally generated responses across retrieval conditions (full support, partial support, distractor present).
  - `Perturbed`: Answers modified via the perturbation engine with 7 typed edits (entity swap, number/date alteration, negation flip, attribution removal/misattribution, honorific/register shift, unsupported addition, invented causal relation) guaranteeing hard negative examples.
- **Sampling Weight**: The inverse probability weight assigned to each item during stratified sampling (by domain, provenance, and claim type) ensuring statistically valid population estimates.
- **Prediction-Powered Inference (PPI)**: Statistical framework (implemented via GLIDE) producing valid confidence intervals on $\Delta_{XL}$ and $\Delta_{MT}$ over the full ~1,500 item corpus using ~120–150 human gold labels and model proxies.

---

## Evaluator Arms

An **Arm** is a specific scoring instrument evaluated under the benchmark. The arm list is frozen at Gate 0:
1. `HHEM-2.1-Open`: Vectara open-weights hallucination evaluation model.
2. `BGE-M3` or `LaBSE`: Dense embedding cosine similarity baseline.
3. `mDeBERTa-xnli` (matched instrument): Evaluated across C1, C2, and C3.
4. `IndicTrans2 → English NLI`: Machine translation followed by English NLI entailment.
5. `LLM judge`: Pinned commercial/open-weights LLM evaluated across C1, C2, and C3.
