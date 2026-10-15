"""NepFaith-120: Cluster-Robust Stratified PPI++ Statistical Engine

Implements the official statistical estimation engine for NepFaith-120:
1. Classical Mean with Cluster-Robust Sandwich Variance (Huber-White)
2. Prediction-Powered Inference (PPI++) with Adaptive Tuning Parameter λ*
3. Cluster-Robust Variance Decomposition (nested claims within items)
4. Stratified PPI++ across Macro-Strata (Wikipedia, Government Reports, News)
5. Paired Difference Estimator (A(C2) - A(C1)) with Active Covariance Cancellation
6. PPSR (Prediction-Powered Sample Ratio) Relative Efficiency Diagnostics

References:
- Angelopoulos et al. (Science 2023), "Prediction-Powered Inference"
- Gao, Sicilia, & Shi (EMNLP 2026), "Which Metrics Save the Most Human Annotation?"
- NepFaith-120 Preregistration Section 7 (docs/PREREGISTRATION.md)
"""

import math
from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class PointEstimate:
    """Statistical point estimate and inference summary."""
    estimate: float
    se: float
    ci_lower: float
    ci_upper: float
    alpha: float
    n_labeled: int
    n_clusters_labeled: int
    N_unlabeled: int = 0
    lambda_star: Optional[float] = None
    correlation_rho: Optional[float] = None
    ppsr: Optional[float] = None
    is_ppi: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "estimate": self.estimate,
            "se": self.se,
            "ci_lower": self.ci_lower,
            "ci_upper": self.ci_upper,
            "alpha": self.alpha,
            "n_labeled": self.n_labeled,
            "n_clusters_labeled": self.n_clusters_labeled,
            "N_unlabeled": self.N_unlabeled,
            "lambda_star": self.lambda_star,
            "correlation_rho": self.correlation_rho,
            "ppsr": self.ppsr,
            "is_ppi": self.is_ppi,
        }


def _get_z_crit(alpha: float) -> float:
    """Returns critical z-value for standard two-sided confidence intervals."""
    if math.isclose(alpha, 0.05, abs_tol=1e-3):
        return 1.95996
    elif math.isclose(alpha, 0.01, abs_tol=1e-3):
        return 2.57583
    elif math.isclose(alpha, 0.10, abs_tol=1e-3):
        return 1.64485
    else:
        # Approximate standard normal quantile using Abramowitz & Stegun
        p = 1.0 - alpha / 2.0
        t = math.sqrt(-2.0 * math.log(1.0 - p))
        c0, c1, c2 = 2.515517, 0.802853, 0.010328
        d1, d2, d3 = 1.432788, 0.189269, 0.001308
        return t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0)


def classical_cluster_mean(
    y: List[float],
    cluster_ids: List[str],
    alpha: float = 0.05,
) -> PointEstimate:
    """Computes the sample mean with cluster-robust (Huber-White sandwich) standard error.
    
    Residuals are aggregated at the cluster (item) level to account for
    intra-cluster correlation across nested claims.
    """
    n = len(y)
    if n == 0:
        raise ValueError("Cannot compute classical estimate on empty data.")
    if len(cluster_ids) != n:
        raise ValueError("Length of y and cluster_ids must match exactly.")

    # 1. Overall sample mean
    y_bar = sum(y) / n

    # 2. Group into clusters
    cluster_totals = defaultdict(float)
    cluster_sizes = defaultdict(int)
    for val, cid in zip(y, cluster_ids):
        cluster_totals[cid] += val
        cluster_sizes[cid] += 1

    C = len(cluster_totals)
    if C < 2:
        # Fallback to classical unclustered variance if single cluster
        var_y = sum((val - y_bar) ** 2 for val in y) / max(n - 1, 1)
        se = math.sqrt(var_y / n)
    else:
        # 3. Cluster residuals: u_c = sum_{j in c} (y_cj - y_bar)
        sum_sq_u = 0.0
        for cid in cluster_totals:
            u_c = cluster_totals[cid] - (cluster_sizes[cid] * y_bar)
            sum_sq_u += u_c ** 2

        # Small sample degrees of freedom correction: C / (C - 1)
        dof_factor = C / (C - 1)
        # Clustered variance of the mean: dof_factor * sum(u_c^2) / n^2
        var_clustered = dof_factor * (sum_sq_u / (n ** 2))
        se = math.sqrt(max(var_clustered, 0.0))

    z_crit = _get_z_crit(alpha)
    ci_lower = max(0.0, y_bar - z_crit * se)
    ci_upper = min(1.0, y_bar + z_crit * se)

    return PointEstimate(
        estimate=y_bar,
        se=se,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        alpha=alpha,
        n_labeled=n,
        n_clusters_labeled=C,
        is_ppi=False,
    )


