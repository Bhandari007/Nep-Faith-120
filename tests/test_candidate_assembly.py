"""Tests for Ticket 01: Stratified Candidate Assembly (120 Items across 10 Domains)."""

import json
from pathlib import Path
import pytest
from src.prepare.schema import Domain, Provenance, PerturbationType, EvaluationItem


def test_candidate_assembly_invariants(tmp_path):
    """Verifies that assemble_120_candidates produces the exact pre-registered stratification."""
    from src.prepare.assemble_candidates import CandidateAssembler

    output_file = tmp_path / "gold_candidates_120.jsonl"
    assembler = CandidateAssembler(output_path=output_file)
    items = assembler.assemble()

    # 1. Total Count Invariant
    assert len(items) == 120, f"Expected exactly 120 items, got {len(items)}"
    assert output_file.exists()

    # 2. Macro-Stratification (40 / 40 / 40)
    domain_counts = {}
    for it in items:
        domain_counts[it.domain] = domain_counts.get(it.domain, 0) + 1

    assert domain_counts[Domain.WIKIPEDIA] == 40, f"Expected 40 Wikipedia items, got {domain_counts.get(Domain.WIKIPEDIA)}"
    assert domain_counts[Domain.GOVERNMENT_REPORT] == 40, f"Expected 40 Gov Report items, got {domain_counts.get(Domain.GOVERNMENT_REPORT)}"
    assert domain_counts[Domain.NEWS] == 40, f"Expected 40 News items, got {domain_counts.get(Domain.NEWS)}"

    # 3. Approved 10-Domain Topical Quotas
    expected_sub_genres = {
        "health": 10,
        "agriculture": 10,
        "education": 10,
        "economy_finance": 10,
        "disaster_geography": 10,
        "governance_law": 10,
        "sports": 12,
        "culture_heritage": 15,
        "biodiversity_parks": 15,
        "infrastructure_tourism": 18,
    }
    actual_sub_genres = {}
    for it in items:
        sg = getattr(it, "sub_genre", None)
        actual_sub_genres[sg] = actual_sub_genres.get(sg, 0) + 1

    for sg, expected_count in expected_sub_genres.items():
        assert actual_sub_genres.get(sg) == expected_count, (
            f"Sub-genre '{sg}' expected {expected_count}, got {actual_sub_genres.get(sg)}"
        )

    # 4. Provenance Balance: Exactly 60 Natural / 60 Perturbed
    provenance_counts = {}
    perturbation_counts = {}
    for it in items:
        provenance_counts[it.source_provenance] = provenance_counts.get(it.source_provenance, 0) + 1
        if it.source_provenance == Provenance.PERTURBED:
            perturbation_counts[it.perturbation_type] = perturbation_counts.get(it.perturbation_type, 0) + 1

    assert provenance_counts[Provenance.NATURAL] == 60, f"Expected 60 natural items, got {provenance_counts.get(Provenance.NATURAL)}"
    assert provenance_counts[Provenance.PERTURBED] == 60, f"Expected 60 perturbed items, got {provenance_counts.get(Provenance.PERTURBED)}"

    # All 7 perturbation types must be represented
    for p_type in PerturbationType:
        assert perturbation_counts.get(p_type, 0) >= 8, f"Perturbation type {p_type} underrepresented: {perturbation_counts.get(p_type, 0)}"

    # 5. Schema Validation & Critical Claim Invariant
    for it in items:
        assert it.item_id.startswith("item_")
        assert len(it.passage_ne.strip()) > 30
        assert len(it.query_en.strip()) > 10
        assert len(it.answer_en.strip()) > 10
        assert it.source_url is not None and it.source_url.startswith("http"), f"Item {it.item_id} missing valid http source_url"
        assert it.source_title is not None and len(it.source_title) > 3, f"Item {it.item_id} missing source_title"
        assert len(it.claims) >= 2, f"Item {it.item_id} has fewer than 2 claims"
        assert any(c.is_critical for c in it.claims), f"Item {it.item_id} has zero critical claims"

        # Hard Rule: No gold labels assigned by machine in candidate pool
        for c in it.claims:
            assert c.gold_label is None, f"Gold label must not be populated in candidate pre-annotations for {c.claim_id}"
