# Ticket 01 · Dossier Section Harmonization & Raw Material Verification

Type: paper drafting / synthesis
Cap: 2 hours
Status: Clearance proposed — awaiting researcher

## Question

Can we harmonize all paper dossier sections (`03-methodology.md`, `04-statistical-framework.md`) and raw notes (`01-intro-raw-material.md`, `02-related-work-raw-material.md`, `05-limitations-raw-material.md`, `06-unblinded-empirical-results.md`) with the full 5-arm evaluation empirical findings, aligning all model names (ADR 0002 `gemini-3.6-flash`), point estimates, and degradation numbers?

## Criteria
1. `paper/dossier/03-methodology.md` updated and consistent with ADR 0002 and candidate findings.
2. `paper/dossier/04-statistical-framework.md` updated with empirical PPSR ($1.15\times$) and cluster SE.
3. Raw material files in `paper/notes/` accurately supply evidence for researcher-authored sections (`01-introduction.md`, `02-related-work.md`, `05-limitations.md`).
4. Absolute Prohibition 1 (The Freeze) and Absolute Prohibition 2 (Gold Isolation) strictly upheld.

## Findings & Evidence (agent)

- 2026-11-05: **Harmonized Dossier & Notes**:
  - `paper/dossier/03-methodology.md`: Updated Arm 5 specification to `gemini-3.6-flash` under ADR 0002, detailing temperature 0.0, seed 42, 10-key rotation pool, and prompt-hash caching.
  - `paper/dossier/04-statistical-framework.md`: Aligned cluster-robust variance, paired difference formulation ($\Delta_{XL} - \Delta_{MT}$), and empirical PPSR range ($1.15\times$ to $1.73\times$).
  - `paper/notes/06-unblinded-empirical-results.md`: Fully populated with Table 1 and Table 2 empirical values for Arm 5 ($A(C1)=56.7\%$, $A(C2)=4.2\%$, $A(C3)=31.7\%$, $\Delta_{MT}=+27.5\%$, $\Delta_{XL}=-25.0\%$, paired diff $-52.5\%$, and 98.3% perturbation sensitivity).
  - `paper/notes/01-intro-raw-material.md`: Aligned contributions with exact $N=1,200$ unlabelled corpus dimensions and 5-arm empirical findings.
  - `paper/notes/02-related-work-raw-material.md`: Harmonized literature positioning (asymmetric cross-lingual claim grounding vs classic symmetric NLI).
  - `paper/notes/05-limitations-raw-material.md`: Added concrete qualitative MT error taxonomy (named entity transliteration drift, Bikram Sambat calendar vs Gregorian, honorific flattening) and honest disclosure of Arm 5 candidate scope.
- **Prohibitions**: Absolute Prohibition 1 (The Freeze) strictly upheld (0 diff on `src/analyze/` and `src/report/`). Absolute Prohibition 2 upheld (zero writes to `data/raw/labels/`).
- **Tests**: All 67 regression & invariant tests passing (`python3 -m pytest tests/`).


## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
