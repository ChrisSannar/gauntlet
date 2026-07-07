# ADR 0010: Deployment bar — two tiers

## Status
Accepted (2026-07-06)

## Context
"Deployed" needs a mechanical definition for rubrics. Rapid projects and the flagship
warrant different bars.

## Decision
- **Tier 1 (rapid projects, weeks 1–6)**: online at a public URL, accessible and
  functional for strangers. No domain/auth/payments requirement.
- **Tier 2 (CodeCardio, weeks 7–10)**: custom domain, working auth, payment rail
  (test-mode acceptable), and error monitoring (Sentry-class).
- **No real-user requirement** in this Gauntlet — user acquisition is deferred to a
  future marketing/sales Gauntlet.

## Consequences
- Tier 1 grading is a simple external probe: fetch the URL, exercise the feature.
- Tier 2 items are individually verifiable rubric lines.
