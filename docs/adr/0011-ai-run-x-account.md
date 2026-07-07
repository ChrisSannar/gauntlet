# ADR 0011: Public accountability via an AI-run X account

## Status
Accepted (2026-07-06)

## Context
Public commitment needs a venue with real social stakes. Chris proposed giving the AI
its own X (Twitter) account that posts his daily progress — "a teacher showing off his
student" — including posting about it if he fails and gets reset.

## Decision
- A dedicated **AI-persona X account** posts daily progress during the Gauntlet.
- The account posts **as itself** (the AI teacher), not impersonating Chris.
- Failure is posted too — this is the enforcement teeth of ADR 0003.
- The posting mechanism is **built as part of Project 1** (style replicator +
  OpenClaw/Hermes autonomous posting, ADR 0008), making the accountability
  infrastructure itself graded coursework.

## Consequences
- Requires an X developer account / API credentials and an always-on runner — a
  session-based CLI agent cannot post daily on its own.
- Until Project 1 ships, week-1 posting needs an interim manual or semi-automated path.

## Open questions
- Who provisions the X account and API tier; feasibility within free/cheap API limits.
  (Round 3)
- Disclosure framing on the account bio ("I am an AI documenting my student"). (Round 3)
