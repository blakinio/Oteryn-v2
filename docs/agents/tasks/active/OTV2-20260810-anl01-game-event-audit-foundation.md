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
updated_at: 2026-08-10T14:55:00+02:00
repair_cycles_for_current_gate: 1
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

Close `ANL-01 — Game Event and Audit Foundation` after accepted/lifecycle-closed DUR-01 without implementing runtime, DB schema, broker or production analytics.

## Canonical coordination

- canonical issue: #135;
- accidental duplicate/placeholder issues #136–#140 are closed and have no architecture authority;
- PROD-ENTITLEMENTS-01 / #115 remains separate and blocked by Oteryn-Platform#944.

## Accepted inputs

ADR-0006; UUIDv7 durable identity baseline; FND-ID-01; accepted FND-02/FND-03/FND-04; accepted/lifecycle-closed DUR-01; Foundation Error Vocabulary, Failure Scenarios and Resource Limits Registry.

## Owned decisions

- EventId, OperationId, TransactionId, CorrelationId, typed CausationRef and AnalyticsActorId;
- protobuf/proto3 event envelope v1 + registry/evolution rules;
- BEST_EFFORT_TELEMETRY vs DURABLE_AUDIT;
- privacy/retention production-collection gate;
- atomic evidence/publication/dedupe/replay semantics;
- scoped RuntimeOrderRef and transaction event complete-set evidence;
- shared error/failure/resource-limit integration;
- deterministic future implementation evidence.

## Explicit exclusions

No PostgreSQL table/outbox/checkpoint layout/isolation/locks/migrations/RPO/RTO; no item/currency conservation semantics; no broker/warehouse/lake/dashboard; no collector; no ANL-02/03/04 implementation; no Platform writes; no production collection/deployment/traffic.

## Repair history

### Cycle 1 — exact byte stability, runtime order scope and transaction event completeness

First adversarial review found three material ambiguities:

1. Protobuf does not guarantee a universal canonical byte serialization, so same-EventId retry could reserialize equivalent semantic content into different bytes/hash.
2. A naked RuntimeExecutionOrdinal loses FND-03 ownership-generation scope after failover/replacement.
3. Transaction event ordinal without total event count cannot prove a committed transaction event set is complete.

Repair:

- same EventId retry/reconciliation/redelivery reuses exact materialized payload bytes fixed before the first possibly ambiguous durable attempt; SHA-256 is over those bytes and is integrity evidence, not semantic canonicalization;
- envelope now uses `RuntimeOrderRef(scope_ownership_generation, runtime_execution_ordinal)` and requires explicit WorldId+ChannelId or WorldId+InstanceId scope;
- registered atomic mutation evidence carries both `transaction_event_ordinal` and `transaction_event_count`; ordinals are exact contiguous `1..count` with one consistent count per TransactionId.

## Remaining acceptance plan

1. Continue independent review; max total material repair cycles = 3, current `1/3`.
2. Freeze final head only after no material review finding remains.
3. Require exact-head Agent Governance, Dependency Review and CodeQL PASS.
4. Require zero unresolved material review threads and terminal exact-head architecture/security/privacy/data-integrity PASS.
5. Squash merge unchanged accepted head.
6. Separate lifecycle closeout/archive closes Issue #135 and releases ownership.

Runtime/component/browser E2E is `NOT_APPLICABLE` for this architecture-only gate.