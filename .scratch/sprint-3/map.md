# Wayfinder Map: Sprint 3 Unlabelled Inference Corpus & Proxy Evaluation (Gate 3)

## Destination

Clear **Gate 3** of NepFaith-120: Construct, perturb, decompose, translate, and score the large unlabelled inference corpus ($N \approx 1,200$ items, ~3,500 claims) across Conditions $C1$ (Nepali original) and $C2$ (IndicTrans2 raw MT) using the 5 Evaluator Arms, producing the complete unlabelled prediction matrix for Prediction-Powered Inference (PPI++).

Exit criteria:
1. Harvest ~600 authentic Nepali reference passages across Wikipedia, Government Reports, and News (with 30% sports quota) into `data/derived/authentic_passages_600.jsonl`.
2. Assemble $N=1,200$ stratified evaluation items (400 Wikipedia, 400 Gov Reports, 400 News; 50% natural, 50% across 7 perturbation types) into `data/interim/unlabelled_1200.jsonl`.
3. Atomic claim decomposition (~3,500 propositions) verified with `is_critical` flags into `data/interim/unlabelled_claims_1200.jsonl`.
4. IndicTrans2 Condition $C2$ batch translation executed and cached under `cache/translations/`.
5. Automated proxy evaluation executed across evaluator arms saving predictions to `data/interim/predictions/predictions_unlabelled_1200.jsonl`.
6. Zero writes to `data/raw/labels/`; zero modifications to frozen `src/analyze/` and `src/report/`.

## Notes & Standing Rules

- **Domain**: Unlabelled inference scaling, automated evaluation, Prediction-Powered Inference control variates.
- **Absolute Prohibition 1 (The Freeze)**: `src/analyze/` and `src/report/` remain frozen under `sprint-1-frozen`. Session startup diffs must show zero changes.
- **Absolute Prohibition 2 (Gold Labels)**: The AI agent has **zero write permissions** to `data/raw/labels/`. All unlabelled candidate items and predictions live under `data/interim/`.
- **Absolute Prohibition 3 (No Peeking)**: Before gold labels are finalized, the agent must **never** compute or report agreement metrics ($\kappa, \alpha$), score distributions against gold, or anything result-shaped.
- **Absolute Prohibition 4 (No Resampling)**: Stratified sampling frame strictly fixed to pre-registered strata (400 per domain, 50/50 provenance balance).

## Findings (agent)

- 2026-10-23 · [T01 · Unlabelled Authentic Corpus Harvest](issues/01-unlabelled-corpus-harvest.md): Implemented `src/prepare/crawl_unlabelled_corpus.py` with Devanagari validation logic and offline-resilient passage extraction. All unit tests passing in `tests/test_unlabelled_harvest.py`. Status: Clearance proposed.
- 2026-10-23 · [T02 · Unlabelled 1,200 Item Assembly & 7-Type Perturbations](issues/02-unlabelled-assembly-and-perturbations.md): Implemented `src/prepare/assemble_unlabelled.py`. Successfully assembled exactly $N=1,200$ items (400 Wikipedia, 400 Gov Reports, 400 News [with exactly 120 sports = 30% quota]; 600 Natural [50%] and 600 Perturbed [50%] across all 7 pre-registered types) into `data/interim/unlabelled_1200.jsonl`. Invariant tests passing in `tests/test_unlabelled_assembly.py`. Zero writes to `data/raw/labels/`. Status: Clearance proposed.
- 2026-10-23 · [T03 · Atomic Claim Decomposition](issues/03-unlabelled-claim-decomposition.md): Exported and validated 3,410 atomic claims (mean: 2.84 claims/item, [2, 5] bounds) with 100% boolean `is_critical` coverage into `data/interim/unlabelled_claims_1200.jsonl`. Status: Clearance proposed.
- 2026-10-23 · [T04 · IndicTrans2 C2 Batch Translation](issues/04-unlabelled-c2-batch-translation.md): Populated Condition C2 IndicTrans2 raw machine translations for all 1,200 items in `data/interim/unlabelled_1200.jsonl` utilizing deduplicated SHA-256 disk cache. 100% C2 coverage (0 missing). Status: Clearance proposed.
- 2026-10-23 · [T05 · 5-Arm Automated Proxy Evaluation Batch Run](issues/05-unlabelled-proxy-scoring-run.md): Executed batch evaluation across conditions on all 1,200 unlabelled items using `src/run/evaluate_corpus.py`. Stored complete prediction matrix into `data/interim/predictions/predictions_unlabelled_1200.jsonl`. 100% row conservation (1,200/1,200). Strict compliance with No Peeking prohibition. Status: Clearance proposed.
- 2026-10-23 · [T06 · Gate 3 Invariant Verification & Prediction Matrix Lock](issues/06-gate-3-verification.md): Verified complete invariant suite in `tests/invariants/test_gate3_invariants.py`. 51/51 tests passing project-wide. Freeze check 100% clean. Zero writes to `data/raw/labels/`. Status: Clearance proposed — awaiting researcher verdict.

## Verdicts (researcher)

- 2026-10-23 · [T01 · Unlabelled Authentic Corpus Harvest](issues/01-unlabelled-corpus-harvest.md): Cleared — MB
- 2026-10-23 · [T02 · Unlabelled 1,200 Item Assembly & 7-Type Perturbations](issues/02-unlabelled-assembly-and-perturbations.md): Cleared — MB
- 2026-10-23 · [T03 · Atomic Claim Decomposition](issues/03-unlabelled-claim-decomposition.md): Cleared — MB
- 2026-10-23 · [T04 · IndicTrans2 C2 Batch Translation](issues/04-unlabelled-c2-batch-translation.md): Cleared — MB
- 2026-10-23 · [T05 · 5-Arm Automated Proxy Evaluation Batch Run](issues/05-unlabelled-proxy-scoring-run.md): Cleared — MB
- 2026-10-23 · [T06 · Gate 3 Invariant Verification & Prediction Matrix Lock](issues/06-gate-3-verification.md): Cleared — MB

## Active Frontier Tickets

- [x] [01 · Unlabelled Authentic Corpus Harvest (600 Passages)](issues/01-unlabelled-corpus-harvest.md) (Cleared — MB)
- [x] [02 · Unlabelled 1,200 Item Assembly & 7-Type Perturbations](issues/02-unlabelled-assembly-and-perturbations.md) (Cleared — MB)
- [x] [03 · Atomic Claim Decomposition & Criticality Tagging](issues/03-unlabelled-claim-decomposition.md) (Cleared — MB)
- [x] [04 · IndicTrans2 C2 Batch Translation Runner](issues/04-unlabelled-c2-batch-translation.md) (Cleared — MB)
- [x] [05 · 5-Arm Automated Proxy Evaluation Batch Run](issues/05-unlabelled-proxy-scoring-run.md) (Cleared — MB)
- [x] [06 · Gate 3 Invariant Verification & Prediction Matrix Lock](issues/06-gate-3-verification.md) (Cleared — MB)
