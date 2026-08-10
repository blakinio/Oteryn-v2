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
updated_at: 2026-08-10T14:41:00+02:00
repair_cycles_for_current_gate: 0
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

Close `ANL-01 — Game Event and Audit Foundation` as the next Stage-B architecture gate after accepted/lifecycle-closed DUR-01. Freeze only the semantic event/audit foundation needed before DUR-02/DUR-03 can finalize transactional outbox and critical item/currency/security evidence.

## Canonical coordination

- canonical issue: #135;
- accidental duplicate/placeholder issues #136, #137, #138, #139 and #140 are closed and have **no architecture authority**;
- PROD-ENTITLEMENTS-01 / #115 remains separate and blocked by Oteryn-Platform#944.

## Accepted inputs

- ADR-0006 Game Intelligence, analytics and audit architecture;
- UUIDv7 durable identity owner baseline;
- FND-ID-01 semantic identifiers/scopes;
- FND-02 CommandId/GameSession/revision semantics;
- FND-03 RuntimeExecutionOrdinal, owner ordering and bounded telemetry behavior;
- accepted/lifecycle-closed FND-04;
- accepted/lifecycle-closed DUR-01 durable representation and ItemInstanceId;
- Foundation Error Vocabulary, Failure Scenarios and Resource Limits Registry.

These are consumed, not reopened.

## Owned decisions

ANL-01 owns:

- EventId, OperationId, TransactionId, CorrelationId, canonical causation-reference semantics and AnalyticsActorId;
- common event-envelope v1 source IDL and event-type registry rules;
- durability/privacy/retention binding classes;
- event schema compatibility and immutable EventId semantics;
- durable audit publication/delivery/dedup/replay checkpoints at semantic level without selecting physical DUR-02 schema or broker;
- transaction-local event ordering and causation rules without a global total order;
- pseudonymization/access/retention/deletion/anonymization/legal-hold contract boundaries;
- event/audit failure/error dispositions;
- ANL-owned hard resource ceilings and deterministic implementation evidence.

## Explicit exclusions

This task does **not** authorize or select:

- PostgreSQL table/outbox/checkpoint layout, transaction isolation, locks, migrations, backups or RPO/RTO (`DUR-02`);
- item/currency transfer/conservation semantics (`DUR-03`);
- broker/stream product (Kafka/NATS/Pulsar/Redpanda/RabbitMQ/etc.);
- warehouse/lake/object-store/dashboard product topology;
- runtime collector implementation;
- ANL-02 balance/world metric definitions;
- ANL-03 detector/sanction logic;
- ANL-04 investigation/AI implementation;
- Platform repository writes;
- production collection, deployment or traffic.

## Delivery plan

1. Produce bounded ANL-01 analysis.
2. Produce normative architecture contract, protobuf envelope source IDL and machine-readable registry.
3. Register ANL-owned hard security/capacity ceilings in the shared resource registry.
4. Update current programme status transition-safely.
5. Perform architecture/security/privacy/data-integrity review with max 3 material repair cycles.
6. Require exact-head Agent Governance, Dependency Review and CodeQL PASS, zero unresolved material threads and terminal exact-head PASS.
7. Squash merge unchanged accepted head.
8. Perform separate lifecycle closeout/archive and close Issue #135.

Runtime/component/browser E2E is `NOT_APPLICABLE` for this architecture-only gate. Later implementation must provide the contract-required DB/serialization/privacy/replay evidence.