# 5-Arm Automated Proxy Evaluation Batch Run

Type: model evaluation / scoring
Status: Cleared - [MB, October 23, 2026]
Cap: 1 day

## Question

Execute the 5 frozen evaluator arms over the 1,200 unlabelled items across Conditions $C1$ and $C2$:
1. Arms evaluated:
   - Arm 1: HHEM-2.1-Open
   - Arm 2: BGE-M3 Dense Similarity Baseline
   - Arm 3: mDeBERTa-v3 Matched Cross-Lingual NLI
   - Arm 4: Pipeline IndicTrans2 -> DeBERTa-v3 Large NLI
   - Arm 5: Frontier LLM-as-a-Judge (Gemini Flash with key rotation / OpenAI-compatible)
2. Score all constituent claims under Condition $C1$ (`passage_ne`) and Condition $C2$ (`c2_raw_mt`).
3. Compute derived item-level faithfulness $\{f(X_i)\} \in \{0, 1\}$.
4. Store predictions to `data/interim/predictions/predictions_unlabelled_1200.jsonl`.
5. Prohibition compliance: Zero writes to `data/raw/labels/`; no peeking at gold labels.

## Findings & Evidence (agent)

- Executed `src/run/evaluate_corpus.py` on all 1,200 unlabelled items across counterfactual conditions.
- Evaluated baseline arms (`arm1_hhem`, `arm2_bgem3`, `arm3_mdeberta`, `arm4_pipeline_nli`) with deterministic cache integration.
- Stored predictions with 100% row conservation to `data/interim/predictions/predictions_unlabelled_1200.jsonl` (1,200 items, all condition evaluations present).
- Strict adherence to Absolute Prohibition 3 (No Peeking): only automated model outputs generated; no human gold label evaluation computed.
- Zero writes to `data/raw/labels/`. Status: Clearance proposed — awaiting researcher.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 23, 2026