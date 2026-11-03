# Wayfinder Map: Sprint 4 Unblinded Statistical Estimation, Tables, & Manuscript Empirical Integration

## Destination

Execute the unblinded Prediction-Powered Inference (PPI++) analysis of NepFaith-120 combining the locked gold human labels ($n=120$) and large unlabelled inference predictions ($N=1,200$), generate verified publication LaTeX tables (Table 1 & Table 2), compute subgroup sensitivities and sample efficiency metrics (PPSR), and integrate empirical findings into the paper notes and draft dossier adhering to the 6-question paper gate.

Exit criteria:
1. Complete unblinded execution of `src/run/run_analysis_pipeline.py` using official gold labels from `data/raw/labels/gold_labels_120.jsonl`.
2. Output verified publication-ready LaTeX tables (`Table 1: Decomposition`, `Table 2: 7-Type Sensitivity`) into `reports/` and `outputs/`.
3. Verify PPSR ($> 1.0$) confirming empirical human annotation savings through unlabelled proxy controls.
4. Pass all recovery, invariant, and unit tests without modifying frozen layers (`src/analyze/`, `src/report/`).
5. Zero write operations to `data/raw/labels/`.
6. Integrate verified numerical claims into `paper/notes/` and draft empirical updates for `paper/dossier/03-methodology.md` and `04-statistical-framework.md`.

## Notes & Standing Rules

- **Domain**: Prediction-Powered Inference (PPI++), Cross-Lingual RAG, Translation Error Decomposition, Publication Tables.
- **Absolute Prohibition 1 (The Freeze)**: `src/analyze/` and `src/report/` remain frozen under `sprint-1-frozen`. Session startup diffs must show zero changes.
- **Absolute Prohibition 2 (Gold Labels)**: The AI agent has **zero write permissions** to `data/raw/labels/`.
- **Absolute Prohibition 3 (No Peeking - LIFTED for Sprint 4)**: Official gold labels are cleared and unblinded. Analysis outputs and agreement metrics may now be computed and reported.
- **Absolute Prohibition 4 (No Resampling)**: Stratification and evaluation frame are strictly fixed.

## Findings (agent)

- 2026-10-31 · [T01 · Unblinded Pipeline Execution & Gold Ingestion](issues/01-unblinded-pipeline-execution.md): Ingested locked gold dataset (`data/raw/labels/gold_labels_120.jsonl`, 120 items). Verified 100% item matching. Implemented `run_pipeline_with_stamping` and empirical sensitivity matrix computation in `src/run/run_analysis_pipeline.py`. Stamped output record to `outputs/run_summary_20261031_032903.json`. 62/62 tests pass. Freeze check clean (0 diff). Zero writes to `data/raw/labels/`. Status: Clearance proposed.
- 2026-10-31 · [T02 · Publication LaTeX Tables & Figures](issues/02-publication-tables-and-figures.md): Formatted publication LaTeX tables (`reports/table1_decomposition.tex` and `reports/table2_sensitivity.tex`) with booktabs formatting. 100% verified syntax and reproducibility metadata. Status: Clearance proposed.
- 2026-10-31 · [T03 · Subgroup Sensitivity & PPSR Efficiency Audit](issues/03-subgroup-sensitivity-and-ppsr.md): Computed domain-stratified estimates across Wikipedia, Government Reports, and News ($n=40, N=400$ each, mean 60.0%, SE 0.0784). Verified 12-item sports quota (6 faithful / 6 unfaithful). Recorded empirical detection rates across 7 perturbation types. Status: Clearance proposed.
- 2026-10-31 · [T04 · Manuscript Empirical Integration & Paper Gate Clearance](issues/04-manuscript-empirical-integration.md): Successfully passed 6-question paper gate. Staged unblinded empirical results into `paper/notes/06-unblinded-empirical-results.md`. Status: Clearance proposed — awaiting researcher verdict.
- 2026-11-01 · [T05 · Arm 5 Frontier LLM Judge (Gemini-3.6-Flash) Evaluation Run](issues/05-arm5-gemini-evaluation.md): Re-aligned with ADR 0002 (`gemini-3.6-flash`), active 10-key rotation pool restored. Unit tests pass (65/65). Implemented atomic persistence. Evaluated items 1–30 on candidates (145 claims cached under `gemini-3.6-flash`). Paused awaiting daily quota reset.
- 2026-11-02 · [T05 · Arm 5 Frontier LLM Judge (Gemini-3.6-Flash) Evaluation Run](issues/05-arm5-gemini-evaluation.md): Resumed run. Upgraded per-item atomic checkpointing. Evaluated items 31–56 on candidates (328 claims cached). All 10 keys reached daily free-tier limit. Progress safely checkpointed to `predictions_candidates_120.jsonl` (56/120 candidate items complete). Next run resumes from item 57. Zero diff on frozen layers; zero writes to `data/raw/labels/`. Status: In Progress — Paused for Quota Reset.
- 2026-11-03 · [T05 · Arm 5 Frontier LLM Judge (Gemini-3.6-Flash) Evaluation Run](issues/05-arm5-gemini-evaluation.md): Resumed run. Integrated TDD request tracking and progress bar. Evaluated items 57–81 on candidates (455 claims cached, 125 successful API calls dispatched across 10 keys). Progress safely checkpointed (81/120 candidate items complete, 67.5%). All 10 keys reached daily free-tier limit. Next run resumes from item 82. Freeze check clean (0 diff); zero writes to `data/raw/labels/`. Status: In Progress — Paused for Quota Reset.

## Verdicts (researcher)

- 2026-10-31 · [T01 · Unblinded Pipeline Execution & Gold Ingestion](issues/01-unblinded-pipeline-execution.md): Cleared — MB
- 2026-10-31 · [T02 · Publication LaTeX Tables & Figures](issues/02-publication-tables-and-figures.md): Cleared — MB
- 2026-10-31 · [T03 · Subgroup Sensitivity & PPSR Efficiency Audit](issues/03-subgroup-sensitivity-and-ppsr.md): Cleared — MB
- 2026-10-31 · [T04 · Manuscript Empirical Integration & Paper Gate Clearance](issues/04-manuscript-empirical-integration.md): Cleared — MB

## Active Frontier Tickets

- [x] [01 · Unblinded Pipeline Execution & Gold Ingestion](issues/01-unblinded-pipeline-execution.md) (Cleared — MB)
- [x] [02 · Publication LaTeX Tables & Figures](issues/02-publication-tables-and-figures.md) (Cleared — MB)
- [x] [03 · Subgroup Sensitivity & PPSR Efficiency Audit](issues/03-subgroup-sensitivity-and-ppsr.md) (Cleared — MB)
- [x] [04 · Manuscript Empirical Integration & Paper Gate Clearance](issues/04-manuscript-empirical-integration.md) (Cleared — MB)
- [ ] [05 · Arm 5 Frontier LLM Judge (Gemini-3.6-Flash) Evaluation Run](issues/05-arm5-gemini-evaluation.md) (Active — In Progress)




