"""Tests for BibTeX Citation Verification and Human Verification Tags.

Enforces Pillar 4 of docs/WORKFLOW.md and AGENTS.md:
Every BibTeX entry must include `verified_by = {Initials, YYYY-MM-DD}` confirming
human check of the primary source.
"""

import re
from pathlib import Path
import pytest


def parse_bibtex_entries(bib_path: Path):
    """Parses BibTeX file and yields (entry_type, cite_key, fields_dict)."""
    text = bib_path.read_text(encoding="utf-8")
    raw_entries = re.findall(r"@(\w+)\s*\{\s*([^,]+),([^@]*)\}", text, re.DOTALL)
    
    parsed = []
    for entry_type, cite_key, body in raw_entries:
        fields = {}
        for line in body.splitlines():
            m = re.match(r"\s*(\w+)\s*=\s*\{([^}]*)\}", line)
            if m:
                fields[m.group(1).lower()] = m.group(2).strip()
        parsed.append((entry_type.strip(), cite_key.strip(), fields))
    return parsed


def test_bibtex_file_exists():
    bib_path = Path("paper/references.bib")
    assert bib_path.exists(), "paper/references.bib must exist."


def test_all_entries_have_human_verification():
    """Verifies that every entry has a valid verified_by = {Initials, YYYY-MM-DD} tag."""
    bib_path = Path("paper/references.bib")
    entries = parse_bibtex_entries(bib_path)
    assert len(entries) >= 5, "Expected at least 5 primary source citations in references.bib."

    verification_pattern = re.compile(r"^[A-Z]{2,3},\s*\d{4}-\d{2}-\d{2}$")

    for entry_type, cite_key, fields in entries:
        assert "verified_by" in fields, (
            f"Entry @{entry_type}{{{cite_key}}} is missing mandatory 'verified_by' tag."
        )
        tag = fields["verified_by"]
        assert verification_pattern.match(tag), (
            f"Entry @{entry_type}{{{cite_key}}} has invalid 'verified_by' format: '{tag}'. "
            f"Expected '{{Initials, YYYY-MM-DD}}'."
        )


def test_all_entries_have_required_fields():
    """Verifies that every entry has author, title, and year fields."""
    bib_path = Path("paper/references.bib")
    entries = parse_bibtex_entries(bib_path)

    for entry_type, cite_key, fields in entries:
        assert "author" in fields and fields["author"], f"Entry {cite_key} missing author."
        assert "title" in fields and fields["title"], f"Entry {cite_key} missing title."
        assert "year" in fields and fields["year"], f"Entry {cite_key} missing year."


def test_no_unverified_citations_in_manuscript():
    """Verifies that every citation in paper/manuscript.tex is verified."""
    manuscript_path = Path("paper/manuscript.tex")
    if not manuscript_path.exists():
        pytest.skip("paper/manuscript.tex does not exist yet.")

    content = manuscript_path.read_text(encoding="utf-8")
    bib_path = Path("paper/references.bib")
    entries = {k: f for _, k, f in parse_bibtex_entries(bib_path)}

    for match in re.findall(r"\\cite\{([^}]+)\}", content):
        for key in match.split(","):
            key = key.strip()
            assert key in entries, f"Manuscript cites unknown key: '{key}'"
            assert "verified_by" in entries[key], f"Cited key '{key}' has not been human verified."
