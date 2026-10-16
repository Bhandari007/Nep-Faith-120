# Agent Instructions

## Agent skills

### Issue tracker

Issues and specs are tracked locally as markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Canonical triage roles mapped to standard role names (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout (`GLOSSARY.md` + `docs/adr/` at the repo root). See `docs/agents/domain.md`.

## Core Operational Documents

All work in this repository is strictly governed by:
- [`docs/WORKFLOW.md`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/docs/WORKFLOW.md) — The five pillars of the research workflow, session startup rules, and boundaries.
- [`docs/CODING_STANDARDS.md`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/docs/CODING_STANDARDS.md) — Research code standards (the 5 properties, research testing taxonomy, repo shape, LLM rules, paper gate).

## Session Startup Sequence (Mandatory)

1. **Freeze check:** If the Sprint 1 freeze tag exists, diff `src/analyze/` and `src/report/` against the tag before anything else. Any change is a **HARD STOP**.
2. **Code standards:** Read `docs/CODING_STANDARDS.md` to uphold engineering discipline.
3. **Docket inspection:** Open the latest docket in `researcher/` (earliest unanswered docket gates).
   - If any question is blank or incomplete: **HARD STOP**. The agent does not write pipeline code and does not advance tickets. Name the source and section, and wait.
   - **The researcher writes the answer first.** The agent responds only after written answers exist (challenging/correcting).
   - **Clearance:** Only the researcher signs `Status: Cleared` with initials and date. The agent may only set `Status: Clearance proposed — awaiting researcher` and stop.
   - **No broad exemptions:** Sprints 1 and 2 are NOT exempt from reading dockets.

## Engineering Discipline: Mandatory Test-Driven Development (TDD)

- **Test First, Always:** Before writing any actual implementation code in `src/`, the agent MUST write tests first in `tests/` specifying expected behaviors, invariants, and edge cases.
- **Red-Green-Refactor:** Implementation code is written strictly to satisfy previously committed or written failing test specifications. No implementation PR or commit without preceding or co-designed tests.

## The Four Absolute Prohibitions

1. **The Freeze:** After the Sprint 1 freeze tag, never modify estimators, metrics, arms, or report generator. Diff at startup.
2. **Gold Labels:** Never write to gold label fields. Pre-annotations go to `data/interim/preannotations/`; gold labels live in `data/raw/labels/` (agent has no write access).
3. **No Peeking:** Before gold labels exist, never compute or report inter-scorer agreement, score distributions, or anything result-shaped.
4. **No Resampling:** Never draw, filter, reorder, or re-weight items outside the recorded sampling procedure.

## Task Tracking & Caps

- Maps and tickets live under `.scratch/<effort>/`.
- Every ticket carries an explicit cap (time or concrete output). Exceeding a cap is an immediate **HARD STOP** to report to the researcher.
- Maps maintain strict separation: `## Findings (agent)` and `## Verdicts (researcher)`.
- Tickets require both `Evidence:` (agent) and `Verdict:` (researcher with initials and date) to close.
- **Mandatory Issue Presentation Before Execution:** Before executing tasks in any sprint, the agent MUST always show the researcher the sprint issues/tickets (with their identifiers, titles, caps, and current status), highlight the next frontier ticket being tackled, and then proceed to execute. Never execute silently without showing the sprint issue list.


## Paper Drafting Split & Citation Verification

- **Agent-draftable from frozen specs:** `paper/dossier/03-methodology.md` and `paper/dossier/04-statistical-framework.md`.
- **Researcher-authored:** `paper/dossier/01-introduction.md`, `paper/dossier/02-related-work.md`, and `paper/dossier/05-limitations.md`.
- **Raw notes:** Agent files raw materials into `paper/notes/`. Nothing crosses into `paper/dossier/` without researcher rewriting.
- **Citation verification:** Every BibTeX entry must include `verified_by = {Initials, YYYY-MM-DD}` confirming human check of primary source.
