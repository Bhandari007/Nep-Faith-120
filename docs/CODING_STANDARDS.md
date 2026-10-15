# Research Coding Standards

## The thing that makes research code different

Production code fails by breaking. You notice. Research code fails by *running fine and producing a wrong number*, which then goes into a paper under your name. There's no stack trace, no alert, no user complaining. The bug publishes.

Nearly every standard below follows from that one asymmetry. Research code doesn't need to be robust against load or hostile input. It needs to be robust against *you being confidently wrong*.

A second asymmetry matters almost as much: in a paper, the analysis is a promise. The point of writing it before the data is that you can't tune it toward the result. Any practice that makes the analysis easy to quietly adjust after seeing numbers is a correctness problem, not a style problem.

---

## The five properties, in priority order

### 1. Determinism

Two runs of the same commit on the same inputs produce byte-identical outputs, or you have a bug you haven't found yet.

- One seed, set at the entry point, passed explicitly down. Never a global seed, never a second seed source.
- Pin every version — libraries, model checkpoints, API model strings. `latest` is a time bomb.
- No wall-clock, no `set` or `dict` iteration order dependence, no unsorted file globs feeding a pipeline.
- No network calls in the analysis path. Fetch once, cache, analyze from the cache.

The test: delete all outputs, rerun, diff. If anything differs, find out why before continuing.

### 2. Traceability

Every number in the paper answers "where did this come from?" with a command, not a memory.

- Every figure and table file carries the commit hash and config hash that produced it. Put it in the filename or in a sidecar JSON.
- One config file, versioned, hashed into the outputs.
- Raw data is immutable. Derived data is regenerable. Never edit a data file in place — the edit is invisible six weeks later.

The test: pick a number from a draft at random, and reproduce it from a clean checkout in one command.

### 3. Loud failure

Silence is the enemy. Research pipelines are full of places where a failure degrades into a plausible-looking number.

- No `except: pass`. No bare `except`. If you must continue past a failure, count it and report the count.
- Never silently drop rows. Log the row count at every stage boundary. A dropped row is a sample-selection decision, and sample selection is a scientific choice.
- NaN is a result, not a nuisance. RAGAS returns NaN when claim extraction fails — that rate belongs in your paper, not in a filter.
- Assert invariants in-line: weights sum to what they should, no item appears in two conditions, label sets match the schema.

### 4. Separation by freeze date

Three layers, three change rates, three different moments they stop changing:

| Layer | Freezes | Why |
|---|---|---|
| Data preparation | Once the corpus is built | Changing it invalidates everything downstream |
| Experiment execution | Per run | Reruns are expected and cheap |
| Analysis and reporting | **Before any labels exist** | This is the pre-registered promise |

Mixing analysis into execution is how people end up tuning the analysis without noticing. Keep them in separate modules with a data file between them. The analysis layer should read a file and never call a model.

### 5. Cheap end-to-end reruns

One command, start to finish. If a full reproduction takes a day, you'll stop doing it, and within a week you'll be reasoning about stale numbers without knowing it.

Cache expensive calls aggressively — keyed on input hash plus model version, so a cache hit is provably the same computation.

---

## Testing: a different taxonomy

Standard unit tests check that code does what you told it. Research code needs tests that check whether what you told it was *right*. Five kinds, roughly in order of value:

### Mandatory Test-Driven Development (TDD)

**Tests are written first, always.** Before writing any implementation code in `src/`, the test suite must be established in `tests/`:
1. **Red (Specification First):** Write tests defining expected input/output schemas, statistical bounds, invariants, and failure modes. Verify tests fail or raise expected errors before implementation exists.
2. **Green (Minimal Correctness):** Implement the minimal pipeline logic in `src/` to satisfy the tests cleanly.
3. **Refactor (Clean & Traceable):** Refactor for performance, loud failure, and determinism while ensuring tests stay green.

Never commit implementation code without its accompanying or preceding test suite.

### The Five Research Test Classes

**Recovery tests.** Generate synthetic data where you chose the ground truth. Confirm the pipeline recovers it. This is the single highest-value test in research code and it has no production equivalent. If your estimator can't recover an effect you planted, it can't find a real one.

**Coverage tests.** For anything producing a confidence interval: run many replicates, confirm the 95% CI contains the truth about 95% of the time. If it doesn't, your intervals are decoration.

**Null tests.** Break the signal deliberately — shuffle the labels, randomize the condition assignment — and confirm the effect vanishes. A pipeline that finds an effect in noise is finding it in your data too.

**Invariant tests.** Cheap assertions that catch the embarrassing bugs: no leakage between conditions, sampling weights intact, row counts conserved, no label visible to a scorer.

**Fixture regression tests.** A tiny frozen input with its outputs committed. Catches accidental changes to numerical behaviour during refactors.

Smoke tests (does it run on 10 rows) are table stakes, not a strategy.

---

## Repository shape

```
config/          one versioned config, hashed into every output
data/
  raw/           immutable, never written after ingestion
  interim/       regenerable
  derived/       regenerable
src/
  prepare/       corpus, generation, perturbation
  run/           scorers, models, API calls
  analyze/       estimators, metrics — freezes first
  report/        tables and figures, reads only from analyze/
tests/
  recovery/      known-truth simulations
  invariants/
  fixtures/
cache/           keyed on input hash + model version
outputs/         every file stamped with commit + config hash
notebooks/       exploration only — never produces a paper number
```

The notebook rule is worth stating plainly: notebooks are for *looking*, never for *producing*. Hidden state and out-of-order execution make them unreproducible by construction. The moment a notebook cell generates something that could reach the paper, move it to a script.

---

## LLM-specific rules

Models in the pipeline add failure modes that classical research code doesn't have.

- **Pin the model string, including version.** "the current Haiku" is not a specification. A silent model update invalidates your results and leaves no trace.
- **Temperature 0, and log it.** Also log top_p, max_tokens, and the full prompt.
- **Cache every response**, keyed on prompt hash plus model string. Reruns must not re-cost you and must not produce different numbers.
- **Commit the cache** if size and licensing allow. It's the difference between "reproducible in principle" and "reproducible."
- **Log refusals and malformed outputs separately from successes.** They have a rate, and the rate is a finding.
- **Never let a model's output into a gold field.** Different file paths, so the boundary is physical rather than procedural.

---

## What to skip

Research code at this scale does not need: comprehensive type coverage, abstract base classes, dependency injection, microservices, 90% line coverage on plumbing, elaborate CI, or a plugin architecture for your three scorers.

It does need a minimal CI that runs the smoke test and the recovery tests on every push. That's maybe fifteen lines and it catches the class of bug that matters.

The governing judgment: **ugly and correct beats clean and unfinished.** But invert the usual testing intuition — the parts that touch numbers reaching the paper get tested *harder* than you'd test production code, and everything else gets tested less.

---

## The gate: can this number go in the paper?

Six questions. If any answer is no, the number isn't ready.

1. Can I regenerate it from a clean checkout with one command?
2. Does the code that produced it predate the labels, verifiably, by tag?
3. Did a recovery test confirm this estimator finds a planted effect?
4. Do I know the row count at every stage, including what was dropped and why?
5. Is the model version, seed and config hash recorded alongside it?
6. Has the other person looked at the code path that produced it?

That last one is worth protecting even under deadline. Two people, one number, is the cheapest error-detection mechanism available to a project your size.
