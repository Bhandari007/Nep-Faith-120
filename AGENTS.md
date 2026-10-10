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
