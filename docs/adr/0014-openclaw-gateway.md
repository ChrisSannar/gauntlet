# ADR 0014: OpenClaw + backend gateway — Project 1 infrastructure

## Status
Accepted (2026-07-06)

## Context
Chris has never run OpenClaw/Hermes. His intent: OpenClaw is the tool that makes the
blog/X posts autonomously. He previously started (never finished) an interface server
to limit OpenClaw's access to his machine:
https://github.com/ChrisSannar/openclaw_backend_gateway

## Decision
- **Standing up OpenClaw is in Project 1's scope**, including finishing the
  `openclaw_backend_gateway` as the sandboxing/permission layer between the agent and
  the machine — a strong senior-judgment artifact (security boundary design).
- **Reset semantics**: like CodeCardio, the gateway repo reverts to its last
  pre-Gauntlet commit on failure.
- The X persona is a **transparent bot**: bio discloses it is an AI documenting its
  student, and the account complies with X's automation rules and any applicable
  bot-disclosure regulations.
- Chris provisions the X account + API credentials as pre-Gauntlet setup.

## Consequences
- Project 1 has an infrastructure flavor (agent runtime, security gateway, API
  integration) on top of its LLM style-replication core — sized accordingly.
- Until Project 1 ships, week-1 progress posts go out via a manual/interim path.
