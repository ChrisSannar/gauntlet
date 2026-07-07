# Week 11 Rubric — CodeCardio: Launch
Spec: `specs/flagship-codecardio.md`, Week 11 milestone. Follow `.grading/README.md`.
This is the final grade of the Gauntlet — hold the line.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-11.md` complete (must include Stripe test-mode
  card instructions and a fresh-signup path).
- **G2 Custom domain + HTTPS**: the product serves at its custom domain over HTTPS
  with a valid certificate.
- **G3 The stranger test completes**: you, as a brand-new user, finish the full
  journey in section C without any workaround that a real user couldn't perform.

## A. Payment rail — 25 pts
- **A1 (8)** Stripe checkout (test mode acceptable) completes with a test card
  (4242…); the purchased entitlement activates in-product.
- **A2 (5)** Webhooks handled: entitlement is granted via webhook confirmation, not
  optimistic client-side assumption (cite the webhook handler, file:line).
- **A3 (7)** The payment gates a **real boundary**: verify the free-tier limit
  triggers (e.g., generate courses until gated), then payment lifts it.
- **A4 (5)** Failure handling: a declined test card (4000 0000 0000 0002) produces a
  graceful, recoverable state — no crash, no phantom entitlement.

## B. Production bar — 20 pts
- **B1 (8)** Error monitoring quiet: no unresolved P0/P1 in the tracker/dashboard;
  the errors dashboard for the past 48h contains no recurring unhandled exception.
- **B2 (7)** Uptime checks configured (external monitor or platform equivalent) with
  alerting; cite the configuration.
- **B3 (5)** Secrets hygiene: no API keys in client bundles or repo history
  (spot-check built JS + `git log -p` grep for key patterns).

## C. The stranger test — 25 pts
Execute the full journey yourself on production, fresh account. Points per stage:
- **C1 (3)** Sign up, land somewhere comprehensible.
- **C2 (5)** Generate an AI drill course on a topic you choose.
- **C3 (5)** Practice drills; free-form answer graded with explanation.
- **C4 (4)** Review queue materializes (test-clock/dev time control acceptable as the
  documented mechanism for the multi-day part).
- **C5 (4)** Edit the course via NL feedback: plan → diff → apply.
- **C6 (4)** Hit the payment gate, pay with a test card, continue.
Any stage requiring developer intervention scores 0 for that stage.

## D. Polish — 15 pts
- **D1 (5)** Mobile-usable: core flows at ~390px width without broken layout.
- **D2 (5)** Loading, empty, and error states present on the main surfaces (course
  list, generation wait, review queue, editor).
- **D3 (5)** No console errors on the happy path (open devtools through the stranger
  test; warnings ignorable, errors count).

## E. Final retrospective critique — 15 pts (judged)
`docs/CRITIQUE.md`, the full-Gauntlet retrospective. Anchors:
- **(4)** Traces specific capabilities from each principle project into the shipped
  flagship (names files/features, not "I learned agents").
- **(4)** Quantified evidence: eval numbers, judge accuracy, costs, latency — the
  actual measurements from the 11 weeks, compared over time.
- **(4)** Honest failure inventory: what never got fixed, what would break at scale,
  what he'd cut from the curriculum.
- **(3)** A defensible answer to "why should a startup hire you now" grounded in the
  evidence above. Bravado without evidence → 0 for this anchor.

Generic reflection throughout → cap section E at 4.
