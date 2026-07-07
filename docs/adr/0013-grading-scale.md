# ADR 0013: Grading scale — A–F, pass ≥ C, unlimited retries until deadline

## Status
Accepted (2026-07-06)

## Context
Grading will be executed by opencode + GLM (or whatever capable model is current)
against hidden rubrics (ADR 0004). Chris wants a typical letter scale and the freedom
to re-attempt repeatedly, with the weekly deadline as the only hard wall.

## Decision
- Each week's milestone is graded **A–F** against its hidden rubric.
- **Pass = C or better.** Below C at the midnight day-7 deadline = Gauntlet failed →
  reset protocol (ADR 0003).
- **Unlimited resubmissions** before the deadline; only the best grade stands.
- **Grades are posted publicly** by the Teacher on X (ADR 0011) — the social pressure
  pushes toward A even though C passes. *(Design call made at Chris's delegation.)*
- Every project ends with a graded **personal critique** — what he'd do differently,
  what the tradeoffs were — which doubles as blog source material.

## Consequences
- Rubrics must define point-weighted checks that map mechanically to letter grades.
- The grader needs a documented invocation ritual (see `.grading/README.md`).
