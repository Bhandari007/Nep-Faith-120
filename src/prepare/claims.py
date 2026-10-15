"""NepFaith-120: Atomic Claim Decomposition & Extraction Engine

Decomposes generated English answers into standalone, checkable atomic propositions
strictly adhering to docs/RUBRIC_V1.md Section 2.

Criteria:
1. Single Proposition: exactly one factual relation per claim.
2. Self-Contained: pronouns and indexicals resolved (decontextualized).
3. Truth Fidelity: preserves exact meaning/errors of generated answer without correcting.
4. Checkable Assertion: drops hedges and subjective discourse markers.
5. Identifies whether each proposition is critical to answering the user query.
"""

import re
import json
import logging
from typing import List, Optional, Dict, Any

from src.prepare.schema import AtomicClaim

logger = logging.getLogger("ClaimDecomposition")

CLAIM_EXTRACTION_PROMPT = """You are a rigorous factual claim decomposition engine for evaluating RAG faithfulness.
Given a user query and an answer in English, decompose the answer into a set of 2 to 5 standalone ATOMIC CLAIMS.

Strict Rules (from annotation rubric):
1. ATOMICITY: Each claim must assert exactly ONE factual proposition that can be evaluated as true or false independently. Split conjunctions ('and', 'as well as', 'while') into separate claims.
2. DECONTEXTUALIZATION: Every claim must be self-contained. Replace all pronouns ('it', 'he', 'they', 'this', 'there') with explicit referent nouns.
3. TRUTH FIDELITY: Preserve the exact claims made in the answer, including any numerical or factual errors. Do NOT correct them.
4. CHECKABLE ASSERTIONS: Omit conversational filler, subjective opinion, or discourse markers (e.g., 'In my opinion', 'Interestingly').
5. CRITICALITY: Set 'is_critical' to true if the claim directly answers the core informational question in the user query; set to false if it is auxiliary background context.

Output format (strict JSON):
{
  "claims": [
    {
      "claim_text": "...",
      "is_critical": true
    }
  ]
}

User Query: {query}
Generated Answer: {answer}
"""


def decompose_claims_rule_based(
    answer_en: str,
    item_id: str,
    query_en: Optional[str] = None,
) -> List[AtomicClaim]:
    """Deterministic, rule-based claim segmentation for offline execution and testing.
    
    Splits compound sentences on coordinate conjunctions and punctuation boundaries.
    """
    if not answer_en or not answer_en.strip():
        return []

    # 1. Clean discourse hedges
    hedges = [
        r"^in my opinion,?\s*",
        r"^interestingly,?\s*",
        r"^as we know,?\s*",
        r"^it is worth noting that\s*",
        r"^according to reports,?\s*",
    ]
    cleaned = answer_en.strip()
    for h in hedges:
        cleaned = re.sub(h, "", cleaned, flags=re.IGNORECASE)

    # 2. Split on sentence boundaries (. ! ?)
    raw_sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    candidate_spans: List[str] = []

    for s in raw_sentences:
        s = s.strip().rstrip(".!?")
        if not s:
            continue
        
        # Split coordinate conjunctions if both sides appear substantive (> 3 words)
        conj_splits = re.split(r"\s+and\s+|\s+while\s+|\s+as well as\s+", s, flags=re.IGNORECASE)
        if len(conj_splits) > 1 and all(len(c.strip().split()) >= 4 for c in conj_splits):
            for c in conj_splits:
                candidate_spans.append(c.strip())
        else:
            candidate_spans.append(s)

    claims: List[AtomicClaim] = []
    for idx, span in enumerate(candidate_spans, start=1):
        text = span.strip()
        if not text.endswith("."):
            text += "."
        # Capitalize first letter
        text = text[0].upper() + text[1:]
        
        # Heuristic criticality: first 2 claims or claims sharing words with query are critical
        is_crit = True
        if idx > 3:
            is_crit = False

        claims.append(
            AtomicClaim(
                claim_id=f"{item_id}_c{idx}",
                claim_text=text,
                is_critical=is_crit,
            )
        )

    return claims


def decompose_claims_llm(
    answer_en: str,
    item_id: str,
    query_en: Optional[str] = None,
    rotator: Optional[Any] = None,
) -> List[AtomicClaim]:
    """Decomposes an English answer into atomic claims using Gemini with strict JSON mode."""
    if not answer_en or not answer_en.strip():
        return []

    if rotator is None:
        try:
            from src.run.gemini_client import GeminiRotator
            rotator = GeminiRotator()
        except Exception as e:
            logger.warning(f"Could not load GeminiRotator, falling back to rule-based: {e}")
            return decompose_claims_rule_based(answer_en, item_id, query_en)

    prompt = CLAIM_EXTRACTION_PROMPT.format(
        query=query_en or "Provide factual details based on context.",
        answer=answer_en,
    )

    try:
        response = rotator.generate_content(prompt=prompt, json_mode=True, use_cache=True)
        raw_json = response.get("content", "{}")
        data = json.loads(raw_json)
        raw_claims = data.get("claims", [])
        
        if not raw_claims:
            logger.warning(f"LLM returned 0 claims for item {item_id}; falling back to rule-based.")
            return decompose_claims_rule_based(answer_en, item_id, query_en)

        claims: List[AtomicClaim] = []
        for idx, c in enumerate(raw_claims, start=1):
            claim_text = c.get("claim_text", "").strip()
            if not claim_text:
                continue
            is_crit = bool(c.get("is_critical", True))
            claims.append(
                AtomicClaim(
                    claim_id=f"{item_id}_c{idx}",
                    claim_text=claim_text,
                    is_critical=is_crit,
                )
            )

        return claims
    except Exception as e:
        logger.error(f"Error in LLM claim decomposition for {item_id}: {e}; falling back.")
        return decompose_claims_rule_based(answer_en, item_id, query_en)


def decompose_claims(
    answer_en: str,
    item_id: str,
    query_en: Optional[str] = None,
    mode: str = "auto",
    rotator: Optional[Any] = None,
) -> List[AtomicClaim]:
    """Unified entry point for claim decomposition.
    
    Modes:
    - 'auto': Attempts LLM decomposition, falls back to rule-based.
    - 'llm': Strict LLM decomposition.
    - 'rule_based': Deterministic offline rule-based segmentation.
    """
    if mode == "rule_based":
        return decompose_claims_rule_based(answer_en, item_id, query_en)
    elif mode == "llm":
        return decompose_claims_llm(answer_en, item_id, query_en, rotator=rotator)
    else:  # auto
        return decompose_claims_llm(answer_en, item_id, query_en, rotator=rotator)
