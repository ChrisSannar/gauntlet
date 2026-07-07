# Week 07 Rubric — Red Pen: The Editor
Spec: `specs/project-4-red-pen.md`. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-07.md` complete; repo checks out.
- **G2 Deployed E2E**: as a stranger, load a sample course, give natural-language
  feedback, see a diff, apply it.

## A. Product brief — 5 pts (judged)
`docs/BRIEF.md` (short is fine): why editing beats regenerating (2.5); who trusts an
agent with their content and what earns that trust (2.5).

## B. Agent core — 25 pts
- **B1 (6)** Visible plan: before editing, the agent shows its intended edits. Verify
  on the deployed app with your own feedback ("make unit 2 easier and add two
  exercises about <topic in the course>").
- **B2 (8)** Scoped tools only: inspect the agent's tool definitions — content changes
  go through named tools (`update_lesson`-class), and the agent has **no** raw
  database/file write path. Cite the tool registry (file:line). Any generic
  execute-SQL/write-file tool reachable by the agent → 0.
- **B3 (6)** Reviewable human-readable diff (before/after) shown prior to apply;
  nothing persists without approval. Try abandoning at the diff — content unchanged.
- **B4 (5)** Atomic apply and rollback: apply, then roll back; state matches the exact
  pre-edit content (compare serialized course before/after).

## C. Guardrails — 20 pts
- **C1 (6)** Cross-course scoping: with two courses present, instruct feedback that
  tempts edits to the other course ("also fix the intro in my other course"). The
  agent must not touch course B. Verify course B is byte-identical after.
- **C2 (5)** Edit budget: find the max-operations constant (cite file:line, 2 pts);
  trigger or trace the abort path with explanation to the user (3 pts).
- **C3 (5)** Audit log: every tool call recorded (timestamp, tool, args, outcome).
  Run one session, count log entries vs. observed actions.
- **C4 (4)** Rollback restores exact prior state (already exercised in B4 — award
  here only if rollback also appears in the audit log and survives a page reload).

## D. Scenario eval suite — 25 pts
- **D1 (10)** ≥10 scripted scenarios with **programmatic** expected-outcome checks
  (assertions on the edited course, not LLM vibes). Read 3 scenarios closely: the
  assertions must actually verify the feedback's intent (1 pt per scenario up to 10,
  but cap at 5 if assertions are superficial, e.g., only "no error thrown").
- **D2 (7)** Re-run the suite yourself; committed pass-rate report with failure
  analysis of any failing scenario.
- **D3 (8)** ≥8/10 scenarios pass on your run. 7/10 → 4; ≤6 → 0.

## E. Observability & ADR — 10 pts
- **E1 (5)** Per-edit-session logs: model, tokens, cost, latency.
- **E2 (5, judged)** Agent-architecture ADR: names the alternative (single-loop vs
  planner-executor or similar), argues from this project's constraints, states
  consequences. Generic → max 2.

## F. Personal critique — 10 pts (judged)
`docs/CRITIQUE.md` (project closes this week). Anchors: ≥3 evidenced tradeoffs (4);
≥2 do-differentlys (3); a candid paragraph on what the one-week pace cost — it must
name something real that was cut or done worse (3; "nothing suffered" → 0).

## G. Deployed stranger flow — 5 pts
Feedback → plan → diff → apply, smooth for a stranger: 5 smooth / 2–3 rough /
0–1 broken.
