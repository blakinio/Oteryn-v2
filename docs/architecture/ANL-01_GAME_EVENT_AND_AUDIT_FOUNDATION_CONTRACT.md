# ANL-01 — Game Event and Audit Foundation Contract

- Status: Candidate; canonical only when the owning ANL-01 delivery merges
- Date: 2026-08-10
- Gate: `ANL-01`
- Issue: #135
- Repository: `blakinio/Oteryn-v2`
- Trusted base: `main@ef42fa47ab054ab8aa304c017307c1945f931b59`
- Scope: event/audit semantics, interchange, privacy and evidence foundation only

## 1. Purpose and authority

This contract freezes the smallest complete Oteryn game-event/audit foundation required by ADR-0006 before DUR-02/DUR-03 may finalize transactional outbox and critical economy/security evidence.

It is not event sourcing. It does not replace authoritative game state, FND-02 command identity, FND-03 execution order, FND-04 session/lease authority, DUR-02 persistence or DUR-03 conservation invariants.

Canonical authority chain:

```text
authoritative gameplay mutation
  -> owning gameplay/FND/DUR contract

required evidence semantics
  -> ANL-01

physical transaction/outbox/checkpoint
  -> DUR-02

item/currency conservation and anti-duplication
  -> DUR-03

analytical/security consumers
  -> ANL-02/ANL-03

investigation/AI
  -> ANL-04, read-only
```

## 2. Event interchange profile v1

Canonical common event interchange uses:

```text
family:             oteryn-game-events
envelope revision:  1
serialization:      Protocol Buffers binary
source IDL:         proto3
source:             docs/contracts/game-events/v1/foundation.proto
registry:           docs/contracts/GAME_EVENT_FOUNDATION_REGISTRY.json
compression:        none at application event-interchange boundary
```

This profile is independent from `protocol-oteryn`; it shares schema technology, not protocol message identity or compatibility negotiation.

No broker, message bus, database table, warehouse, lake or dashboard product is selected.

## 3. Canonical identities

### 3.1 EventId

```text
EventId
representation: UUIDv7, full 128 bits
owner/issuer: authoritative event producer boundary
scope: global one-event identity
nil: invalid
reuse: never
```

One EventId always means one immutable event. Delivery retry, redelivery, consumer replay and projection rebuild reuse the same EventId.

Same EventId with different event type, schema revision, immutable envelope context or payload is an integrity conflict. Last-write-wins is prohibited.

Best-effort observations rejected/sampled before event admission need not mint EventId; their loss is represented by bounded counters. Once admitted as an event, EventId is present.

Durable audit EventId is fixed before/inside the authoritative transaction that commits the required audit record.

### 3.2 OperationId

```text
OperationId
representation: UUIDv7
owner/issuer: owner of the logical operation
scope: one independently durable multi-step/retry-capable logical operation
```

OperationId is optional and only exists when the operation needs durable independent correlation. It is not automatically created for every command.

Retries/reconciliation of the same logical operation retain OperationId. A new independent operation receives a new ID.

`CommandRef` and OperationId may coexist and are not aliases.

### 3.3 TransactionId

```text
TransactionId
representation: UUIDv7
owner/issuer: authoritative durable transaction coordinator/owner
scope: one logical atomic durable mutation transaction
```

TransactionId is stable while resolving an ambiguous commit/retry of the same logical transaction. Physical SQL/backend attempts do not receive new canonical TransactionIds merely because a retry occurs.

A new TransactionId requires proof that the prior transaction is terminal and the domain has intentionally begun a new logical transaction.

### 3.4 CorrelationId

```text
CorrelationId
representation: UUIDv7
owner/issuer: trusted Oteryn root/workflow boundary
scope: one bounded correlation context
```

CorrelationId is optional unless a family explicitly requires it. It provides grouping, never authorization, causality, order or transaction identity.

Untrusted external/client correlation text is not canonical CorrelationId authority. External tracing context is treated as separate bounded diagnostic input.

### 3.5 Canonical causation

ANL-01 **does not define a separately generated CausationId UUID**.

Canonical immediate causation is a typed `CausationRef`:

```text
Event(EventId)
Command(GameSessionId, CommandId)
Operation(OperationId)
Transaction(TransactionId)
```

A genuine root event has no CausationRef.

This supersedes any earlier conceptual field that implied causation required a new independent identifier. The cause's existing typed identity is the reference.

### 3.6 AnalyticsActorId

```text
AnalyticsActorId
representation: UUIDv7
owner/issuer: analytics privacy-identity authority
scope: analytics_identity_domain + identity_epoch + AnalyticsActorId
```

