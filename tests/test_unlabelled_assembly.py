"""Tests for Sprint 3 Ticket 02: Unlabelled 1,200 Item Assembly & Stratification."""

import json
from pathlib import Path
import pytest

from src.prepare.assemble_unlabelled import assemble_unlabelled_corpus
from src.prepare.schema import Domain, PerturbationType


def test_assemble_unlabelled_corpus(tmp_path):
    """Verifies that the unlabelled 1,200 corpus strictly adheres to pre-registered stratification."""
    out_file = tmp_path / "unlabelled_1200.jsonl"
    total_items = assemble_unlabelled_corpus(output_path=out_file)

    assert total_items == 1200
    assert out_file.exists()

    items = []
    with open(out_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))

    assert len(items) == 1200

    # 1. Stratification Checks: 400 items per macro-stratum
    domain_counts = {}
    sports_count = 0
    natural_count = 0
    perturbed_counts = {}
    total_claims = 0

    for it in items:
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

        # Check claims
        claims = it.get("claims", [])
        assert len(claims) >= 2, f"Item {it['item_id']} has fewer than 2 claims"
        assert len(claims) <= 5, f"Item {it['item_id']} has more than 5 claims"
        total_claims += len(claims)
        for cl in claims:
            assert "is_critical" in cl
            assert isinstance(cl["is_critical"], bool)
            assert len(cl["claim_text"].strip()) > 0

    assert domain_counts.get("wikipedia") == 400
    assert domain_counts.get("government_report") == 400
    assert domain_counts.get("news") == 400

    # 2. Sports Quota in News (Mandatory 30% = 120 items)
    assert sports_count == 120, f"Expected 120 sports items, got {sports_count}"

    # 3. Provenance Balance: Exactly 50% Natural / 50% Perturbed
    assert natural_count == 600, f"Expected 600 natural items, got {natural_count}"
    assert sum(perturbed_counts.values()) == 600

    # 4. All 7 Perturbation Types Represented
    assert len(perturbed_counts) == 7
    for pt in [
        PerturbationType.ENTITY_SWAP.value,
        PerturbationType.NUMBER_DATE_ALTERATION.value,
        PerturbationType.NEGATION_FLIP.value,
        PerturbationType.MISATTRIBUTION.value,
        PerturbationType.REGISTER_SHIFT.value,
        PerturbationType.UNSUPPORTED_ADDITION.value,
        PerturbationType.INVENTED_CAUSALITY.value,
    ]:
        assert perturbed_counts.get(pt, 0) >= 80

    # 5. Claim Scale Bounds (~3,000–4,500 claims)
    assert 2800 <= total_claims <= 4800, f"Total claims {total_claims} out of expected range"
