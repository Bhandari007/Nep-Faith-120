"""NepFaith-120: Condition C3 Human Post-Editing Workbench Exporter (Ticket 05)

Generates the minimal-pair human post-editing workbench under data/interim/preannotations/
to allow rapid, consistent post-editing of IndicTrans2 raw MT (p_c2) into gold post-edited MT (p_c3):
Δ_MT = A(C3) - A(C2)

Features:
- Groups items by unique reference passages (61 unique passages across 120 items).
- Side-by-side presentation of Source Nepali (p_ne) and Raw IndicTrans2 MT (p_c2).
- Editable slot pre-populated with p_c2 so post-editors only correct translation errors (minimal edit distance).
- Explicit minimal-pair post-editing guidelines (aspect collapse, evidentials, polarity, entity names).
- Stopwatch timing and error taxonomy categorization checkboxes.
- Absolute prohibition: Zero writes to data/raw/labels/.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional


C3_WORKBENCH_HEADER = """# NepFaith-120 Condition C3 Post-Editing Workbench

**Version:** 1.0 (Locked Protocol)  
**Editor:** Human Bilingual Post-Editor  
**Target:** 60 Unique Reference Passages (spanning all 120 candidate items)  
**Storage Protocol:** Save completed post-edits directly to `data/interim/preannotations/post_edit_c3_workbench.md`.

---

## Minimal-Pair Post-Editing Principles
The purpose of Condition $C3$ is to compute the pure Machine Translation Error Gap:
$$\\Delta_{\\text{MT}} = A(C3) - A(C2)$$
To ensure that $C3$ differs from $C2$ **only** by the absence of translation errors (and not by human stylistic embellishments), adhere strictly to these rules:

1. **Minimal Edit Distance**: Start with the Raw IndicTrans2 translation ($p_{c2}$) and edit **only** what is factually, syntactically, or semantically incorrect. Do not rephrase well-formed sentences simply to improve style or prose.
2. **Entity & Number Precision**: Fix mistranslated numbers, years, currencies, and proper nouns (e.g., if "सन् १९७९" was translated as "2001", fix it to "1979").
3. **Evidentials & Epistemic Stance**: Preserve evidential markers and modal qualifiers present in Nepali (e.g., "भनिन्छ", "दाबी गरिएको छ").
4. **Negation & Polarities**: Ensure negation particles (e.g., "छैन", "हुँदैन") are accurately reflected in English without polarity inversion.
5. **No Edit Needed**: If the raw MT is fluent, accurate, and contains no translation errors, leave the editable slot unchanged and check `[X] Clean / No edit needed`.
6. **Stopwatch Duration**: Record the elapsed time (`mm:ss`) spent on each passage.

---
"""


def format_passage_block(
    passage_idx: int,
    total_passages: int,
    passage_ne: str,
    c2_raw_mt: str,
    linked_items: List[str],
    domain: str,
    sub_genre: str,
    source_title: Optional[str] = None,
    source_url: Optional[str] = None,
) -> str:
    """Formats a single passage into a side-by-side minimal-pair post-editing block."""
    items_str = ", ".join(f"`{item_id}`" for item_id in linked_items)
    meta_line = f"**Domain:** {domain} | **Topic Sub-Genre:** {sub_genre}"
    if source_title:
        meta_line += f" | **Source:** [{source_title}]({source_url})" if source_url else f" | **Source:** {source_title}"

    lines = [
        f"## Passage {passage_idx:02d} / {total_passages}",
        f"**Linked Candidate Items:** {items_str}",
        meta_line,
        "",
        "### 1. Source Passage (Nepali · Condition C1)",
        f"> {passage_ne}",
        "",
        "### 2. Raw IndicTrans2 MT (Condition C2)",
        f"> {c2_raw_mt}",
        "",
        "### 3. Human Post-Edited Translation (Condition C3 Slot)",
        "> *Edit the text below to fix translation errors while preserving phrasing:*",
        f"```text\n{c2_raw_mt}\n```",
        "",
        "### 4. Post-Editing Metadata",
        "**Stopwatch Elapsed Time:** `[ mm:ss ]`",
        "",
        "**Error Types Corrected in this Passage (Select all that apply):**",
        "- [ ] Entity / Proper Noun mistranslation",
        "- [ ] Number / Date / Metric distortion",
        "- [ ] Omission / Dropped clauses",
        "- [ ] Polarity / Negation flip",
        "- [ ] Tense / Aspect collapse",
        "- [ ] Evidential / Epistemic stance distortion",
        "- [ ] Clean / No edit needed (Raw MT is faithful and accurate)",
        "",
        "**Editor Notes / Justification:** `[                                                 ]`",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def export_c3_workbench(
    candidates_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl"),
    output_path: Path = Path("data/interim/preannotations/post_edit_c3_workbench.md"),
) -> int:
    """Extracts unique passages from candidate items and exports the Condition C3 post-editing workbench."""
    assert "data/raw/labels" not in str(output_path), "PROHIBITION: Cannot write directly to gold label directory"

    candidates_path = Path(candidates_path)
    output_path = Path(output_path)
    if not candidates_path.exists():
        raise FileNotFoundError(f"Candidate file not found: {candidates_path}")

    items: List[Dict[str, Any]] = []
    with open(candidates_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))

    # Deduplicate passages in order of appearance
    unique_passages: Dict[str, Dict[str, Any]] = {}
    for it in items:
        p_ne = it["passage_ne"].strip()
        if p_ne not in unique_passages:
            unique_passages[p_ne] = {
                "passage_ne": p_ne,
                "c2_raw_mt": it.get("c2_raw_mt", "").strip(),
                "linked_items": [it["item_id"]],
                "domain": it.get("domain", "unknown"),
                "sub_genre": it.get("sub_genre", "general"),
                "source_title": it.get("source_title"),
                "source_url": it.get("source_url"),
            }
        else:
            unique_passages[p_ne]["linked_items"].append(it["item_id"])

    # Build workbench markdown
    lines = [C3_WORKBENCH_HEADER]
    total_unique = len(unique_passages)
    for idx, (_, p_data) in enumerate(unique_passages.items(), start=1):
        lines.append(
            format_passage_block(
                passage_idx=idx,
                total_passages=total_unique,
                passage_ne=p_data["passage_ne"],
                c2_raw_mt=p_data["c2_raw_mt"],
                linked_items=p_data["linked_items"],
                domain=p_data["domain"],
                sub_genre=p_data["sub_genre"],
                source_title=p_data.get("source_title"),
                source_url=p_data.get("source_url"),
            )
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return len(unique_passages)


if __name__ == "__main__":
    count = export_c3_workbench()
    print(f"Exported Condition C3 post-editing workbench with {count} unique passages.")
