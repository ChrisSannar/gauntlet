# ADR 0003: Stakes and failure protocol — public commitment + full reset

## Status
Accepted (2026-07-06)

## Context
Gauntlet AI's power comes from real expulsion stakes. A solo self-imposed rule has no
teeth. Chris is unemployed with savings, committing 60 hours/week (revised down from 60–80
to leave room for cooking, chores, and networking).

## Decision
- **Enforcement**: public commitment (announcing the Gauntlet and each week's
  pass/fail publicly) + an LLM grader scoring each week against a hidden rubric.
- **Failure consequence**: if a week is failed, **all Gauntlet coursework is deleted —
  reset to zero**. A second attempt is allowed, but no progress carries over and the
  second attempt must use new projects.

## Consequences
- Weekly grading is non-negotiable and must be mechanical enough for an LLM to judge.
- The reset rule makes early weeks as high-stakes as late ones.

## Resolved (Round 2)
- **Reset blast radius**: CodeCardio itself survives a reset; only Gauntlet-era work
  on it is reverted.
- **Public commitment venue**: a dedicated AI-run X account posts daily progress —
  including the failure post if Chris washes out (see ADR 0011).

## Open questions
- Whether published blog posts survive a reset. (Round 3)
