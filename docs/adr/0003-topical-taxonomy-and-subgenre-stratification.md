# ADR 0003: 10-Domain Topical Taxonomy & Sub-Genre Stratification

- **Status:** Accepted
- **Date:** 2026-10-16
- **Deciders:** Muskan Bhandari (Lead Researcher), Antigravity AI
- **Related Issues:** [Sprint 2 Issue 01](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/.scratch/sprint-2/issues/01-stratified-sampling-120.md)

---

## Context & Problem Statement

`docs/PREREGISTRATION.md` defines three macro-strata: `wikipedia`, `government_report`, and `news` (with a 30% sports quota). However, to prevent evaluation bias towards general encyclopedic or single-topic data, the 120-item gold benchmark requires a granular, domain-specific topical taxonomy reflecting real-world Nepali information retrieval and RAG applications (e.g. healthcare, agriculture, administrative reports, public education).

## Decision

The 120 candidate items are explicitly stratified across 10 distinct topical sub-genres mapped cleanly into the 3 macro-strata:

| Domain | Sub-Genre (`sub_genre`) | Target Items | Key Linguistic & Numerical Evaluator Stress-Tests |
|---|---|---|---|
| **`government_report`** | `health` | 10 | Clinical dosages, epidemic case figures, hedging / evidentiality preservation. |
| **`government_report`** | `agriculture` | 10 | Indigenous crop names (धान, मकै, कोदो), metric vs local units (रोपनी, बिघा, मुरी). |
| **`government_report`** | `education` | 10 | Passing percentages, institutional designations, demographic literacy rates. |
| **`government_report`** | `economy_finance` | 10 | Lakh/Crore/Arba (लाख, करोड, अर्ब) scale stress-test, remittance indicators. |
| **`news` / `government`** | `disaster_geography` | 10 | Seismic data (Richter scale, epicenters), monsoon flood / landslide casualties. |
| **`government_report`** | `governance_law` | 10 | Constitution 2072 articles, federal vs provincial powers, nested legal negation. |
| **`news`** | `sports` | 12 | Pre-registered 30% news quota (CAN cricket, ANFA football, player entity swaps). |
| **`wikipedia`** | `culture_heritage` | 15 | UNESCO monument entities, BS vs AD calendar years (वि.सं.), festival rituals. |
| **`wikipedia`** | `biodiversity_parks` | 15 | National parks (Chitwan, Sagarmatha), endangered species counts, elevations. |
| **`news` / `wikipedia`** | `infrastructure_tourism` | 18 | Hydropower MW capacities, Fast Track tunnels, tourist arrival metrics. |
| **Total** | | **120** | **Balanced across 50% Natural / 50% 7-Type Perturbed** |

## Consequences

- **Positive:** Evaluators are tested on high-stakes civic, economic, and medical language where hallucination has severe consequences. Guarantees that the benchmark cannot be solved by memorization of general Wikipedia facts.
- **Traceability:** Every passage in `data/interim/preannotations/gold_candidates_120.jsonl` carries its explicit `sub_genre` and source document attribution.
