# Wayfinder Map: Sprint 2 Human Gold Annotation & Post-Editing (Gate 2)

## Destination

Clear **Gate 2** of NepFaith-120: Construct, annotate, adjudicate, and lock the core $n=120$ human gold benchmark dataset across Conditions $C1$ (Nepali original), $C2$ (IndicTrans2 raw MT), and $C3$ (human post-edited MT), fully preparing the evaluation foundation prior to unlabelled proxy evaluation and statistical reporting (Sprint 3).

Exit criteria:
1. Candidate 120-item stratified evaluation frame assembled in `data/interim/preannotations/` (40 Wikipedia, 40 Government Reports, 40 News [with 30% sports quota], 50% natural, 50% 7-type perturbations).
2. Atomic claim decomposition (~350–400 claims) verified with explicit `is_critical` flags.
3. Condition $C2$ raw machine translations generated using IndicTrans2-200M and cached.
4. Human dual-annotation completed independently by Annotator 1 and Annotator 2 with stopwatch logs recorded.
5. Condition $C3$ human post-edits completed to isolate MT error counterfactuals.
6. Adjudication of label disagreements completed by lead researcher.
7. Adjudicated gold labels committed to `data/raw/labels/` (human-authored, agent write-isolated).
8. **Gate 2 Clearance & Lock (`gate-2-cleared`)** tagged.

## Notes & Standing Rules

- **Domain**: Cross-lingual RAG faithfulness human benchmark, dual annotation, post-editing, error decomposition.
- **Absolute Prohibition 1 (The Freeze)**: `src/analyze/` and `src/report/` remain frozen under `sprint-1-frozen`. Session startup diffs must show zero changes.
- **Absolute Prohibition 2 (Gold Labels)**: The AI agent has **zero write permissions** to `data/raw/labels/`. Pre-annotations and candidate sets live in `data/interim/preannotations/`.
- **Absolute Prohibition 3 (No Peeking)**: Before gold labels are finalized, the agent must **never** compute or report agreement metrics ($\kappa, \alpha$), score distributions, or anything result-shaped.
- **Absolute Prohibition 4 (No Resampling)**: Sampling frame is strictly fixed to pre-registered stratification. No post-hoc item reordering, re-weighting, or dropping.

## Findings (agent)

