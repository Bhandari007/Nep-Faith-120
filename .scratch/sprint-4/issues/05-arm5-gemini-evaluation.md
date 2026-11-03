# Ticket 05 · Arm 5 Frontier LLM Judge (Gemini-3.6-Flash) Evaluation Run

Type: model evaluation / scoring
Status: In Progress — Paused for Daily Quota Reset

## Question

Can we execute Arm 5 (Frontier LLM Judge) using `gemini-3.6-flash` (governed by ADR 0002) with round-robin key rotation and deterministic disk caching across candidate items ($n=120$) and the unlabelled inference corpus ($N=1,200$) under Conditions $C1$ and $C2$, updating Table 1 and Table 2?

## Criteria
1. TDD tests for `Arm5LLMJudge` integration with `gemini-3.6-flash` and `GeminiRotator`.
2. Validated API key connectivity across all 10 keys without 404 deprecation blocks.
3. Scoring constituent claims under Conditions $C1$ and $C2$ with deterministic caching.
4. Record derived item-level faithfulness and update prediction matrix.
5. Absolute Prohibition 1 (The Freeze) and Absolute Prohibition 2 (Gold Isolation) strictly upheld.

## Findings & Evidence (agent)

- 2026-11-01: **Re-aligned with ADR 0002 (`gemini-3.6-flash`)**:
  - Restored canonical model specification to `gemini-3.6-flash` across `src/run/scorers.py`, `src/run/gemini_client.py`, and `src/run/evaluate_corpus.py`.
  - Removed artificial key filter, enabling all 10 API keys in `.env` for round-robin rotation.
  - Added TDD unit tests in `tests/test_scorers.py` and `tests/test_evaluate_corpus.py`. 65/65 tests passing.
- 2026-11-01: **Atomic Persistence & Progress Checkpoint**:
  - Implemented `.tmp` atomic file replacement in `src/run/evaluate_corpus.py` to prevent data loss or file truncation upon interruption.
  - Candidate benchmark ($n=120$): Successfully evaluated items 1 through 30 across conditions $C1, C2, C3$.
  - 145 constituent claims evaluated and cached under `cache/scorers/` and `cache/llm_raw/`.
  - Predictions safely recorded in `data/interim/predictions/predictions_candidates_120.jsonl` (30 items have `arm5_gemini`, items 31–120 remain intact with arms 1–4).
- 2026-11-01: **Free Tier Daily Quota Ceiling Reached**:
  - All 10 free-tier keys reached Google's daily quota limit (`generate_content_free_tier_requests`, 20 req/day/project) with HTTP 429 (`RESOURCE_EXHAUSTED`).
  - Next reset window: ~23 hours (tomorrow).
  - State safely saved and verified. Execution will resume seamlessly from item 31.
- 2026-11-02: **Daily Run Resumed — Items 31 to 56 Completed**:
  - Atomic checkpointing upgraded in `src/run/evaluate_corpus.py` to persist to disk immediately after each completed item.
  - Successfully evaluated items 31 through 56 across conditions $C1, C2, C3$.
  - 328 raw LLM claims cached under `cache/llm_raw/` (up from 145).
  - Predictions recorded in `data/interim/predictions/predictions_candidates_120.jsonl` (56/120 candidate items now have `arm5_gemini`).
  - All 10 keys reached daily free-tier request limit after 24 minutes of active execution.
  - State safely saved. Next execution will resume seamlessly from item 57.
- 2026-11-03: **Daily Run Resumed — Items 57 to 81 Completed with Live Progress & Request Tracking**:
  - Implemented TDD-backed live request tracking in `GeminiRotator` (`total_requests_made`, `total_cache_hits`, `requests_by_key`) and ASCII progress bar in `evaluate_corpus.py` (67/67 tests passing).
  - Successfully evaluated items 57 through 81 across conditions $C1, C2, C3$.
  - Total API requests executed this session: 125 successful calls dispatched across the 10 rotating keys.
  - Cached claims in `cache/llm_raw/` increased from 328 to 455 (+127 new claims evaluated).
  - Benchmark completion: 81 / 120 items complete (67.5% complete; 39 items remaining).
  - All 10 keys reached daily free-tier limit after 21 minutes of rotation.
  - Progress safely flushed and checkpointed to `data/interim/predictions/predictions_candidates_120.jsonl`.
  - Next execution will resume seamlessly from item 82.
- **Prohibitions**: Absolute Prohibition 1 (The Freeze) strictly upheld (0 diff on `sprint-1-frozen` for `src/analyze/` and `src/report/`). Absolute Prohibition 2 upheld (zero writes to `data/raw/labels/`).

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
