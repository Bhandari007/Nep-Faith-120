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

<!-- Agent records engineering findings, test run outputs, and benchmarks here -->

## Verdicts (researcher)

<!-- Researcher records verdicts with initials and date here -->

## Active Frontier Tickets

- [ ] [01 · Corpus Ingestion & Passages Pipeline](issues/01-corpus-ingestion.md) (Cap: 1 day)
- [ ] [02 · Claim Decomposition & Extraction Engine](issues/02-claim-decomposition.md) (Cap: 1 day)
- [ ] [03 · 7-Type Perturbation Engine](issues/03-perturbation-engine.md) (Cap: 2 days)
- [ ] [04 · IndicTrans2 Local Translation Runner](issues/04-indictrans2-runner.md) (Cap: 1 day)
- [ ] [05 · 5 Evaluator Arms & Key-Rotation Client](issues/05-evaluator-arms-runner.md) (Cap: 2 days)
- [ ] [06 · Cluster-Robust Stratified PPI++ Engine](issues/06-ppi-statistical-engine.md) (Cap: 2 days)
- [ ] [07 · Planted Effect Recovery Simulation Tests](issues/07-recovery-tests.md) (Cap: 1 day)
- [ ] [08 · Freeze Tag Gate 1 Verification](issues/08-freeze-gate-1.md) (Cap: 0.5 day)
