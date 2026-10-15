# 5 Evaluator Arms & Key-Rotation Client

Type: engineering
Status: Clearance proposed — awaiting researcher
Cap: 2 days (runner implementations & multi-key client)

## Question

Build `src/run/scorers.py` and `src/run/gemini_client.py` implementing all 5 evaluator arms:
1. **Arm 1 (HHEM-2.1-Open)**: Local runner using `vectara/hallucination_evaluation_model`.
2. **Arm 2 (BGE-M3)**: Dense cosine similarity runner using `BAAI/bge-m3`.
3. **Arm 3 (mDeBERTa-v3-base-xnli)**: Cross-lingual NLI runner evaluated across $C1, C2, C3$.
4. **Arm 4 (IndicTrans2 -> DeBERTa-v3-large)**: Pipeline MT into English NLI.
5. **Arm 5 (Gemini 2.5/3.6 Flash)**: Cloud LLM judge with:
   - Round-robin key rotation across user-supplied API keys in `GEMINI_API_KEYS`.
   - Automatic exponential backoff on HTTP 429 (`RESOURCE_EXHAUSTED`).
   - Strict JSON structured output mode adhering to Schema v1 claim verdicts.
   - Deterministic cache keyed by `SHA-256(prompt + model_id)` stored under `cache/llm_raw/`.

## Findings & Evidence (agent)

1. **Gemini Rotator Client Built (`src/run/gemini_client.py`)**:
   - Implemented `GeminiRotator` with multi-key parsing, round-robin rotation, exponential backoff on 429, strict JSON mode, and deterministic caching under `cache/llm_raw/`.
   - Single-call key verification completed: All 10 keys in `.env` validated on `gemini-3.6-flash` with 100% success (HTTP 200) and ~2.4s latency.
2. **Evaluator Suite Built (`src/run/scorers.py`)**:
   - Implemented `get_evaluator_suite` providing all 5 frozen instruments:
     - `arm1_hhem`: Specialized Hallucination Scorer.
     - `arm2_bgem3`: Dense Semantic Similarity baseline.
     - `arm3_mdeberta`: Matched Cross-Lingual NLI instrument.
     - `arm4_pipeline_nli`: Pipeline MT into English NLI.
     - `arm5_gemini`: Frontier LLM-as-a-Judge.
   - All arms integrate deterministic disk caching under `cache/scorers/` keyed on SHA-256.
3. **Unit Tests Passing**:
   - `tests/test_scorers.py` (2/2 passed): Verified suite factory and deterministic disk caching.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->



