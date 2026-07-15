# Tutoring Platform

**Dates:** 2026-07-15 through 2026-07-17

**Target:** 30 focused hours across three days

**Product:** operating system for a single-tutor business

**Purpose:** test the Gauntlet accountability system while building useful software

This is a ledger-owned configuration folder, not the product repository. It must not
contain `.git` metadata or application code. Tutoring-platform scope, domain language,
product decisions, and backlog candidates belong here. The operational Gauntlet
configuration lives only at `runs/2026-07-15-tutoring-platform/run.json`. Reusable
Gauntlet machinery stays at the ledger root; application code lives in the separate
`tutoring-platform` repository configured by the active run.

## Continue tomorrow

Resume with [`PRODUCT-GRILLING.md`](PRODUCT-GRILLING.md). It contains the settled
domain model, product policies, deployment constraint, and remaining product questions
from the 2026-07-12 grilling session.

Use [`GLOSSARY.md`](GLOSSARY.md) for product-specific language. Accountability terms
remain in the repository-wide `docs/GLOSSARY.md`.

Do not silently turn unresolved questions into requirements. The adaptive planner may
schedule a product-decision task, freeze its answer, and then schedule implementation.

The frozen required slice is `landing page → personalized invitation → account claim
→ session request`. See [`BOUNDARIES.md`](BOUNDARIES.md). Grading uses only committed
and pushed repository evidence; deployment and external services are not required.