def ppi_plus_plus_cluster_mean(
    y_labeled: List[float],
    f_labeled: List[float],
    cluster_ids_labeled: List[str],
    f_unlabeled: List[float],
    alpha: float = 0.05,
    clip_lambda: bool = True,
) -> PointEstimate:
    """Computes the Prediction-Powered Inference (PPI++) estimator with adaptive tuning λ*
    and cluster-robust variance.
    
    Protects against variance inflation under weak proxy evaluators by optimizing
    λ* = Cov(f, Y) / ((1 + n/N) * Var(f)).
    """
    n = len(y_labeled)
    N = len(f_unlabeled)
    if n == 0:
        raise ValueError("Labeled set cannot be empty.")
    if len(f_labeled) != n or len(cluster_ids_labeled) != n:
        raise ValueError("Labeled inputs (y, f, cluster_ids) must have equal lengths.")

    # Classical baseline for comparison and fallback
    classical_est = classical_cluster_mean(y_labeled, cluster_ids_labeled, alpha=alpha)
    if N == 0:
        return classical_est

    # 1. Summary means
    y_bar = sum(y_labeled) / n
    f_bar_labeled = sum(f_labeled) / n
    f_bar_unlabeled = sum(f_unlabeled) / N

    # 2. Sample covariance and variance on labeled set
    cov_fy = 0.0
    var_f = 0.0
    var_y = 0.0
    for y_val, f_val in zip(y_labeled, f_labeled):
        cov_fy += (f_val - f_bar_labeled) * (y_val - y_bar)
        var_f += (f_val - f_bar_labeled) ** 2
        var_y += (y_val - y_bar) ** 2

    cov_fy /= max(n - 1, 1)
    var_f /= max(n - 1, 1)
    var_y /= max(n - 1, 1)

    # Correlation rho
    if var_f > 1e-12 and var_y > 1e-12:
        rho = cov_fy / math.sqrt(var_f * var_y)
        rho = max(-1.0, min(1.0, rho))
    else:
        rho = 0.0

    # 3. Optimal adaptive shrinkage parameter λ*
    if var_f > 1e-12:
        inflation_weight = 1.0 + (n / N)
        lambda_star = cov_fy / (inflation_weight * var_f)
        if clip_lambda:
            lambda_star = max(0.0, lambda_star)
    else:
        lambda_star = 0.0

    # 4. Point estimate: \hat\theta_{PPI++} = y_bar + \lambda^* * (f_bar_unlabeled - f_bar_labeled)
    correction = lambda_star * (f_bar_unlabeled - f_bar_labeled)
    ppi_estimate = y_bar + correction

    # 5. Cluster-robust variance computation
    cluster_residuals = defaultdict(float)
    cluster_sizes = defaultdict(int)

    for y_val, f_val, cid in zip(y_labeled, f_labeled, cluster_ids_labeled):
        cluster_sizes[cid] += 1
        # Residual: (Y_ij - y_bar) - \lambda^* * (f_ij - f_bar_labeled)
        res = (y_val - y_bar) - lambda_star * (f_val - f_bar_labeled)
        cluster_residuals[cid] += res

    C = len(cluster_residuals)
    if C < 2:
        # Fallback to unclustered residual variance
        sum_sq_res = sum(
            ((y_v - y_bar) - lambda_star * (f_v - f_bar_labeled)) ** 2
            for y_v, f_v in zip(y_labeled, f_labeled)
        )
        var_labeled = sum_sq_res / (n * max(n - 1, 1))
    else:
        dof_factor = C / (C - 1)
        sum_sq_u = sum(u ** 2 for u in cluster_residuals.values())
        var_labeled = dof_factor * (sum_sq_u / (n ** 2))

    # Variance contribution from the unlabeled set
    var_unlabeled = (lambda_star ** 2) * (var_f / N)

    total_var = var_labeled + var_unlabeled
    se = math.sqrt(max(total_var, 0.0))

    # Fallback to classical if PPI++ variance exceeds classical (finite-sample protection)
    if se > classical_est.se:
        return classical_est

    # Relative efficiency / PPSR
    var_classical = classical_est.se ** 2
    ppsr = (var_classical / total_var) if total_var > 1e-12 else 1.0

    z_crit = _get_z_crit(alpha)
    ci_lower = max(0.0, ppi_estimate - z_crit * se)
    ci_upper = min(1.0, ppi_estimate + z_crit * se)

    return PointEstimate(
        estimate=ppi_estimate,
        se=se,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        alpha=alpha,
        n_labeled=n,
        n_clusters_labeled=C,
        N_unlabeled=N,
        lambda_star=lambda_star,
        correlation_rho=rho,
        ppsr=ppsr,
        is_ppi=True,
    )


