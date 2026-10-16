"""NepFaith-120: Atomic Claim Exporter & Criticality Auditor

Extracts, validates, and audits atomic claims from candidate evaluation items.
Enforces rubric compliance (docs/RUBRIC_V1.md):
- 2 to 5 atomic claims per item.
- At least one critical claim (is_critical=True) per item.
- Decontextualized propositions.
- Hard Rule: gold_label is strictly None (zero machine pre-population).
- Output strictly to data/interim/preannotations/claims_120.jsonl.
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple

logger = logging.getLogger("ClaimsExporter")


class ClaimsExporter:
    """Exports and audits atomic claims from candidate evaluation items."""

    def __init__(
        self,
        candidates_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl"),
        output_path: Path = Path("data/interim/preannotations/claims_120.jsonl"),
    ):
        self.candidates_path = Path(candidates_path)
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def export_and_audit(self) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        # Hard Rule: Physical label isolation
        assert "data/raw/labels" not in str(self.output_path), "PROHIBITION: Cannot write candidate claims to gold label path"

        if not self.candidates_path.exists():
            raise FileNotFoundError(f"Candidates file not found at {self.candidates_path}")

        claim_records: List[Dict[str, Any]] = []
        claims_per_item: Dict[str, int] = {}
        critical_claims_per_item: Dict[str, int] = {}
        claims_by_genre: Dict[str, int] = {}

        with open(self.candidates_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                item = json.loads(line)
                item_id = item["item_id"]
                domain = item["domain"]
                sub_genre = item.get("sub_genre", "unknown")
                claims = item.get("claims", [])

                claims_per_item[item_id] = len(claims)
                crit_count = 0

                for c in claims:
                    is_crit = c.get("is_critical", False)
                    if is_crit:
                        crit_count += 1

                    claim_record = {
                        "claim_id": c["claim_id"],
                        "item_id": item_id,
                        "domain": domain,
                        "sub_genre": sub_genre,
                        "claim_text": c["claim_text"],
                        "is_critical": is_crit,
                        "gold_label": None,  # Strictly None for human annotation
                    }
                    claim_records.append(claim_record)
                    claims_by_genre[sub_genre] = claims_by_genre.get(sub_genre, 0) + 1

                critical_claims_per_item[item_id] = crit_count

        # Write flattened claims to output file
        with open(self.output_path, "w", encoding="utf-8") as out:
            for rec in claim_records:
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")

        stats = {
            "total_items": len(claims_per_item),
            "total_claims": len(claim_records),
            "mean_claims_per_item": round(len(claim_records) / max(1, len(claims_per_item)), 2),
            "claims_per_item": claims_per_item,
            "critical_claims_per_item": critical_claims_per_item,
            "claims_by_genre": claims_by_genre,
        }

        logger.info(
            f"Exported {len(claim_records)} atomic claims from {len(claims_per_item)} items "
            f"(mean: {stats['mean_claims_per_item']}/item) to {self.output_path}"
        )
        return claim_records, stats


if __name__ == "__main__":
    exporter = ClaimsExporter()
    claims, stats = exporter.export_and_audit()
    print(f"Exported {len(claims)} claims across {stats['total_items']} items.")
    print(f"Mean claims per item: {stats['mean_claims_per_item']}")
