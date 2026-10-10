# Paper Section: 2. Related Work & Positioning

> **Status:** Seed Draft (Harvested from Tickets 01–04)  
> **Target Venue:** ACL / EMNLP / NAACL

---

## 1. RAG Faithfulness & Hallucination Evaluation
- **Monolingual & LLM-as-a-Judge:** RAGAS (Es et al., 2024), TruLens, DeepEval, and HHEM-2.1 (Vectara, 2024) evaluate faithfulness either strictly monolingually in English or via uncalibrated zero-shot prompt translation. They treat the evaluator as an unexamined instrument and do not isolate MT quality from scoring ability.
- **Multilingual Evaluator Transfer:** mFACT (Qiu et al., EMNLP 2023) transfers English factual consistency metrics to multilingual abstractive summarization via MT, but treats MT as a black-box transfer channel without decomposing $\Delta_{MT}$ from $\Delta_{XL}$, and completely excludes Nepali. ANHALTEN (Herrlein et al., ACL 2024) focuses on German token-level reference-free hallucination without reference grounding. CrossLinguaRAG (Sandesh et al., 2026) evaluates Kannada retrieval but does not evaluate faithfulness scoring pipelines.
- **NepFaith-120 Distinction:** Unlike prior works that either assume MT is harmful or ignore its contribution, we introduce a controlled post-edited MT oracle ($C3$) to causally isolate MT degradation from cross-lingual evaluation failure.

## 2. Symmetric NLI Transfer vs Asymmetric RAG Grounding
- **The Classical Debate:** Classic cross-lingual NLI (Conneau et al., 2018; Artetxe et al., 2020; Agrawal et al., EACL 2024) analyzes *Translate-Test* vs *Zero-Shot Cross-Lingual Transfer*.
- **Asymmetric Claim Grounding:** Classical NLI is strictly *symmetric* (premise and hypothesis are in the same language). In cross-lingual RAG, evaluation is inherently *asymmetric* (retrieved evidence in source language $L_{\text{src}}$, generated claim in target language $L_{\text{tgt}}$). Prior NLI work directly compares $A(\text{Translate-Test}) - A(\text{Zero-Shot})$, conflating MT errors with reasoning errors because no post-edited MT ceiling is employed.

## 3. Indic NLP & Low-Resource Benchmarking
- **Indic Pretraining & Evaluation Gaps:** While IndicTrans2 (Gala et al., 2023) covers 22 scheduled Indian languages including Nepali, Nepali remains omitted from cross-lingual NLI benchmarks (XNLI covers 15 languages, IndicXNLI covers 11 languages).
- **Recent Hallucination Benchmarks:** MultiWikiQHalluA (Thoresen & Smart, 2026) generates synthetic monolingual reading comprehension hallucinations, but truncated its release without evaluating or releasing models for Nepali. BHRAM-IL (Terdalkar et al., 2025) benchmarks generative QA hallucinations, not faithfulness scoring pipelines.

## 4. Prediction-Powered Inference (PPI) in NLP
- **Annotation Cost Reduction:** Angelopoulos et al. (Science 2023) formalized PPI, and Gao et al. (EMNLP 2026 / arXiv:2608.26638) demonstrated that neural metrics save 50%–80% of human annotation via Prediction-Powered Saving Ratios (PPSR). StratPPI (Fisch et al., NeurIPS 2024) demonstrated a $2\times$ sample efficiency gain in multilingual summarization.
- **NepFaith-120 Framing:** We do not claim PPI sample savings as our primary novelty. Instead, we employ cluster-robust stratified paired PPI as a rigorous statistical engine to project claim-level evaluations over 1,500 items while preserving valid coverage guarantees.
