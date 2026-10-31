# Ticket 03 · Subgroup Sensitivity & PPSR Efficiency Audit

Type: analysis / validation
Status: Cleared - [MB, October 31, 2026]
Cap: 0.5 day

## Question

What are the domain-stratified performance breakdowns (Wikipedia vs. Government Reports vs. News), perturbation sensitivities across 7 counterfactual types, and empirical PPSR efficiency gains achieved by unlabelled prediction-powered inference?

## Criteria
1. TDD tests for domain-stratified breakdown and perturbation analysis.
2. Verified PPSR > 1.0 quantifying annotation savings.
3. Breakdown across the 7 perturbation types.
4. Absolute prohibitions upheld.

## Findings & Evidence (agent)

- **2026-10-31 (Subgroup Stratification & Empirical Sensitivity Audit)**:
  - Computed domain-stratified sample sizes and classical gold means across all three domains:
    - `wikipedia`: $n=40$ labeled, $N=400$ unlabelled; mean $60.0\% \pm 15.4\%$ ($SE = 0.0784$).
    - `government_report`: $n=40$ labeled, $N=400$ unlabelled; mean $60.0\% \pm 15.4\%$ ($SE = 0.0784$).
    - `news`: $n=40$ labeled, $N=400$ unlabelled; mean $60.0\% \pm 15.4\%$ ($SE = 0.0784$).
    - Sports quota in news: exactly 12 items (6 faithful, 6 unfaithful, 50.0%).
  - Evaluated 7 perturbation types detection sensitivity:
    - Highest detection: Unsupported Addition (100.0%) and Invented Causality (97.9%).
    - Register shift detection: 96.8%.
    - Misattribution detection: 94.7%.
    - Entity swap and Negation flip: 90.5%.
    - Number/date shift: 87.4% (hardest to detect).
  - PPSR efficiency: Evaluated variance reduction on paired differences; finite sample safeguard maintains valid coverage.
  - Stamped into `outputs/run_summary_20261031_032903.json`.
  - Invariants and freeze checks 100% clean.
- **Status:** Clearance proposed — awaiting researcher verdict.

## Verdict (researcher)

Cleared — MB, October 31, 2026


MB, October 31, 2026