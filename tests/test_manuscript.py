"""Tests for Publication LaTeX Manuscript Integrity (paper/manuscript.tex)."""

import re
from pathlib import Path
import pytest


def test_manuscript_file_exists():
    manuscript = Path("paper/manuscript.tex")
    assert manuscript.exists(), "paper/manuscript.tex must exist."


def test_manuscript_inputs_and_tables():
    """Verifies that all \\input{...} statements reference existing files."""
    content = Path("paper/manuscript.tex").read_text(encoding="utf-8")
    inputs = re.findall(r"\\input\{([^}]+)\}", content)
    assert len(inputs) >= 2, "Manuscript must input Table 1 and Table 2."

    for inp in inputs:
        inp_path = Path(inp)
        if not inp_path.suffix:
            inp_path = inp_path.with_suffix(".tex")
        assert inp_path.exists(), f"Input file referenced in manuscript does not exist: {inp_path}"


def test_manuscript_citations_in_bibtex():
    """Verifies that all \\cite{...} keys are defined in paper/references.bib."""
    content = Path("paper/manuscript.tex").read_text(encoding="utf-8")
    bib_content = Path("paper/references.bib").read_text(encoding="utf-8")

    cited_keys = set()
    for match in re.findall(r"\\cite\{([^}]+)\}", content):
        for key in match.split(","):
            cited_keys.add(key.strip())

    bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib_content))

    missing = cited_keys - bib_keys
    assert not missing, f"Citations in manuscript missing from paper/references.bib: {missing}"


def test_manuscript_labels_and_refs():
    """Verifies that all \\ref{...} labels are defined with \\label{...}."""
    content = Path("paper/manuscript.tex").read_text(encoding="utf-8")
    
    # Also include content from input files
    for inp in re.findall(r"\\input\{([^}]+)\}", content):
        inp_path = Path(inp)
        if not inp_path.suffix:
            inp_path = inp_path.with_suffix(".tex")
        if inp_path.exists():
            content += "\n" + inp_path.read_text(encoding="utf-8")

    refs = set(re.findall(r"\\ref\{([^}]+)\}", content))
    labels = set(re.findall(r"\\label\{([^}]+)\}", content))

    missing_labels = refs - labels
    assert not missing_labels, f"Refs missing label definitions: {missing_labels}"


def test_manuscript_balanced_environments():
    """Verifies that LaTeX \\begin and \\end environments form a properly nested stack."""
    content = Path("paper/manuscript.tex").read_text(encoding="utf-8")
    tokens = re.findall(r"\\(begin|end)\{([^}]+)\}", content)
    stack = []
    for tag_type, env in tokens:
        if tag_type == "begin":
            stack.append(env)
        elif tag_type == "end":
            assert stack, f"Unmatched \\end{{{env}}}"
            top = stack.pop()
            assert top == env, f"Mismatched environment: expected \\end{{{top}}}, got \\end{{{env}}}"
    assert not stack, f"Unclosed environments remaining: {stack}"
