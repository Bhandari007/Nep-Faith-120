# Agent Instructions

## Agent skills

### Issue tracker

Issues and specs are tracked locally as markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Canonical triage roles mapped to standard role names (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout (`GLOSSARY.md` + `docs/adr/` at the repo root). See `docs/agents/domain.md`.

## Human-Agent Boundaries

- **Human leads literature reading and research**: The agent must NOT conduct autonomous paper reading or replace human literature study. Instead, the agent assigns prioritized reading tasks, pinpoints specific papers/sections, and frames targeted questions for the human researcher to study.
- **Agent leads organization, coding, and infrastructure**: The agent manages the issue tracker, writes pipeline and statistical code, maintains schemas and environments, scaffolds tests, and assists the researcher.

## Researcher Learning & Docket Protocol

- **Location**: Reading dockets are maintained under `researcher/` as date-based files (e.g. `researcher/YYYY-MM-DD-reading-docket.md`).
- **Session Startup Rule**: At the start of every session or turn, the agent MUST inspect the latest reading docket in `researcher/`.
- **Hard Gate / Stop Condition**: If any answer is missing or incomplete in an active reading docket, the agent MUST IMMEDIATELY STOP from proceeding further. The agent must NOT write downstream pipeline code or advance tickets until the gap is addressed. The agent must pause and actively guide the researcher through the missing concept.
- **Phase Clearance / Exemption**: When a milestone's reading is verified, or when the project transitions into an engineering-only phase (e.g. Sprint 1 pipeline construction or Sprint 2 annotation), the docket status is set to `Status: Cleared — No Active Reading Required for Current Phase`. When cleared, the agent proceeds directly with coding and organization without triggering the stop gate.

## Paper Dossier & Continuous Writing Protocol

- **Location**: Paper sections and evidence notes are maintained under `paper/dossier/`.
- **Continuous Harvesting**: The agent must continuously extract the researcher's answers from `researcher/`, architectural decisions from `.scratch/`, and empirical findings into structured paper sections:
  - `paper/dossier/01-introduction.md`
  - `paper/dossier/02-related-work.md`
  - `paper/dossier/03-methodology.md`
  - `paper/dossier/04-statistical-framework.md`
  - `paper/dossier/05-limitations-and-findings.md`
- **Objective**: Prevent end-of-project writing bottlenecks. By Sprint 3, the core prose, citations, and formulas must already be drafted in the researcher's voice, ready to assemble into the final submission.
