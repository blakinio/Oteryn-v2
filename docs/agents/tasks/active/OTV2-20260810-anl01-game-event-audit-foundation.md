# OTV2-20260810-anl01-game-event-audit-foundation

```yaml
task_id: OTV2-20260810-anl01-game-event-audit-foundation
title: ANL-01 game event and audit foundation
mode: CONTRACT
status: active
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/anl01-game-event-audit-foundation
issue: 135
trusted_base_sha: ef42fa47ab054ab8aa304c017307c1945f931b59
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-10T14:41:00+02:00
updated_at: 2026-08-10T15:01:00+02:00
repair_cycles_for_current_gate: 2
max_repair_cycles_for_current_gate: 3
blocker: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260810-anl01-game-event-audit-foundation.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_ANALYSIS.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/contracts/GAME_EVENT_FOUNDATION_REGISTRY.json
  - docs/contracts/game-events/v1/foundation.proto
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
```

## Goal

Close `ANL-01 — Game Event and Audit Foundation` after accepted/lifecycle-closed DUR-01 without runtime/DB/broker/production implementation.

## Canonical coordination

- canonical issue: #135;
- accidental duplicate/placeholder issues #136–#140 are closed and have no architecture authority;
- #115 entitlement gate remains separate/blocking on Oteryn-Platform#944.

## Owned decisions

Event/operation/transaction/correlation identities; typed causation; AnalyticsActorId; protobuf envelope/registry; durability/privacy/retention; immutable event retry; RuntimeOrderRef; TransactionEventRef; atomic audit/publication/dedupe/replay; failure/error/resource limits/evidence.

## Explicit exclusions

No PostgreSQL layout/isolation/locks/migrations/RPO/RTO; no DUR-03 conservation semantics; no broker/warehouse/lake/dashboard; no runtime collector; no ANL-02/03/04 implementation; no Platform writes; no production collection/deployment/traffic.

## Repair history

### Cycle 1 — byte stability, runtime order scope, transaction completeness

Findings:

1. Protobuf alternate valid serializations could make reserialized same-EventId retry drift in bytes/hash.
2. Naked RuntimeExecutionOrdinal was ambiguous without ownership generation.
3. Transaction ordinal without total count could not prove complete event set.

Repairs:

- exact payload bytes fixed before first ambiguous durable attempt and reused across same-EventId retry/redelivery;
- RuntimeOrderRef = scope ownership generation + runtime ordinal, with concrete channel/instance scope;
- count added to transaction event evidence.

### Cycle 2 — structural transaction binding, epoch unlinkability, full envelope immutability

Findings:

1. Independent TransactionId/ordinal/count fields still allowed partial malformed combinations.
2. Epoch-scoped AnalyticsActorId still allowed the same UUID to be reused across epochs, defeating ordinary unlinkability.
3. Payload byte immutability did not explicitly freeze all semantic envelope values across same-EventId ambiguous retry.

Repairs:

- one atomic `TransactionEventRef(transaction_id, ordinal, count)`; later observations use CausationRef::Transaction instead of partial membership;
- same operational actor receives a fresh AnalyticsActorId in each new epoch; ordinary consumers get no implicit cross-epoch join key;
- EventId now binds all semantic envelope field values plus exact payload bytes; raw protobuf envelope byte ordering is not semantic.

## Final acceptance plan

1. One final adversarial review remains; repair budget `2/3`.
2. If no material issue remains, freeze final head. If one exists, cycle 3 is the last permitted repair; any later material finding blocks/rotates the gate.
3. Require exact-head Agent Governance, Dependency Review and CodeQL PASS.
4. Require zero unresolved material review threads and terminal exact-head architecture/security/privacy/data-integrity PASS.
5. Squash merge unchanged accepted head.
6. Separate lifecycle closeout archives task, releases ownership and closes Issue #135.

Runtime/component/browser E2E is `NOT_APPLICABLE` for this architecture-only gate.