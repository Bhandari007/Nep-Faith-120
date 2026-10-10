# NepFaith-120

> **Why cross-lingual faithfulness scoring fails on Nepali → English RAG, and how much of the failure is translation's fault.**  
> *A 35-day research sprint decomposing $\Delta_{MT} = A(C3) - A(C2)$ vs $\Delta_{XL} = A(C3) - A(C1)$ with Prediction-Powered Inference (PPI).*

---

## Repository Map

This repository is strictly organized into **three distinct domains**: Research & Paper, Engineering Pipeline, and Governance.

```
NepFaith-120/
│
├── 📚 RESEARCH & PAPER (Human Learning & Manuscript)
│   ├── researcher/            # Date-based study dockets & researcher answers
│   ├── paper/
│   │   ├── dossier/           # Living manuscript sections (ACL/EMNLP format)
│   │   └── notes/             # Raw literature notes & evidence drafts
│   └── GLOSSARY.md            # Canonical domain vocabulary & math definitions
│
├── 💻 ENGINEERING PIPELINE (Reproducible Codebase)
│   ├── src/
│   │   ├── prepare/           # Ingestion, query generation, 7 perturbation edits
│   │   ├── run/               # 5 evaluator arms, IndicTrans2 execution
│   │   ├── analyze/           # Estimators & GLIDE (FROZEN at Sprint 1 tag)
│   │   └── report/            # Tables & figures generator (FROZEN at Sprint 1 tag)
│   ├── tests/
│   │   ├── recovery/          # Known-truth planted effect simulation tests
│   │   ├── invariants/        # Row count & cross-condition leakage checks
│   │   └── fixtures/          # Frozen miniature regression inputs
│   ├── config/                # Versioned configs hashed into every output
│   ├── data/
│   │   ├── raw/corpus/        # Immutable source Nepali passages
│   │   ├── raw/labels/        # Gold labels (AGENT HAS NO WRITE ACCESS)
│   │   ├── interim/           # Model pre-annotations & intermediate tables
│   │   └── derived/           # Regenerable processed datasets
│   ├── outputs/               # Stamped with commit hash + config hash
│   ├── cache/                 # Deterministic LLM response cache (keyed by prompt hash)
│   └── notebooks/             # Exploration only (never generates paper numbers)
│
└── 🤖 GOVERNANCE & TRACKER (AI Assistant & Workflow Rules)
    ├── AGENTS.md              # Root entrypoint for AI agent boot sequence
    ├── docs/
    │   ├── WORKFLOW.md        # The 5 pillars, startup order & the 4 prohibitions
    │   ├── CODING_STANDARDS.md# Research code principles & 6-question paper gate
    │   ├── CONTRIBUTING.md    # Pointer to standards
    │   └── agents/            # Tracker conventions, triage roles & domain rules
    └── .scratch/              # Local issue tracker & active Wayfinder maps
```

---

## 1. The Research & Paper

This domain captures the scientific thinking, researcher learning, and the evolving paper draft.

- **[`researcher/`](researcher/)**: Date-based reading dockets (e.g. `YYYY-MM-DD-reading-docket.md`). The researcher reads primary literature and types their answers here. The agent is gated on these answers.
- **[`paper/dossier/`](paper/dossier/)**: The living paper draft. Split by author:
  - `01-introduction.md`, `02-related-work.md`, `05-limitations.md` $\to$ **Researcher-authored**.
  - `03-methodology.md`, `04-statistical-framework.md` $\to$ **Agent-draftable** from frozen specs.
- **[`paper/notes/`](paper/notes/)**: Raw evidence, extracted claims, and literature summaries filed by the agent for researcher review.
- **[`GLOSSARY.md`](GLOSSARY.md)**: Mathematical definitions ($\Delta_{MT}$, $\Delta_{XL}$), counterfactual conditions ($C1, C2, C3$), claim labels (`Supported`, `Contradicted`, `Not-in-context`), and the 5 frozen evaluator arms.

---

## 2. The Engineering Pipeline

This domain contains all executable code governed by [`docs/CODING_STANDARDS.md`](docs/CODING_STANDARDS.md).

- **Determinism**: Pinned versions, single seed (`42`), offline analysis.
- **Loud Failure**: No bare `except`, no silent `.dropna()`, row counts logged at every stage boundary.
- **Separation by Freeze Date**: Data preparation vs Run vs Analyze/Report (frozen before labels exist).
- **Physical Label Isolation**: Pre-annotations live in `data/interim/preannotations/`; human gold labels live in `data/raw/labels/` (the AI agent has zero write path to gold labels).
- **Paper Gate**: No number enters the manuscript without passing the 6-question checklist in `docs/CODING_STANDARDS.md`.

---

## 3. Governance & Workflow

This domain manages the collaboration between the researcher and the AI coding assistant, governed by [`docs/WORKFLOW.md`](docs/WORKFLOW.md).

- **[`AGENTS.md`](AGENTS.md)**: Entry point for AI pair programming sessions.
- **Session Startup Sequence**:
  1. **Freeze Check**: Diffs `src/analyze/` and `src/report/` against the freeze tag if it exists. Any difference is an immediate **HARD STOP**.
  2. **Code Standards**: Reads [`docs/CODING_STANDARDS.md`](docs/CODING_STANDARDS.md).
  3. **Docket Inspection**: Checks the latest docket in `researcher/`. If questions are unanswered, the agent **HARD STOPS** and waits for the researcher to write answers first.
- **Issue Tracking ([`.scratch/`](.scratch/))**:
  - Work is tracked via Wayfinder maps (e.g. [`.scratch/sprint-0/map.md`](.scratch/sprint-0/map.md)).
  - Tickets carry caps and are split into `## Findings (agent)` and `## Verdicts (researcher)`.
