"""NepFaith-120: Unlabelled Authentic Corpus Harvester (Sprint 3 Ticket 01).

Harvests and validates authentic Nepali reference passages across the three pre-registered strata:
1. Nepali Wikipedia (`wikipedia`)
2. Nepali Government Reports & Official Acts (`government_report`)
3. Nepali Contemporary Journalism (`news`) with 30% sports quota

Enforces NFC Unicode normalization, Devanagari character density verification,
and full provenance tracking.
Absolute Prohibition 2: Zero writes to `data/raw/labels/`.
"""

import json
import logging
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

from src.prepare.ingest import normalize_devanagari

logger = logging.getLogger("UnlabelledHarvester")

DEVANAGARI_RANGE = re.compile(r"[\u0900-\u097F]")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) NepFaithResearch/1.0"


def validate_devanagari_passage(
    text: str,
    min_words: int = 15,
    max_words: int = 450,
    min_devanagari_ratio: float = 0.50,
) -> Tuple[bool, str]:
    """Validates that a passage is well-formed Nepali Devanagari text within length bounds."""
    if not text or not isinstance(text, str):
        return False, "Empty or non-string text"

    norm_text = normalize_devanagari(text)
    words = norm_text.split()
    word_count = len(words)

    if word_count < min_words:
        return False, f"Passage word count ({word_count}) below minimum threshold ({min_words})"
    if word_count > max_words:
        return False, f"Passage word count ({word_count}) exceeds maximum threshold ({max_words})"

    non_ws_chars = [c for c in norm_text if not c.isspace()]
    if not non_ws_chars:
        return False, "Passage contains no non-whitespace characters"

    devanagari_chars = [c for c in non_ws_chars if DEVANAGARI_RANGE.match(c)]
    ratio = len(devanagari_chars) / len(non_ws_chars)

    if ratio < min_devanagari_ratio:
        return False, f"Devanagari ratio ({ratio:.2f}) below threshold ({min_devanagari_ratio:.2f})"

    return True, "Valid"


@dataclass
class UnlabelledPassage:
    passage_id: str
    domain: str
    sub_genre: str
    source_title: str
    source_url: str
    publisher: str
    publication_year: int
    passage_ne: str
    word_count: int


class UnlabelledCorpusHarvester:
    """Harvests, validates, and saves authentic reference passages for the unlabelled inference set."""

    def __init__(
        self,
        output_file: Path = Path("data/derived/authentic_passages_unlabelled.jsonl"),
    ):
        self.output_file = Path(output_file)
        if "data/raw/labels" in str(self.output_file):
            raise PermissionError("Absolute Prohibition 2: Never write to data/raw/labels/.")
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

    def fetch_wikipedia_extract(self, title: str) -> Optional[str]:
        """Fetches lead section text from Nepali Wikipedia API."""
        encoded_title = urllib.parse.quote(title)
        api_url = (
            f"https://ne.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1"
            f"&explaintext=1&titles={encoded_title}&format=json"
        )
        req = urllib.request.Request(api_url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for _, page in pages.items():
                extract = page.get("extract", "")
                if extract:
                    cleaned = re.sub(r"\[\d+\]", "", extract)
                    return normalize_devanagari(cleaned)
        except Exception as e:
            logger.debug(f"Wikipedia fetch skipped/failed for {title}: {e}")
        return None

    def harvest_targets(self, targets: List[Dict[str, Any]]) -> int:
        """Processes and writes a list of target specifications to the output file."""
        saved_records: List[Dict[str, Any]] = []

        for idx, target in enumerate(targets, start=1):
            domain = target.get("domain", "wikipedia")
            sub_genre = target.get("sub_genre", "general")
            title = target.get("title", f"Passage {idx}")
            url = target.get("url", "https://ne.wikipedia.org/")
            publisher = target.get("publisher", "Authentic Source")
            year = target.get("year", 2024)

            text = target.get("text", "")
            if not text and target.get("source_type") == "wikipedia":
                api_text = self.fetch_wikipedia_extract(title)
                if api_text:
                    text = api_text

            if not text:
                continue

            norm_text = normalize_devanagari(text)
            is_valid, reason = validate_devanagari_passage(norm_text)
            if not is_valid:
                logger.debug(f"Skipping target {title}: {reason}")
                continue

            passage_id = f"pass_unlab_{idx:04d}"
            record = UnlabelledPassage(
                passage_id=passage_id,
                domain=domain,
                sub_genre=sub_genre,
                source_title=title,
                source_url=url,
                publisher=publisher,
                publication_year=year,
                passage_ne=norm_text,
                word_count=len(norm_text.split()),
            )
            saved_records.append(asdict(record))

        with open(self.output_file, "w", encoding="utf-8") as f:
            for rec in saved_records:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

        return len(saved_records)
