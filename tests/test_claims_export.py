"""Tests for Ticket 02: Atomic Claim Decomposition & Criticality Invariants."""

import json
from pathlib import Path
import pytest


def test_claims_export_invariants(tmp_path):
    """Verifies that export_claims extracts valid atomic claims across all 120 items."""
    from src.prepare.export_claims import ClaimsExporter

    candidates_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    assert candidates_path.exists(), "Candidates file must exist before claim export"

    output_path = tmp_path / "claims_120.jsonl"
    exporter = ClaimsExporter(candidates_path=candidates_path, output_path=output_path)
    claims_records, stats = exporter.export_and_audit()

    # 1. Total Claim Count Invariant (target: 300 to 450 atomic claims across 120 items)
    assert 300 <= len(claims_records) <= 450, f"Expected 300-450 claims, got {len(claims_records)}"
    assert output_path.exists()

    # 2. Per-Item Bounds Invariant (2 to 5 claims per item)
    for item_id, count in stats["claims_per_item"].items():
        assert 2 <= count <= 5, f"Item {item_id} has {count} claims (out of bounds [2, 5])"

    # 3. Criticality Invariant (every item must have at least one critical claim)
    for item_id, crit_count in stats["critical_claims_per_item"].items():
        assert crit_count >= 1, f"Item {item_id} has no critical claims"

    # 4. Schema & Field Invariant
    for c in claims_records:
        assert c["claim_id"].startswith("item_")
        assert len(c["claim_text"].strip()) > 10
        assert isinstance(c["is_critical"], bool)
        assert c["gold_label"] is None, "Gold label must remain null in pre-annotation stage"
        assert c["sub_genre"] in [
            "health",
            "agriculture",
            "education",
            "economy_finance",
            "disaster_geography",
            "governance_law",
            "sports",
            "culture_heritage",
            "biodiversity_parks",
            "infrastructure_tourism",
        ]
