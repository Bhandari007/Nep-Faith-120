# Wayfinder Map: Sprint 1 Pipeline Build & Analysis Freeze (Gate 1)

## Destination

Clear **Gate 1** of NepFaith-120: Construct and verify the full engineering pipeline, validate recovery tests on planted synthetic effects, and freeze the analysis and reporting layers before any gold human labels exist.

Exit criteria:
1. Data preparation pipeline (`src/prepare/`) operational for corpus ingestion, generation, claim extraction, and 7 typed perturbations.
2. Translation runner (`src/run/translate.py`) operational for IndicTrans2-200M generating Condition $C2$.
3. 5 Evaluator Arms (`src/run/`) operational, including Gemini 2.5 Flash 10-key rotation runner with deterministic prompt caching.
4. Statistical engine (`src/analyze/estimators.py`) implements cluster-robust stratified paired PPI++ via GLIDE.
5. All recovery tests in `tests/recovery/` pass (verifying the estimator recovers planted effects).
6. Invariant tests in `tests/invariants/` pass (zero cross-condition leakage, strict row conservation).
7. **The Freeze Tag (`sprint-1-frozen`)** committed and tagged, locking `src/analyze/` and `src/report/`.

## Notes

- **Domain**: Automated RAG faithfulness evaluation pipeline, IndicTrans2 translation, 5 evaluator arms, Prediction-Powered Inference (PPI++).
- **Hard Rule**: No model output may ever write to `data/raw/labels/`. Pre-annotations go to `data/interim/preannotations/`.
- **Hard Rule**: `src/analyze/` and `src/report/` must freeze *before* human gold labels are annotated in Sprint 2.

## Findings (agent)

1. **Ingestion & Corpus Pipeline (`src/prepare/ingest.py`):**
   - Implemented NFC Unicode normalization, 8-bit Preeti/Kantipur transliteration, and multi-format PDF extraction with Gemini OCR fallback.
   - Seed corpus with sports quota (30% of news stratum) validated and saved to `data/derived/corpus_passages.jsonl`.
2. **Claim Extraction Engine (`src/prepare/claims.py`):**
   - Decomposes English answers into 2–5 atomic, decontextualized propositions adhering to `docs/RUBRIC_V1.md` with criticality labeling.
3. **7-Type Perturbation Engine (`src/prepare/perturb.py`):**
   - Built deterministic generators for the 7 negative categories: `entity_swap`, `number_date_alteration`, `negation_flip`, `misattribution`, `register_shift`, `unsupported_addition`, `invented_causality`.
4. **Local IndicTrans2 Translation Runner (`src/run/translate.py`):**
   - FP16 GPU runner with `ai4bharat/indictrans2-indic-en-dist-200M` (`npi_Deva` -> `eng_Latn`) with SHA-256 disk caching under `cache/translations/`.
5. **5 Evaluator Arms (`src/run/scorers.py`, `src/run/gemini_client.py`):**
   - Arm 1 (HHEM-2.1), Arm 2 (BGE-M3), Arm 3 (mDeBERTa-v3), Arm 4 (Pipeline NLI), Arm 5 (Gemini Flash judge).
   - Gemini rotator tested with 10 keys: 100% success (HTTP 200) with deterministic disk caching under `cache/llm_raw/` and `cache/scorers/`.
6. **Cluster-Robust Stratified PPI++ Engine (`src/analyze/estimators.py`):**
   - Huber-White sandwich variance clustered by `item_id`, adaptive $\lambda^*$ tuning with finite-sample variance protection, stratum weighting, and paired difference $(C2 - C1)$ covariance cancellation.
7. **Monte Carlo Planted Effect Recovery Simulation (`tests/recovery/test_ppi_recovery.py`):**
   - 100 trials with planted gap $\Delta^* = 0.1200$: Mean recovered delta $= 0.1178$ (bias: $0.0022$), empirical 95% CI coverage $= 95.0\%$, mean PPSR $= 1.730\times$.
8. **Invariants & Full Test Suite:**
   - 28/28 tests passing across `tests/` in 3.35s. Zero writes to `data/raw/labels/`.
   - Arm 5 configurable frontier judge (`Arm5LLMJudge`) operational for Gemini rotation and OpenAI-compatible endpoints with cache isolation.
   - All 8 issues in Sprint 1 cleared by researcher.

## Verdicts (researcher)

2026-10-16 · Sprint 1 pipeline, estimators, and recovery benchmarks verified. Invariant tests and Monte Carlo recovery pass. Arm 5 configurable interface approved for frontier/OSS models. Gate 1 cleared for freeze. — MB

## Active Frontier Tickets

- [x] [01 · Corpus Ingestion & Passages Pipeline](issues/01-corpus-ingestion.md) (Cap: 1 day)
- [x] [02 · Claim Decomposition & Extraction Engine](issues/02-claim-decomposition.md) (Cap: 1 day)
- [x] [03 · 7-Type Perturbation Engine](issues/03-perturbation-engine.md) (Cap: 2 days)
- [x] [04 · IndicTrans2 Local Translation Runner](issues/04-indictrans2-runner.md) (Cap: 1 day)
- [x] [05 · 5 Evaluator Arms & Key-Rotation Client](issues/05-evaluator-arms-runner.md) (Cap: 2 days)
- [x] [06 · Cluster-Robust Stratified PPI++ Engine](issues/06-ppi-statistical-engine.md) (Cap: 2 days)
- [x] [07 · Planted Effect Recovery Simulation Tests](issues/07-recovery-tests.md) (Cap: 1 day)
- [x] [08 · Freeze Tag Gate 1 Verification](issues/08-freeze-gate-1.md) (Cap: 0.5 day)
