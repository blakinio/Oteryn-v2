# ANL-01 — Game Event and Audit Foundation Analysis

- Status: bounded decision analysis for Issue #135
- Date: 2026-08-10
- Trusted base: `main@ef42fa47ab054ab8aa304c017307c1945f931b59`
- Gate: `ANL-01`
- Does not authorize: runtime, PostgreSQL schema, broker, warehouse, detector, Platform or production implementation

## 1. Purpose

ADR-0006 already accepts Oteryn Game Intelligence and three distinct data classes: low-cardinality operational observability, bounded best-effort gameplay telemetry and durable economy/security audit. ANL-01 turns that direction into a precise event/audit contract that DUR-02/DUR-03 can consume without guessing identity, causation, ordering, atomic publication, privacy or schema evolution.

```text
runtime/gameplay authority        -> FND/gameplay owners
command/session authority         -> FND-02/FND-04
durable representation           -> DUR-01
persistence transaction/schema    -> DUR-02
item/currency conservation        -> DUR-03
event/audit semantics             -> ANL-01
analytics/security consumers      -> ANL-02/03
read-only investigation/AI        -> ANL-04
```

ANL-01 is evidence architecture, not event sourcing and not gameplay authority.

## 2. Accepted inputs not reopened

- `CommandRef = (GameSessionId, CommandId)` remains FND-02 identity/order.
- RuntimeExecutionOrdinal is scoped to semantic runtime scope + ownership generation.
- connection/ownership generations and revisions remain fences/order values, not entity/event IDs.
- durable UUIDv7 IDs use DUR-01 lossless PostgreSQL `uuid` when persisted.
- persisted CommandId retains full nonzero uint64 via DUR-01 `numeric(20,0)`.
- ItemInstanceId is available for DUR-03 provenance.
- analytics/investigation cannot mutate gameplay, auto-sanction, balance, rollback or deploy.
- durable audit cannot silently downgrade to best effort.

## 3. Event source IDL choice

Options considered: bespoke binary, JSON, Avro, Protobuf, implementation-defined serializer.

Protobuf/proto3 is selected because it provides a versionable cross-language source schema without adding a second bespoke parser model. Reuse of Protobuf technology does not merge the event family with `protocol-oteryn`; the registries, payloads, revisions and transports remain separate.

Decision:

```text
family = oteryn-game-events
envelope revision = 1
serialization = protobuf binary
source IDL = proto3
broker/storage = deferred
application event compression = none
```

Important review refinement: Protobuf bytes are **not assumed globally canonical**. Exact committed event bytes must therefore remain stable across retry/redelivery; semantic equality is not defined as decode+reserialize.

## 4. Identifier decisions

### EventId

Strong UUIDv7, global one-event identity, producer-owned, non-nil, never reused. Same EventId means one immutable event. Best-effort observations dropped before event admission need no EventId; admitted events do.

### OperationId

Strong UUIDv7 for one independently durable logical multi-step/retry-capable operation. It is optional and not minted for every command. Same-operation retries retain it.

### TransactionId

Strong UUIDv7 for one logical atomic durable mutation transaction. Ambiguous commit/retry retains it. Physical DB attempt identity remains internal. A new TransactionId requires prior terminal outcome plus an intentionally new logical transaction.

### CorrelationId

Strong UUIDv7 for one trusted bounded correlation context. Grouping only; never authority/causality/order. Untrusted client trace strings do not become canonical CorrelationId.

### Causation

A separately generated CausationId is rejected as redundant/type-erasing. Canonical immediate causation is a typed reference to EventId, CommandRef, OperationId or TransactionId; roots may have no cause.

### AnalyticsActorId

Strong UUIDv7 scoped by analytics identity domain + nonzero identity epoch. It is purpose-scoped pseudonymization, never public/operational identity. Mapping to CharacterId/AccountId is separately protected and access-audited. Pseudonymous telemetry may drop if mapping is unavailable; it may not leak raw identity as fallback.

## 5. Durability classes

Only two game-event durability classes are needed:

### BEST_EFFORT_TELEMETRY

Bounded, asynchronous, optionally sampled/aggregated, explicit counted drops, gameplay fail-open on analytics dependency failure, no completeness/economy-integrity claim.

### DURABLE_AUDIT

Never sampled/dropped, mandatory mutation evidence atomic with owning mutation, publication only after commit, at-least-once delivery, immutable EventId/content across retry, consumer dedupe, read-only replay, committed backlog never dropped for RAM pressure.

Operational metrics/logs remain outside this classification.

## 6. Common envelope design

