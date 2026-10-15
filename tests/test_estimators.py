"""Tests for Cluster-Robust Stratified PPI++ Statistical Engine."""

import math
import random
import pytest

from src.analyze.estimators import (
    classical_cluster_mean,
    ppi_plus_plus_cluster_mean,
    stratified_ppi_cluster_mean,
    paired_difference_estimator,
)


def test_classical_cluster_mean():
    # 10 clusters (items), each having 3 claims
    # Uniform mean = 0.8
    y = [1.0, 1.0, 0.0] * 5 + [1.0, 1.0, 1.0] * 5
    cluster_ids = []
    for i in range(10):
        cluster_ids.extend([f"item_{i}"] * 3)

    est = classical_cluster_mean(y, cluster_ids)
    assert math.isclose(est.estimate, (10 + 15) / 30.0, rel_tol=1e-3)
    assert est.n_labeled == 30
    assert est.n_clusters_labeled == 10
    assert est.se > 0.0
    assert est.ci_lower <= est.estimate <= est.ci_upper


def test_ppi_high_correlation_shrinks_variance():
    # Synthetic ground truth
    rng = random.Random(42)
    n = 100
    N = 1000

    cluster_ids_lab = [f"item_{i // 4}" for i in range(n)]

    # Ground truth Y: binary outcomes
    y_lab = [1.0 if rng.random() > 0.3 else 0.0 for _ in range(n)]
    
    # Strong proxy f (90% agreement with Y)
    f_lab = [y if rng.random() > 0.1 else (1.0 - y) for y in y_lab]
    f_unlab = [1.0 if rng.random() > 0.3 else 0.0 for _ in range(N)]

    classical_est = classical_cluster_mean(y_lab, cluster_ids_lab)
    ppi_est = ppi_plus_plus_cluster_mean(y_lab, f_lab, cluster_ids_lab, f_unlab)

    assert ppi_est.is_ppi is True
    assert ppi_est.lambda_star > 0.0
    assert ppi_est.correlation_rho > 0.6
    # PPI++ variance must be strictly smaller than classical variance (PPSR > 1.0)
    assert ppi_est.se <= classical_est.se
    assert ppi_est.ppsr >= 1.0


def test_ppi_zero_correlation_protects_variance():
    # Noise proxy f completely independent of Y
    rng = random.Random(999)
    n = 100
    N = 500

    cluster_ids_lab = [f"item_{i // 2}" for i in range(n)]
    y_lab = [1.0 if rng.random() > 0.4 else 0.0 for _ in range(n)]
    # Random coin flips
    f_lab = [1.0 if rng.random() > 0.5 else 0.0 for _ in range(n)]
    f_unlab = [1.0 if rng.random() > 0.5 else 0.0 for _ in range(N)]

    classical_est = classical_cluster_mean(y_lab, cluster_ids_lab)
    ppi_est = ppi_plus_plus_cluster_mean(y_lab, f_lab, cluster_ids_lab, f_unlab)

    # When proxy is uninformative, PPI++ does NOT inflate variance beyond classical
    assert ppi_est.se <= classical_est.se * 1.001


def test_paired_difference_estimator():
    # Hypothesis H1: C2 (raw MT) has higher accuracy than C1 (cross-lingual): Δ > 0
    rng = random.Random(123)
    n = 60
    N = 600
    cluster_ids = [f"item_{i // 3}" for i in range(n)]

    # Baseline item difficulty shared between C1 and C2 (causes positive covariance)
    item_diff = {f"item_{k}": rng.uniform(0.1, 0.9) for k in range(20)}

    y_c1 = []
    y_c2 = []
    f_c1 = []
    f_c2 = []

    for cid in cluster_ids:
        base = item_diff[cid]
        # C2 has +0.15 advantage over C1
        y1 = 1.0 if rng.random() < base else 0.0
        y2 = 1.0 if rng.random() < min(1.0, base + 0.15) else 0.0
        y_c1.append(y1)
        y_c2.append(y2)
        f_c1.append(y1 if rng.random() > 0.1 else (1.0 - y1))
        f_c2.append(y2 if rng.random() > 0.1 else (1.0 - y2))

    f_c1_unlab = [1.0 if rng.random() > 0.4 else 0.0 for _ in range(N)]
    f_c2_unlab = [1.0 if rng.random() > 0.3 else 0.0 for _ in range(N)]

    paired_est = paired_difference_estimator(
        y_c2_labeled=y_c2,
        y_c1_labeled=y_c1,
        f_c2_labeled=f_c2,
        f_c1_labeled=f_c1,
        cluster_ids_labeled=cluster_ids,
        f_c2_unlabeled=f_c2_unlab,
        f_c1_unlabeled=f_c1_unlab,
    )

    assert paired_est.is_ppi is True
    assert paired_est.se > 0.0
    # True expected difference is ~+0.15
    assert paired_est.estimate > 0.0


def test_stratified_ppi_cluster_mean():
    strata_labeled = {
        "wikipedia": {
            "y": [1.0] * 20 + [0.0] * 10,
            "f": [1.0] * 22 + [0.0] * 8,
            "cluster_ids": [f"wiki_{i // 3}" for i in range(30)],
        },
        "government_report": {
            "y": [1.0] * 15 + [0.0] * 15,
            "f": [1.0] * 16 + [0.0] * 14,
            "cluster_ids": [f"gov_{i // 3}" for i in range(30)],
        },
        "news": {
            "y": [1.0] * 25 + [0.0] * 5,
            "f": [1.0] * 24 + [0.0] * 6,
            "cluster_ids": [f"news_{i // 3}" for i in range(30)],
        },
    }
    strata_unlabeled = {
        "wikipedia": [1.0] * 200 + [0.0] * 100,
        "government_report": [1.0] * 150 + [0.0] * 150,
        "news": [1.0] * 250 + [0.0] * 50,
    }

    strat_est = stratified_ppi_cluster_mean(strata_labeled, strata_unlabeled)
    assert strat_est.is_ppi is True
    assert 0.0 <= strat_est.ci_lower <= strat_est.estimate <= strat_est.ci_upper <= 1.0
