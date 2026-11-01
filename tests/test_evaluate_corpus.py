"""Tests for Evaluation Corpus Runner (src/run/evaluate_corpus.py)."""

import json
from pathlib import Path
import pytest

from src.run.evaluate_corpus import (
    evaluate_item_condition,
    evaluate_dataset,
    compute_item_faithfulness_from_claims,
)
from src.prepare.schema import ClaimLabel


def test_compute_item_faithfulness():
    """Verifies item-level binary faithfulness aggregation logic."""
    # Case 1: All supported -> Faithful (1)
    claims_1 = [
        {"claim_id": "c1", "is_critical": True, "predicted_label": ClaimLabel.SUPPORTED.value},
        {"claim_id": "c2", "is_critical": False, "predicted_label": ClaimLabel.SUPPORTED.value},
    ]
    assert compute_item_faithfulness_from_claims(claims_1) == 1

    # Case 2: Non-critical contradicted, critical supported -> Unfaithful (all claims must be supported)
    claims_2 = [
        {"claim_id": "c1", "is_critical": True, "predicted_label": ClaimLabel.SUPPORTED.value},
        {"claim_id": "c2", "is_critical": False, "predicted_label": ClaimLabel.CONTRADICTED.value},
    ]
    assert compute_item_faithfulness_from_claims(claims_2) == 0

    # Case 3: Critical claim contradicted -> Unfaithful (0)
    claims_3 = [
        {"claim_id": "c1", "is_critical": True, "predicted_label": ClaimLabel.CONTRADICTED.value},
    ]
    assert compute_item_faithfulness_from_claims(claims_3) == 0

    # Case 4: Critical claim not-in-context -> Unfaithful (0)
    claims_4 = [
        {"claim_id": "c1", "is_critical": True, "predicted_label": ClaimLabel.NOT_IN_CONTEXT.value},
    ]
    assert compute_item_faithfulness_from_claims(claims_4) == 0


def test_evaluate_item_condition(tmp_path):
    """Verifies single item condition scoring across claims with an evaluator arm."""
    from src.run.scorers import Arm2BgeM3Similarity

    scorer = Arm2BgeM3Similarity(cache_dir=tmp_path / "cache")
    item = {
        "item_id": "test_001",
        "passage_ne": "नेपाल एक सुन्दर देश हो।",
        "c2_raw_mt": "Nepal is a beautiful country.",
        "c3_post_edited_mt": "Nepal is a beautiful country.",
        "claims": [
            {"claim_id": "test_001_c1", "claim_text": "Nepal is a beautiful country.", "is_critical": True},
            {"claim_id": "test_001_c2", "claim_text": "France is in Asia.", "is_critical": True},
        ]
    }

    result = evaluate_item_condition(item, condition="C2", scorer=scorer)
    assert result["item_id"] == "test_001"
    assert result["condition"] == "C2"
    assert len(result["claim_evaluations"]) == 2
    assert "derived_faithfulness" in result
    assert result["derived_faithfulness"] in (0, 1)


