# Week 01 Rubric — Ghostwriter: The Voice
Spec: `specs/project-1-ghostwriter.md`, Week 1 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-01.md` exists with repo, SHA, deployed URL, run
  commands. Repo checks out at SHA.
- **G2 Deployed**: fetch the deployed URL; the app loads and is interactive.
- **G3 No fine-tuning** (ADR 0001): grep the codebase for fine-tune API usage
  (`fine_tun`, `/fine-tuning`, training-job calls). Any runtime fine-tuning → gate fail.

## A. Product brief — 10 pts
- **A1 (2)** `docs/BRIEF.md` exists and predates the bulk of feature code: check
  `git log --follow docs/BRIEF.md` — its first commit must be within the repo's first
  25% of commits. Evidence: commit dates.
- **A2 (8, judged)** Anchors — award 2 pts each, quote passages: names a specific
  paying customer type (not "writers everywhere"); states the business problem in
  cost/time terms; compares ≥1 real alternative and says why this wins; defines
  measurable "good" (a number or observable behavior).

## B. Corpus & held-out discipline — 15 pts
- **B1 (5)** Via the deployed app, corpus intake accepts ≥10 samples. Evidence: do it
  (use public-domain text as dummy samples).
- **B2 (3)** Code shows a profile/eval split with the split recorded (seed or manifest).
- **B3 (7)** Isolation is enforced in code: trace the generation path and confirm it
  cannot read the held-out set (separate storage/table/namespace, or access guarded).
  A comment saying "don't use eval set" with shared access = 0. Cite file:line.

## C. Elicitation engine — 20 pts
- **C1 (6)** Run the full flow on the deployed app: ≥15 questions/exercises spanning
  ≥4 of: tone, diction, rhythm, structure, stance.
- **C2 (4)** ≥3 items are free-writing exercises (you type prose), not multiple choice.
- **C3 (6)** Output is a structured style profile validated against a schema — find the
  schema and the validation call; cite file:line. Inspect a produced profile.
- **C4 (4)** Profiles are versioned (version field + stored history, or equivalent).

## D. Draft generation — 10 pts
- **D1 (6)** On the deployed app: give a topic, receive a complete article (≥500
  words, coherent, in a discernible consistent voice).
- **D2 (4)** Code confirms generation consumes the style profile AND profile-set
  samples (few-shot/context). Cite file:line.

## E. Style-fidelity eval harness — 25 pts
- **E1 (4)** The judge rubric/prompt is a committed artifact; it defines the scored
  dimensions (tone, flow, diction, rhythm at minimum).
- **E2 (5)** Run the harness yourself using the submission's eval command. It produces
  a numeric fidelity score; the scale is documented.
- **E3 (10)** Baseline comparison: harness (or committed report) shows profiled
  generation vs. no-profile baseline on the same topics. Full 10 only if you can
  re-run it and the profiled score beats baseline by a nontrivial margin (>5% of the
  scale). Re-run impossible but report is complete and credible → max 5.
- **E4 (6)** `docs/EVAL_REPORT.md` committed: numbers, methodology, at least one
  honest limitation.

## F. Observability & cost — 10 pts
- **F1 (6)** Generate a draft, then find its log entries: model, input/output tokens,
  cost, latency all present. 1.5 pts per field.
- **F2 (4)** `docs/COST_BUDGET.md`: target cost per draft + measured actuals.

## G. Project ADR — 5 pts (judged)
- ≥1 ADR recording a real tradeoff: names ≥2 options, gives a reason grounded in this
  project's constraints, states consequences. Generic ("we chose React because it's
  popular") → 1. Real tradeoff with consequences → 5.

## H. Repo hygiene — 5 pts
- **H1 (3)** Commit history shows real progression: ≥15 commits over multiple days
  with coherent messages (one giant dump → 0).
- **H2 (2)** Fresh-clone run instructions from the submission actually work.
