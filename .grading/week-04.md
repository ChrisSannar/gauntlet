# Week 04 Rubric — Course Forge: Grounding & Quality
Spec: `specs/project-2-course-forge.md`, Week 4 milestone. Follow `.grading/README.md`.

## Gates (any failure → F)
- **G1 Submission**: `submissions/week-04.md` complete; repo checks out.
- **G2 Deployed E2E**: as a stranger, upload a corpus (use a public-domain text you
  bring), generate a course from it, and see citations.
- **G3 CI exists**: a CI pipeline runs on push (check the repo's CI config + recent
  run history).

## A. RAG grounding — 20 pts
- **A1 (5)** Corpus upload works with your own document (PDF or markdown, ≥20 pages
  equivalent).
- **A2 (5)** Generated lessons contain citations to the corpus.
- **A3 (10)** Sample 10 citations: each resolves (clickable/inspectable) to a real
  chunk whose content actually supports the cited statement. 1 pt each. A citation
  that resolves but doesn't support the claim = 0 for that citation.

## B. Retrieval evaluation — 15 pts
- **B1 (5)** Labeled query set of ≥20 queries with known-relevant chunks, committed.
- **B2 (5)** Metrics computed (context precision/recall or RAGAS-equivalents); re-run
  the eval command yourself if possible.
- **B3 (5, judged)** Failure analysis: identifies specific failing queries and
  hypothesizes why. Numbers with no analysis → max 1.

## C. Content-quality eval suite in CI — 25 pts
- **C1 (8)** Groundedness check: sampled claims judged against retrieved chunks, with
  a written judge rubric. Run it; verify it catches a fabricated claim if you can
  inject one via its test fixtures — otherwise verify its methodology from code.
- **C2 (6)** Objective-coverage check: verifies every stated objective is exercised by
  content + checks. Cite the implementation.
- **C3 (5)** Difficulty-consistency check: declared level vs. content, judged with a
  written rubric.
- **C4 (6)** Thresholds wired to CI: locate threshold values and confirm CI fails when
  violated (from CI config + code; if run history shows a threshold failure, cite it).

## D. Budget enforcement — 10 pts
- **D1 (10)** Cost/latency budget per course generation enforced in CI (exceeding
  budget fails the run). Cite mechanism + budget values. Documented but not
  enforced → max 3.

## E. Deployed quality — 10 pts
The full stranger flow (upload → generate → inspect citations) is smooth: no errors,
no dead ends, states handled. Fully smooth → 10; works with rough edges → 5–7;
requires workarounds → 0–4.

## F. Personal critique — 10 pts (judged)
`docs/CRITIQUE.md`, project close. Anchors: ≥3 evidenced tradeoffs (4); ≥2 specific
do-differentlys (3); honest engagement with the actual eval/retrieval numbers (3).

## G. ADR — 5 pts (judged)
≥1 new ADR on grounding architecture (chunking/embedding/retrieval choices), real
tradeoff anchors as week 01 G.

## H. Repo hygiene — 5 pts
As week 03 I (3 history / 2 run instructions).
