# Project 3: Drillmaster (Weeks 5–6)

*Exercise generation, automated grading you can trust, and memory that persists.*

CodeCardio's second mechanic: drills with trustworthy grading, scheduled for
retention. The centerpiece skill is **measuring your grader** — an LLM-as-judge is
worthless until you know its accuracy.

**Stack**: React + TypeScript frontend, Python AI backend, Postgres for memory state.
Reading: retrieval practice & the testing effect (week 5); FSRS/SM-2 algorithm
documentation (week 6).

---

## Week 5 Milestone — The Judge

### Required deliverables

1. **Product brief** (`docs/BRIEF.md`, before building): why automated grading of
   free-form answers is the unlock for drill platforms, and what a wrong grade costs
   (learner trust, churn).

2. **Drill generation with verifiable answers.** Given a topic/skill, generate drills
   whose canonical answers are *validated*, not just generated (e.g., generated code
   answers actually execute; factual answers are grounded). ≥3 drill formats,
   including at least one free-form format.

3. **LLM-as-judge grading of free-form student input**, with:
   - a written grading rubric per drill type (the judge prompt is an artifact),
   - structured verdicts: correct/partial/incorrect + *which specific part* of the
     answer earns that verdict (no unexplained grades),
   - an **abstain path**: below a confidence threshold, the judge flags for human
     review instead of guessing.

4. **The grader-accuracy harness** (the centerpiece):
   - a hand-labeled set of ≥100 student answers (you author and label them; include
     tricky cases: partially right, right-but-weird-phrasing, confidently wrong),
   - measured agreement of the judge against your labels: overall accuracy plus
     per-class precision/recall (correct/partial/incorrect),
   - a committed report (`docs/JUDGE_ACCURACY.md`) with the numbers, a confusion
     matrix, failure analysis, and at least one iteration where you improved the judge
     and re-measured. Target: ≥85% overall agreement.

5. **Observability + cost** per graded answer; `docs/COST_BUDGET.md`.

6. **≥1 ADR. Deployed** at a public URL: a stranger can take drills and get graded.

## Week 6 Milestone — The Memory

### Required deliverables

1. **FSRS-based spaced repetition.** Real FSRS scheduling (implement or integrate a
   library — either way you must be able to explain the memory-state model), per-item
   state persisted in Postgres per user.

2. **Scheduler correctness tests.** Automated tests verifying scheduling behavior
   against FSRS reference behavior, including a **test clock**: simulate days passing
   and assert the right items come due (no waiting for real days).

3. **Mastery gating.** Advancement to the next unit is blocked until a defined mastery
   criterion is met (documented in `docs/PEDAGOGY.md` with reference to the reading);
   demonstrably enforced in the UI and API (not just hidden client-side).

4. **Review-queue UX**: due items surface correctly; the loop (drill → grade →
   schedule → resurface) works end-to-end for a real user across simulated days.

5. **Deployed Tier 1**: a stranger can drill, get graded, and see a review queue.

6. **Personal critique** (`docs/CRITIQUE.md`): ≥3 tradeoffs, ≥2 do-differentlys,
   honest read on judge-accuracy and scheduling correctness. **≥1 new ADR.**
