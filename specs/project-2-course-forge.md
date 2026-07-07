# Project 2: Course Forge (Weeks 3–4)

*Topic in, grounded interactive multi-lesson course out.*

This is CodeCardio's core mechanic rehearsed in Python: an LLM builds an interactive
course for a user — structured, pedagogically sound, grounded in real sources, and
evaluated for quality.

**Stack**: React + TypeScript frontend, Python AI backend. Reading budget this
project: Bloom's taxonomy, cognitive load theory basics (week 3); retrieval
evaluation metrics (week 4).

---

## Week 3 Milestone — Generation

### Required deliverables

1. **Product brief** (`docs/BRIEF.md`, before building): who pays for generated
   courses, why generation beats authoring, and what a *bad* generated course costs
   the business.

2. **Course generation pipeline.** User provides a topic (+ optional audience/level)
   → a complete structured course: course → units → lessons → interactive checks.
   - Schema-constrained generation (structured outputs), validated with
     pydantic/zod-class validation; automatic repair/retry on schema failure with a
     bounded retry count.
   - Minimum output shape: ≥3 units, ≥3 lessons per unit, ≥1 interactive check per
     lesson with varied check types (not all multiple-choice).

3. **Learning objectives, done properly.** Every lesson carries ≥1 measurable
   objective: an observable verb + criterion (no "understand X"), tagged with its
   Bloom's level. Course-level objectives roll up from lessons.

4. **Cognitive-load-informed design.** Documented lesson-sizing rules (length limits,
   concept-per-lesson limits) with a short written justification referencing the
   reading (`docs/PEDAGOGY.md`). The generator enforces these rules.

5. **Streaming UX.** The course materializes progressively in the UI (SSE or
   equivalent); first meaningful content visible in ≤5 seconds on a typical topic.

6. **Observability + cost**: per-generation cost, tokens, latency logged;
   `docs/COST_BUDGET.md` with target cost per full course generation.

7. **≥1 project ADR.** **Deployed** at a public URL (rough is fine this week; a
   stranger can generate and browse a course).

## Week 4 Milestone — Grounding & Quality

### Required deliverables

1. **RAG grounding.** User uploads a corpus (PDF/markdown/docs). Pipeline: chunking →
   embeddings → retrieval. Generated lesson content **cites its sources**, and every
   citation resolves to a real chunk of the uploaded corpus (clickable/inspectable in
   the UI).

2. **Retrieval evaluation.** A labeled query set (≥20 queries with known-relevant
   chunks) and computed retrieval metrics (context precision/recall or RAGAS-style
   equivalents), committed as a report with your analysis of failures.

3. **Content-quality eval suite**, run in CI, with explicit thresholds:
   - **Groundedness/factuality**: sampled claims from generated lessons are checked
     against retrieved chunks (LLM-as-judge with a written rubric).
   - **Objective coverage**: every stated objective is actually exercised by lesson
     content + checks.
   - **Difficulty consistency**: declared level matches content (judged).
   CI fails when thresholds are violated.

4. **Budget enforcement**: cost/latency budget per course generation enforced in CI
   (a run exceeding budget fails the pipeline).

5. **Deployed Tier 1** at quality: a stranger can upload a corpus, generate a grounded
   course, and inspect citations.

6. **Personal critique** (`docs/CRITIQUE.md`): ≥3 tradeoffs, ≥2 do-differentlys,
   honest read on the eval numbers. **≥1 new ADR** for the grounding architecture.