The common envelope contains stable event identity/type/schema/durability/privacy/retention/wall-time/build/payload context plus optional typed scope and correlation fields.

Generic actor/subject/object UUIDs and arbitrary metadata maps are rejected. They would erase semantic type, complicate privacy classification and create unbounded/cardinality hazards. Domain identities live in registered typed payloads.

CommandId appears only with GameSessionId. ChannelId/InstanceId preserve WorldId semantic scope. Secrets/credentials/proofs are prohibited.

## 7. Review repair: RuntimeExecutionOrdinal scope

Initial candidate placed RuntimeExecutionOrdinal alone in the envelope. That is materially ambiguous after GameNode/scope-owner replacement because FND-03 scopes the ordinal to `(semantic scope, scope ownership generation)`.

Repair cycle 1 changes the envelope to a typed:

```text
RuntimeOrderRef {
  scope_ownership_generation
  runtime_execution_ordinal
}
```

and requires a concrete `WorldId + ChannelId` or `WorldId + InstanceId` envelope scope.

Both values are nonzero. The reference is internal evidence, stripped from ordinary projections unless purpose explicitly requires it. It never creates global/cross-generation order.

## 8. Review repair: transaction event completeness

Initial candidate carried only `transaction_event_ordinal`. A consumer could not distinguish a completed one-event transaction from an incomplete multi-event transaction without knowing the expected count.

Repair cycle 1 requires `transaction_event_count` for registered atomic mutation evidence.

For one committed TransactionId:

```text
count >= 1
1 <= ordinal <= count
same count on every event
ordinals exactly 1..count
no duplicate ordinal
```

This detects incomplete/duplicate event sets without inventing global ordering.

## 9. Review repair: Protobuf byte stability

Protobuf serialization can have multiple valid byte encodings for equivalent decoded content. If a retry reconstructed and reserialized an event, “same EventId” could accidentally produce different bytes/hash.

Repair cycle 1 freezes this rule:

1. materialize exact registered payload bytes once;
2. compute SHA-256 over those exact bytes;
3. bind EventId/type/schema/exact bytes before the first possibly ambiguous durable commit/publication attempt;
4. same-EventId retry/redelivery reuses exact bytes, never reconstructs from mutable domain state;
5. durable storage/outbox implementation retains exact bytes or proves an equivalently byte-preserving representation;
6. raw serialized envelope byte equality is not required because envelope field ordering is not semantic.

The payload hash is integrity evidence, not event identity or semantic canonicalization.

## 10. Registry/evolution

Separate machine-readable event registry:

- type ID 0 invalid;
- positive uint32 IDs never reused;
- each type declares owner, payload schema/message, schema revision, durability, privacy floor, retention profile, atomic-mutation-evidence flag;
- schema revision nonzero/monotonic per type;
- removed protobuf fields reserved;
- compatible additive evolution only when older consumers remain safe;
- unsafe semantics require new type/family-major decision;
- durable unsupported schema quarantines/rejects without evidence loss/reinterpretation;
- best-effort unsupported schema may count/drop but never claim completeness.

The initial registry intentionally has no domain event IDs. Combat/item/social families belong to their owners.

## 11. Ordering model

No global event total order is introduced.

```text
CommandRef                      per-GameSession command order
RuntimeOrderRef                 scope+owner-generation-local execution order
TransactionId + ordinal/count   one atomic transaction event set/order
CausationRef                    immediate causal edge
CorrelationId                  grouping only
domain/state revisions          authoritative state progression
wall timestamp                  cross-system correlation only
EventId UUIDv7 order            storage locality only
```

Cross-transaction operation progression uses causation + domain revisions; no global operation ordinal.

## 12. Atomic audit/outbox semantic boundary

For a mutation requiring audit, before commit the TransactionId, EventIds, exact event bytes, expected event count/ordinals and immutable type/schema/scope/privacy/retention bindings are fixed.

Valid outcome:

```text
mutation + every mandatory audit record commit
OR
neither becomes authoritative
```

ANL-01 owns the invariant; DUR-02/03 own physical DB transaction/outbox proof.

After commit publication is at-least-once. Lost ack may redeliver exact same EventId/content. Consumer dedup is mandatory. Consumer checkpoint advances only after its derived projection is safely accepted. No broker-level exactly-once assumption.

## 13. Duplicate/out-of-order/replay

- identical same-EventId redelivery -> one consumer effect;
- same EventId conflicting immutable record -> hard conflict, no overwrite;
- out-of-order events -> bounded buffer/defer/quarantine/rebuild using transaction set, causation and domain revisions;
- replay only updates derived/read-only consumers/test fixtures, never authoritative gameplay or original CommandId execution.

