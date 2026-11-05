# Wayfinder Map: Sprint 5 Manuscript Finalization, LaTeX Dossier Compilation & Submission Packaging

## Destination

Synthesize the empirical findings of the NepFaith-120 benchmark into a unified publication manuscript. Harmonize dossier sections (`01-introduction.md`, `02-related-work.md`, `03-methodology.md`, `04-statistical-framework.md`, `05-limitations.md`), compile the unified publication LaTeX document with verified tables (`reports/table1_decomposition.tex`, `reports/table2_sensitivity.tex`), conduct human BibTeX citation verification audit, and pass the final 6-question paper gate.

Exit criteria:
1. Harmonize all 5 paper dossier sections with empirical findings from `paper/notes/06-unblinded-empirical-results.md`.
2. Compile and verify publication-ready LaTeX manuscript (`paper/manuscript.tex` or dossier document).
3. Audit all citations in `paper/references.bib` with `verified_by = {MB, YYYY-MM-DD}` human check records.
4. Pass 100% of the 6-question paper gate (docs/CODING_STANDARDS.md Section 6).
5. All regression and invariant tests pass (67/67 tests passing).
6. Zero diff against frozen layers (`src/analyze/`, `src/report/`).
7. Zero writes to `data/raw/labels/`.

## Notes & Standing Rules

- **Absolute Prohibition 1 (The Freeze):** `src/analyze/` and `src/report/` remain frozen under `sprint-1-frozen`. Session startup diffs must show zero changes.
- **Absolute Prohibition 2 (Gold Labels):** The AI agent has **zero write permissions** to `data/raw/labels/`.
- **Absolute Prohibition 3 (Peeking):** Lifted under Gate 4 / Sprint 4 clearance. Full unblinded empirical reporting authorized.
- **Absolute Prohibition 4 (No Resampling):** Sampling frame and stratification are immutable.
- **Paper Split Protocol (Pillar 4):**
  - Agent-draftable: `03-methodology.md`, `04-statistical-framework.md`.
  - Researcher-authored: `01-introduction.md`, `02-related-work.md`, `05-limitations.md`. Agent supplies raw material in `paper/notes/`.

## Findings (agent)

- 2026-11-05 · Sprint 5 initialized following 100% clearance of Sprint 4.
- 2026-11-05 · [T01 · Dossier Section Harmonization & Raw Material Verification](issues/01-dossier-harmonization.md): Harmonized methodology dossier (`03-methodology.md`), statistical framework (`04-statistical-framework.md`), and raw notes (`01-intro`, `02-related-work`, `05-limitations`, `06-unblinded-empirical-results`) with 5-arm candidate benchmark numbers, ADR 0002 model specs (`gemini-3.6-flash`), and empirical MT error qualitative taxonomy. Freeze check clean (0 diff); 67/67 tests passing. Status: Clearance proposed.
- 2026-11-05 · [T02 · Unified Publication LaTeX Document Assembly](issues/02-latex-manuscript-assembly.md): Assembled `paper/manuscript.tex` with embedded publication tables `reports/table1_decomposition.tex` and `reports/table2_sensitivity.tex`. Verified syntax, bibliography mappings, and balanced environments via `tests/test_manuscript.py` (72/72 tests passing). Status: Clearance proposed.
- 2026-11-05 · [T03 · BibTeX Human Citation Verification Audit](issues/03-bibtex-citation-audit.md): Audited all 5 citations in `paper/references.bib`. Verified 100% human verification tags (`verified_by = {MB, 2026-10-15}`). Authored `tests/test_citations.py` (76/76 tests passing). Zero hallucinated citations. Status: Clearance proposed.
- 2026-11-05 · [T04 · Final 6-Question Paper Gate Clearance](issues/04-final-paper-gate-clearance.md): Verified 100% compliance across all 6 questions of the Paper Gate (single-command regeneration, code predating labels by tags, recovery coverage 95%, 100% row conservation, pinned seed 42/models, and code review). Stamped run summary saved to `outputs/run_summary_20261105_055653.json`. 76/76 tests pass; freeze check clean (0 diff). Status: Clearance proposed.

## Verdicts (researcher)

- 2026-11-05 · [T01 · Dossier Section Harmonization & Raw Material Verification](issues/01-dossier-harmonization.md): Cleared — MB
- 2026-11-05 · [T02 · Unified Publication LaTeX Document Assembly](issues/02-latex-manuscript-assembly.md): Cleared — MB
- 2026-11-05 · [T03 · BibTeX Human Citation Verification Audit](issues/03-bibtex-citation-audit.md): Cleared — MB
- 2026-11-05 · [T04 · Final 6-Question Paper Gate Clearance](issues/04-final-paper-gate-clearance.md): Cleared — MB

## Active Frontier Tickets

- [x] [01 · Dossier Section Harmonization & Raw Material Verification](issues/01-dossier-harmonization.md) (Cleared — MB)
- [x] [02 · Unified Publication LaTeX Document Assembly](issues/02-latex-manuscript-assembly.md) (Cleared — MB)
- [x] [03 · BibTeX Human Citation Verification Audit](issues/03-bibtex-citation-audit.md) (Cleared — MB)
- [x] [04 · Final 6-Question Paper Gate Clearance](issues/04-final-paper-gate-clearance.md) (Cleared — MB)
