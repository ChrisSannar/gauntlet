# Week 09 Rubric — CodeCardio: The Forge, in Go
Spec: `specs/flagship-codecardio.md`, Week 9 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-09.md` complete; repo checks out.
- **G2 Live E2E**: on production, a logged-in test user can enter a topic and receive
  a persisted, browsable, practicable drill course.
- **G3 Week 8 holds**: auth still solid (spot-check login + one protected route),
  CI still green, error monitoring still wired.

## A. In-product AI course creation — 30 pts
- **A1 (12)** Generate courses on 2 topics of your choosing on production: complete
  drill courses (units → lessons → drills), persisted (survive logout/login),
  immediately practicable. 6 per topic.
- **A2 (6)** The generation service is implemented in the **Go backend** (not a
  side-carred copy of the Python project): cite the Go implementation (file:line).
  A separate Python service called by Go is acceptable ONLY if the submission's
  week-8 brief scoped it and an ADR defends it — then max 3.
- **A3 (12)** Schema-constrained with validation and bounded repair/retry in Go. Cite
  schema (4), validation call (4), bounded retry (4).

## B. Objectives & pedagogy ported — 15 pts
- **B1 (8)** Sample 8 generated lessons: measurable objective (observable verb +
  criterion) on each. 1 pt each.
- **B2 (7)** Lesson-sizing rules from Project 2's `PEDAGOGY.md` enforced here: cite
  enforcing Go code (4) and confirm sampled lessons obey the limits (3).

## C. Content-quality evals in CI — 20 pts
- **C1 (12)** The quality suite (groundedness where applicable, objective coverage,
  difficulty consistency) runs against CodeCardio-generated courses. Harness language
  is free; it must execute in CI. Verify a CI run that executed it (4 per check type).
- **C2 (8)** Thresholds fail CI when violated: cite threshold values + wiring; run
  history or a forced-failure fixture as evidence.

## D. LLM observability in Go — 15 pts
- **D1 (9)** Per-call logs from the Go service: model, tokens, cost, latency. Generate
  a course, then locate its log entries (2.25 each).
- **D2 (6)** Provider-agnostic config: model/provider swappable via configuration in
  the Go service; show the config surface (3) and evidence of two providers/models
  having been exercised (3).

## E. ADR — 5 pts (judged)
≥1 ADR on the Go AI-service architecture (where the AI layer lives, sync vs async
generation, schema strategy). Week 01 G anchors.

## F. Stranger flow quality — 10 pts
The topic → course → practice flow on production is smooth: 10 smooth / 5–7 rough /
0–4 broken.

## G. Repo hygiene — 5 pts
Real commit progression this week (3); CI configuration comprehensible and green (2).
