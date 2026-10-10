# Freeze Schema v1

Type: task
Status: open
Blocked by: 01, 05, 07
Cap: 1 day (schema specification & consumer audit)

## Question

Specify and freeze Schema v1 for all corpus items, perturbations, and annotation records.

Rules:
- Every field must be explicitly justified by an analysis in Sprint 1 or Sprint 3 that consumes it. Fields that no planned analysis consumes must be dropped.
- Required fields:
  - `item_id`: Unique identifier
  - `domain`: `wikipedia` | `government_report` | `news`
  - `source_provenance`: `natural` | `perturbed`
  - `perturbation_type`: (if perturbed) one of the 7 typed edits, else `null`
  - `perturbation_span`: target text span
  - `passage_ne`: Nepali reference context
  - `query_ne`: Nepali query
  - `query_en`: English query
  - `answer_en`: Generated English response
  - `retrieval_condition`: `full_support` | `partial_support` | `distractor_present`
  - `sampling_weight`: Assigned stratum weight
  - `claims`: Array of segmented claims with spans and criticality (`critical` | `non_critical`)
  - `gold_claim_labels`: Array of human consensus labels (`Supported` | `Contradicted` | `Not-in-context`)
  - `derived_item_label`: Derived overall faithfulness with critical override
