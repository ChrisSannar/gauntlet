# Week 02 Rubric — Ghostwriter: The Hands
Spec: `specs/project-1-ghostwriter.md`, Week 2 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-02.md` complete; repos check out (project +
  `openclaw_backend_gateway`).
- **G2 Week 1 alive**: the Week 1 deployed app still loads and can generate a draft.
- **G3 Transparent bot**: the Teacher X account exists and its bio plainly discloses
  it is an AI/bot (ADR 0014). Fetch the profile.

## A. OpenClaw running — 10 pts
- **A1 (5)** Evidence OpenClaw is installed and operational: config files in repo or
  documented host, plus logs/audit entries showing it executed publishing actions
  during the week.
- **A2 (5)** OpenClaw's access to accounts/machine goes **through the Gateway** — its
  config must point at the Gateway endpoint, not directly at X/blog APIs. Cite config.

## B. The Gateway — 25 pts
- **B1 (6)** `openclaw_backend_gateway` is complete and running: start it per the
  submission instructions; health endpoint or equivalent responds.
- **B2 (8)** Deny-by-default verified empirically: send a request for an action NOT
  on the allowlist (e.g., a filesystem or arbitrary-HTTP action). It must be refused.
  Evidence: the request and the refusal.
- **B3 (4)** Allowlist contains post-to-X and post-to-blog and is explicit in config
  (not wildcards). Cite file:line.
- **B4 (7)** Audit log: every action (allowed AND refused) is recorded with timestamp,
  actor, action, outcome. Trigger one allowed + one refused action and find both
  entries. 3.5 pts each.

## C. Threat-model ADR — 10 pts (judged)
Anchors, 2.5 pts each, quote passages: enumerates what the agent CAN do; enumerates
what it must NEVER be able to do; maps each "never" to the Gateway mechanism that
enforces it; considers ≥1 failure mode (stolen credentials, prompt-injected agent).

## D. Publishing pipeline — 20 pts
- **D1 (8)** End-to-end: a Ghostwriter draft goes through approval and is published to
  blog and X via the Gateway. Verify a published post pairs with an approval record
  and Gateway audit entry.
- **D2 (8)** Approval is mandatory, enforced server-side: attempt (or have the
  submission demonstrate reproducibly) a publish without approval — it must be
  blocked. UI-only enforcement → max 3.
- **D3 (4)** Approval events are logged (who/when/what draft).

## E. The Teacher is live — 10 pts
- **E1 (7)** ≥3 posts on the Teacher account went through the full pipeline: correlate
  each post with Gateway audit entries (timestamps/content match). ~2.3 pts per post.
- **E2 (3)** Daily cadence: posts on ≥5 distinct days this week (any path pre-pipeline
  per ADR 0014's interim allowance; at least the last ones via pipeline).

## F. Provider-agnostic model swap — 10 pts
- **F1 (4)** Model/provider is configuration, not code: show the config surface; the
  diff to swap is config-only.
- **F2 (6)** Both runs documented with the Week 1 eval harness executed against each
  model, scores recorded. Re-run at least one yourself if credentials allow.

## G. Personal critique — 10 pts (judged)
`docs/CRITIQUE.md`. Anchors: ≥3 concrete tradeoffs each tied to evidence (files,
numbers, incidents) — 4 pts; ≥2 specific do-differentlys with reasoning — 3 pts;
honest engagement with the actual fidelity numbers (including weaknesses) — 3 pts.
Vague reflection ("it went well, I learned a lot") scores ≤2 total.

## H. No regressions — 5 pts
Re-run the Week 1 core flow (elicitation → profile → draft) on the deployed app.
Fully working → 5; degraded → 0–2.
