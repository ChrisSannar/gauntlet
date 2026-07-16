# Daily Plan — 2026-07-16

## Required boundary

- **Fix critical-path defect from Day 1:** add a `test` script to `frontend/package.json` and deliver at least one passing frontend unit test before any Day 2 product work counts.
- **Fix critical-path defect from Day 1:** write a mastery note that names specific tests, code paths, and model changes in both the AI-verification and uncertainty sections — no generic statements.
- **Day 2 product:** implement tutor-side invitation creation with an opaque, unguessable token persisted in the database.
- **Day 2 product:** keep private tutor notes in a separate field from the invitee-visible message; neither leaks into the other on any response path.
- **Day 2 product:** build the invitee-facing personalized setup page that loads by token and shows the invitee-visible message.
- **Day 2 product:** persist invitation lifecycle state (created → opened → claimed/expired/revoked) with explicit transitions.
- **Day 2 product:** write and pass tests for authorization, invalid-token rejection, and revocation behavior across both backend and E2E layers.
- Push product work and this day's mastery note before midnight America/Chicago.

## Proof required

- `frontend-unit` passes with at least one meaningful unit test (not an empty stub).
- `frontend-typecheck` and `frontend-build` both pass.
- `backend-tests` pass with new invitation lifecycle, authorization, invalid-token, and revocation coverage.
- `critical-path-e2e` passes including a new path: tutor creates invitation → invitee opens setup page by token → invalid token is rejected → revoked token is rejected.
- Mastery note cites specific file paths, test names, and state-transition logic; AI-verification and uncertainty sections each reference concrete evidence.
- No deployed URL, browser-review artifact, or external service required.

## Scope guard

- Claim and session-request behavior belongs to Day 3; do not implement account claim or session submission today.
- Calendar sync, payment, real email, deployment, reminders, lesson notes, files, rescheduling, cancellation, and social login remain optional backlog only.
- Finishing early unlocks optional backlog only after every required bullet above is proven green.