def stratified_ppi_cluster_mean(
    strata_labeled: Dict[str, Dict[str, Any]],
    strata_unlabeled: Dict[str, List[float]],
    stratum_weights: Optional[Dict[str, float]] = None,
    alpha: float = 0.05,
) -> PointEstimate:
    """Computes stratum-weighted PPI++ across Wikipedia, Government Reports, and News.
    
    Each stratum dictionary in `strata_labeled` must contain:
    - 'y': List[float]
    - 'f': List[float]
    - 'cluster_ids': List[str]
    """
    strata_keys = list(strata_labeled.keys())
    if not strata_keys:
        raise ValueError("Must provide at least one stratum.")

    # Calculate default proportional weights if not provided
    total_unlabeled = sum(len(strata_unlabeled.get(s, [])) for s in strata_keys)
    weights = {}
    for s in strata_keys:
        if stratum_weights and s in stratum_weights:
            weights[s] = stratum_weights[s]
        else:
            n_unlab = len(strata_unlabeled.get(s, []))
            weights[s] = (n_unlab / total_unlabeled) if total_unlabeled > 0 else (1.0 / len(strata_keys))

    # Normalize weights to sum to 1.0
    weight_sum = sum(weights.values())
    for s in weights:
        weights[s] /= weight_sum

    strat_est = 0.0
    strat_var = 0.0
    total_labeled_n = 0
    total_clusters = 0

    for s in strata_keys:
        lab = strata_labeled[s]
        unlab_f = strata_unlabeled.get(s, [])
        est_s = ppi_plus_plus_cluster_mean(
            y_labeled=lab["y"],
            f_labeled=lab["f"],
            cluster_ids_labeled=lab["cluster_ids"],
            f_unlabeled=unlab_f,
            alpha=alpha,
        )
        w = weights[s]
        strat_est += w * est_s.estimate
        strat_var += (w ** 2) * (est_s.se ** 2)
        total_labeled_n += est_s.n_labeled
        total_clusters += est_s.n_clusters_labeled

    se = math.sqrt(max(strat_var, 0.0))
    z_crit = _get_z_crit(alpha)
    ci_lower = max(0.0, strat_est - z_crit * se)
    ci_upper = min(1.0, strat_est + z_crit * se)

    return PointEstimate(
        estimate=strat_est,
        se=se,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        alpha=alpha,
        n_labeled=total_labeled_n,
        n_clusters_labeled=total_clusters,
        N_unlabeled=total_unlabeled,
        is_ppi=True,
    )


def paired_difference_estimator(
    y_c2_labeled: List[float],
    y_c1_labeled: List[float],
    f_c2_labeled: List[float],
    f_c1_labeled: List[float],
    cluster_ids_labeled: List[str],
    f_c2_unlabeled: List[float],
    f_c1_unlabeled: List[float],
    alpha: float = 0.05,
) -> PointEstimate:
    """Computes the paired difference estimate Δ = A(C2) - A(C1) using PPI++.
    
    Actively exploits within-item covariance cancellation:
    Var(C2 - C1) = Var(C2) + Var(C1) - 2 * Cov(C2, C1)
    """
    n = len(y_c2_labeled)
    if n != len(y_c1_labeled):
        raise ValueError("Paired observations must have identical lengths for C1 and C2.")
    if len(f_c2_unlabeled) != len(f_c1_unlabeled):
        raise ValueError("Unlabeled proxy sets must have identical lengths for C1 and C2.")

    # Form paired differences: D_i = Y_{C2, i} - Y_{C1, i}
    diff_y_labeled = [c2 - c1 for c2, c1 in zip(y_c2_labeled, y_c1_labeled)]
    diff_f_labeled = [c2 - c1 for c2, c1 in zip(f_c2_labeled, f_c1_labeled)]
    diff_f_unlabeled = [c2 - c1 for c2, c1 in zip(f_c2_unlabeled, f_c1_unlabeled)]

    # Compute PPI++ on the paired difference series
    diff_est = ppi_plus_plus_cluster_mean(
        y_labeled=diff_y_labeled,
        f_labeled=diff_f_labeled,
        cluster_ids_labeled=cluster_ids_labeled,
        f_unlabeled=diff_f_unlabeled,
        alpha=alpha,
        clip_lambda=True,
    )

    # Allow negative bounds for difference estimate
    z_crit = _get_z_crit(alpha)
    ci_lower = diff_est.estimate - z_crit * diff_est.se
    ci_upper = diff_est.estimate + z_crit * diff_est.se

    return PointEstimate(
        estimate=diff_est.estimate,
        se=diff_est.se,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
        alpha=alpha,
        n_labeled=n,
        n_clusters_labeled=diff_est.n_clusters_labeled,
        N_unlabeled=len(diff_f_unlabeled),
        lambda_star=diff_est.lambda_star,
        correlation_rho=diff_est.correlation_rho,
        ppsr=diff_est.ppsr,
        is_ppi=True,
    )
