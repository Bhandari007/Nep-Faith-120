# Paper Section: 1. Introduction & Motivation

> **Status:** Seed Draft (Living Section)  
> **Target Venue:** ACL / EMNLP / NAACL (4-page short paper format)

---

## 1. The Real-World Dilemma
In Retrieval-Augmented Generation (RAG) for low-resource or non-English contexts, systems frequently retrieve local-language documents (e.g. Nepali) to answer queries in a high-resource language (e.g. English). Evaluating whether the generated answer is faithful to the retrieved passage poses a fundamental architectural dilemma:
1. **Direct Cross-Lingual Evaluation ($C1$):** Pass the original Nepali context and English answer directly to a cross-lingual evaluator (e.g. mDeBERTa, LLM-as-a-judge).
2. **Translate-then-Evaluate ($C2$):** Translate the Nepali context to English via Machine Translation (IndicTrans2) and evaluate monolingually in English.

Conventional wisdom in NLP assumes machine translation introduces fatal semantic drift. However, cross-lingual evaluators themselves struggle with cross-lingual entailment judgment, especially on low-resource scripts like Devanagari.

## 2. The Core Scientific Question
Does cross-lingual faithfulness evaluation fail because machine translation distorts the source context ($\Delta_{MT}$), or because the evaluator fails at cross-lingual alignment and entailment ($\Delta_{XL}$)?

## 3. The Causal Decomposition Framework
To isolate these two error sources cleanly, we introduce a counterfactual human post-edited machine translation ceiling ($C3$):
- **$\Delta_{MT} = A(C3) - A(C2)$**: The accuracy penalty attributable strictly to machine translation noise.
- **$\Delta_{XL} = A(C3) - A(C1)$**: The accuracy penalty attributable strictly to cross-lingual evaluation.

**Primary Hypothesis ($H1$):** $\Delta_{XL} > \Delta_{MT}$ — The primary bottleneck in cross-lingual RAG evaluation is the evaluator's cross-lingual entailment failure, not translation error.

## 4. Why Nepali (`ne` / Devanagari)?
Nepali represents a critical low-resource stress-test:
- Present in multilingual pretraining (CC100), but **completely excluded** from standard NLI fine-tuning benchmarks (XNLI covers 15 languages, excluding Nepali; IndicXNLI covers 11 Indic languages, also excluding Nepali).
- Written in Devanagari with complex morphology, honorifics, and split-ergativity.
- If cross-lingual evaluation is worse than machine translation even in a language where MT has noticeable error rates, it definitively proves that cross-lingual semantic judgment is the overriding bottleneck.

## 5. Summary of Contributions
1. **The First Causal Error Decomposition:** Formal decoupling of MT error ($\Delta_{MT}$) vs cross-lingual evaluator alignment error ($\Delta_{XL}$) via a human post-edited MT ceiling ($C3$).
2. **The NepFaith-120 Benchmark:** A claim-level, human-adjudicated benchmark of 120 items with 7 typed perturbation edits (attribution, register, numbers, causal links) and consensus gold labels.
3. **Prediction-Powered Scaling:** Scaling rigorous statistical confidence intervals over $\sim 1,500$ items using cluster-robust stratified paired PPI (via GLIDE).
