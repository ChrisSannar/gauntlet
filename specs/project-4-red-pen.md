# Project 4: Red Pen (Week 7)

*An agentic course editor. One week. This is the compression test before the flagship.*

CodeCardio's "edit courses with AI" requirement rehearsed: a multi-step, tool-using
agent that modifies course content **safely** — scoped tools, budgets, reviewable
diffs, rollback.

**Stack**: React + TypeScript frontend, Python AI backend. Operates on Course Forge's
course format (reuse Project 2's schema and, ideally, its generated courses).

---

## Week 7 Milestone — The Editor

### Required deliverables

1. **Product brief** (`docs/BRIEF.md`, short — half a page, before building): why
   editing beats regenerating, and who trusts an agent to touch their content.

2. **The editing agent.** Natural-language feedback in ("make unit 2 easier and add
   two exercises about X") → the agent:
   - **plans** (visible plan of intended edits),
   - **edits** course content via scoped tools only (no arbitrary write access to the
     data store — tools like `update_lesson`, `add_check`, `retag_objective`),
   - **presents a reviewable diff** (before/after, human-readable) — nothing applies
     without approval,
   - **applies or rolls back** atomically.

3. **Guardrails**, each demonstrable:
   - tool scoping (the agent cannot touch content outside the targeted course),
   - edit budget (max N operations per request; exceeding aborts with explanation),
   - full audit log of every tool call,
   - rollback restores the exact prior state.

4. **Scenario eval suite**: ≥10 scripted feedback scenarios with programmatic
   expected-outcome checks (e.g., "make it easier" → difficulty tags decrease and
   scaffolding content is added; "remove jargon" → flagged terms gone). Committed
   pass-rate report with failure analysis. Target: ≥8/10 passing.

5. **Observability + cost** per edit session; **≥1 ADR** (agent architecture:
   single-loop vs planner-executor, and why).

6. **Deployed** at a public URL: a stranger can load a sample course, give feedback,
   review the diff, apply it.

7. **Personal critique** (`docs/CRITIQUE.md`): this project closes the same week —
   ≥3 tradeoffs, ≥2 do-differentlys, and one paragraph on what the one-week pace cost
   you (that honesty is part of the grade).
