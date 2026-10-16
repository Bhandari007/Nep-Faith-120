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

<!-- Agent records empirical progress, commands executed, and verified deliverables here -->

## Verdicts (researcher)

<!-- Researcher records verdicts with initials and date here -->

## Active Frontier Tickets

- [ ] [01 · Stratified Sampling & 120 Candidate Corpus Assembly](issues/01-stratified-sampling-120.md) (Cap: 1 day)
- [ ] [02 · Atomic Claim Decomposition & Criticality Tagging](issues/02-atomic-claim-decomposition.md) (Cap: 1 day)
- [ ] [03 · IndicTrans2 C2 Batch Translation Runner](issues/03-indictrans2-c2-batch-generation.md) (Cap: 1 day)
- [ ] [04 · Human Dual-Annotation Workbench & Tooling Setup](issues/04-annotation-workbench-setup.md) (Cap: 1 day)
- [ ] [05 · Condition C3 Human Post-Editing Workbench Setup](issues/05-c3-post-editing-workbench.md) (Cap: 1 day)
- [ ] [06 · Dual Human Annotation & Stopwatch Timing Intake](issues/06-dual-annotation-execution.md) (Cap: 14 days / Human Task ~8.5h)
- [ ] [07 · Adjudication Protocol & Gold Label Data Intake](issues/07-adjudication-and-gold-intake.md) (Cap: 2 days / Human Task)
- [ ] [08 · Gate 2 Verification & Data Lock](issues/08-gate-2-verification-and-lock.md) (Cap: 0.5 day)
