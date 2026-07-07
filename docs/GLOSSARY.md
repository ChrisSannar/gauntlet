# Gauntlet Glossary

Living document. Terms are added as they acquire a settled meaning during design.

- **Gauntlet** — this 10-week, all-building curriculum. Inspired by Gauntlet AI's
  weekly pass-or-expelled challenge format, adapted for solo execution.
- **Challenge** — one week's fixed-scope build assignment, defined by a SPEC and judged
  by a hidden rubric. Pass/fail.
- **SPEC** — the visible statement of a challenge's requirements. What Chris builds to.
- **Rubric** — the hidden grading criteria for a challenge, stored in `.grading/`,
  written to be executable by any capable LLM grader (see ADR 0004).
- **Grader** — the LLM instance that scores a completed challenge against its rubric.
- **Flagship** — CodeCardio (https://www.codecardio.org): an existing coding-drill
  platform ("coding drills to improve your syntax memory") with auth, lesson categories,
  and interactive terminal exercises. Buggy and incomplete; the Gauntlet finishes it.
- **Reset** — the failure consequence: all Gauntlet coursework deleted, second attempt
  starts from zero with new projects (see ADR 0003).
- **Deployed** — two tiers (ADR 0010). *Tier 1* (rapid projects): online at a public
  URL, functional for strangers. *Tier 2* (flagship): custom domain, working auth,
  payment rail, error monitoring.
- **Rapid Project** — one of the three ~2-week projects in weeks 1–6, each teaching a
  principle CodeCardio needs (ADR 0008).
- **Flagship Phase** — weeks 7–10, spent entirely finishing CodeCardio to MVP.
- **Style Replicator** — Project 1: derives a model of Chris's writing voice via
  questioning and writing exercises, drafts blog posts in that voice, and publishes
  autonomously via OpenClaw/Hermes (ADR 0008, 0011).
- **The Teacher** — the AI persona running the Gauntlet's X account, posting daily
  progress on Chris's work as itself (ADR 0011).
- **Product Brief** — the pre-build document each project starts with: business
  problem, who pays, why this solution (ADR 0006).
- **Milestone** — the graded deliverable each week ends with; A–F, pass = C or better,
  unlimited resubmissions until the midnight day-7 deadline (ADR 0013).
- **Critique** — the graded self-review closing each project: tradeoffs, what he'd do
  differently. Source material for that project's blog post (ADR 0013, 0015).
- **The Gateway** — `openclaw_backend_gateway`: Chris's unfinished permission-boundary
  server between OpenClaw and his machine; finished as part of Project 1 (ADR 0014).
- **Ghostwriter / Course Forge / Drillmaster / Red Pen** — Projects 1–4 (see
  CURRICULUM.md).