AnalyticsActorId is a pseudonymous analytical identity and is never AccountId/CharacterId/public identity.

Mandatory rules:

- no reversible/truncated formatting of AccountId, CharacterId, name or email;
- purpose/domain-scoped pseudonyms instead of one universal cross-purpose analytics identity;
- explicit non-zero identity epoch/policy revision;
- protected mapping to operational identity under least privilege;
- every privileged mapping lookup is audited;
- pseudonymous family cannot fall back to raw CharacterId when mapping is unavailable;
- raw operational identities needed by critical audit use `RESTRICTED_PLAYER_LINKED` or `SECURITY_SENSITIVE` instead.

Exact epoch duration is privacy-policy owned. Production requires a concrete accepted policy.

## 4. Physical durability representation

Where the above canonical UUIDv7 identities are stored in native game PostgreSQL, DUR-01 applies unchanged:

```text
PostgreSQL scalar = uuid
full 128 bits
strong semantic type preserved
nil invalid
no reuse
```

ANL-01 does not design tables or indexes.

FND-02 CommandId remains full non-zero uint64 scoped by GameSessionId; if persisted, DUR-01 `numeric(20,0)` applies.

## 5. Durability classes

### 5.1 BEST_EFFORT_TELEMETRY

Purpose: high-volume gameplay/world analytical facts where bounded loss is acceptable.

Rules:

- asynchronous bounded collection;
- may sample/aggregate/drop only under registered family policy;
- producer/runtime continues gameplay when analytics dependency is unavailable;
- accepted/dropped/retried/lag evidence is observable;
- data gaps are explicit and no completeness claim is allowed;
- never used as sole proof of item/currency conservation or security-authoritative state.

### 5.2 DURABLE_AUDIT

Purpose: critical economy/security/state-transition evidence requiring durable provenance.

Rules:

- never sampled or silently dropped;
- when evidence is mandatory for an authoritative mutation, mutation + audit/outbox record share one accepted atomic transaction boundary;
- publication occurs only after commit;
- publication is at-least-once;
- EventId and immutable content are stable across retries;
- every durable consumer deduplicates by EventId and verifies family invariants;
- replay cannot reapply gameplay mutation;
- committed backlog is never discarded to satisfy an in-memory limit.

A non-mutating security decision/rejection may be durable audit without TransactionId only if the registered family declares `atomic_mutation_evidence=false`.

Operational Prometheus/OpenTelemetry/logging remains separate and is not a third event durability class.

## 6. Envelope v1

Normative source is `docs/contracts/game-events/v1/foundation.proto`.

### 6.1 Required fields

Every admitted event requires:

- `envelope_revision = 1`;
- EventId;
- registered nonzero `event_type_id`;
- registered nonzero `event_schema_revision`;
- durability class;
- privacy class;
- non-empty accepted `retention_profile_id` for production use;
- trusted server `occurred_at_unix_ms` wall timestamp;
- bounded `server_build_id`;
- registered protobuf payload;
- exact 32-byte SHA-256 of the payload bytes.

### 6.2 Optional typed context

When semantically applicable:

- WorldId;
- ChannelId with WorldId;
- InstanceId with WorldId;
- NodeId;
- GameSessionId;
- connection_generation with GameSessionId;
- RuntimeExecutionOrdinal;
- CommandId with GameSessionId;
- OperationId;
- TransactionId;
- transaction_event_ordinal with TransactionId;
- CorrelationId;
- CausationRef;
- AnalyticsActorRef;
- protocol major;
- ruleset/content revisions.

### 6.3 Validation invariants

- UUID identity fields are exact 16-byte non-nil canonical values and UUIDv7 where their owning contract requires it;
- ChannelId/InstanceId do not erase WorldId scope;
- CommandId is nonzero and cannot appear without GameSessionId;
- connection_generation is nonzero and cannot appear without GameSessionId;
- transaction_event_ordinal cannot appear without TransactionId;
- revision strings and registry/policy keys are bounded canonical ASCII according to registry/resource limits;
- `payload_sha256 == SHA-256(payload)`;
- credentials, tickets, reconnect material, private keys, secrets and raw authorization proofs are forbidden in envelope/payload;
- no arbitrary free-form metadata map is provided by the foundation envelope.

`occurred_at_unix_ms` is correlation evidence, never causality/fencing/order authority.

## 7. Typed payload rule

Generic `actor_id`, `subject_id`, `object_id` or untyped UUID fields are not part of the common envelope.

Event families use explicit payload types such as CharacterId, ItemInstanceId, content keys and domain revisions under their owning contract. This prevents UUID type erasure and privacy policy from depending on undocumented metadata conventions.

