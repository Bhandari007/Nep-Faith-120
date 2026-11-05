# Ticket 02 · Unified Publication LaTeX Document Assembly

Type: document compilation / publication
Cap: 2 hours
Status: Clearance proposed — awaiting researcher

## Question

Can we compile a unified, publication-ready LaTeX manuscript incorporating the booktabs LaTeX tables (`reports/table1_decomposition.tex` and `reports/table2_sensitivity.tex`), mathematical notation, and bibliography citations without compilation errors?

## Criteria
1. Complete publication LaTeX document structured per standard ACL / EMNLP formatting.
2. Ingests Table 1 and Table 2 cleanly with booktabs formatting and reproducibility headers.
3. Clean LaTeX syntax verification without missing references, broken math, or duplicate labels.
4. Absolute Prohibition 1 (The Freeze) strictly upheld.

## Findings & Evidence (agent)

- 2026-11-05: **Unified Manuscript Assembled & Validated**:
  - Authored `paper/manuscript.tex` adhering to standard two-column computational linguistics conference format.
  - Formatted and updated publication tables `reports/table1_decomposition.tex` and `reports/table2_sensitivity.tex` with complete 5-arm empirical numbers (Arm 5 Gemini-3.6-Flash: $A(C1)=56.7\%$, $A(C2)=4.2\%$, $A(C3)=31.7\%$, paired difference $-52.5\%$, and 98.3% unfaithfulness detection).
  - Authored TDD test suite `tests/test_manuscript.py` verifying:
    1. Existence of `paper/manuscript.tex`.
    2. Validity and presence of all `\input{...}` files (Table 1 and Table 2).
    3. Exact correspondence between `\cite{...}` citation keys and `paper/references.bib`.
    4. Label and reference resolution (`\ref{...}` / `\label{...}`).
    5. Properly nested LIFO environment stack (`\begin{...}` / `\end{...}`).
  - All 5 manuscript integrity tests passing (72/72 total pytest suite passing).
  - Freeze check clean (0 diff on `src/analyze/` and `src/report/`).
  - Zero writes to `data/raw/labels/`.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
