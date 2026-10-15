"""Tests for 7-Type Perturbation Engine."""

import pytest
from src.prepare.schema import PerturbationType
from src.prepare.perturb import apply_perturbation


SAMPLE_ANSWERS = {
    PerturbationType.ENTITY_SWAP: "Chitwan National Park is located in the southern plains of Nepal.",
    PerturbationType.NUMBER_DATE_ALTERATION: "In 2023, the remittance inflow reached 25.3% growth.",
    PerturbationType.NEGATION_FLIP: "The government was supportive of the new agricultural policy.",
    PerturbationType.MISATTRIBUTION: "According to Nepal Rastra Bank, the foreign exchange reserve increased.",
    PerturbationType.REGISTER_SHIFT: "The Prime Minister addressed the annual session of parliament.",
    PerturbationType.UNSUPPORTED_ADDITION: "Lumbini is the birthplace of Gautam Buddha.",
    PerturbationType.INVENTED_CAUSALITY: "Heavy rainfall occurred in Kathmandu. The stock exchange index fell by 30 points.",
}


def test_all_seven_perturbations():
    for p_type, base_text in SAMPLE_ANSWERS.items():
        perturbed, span = apply_perturbation(base_text, perturbation_type=p_type, seed=123)
        assert perturbed != base_text, f"Perturbation {p_type.value} failed to modify text"
        assert len(span) > 0, f"Perturbation {p_type.value} did not record a span"


def test_determinism():
    base_text = "Chitwan National Park protects one-horned rhinos."
    p1, s1 = apply_perturbation(base_text, PerturbationType.ENTITY_SWAP, seed=42)
    p2, s2 = apply_perturbation(base_text, PerturbationType.ENTITY_SWAP, seed=42)
    assert p1 == p2
    assert s1 == s2