Pseudonymous analytical families use AnalyticsActorRef where required. Restricted durable families may carry raw operational typed identity only under their declared privacy class/purpose.

## 8. Event type registry

`GAME_EVENT_FOUNDATION_REGISTRY.json` is the machine-readable allocation/evolution registry.

Rules:

1. `event_type_id = 0` invalid.
2. Event type IDs are positive uint32 and never reused.
3. Every concrete event type declares owner, payload schema/message, current schema revision, durability class, privacy floor, retention profile and whether it is atomic mutation evidence.
4. Every event type maintains a nonzero monotonic schema revision.
5. Removed protobuf field numbers/names are reserved.
6. Additive fields are allowed only when older compatible consumers can safely ignore them.
7. Semantics that cannot be safely interpreted by older consumers require a new event type or explicit reviewed family-major transition.
8. Producer may not emit an unregistered event type/schema as canonical production data.
9. Durable unknown/unsupported schema is quarantined/rejected without deletion/reinterpretation.
10. Best-effort unsupported schema may be counted/dropped and cannot be described as complete.
11. EventId immutable content never changes merely because registry revision advances.

The initial registry contains no gameplay-domain event IDs intentionally. Domain owners add them later.

## 9. Ordering model

ANL-01 defines **no global event total order**.

Use the correct existing order evidence:

```text
(GameSessionId, CommandId)           per-session command identity/order
RuntimeExecutionOrdinal              scope-owner/generation-local execution evidence
TransactionId + transaction ordinal one atomic transaction's emitted-event order
CausationRef                         immediate causal graph edge
CorrelationId                        grouping only
state/domain revisions               authoritative domain progression
wall timestamp                       cross-system correlation only
EventId UUIDv7 sorting               storage/locality only
```

### 9.1 transaction_event_ordinal

If one logical committed TransactionId emits N ordered durable events:

- ordinals are exactly `1..N`;
- unique and contiguous inside that transaction;
- immutable;
- never used as cross-transaction/global order.

Cross-transaction ordering uses causation and domain revisions. No generic globally coordinated operation ordinal is introduced.

## 10. Atomic mutation/audit boundary

For every operation whose owning contract requires durable audit:

### Prepare

- applicable TransactionId is fixed;
- required EventIds are fixed;
- audit event set and transaction ordinals are deterministically defined;
- event type/schema/privacy/retention/scope/payload bindings are fixed.

### Commit invariant

```text
(authoritative mutation + all mandatory durable audit records) commit
OR
(neither becomes authoritative)
```

Mutation committed with missing mandatory audit evidence is invalid and must not remain silent.

DUR-02/DUR-03 define the concrete transaction/isolation/outbox mechanics that prove this invariant.

## 11. Publication and delivery

Durable publication semantics are:

```text
committed record -> publish at least once -> idempotent consumer
```

Rules:

- unpublished records remain recoverable backlog;
- only committed records are publishable;
- lost publication acknowledgement may cause redelivery;
- EventId does not change across delivery attempts;
- transport/broker delivery ID is not canonical EventId;
- delivery replay never reissues the original gameplay CommandId;
- consumer applies at most one derived effect per EventId;
- consumer checkpoint advances only after the consumer's own projection effect is safely accepted;
- checkpoint storage/locking is implementation-owned;
- no architecture claim of broker-level exactly-once is made or required.

## 12. Duplicate/conflict semantics

### Identical redelivery

Same EventId + same immutable event content:

```text
idempotent duplicate
-> no second consumer projection/provenance effect
```

### Conflicting redelivery

Same EventId + different immutable content:

```text
ANL_EVENT_ID_CONFLICT / CONFLICT
-> never overwrite or merge silently
-> affected path quarantines/fails safe
-> integrity evidence retained
```

Content equality includes event type, schema revision, required immutable envelope bindings and payload SHA-256/bytes. Hash comparison is an optimization/evidence; collision-sensitive semantic validation must not rely solely on a truncated hash.

## 13. Out-of-order and replay

Related events arriving outside expected transaction/causal/domain revision order are handled by registered consumer policy:

- buffer within registered limits;
- defer awaiting predecessor;
- quarantine/reject if reconciliation cannot prove safety;
- rebuild from a known checkpoint/snapshot when consumer supports it.

Consumers never fabricate missing authoritative state.

Replay is permitted only for read-only/derived consumers and deterministic test fixtures. Replaying an EventId never invokes gameplay mutation or original credentials/commands.

## 14. Privacy classes

### INTERNAL_NON_PERSONAL

