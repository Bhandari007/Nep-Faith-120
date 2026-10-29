"""NepFaith-120: Invariants for Gate 2 (Human Gold Benchmark & Data Lock).

Verifies that the n=120 gold dataset in data/raw/labels/gold_labels_120.jsonl
strictly adheres to all pre-registered stratification, claim conservation,
derived faithfulness overrides, and frozen layer constraints.
"""

import json
import subprocess
from pathlib import Path
import pytest

from src.prepare.schema import EvaluationItem, ClaimLabel, Domain, Provenance


def test_gate2_gold_benchmark_invariants():
    """Verifies that the n=120 gold dataset upholds all pre-registered invariants."""
    gold_path = Path("data/raw/labels/gold_labels_120.jsonl")
    if not gold_path.exists():
        pytest.skip("data/raw/labels/gold_labels_120.jsonl not yet committed by researcher")

    items = []
    with open(gold_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))

    assert len(items) == 120, f"Expected 120 items, got {len(items)}"

    domain_counts = {}
    sports_count = 0
    natural_count = 0
    perturbed_counts = {}
    total_claims = 0

    for it in items:
        # Validate schema via Pydantic model
        eval_item = EvaluationItem.model_validate(it)

        # Context coverage
        assert eval_item.passage_ne and len(eval_item.passage_ne.strip()) > 0
        assert eval_item.c2_raw_mt and len(eval_item.c2_raw_mt.strip()) > 0
        assert eval_item.c3_post_edited_mt and len(eval_item.c3_post_edited_mt.strip()) > 0

        # Derived item label
        assert eval_item.derived_item_label is not None
        assert isinstance(eval_item.derived_item_label, bool)

        # Stratification counts
        dom = eval_item.domain.value
        domain_counts[dom] = domain_counts.get(dom, 0) + 1

        if dom == Domain.NEWS.value and eval_item.sub_genre == "sports":
            sports_count += 1

        prov = eval_item.source_provenance.value
        if prov == Provenance.NATURAL.value:
            natural_count += 1
        elif prov == Provenance.PERTURBED.value:
            pt = eval_item.perturbation_type.value if eval_item.perturbation_type else None
            assert pt is not None, f"Perturbed item {eval_item.item_id} missing perturbation_type"
            perturbed_counts[pt] = perturbed_counts.get(pt, 0) + 1

        # Claim checks
        claims = eval_item.claims
        assert len(claims) >= 2, f"Item {eval_item.item_id} has fewer than 2 claims"
        total_claims += len(claims)

        for c in claims:
            assert c.gold_label in (ClaimLabel.SUPPORTED, ClaimLabel.CONTRADICTED, ClaimLabel.NOT_IN_CONTEXT)

        # Critical claim override invariant
        has_critical_failure = any(
            c.is_critical and c.gold_label in (ClaimLabel.CONTRADICTED, ClaimLabel.NOT_IN_CONTEXT)
            for c in claims
        )
        if has_critical_failure:
            assert eval_item.derived_item_label is False

        all_supported = all(c.gold_label == ClaimLabel.SUPPORTED for c in claims)
        if all_supported:
            assert eval_item.derived_item_label is True

    # Quotas verification
    assert domain_counts == {
        Domain.WIKIPEDIA.value: 40,
        Domain.GOVERNMENT_REPORT.value: 40,
        Domain.NEWS.value: 40,
    }, f"Domain stratification mismatch: {domain_counts}"

    assert sports_count == 12, f"Expected 12 sports items (30% quota), got {sports_count}"
    assert natural_count == 60, f"Expected 60 natural items (50%), got {natural_count}"
    assert sum(perturbed_counts.values()) == 60, f"Expected 60 perturbed items, got {sum(perturbed_counts.values())}"
    assert total_claims == 340, f"Expected 340 claims, got {total_claims}"


def test_gate2_freeze_invariant():
    """Verify that analysis and reporting layers remain unchanged against sprint-1-frozen."""
    diff = subprocess.check_output(
        ["git", "diff", "sprint-1-frozen", "--", "src/analyze/", "src/report/"],
        text=True,
    )
    assert diff.strip() == "", f"Freeze violation: modifications found in frozen layers:\n{diff}"
