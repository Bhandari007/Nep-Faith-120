"""Tests for Ticket 04: Dual-Annotation Workbench Setup."""

from pathlib import Path
import pytest


def test_export_dual_annotation_workbenches(tmp_path):
    """Verifies that dual annotation workbenches are exported correctly for human annotators."""
    from src.prepare.export_workbenches import export_annotation_workbenches

    candidates_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    if not candidates_path.exists():
        pytest.skip("gold_candidates_120.jsonl not found")

    out_1 = tmp_path / "workbench_annotator_1.md"
    out_2 = tmp_path / "workbench_annotator_2.md"

    export_annotation_workbenches(
        candidates_path=candidates_path,
        output_annotator_1=out_1,
        output_annotator_2=out_2,
    )

    assert out_1.exists()
    assert out_2.exists()

    content_1 = out_1.read_text(encoding="utf-8")
    content_2 = out_2.read_text(encoding="utf-8")

    # Invariant: Contains instructions and Rubric reference
    assert "NepFaith-120 Human Annotation Workbench" in content_1
    assert "Annotator 1" in content_1
    assert "Annotator 2" in content_2

    # Invariant: Contains all 120 items
    for item_idx in range(1, 121):
        item_id = f"item_{item_idx:03d}"
        assert f"## Item: `{item_id}`" in content_1
        assert f"## Item: `{item_id}`" in content_2

    # Invariant: Contains options, timing, and claim checkboxes
    assert "[ ] Supported" in content_1
    assert "[ ] Contradicted" in content_1
    assert "[ ] Not-in-context" in content_1
    assert "Stopwatch Elapsed Time:" in content_1

    # Invariant: Blinded from annotators (perturbation type not revealed in item body)
    assert "entity_swap" not in content_1
    assert "invented_causality" not in content_1
