# Draft Rubric v1 and Run Timed 8-Item Annotation Pilot

Type: task
Status: open
Priority: critical path (parallel track)
Cap: 1 day (timed pilot & rubric v1)

## Question

Draft Rubric v1 and execute the 8-item timed pilot with both annotators to establish concrete scheduling parameters and refine claim segmentation before scaling.

Requirements:
1. **Rubric v1**:
   - Define claim segmentation rules (atomic factual claims, mirrored to RAGAS).
   - Define labels: `Supported`, `Contradicted`, `Not-in-context` (ensure `Contradicted` $\ne$ `Not-in-context`).
   - Define the 7 perturbation error types (entity swap, number/date alteration, negation flip, attribution removal/misattribution, honorific/register shift, unsupported addition, invented causal relation).
   - Define critical claim override rules.
2. **Timed Pilot**:
   - Both annotators independently annotate 8 representative items (Nepali context, English answers across natural/perturbed, segmented claims).
   - Measure and record exact minutes per item and minutes per claim.
   - Calculate preliminary agreement and surface any ambiguous rubric edge cases.
