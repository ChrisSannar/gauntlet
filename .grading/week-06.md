# Week 06 Rubric — Drillmaster: The Memory
Spec: `specs/project-3-drillmaster.md`, Week 6 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-06.md` complete; repo checks out.
- **G2 Deployed E2E**: as a stranger, drill → get graded → a review queue exists for
  your account.
- **G3 Week 5 alive**: judge grading from Week 5 still functions.

## A. FSRS implementation — 25 pts
- **A1 (10)** Real FSRS, not naive fixed intervals: the code models memory state
  (stability/difficulty/retrievability or library equivalent) and computes intervals
  from it. Cite file:line. A hardcoded `[1, 3, 7, 14]`-style ladder → 0. A vetted FSRS
  library correctly integrated earns full points.
- **A2 (8)** Per-item, per-user memory state persisted in Postgres: inspect the schema
  (migration or live) — 4 pts; confirm rows update after a graded review — 4 pts.
- **A3 (7, judged)** The student can explain the model: docs or ADR explaining the
  memory-state variables and how grades move them, in their own words with reference
  to the FSRS reading. Restated marketing copy → max 2.

## B. Scheduler correctness tests — 20 pts
- **B1 (8)** Automated scheduler tests exist and pass when you run them.
- **B2 (8)** Test clock: tests simulate days passing and assert which items come due
  (no real-time waiting). Cite the clock injection mechanism (file:line).
- **B3 (4)** At least one test compares behavior against FSRS reference expectations
  (documented expected intervals for a grade sequence).

## C. Mastery gating — 15 pts
- **C1 (5, judged)** Mastery criterion documented in `docs/PEDAGOGY.md` with reference
  to the retrieval-practice/mastery reading. Arbitrary threshold with no rationale →
  max 2.
- **C2 (10)** Enforced server-side: call the API directly (bypassing the UI) to
  attempt advancing past an unmastered unit — must be refused. UI-only gating → max 3.

## D. Review loop end-to-end — 15 pts
- **D1 (10)** Using the test clock (or an admin/dev time control), drive a user
  through: drill → grade → scheduled → comes due on the right simulated day →
  resurfaces in the queue. 10 if the full loop verifies; partial per stage.
- **D2 (5)** Due-item correctness: items NOT yet due do not appear; overdue items do.

## E. Deployed stranger flow — 10 pts
Drill → grade → queue visible and comprehensible to a stranger: 10 smooth / 5–7 rough
/ 0–4 broken.

## F. Personal critique — 10 pts (judged)
`docs/CRITIQUE.md`, project close. Anchors: ≥3 evidenced tradeoffs (4); ≥2
do-differentlys (3); honest engagement with judge-accuracy and scheduler-correctness
results (3).

## G. ADR — 5 pts (judged)
≥1 new ADR (e.g., FSRS build-vs-integrate, state-storage design). Week 01 G anchors.
