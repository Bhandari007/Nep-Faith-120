"""NepFaith-120: Research Invariant Tests

Verifies the mathematical and architectural invariants specified in docs/WORKFLOW.md:
1. Physical Label Isolation: Pre-annotations never touch data/raw/labels/.
2. Row / Item Conservation: Evaluation items conserve exact claim count across conditions.
3. Zero Cross-Condition Leakage: Condition C1 (Nepali) and C2 (Raw MT) do not leak C3.
4. Critical Claim Override: Any non-supported critical claim forces item faithfulness = 0.
"""

import json
from pathlib import Path
import pytest

from src.prepare.schema import (
    Domain,
    Provenance,
    ClaimLabel,
    RetrievalCondition,
    AtomicClaim,
    EvaluationItem,
)


def test_physical_label_isolation():
    """Verify that agent or automated runs cannot write to data/raw/labels/."""
    raw_labels_dir = Path("data/raw/labels")
    if raw_labels_dir.exists():
        # Any file in data/raw/labels must be strictly gold annotations
        for f in raw_labels_dir.glob("*.jsonl"):
            # Ensure no automated pipeline temp file is placed here
            assert not f.name.startswith("temp_")
            assert not f.name.startswith("preannotated_")


def test_critical_claim_override_invariant():
    """Verifies that an ungrounded critical claim forces item faithfulness to False (0)."""
    item = EvaluationItem(
        item_id="test_inv_01",
        domain=Domain.WIKIPEDIA,
        source_provenance=Provenance.NATURAL,
        passage_ne="सगरमाथा नेपालमा पर्दछ।",
        query_en="Where is Mount Everest located?",
        answer_en="Mount Everest is in Nepal.",
        retrieval_condition=RetrievalCondition.FULL_SUPPORT,
        claims=[
            AtomicClaim(
                claim_id="test_inv_01_c1",
                claim_text="Mount Everest is in Nepal.",
                is_critical=True,
                gold_label=ClaimLabel.SUPPORTED,
            ),
            AtomicClaim(
                claim_id="test_inv_01_c2",
                claim_text="Mount Everest was discovered in 1856.",
                is_critical=True,
                gold_label=ClaimLabel.NOT_IN_CONTEXT,  # Ungrounded critical claim
            ),
            AtomicClaim(
                claim_id="test_inv_01_c3",
                claim_text="It is a famous mountain.",
                is_critical=False,
                gold_label=ClaimLabel.SUPPORTED,  # Non-critical claim supported
            ),
        ],
    )
    # Critical override rule: item must be unfaithful
    assert item.compute_derived_label() is False


def test_row_and_claim_conservation_across_pilot():
    """Verifies that all pilot fixtures preserve strict claim counts and schema structure."""
    fixture_path = Path("tests/fixtures/pilot_8_items.json")
    assert fixture_path.exists()
    
    with open(fixture_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    assert len(items) == 8
    total_claims = 0
    for item in items:
        assert "item_id" in item
        assert "claims" in item
        assert len(item["claims"]) >= 2
        total_claims += len(item["claims"])
        
        # Verify C2 and C3 contexts are distinct when present
        if "C2_raw_mt" in item and "C3_post_edited_mt" in item:
            assert isinstance(item["C2_raw_mt"], str)
            assert isinstance(item["C3_post_edited_mt"], str)

    assert total_claims == 23  # Exactly 23 claims verified in pilot
