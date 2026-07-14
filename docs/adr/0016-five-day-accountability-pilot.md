# ADR 0016: Five-day accountability pilot

## Status
Proposed (2026-07-12)

## Context
Before beginning the full Gauntlet, Chris wants a consequence-free test run from
2026-07-13 through 2026-07-17. The pilot targets 40 focused hours while testing whether
automated AI accountability feels firm, fair, and useful in practice.

The configured build is the tutoring platform defined in
`projects/tutoring-platform/`. Its product scope, domain decisions, backlog candidates,
and build constraints live there instead of in the reusable Gauntlet documentation.
The build is evidence for testing the accountability system; finishing every product
feature is not assumed here.

## Decision
- The pilot runs for five calendar days and targets 40 focused hours.
- There is no repository deletion, public failure, or other hard failure consequence.
- A scheduled job triggers a daily AI review at midnight. Review does not depend on
  Chris remembering or choosing to request it.
- The scheduling and orchestration script is LLM-agnostic. Model/provider selection is
  configuration behind the runner rather than embedded in the grading contract.
- Daily results are retained as pilot evidence so the rubric and accountability loop
  can be adjusted before the full Gauntlet.
- The daily grade primarily answers: **was the required work completed, and does the
  evidence demonstrate learning quality?** Logged hours are calibration telemetry,
  not points awarded for time spent.
- The pilot maintains an ordered backlog of evidence-bearing tasks. Completing the
  expected work substantially faster than intended raises later difficulty or scope;
  struggling despite sound effort lowers, decomposes, or resequences later work.
- Each day's required boundary is finite and frozen before work begins. It represents
  "good enough" for that day and cannot expand after Chris completes it.
- The backlog intentionally remains open-ended. After crossing the required boundary,
  Chris may pull future or stretch work; those completions are retained as real project
  progress and calibration evidence, not retroactively added to that day's obligation.
- The reward for completing work efficiently is that more useful product exists. The
  system does not need an artificial stopping point after the required boundary.
- The midnight workflow grades the completed day, then a separate planner invocation
  automatically freezes the next day's required boundary. Chris may object only to a
  factual error, unavailable dependency, or changed external condition; difficulty by
  itself is not grounds to renegotiate the boundary.
- Defects and maintenance compete with features in the same backlog. The planner may
  require investigation, regression coverage, refactoring, dependency maintenance, or
  bug fixes when those are the highest-value engineering work.
- Grading includes deterministic end-to-end tests and an AI-driven browser review of
  the deployed website. Provisioning a live browser-access tool for the grader is part
  of the pilot setup and later Gauntlet infrastructure.
- Day 1 must satisfy the product workspace's deployment constraint. The final URL is a
  run input and will be configured when Chris supplies it.
- At midnight, only work committed and pushed to the configured remote can satisfy the
  day's required boundary. The runner pins the remote-reachable commit SHA before it
  performs any judgment.
- The evidence bundle includes the frozen daily plan, pinned product commit,
  deterministic test and E2E results, deployed-site browser evidence, and the daily
  mastery note. The note's time and blocker entries calibrate planning but do not award
  completion points.
- The required daily mastery note lives in the Gauntlet run ledger, not the product
  repository and not the deployed application. It must be committed and pushed to the
  Gauntlet remote before midnight using the repository template.
- The evidence bundle pins two repositories: the graded product commit and the Gauntlet
  commit containing the frozen plan and completed mastery note.
- The grader has read-only access to the product repository. It does not commit, push,
  deploy, or repair the student's work.
- A minimal accountability controller is pre-pilot infrastructure and must exist before
  the first product workday. It can trigger on schedule, pin evidence, invoke a
  configured LLM command, and persist a result without learner intervention.
- Controller hardening—including deployment isolation, browser tooling, retries,
  observability, and failure recovery—may enter the pilot backlog as infrastructure
  work after the minimum independent loop exists.
