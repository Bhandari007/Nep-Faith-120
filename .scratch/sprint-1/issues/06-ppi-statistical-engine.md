# Cluster-Robust Stratified PPI++ Engine

Type: statistical
Status: Clearance proposed — awaiting researcher
Cap: 2 days (PPI++ estimator, cluster sandwich variance, paired covariance cancellation & tests)

## Question

Build `src/analyze/estimators.py` implementing the complete statistical inference engine for NepFaith-120:
1. **Classical Baseline Estimator:** Cluster-robust mean with Huber-White sandwich variance clustered by `item_id`.
2. **Prediction-Powered Estimator (PPI++):** Adaptive control variate with data-driven tuning parameter $\lambda^*$ protecting against proxy degradation.
3. **Cluster-Robust Residuals:** Exact cluster variance summation over constituent claims $k_{ij}$ within items $i$.
4. **Stratified Extension:** Stratum-weighted aggregation across the 3 macro-strata (`wikipedia`, `government_report`, `news`).
5. **Paired Difference Estimator ($H1$):** Direct estimation of $\Delta = A(C2) - A(C1)$ exploiting within-item covariance cancellation $-2\mathrm{Cov}(A(C2), A(C1))$.
6. **Diagnostics & Reporting:** Automatic calculation of $\lambda^*$, correlation $\rho(f, Y)$, effective sample size, PPSR (Prediction-Powered Sample Ratio), and $(1-\alpha)$ confidence intervals.
7. **Freeze Commitment:** This engine must be complete, verified, and frozen under `src/analyze/` prior to Gate 1 freeze tag.

## Findings & Evidence (agent)

1. **Statistical Engine Built (`src/analyze/estimators.py`):**
   - Implemented `classical_cluster_mean`: Huber-White sandwich cluster variance accounting for nested claims within items ($C / (C-1)$ small-sample adjustment).
   - Implemented `ppi_plus_plus_cluster_mean`: Optimal adaptive weight $\lambda^* = \frac{\widehat{\mathrm{Cov}}(f, Y)}{(1 + n/N)\widehat{\mathrm{Var}}(f)}$ with finite-sample variance protection.
   - Implemented `stratified_ppi_cluster_mean`: Linear combination of stratum-specific estimators weighted by stratum population proportions $w_s = N_s / N$.
   - Implemented `paired_difference_estimator`: Formulates paired observation difference series $(C2 - C1)$ directly cancelling background item difficulty variance.
2. **Mathematical Verification:**
   - Abramowitz & Stegun normal critical value approximation and exact standard normal quantiles.
   - PPSR calculated as $\mathrm{Var}(\hat\theta_{\text{classical}}) / \mathrm{Var}(\hat\theta_{\text{PPI++}})$.
3. **Unit Tests Passing:**
   - `tests/test_estimators.py` (5/5 passed in 0.01s): Verified classical cluster mean, variance shrinkage under strong proxy ($\rho = 0.9$), safety under uninformative proxy ($\rho = 0.0$), paired difference recovery, and stratified estimation.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->

