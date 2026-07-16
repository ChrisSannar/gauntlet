# ADR 0017: Pre-cutoff grading skill and developmental feedback

## Status

Accepted (2026-07-16)

## Context

The local midnight timer added installation, shell-environment, retry, cache, and
observability complexity disproportionate to a personal Gauntlet. It also obscured the
learner's end-of-day ritual. The accountability system still needs an enforceable
deadline, immutable evidence, reproducible grading, and safe infrastructure retries.

Daily grades also need to teach, not merely rank. Numeric Delivery and Mastery anchors
without concrete next actions leave the learner guessing how to improve engineering
proof, system understanding, debugging, AI verification, and transfer.

## Decision

- Make `$gauntlet-grade` the only supported daily grading trigger.
- Require first invocation before the configured cutoff.
- Treat invocation as submission: immediately record it and freeze the pushed product
  and ledger SHAs. Work pushed afterward is ineligible even before midnight.
- Permit completion or retry after the cutoff only when the original receipt and
  complete freeze exist. Never create a late freeze or admit later heads.
- Keep evidence collection, deterministic checks, LLM judgment, report persistence,
  and next-day planning in the provider-neutral controller behind the skill.
- Remove the tracked systemd timer, cron generation, and automatic-close commands.
- Make `schedule.grading_trigger: learner-before-cutoff` explicit in every run contract.
- Require every grade to include evidence-backed strengths, two to five ordered
  improvement actions, and one to three deliberate learning directions with observable
  proof, alongside separate Delivery and Mastery scores.
- Publish detailed evidence anchors and improvement patterns in the public rubric.
- Extend the reusable mastery template with deliberate practice and exact AI
  verification prompts.

This supersedes ADR 0016 only where it requires automatic midnight triggering and an
external scheduler. Frozen-evidence, separate Delivery/Mastery, planner, appeal, and
infrastructure-fairness decisions remain in force.

## Consequences

- The workflow is simpler and visible: push both repositories, then invoke one skill.
- The learner controls whether submission happens. Forgetting to invoke the skill before
  cutoff means no eligible grade; this is a deliberate tradeoff against external
  enforcement.
- Invoking early closes the evidence window early. The skill must warn about this before
  execution.
- A local state directory remains required because receipts and freezes make after-
  cutoff retries fair and idempotent.
- Model or test infrastructure failures remain `INFRA_ERROR`, never learner failure.
- Feedback becomes more actionable without allowing the grader to expand the frozen
  daily boundary; only the next-day planner may turn advice into required work.
