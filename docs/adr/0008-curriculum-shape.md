# ADR 0008: Curriculum shape — principle projects, then flagship phase

> **Amended by ADR 0012**: expanded to four rapid projects over weeks 1–7, flagship
> weeks 8–11 (11 weeks planned).

## Status
Accepted (2026-07-06)

## Context
CodeCardio's destiny is **LLM-generated and LLM-edited drill courses** — "make and edit
courses using AI/LLMs" is the MVP bar. Chris wants the early weeks to teach exactly the
principles the flagship needs, then a dedicated final phase to apply them.

## Decision
- **Weeks 1–6**: three rapid projects (~2 weeks each) in the committed stack (ADR
  0007). Each project is chosen so its core principle is one CodeCardio will need.
- **Project 1 (fixed)**: a **writing-style replicator** — derives an acute model of
  Chris's writing voice via rigorous questioning/writing exercises, then drafts his
  blog posts in that voice; includes an autonomous-posting mechanism (OpenClaw/Hermes)
  so an AI can publish on his behalf. Two birds: teaches style/context engineering and
  builds the Gauntlet's own publishing pipeline (ADR 0011).
- **Weeks 7–10**: 100% CodeCardio — bring it to MVP (AI course creation/editing) at
  the full deployment bar (ADR 0010), re-implementing weeks 1–6 principles in Go.

## Consequences
- Projects 2 and 3 must be selected for maximal transfer to CodeCardio (candidates:
  LLM course generation with structured outputs + evals; RAG over learning content;
  agentic content editing; learning-science mechanics like spaced repetition).
- The Go pivot lands inside week 7 and must be budgeted for explicitly.

## Resolved (Round 3)
All four candidates are in (ADR 0012): Project 2 = LLM Course Generator (with RAG
grounding folded in), Project 3 = Exercise Generator + Auto-Grader (with spaced
repetition), Project 4 = Agentic Course Editor. See CURRICULUM.md.
