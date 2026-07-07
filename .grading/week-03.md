# Week 03 Rubric — Course Forge: Generation
Spec: `specs/project-2-course-forge.md`, Week 3 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-03.md` complete; repo checks out at SHA.
- **G2 Deployed E2E**: at the public URL, you (as a stranger) can enter a topic and
  receive a browsable course. Pick a topic unlikely to be cached (e.g., "intro to
  tidal energy for high schoolers").

## A. Product brief — 8 pts
- **A1 (2)** `docs/BRIEF.md` predates the bulk of feature code (first 25% of commits).
- **A2 (6, judged)** 2 pts each: who pays and why generation beats authoring for them;
  what a *bad* generated course costs the business (specific harm, not "it's bad");
  measurable definition of a good course.

## B. Generation pipeline — 22 pts
- **B1 (6)** Deployed generation works on 2 different topics you choose; both produce
  complete, coherent courses.
- **B2 (6)** Schema-constrained: find the schema (course→units→lessons→checks) and the
  validation call (pydantic/zod-class). Cite file:line. Structured-output API usage or
  strict post-validation both acceptable; no validation → 0.
- **B3 (5)** Repair/retry on schema failure exists and is bounded (max attempts
  constant). Cite file:line. Unbounded retry loop → max 2.
- **B4 (5)** Minimum shape on your 2 generated courses: ≥3 units, ≥3 lessons/unit,
  ≥1 check/lesson. 2.5 per course.

## C. Learning objectives — 20 pts
Sample 10 lessons across your 2 generated courses.
- **C1 (10)** Each sampled lesson has ≥1 measurable objective: observable verb +
  criterion. "Understand/know/learn X" = not measurable. 1 pt per passing lesson.
- **C2 (6)** Objectives carry Bloom's-level tags and the tag is plausible for the verb
  (e.g., "list" tagged Create → implausible). ≥9/10 plausible → 6; 7–8 → 4; 5–6 → 2.
- **C3 (4)** Course-level objectives exist and reference/aggregate lesson objectives.

## D. Interactive checks quality — 10 pts
Sample 5 checks across the generated courses.
- **D1 (5)** Varied types: ≥2 distinct check types among the 5; not all
  multiple-choice.
- **D2 (5)** Each sampled check is answerable from its lesson's content and maps to a
  stated objective. 1 pt per passing check.

## E. Pedagogy rules — 10 pts
- **E1 (5, judged)** `docs/PEDAGOGY.md`: concrete sizing rules (length limits,
  concepts-per-lesson) with justification that references cognitive-load reading.
  Rules without justification → max 2.
- **E2 (5)** Enforcement is real: find the enforcing code (cite file:line) AND confirm
  your generated lessons obey the stated limits.

## F. Streaming UX — 10 pts
- **F1 (6)** Generation renders progressively (SSE/streaming — watch the network
  behavior or the UI; an all-at-once spinner → 0).
- **F2 (4)** First meaningful content ≤5s on a typical topic. Time it. 5–10s → 2.

## G. Observability & cost — 10 pts
- **G1 (6)** Per-generation logs: model, tokens, cost, latency (1.5 each).
- **G2 (4)** `docs/COST_BUDGET.md`: target per full course + actuals.

## H. ADR — 5 pts (judged)
≥1 real tradeoff ADR (same anchors as week 01 G).

## I. Repo hygiene — 5 pts
- **I1 (3)** ≥15 commits, multiple days, coherent messages.
- **I2 (2)** Fresh-clone run instructions work.
