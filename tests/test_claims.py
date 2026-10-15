"""Tests for Atomic Claim Decomposition Engine."""

import pytest
from src.prepare.schema import AtomicClaim
from src.prepare.claims import decompose_claims_rule_based, decompose_claims


def test_decompose_claims_rule_based():
    answer = (
        "In my opinion, Mount Everest is 8,848.86 meters tall and it lies on the Nepal-China border. "
        "It was first summited in 1953."
    )
    claims = decompose_claims_rule_based(answer, item_id="item_001", query_en="How tall is Everest?")
    
    assert len(claims) >= 2
    # Verify claims are valid AtomicClaim instances
    for idx, c in enumerate(claims, 1):
        assert isinstance(c, AtomicClaim)
        assert c.claim_id == f"item_001_c{idx}"
        assert len(c.claim_text) > 0
        assert "In my opinion" not in c.claim_text

    # First claim should be critical
    assert claims[0].is_critical is True


def test_decompose_claims_empty_input():
    claims = decompose_claims_rule_based("", item_id="item_empty")
    assert claims == []

    claims_ws = decompose_claims_rule_based("   \n\t ", item_id="item_ws")
    assert claims_ws == []


def test_decompose_claims_mode_rule_based():
    answer = "Nepal defeated UAE by 8 wickets. Rohit Paudel scored 34 runs."
    claims = decompose_claims(answer, item_id="sports_01", mode="rule_based")
    assert len(claims) == 2
    assert claims[0].claim_id == "sports_01_c1"
    assert claims[1].claim_id == "sports_01_c2"
