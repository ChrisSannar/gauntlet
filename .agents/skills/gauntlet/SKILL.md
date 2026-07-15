---
name: gauntlet
description: Configure and operate reusable, evidence-driven AI accountability runs with variable timelines, scope, hours, consequences, publishing policy, verification, and LLM adapters. Use when the user invokes /gauntlet or $gauntlet, starts a trial or full Gauntlet, requests a daily plan or midnight grade, manages an appeal, adjusts future difficulty, or evaluates a completed run.
---

# Gauntlet

Run a time-boxed build-and-learn accountability loop. Treat every project as one
configuration of the reusable system; never hard-code a specific project or pilot into
the skill.

## Load the contract

Read only the material needed for the requested operation:

- `docs/run-contract.md` and `schemas/run.schema.json` when configuring a run.
- `runs/README.md` for ledger paths and append-only rules.
- The run's `run.json`, current `plan.md`, backlog, and latest finalized grade when
  operating an active run.
- The configured public rubric and `templates/daily-mastery-note.md` when planning or
  grading.
- `docs/accountability-system-evaluation.md` when finishing or evaluating a run.
- `templates/daily-grade-appeal.md` when handling an appeal.

Do not read `.grading/` or reveal hidden curriculum rubrics during interactive learner
operations. The configured controller/grader may access separately authorized grading
material only when its run contract explicitly requires it.

## Choose one operation

Infer the operation from the request. If ambiguous, report the active run and ask for
the smallest missing decision.

### Configure

1. Start from `templates/run.json`.
2. Collect or derive project, schedule, target hours, cutoff, backlog, verification,
   browser, and adapter configuration.
3. Require explicit user decisions for consequences and publishing. Default both to
   disabled; do not copy authority from another run.
4. Keep a product's draft configuration under `projects/<project>/` only before
   activation. Copy the activated configuration to `runs/<run-id>/run.json`, then
   remove the draft so there is one operational configuration.
5. Validate against `schemas/run.schema.json`. Keep unresolved external values as
   `PENDING` while status is `draft`; never activate a run containing them.

### Start

1. Refuse activation until dates, remote, branch, adapters, verification, and required
   deployment/browser settings are usable.
2. Create `runs/<run-id>/run.json` and the first dated day folder.
3. Freeze the first `plan.md` and copy the mastery template to `mastery.md`.
4. Record the run configuration hash and controller version.
5. Confirm the scheduler installation or clearly mark the run `NOT_AUTOMATED`. Do not
   imply accountability is external when the learner must trigger grading manually.

### Plan

Plan only the next unfrozen day. Read the remaining backlog, dependency order, prior
Delivery and Mastery scores, cited gaps, effort telemetry, stretch completion, defects,
and infrastructure maintenance.

Freeze a finite required boundary containing:

- task IDs and observable outcomes;
- why each task is on the critical path;
- acceptance evidence and exact verification commands;
- dependencies and explicit non-goals;
- one mastery target or transfer/debugging check;
- ordered optional stretch work;
- difficulty estimate and the evidence that informed it.

Never move the boundary after the day begins. Fast completion may pull stretch work and
raise later difficulty, but cannot enlarge today's obligation.

### Wayfind

Use the repo-local `$gauntlet-wayfinder` skill. A wayfinding check is read-only and
cannot grade, edit work, fill the mastery note, or renegotiate the boundary.

### Grade

Midnight grading belongs to the external controller, not learner discretion.

1. Pin the remote-reachable product SHA and Gauntlet evidence SHA at the configured
   cutoff.
2. Reject late, uncommitted, or unpushed evidence.
3. Run deterministic checks and E2E before subjective judgment.
4. Collect live-browser evidence when configured.
5. Distinguish product failure from `INFRA_ERROR`.
6. Invoke the configured grader adapter with the frozen evidence bundle.
7. Score Delivery and Mastery independently using the configured public rubric. Overall
   is the lower score unless the run contract defines another supported rule.
8. Persist machine-readable and human-readable reports with evidence citations,
   confidence, model, prompt, rubric, and controller versions.
9. Append results; never overwrite finalized evidence or reports.
10. Invoke the planner separately to freeze tomorrow's boundary.

Do not commit, push, deploy, repair, or otherwise modify the graded product.

### Appeal

Allow at most one appeal per finalized daily report. Require the appeal template, one
specific error category, and citations to the original frozen bundle. Admit no new
evidence. Use the separately configured appeal judge, preserve the original report, and
append the decision. Reject general requests to try models until one gives a better
grade.

### Finish

After the configured end date, aggregate daily records and evaluate the accountability
system against `docs/accountability-system-evaluation.md`. Report manual interventions,
adapter disagreement, calibration changes, controller failures, appeal behavior, and a
prioritized revision list. Do not retroactively rewrite plans, rubrics, or grades.

## Invariants

- Required work is finite per day; the optional queue may be endless.
- More useful product is the reward for efficient completion.
- Hours are calibration telemetry, never completion points.
- Delivery cannot hide weak Mastery; Mastery cannot hide incomplete Delivery.
- Maintenance and defects compete honestly with feature work.
- Infrastructure failure never becomes learner failure.
- Consequences, publishing, dates, hours, scope, and integrations are run variables.
- External mutations require separately provisioned, narrowly scoped authority and an
  audit record.
- Product-specific material stays inside its `projects/<project>/` folder.

## Communication

Be concise, direct, and evidence-led. During an active run, lead with the current
boundary, status, and next action. Never soften an evidence failure, but never invent a
failure when infrastructure is at fault.