Internal non-player-linked service/content facts. No direct or pseudonymous player identity required.

### PSEUDONYMOUS_ANALYTICS

Ordinary gameplay/world analytical data linked through approved AnalyticsActorId. Raw AccountId/CharacterId is forbidden by family contract unless the class is raised.

### RESTRICTED_PLAYER_LINKED

Operational player/session/item-linked evidence required for durable audit, administration or authorized investigation. Least privilege and access audit required.

### SECURITY_SENSITIVE

Security/recovery/abuse evidence whose disclosure materially increases privacy or attack risk. Strongest role separation, export/redaction and access audit requirements.

A transformation may raise privacy protection; it cannot silently downgrade below the source family/privacy obligations.

## 15. Retention and production collection gate

Every concrete event family must bind a `retention_profile_id` before production collection.

The referenced accepted profile must define:

- explicit purpose;
- privacy class;
- finite ordinary retention duration or ceiling;
- allowed roles/consumers;
- aggregation/anonymization transition if used;
- deletion/anonymization behavior;
- export/redaction behavior;
- legal-hold authorization/audit behavior;
- profile revision and rollout/rollback.

`UNBOUNDED` ordinary retention is prohibited. Legal hold is an explicitly authorized exception, not a default profile.

If purpose/privacy/retention/access cannot be resolved to an accepted current profile, production collection/projection for that family is rejected. Privacy does not fail open merely because telemetry is best-effort.

ANL-01 does not freeze jurisdiction-specific duration numbers. Product/privacy policy must provide them before activation.

## 16. Pseudonym mapping boundary

The mapping from AnalyticsActorId to operational identity:

- is not stored in ordinary analytics datasets;
- is not available to all balance analysts/operators by default;
- uses least-privilege authorized lookup;
- audits requester/purpose/time/affected mapping reference;
- never grants gameplay authority;
- may be destroyed/rotated/anonymized according to accepted retention/deletion policy;
- does not allow an old identity epoch to be silently reused as the new epoch.

If pseudonym resolution is unavailable for a `PSEUDONYMOUS_ANALYTICS` best-effort family, policy may count/drop the event. It may not replace the pseudonym with raw identity.

## 17. Observability/cardinality boundary

Prometheus/OpenTelemetry operational metrics do not use AccountId, CharacterId, AnalyticsActorId, ItemInstanceId, TransactionId, EventId, GameSessionId or similar high-cardinality identity as ordinary labels.

Operational logs may contain bounded redacted correlation references only under their logging policy. Secrets and raw event payloads are never logged merely to debug an event failure.

## 18. Error contract

ANL-01 adds narrower codes mapped to existing Foundation Error Vocabulary categories:

