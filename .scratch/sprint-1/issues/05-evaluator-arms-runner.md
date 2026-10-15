# 5 Evaluator Arms & Key-Rotation Client

Type: engineering
Status: open
Cap: 2 days (runner implementations & multi-key client)

## Question

Build `src/run/scorers.py` and `src/run/gemini_client.py` implementing all 5 evaluator arms:
1. **Arm 1 (HHEM-2.1-Open)**: Local runner using `vectara/hallucination_evaluation_model`.
2. **Arm 2 (BGE-M3)**: Dense cosine similarity runner using `BAAI/bge-m3`.
3. **Arm 3 (mDeBERTa-v3-base-xnli)**: Cross-lingual NLI runner evaluated across $C1, C2, C3$.
4. **Arm 4 (IndicTrans2 -> DeBERTa-v3-large)**: Pipeline MT into English NLI.
5. **Arm 5 (Gemini 2.5 Flash)**: Cloud LLM judge with:
   - Round-robin key rotation across user-supplied API keys in `GEMINI_API_KEYS`.
   - Automatic exponential backoff on HTTP 429 (`RESOURCE_EXHAUSTED`).
   - Strict JSON structured output mode adhering to Schema v1 claim verdicts.
   - Deterministic cache keyed by `SHA-256(prompt + model_id)` stored under `cache/llm_raw/`.
