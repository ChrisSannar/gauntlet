# The Gauntlet — AI × EdTech

An 11-week, all-building curriculum forging an **AI engineer for early-stage
AI-EdTech startups**. Inspired by Gauntlet AI: every week is a pass-or-die challenge.
Fail a deadline → total reset (ADR 0003). Design decisions live in `docs/adr/`;
terminology in `docs/GLOSSARY.md`.

**The thesis**: an LLM should be able to build an interactive course for a user. Every
project rehearses a piece of that thesis; the flagship phase assembles the pieces into
CodeCardio.

## Rules of engagement

- **Stack**: React + TypeScript frontend, Python AI backend (weeks 1–7). CodeCardio's
  Go backend is the sole exception (ADR 0007).
- **Models**: open-source-first, provider-agnostic by construction, < $100/month
  API + infra (ADR 0009).
- **Pace**: 6 days × 10 hrs. Each week = 7 calendar days, deadline midnight day 7.
  Finish early → next week can start immediately; the Gauntlet compresses but never
  extends (ADR 0012, 0015).
- **Grading**: A–F against hidden rubrics in `.grading/` (do not read them). Pass = C
  or better at deadline. Unlimited resubmissions before the wall. Grades post publicly
  via the Teacher (ADR 0013). Below C at deadline → reset.
- **Judgment artifacts** (ADR 0006): every project opens with a product brief and
  closes with a graded personal critique; every project ships evals, LLM-call
  observability, and cost/latency budgets; architectural choices get project ADRs.
- **Reading**: ≤ 4–5 hrs/week, assigned per week below, graded only through the build.

## Pre-Gauntlet setup (before Week 1 kickoff)

1. Provision the Teacher's X account + API credentials (free tier suffices; transparent
   bot bio per ADR 0014).
2. Choose blog home (it will be Ghostwriter's publishing target).
3. Snapshot pre-Gauntlet commits of `codecardio` and `openclaw_backend_gateway`
   (reset boundary).
4. Pick an open-source model provider/router and set the monthly spend alarm.
5. Send the kickoff message the day before Week 1.

---

## Phase 1 — Principle Projects (Weeks 1–7)

### Project 1: Ghostwriter (Weeks 1–2)
*A writing-style replicator with an autonomous publishing pipeline.*
**Principle rehearsed**: context/style engineering, LLM-as-judge evals, agent
infrastructure with a real security boundary.

- **Week 1 — The Voice.** Build the elicitation engine: a rigorous interview +
  writing-exercise flow that derives an acute style profile of Chris's writing (tone,
  flow, rhythm, diction). Draft-generation pipeline produces articles in that voice.
  Style fidelity is measured, not vibed: an eval harness scores drafts against a
  held-out corpus of Chris's real writing (LLM-as-judge with calibrated rubric +
  A/B human spot-checks). Deployed Tier 1.
  *Reading: context-engineering and prompting guides; LLM-as-judge calibration.*
- **Week 2 — The Hands.** Stand up OpenClaw; finish `openclaw_backend_gateway` as the
  permission boundary between agent and machine (ADR 0014). Wire autonomous publishing:
  Ghostwriter drafts → Chris approves → agent posts to blog and X. The Teacher account
  goes live and takes over daily progress posts. Provider-agnostic model config
  demonstrated by a live model swap.

### Project 2: Course Forge (Weeks 3–4)
*Topic in, interactive multi-lesson course out.*
**Principle rehearsed**: CodeCardio's core mechanic — structured generation of
pedagogically sound courses, grounded and evaluated.

- **Week 3 — Generation.** Topic → structured course (units → lessons → interactive
  checks) via schema-constrained outputs. Every lesson carries measurable learning
  objectives (Bloom's-aligned). Streaming UX: the course materializes progressively.
  *Reading: Bloom's taxonomy; cognitive load theory basics.*
- **Week 4 — Grounding & Quality.** RAG over an uploaded corpus (textbook, docs) so
  generated courses cite real source material. Content-quality eval suite (factuality,
  objective coverage, difficulty consistency) with per-generation cost/latency budgets
  enforced in CI. Deployed Tier 1.
  *Reading: retrieval evaluation (e.g., RAGAS-style metrics).*

### Project 3: Drillmaster (Weeks 5–6)
*Exercise generation, automated grading, and memory that persists.*
**Principle rehearsed**: CodeCardio's second mechanic — drills with trustworthy
grading, scheduled for retention.

- **Week 5 — The Judge.** Generate drills with verifiable answers; grade free-form
  student input via LLM-as-judge. The centerpiece: a grader-accuracy harness measured
  against a hand-labeled answer set, with anti-hallucination checks and a published
  accuracy number.
  *Reading: retrieval practice & the testing effect (Make It Stick, selected chapters).*
- **Week 6 — The Memory.** FSRS-based spaced-repetition scheduling and mastery gating
  (no advancement without demonstrated competence). Deployed Tier 1.
  *Reading: FSRS/SM-2 algorithm documentation.*

### Project 4: Red Pen (Week 7)
*An agentic course editor.*
**Principle rehearsed**: CodeCardio's "edit courses with AI" requirement — multi-step
tool-using agents that modify content safely.

- **Week 7.** Natural-language feedback ("make unit 2 easier, add exercises on X") →
  agent plans, edits course content, and presents reviewable diffs. Guardrails:
  scoped tools, edit budgets, rollback. Runs against Course Forge's output. Deployed
  Tier 1. One week, hard pace — the compression test before the flagship.

---

## Phase 2 — Flagship: CodeCardio (Weeks 8–11)

Bring https://www.codecardio.org to MVP: **make and edit drill courses with AI**, at
the Tier 2 deployment bar (custom domain, auth, payments, error monitoring — ADR 0010).
Backend is Go: weeks 1–7 principles get re-implemented, proving pattern transfer
across languages (ADR 0007).

- **Week 8 — Re-entry & Hardening.** Go re-adjustment while front-end work carries
  momentum: full bug triage, existing-feature hardening, auth solidified, error
  monitoring live, CI green. The codebase becomes trustworthy before it grows.
- **Week 9 — The Forge, in Go.** AI course creation (Project 2's principles) inside
  CodeCardio: topic → drill course, schema-constrained, objective-tagged, with the
  eval suite ported.
- **Week 10 — The Judge & The Pen.** Drill auto-grading + spaced repetition (Project 3)
  and agentic course editing (Project 4) integrated into the product.
- **Week 11 — Launch.** Payment rail (test-mode), custom domain, polish pass,
  production launch. Final critique: the full-Gauntlet retrospective, published as the
  capstone blog post.

---

## Rituals

- **Kickoff**: Chris messages the day before a week starts; the week's SPEC is then in
  effect for 7 days.
- **Daily**: the Teacher posts progress on X (manual/interim path until Week 2 ships).
- **Submission**: request grading any time; opencode + GLM (or current model) executes
  `.grading/README.md`. Resubmit freely until midnight day 7.
- **Project close**: personal critique graded, blog post published, next project opens.
- **Reset (on failure)**: Gauntlet coursework deleted; `codecardio` and
  `openclaw_backend_gateway` revert to pre-Gauntlet commits; published posts stay up;
  the Teacher posts the failure. Second attempt = new projects, from zero.
