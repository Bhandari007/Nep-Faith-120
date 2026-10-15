# Pre-Registration: NepFaith-120

> **Study Title:** Decomposing Machine Translation Error vs. Cross-Lingual Evaluator Alignment in Nepali → English RAG Faithfulness Scoring  
> **Lead Researcher:** Muskan Bhandari  
> **Registration Date:** 2026-10-15  
> **Status:** Committed Prior to Engineering Pipeline Build (Gate 0)  
> **Target Venues:** ACL / EMNLP / NAACL  

---

## 1. Study Rationale & Research Questions

In cross-lingual Retrieval-Augmented Generation (RAG) involving low-resource Indic languages such as Nepali (`ne` / `npi_Deva`), systems retrieve local-language passages to answer English queries. Evaluating factual faithfulness introduces an architectural trade-off:
1. **Direct Cross-Lingual Evaluation ($C1$):** Score the English answer directly against the raw Nepali context.
2. **Translate-then-Evaluate ($C2$):** Translate the Nepali context to English via Machine Translation (IndicTrans2) and evaluate monolingually.

Conventional NLP wisdom assumes machine translation introduces destructive semantic drift. However, cross-lingual evaluators themselves struggle with semantic entailment on low-resource scripts like Devanagari.

**Core Question:** When cross-lingual faithfulness evaluation fails on Nepali $\to$ English RAG, *why* does it fail, and *how much of the failure is machine translation's fault versus the evaluator's cross-lingual reasoning fault?

---

## 2. Formal Hypotheses

### Primary Hypothesis ($H1$): The Cross-Lingual Evaluator Bottleneck
$$\Delta_{XL} > \Delta_{MT}$$
Where:
- $\Delta_{MT} = A(C3) - A(C2)$ measures the accuracy penalty attributable strictly to machine translation errors.
- $\Delta_{XL} = A(C3) - A(C1)$ measures the accuracy penalty attributable strictly to cross-lingual evaluation.
- $A(C)$ denotes the macro F1 / accuracy of an evaluator arm under context condition $C$ against human gold labels.

**Prediction:** Across automated evaluator arms, the degradation caused by cross-lingual semantic judgment ($\Delta_{XL}$) will strictly exceed the degradation introduced by state-of-the-art machine translation ($\Delta_{MT}$).
- **Null Hypothesis ($H_{1,0}$):** $\Delta_{XL} \le \Delta_{MT}$.
- **Decision Rule:** Reject $H_{1,0}$ if the cluster-robust paired PPI++ 95% confidence interval for $\Delta_{XL} - \Delta_{MT} = A(C2) - A(C1)$ strictly excludes zero and is positive ($\alpha = 0.05$).

### Secondary Hypothesis ($H2$): Claim-Type Survival Across Perturbations
The survival rate of factual claims across MT ($C2$) versus cross-lingual evaluation ($C1$) will systematically vary by perturbation type:
- Fine-grained entity swaps and numerical modifications will suffer higher degradation under machine translation.
- Honorific / register shifts, evidential shifts, and invented causal relations will suffer higher degradation under direct cross-lingual evaluation.

---

## 3. Experimental Counterfactual Conditions

Every evaluation item is paired and evaluated across three distinct context conditions:

1. **Condition $C1$ (Direct Cross-Lingual):**
   - Context: Original Nepali passage ($c_{\text{ne}}$).
   - Hypotheses: Segmented English atomic claims ($\{k_{ij}\}$).
2. **Condition $C2$ (Raw Machine Translation):**
   - Context: Passage translated to English via IndicTrans2 ($MT(c_{\text{ne}})$).
   - Hypotheses: Segmented English atomic claims ($\{k_{ij}\}$).
3. **Condition $C3$ (Human Post-Edited MT Ceiling):**
   - Context: Machine-translated passage post-edited by a human translator ($PE(MT(c_{\text{ne}}))$) to correct MT distortions while preserving syntactic framing.
   - Hypotheses: Segmented English atomic claims ($\{k_{ij}\}$).
   - *Pre-registered Rule:* Condition $C3$ is strictly human *post-edited* MT, *not* from-scratch translation, ensuring that stylistic and syntactic divergence is controlled as a confounding variable.

---

## 4. Sampling Frame & Dataset Design

### Source Domains & Stratification
Passages are stratified across three distinct domains:
1. **Nepali Wikipedia (`wikipedia`):** General encyclopedic entities (CC BY-SA 4.0).
2. **Nepali Government & Public Reports (`government_report`):** Statistical, demographic, and policy reports with dense numerical tables and low web-crawl pretraining leakage (Public domain under Nepal Copyright Act Sec 4/16).
3. **Nepali Contemporary News (`news`):** Current event reporting with explicit source attribution.

