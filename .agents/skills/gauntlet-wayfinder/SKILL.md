---
name: gauntlet-wayfinder
description: Check whether active Gauntlet work is headed in the right direction without grading it. Use when the learner invokes $gauntlet-wayfinder or asks for a quick mid-development direction check, priority check, scope check, or confirmation that current work supports today's frozen required boundary.
---

# Gauntlet Wayfinder

Provide a fast, read-only course correction during development. Protect the frozen
daily boundary while identifying the most important next action.

## Inspect

1. Locate the active run under `runs/` and read its `run.yaml`.
2. Read today's `plan.md`, including required tasks, acceptance evidence, dependencies,
   and stretch boundary.
3. Read the in-progress `mastery.md` when it exists.
4. Inspect the configured product repository's status, diff, recent commits, and tests
   relevant to the current task. Inspect the deployed URL only when live-browser access
   is already configured and the check can remain quick.
5. Compare actual work with the frozen plan and its critical path.

If there is no active run or frozen plan, stop and name the missing artifact. Do not
invent today's requirements.

Never read `.grading/` or hidden weekly rubrics. The wayfinder uses only learner-visible
plans, product evidence, and repository-wide accountability contracts.

## Judge direction

Prioritize, in order:

1. Work needed to cross today's required boundary.
2. Broken critical-path behavior, failed tests, security issues, or deployment drift.
3. Missing evidence needed to prove a required task.
4. Mastery gaps the learner should investigate or explain.
5. Stretch work, polish, and speculative architecture.

Treat uncommitted work as valid in-progress evidence. Warn that it cannot count at the
midnight cutoff until committed and pushed.

Do not reward activity, code volume, or time spent. Look for movement toward observable
acceptance evidence and demonstrated understanding.

## Return

Keep the response brief and use this structure:

```markdown
Direction: ON TRACK | AT RISK | OFF TRACK | BLOCKED

Why: <one evidence-based sentence>

Required boundary:
- Done: <verified required outcomes>
- Next: <single highest-value action>
- Missing proof: <tests, deployment, or explanation still needed>

Biggest risk: <one risk, or none>
Avoid for now: <one distraction, or none>
Cutoff warning: <commit/push or mastery-note warning, or none>
```

Give file paths, commands, test names, or deployed behaviors when they support the
finding. Distinguish observed facts from inference.

## Guardrails

- Do not issue points, a letter grade, pass/fail, or a simulated midnight verdict.
- Do not move, add to, weaken, or renegotiate today's required boundary.
- Do not edit code, plans, backlog, or mastery evidence unless the user separately asks
  for implementation after receiving the direction check.
- Do not complete the mastery note for the learner.
- Do not treat optional stretch work as required.
- Do not expose hidden grading material.
- Surface genuine factual blockers; do not classify ordinary difficulty as a blocker.