def test_evaluate_dataset_end_to_end(tmp_path):
    """Verifies end-to-end dataset evaluation with row conservation and cache integrity."""
    from src.run.scorers import Arm2BgeM3Similarity

    sample_items = [
        {
            "item_id": f"item_{i:03d}",
            "domain": "wikipedia",
            "sub_genre": "culture_heritage",
            "passage_ne": "नेपाल एक हिमाल भएको देश हो।",
            "c2_raw_mt": "Nepal is a country with mountains.",
            "c3_post_edited_mt": "Nepal is a country with mountains.",
            "claims": [
                {"claim_id": f"item_{i:03d}_c1", "claim_text": "Nepal has mountains.", "is_critical": True}
            ]
        }
        for i in range(3)
    ]

    input_file = tmp_path / "sample_items.jsonl"
    with open(input_file, "w", encoding="utf-8") as f:
        for it in sample_items:
            f.write(json.dumps(it) + "\n")

    output_file = tmp_path / "predictions.jsonl"
    scorers = {"arm2_bgem3": Arm2BgeM3Similarity(cache_dir=tmp_path / "cache")}

    total_evaluated = evaluate_dataset(
        input_path=input_file,
        output_path=output_file,
        scorers=scorers,
        conditions=["C1", "C2", "C3"],
    )

    assert total_evaluated == 3
    assert output_file.exists()

    with open(output_file, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    assert len(records) == 3
    for r in records:
        assert "item_id" in r
        assert "arm2_bgem3" in r["predictions"]
        for c in ["C1", "C2", "C3"]:
            assert c in r["predictions"]["arm2_bgem3"]
            assert "derived_faithfulness" in r["predictions"]["arm2_bgem3"][c]
            assert "claims" in r["predictions"]["arm2_bgem3"][c]


def test_evaluate_dataset_merges_new_arm_preserving_existing(tmp_path):
    """Verifies that running evaluate_dataset merges new arm predictions preserving existing arms."""
    from src.run.scorers import Arm1HHEMScorer, Arm2BgeM3Similarity

    sample_items = [
        {
            "item_id": "item_001",
            "domain": "wikipedia",
            "passage_ne": "नेपाल एक हिमाल भएको देश हो।",
            "c2_raw_mt": "Nepal is a country with mountains.",
            "c3_post_edited_mt": "Nepal is a country with mountains.",
            "claims": [
                {"claim_id": "item_001_c1", "claim_text": "Nepal has mountains.", "is_critical": True}
            ]
        }
    ]

    input_file = tmp_path / "sample_items.jsonl"
    with open(input_file, "w", encoding="utf-8") as f:
        for it in sample_items:
            f.write(json.dumps(it) + "\n")

    output_file = tmp_path / "predictions_merge.jsonl"

    # 1. Run first arm
    evaluate_dataset(input_file, output_file, {"arm2_bgem3": Arm2BgeM3Similarity(cache_dir=tmp_path / "cache")})
    
    # 2. Run second arm to same output file
    evaluate_dataset(input_file, output_file, {"arm1_hhem": Arm1HHEMScorer(cache_dir=tmp_path / "cache")})

    with open(output_file, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    assert len(records) == 1
    # Both arms must be present in the merged output!
    assert "arm2_bgem3" in records[0]["predictions"]
    assert "arm1_hhem" in records[0]["predictions"]


def test_evaluate_dataset_atomic_checkpoint_preserves_all_items(tmp_path):
    """Verifies that checkpointing preserves existing items without truncation."""
    from src.run.scorers import Arm2BgeM3Similarity

    sample_items = [
        {
            "item_id": f"item_{i:03d}",
            "domain": "wikipedia",
            "passage_ne": f"नेपाल {i}।",
            "c2_raw_mt": f"Nepal {i}.",
            "c3_post_edited_mt": f"Nepal {i}.",
            "claims": [
                {"claim_id": f"item_{i:03d}_c1", "claim_text": f"Nepal {i}.", "is_critical": True}
            ]
        }
        for i in range(1, 12)
    ]

    input_file = tmp_path / "all_items.jsonl"
    with open(input_file, "w", encoding="utf-8") as f:
        for it in sample_items:
            f.write(json.dumps(it) + "\n")

    output_file = tmp_path / "predictions_atomic.jsonl"

    # Pre-populate output file with dummy records for all 11 items
    with open(output_file, "w", encoding="utf-8") as f:
        for it in sample_items:
            f.write(json.dumps({"item_id": it["item_id"], "predictions": {"dummy_arm": {}}}) + "\n")

    # Evaluate using evaluate_dataset
    evaluate_dataset(input_file, output_file, {"arm2_bgem3": Arm2BgeM3Similarity(cache_dir=tmp_path / "cache")})

    with open(output_file, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    assert len(records) == 11
    for r in records:
        assert "dummy_arm" in r["predictions"]
        assert "arm2_bgem3" in r["predictions"]


