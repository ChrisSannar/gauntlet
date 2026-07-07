# Project 1: Ghostwriter (Weeks 1–2)

*A writing-style replicator with an autonomous, security-bounded publishing pipeline.*

**Why this exists (the business frame you must articulate yourself in the brief):**
creators and founders need content in their own voice at a volume they can't write
personally. Ghostwriter derives a rigorous model of one person's voice and drafts for
them — with a human approval gate and an agent that publishes.

**Stack**: React + TypeScript frontend, Python AI backend (ADR 0007).
Open-source-first, provider-agnostic models (ADR 0009).

---

## Week 1 Milestone — The Voice

### Required deliverables

1. **Product brief** (`docs/BRIEF.md` in the project repo, written *before* building):
   the business problem, who would pay, why this solution over alternatives, and what
   "good" measurably looks like. One to two pages.

2. **Corpus intake with held-out discipline.** The user uploads/pastes writing samples
   (Chris's real writing; minimum 10 samples). The system splits them into a *profile
   set* and a *held-out eval set*. The held-out set must never be visible to the
   generation pipeline — enforce this in code, not by convention.

3. **Voice elicitation engine.** An interactive interview + writing-exercise flow
   (minimum 15 questions/exercises across tone, diction, rhythm, structure, stance;
   at least 3 must be *writing exercises*, not multiple choice). Output: a structured,
   versioned **style profile** artifact (JSON or similar, schema-validated).

4. **Draft generation.** Topic/outline in → full article out, in the profiled voice,
   using the style profile + profile-set samples (prompting/context engineering only —
   no fine-tuning, ADR 0001).

5. **Style-fidelity eval harness.** LLM-as-judge scoring generated drafts against the
   *held-out* set on defined dimensions (tone, flow, diction, rhythm). Must include:
   - a written judge rubric (the prompt itself is an artifact),
   - a numeric fidelity score with a documented scale,
   - a **baseline comparison**: the same topics generated *without* the style profile
     must score measurably lower — this proves the profile does real work,
   - results committed as a report (`docs/EVAL_REPORT.md`).

6. **Observability**: every LLM call logged with model, token counts, cost, latency.
   A cost budget documented (`docs/COST_BUDGET.md`): target cost per draft, actuals.

7. **≥1 project ADR** recording a real architectural tradeoff you faced.

8. **Deployed** at a public URL (Tier 1): a stranger can run the elicitation flow and
   generate a draft.

## Week 2 Milestone — The Hands

### Required deliverables

1. **OpenClaw running** as the publishing agent.

2. **The Gateway finished**: `openclaw_backend_gateway` completed as the permission
   boundary between the agent and your machine/accounts. Deny-by-default; explicit
   allowlist (post-to-X, post-to-blog); every agent action audit-logged. Include a
   **threat-model ADR**: what the agent can do, what it must never be able to do, and
   how the gateway enforces that.

3. **Publishing pipeline**: Ghostwriter draft → human approval step (explicit, logged)
   → agent publishes to the blog and to X through the Gateway. No approval, no post.

4. **The Teacher goes live**: the AI-persona X account (transparent bot bio, ADR 0014)
   posts daily Gauntlet progress through this pipeline. At least 3 real posts must
   have gone through the full pipeline by submission.

5. **Provider-agnostic demo**: swap the underlying model via configuration only;
   document both runs (model A and model B) with the eval harness run against each.

6. **Personal critique** (`docs/CRITIQUE.md`, project close): ≥3 concrete tradeoffs
   you made with evidence, ≥2 things you would do differently, honest assessment of
   style-fidelity results. This is graded on specificity, not positivity.

7. All Week 1 systems still deployed and functional (regressions count against you).