- Each daily report exposes **Delivery** and **Mastery** separately. Delivery answers
  whether the pushed evidence met the frozen boundary; Mastery evaluates demonstrated
  understanding, judgment, debugging, and transfer. An overall grade may summarize
  them but cannot replace either result.
- Delivery and Mastery use public, versioned 0–4 anchors. The overall score is the lower
  of the two, preventing shipped output from hiding weak understanding or strong prose
  from hiding incomplete work.
- The controller, contracts, schemas, installation path, and evaluation method are
  documented for repeat personal runs and possible open-source reuse. Product-specific
  configuration must not leak into the reusable core.
- Timeline, target hours, scope, consequences, publication policy, cutoff, and external
  integrations are per-run configuration. This pilot's values are test inputs, not
  permanent Gauntlet behavior.
- The repo-local `$gauntlet` skill is the reusable LLM-facing lifecycle for configuring,
  starting, planning, operating, appealing, and evaluating runs. The controller supplies
  external scheduling; the skill does not pretend an interactive LLM session is a cron
  service.
- The repo-local `$gauntlet-wayfinder` skill provides an optional, read-only mid-day
  direction check against the frozen plan. It may identify priority, risk, missing
  evidence, and the next best action, but it cannot grade, edit work, or move the
  required boundary.
- One learner-initiated appeal is allowed per finalized day. It must be a committed,
  template-based challenge to one factual or rubric-application error and may cite only
  the original frozen bundle. General regrade requests and new evidence are ineligible.
- Low-confidence grades receive an automatic second-model pass. A dimension disagreement
  greater than 0.5 becomes `REVIEW_NEEDED` rather than an averaged score.
- Posting to X may be rehearsed during the pilot, but publication is not yet decided.

## Consequences
- Missing the voluntary check-in cannot prevent the daily review from running.
- The review needs a deterministic evidence cutoff and a durable result format.
- Scheduling, evidence collection, deterministic checks, and LLM judgment should be
  separate responsibilities so a future model swap does not change the workflow.
- The cron entry should call a repository-owned command; cron itself should contain no
  provider-specific prompt or credentials.
- A short day with complete, high-quality evidence can earn a strong grade. A long day
  without the required evidence cannot earn credit merely from hours logged.
- Task selection and task grading are separate: the adaptive planner changes future
  requirements, while the grader judges frozen requirements against frozen evidence.
- Early completion can change which unfinished tasks are available for the next daily
  plan, but it never erases credit already earned or turns optional work into a hidden
  requirement.
- Browser judgment supplements rather than replaces deterministic E2E assertions. The
  grader should preserve screenshots, traces, or equivalent evidence when practical.
- Uncommitted or unpushed work may be mentioned in the learner-authored mastery note but
  cannot satisfy a required task or change the frozen verdict.
- The intended production home for the controller is Chris's always-on DigitalOcean
  server. Installation details remain configuration rather than grading logic.
- The adaptive planner reacts to Delivery and Mastery independently rather than using
  only the overall letter grade.
- Product deployment excludes learner mastery notes, grades, prompts, and controller
  evidence.
- Missing pushed work or a required mastery note is learner evidence failure. Failed
  product tests and E2E checks are graded product evidence. LLM, network, browser, or
  controller failures are `INFRA_ERROR`, never automatic learner failure.
- Infrastructure failures retry without moving the midnight cutoff and enter the
  maintenance backlog. Retries cannot admit work pushed after the frozen cutoff.
- Appeal decisions append to the ledger without overwriting the original report. A
  denied good-faith appeal carries no grade penalty and exhausts that day's appeal.

## Open questions
- How are effort, shipped product progress, engineering quality, and learning weighted?
- What evidence lets the planner distinguish a task that was too easy from a shallow
  implementation that merely finished quickly?
- Which browser-access tool and E2E framework will be pinned for the pilot?
- What may an X rehearsal generate, and what requires explicit approval to publish?
- What marks the day off, and should that day receive a grade?