| Code | Foundation category | Retry/mutation meaning |
|---|---|---|
| `ANL_TELEMETRY_CAPACITY_DROPPED` | `CAPACITY_EXCEEDED` | best-effort counted loss; gameplay unchanged |
| `ANL_AUDIT_DEPENDENCY_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | no downgrade; owning durable operation follows DUR policy |
| `ANL_EVENT_MALFORMED` | `INVALID_INPUT` | no consumer effect |
| `ANL_EVENT_SCHEMA_UNSUPPORTED` | `UNSUPPORTED_REVISION` | no reinterpretation/downgrade |
| `ANL_EVENT_ID_CONFLICT` | `CONFLICT` | no overwrite/merge |
| `ANL_EVENT_ORDER_BLOCKED` | `CONFLICT` | buffer/defer/quarantine within bounds |
| `ANL_REPLAY_CONFLICT` | `CONFLICT` | affected replay/projection stops; gameplay unchanged |
| `ANL_PRIVACY_POLICY_REJECTED` | `INVALID_INPUT`/`CONFLICT` as boundary-specific mapping | no collection/disclosure |
| `ANL_INVESTIGATION_ACCESS_DENIED` | `AUTHENTICATION_FAILED`/`CONFLICT` as authn/authz-specific mapping | no evidence disclosure |
| `ANL_EVIDENCE_INTEGRITY_FAILURE` | `INTERNAL_UNAVAILABLE` | fail safe; preserve bounded evidence |

Concrete public messages are redacted and do not contain private payloads/credentials.

## 19. Resource limits

The shared `RESOURCE_LIMITS_REGISTRY.json` carries the normative ANL-01 hard ceilings.

Principles:

- ceilings are security/allocation boundaries, not capacity guarantees or recommended tuned defaults;
- implementation/OPS may configure lower values;
- peer/event controlled sizes are checked before allocation/decode/work amplification;
- no application-level event compression in v1;
- arbitrary metadata maps are absent;
- committed durable backlog is not dropped to enforce in-memory limits;
- large replay/export work is paged/batched under limits.

## 20. Foundation failure scenarios

| Scenario | Status | ANL-01 invariant |
|---|---|---|
| `FS-ANALYTICS-TELEMETRY-OVERFLOW` | `PASS` | bounded best-effort queue, counted loss, no completeness claim/gameplay change |
| `FS-AUDIT-OUTBOX-BACKLOG` | `PASS` semantic / DUR-02 physical | committed evidence not silently dropped; retryable publication |
| `FS-EVENT-DUPLICATE-DELIVERY` | `PASS` | EventId dedupe; no gameplay replay |
| `FS-EVENT-OUT-OF-ORDER` | `PASS` | transaction ordinal/causation/domain revisions; no invented state |
| `FS-AUDIT-MUTATION-MISMATCH` | `PASS` semantic / DUR-02+DUR-03 physical | mandatory mutation+audit atomicity |
| `FS-ANALYTICS-PRIVACY-POLICY` | `PASS` | missing purpose/privacy/retention/access blocks production collection |
| `FS-DETECTOR-FALSE-POSITIVE` | `DEFERRED_BY_ACCEPTED_GATE` | ANL-03; ADR-0006 still forbids automatic sanction |
| `FS-INVESTIGATION-MUTATION-ATTEMPT` | `DEFERRED_BY_ACCEPTED_GATE` | ANL-04 must prove read-only least privilege |
| `FS-DB-OUTBOX-BOUNDARY` | `PASS` semantic / DUR-02 physical | no valid mutation commit without mandatory audit record |

Architecture PASS is not implementation evidence.

## 21. Required implementation evidence

A later implementation may claim ANL-01 conformance only after deterministic evidence covers:

- protobuf envelope/payload golden fixtures and cross-language round-trip;
- malformed/oversized/nesting/resource limit negative corpus;
- fuzz/property tests for cross-component decoders;
- UUID type/version/nil/scoped-identity negatives;
- CommandId/GameSession scoping;
- payload SHA-256 validation;
- EventId duplicate identical and conflict paths;
- transaction_event_ordinal contiguity and duplicate/gap rejection;
- crash before/after durable commit and publication acknowledgement;
- at-least-once redelivery with one consumer effect;
- consumer checkpoint crash recovery;
- out-of-order causal/transaction/domain revision handling;
- unsupported schema behavior per durability class;
- best-effort overflow/drop counters;
- durable backlog without evidence loss;
- privacy fixture proving raw identities cannot enter pseudonymous families;
- pseudonym domain/epoch isolation and privileged mapping access audit;
- unresolved/expired retention-policy binding blocks production collection;
- bounded query/replay/export/evidence package handling;
- no authoritative gameplay mutation from replay/investigation paths.

Physical PostgreSQL atomicity tests are DUR-02/DUR-03 implementation evidence and become mandatory when those layers are authorized.

## 22. Downstream gates

After ANL-01 acceptance/lifecycle closeout:

- DUR-02 may finalize PostgreSQL transaction/outbox/checkpoint schema using ANL-01 EventId/TransactionId/publication/privacy semantics;
- DUR-03 may define item/currency critical event families and prove anti-duplication plus atomic evidence;
- ANL-02 may define gameplay/balance/world metrics on registered event families;
- ANL-03 may define economy/security detectors/cases without becoming enforcement authority;
- ANL-04 may implement least-privilege read-only investigation only after its own contract;
- no production analytics collection is authorized merely by ANL-01 acceptance.

## 23. Non-goals

This contract does not authorize or select:

- database table/index/partition/outbox/checkpoint schema;
- isolation/locking/retry/RPO/RTO;
- Kafka/NATS/Pulsar/Redpanda/RabbitMQ or other broker;
- ClickHouse/warehouse/data lake/object store/Grafana topology;
- runtime collector implementation;
- exact product/jurisdiction retention durations;
- gameplay event payload families beyond foundation registry rules;
- detector/model thresholds;
- automated bans/sanctions;
- AI mutation rights;
- Platform writes;
- deployment/traffic/production collection.

## 24. Acceptance rule

ANL-01 becomes accepted only when:

- analysis/contract/IDL/registry/resource-limit package is internally consistent with accepted ADR-0006/FND/DUR-01;
- exact-head repository governance/CI pass;
- architecture/security/privacy/data-integrity review has zero material findings;
- zero unresolved material review threads remain;
- accepted head is squash-merged unchanged;
- a separate lifecycle closeout archives/releases ownership and closes Issue #135.
