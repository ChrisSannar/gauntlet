# Week 05 Rubric — Drillmaster: The Judge
Spec: `specs/project-3-drillmaster.md`, Week 5 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-05.md` complete; repo checks out.
- **G2 Deployed E2E**: as a stranger, take a drill and receive a grade with an
  explanation.

## A. Product brief — 8 pts
- **A1 (2)** `docs/BRIEF.md` predates the bulk of feature code.
- **A2 (6, judged)** 2 pts each: why auto-grading free-form answers is the unlock (a
  business argument, not a feature description); what a wrong grade costs (specific:
  trust/churn mechanics); measurable target for grader quality stated up front.

## B. Drill generation with verifiable answers — 17 pts
- **B1 (5)** ≥3 drill formats exist, at least one free-form. Exercise each on the
  deployed app.
- **B2 (8)** Answer validation is a mechanism, not vibes: find the code that validates
  canonical answers (generated code answers execute; factual answers grounded).
  Cite file:line. Generation-only with no validation → 0.
- **B3 (4)** Spot-check 10 generated drills: canonical answers are actually correct.
  ≥9 → 4; 8 → 2; ≤7 → 0.

## C. Judge grading — 20 pts
- **C1 (5)** Written grading rubric per drill type, committed as artifacts.
- **C2 (8)** Submit 5 test answers of your own design (1 clearly right, 1 clearly
  wrong, 1 partially right, 1 right-but-oddly-phrased, 1 confidently wrong). Each
  verdict must be structured (correct/partial/incorrect) AND point to the specific
  part of the answer earning it. 1.6 pts per answer handled correctly-with-explanation.
- **C3 (7)** Abstain path: craft a genuinely ambiguous answer; below-threshold
  confidence must flag for human review, not guess. Verify the threshold exists in
  code (cite file:line, 3 pts) and the behavior triggers (4 pts).

## D. Grader-accuracy harness — 30 pts
- **D1 (8)** Hand-labeled set ≥100 answers, committed. Sample 10 labels yourself: do
  you agree with ≥9? Includes tricky cases (partial, odd phrasing, confidently wrong)
  — 5 pts size/quality, 3 pts tricky-case coverage.
- **D2 (8)** Re-run the harness with the submission's command: overall accuracy plus
  per-class precision/recall for correct/partial/incorrect all computed.
- **D3 (6)** `docs/JUDGE_ACCURACY.md`: numbers, confusion matrix, failure analysis
  naming specific failure patterns (2 each).
- **D4 (4)** ≥1 documented improvement iteration: judge changed, re-measured,
  before/after numbers shown.
- **D5 (4)** Overall agreement ≥85% on your re-run. 80–85% → 2.

## E. Observability & cost — 7 pts
- **E1 (4)** Per-graded-answer logs: model, tokens, cost, latency (1 each).
- **E2 (3)** `docs/COST_BUDGET.md`: target per graded answer + actuals.

## F. Deployed stranger flow — 10 pts
Full flow (get drills → answer free-form → structured grade with explanation) smooth
for a stranger: 10 smooth / 5–7 rough / 0–4 broken paths.

## G. ADR — 4 pts (judged)
≥1 real-tradeoff ADR (anchors as week 01 G, scaled to 4).

## H. Repo hygiene — 4 pts
≥15 commits over multiple days with coherent messages (2); fresh-clone instructions
work (2).
