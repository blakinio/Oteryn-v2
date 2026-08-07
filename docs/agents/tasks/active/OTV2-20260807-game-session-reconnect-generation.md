# OTV2-20260807-game-session-reconnect-generation

```yaml
task_id: OTV2-20260807-game-session-reconnect-generation
title: Record GameSession reconnect continuity and transport-generation fencing
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260807-game-session-reconnect-generation
pr: 73
base_sha: 97b29e5c927f319ed03fb5583614d5fe0366d134
owner: ChatGPT architecture coordinator
created_at: 2026-08-07T14:00:00+02:00
updated_at: 2026-08-07T14:14:00+02:00
execution_budget_minutes: 30
owned_paths:
  - docs/agents/tasks/active/OTV2-20260807-game-session-reconnect-generation.md
  - docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md
depends_on:
  - FND-ID-01 account single-online-character baseline
  - PR #72 combat-session duplicate-login protection
blocks:
  - FND-04 must consume logical GameSession continuity, initial 15-second grace policy and transport-generation fencing semantics
  - FND-02 must not freeze reconnect/session wire fields before these semantics are consumed
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Record the owner decision that a bounded eligible reconnect after genuine transport loss preserves the same logical `GameSessionId`, while rebinding control through a newer transport/connection fencing generation, with an initial default reconnect grace window of 15 seconds.

## Accepted decision

- a transient transport/network loss does not by itself end the logical gameplay session;
- reconnect inside the accepted eligibility/grace window may preserve the same `GameSessionId`;
- the owner-accepted initial reconnect grace-window value is `15 seconds`;
- 15 seconds is an initial tunable policy target, not an immutable protocol constant;
- the exact server-authoritative start/measurement instant remains `FND-04` work;
- no separate combat/PZ-specific grace duration has been accepted yet;
- every accepted transport rebind establishes a newer transport/connection generation;
- packets/commands from older transport generations fail closed after the new binding becomes authoritative;
- reconnect resumes the same in-world actor and does not reset combat or gameplay state;
- a new `GameSessionId` is required only after a terminal logical session boundary, not merely after socket/transport loss;
- exact liveness proof, token format, wire field name and persistence remain later contract work;
- no runtime/protocol/persistence/Platform implementation is authorized.

## Acceptance criteria

- [x] Separate logical GameSession identity from concrete transport identity.
- [x] Preserve `GameSessionId` across bounded eligible reconnect.
- [x] Set the initial reconnect grace-window policy to 15 seconds.
- [x] Keep the exact server-side measurement/start semantics deferred to FND-04.
- [x] Require a fresh transport-generation fence on each accepted rebind.
- [x] Reject stale prior-transport commands after rebinding.
- [x] Preserve exact in-world actor state across reconnect.
- [x] Define terminal logical session end as the boundary for issuing a new GameSessionId.
- [x] Preserve duplicate-login/combat anti-abuse decisions.
- [x] Keep implementation and exact protocol representation deferred.
- [ ] Exact-head checks and independent architecture audit before merge readiness.

## Validation

PR #73 owns exactly the two declared documentation paths. Documentation-only architecture decision. The owner subsequently accepted 15 seconds as the initial reconnect grace-window policy value; the exact timer start semantics and any later combat-specific override remain explicit unresolved FND-04/product decisions. Exact-head governance/security checks and independent architecture audit are required before merge readiness.
