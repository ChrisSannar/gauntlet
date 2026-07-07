# ADR 0004: LLM grading system — hidden rubrics in `.grading/`

## Status
Accepted (2026-07-06)

## Context
Grading must survive model transitions (the curriculum is being designed by one model;
future weekly grading will be performed by whatever model is current). Rubrics must be
hidden from Chris during the week so he builds to the spec, not to the test.

## Decision
- Each week's grading criteria live in a **`.grading/` folder** in the gauntlet repo,
  written at curriculum-design time.
- Rubrics are **hidden by honor system**: Chris does not read `.grading/` contents.
  Weekly SPECs state the requirements; rubrics state how they are judged.
- Rubrics must be **model-agnostic**: self-contained instructions any capable LLM can
  execute (what to run, what to check, how to score, what constitutes pass/fail).

## Consequences
- Rubrics must be mechanical and evidence-based (run this, fetch that URL, check this
  behavior) rather than vibes-based, so different grader models converge on the same
  verdict.
- Each rubric needs an unambiguous pass threshold.
