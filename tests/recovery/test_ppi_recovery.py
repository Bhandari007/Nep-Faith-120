"""NepFaith-120: Planted Effect Recovery Simulation Tests

Verifies that the cluster-robust paired PPI++ estimator recovers known planted effects
with valid confidence interval coverage (nominal 95% CI covering >= 90% in 100 trials),
unbiased point estimation, and empirical variance reduction (PPSR > 1.0).
"""

import random
import pytest
from src.analyze.estimators import paired_difference_estimator


def test_planted_effect_recovery_monte_carlo():
    """Simulates 100 Monte Carlo trials with planted effect Delta* = 0.12."""
    planted_delta = 0.12
    n_trials = 100
    covered_count = 0
    estimates = []
    ppsrs = []

    rng = random.Random(2026)

    # 40 items * 3 claims = 120 labeled claims
    n_items_labeled = 40
    claims_per_item = 3
    n_labeled = n_items_labeled * claims_per_item
    N_unlabeled = 900

    cluster_ids = [f"item_{i // claims_per_item}" for i in range(n_labeled)]

    for trial in range(n_trials):
        # 1. Generate base item difficulty (item-level random effect)
        item_difficulty = {
            f"item_{k}": rng.uniform(0.35, 0.75) for k in range(n_items_labeled)
        }

        y_c1 = []
        y_c2 = []
        f_c1 = []
        f_c2 = []

        for cid in cluster_ids:
            base_p = item_difficulty[cid]
            p_c1 = max(0.05, min(0.95, base_p - (planted_delta / 2.0)))
            p_c2 = max(0.05, min(0.95, base_p + (planted_delta / 2.0)))

            # True labels
            y1 = 1.0 if rng.random() < p_c1 else 0.0
            y2 = 1.0 if rng.random() < p_c2 else 0.0
            y_c1.append(y1)
            y_c2.append(y2)

            # Proxy predictions with 85% accuracy (good LLM judge)
            f1 = y1 if rng.random() < 0.85 else (1.0 - y1)
            f2 = y2 if rng.random() < 0.85 else (1.0 - y2)
            f_c1.append(f1)
            f_c2.append(f2)

        # Unlabeled set proxy predictions
        f_c1_unlab = []
        f_c2_unlab = []
        for _ in range(N_unlabeled):
            base_p = rng.uniform(0.35, 0.75)
            p_c1 = max(0.05, min(0.95, base_p - (planted_delta / 2.0)))
            p_c2 = max(0.05, min(0.95, base_p + (planted_delta / 2.0)))
            y1 = 1.0 if rng.random() < p_c1 else 0.0
            y2 = 1.0 if rng.random() < p_c2 else 0.0
            f1 = y1 if rng.random() < 0.85 else (1.0 - y1)
            f2 = y2 if rng.random() < 0.85 else (1.0 - y2)
            f_c1_unlab.append(f1)
            f_c2_unlab.append(f2)

        # 2. Run Paired Difference PPI++ Estimator
        res = paired_difference_estimator(
            y_c2_labeled=y_c2,
            y_c1_labeled=y_c1,
            f_c2_labeled=f_c2,
            f_c1_labeled=f_c1,
            cluster_ids_labeled=cluster_ids,
            f_c2_unlabeled=f_c2_unlab,
            f_c1_unlabeled=f_c1_unlab,
            alpha=0.05,
        )

        estimates.append(res.estimate)
        if res.ppsr is not None:
            ppsrs.append(res.ppsr)

        if res.ci_lower <= planted_delta <= res.ci_upper:
            covered_count += 1

    # 3. Validation Criteria
    coverage_rate = covered_count / n_trials
    mean_estimate = sum(estimates) / len(estimates)
    abs_bias = abs(mean_estimate - planted_delta)
    mean_ppsr = sum(ppsrs) / len(ppsrs) if ppsrs else 1.0

    print(f"\n--- MONTE CARLO RECOVERY REPORT ({n_trials} trials) ---")
    print(f"Planted Delta: {planted_delta:.4f}")
    print(f"Mean Recovered Delta: {mean_estimate:.4f} (Bias: {abs_bias:.4f})")
    print(f"Empirical 95% CI Coverage: {coverage_rate * 100:.1f}%")
    print(f"Mean PPSR (Efficiency Gain): {mean_ppsr:.3f}x")

    # Assertions
    assert coverage_rate >= 0.90, f"Coverage rate {coverage_rate:.2f} fell below 90% threshold"
    assert abs_bias < 0.02, f"Absolute bias {abs_bias:.4f} exceeded tolerance of 0.02"
    assert mean_ppsr > 1.0, f"PPSR {mean_ppsr:.3f} failed to demonstrate variance reduction"
