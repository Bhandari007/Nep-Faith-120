# Ticket 03 · BibTeX Human Citation Verification Audit

Type: bibliographic integrity / verification
Cap: 2 hours
Status: Cleared — MB

## Question

Do 100% of the BibTeX entries in `paper/references.bib` carry human verification records (`verified_by = {MB, YYYY-MM-DD}`) confirming that the primary sources were opened and verified for authors, title, year, venue, and DOI?

## Criteria
1. Automated scanner / test verifies every entry in `paper/references.bib` has a valid `verified_by` field.
2. Zero unverified or agent-hallucinated citations in the manuscript bibliography.
3. All cited works correspond to real, published peer-reviewed papers or preprints.

## Findings & Evidence (agent)

- 2026-11-05: **Citation Verification Audit Completed**:
  - Implemented automated BibTeX integrity test suite in `tests/test_citations.py` enforcing Pillar 4 of `docs/WORKFLOW.md` and `AGENTS.md`.
  - Audited all 5 citations in `paper/references.bib`:
    1. `angelopoulos2023ppi`: Angelopoulos et al., Science 2023 (doi: 10.1126/science.adi6000), `verified_by = {MB, 2026-10-15}`.
    2. `gao2026ppsr`: Gao, Sicilia, & Shi, EMNLP 2026, `verified_by = {MB, 2026-10-15}`.
    3. `gala2023indictrans2`: Gala et al., TMLR 2023, `verified_by = {MB, 2026-10-15}`.
    4. `laurer2022mdeberta`: Laurer et al., Political Analysis 2022 (doi: 10.1017/pan.2023.20), `verified_by = {MB, 2026-10-15}`.
    5. `chen2024bgem3`: Chen et al., arXiv 2024 (2402.03216), `verified_by = {MB, 2026-10-15}`.
  - 100% of entries contain verified author, title, year, venue, and human verification signatures (`MB, 2026-10-15`).
  - Zero unverified or hallucinated citations present in `paper/manuscript.tex`.
  - 76/76 unit, recovery, and citation tests pass.
  - Freeze check clean (0 diff on `src/analyze/` and `src/report/`). Zero writes to `data/raw/labels/`.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, November 5, 2026