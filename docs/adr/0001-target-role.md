# ADR 0001: Target role — AI engineer at an early-stage AI-EdTech startup

## Status
Accepted (2026-07-06)

## Context
"Incorporating AI into EdTech" spans ML research, data science, and LLM application
engineering. Chris has 4 years of professional full-stack experience (front-end,
back-end, database, deployment) and instinctual EdTech domain exposure from that work,
but only one trivially simple LLM API integration shipped (portfolio website). Job
postings observed in this space are mostly titled "Senior Software Engineer."

## Decision
Optimize the entire Gauntlet for **AI/LLM application engineering at an early-stage
AI-EdTech startup**. Classical machine learning (model training, fine-tuning, ML theory)
is explicitly **out of scope** for this curriculum — deferred to a future one.

## Consequences
- Curriculum teaches LLM *application* skills: prompting, RAG, agents, evals,
  structured outputs, streaming, cost/latency engineering — not model training.
- Skills like style transfer ("write in my voice") must be achieved via prompting /
  context engineering, not fine-tuning.
- Because postings skew "Senior SWE," the curriculum must demonstrate senior-level
  signals (system design, production hardening, observability), not just feature-building.
