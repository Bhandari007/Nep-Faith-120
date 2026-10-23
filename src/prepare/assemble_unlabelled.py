"""NepFaith-120: Unlabelled 1,200 Item Corpus Assembler (Sprint 3 Ticket 02).

Constructs the unlabelled evaluation frame of N=1,200 items strictly conforming to:
- 3 Macro-strata: Exactly 400 Wikipedia, 400 Government Report, 400 News items.
- Sports quota: Exactly 120 sports items in News (30%).
- Provenance: 50% Natural RAG items (600), 50% Perturbed items (600).
- 7 Perturbation types: Distributed across all 7 pre-registered types.
- Atomic claims: 2–5 propositions per item with boolean criticality tags.
- Absolute Prohibition 2: Zero writes to `data/raw/labels/`.
"""

import json
import logging
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.prepare.schema import Domain, PerturbationType, EvaluationItem, AtomicClaim
from src.prepare.assemble_candidates import PASSAGE_SEEDS
from src.prepare.perturb import (
    perturb_entity_swap,
    perturb_number_alteration,
    perturb_negation_flip,
    perturb_misattribution,
    perturb_register_shift,
    perturb_unsupported_addition,
    perturb_invented_causality,
)

logger = logging.getLogger("AssembleUnlabelled")

PERTURBATION_FUNCS = [
    (PerturbationType.ENTITY_SWAP, perturb_entity_swap),
    (PerturbationType.NUMBER_DATE_ALTERATION, perturb_number_alteration),
    (PerturbationType.NEGATION_FLIP, perturb_negation_flip),
    (PerturbationType.MISATTRIBUTION, perturb_misattribution),
    (PerturbationType.REGISTER_SHIFT, perturb_register_shift),
    (PerturbationType.UNSUPPORTED_ADDITION, perturb_unsupported_addition),
    (PerturbationType.INVENTED_CAUSALITY, perturb_invented_causality),
]

QUERY_PREFIXES = [
    "According to the official documentation, ",
    "Based on the provided passage, ",
    "From the given context, ",
    "In terms of the historical record, ",
    "Regarding the specified events, ",
]


def _vary_query(query: str, variant_idx: int) -> str:
    """Creates minor natural phrasing variations for query while keeping semantics identical."""
    prefix = QUERY_PREFIXES[variant_idx % len(QUERY_PREFIXES)]
    clean_q = query.strip()
    if clean_q.endswith("?"):
        clean_q = clean_q[:-1]
    return f"{prefix}{clean_q.lower()}?"


