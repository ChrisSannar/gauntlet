# Week 08 Rubric — CodeCardio: Re-entry & Hardening
Spec: `specs/flagship-codecardio.md`, Week 8 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-08.md` complete; CodeCardio repo checks out.
- **G2 Live**: https://www.codecardio.org (or the submission's production URL) loads
  and login works with the provided test credentials.
- **G3 CI exists** and ran on recent pushes.

## A. Flagship product brief — 8 pts (judged)
`docs/BRIEF.md`: the MVP feature list scoped from the spec's MVP definition (3);
explicit non-goals with reasons (3); a sequencing rationale for weeks 8–11 (2).

## B. Bug triage — 15 pts
- **B1 (6)** `docs/TRIAGE.md`: a complete inventory — cross-check by exploring the
  live product yourself for 15 minutes; every defect you find must already be in the
  triage doc (each miss −2, floor 0).
- **B2 (5)** Sample 3 listed bugs: repro steps are followable and accurate.
- **B3 (4, judged)** P0–P3 prioritization has stated rationale tied to user impact.

## C. P0/P1 fixes with regression tests — 25 pts
- **C1 (13)** Every P0 and P1 in the triage doc is fixed: verify each on the live
  product using the triage repro steps. Points split evenly across P0/P1 items; an
  unfixed P0 → the whole check scores 0.
- **C2 (12)** Each fixed P0/P1 has an associated regression test: match tests to bugs
  (commit messages/test names referencing the bug). Run the suite. Points split evenly.

## D. Auth solidified — 20 pts
Verify each live (2 pts each, 12 total): signup with a fresh email; login; logout
(session actually invalidated — back button/API calls fail); session expiry configured
(inspect cookie/token TTL); protected routes reject unauthenticated API calls (curl
them directly); no auth secrets in client code.
- **D-tests (8)** Automated auth tests exist covering signup/login/logout/protected
  routes (2 each). Run them.

## E. Error monitoring — 10 pts
- **E1 (6)** A Sentry-class service is wired in production: trigger or have the
  student trigger a test error; confirm it appears in the dashboard (screenshot or
  read access counts as evidence).
- **E2 (4)** Both backend and frontend errors are captured (2 each).

## F. CI green and blocking — 10 pts
- **F1 (6)** CI runs build + full test suite on every push; latest run green.
- **F2 (4)** Failing CI blocks merge (branch protection or documented equivalent).

## G. Navigation/UX debt — 7 pts
Crawl the live product: no truncated nav (2), no dead links (2), empty states handled
on content-less pages (3).

## H. Repo hygiene — 5 pts
Gauntlet-era commits show real progression (3); local dev setup instructions work (2).
