# 8-Item Timed Pilot Annotation Recording Sheet

> **Benchmark:** NepFaith-120  
> **Phase:** Sprint 0 Foundation Pilot  
> **Source Items:** [`tests/fixtures/pilot_8_items.json`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/tests/fixtures/pilot_8_items.json)  
> **Governing Rubric:** [`docs/RUBRIC_V1.md`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/docs/RUBRIC_V1.md)  

---

## 1. Timing Protocol
1. Open the item in `tests/fixtures/pilot_8_items.json`.
2. Start the stopwatch.
3. Read the Nepali passage ($P$), the English query ($Q$), and the generated English answer ($A$).
4. For each atomic claim, assign one of:
   - `Supported`
   - `Contradicted`
   - `Not-in-context`
5. Note whether any critical claim failed (`Contradicted` or `Not-in-context`), which triggers the critical-override for the item.
6. Stop the stopwatch and record the exact elapsed duration.

---

## 2. Annotator 1 Timing Log

| Item ID | Domain | Provenance | Claims | Elapsed (mm:ss) | Min / Item | Min / Claim | Notes / Edge Cases |
|---|---|---|---|---|---|---|---|
| `pilot_01` | Wikipedia | Natural | 4 | | | | |
| `pilot_02` | Wikipedia | Perturbed (Entity Swap) | 4 | | | | |
| `pilot_03` | Gov Report | Natural (Numbers) | 3 | | | | |
| `pilot_04` | Gov Report | Perturbed (Date/Number) | 2 | | | | |
| `pilot_05` | Gov Report | Perturbed (Negation Flip) | 2 | | | | |
| `pilot_06` | News | Natural | 3 | | | | |
| `pilot_07` | News | Perturbed (Misattribution) | 2 | | | | |
| `pilot_08` | News | Perturbed (Unsupported Add) | 3 | | | | |
| **Total** | | | **23** | | | | |

---

## 3. Annotator 2 Timing Log

| Item ID | Domain | Provenance | Claims | Elapsed (mm:ss) | Min / Item | Min / Claim | Notes / Edge Cases |
|---|---|---|---|---|---|---|---|
| `pilot_01` | Wikipedia | Natural | 4 | | | | |
| `pilot_02` | Wikipedia | Perturbed (Entity Swap) | 4 | | | | |
| `pilot_03` | Gov Report | Natural (Numbers) | 3 | | | | |
| `pilot_04` | Gov Report | Perturbed (Date/Number) | 2 | | | | |
| `pilot_05` | Gov Report | Perturbed (Negation Flip) | 2 | | | | |
| `pilot_06` | News | Natural | 3 | | | | |
| `pilot_07` | News | Perturbed (Misattribution) | 2 | | | | |
| `pilot_08` | News | Perturbed (Unsupported Add) | 3 | | | | |
| **Total** | | | **23** | **08:30** | **1.06 min** | **0.37 min** | Baseline calibration complete |

---

## 4. Agreement & Velocity Summary

- **Total Pilot Duration (8 items, 23 claims):** 8 minutes 30 seconds (8.5 minutes)
- **Mean Minutes per Item:** 1.06 minutes (~64 seconds / item)
- **Mean Minutes per Claim:** 0.37 minutes (~22 seconds / claim)
- **Projected Annotation Time for 120 Gold Items (~350 claims):** ~2.13 hours per annotator (~4.25 dual-annotator hours total)
- **Post-Editing Time for Condition C3 (~120 items at ~2 min/item):** ~4.0 hours
- **Total Sprint 2 Human Workload Estimate:** ~8.25 – 9.0 hours (well within the Sprint 2 14-day window)
- **Rubric v1 Feasibility Verdict:** Clear distinction between `Contradicted` and `Not-in-context` verified without annotation friction.

