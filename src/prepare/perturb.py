"""NepFaith-120: 7-Type Perturbation Engine for Controlled Counterfactual Synthesis

Implements the negative taxonomy defined in docs/RUBRIC_V1.md Section 5:
1. entity_swap: In-domain entity substitution (Target: Contradicted)
2. number_alteration: Numerical, percentage, date, or BS/AD shifts (Target: Contradicted)
3. negation_flip: Polarity reversal of core factual clauses (Target: Contradicted)
4. misattribution: Re-attribution of findings/statements to wrong institution (Target: Contradicted)
5. register_shift: Distorted honorific or grammatical status (Target: Contradicted / Not-in-context)
6. unsupported_addition: Injection of plausible ungrounded external claims (Target: Not-in-context)
7. invented_causality: Spurious causal linking of independent true propositions (Target: Contradicted / Not-in-context)
"""

import re
import json
import random
import logging
from typing import Tuple, Optional, Dict, Any, List

from src.prepare.schema import PerturbationType, ClaimLabel

logger = logging.getLogger("PerturbationEngine")

# Curated in-domain distractor pools for Nepali context entities
ENTITY_DISTRACTORS = {
    # Locations & Parks
    "Chitwan National Park": "Bardiya National Park",
    "Lumbini": "Janakpur",
    "Kathmandu": "Pokhara",
    "Pokhara": "Biratnagar",
    "Rupandehi": "Dhanusha",
    "Babar Mahal": "Singha Durbar",
    "Kirtipur": "Pokhara Stadium",
    # Institutions
    "Nepal Rastra Bank": "Ministry of Finance",
    "Ministry of Finance": "National Planning Commission",
    "Cricket Association of Nepal (CAN)": "All Nepal Football Association (ANFA)",
    "Tribhuvan University": "Kathmandu University",
    "Nepali Army": "Nepal Police",
    # People
    "Pushpa Kamal Dahal": "KP Sharma Oli",
    "Sher Bahadur Deuba": "Madhav Kumar Nepal",
    "Rohit Paudel": "Dipendra Singh Airee",
    "Paras Khadka": "Gyanendra Malla",
    "Tenzing Norgay Sherpa": "Babu Chiri Sherpa",
    "Edmund Hillary": "George Mallory",
}

MISATTRIBUTIONS = [
    ("Nepal Rastra Bank", "the World Bank"),
    ("Central Bureau of Statistics", "Transparency International"),
    ("National Planning Commission", "Asian Development Bank"),
    ("Ministry of Finance", "International Monetary Fund"),
    ("Cricket Association of Nepal", "International Cricket Council"),
]

UNSUPPORTED_CLAIMS = [
    "The initiative was financed through a low-interest loan from the Asian Development Bank.",
    "A bilateral memorandum of understanding was signed between Nepal and India regarding this matter.",
    "The official delegation was led by senior representatives from the European Union.",
    "Preliminary feasibility studies were conducted by Japanese engineering consultants.",
]


