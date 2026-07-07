# Week 10 Rubric — CodeCardio: The Judge & The Pen
Spec: `specs/flagship-codecardio.md`, Week 10 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-10.md` complete; repo checks out.
- **G2 Live E2E**: on production, a test user can answer a drill free-form and get a
  graded verdict; a review queue exists; the course editor is reachable.
- **G3 Weeks 8–9 hold**: spot-check auth, course generation, CI green.

## A. Drill grading in-product — 20 pts
- **A1 (10)** Submit 4 answers on production (right / wrong / partial / oddly-phrased
  right): structured verdicts naming the specific part of the answer that earned them.
  2.5 each.
- **A2 (5)** Abstain path live: an ambiguous answer flags for review rather than
  guessing; threshold exists in code (cite file:line).
- **A3 (5)** Integrated, not bolted on: grading writes results the product actually
  uses (feeds scheduling/mastery — trace the data flow, cite file:line).

## B. Judge-accuracy re-run — 15 pts
- **B1 (10)** The accuracy harness runs against CodeCardio's judge (labeled set may be
  reused/adapted from Project 3): re-run it; committed report with overall accuracy +
  per-class precision/recall + confusion matrix.
- **B2 (5)** ≥85% agreement → 5; 80–85% → 3 only if the report analyzes the gap and
  names causes; below 80% → 0.

## C. Spaced repetition in-product — 20 pts
- **C1 (8)** FSRS-modeled state per user per drill in Postgres: schema (4) + rows
  updating after graded reviews (4).
- **C2 (8)** Review queue live and mastery gating enforced server-side (direct API
  attempt to advance past an unmastered unit is refused — 5; queue shows due items
  correctly — 3).
- **C3 (4)** Scheduler tests with a test clock exist and pass in this repo.

## D. Agentic course editing in-product — 25 pts
- **D1 (15)** On production: NL feedback → visible plan → scoped-tool edits →
  human-readable diff → apply → rollback restores exact prior state. 3 pts per stage.
- **D2 (10)** Audit log records every tool call (5); edit budget exists and aborts
  gracefully (cite constant + abort path, 5).

## E. Scenario evals re-run — 10 pts
- **E1 (6)** ≥10 scripted scenarios with programmatic assertions run against
  CodeCardio's editor; committed pass-rate report.
- **E2 (4)** ≥8/10 pass on your re-run. 7/10 → 2.

## F. ADR + hygiene — 5 pts
≥1 new ADR on an integration tradeoff this week (3, judged, week 01 G anchors);
commit progression (2).

## G. Stranger flow quality — 5 pts
Drill → grade → queue → edit course, smooth on production: 5 / 2–3 / 0–1.
