# OTV2-20260810-dur01-durable-identifier-representation

```yaml
task_id: OTV2-20260810-dur01-durable-identifier-representation
title: DUR-01 durable identifier representation
mode: CONTRACT
status: active
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/dur01-durable-identifier-representation
issue: 111
trusted_base_sha: adb0882a5ddbe42944fe955f5effb78fd5495422
owner: GPT-5.6 Sol architecture continuation session
created_at: 2026-08-10T13:56:00+02:00
updated_at: 2026-08-10T13:56:00+02:00
repair_cycles_for_current_gate: 0
max_repair_cycles_for_current_gate: 3
blocker: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260810-dur01-durable-identifier-representation.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_ANALYSIS.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
```

## Goal

Close the Stage-B `DUR-01` architecture gate after accepted/lifecycle-closed FND-04. Freeze only the durable/database identity representation required before persistence and item/economy contracts can safely design authoritative durable state.

## Normative accepted inputs

- `FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md`;
- ADR-0004 PostgreSQL and separate Platform/game data ownership;
- ADR-0006 Game Intelligence analytics/audit separation;
- accepted FND-02 protocol semantics;
- accepted FND-03 runtime/fencing semantics;
- accepted/lifecycle-closed FND-04 A/B/C contracts;
- Platform ADR 0028: canonical native `AccountId` is Platform-issued strongly typed UUIDv7, full 128 bits;
- Platform ADR 0029 for WorldId/ChannelId topology identities where applicable.

These inputs are consumed, not reopened.

## Owned decisions

DUR-01 owns:

- exact PostgreSQL physical representation of accepted durable UUID identities;
- Rust/persistence strong-typing and canonicalization obligations;
- nil/absence rules;
- scoped composite persistence rules;
- identity versus revision/generation/order separation;
- minimum new durable-domain identity needed by DUR-03 (`ItemInstanceId`);
- internal foreign-key and cross-database boundary rules;
- legacy/import anti-corruption mapping rules;
- privacy/public-reference boundary for UUIDv7 exposure;
- representation evolution and migration compatibility;
- deterministic representation evidence required before implementation claims.

## Explicit exclusions

This task does **not** authorize or select:

- concrete table layout, migration SQL/tooling, transaction isolation, row/advisory locks, retry policy, outbox/checkpoint/RPO/RTO (`DUR-02`);
- item movement/split/merge/conservation/anti-dup transaction semantics (`DUR-03`);
- event/audit envelope IDs such as EventId/OperationId/TransactionId/CorrelationId/CausationId/AnalyticsActorId (`ANL-01`, with DUR integration where required);
- protocol wire changes (`FND-02`);
- runtime-local handles/fencing (`FND-03`);
- session/admission/lease semantics (`FND-04`);
- Platform database migration or Platform repository writes;
- application/runtime implementation, PostgreSQL schema creation, deployment or production mutation.

## Delivery plan

1. Produce a bounded analysis that resolves all Issue #111 representation questions against current accepted authority.
2. Produce a final DUR-01 contract only for decisions closed by that analysis.
3. Update current programme status transition-safely.
4. Perform full architecture/security/data-integrity self-review with max 3 repair cycles.
5. Require exact-head Agent Governance, Dependency Review and CodeQL PASS.
6. Require zero unresolved material review threads and terminal exact-head review with zero material findings.
7. Squash merge unchanged accepted head.
8. Perform separate lifecycle closeout/archive and close Issue #111.

Runtime/component/browser E2E is `NOT_APPLICABLE` for this architecture-only gate; the contract defines later implementation evidence.