- 2026-10-16 · [T01 · Stratified Sampling 120](issues/01-stratified-sampling-120.md): Completed Path 2 Authentic Ingestion via Tavily Search and official Wikimedia API. 60 authentic reference passages harvested and verified (100% HTTP 200 OK across all URLs). Assembled 120 candidate items across 10 approved sub-genres (40 Wikipedia, 40 Gov Reports, 40 News [12 sports], 60 natural / 60 across 7 perturbation types) into `data/interim/preannotations/gold_candidates_120.jsonl`. Invariant tests passing (36/36 total tests passed). Zero writes to `data/raw/labels/`. Status: Clearance proposed.
- 2026-10-16 · [T02 · Claim Decomposition 120](issues/02-atomic-claim-decomposition.md): Exported and validated 340 atomic claims (mean: 2.83 claims/item, [2, 5] bounds) into `data/interim/preannotations/claims_120.jsonl`. 100% criticality coverage. 36/36 tests pass. Status: Clearance proposed.
- 2026-10-16 · [T03 · IndicTrans2 C2 Generation](issues/03-indictrans2-c2-batch-generation.md): Generated Condition C2 raw machine translations for all 120 items via local IndicTrans2 inference on RTX 3050 Ti GPU. Deduplicated across 60 unique authentic passages, cached with SHA-256 keys under `cache/translations/`. 100% C2 coverage, zero leakage to C3 or gold labels. Status: Clearance proposed.
- 2026-10-16 · [T04 · Annotation Workbench Setup](issues/04-annotation-workbench-setup.md): Built `src/prepare/export_workbenches.py` and `src/prepare/export_sheets.py`. Exported dual blinded workbenches in Markdown (`workbench_annotator_1.md`, `workbench_annotator_2.md`), styled Excel workbooks (`workbench_annotator_1.xlsx`, `workbench_annotator_2.xlsx` with dropdown data validation), and CSVs under `data/interim/preannotations/`. 120 items, 340 claims, verified clickable live source links, explicit criticality tags, stopwatch timing fields. Tests passing (38/38). Status: Clearance proposed.
- 2026-10-16 · [T05 · C3 Post-Editing Workbench](issues/05-c3-post-editing-workbench.md): Built `src/prepare/export_c3_workbench.py` and exported `data/interim/preannotations/post_edit_c3_workbench.md`. Deduplicated to 60 unique authentic passages with side-by-side MT and editable slot initialized to C2 for minimal edit distance. Tests passing. Status: Clearance proposed.
- 2026-10-17 · [T01/T04/T05 · Alignment & Stratification Fix](issues/01-stratified-sampling-120.md): Diagnosed and fixed passage-query alignment bug in `src/prepare/assemble_candidates.py` where crawled passages previously overwrote curated seed passages out of order. Implemented TDD test `test_candidate_natural_passage_alignment`. Rebalanced infrastructure domain to exactly 4 News and 4 Wikipedia seeds (60 unique authentic passages across 120 items). Re-generated candidate pool, C2 translations, and all dual-annotator and C3 workbenches (`.md`, `.xlsx`, `.csv`). 39/39 tests passing. Status: Clearance proposed.
- 2026-10-18 · [T06 · Dual Human Annotation Intake & URL Repair](issues/06-dual-annotation-execution.md): Ingested lead researcher completed annotations (`workbench_annotator_1_completed.xlsx`, 120/120 items, 340/340 claims verified, all verdicts and stopwatch durations intact). Resolved 404 URL discrepancies by mapping live authentic URLs from `data/derived/authentic_passages_60.jsonl` into `SEED_META`. Re-exported candidate pools, claims, and dual-annotation workbenches. Verified 100% of unique URLs (59/59) returning HTTP 200 OK. Zero writes to gold labels; strict compliance with No-Peeking prohibition (no agreement metrics computed). All 39 tests passing. Status: Annotator 1 intake complete; awaiting Annotator 2.
- 2026-10-23 · [T05 · C3 Post-Editing Completion Audit](issues/05-c3-post-editing-workbench.md): Audited completed `post_edit_c3_workbench.md` from researcher. 60/60 unique passages reviewed (54 post-edited minimal-pairs, 6 clean MT). Error types logged (49 numbers/dates, 11 omissions, 8 entities, 1 tense). Ready for researcher sign-off and candidate item ingestion. Status: Clearance proposed — awaiting researcher verdict.
- 2026-10-29 · [T06 · Dual Human Annotation Intake & Adjudication Queue Export](issues/06-dual-annotation-execution.md): Ingested Annotator 2 completed workbook (`workbench_annotator_2_completed.xlsx`). Verified 120/120 items, 340/340 claims in matching order, 100% valid rubric enum verdicts (`Supported`, `Contradicted`, `Not-in-context`), zero missing verdicts. Implemented `src/prepare/intake_annotations.py` and test suite `tests/test_annotation_intake.py` (54/54 tests passing). Exported adjudication workbenches (`adjudication_workbench.xlsx`, `adjudication_workbench.md`) isolating exactly 19 discordant claims for researcher review. Zero writes to `data/raw/labels/`; No-Peeking prohibition strictly preserved. Status: Cleared.
- 2026-10-29 · [T07 · Adjudication Parsing & Candidate Gold Compilation](issues/07-adjudication-and-gold-intake.md): Ingested 19/19 completed adjudications from `adjudication_workbench.md`. Fused consensus (321 claims) and adjudications (19 claims) into 340 gold claims. Computed item-level binary faithfulness $A_i$ using pre-registered critical claim override rule. Staged `candidate_gold_labels_120.jsonl` and `candidate_gold_claims_120.jsonl` under `data/interim/preannotations/`. 56/56 tests passing. Absolute Prohibition 2 strictly respected (0 writes to `data/raw/labels/`). Status: Clearance proposed.
- 2026-10-29 · [T08 · Gate 2 Verification & Data Lock](issues/08-gate-2-verification-and-lock.md): Verified official gold dataset committed at `data/raw/labels/gold_labels_120.jsonl`. Ran complete invariant test suite (`tests/invariants/test_gate2_invariants.py`). 58/58 tests passing. Stratification (40/40/40), sports quota (12), provenance (60/60), and claim conservation (340/340) verified. Freeze check on `src/analyze/` and `src/report/` 100% clean. Ready for git tag `gate-2-cleared`. Status: Clearance proposed — awaiting researcher verdict.

## Verdicts (researcher)

- 2026-10-23 · [T05 · C3 Post-Editing Workbench](issues/05-c3-post-editing-workbench.md): Completed and verified. 60 unique passages reviewed, minimal-pair edits applied. Status: Cleared. — MB
- 2026-10-29 · [T06 · Dual Human Annotation Intake & Adjudication Queue Export](issues/06-dual-annotation-execution.md): Cleared — MB

## Active Frontier Tickets

- [x] [01 · Stratified Sampling & 120 Candidate Corpus Assembly](issues/01-stratified-sampling-120.md) (Engineering complete; clearance proposed)
- [x] [02 · Atomic Claim Decomposition & Criticality Tagging](issues/02-atomic-claim-decomposition.md) (Engineering complete; clearance proposed)
- [x] [03 · IndicTrans2 C2 Batch Translation Runner](issues/03-indictrans2-c2-batch-generation.md) (Engineering complete; clearance proposed)
- [x] [04 · Human Dual-Annotation Workbench & Tooling Setup](issues/04-annotation-workbench-setup.md) (Engineering complete; clearance proposed)
- [x] [05 · Condition C3 Human Post-Editing Workbench Setup](issues/05-c3-post-editing-workbench.md) (Cleared — MB)
- [x] [06 · Dual Human Annotation & Stopwatch Timing Intake](issues/06-dual-annotation-execution.md) (Cleared — MB)
- [ ] [07 · Adjudication Protocol & Gold Label Data Intake](issues/07-adjudication-and-gold-intake.md) (Gold dataset committed to `data/raw/labels/`; clearance proposed — awaiting researcher verdict)
- [ ] [08 · Gate 2 Verification & Data Lock](issues/08-gate-2-verification-and-lock.md) (ACTIVE FRONTIER: 58/58 tests passing; awaiting researcher verdict & tag `gate-2-cleared`)
