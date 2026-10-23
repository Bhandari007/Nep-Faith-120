"""NepFaith-120: Condition C3 Human Post-Editing Ingestion Module.

Ingests completed minimal-pair post-edits from `data/interim/preannotations/post_edit_c3_workbench.md`
into the candidate evaluation frame `data/interim/preannotations/gold_candidates_120.jsonl`.
Strictly respects Absolute Prohibition 2: No writes to `data/raw/labels/`.
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional


def parse_c3_workbench(workbench_path: Path) -> List[Dict[str, Any]]:
    """Parses all passage blocks from a Condition C3 post-editing markdown workbench."""
    text = workbench_path.read_text(encoding="utf-8")
    blocks = text.split("## Passage ")[1:]

    parsed_entries: List[Dict[str, Any]] = []

    for block in blocks:
        # Linked Candidate Items
        items_match = re.search(r"\*\*Linked Candidate Items:\*\*\s*(.*?)(?:\n|$)", block)
        linked_items = []
        if items_match:
            linked_items = [
                tok.strip("` ,")
                for tok in re.findall(r"`item_\d+`", items_match.group(1))
            ]

        # Source Passage (C1)
        p_ne_match = re.search(
            r"### 1\. Source Passage \(Nepali · Condition C1\)\n>\s*(.*?)(?=\n\n### 2|\n### 2)",
            block,
            re.DOTALL,
        )
        passage_ne = p_ne_match.group(1).strip() if p_ne_match else ""

        # Raw IndicTrans2 MT (C2)
        c2_match = re.search(
            r"### 2\. Raw IndicTrans2 MT \(Condition C2\)\n>\s*(.*?)(?=\n\n### 3|\n### 3)",
            block,
            re.DOTALL,
        )
        c2_raw_mt = c2_match.group(1).strip() if c2_match else ""

        # Human Post-Edited Translation (C3 Slot)
        c3_match = re.search(
            r"### 3\. Human Post-Edited Translation \(Condition C3 Slot\).*?```text\n(.*?)\n```",
            block,
            re.DOTALL,
        )
        c3_post_edited_mt = c3_match.group(1).strip() if c3_match else ""

        # Stopwatch Elapsed Time
        time_match = re.search(
            r"\*\*Stopwatch Elapsed Time:\*\*\s*`\[\s*(.*?)\s*\]`",
            block,
        )
        elapsed_time = time_match.group(1).strip() if time_match else ""
        if elapsed_time == "mm:ss":
            elapsed_time = ""

        # Checked Error Types
        error_types = [
            m.strip()
            for m in re.findall(r"- \[[xX]\] (.*)", block)
        ]

        # Editor Notes
        notes_match = re.search(
            r"\*\*Editor Notes / Justification:\*\*\s*`\[\s*(.*?)\s*\]`",
            block,
        )
        editor_notes = notes_match.group(1).strip() if notes_match else ""

        parsed_entries.append({
            "linked_items": linked_items,
            "passage_ne": passage_ne,
            "c2_raw_mt": c2_raw_mt,
            "c3_post_edited_mt": c3_post_edited_mt,
            "elapsed_time": elapsed_time,
            "error_types": error_types,
            "editor_notes": editor_notes,
        })

    return parsed_entries


def apply_c3_to_candidates(
    candidates_path: Path,
    workbench_path: Path,
    output_path: Optional[Path] = None,
) -> int:
    """Applies parsed C3 post-edited translations into the candidate items JSONL."""
    parsed_passages = parse_c3_workbench(workbench_path)

    # Build lookup table: item_id -> c3_text, and fallback normalized passage_ne -> c3_text
    item_to_c3: Dict[str, str] = {}
    passage_to_c3: Dict[str, str] = {}

    for entry in parsed_passages:
        c3_text = entry["c3_post_edited_mt"]
        for it_id in entry["linked_items"]:
            item_to_c3[it_id] = c3_text
        norm_passage = " ".join(entry["passage_ne"].split())
        passage_to_c3[norm_passage] = c3_text

    items: List[Dict[str, Any]] = []
    with open(candidates_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))

    matched_count = 0
    for it in items:
        it_id = it.get("item_id")
        norm_p = " ".join((it.get("passage_ne") or "").split())
        c3_text = item_to_c3.get(it_id) or passage_to_c3.get(norm_p)
        if c3_text is not None:
            it["c3_post_edited_mt"] = c3_text
            matched_count += 1

    dest = output_path or candidates_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")

    return matched_count


if __name__ == "__main__":
    wb_file = Path("data/interim/preannotations/post_edit_c3_workbench.md")
    cand_file = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    updated = apply_c3_to_candidates(cand_file, wb_file)
    print(f"Successfully ingested C3 post-edits for {updated} items.")
