"""NepFaith-120: Human Annotation Workbench Exporter (Ticket 04)

Generates human-friendly dual-annotation markdown sheets for Annotator 1 and Annotator 2
under data/interim/preannotations/ to allow friction-free, blinded annotation.

Invariants:
- Zero writes to data/raw/labels/ (physical label isolation).
- Evaluators are strictly blinded to perturbation types and synthetic spans.
- Claims explicitly demarcated with [CRITICAL] or [NON-CRITICAL] indicators.
- Stopwatch timing and justification notes fields included for every item.
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional


ANNOTATION_GUIDELINES_HEADER = """# NepFaith-120 Human Annotation Workbench ({annotator_name})

**Version:** 1.0 (Locked Protocol)  
**Annotator:** {annotator_name}  
**Reference Document:** `docs/RUBRIC_V1.md` and `docs/PILOT_ANNOTATION_SHEET.md`  
**Storage Protocol:** Save completed annotations to `data/interim/preannotations/workbench_{annotator_slug}.md`. (Do not write directly to `data/raw/labels/`).

---

## Instructions for Human Annotators
1. **Core Task**: Read the **Nepali Context Passage** ($p_{ne}$) and the **English Generated Answer** ($a_{en}$).
2. **Atomic Claim Evaluation**: For every atomic claim listed under the answer, evaluate its factual consistency with the Nepali context passage:
   - `[X] Supported`: The claim is directly stated or logically entailed by the Nepali passage.
   - `[X] Contradicted`: The claim directly contradicts facts explicitly asserted in the Nepali passage.
   - `[X] Not-in-context`: The claim makes assertions completely absent, ungrounded, or unverifiable from the Nepali passage (hallucination/extrapolation).
3. **Criticality**: Claims marked `[CRITICAL]` represent essential, core factual propositions. Non-critical claims represent secondary background details.
4. **Stopwatch Timing**: Record the elapsed annotation time (`mm:ss`) using a standard stopwatch for each item.
5. **Marking**: Replace `[ ]` with `[X]` for your chosen verdict.

---
"""


def format_item_markdown(item: Dict[str, Any], item_index: int) -> str:
    """Formats a single candidate item into a blinded human annotation section."""
    item_id = item["item_id"]
    domain = item.get("domain", "unknown")
    sub_genre = item.get("sub_genre", "general")
    passage_ne = item.get("passage_ne", "").strip()
    query_en = item.get("query_en", "").strip()
    answer_en = item.get("answer_en", "").strip()
    claims = item.get("claims", [])

    source_title = item.get("source_title")
    source_url = item.get("source_url")
    meta_line = f"**Domain:** {domain} | **Topic Sub-Genre:** {sub_genre}"
    if source_title:
        meta_line += f" | **Source:** [{source_title}]({source_url})" if source_url else f" | **Source:** {source_title}"

    lines = [
        f"## Item: `{item_id}` ({item_index}/120)",
        meta_line,
        "",
        "### Context Passage (Nepali · Condition C1)",
        f"> {passage_ne}",
        "",
        "### User Query (English)",
        f"**Q:** {query_en}",
        "",
        "### Generated Answer (English)",
        f"**A:** {answer_en}",
        "",
        "### Atomic Claims Evaluation",
        "",
    ]

    for c_idx, claim in enumerate(claims, start=1):
        claim_id = claim.get("claim_id", f"{item_id}_c{c_idx}")
        claim_text = claim.get("claim_text", "").strip()
        is_critical = claim.get("is_critical", False)
        crit_tag = "**[CRITICAL CLAIM]**" if is_critical else "*[NON-CRITICAL CLAIM]*"

        lines.extend([
            f"#### Claim {c_idx}: `{claim_id}` {crit_tag}",
            f"> \"{claim_text}\"",
            "",
            "Select one verdict:",
            "- [ ] Supported",
            "- [ ] Contradicted",
            "- [ ] Not-in-context",
            "",
            "Rationale / Notes: [                                                 ]",
            "",
        ])

    lines.extend([
        "### Item Annotation Metadata",
        "Stopwatch Elapsed Time: [ mm:ss ]",
        "Item Notes: [                                                 ]",
        "",
        "---",
        "",
    ])

    return "\n".join(lines)


def export_annotation_workbenches(
    candidates_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl"),
    output_annotator_1: Path = Path("data/interim/preannotations/workbench_annotator_1.md"),
    output_annotator_2: Path = Path("data/interim/preannotations/workbench_annotator_2.md"),
):
    """Exports dual annotation workbenches from the candidate 120 dataset."""
    assert "data/raw/labels" not in str(output_annotator_1), "PROHIBITION: Cannot write directly to gold label directory"
    assert "data/raw/labels" not in str(output_annotator_2), "PROHIBITION: Cannot write directly to gold label directory"

    candidates_path = Path(candidates_path)
    if not candidates_path.exists():
        raise FileNotFoundError(f"Candidate file not found: {candidates_path}")

    items: List[Dict[str, Any]] = []
    with open(candidates_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))

    # Build contents for Annotator 1
    header_1 = (
        ANNOTATION_GUIDELINES_HEADER
        .replace("{annotator_name}", "Annotator 1")
        .replace("{annotator_slug}", "annotator_1")
    )
    content_a1 = [header_1]
    for idx, it in enumerate(items, start=1):
        content_a1.append(format_item_markdown(it, idx))

    # Build contents for Annotator 2
    header_2 = (
        ANNOTATION_GUIDELINES_HEADER
        .replace("{annotator_name}", "Annotator 2")
        .replace("{annotator_slug}", "annotator_2")
    )
    content_a2 = [header_2]
    for idx, it in enumerate(items, start=1):
        content_a2.append(format_item_markdown(it, idx))

    output_annotator_1 = Path(output_annotator_1)
    output_annotator_2 = Path(output_annotator_2)
    output_annotator_1.parent.mkdir(parents=True, exist_ok=True)
    output_annotator_2.parent.mkdir(parents=True, exist_ok=True)

    output_annotator_1.write_text("\n".join(content_a1), encoding="utf-8")
    output_annotator_2.write_text("\n".join(content_a2), encoding="utf-8")


if __name__ == "__main__":
    export_annotation_workbenches()
    print("Exported dual-annotation workbenches for Annotator 1 and Annotator 2.")