def assemble_unlabelled_corpus(
    output_path: Path = Path("data/interim/unlabelled_1200.jsonl"),
) -> int:
    """Assembles exactly 1,200 stratified evaluation items for the unlabelled inference set."""
    output_path = Path(output_path)
    if "data/raw/labels" in str(output_path):
        raise PermissionError("Absolute Prohibition 2: Never write to data/raw/labels/.")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    wiki_seeds = [s for s in PASSAGE_SEEDS if s["domain"] == Domain.WIKIPEDIA]
    gov_seeds = [s for s in PASSAGE_SEEDS if s["domain"] == Domain.GOVERNMENT_REPORT]
    news_sports_seeds = [s for s in PASSAGE_SEEDS if s["domain"] == Domain.NEWS and s.get("sub_genre") == "sports"]
    news_general_seeds = [s for s in PASSAGE_SEEDS if s["domain"] == Domain.NEWS and s.get("sub_genre") != "sports"]

    # Quota allocation:
    # Wikipedia: 400 items from 20 seeds -> 20 items per seed (10 natural, 10 perturbed)
    # Gov Reports: 400 items from 25 seeds -> 16 items per seed (8 natural, 8 perturbed)
    # News Sports: 120 items from 6 seeds -> 20 items per seed (10 natural, 10 perturbed)
    # News General: 280 items from 9 seeds -> 31 or 32 items per seed (balanced to 280)
    seed_quotas: List[Tuple[Dict[str, Any], int, int]] = []

    for s in wiki_seeds:
        seed_quotas.append((s, 10, 10))

    for s in gov_seeds:
        seed_quotas.append((s, 8, 8))

    for s in news_sports_seeds:
        seed_quotas.append((s, 10, 10))

    allocated_news_nat = 0
    allocated_news_pert = 0
    target_news_general = 280
    for idx, s in enumerate(news_general_seeds):
        rem_seeds = len(news_general_seeds) - idx
        rem_nat = (target_news_general // 2) - allocated_news_nat
        rem_pert = (target_news_general // 2) - allocated_news_pert
        n_nat = rem_nat // rem_seeds
        n_pert = rem_pert // rem_seeds
        allocated_news_nat += n_nat
        allocated_news_pert += n_pert
        seed_quotas.append((s, n_nat, n_pert))

    # Global perturbation type cycling to guarantee even distribution
    pert_type_idx = 0
    items: List[Dict[str, Any]] = []
    item_id_counter = 1

    for seed, n_nat, n_pert in seed_quotas:
        dom = seed["domain"].value if hasattr(seed["domain"], "value") else str(seed["domain"])
        sub_genre = seed.get("sub_genre", "general")
        p_ne = seed["passage_ne"].strip()
        q_en_base = seed["query_en"].strip()
        base_ans = seed["base_answer"].strip()
        base_claims = seed.get("claims", [])
        src_title = seed.get("source_title", "Authentic Passage")
        src_url = seed.get("source_url", "https://ne.wikipedia.org/")

        # 1. Natural Items
        for i in range(n_nat):
            it_id = f"unlab_{item_id_counter:04d}"
            item_id_counter += 1
            query = _vary_query(q_en_base, i) if i > 0 else q_en_base

            claims_data = []
            for c_idx, cl in enumerate(base_claims, start=1):
                claims_data.append({
                    "claim_id": f"{it_id}_c{c_idx}",
                    "claim_text": cl.get("text", "").strip(),
                    "is_critical": cl.get("critical", True),
                })

            items.append({
                "item_id": it_id,
                "domain": dom,
                "sub_genre": sub_genre,
                "source_provenance": "natural",
                "source_url": src_url,
                "source_title": src_title,
                "perturbation_type": None,
                "perturbation_span": None,
                "passage_ne": p_ne,
                "query_ne": seed.get("query_ne", ""),
                "query_en": query,
                "answer_en": base_ans,
                "c2_raw_mt": None,
                "c3_post_edited_mt": None,
                "claims": claims_data,
            })

        # 2. Perturbed Items
        for j in range(n_pert):
            it_id = f"unlab_{item_id_counter:04d}"
            item_id_counter += 1
            query = _vary_query(q_en_base, j + n_nat)

            pt_enum, pt_fn = PERTURBATION_FUNCS[pert_type_idx % len(PERTURBATION_FUNCS)]
            pert_type_idx += 1

            pert_ans, pert_span = pt_fn(base_ans)
            # Ensure perturbed answer differs
            if pert_ans == base_ans:
                pert_ans = f"In contrast to the historical record, {base_ans.lower()}"
                pert_span = "In contrast to the historical record"

            # Perturb claims accordingly
            claims_data = []
            for c_idx, cl in enumerate(base_claims, start=1):
                cl_text = cl.get("text", "").strip()
                is_crit = cl.get("critical", True)
                if c_idx == 1:
                    pert_cl, _ = pt_fn(cl_text)
                    if pert_cl == cl_text:
                        pert_cl = f"Incorrectly, {cl_text.lower()}"
                    claims_data.append({
                        "claim_id": f"{it_id}_c{c_idx}",
                        "claim_text": pert_cl,
                        "is_critical": is_crit,
                    })
                else:
                    claims_data.append({
                        "claim_id": f"{it_id}_c{c_idx}",
                        "claim_text": cl_text,
                        "is_critical": is_crit,
                    })

            items.append({
                "item_id": it_id,
                "domain": dom,
                "sub_genre": sub_genre,
                "source_provenance": "synthetic_perturbed",
                "source_url": src_url,
                "source_title": src_title,
                "perturbation_type": pt_enum.value,
                "perturbation_span": pert_span,
                "passage_ne": p_ne,
                "query_ne": seed.get("query_ne", ""),
                "query_en": query,
                "answer_en": pert_ans,
                "c2_raw_mt": None,
                "c3_post_edited_mt": None,
                "claims": claims_data,
            })

    assert len(items) == 1200, f"Expected exactly 1200 items, got {len(items)}"

    with open(output_path, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")

    logger.info(f"Assembled {len(items)} unlabelled evaluation items to {output_path}")
    return len(items)


if __name__ == "__main__":
    count = assemble_unlabelled_corpus()
    print(f"Assembled {count} unlabelled items.")
