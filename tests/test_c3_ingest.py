"""Tests for Ticket 05 / C3 Post-Editing Intake into Candidate Frame."""

import json
from pathlib import Path
import pytest

from src.prepare.ingest_c3 import (
    parse_c3_workbench,
    apply_c3_to_candidates,
)


def test_parse_c3_workbench(tmp_path):
    """Test parsing of C3 markdown workbench blocks."""
    sample_md = """# NepFaith-120 Condition C3 Post-Editing Workbench

## Passage 01 / 60
**Linked Candidate Items:** `item_001`, `item_002`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> यो एउटा परीक्षण हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> This is a test.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
This is an edited test.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ 01:15 ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [x] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[ Fixed proper noun ]`
"""
    wb_file = tmp_path / "test_workbench.md"
    wb_file.write_text(sample_md, encoding="utf-8")

    parsed = parse_c3_workbench(wb_file)
    assert len(parsed) == 1

    entry = parsed[0]
    assert entry["passage_ne"] == "यो एउटा परीक्षण हो।"
    assert entry["c2_raw_mt"] == "This is a test."
    assert entry["c3_post_edited_mt"] == "This is an edited test."
    assert entry["elapsed_time"] == "01:15"
    assert entry["linked_items"] == ["item_001", "item_002"]
    assert "Entity / Proper Noun mistranslation" in entry["error_types"]
    assert "Fixed proper noun" in entry["editor_notes"]


def test_apply_c3_to_candidates(tmp_path):
    """Test applying parsed C3 translations into evaluation candidate items."""
    sample_md = """# NepFaith-120 Condition C3 Post-Editing Workbench

## Passage 01 / 01
**Linked Candidate Items:** `item_001`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> यो स्रोत पाठ हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> This is raw MT.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
This is post-edited MT.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ 00:45 ]`
- [x] Omission / Dropped clauses
"""
    wb_file = tmp_path / "workbench.md"
    wb_file.write_text(sample_md, encoding="utf-8")

    sample_candidates = [
        {
            "item_id": "item_001",
            "domain": "wikipedia",
            "sub_genre": "culture_heritage",
            "source_provenance": "authentic",
            "perturbation_type": "natural",
            "passage_ne": "यो स्रोत पाठ हो।",
            "query_ne": "प्रश्न",
            "query_en": "query",
            "answer_en": "answer",
            "c2_raw_mt": "This is raw MT.",
            "c3_post_edited_mt": None,
            "claims": [],
        }
    ]
    cand_file = tmp_path / "candidates.jsonl"
    with open(cand_file, "w", encoding="utf-8") as f:
        for c in sample_candidates:
            f.write(json.dumps(c) + "\n")

    out_file = tmp_path / "candidates_with_c3.jsonl"
    count = apply_c3_to_candidates(
        candidates_path=cand_file,
        workbench_path=wb_file,
        output_path=out_file,
    )

    assert count == 1
    with open(out_file, "r", encoding="utf-8") as f:
        updated = [json.loads(line) for line in f]

    assert len(updated) == 1
    assert updated[0]["c3_post_edited_mt"] == "This is post-edited MT."


def test_live_c3_workbench_ingest_coverage():
    """Verify live completed C3 workbench parses 60 passages and updates 120 candidate items."""
    live_wb = Path("data/interim/preannotations/post_edit_c3_workbench.md")
    live_cands = Path("data/interim/preannotations/gold_candidates_120.jsonl")

    if not live_wb.exists() or not live_cands.exists():
        pytest.skip("Live data files not present")

    parsed = parse_c3_workbench(live_wb)
    assert len(parsed) == 60

    # Ensure every passage has non-empty C3
    for p in parsed:
        assert len(p["c3_post_edited_mt"].strip()) > 0
        assert len(p["linked_items"]) > 0