### Balanced Provenance (50% Natural / 50% Perturbed)
To guarantee label balance and prevent evaluator bias toward default "Supported" outputs:
- **50% Natural RAG Items:** Responses generated from retrieval conditions (full support, partial support, distractor present).
- **50% Perturbed Items:** Synthesized via deterministic, typed edits across 7 categories:
  1. `entity_swap` (Named entity replacement with in-domain distractor)
  2. `number_date_alteration` (Numerical, percentage, or Bikram Sambat date distortion)
  3. `negation_flip` (Grammatical polarity reversal)
  4. `misattribution` (Shifting statements to incorrect agencies/speakers)
  5. `register_shift` (Altering Nepali honorific markers affecting authority/plurality)
  6. `unsupported_addition` (Injecting ungrounded external confabulations)
  7. `invented_causality` (Connecting true facts with false causal links)

### Sample Sizes
- **Core Human Gold Benchmark ($n$):** 120 items (~350 atomic claims), doubly annotated and adjudicated.
- **Unlabelled Inference Corpus ($N$):** $\sim 1,500$ items (~4,500 atomic claims) scored by proxy autoraters.

---

## 5. Annotation Unit & Operational Rubric

1. **Unit of Evaluation:** Atomic factual propositions (single assertion, self-contained references, checkable).
2. **Three-Way Grounded Labels:**
   - `Supported`: Proposition is entailed by the reference passage.
   - `Contradicted`: Proposition directly conflicts with the reference passage.
   - `Not-in-context`: Proposition introduces external facts neither confirmed nor refuted by the context.
   - *Pre-registered Rule:* $\text{Contradicted} \ne \text{Not-in-context}$.
3. **Derived Item Faithfulness:** An answer item is faithful ($1$) iff all constituent claims are `Supported`. If any claim flagged as `critical` receives `Contradicted` or `Not-in-context`, the item is designated `Unfaithful` ($0$).

---

## 6. Frozen Evaluator Arms

The evaluation suite is frozen across 5 scoring instruments:
1. **Arm 1 (Specialized Hallucination Scorer):** `vectara/hallucination_evaluation_model` (HHEM-2.1-Open).
2. **Arm 2 (Dense Semantic Similarity Baseline):** `BAAI/bge-m3` (cosine similarity).
3. **Arm 3 (Matched Cross-Lingual NLI Instrument):** `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` evaluated across $C1$, $C2$, and $C3$.
4. **Arm 4 (Pipeline MT $\to$ English NLI):** `ai4bharat/indictrans2-indic-en-dist-200M` $\to$ `cross-encoder/nli-deberta-v3-large`.
5. **Arm 5 (Frontier LLM-as-a-Judge):** `gemini-2.5-flash` at `temperature: 0.0`, `seed: 42`, with round-robin key rotation across 10 API keys and prompt-hash deterministic caching. Generator is decoupled (`Meta-Llama-3-8B-Instruct`).

---

## 7. Statistical Inference Engine (PPI++)

To scale statistical power over the full $N \approx 1,500$ corpus without model bias:
1. **Prediction-Powered Inference (PPI++):** Uses proxy predictions with data-driven tuning parameter $\lambda^*$ as a control variate, falling back to classical variance if correlation $\rho \approx 0$.
2. **Cluster-Robust Residuals:** Because claims $k_{ij}$ are nested within answer item $i$ ($\rho_{\text{ICC}} > 0$), standard errors are computed at the cluster (item) level.
3. **Paired Covariance Cancellation:** Because identical items are evaluated under $C1, C2, C3$, the covariance term $-2\,\mathrm{Cov}(A(C2), A(C1))$ actively cancels background item-difficulty noise, yielding tight confidence intervals for $H1$.

---

## 8. Governance Commitments & The Four Prohibitions

1. **The Freeze:** The analysis and reporting layers (`src/analyze/`, `src/report/`) must be tagged and frozen prior to human gold label generation.
2. **Physical Label Isolation:** Pre-annotations reside in `data/interim/preannotations/`; human gold labels reside in `data/raw/labels/` (AI agent has zero write permissions).
3. **No Peeking:** No agreement metrics or score distributions will be computed before gold annotation adjudication is complete.
4. **No Resampling:** Items will never be filtered, reordered, or re-weighted post hoc outside the recorded sampling frame.

---

## 9. Signatures & Registration Commitment

By signing below, the lead researcher commits this protocol as the official, frozen pre-registration for the NepFaith-120 research project prior to pipeline execution.

- **Lead Researcher:** Muskan Bhandari  
- **Signature:** `MB`  
- **Date:** 2026-10-15  
