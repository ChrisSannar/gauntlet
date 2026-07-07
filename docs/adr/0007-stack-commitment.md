# ADR 0007: Stack commitment — React/TypeScript + Python AI backends

## Status
Accepted (2026-07-06)

## Context
Ten weeks is short; stack-switching burns days. Early-stage AI-EdTech startups are
overwhelmingly React/TS frontends with TS or Python AI services. CodeCardio, however,
already has a Go backend (React, TypeScript, Go, Postgres).

## Decision
- Weeks 1–6 projects: **React + TypeScript frontend, Python AI backend** — one stack,
  for depth and speed.
- **Exception**: CodeCardio keeps its Go backend. The transition into the flagship
  phase includes a deliberate Go re-adjustment period while front-end work (already
  familiar React/TS) carries the early flagship momentum.

## Consequences
- AI-engineering patterns (RAG, evals, agents, streaming) are learned once in Python,
  then *re-implemented* in Go for CodeCardio — which is itself a hireable demonstration
  of transferring patterns across languages.
- No .NET, no Bun-as-backend, no stack tourism during the Gauntlet.
