# ADR 0006: Optimize for senior-level engineering judgment

## Status
Accepted (2026-07-06)

## Context
Postings in this space skew "Senior Software Engineer." Chris self-assesses: confident
he can build and figure things out, but lacking discernment about *what/why* to build —
translating business ideas into software solutions. Interviews test judgment
((a)-shaped) even when portfolios demonstrate velocity ((b)-shaped).

## Decision
The curriculum optimizes for **judgment signals**, not raw output count. Every project
ships with the artifacts a senior engineer would produce:
- A short **product brief** (the business problem, who pays, why this solution) written
  *before* building — practicing business-idea → software-solution translation.
- **Evals** for LLM behavior, **observability** (logging/tracing of LLM calls),
  explicit **cost and latency budgets**.
- Project-level **ADRs** recording architectural tradeoffs.

## Consequences
- Fewer, deeper projects rather than maximum shipping velocity.
- Rubrics grade the judgment artifacts as first-class requirements, not extra credit.
- These artifacts double as interview material and blog source.