def perturb_entity_swap(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Swaps a recognized named entity with an in-domain distractor."""
    rng = random.Random(seed)
    candidates = [k for k in ENTITY_DISTRACTORS if k in answer_en]
    if not candidates:
        # Fallback to common generic entities
        if "Nepal" in answer_en:
            return answer_en.replace("Nepal", "Bhutan", 1), "Bhutan"
        return answer_en, ""
    
    target = rng.choice(candidates)
    replacement = ENTITY_DISTRACTORS[target]
    perturbed = answer_en.replace(target, replacement, 1)
    return perturbed, f"{target} -> {replacement}"


def perturb_number_alteration(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Alters numerical counts, years, or percentages."""
    rng = random.Random(seed)
    # Match numbers (including decimals, commas, percentages, years)
    matches = list(re.finditer(r"\b\d{1,4}(?:\.\d+)?%?\b", answer_en))
    if not matches:
        return answer_en, ""
    
    chosen = rng.choice(matches)
    raw_val = chosen.group(0)
    has_pct = raw_val.endswith("%")
    clean_val = raw_val.rstrip("%")

    try:
        if "." in clean_val:
            float_val = float(clean_val)
            altered = f"{float_val + rng.choice([2.5, -3.1, 5.0]):.1f}"
        else:
            int_val = int(clean_val)
            # If it's a 4-digit year like 2023 or 1953
            if 1900 <= int_val <= 2030:
                altered = str(int_val + rng.choice([5, -4, 10]))
            else:
                altered = str(max(1, int_val + rng.choice([15, -12, 50, 100])))
        
        if has_pct:
            altered += "%"
            
        start, end = chosen.span()
        perturbed = answer_en[:start] + altered + answer_en[end:]
        return perturbed, f"{raw_val} -> {altered}"
    except ValueError:
        return answer_en, ""


def perturb_negation_flip(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Toggles grammatical polarity in an affirmative or negative clause."""
    pairs = [
        (r"\bwas not\b", "was"),
        (r"\bwere not\b", "were"),
        (r"\bdid not\b", "did"),
        (r"\bdoes not\b", "does"),
        (r"\bwas\b", "was not"),
        (r"\bwere\b", "were not"),
        (r"\bhas been\b", "has not been"),
        (r"\bis\b", "is not"),
        (r"\bare\b", "are not"),
        (r"\bincreased\b", "decreased"),
        (r"\bgrew\b", "declined"),
        (r"\bsuccessfully\b", "unsuccessfully"),
    ]
    for pattern, repl in pairs:
        if re.search(pattern, answer_en, flags=re.IGNORECASE):
            perturbed, count = re.subn(pattern, repl, answer_en, count=1, flags=re.IGNORECASE)
            if count > 0:
                return perturbed, f"negation: {repl}"
    
    # Generic prefix flip if no match
    return f"It is false that {answer_en[0].lower() + answer_en[1:]}", "polarity inverted"


def perturb_misattribution(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Attributes statements, statistics, or directives to the wrong official entity."""
    for orig, wrong in MISATTRIBUTIONS:
        if orig.lower() in answer_en.lower():
            pattern = re.compile(re.escape(orig), re.IGNORECASE)
            perturbed = pattern.sub(wrong, answer_en, count=1)
            return perturbed, f"misattributed: {orig} -> {wrong}"
    
    # Generic misattribution prefix
    return f"According to the Asian Development Bank, {answer_en[0].lower() + answer_en[1:]}", "misattributed to ADB"


def perturb_register_shift(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Distorts formal authority or grammatical agreement via honorific / register shift."""
    replacements = [
        (r"\bThe Prime Minister\b", "The Prime Ministers"),
        (r"\bPresident\b", "Presidents"),
        (r"\bHis Majesty's Government\b", "Local Municipal Clerks"),
        (r"\bCommander-in-Chief\b", "Subordinate Corporals"),
    ]
    for pattern, repl in replacements:
        if re.search(pattern, answer_en):
            perturbed = re.sub(pattern, repl, answer_en, count=1)
            return perturbed, f"register shift: {repl}"
    
    # Fallback register distortion: pluralizing head entity
    tokens = answer_en.split()
    if len(tokens) > 2:
        perturbed = f"The respective authorities and multiple delegates {tokens[1]} " + " ".join(tokens[2:])
        return perturbed, "register shift: plural authority distortion"
    return answer_en, ""


def perturb_unsupported_addition(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Injects a plausible, ungrounded external proposition absent from context."""
    rng = random.Random(seed)
    addition = rng.choice(UNSUPPORTED_CLAIMS)
    clean_ans = answer_en.strip()
    if not clean_ans.endswith("."):
        clean_ans += "."
    perturbed = f"{clean_ans} Furthermore, {addition[0].lower() + addition[1:]}"
    return perturbed, f"unsupported addition: {addition}"


def perturb_invented_causality(answer_en: str, seed: int = 42) -> Tuple[str, str]:
    """Links two independent sentences or clauses with a spurious causal connective."""
    sentences = re.split(r"(?<=[.!?])\s+", answer_en.strip())
    if len(sentences) >= 2:
        first = sentences[0].rstrip(".!?")
        second = sentences[1][0].lower() + sentences[1][1:].rstrip(".!?")
        connective = random.Random(seed).choice([
            "as a direct consequence of which",
            "which consequently triggered",
            "primarily because",
        ])
        combined = f"{first}, {connective} {second}."
        remaining = " ".join(sentences[2:])
        perturbed = f"{combined} {remaining}".strip()
        return perturbed, f"spurious causality: '{connective}'"
    
    # Fallback: inject causal tail
    clean = answer_en.strip().rstrip(".!?")
    perturbed = f"{clean}, directly leading to an unprecedented national crisis."
    return perturbed, "spurious causality: 'directly leading to...'"


def apply_perturbation(
    answer_en: str,
    perturbation_type: PerturbationType,
    seed: int = 42,
) -> Tuple[str, str]:
    """Deterministic dispatcher for the 7 perturbation types."""
    dispatch = {
        PerturbationType.ENTITY_SWAP: perturb_entity_swap,
        PerturbationType.NUMBER_DATE_ALTERATION: perturb_number_alteration,
        PerturbationType.NEGATION_FLIP: perturb_negation_flip,
        PerturbationType.MISATTRIBUTION: perturb_misattribution,
        PerturbationType.REGISTER_SHIFT: perturb_register_shift,
        PerturbationType.UNSUPPORTED_ADDITION: perturb_unsupported_addition,
        PerturbationType.INVENTED_CAUSALITY: perturb_invented_causality,
    }
    operator = dispatch.get(perturbation_type)
    if not operator:
        raise ValueError(f"Unknown perturbation type: {perturbation_type}")
    
    return operator(answer_en, seed=seed)
