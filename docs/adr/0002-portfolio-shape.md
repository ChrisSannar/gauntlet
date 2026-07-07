# ADR 0002: Portfolio shape — 3 deployed projects + 1 flagship + blog posts

## Status
Accepted (2026-07-06)

## Context
The hiring signal Chris is optimizing for: "can this person build and deploy?" That is
best evidenced by publicly deployed, working software plus written reasoning about how
it was built.

## Decision
The 10-week Gauntlet produces:
1. **Three deployed projects** — each publicly reachable and functional.
2. **One flagship product** — CodeCardio (https://www.codecardio.org), which already
   exists but has bugs and is not fully developed. The Gauntlet brings it to fully
   deployed, polished completion.
3. **Blog posts** written along the way documenting the work.

## Consequences
- Every project must actually ship to a public URL — "works on my machine" fails.
- The flagship is brownfield work (debugging, hardening, finishing) — a different and
  hireable skill from greenfield building.
- Blog cadence must be built into weekly time budgets, not bolted on.

## Resolved (Round 2)
- Flagship work is a **phase**: weeks 7–10 are entirely CodeCardio (see ADR 0008).
- "Deployed" has two tiers (see ADR 0010).
