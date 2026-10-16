"""NepFaith-120: Batch Translation Runner for Condition C2

Executes IndicTrans2 (ai4bharat/indictrans2-indic-en-dist-200M) locally on GPU/CPU
to generate raw machine translations (p_c2) for candidate evaluation items:
Δ_MT = A(C3) - A(C2)

Features:
- Deterministic SHA-256 disk caching under cache/translations/.
- Batch deduplication: translates unique passages once and maps back.
- Physical label isolation: Zero writes to data/raw/labels/.
- C3 and gold labels strictly untouched.
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

from src.run.translate import IndicTrans2Translator

logger = logging.getLogger("BatchC2Translator")


class BatchC2Translator:
    """Batch translation runner populating Condition C2 raw MT across candidate items."""

    def __init__(
        self,
        input_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl"),
        output_path: Optional[Path] = None,
        cache_dir: Path = Path("cache/translations"),
        batch_size: int = 8,
    ):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path or input_path)
        self.cache_dir = Path(cache_dir)
        self.batch_size = batch_size
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def run(self) -> List[Dict[str, Any]]:
        # Hard Rule: Physical label isolation
        assert "data/raw/labels" not in str(self.output_path), "PROHIBITION: Cannot write candidate C2 translations to gold label path"

        if not self.input_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_path}")

        items: List[Dict[str, Any]] = []
        with open(self.input_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    items.append(json.loads(line))

        # Collect unique passages to optimize translation throughput
        unique_passages = list(dict.fromkeys(it["passage_ne"].strip() for it in items if it.get("passage_ne")))
        logger.info(f"Loaded {len(items)} items containing {len(unique_passages)} unique passages for C2 translation.")

        # Run translation via IndicTrans2Translator with disk cache
        translator = IndicTrans2Translator(cache_dir=self.cache_dir)
        translations = translator.translate_batch(unique_passages, use_cache=True, batch_size=self.batch_size)
        passage_to_mt = dict(zip(unique_passages, translations))

        # Populate c2_raw_mt on all items
        for it in items:
            p_ne = it["passage_ne"].strip()
            it["c2_raw_mt"] = passage_to_mt.get(p_ne, "")

        # Write populated items back
        with open(self.output_path, "w", encoding="utf-8") as out:
            for it in items:
                out.write(json.dumps(it, ensure_ascii=False) + "\n")

        logger.info(f"Successfully populated Condition C2 raw MT on {len(items)} items at {self.output_path}")
        return items


if __name__ == "__main__":
    runner = BatchC2Translator()
    processed = runner.run()
    print(f"Condition C2 batch translation complete: {len(processed)} items updated.")
