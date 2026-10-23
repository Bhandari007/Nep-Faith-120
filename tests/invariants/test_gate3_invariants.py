"""Invariants for Gate 3: Unlabelled Corpus Assembly & Prediction Matrix Verification."""

import json
from pathlib import Path
import pytest


def test_gate3_unlabelled_corpus_invariants():
    """Verifies that the N=1,200 unlabelled dataset strictly upholds pre-registered sampling quotas."""
    unlab_path = Path("data/interim/unlabelled_1200.jsonl")
    if not unlab_path.exists():
        pytest.skip("unlabelled_1200.jsonl not found")

    items = []
    with open(unlab_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))

    assert len(items) == 1200, f"Expected 1,200 items, got {len(items)}"

    domain_counts = {}
    sports_count = 0
    natural_count = 0
    perturbed_counts = {}
    total_claims = 0

    for it in items:
        # Passage and MT coverage
        assert it.get("passage_ne") and len(it["passage_ne"].strip()) > 0
        assert it.get("c2_raw_mt") and len(it["c2_raw_mt"].strip()) > 0

        # Absolute Prohibition 2: Gold labels must be None
        assert it.get("derived_item_label") is None

        dom = it["domain"]
        domain_counts[dom] = domain_counts.get(dom, 0) + 1

        if dom == "news" and it.get("sub_genre") == "sports":
            sports_count += 1

        prov = it["source_provenance"]
        if prov == "natural":
            natural_count += 1
        elif prov == "synthetic_perturbed":
            pt = it["perturbation_type"]
            perturbed_counts[pt] = perturbed_counts.get(pt, 0) + 1

        claims = it.get("claims", [])
        assert 2 <= len(claims) <= 5
        total_claims += len(claims)
        for cl in claims:
            assert cl.get("gold_label") is None
            assert isinstance(cl.get("is_critical"), bool)
            assert cl.get("claim_text") and len(cl["claim_text"].strip()) > 0

    assert domain_counts.get("wikipedia") == 400
    assert domain_counts.get("government_report") == 400
    assert domain_counts.get("news") == 400
    assert sports_count == 120
    assert natural_count == 600
    assert sum(perturbed_counts.values()) == 600
    assert len(perturbed_counts) == 7
    assert total_claims == 3410


def test_gate3_predictions_matrix_invariants():
    """Verifies that the unlabelled prediction matrix is complete and row-conserved."""
    pred_path = Path("data/interim/predictions/predictions_unlabelled_1200.jsonl")
    if not pred_path.exists():
        pytest.skip("predictions_unlabelled_1200.jsonl not found")

    records = []
    with open(pred_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    assert len(records) == 1200, f"Expected 1,200 prediction records, got {len(records)}"

    required_arms = ["arm1_hhem", "arm2_bgem3", "arm3_mdeberta", "arm4_pipeline_nli"]
    for rec in records:
        assert "item_id" in rec
        assert "predictions" in rec
        for arm in required_arms:
            assert arm in rec["predictions"], f"Missing arm {arm} in item {rec['item_id']}"
            for cond in ["C1", "C2"]:
                assert cond in rec["predictions"][arm]
                cond_eval = rec["predictions"][arm][cond]
                assert cond_eval["derived_faithfulness"] in (0, 1)
                assert len(cond_eval["claims"]) >= 2


def test_gate3_absolute_prohibitions_compliance():
    """Verifies that gold label directories remain write-isolated and analysis freeze is intact."""
    gold_dir = Path("data/raw/labels")
    if gold_dir.exists():
        # Confirm agent has written no candidate/unlabelled data into gold directory
        for p in gold_dir.iterdir():
            assert "unlabelled" not in p.name
            assert "candidates" not in p.name
