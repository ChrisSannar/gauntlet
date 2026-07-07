# ADR 0009: Model and budget strategy — open-source-first, under $100/month

## Status
Accepted (2026-07-06)

## Context
Chris holds Claude Code and OpenAI subscriptions but prefers open-source models (e.g.
GLM 5.2) on principle, and plans to shift toward opencode. Postings name Anthropic and
OpenAI APIs, but demonstrated skill with model-agnostic architectures is also a signal.

## Decision
- **Open-source models are the default** for project runtime LLM calls.
- Monthly budget for API + hosting/infra: **under $100**, on top of existing
  subscriptions.
- Projects should be **provider-agnostic by construction** (swap models via config) —
  which both honors the open-source preference and reads well to employers using
  Anthropic/OpenAI.

## Consequences
- Cost engineering is a real constraint, not a hypothetical — eval suites and
  course-generation pipelines must be budgeted per-run.
- Rubrics can require a demonstrated model swap as evidence of provider-agnosticism.
