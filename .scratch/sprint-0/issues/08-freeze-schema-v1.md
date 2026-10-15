# Freeze Schema v1

Type: task
Status: awaiting-verdict
Cap: 1 day (schema specification & consumer audit)

## Question

Specify and freeze Schema v1 for all corpus items, perturbations, and annotation records.

Rules:
- Every field must be explicitly justified by an analysis in Sprint 1 or Sprint 3 that consumes it. Fields that no planned analysis consumes must be dropped.

## Evidence (agent)

1. **Consumer Justification Audit**:
   Every field in Schema v1 maps directly to an active consumer in the experimental pipeline:

   | Field Name | Downstream Consumer Layer | Analysis / Scientific Justification |
   |---|---|---|
   | `item_id` | `src/analyze/`, `tests/invariants/` | Cluster ID for cluster-robust PPI variance estimation ($\rho_{\text{ICC}} > 0$). |
   | `domain` | `src/prepare/`, `src/analyze/` | Stratum variable $s$ for domain-stratified inverse-probability sampling. |
   | `source_provenance` | `src/report/`, `tests/invariants/` | Guarantees 50/50 balance check; separate reporting of natural vs. perturbed performance. |
   | `perturbation_type` | `src/analyze/`, `src/report/` | Evaluates Hypothesis H2 (claim-type survival across 7 typed errors). |
   | `perturbation_span` | `src/prepare/`, `tests/recovery/` | Planted effect verification in synthetic recovery tests. |
   | `passage_ne` | `src/run/` | Evaluator input for Condition $C1$ (direct cross-lingual) and IndicTrans2 MT input. |
   | `query_en` | `src/prepare/`, `src/run/` | Prompt conditioning for RAG answer generation and claim criticality. |
   | `answer_en` | `src/prepare/` | Input text decomposed into atomic claims $\{k_j\}$. |
   | `c2_raw_mt` | `src/run/` | Evaluator input for Condition $C2$ (raw machine translation). |
   | `c3_post_edited_mt` | `src/run/` | Evaluator input for Condition $C3$ (counterfactual human post-edited ceiling). |
   | `retrieval_condition` | `src/analyze/` | Stratified weighting across support levels (`full`, `partial`, `distractor`). |
   | `sampling_weight` | `src/analyze/` (GLIDE) | Stratum weights ($W_s$) applied to PPI debiasing rectifier $\Delta$. |
   | `claims` | `src/run/`, `src/analyze/` | Atomic scoring unit evaluated by 5 evaluator arms. |
   | `gold_claim_labels` | `src/analyze/` | Ground truth for computing accuracy $A(C)$ and rectifying proxy bias. |
   | `derived_item_label` | `src/report/` | Answer-level binary faithfulness with critical claim override. |

2. **Code & Specification Assets**:
   - Pydantic models with validation rules implemented in [`src/prepare/schema.py`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/src/prepare/schema.py).
   - Machine-readable JSON Schema exported to [`config/schema_v1.json`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/config/schema_v1.json).
   - Validated end-to-end on all 8 pilot items in `tests/fixtures/pilot_8_items.json`.

## Verdict (researcher)

<!-- Researcher writes verdict with initials and date to close this ticket. Example:
- 2026-10-15 · Schema v1 locked and verified against consumer audit. — [Initials]
-->