## 14. Privacy classes

1. INTERNAL_NON_PERSONAL.
2. PSEUDONYMOUS_ANALYTICS.
3. RESTRICTED_PLAYER_LINKED.
4. SECURITY_SENSITIVE.

Privacy class is a minimum floor. Raw AccountId/CharacterId cannot appear in pseudonymous families. High-cardinality player/item/event/session IDs are prohibited as ordinary Prometheus labels.

## 15. Retention and production collection

ANL-01 intentionally does not guess jurisdiction/product-specific retention durations. Every concrete event family must bind an accepted retention profile before production collection. It must define purpose, privacy class, finite ordinary retention duration/ceiling, allowed roles, export/redaction, deletion/anonymization, legal-hold authorization/audit and policy revision/rollout.

Ordinary unlimited retention is prohibited. Legal hold is an explicit exception. Missing/unresolved policy blocks production collection/projection; privacy never fails open.

## 16. Error mapping

Narrow ANL codes map into existing Foundation categories rather than adding a new global category:

- telemetry capacity drop -> CAPACITY_EXCEEDED;
- audit dependency unavailable -> DEPENDENCY_UNAVAILABLE;
- malformed -> INVALID_INPUT;
- schema unsupported -> UNSUPPORTED_REVISION;
- EventId/order/replay conflicts -> CONFLICT;
- privacy-policy rejection -> CONFLICT;
- authenticated investigation access denial -> CONFLICT;
- evidence integrity failure -> INTERNAL_UNAVAILABLE.

Authentication failures remain AUTHENTICATION_FAILED.

## 17. Resource limits

ADR-0006 requires ANL-01 hard resource registration. The shared registry now bounds event/payload/string/nesting, best-effort queue entries/bytes, publish/quarantine/replay batches, replay windows, query pages/results and evidence-package bytes.

These are absolute security/allocation ceilings, not throughput promises or tuned defaults. Implementation may configure lower values and must use PERF/OPS evidence. Committed durable audit backlog is never dropped to satisfy an in-memory limit.

## 18. Failure scenario dispositions

- FS-ANALYTICS-TELEMETRY-OVERFLOW: PASS.
- FS-AUDIT-OUTBOX-BACKLOG: semantic PASS; physical backlog/recovery DUR-02.
- FS-EVENT-DUPLICATE-DELIVERY: PASS.
- FS-EVENT-OUT-OF-ORDER: PASS.
- FS-AUDIT-MUTATION-MISMATCH: semantic PASS; physical DUR-02/03.
- FS-ANALYTICS-PRIVACY-POLICY: PASS.
- FS-DB-OUTBOX-BOUNDARY: semantic PASS; physical DUR-02.
- FS-DETECTOR-FALSE-POSITIVE: deferred ANL-03.
- FS-INVESTIGATION-MUTATION-ATTEMPT: deferred ANL-04 implementation evidence.

Architecture PASS does not claim runtime evidence.

## 19. Required implementation evidence

Future conformance requires: protobuf golden/cross-language fixtures; decoder fuzz/property/negative corpora; resource-bound tests; UUID/scope/CommandRef negatives; exact byte preservation across ambiguous retry; EventId identical/conflict tests; RuntimeOrderRef generation/scope tests; transaction event count/ordinal complete-set tests; commit/publication crash tests; consumer checkpoint recovery; out-of-order handling; unsupported schema by durability class; telemetry overflow counters; durable backlog no-loss; pseudonymous raw-ID rejection; mapping access audit/domain+epoch isolation; retention collection gate; bounded replay/query/export; and proof replay/investigation cannot mutate gameplay.

## 20. Closed decisions

ANL-01 closes:

1. protobuf/proto3 event interchange, broker independent;
2. EventId/OperationId/TransactionId/CorrelationId/AnalyticsActorId ownership and UUIDv7 representation;
3. typed causation reference instead of new CausationId;
4. two game-event durability classes;
5. typed bounded envelope without arbitrary metadata;
6. exact-byte stability across retries despite noncanonical protobuf serialization;
7. runtime order paired with owner generation/scope;
8. transaction event count + ordinal completeness;
9. no global event order;
10. atomic mutation/audit + at-least-once publication + EventId dedupe/read-only replay;
11. privacy/pseudonym/retention production gate;
12. shared error/resource/failure integration.

No unresolved ANL-01 semantic decision blocks DUR-02/DUR-03 architecture consumption. Physical persistence/broker, exact retention durations, domain payload families and analytics products remain downstream.