"""Tests for Ticket 05: Condition C3 Human Post-Editing Workbench Setup."""

from pathlib import Path
import pytest


def test_export_c3_post_editing_workbench(tmp_path):
    """Verifies that the Condition C3 post-editing workbench is generated with side-by-side MT and editing slots."""
    from src.prepare.export_c3_workbench import export_c3_workbench

    candidates_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    if not candidates_path.exists():
        pytest.skip("gold_candidates_120.jsonl not found")

    out_file = tmp_path / "post_edit_c3_workbench.md"
    unique_count = export_c3_workbench(
        candidates_path=candidates_path,
        output_path=out_file,
    )

    assert out_file.exists()
    assert unique_count == 61  # Exactly 61 unique passages across 120 items

    content = out_file.read_text(encoding="utf-8")
    assert "NepFaith-120 Condition C3 Post-Editing Workbench" in content
    assert "Minimal-Pair Post-Editing Principles" in content
    assert "Raw IndicTrans2 MT (Condition C2)" in content
    assert "Human Post-Edited Translation (Condition C3 Slot)" in content
    assert "Stopwatch Elapsed Time:" in content
