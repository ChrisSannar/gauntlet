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
- **Accountability Pilot** — a consequence-free, time-boxed rehearsal before the full
  Gauntlet. Its current run targets 40 focused hours over five days while using daily
  results to calibrate the accountability system (ADR 0016).
- **Daily Review** — an automatically triggered midnight assessment of a frozen day's
  evidence. It runs whether or not Chris requests it and produces a durable result.
- **Grade Runner** — the repository-owned, provider-neutral command invoked by an
  external scheduler to collect evidence, run checks, request LLM judgment, and save
  the daily review.
- **Task Backlog** — the dependency-aware, difficulty-ranked pool from which daily
  project work is selected. Tasks state their completion evidence so the grader can
  judge them without inventing requirements after the fact.
- **Adaptive Planner** — the component that uses completion quality, elapsed effort,
  blockers, and prior grades to select or reshape later backlog work. It assigns work
  but does not grade it.
- **Required Boundary** — the frozen set of tasks whose evidence is graded for a given
  day. Work outside it may inform difficulty calibration but cannot retroactively
  redefine whether the day succeeded.
- **Stretch Work** — backlog work pulled after crossing the day's required boundary.
  It counts as real project progress and planning evidence but is not required to pass
  the day on which it was pulled.
- **Maintenance Work** — defects, regression coverage, refactoring, dependency upkeep,
  and operational repairs. It competes with feature work in the same task backlog.
- **Live Product Check** — an AI-driven browser review of the deployed product using a
  pinned browser-access tool. It produces review evidence and complements E2E tests.
- **E2E Gate** — deterministic browser automation that verifies critical user journeys
  against the running application as part of daily grading.
- **Evidence Cutoff** — midnight in the pilot's configured timezone, when the grade
  runner pins the remote-reachable commit and closes the day's evidence window.
- **Evidence Bundle** — the immutable inputs for one daily review: frozen plan, pinned
  commit, test and E2E results, deployed-site browser evidence, and work log.
- **Accountability Controller** — the externally scheduled service that closes the
  evidence window, invokes the grade runner, persists the result, and freezes the next
  plan without waiting for learner action.
- **Mastery Note** — required learner-authored daily evidence stored in the Gauntlet
  run ledger. It records reasoning, debugging, system understanding, AI contribution,
  personal verification, and calibration telemetry; it is never deployed with the
  graded product.
- **Wayfinder** — a read-only mid-development direction check against the frozen daily
  plan. It reports priority, risk, and missing proof without issuing a grade or changing
  requirements.
- **Infrastructure Error** — failure of the controller, model, network, or browser
  tooling. It triggers retry and maintenance evidence, not learner failure.
- **Appeal** — one committed, evidence-cited challenge to a specific factual or rubric-
  application error in a finalized daily report. It cannot add evidence or request a
  general regrade.
- **Gauntlet Skill** — the reusable LLM-facing lifecycle that configures and operates
  variable accountability runs. Scheduling and external enforcement remain controller
  responsibilities.
