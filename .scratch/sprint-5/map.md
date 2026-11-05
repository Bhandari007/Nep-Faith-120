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

## Verdicts (researcher)

<!-- Researcher signs verdicts with initials and date below -->

## Active Frontier Tickets

- [ ] [01 · Dossier Section Harmonization & Raw Material Verification](issues/01-dossier-harmonization.md) (Active — Frontier)
- [ ] [02 · Unified Publication LaTeX Document Assembly](issues/02-latex-manuscript-assembly.md) (Pending)
- [ ] [03 · BibTeX Human Citation Verification Audit](issues/03-bibtex-citation-audit.md) (Pending)
- [ ] [04 · Final 6-Question Paper Gate Clearance](issues/04-final-paper-gate-clearance.md) (Pending)
