# ANL-01 — Game Event and Audit Foundation Analysis

- Status: bounded decision analysis for Issue #135
- Date: 2026-08-10
- Trusted base: `main@ef42fa47ab054ab8aa304c017307c1945f931b59`
- Gate: `ANL-01`
- Does not authorize: runtime, PostgreSQL schema, broker, warehouse, detector, Platform or production implementation

## 1. Purpose

ADR-0006 already accepts Oteryn Game Intelligence and the separation between operational observability, best-effort gameplay telemetry and durable economy/security audit. ANL-01 must now turn that direction into a precise event/audit contract that DUR-02 and DUR-03 can consume without guessing identity, causation, atomic publication, privacy or schema-evolution semantics.

The canonical ownership split is:

```text
runtime/gameplay authority            -> FND-03 + gameplay owners
session/command authority             -> FND-02/FND-04
durable ID representation             -> DUR-01
persistence transaction/schema        -> DUR-02
item/currency conservation            -> DUR-03
event/audit semantics                 -> ANL-01
balance/world consumers               -> ANL-02
economy/security detectors            -> ANL-03
read-only investigation/AI            -> ANL-04
```

ANL-01 is therefore an evidence contract, not event sourcing and not a second gameplay authority.

## 2. Accepted inputs

### 2.1 ADR-0006

The following are already accepted and cannot be weakened:

- operational observability is low-cardinality and separate from player/item-linked event data;
- best-effort gameplay telemetry uses bounded asynchronous collection and may fail open with counted loss;
- durable item/currency/security mutation evidence cannot silently downgrade to best effort;
- authoritative mutation and required audit evidence must share one accepted atomic transaction boundary;
- consumer replay never replays gameplay mutation;
- analytics/investigation remain read-only and cannot autonomously sanction, mutate, balance, rollback or deploy;
- ordinary analytics uses pseudonymous actor identity and role-separated access;
- production collection requires accepted purpose, privacy, retention and access policy.

### 2.2 FND-02/FND-03/FND-04

- `CommandRef = (GameSessionId, CommandId)` remains the command identity and order; ANL-01 does not mint a competing command UUID.
- `RuntimeExecutionOrdinal` is owner/generation-local execution evidence and is not EventId/OperationId/TransactionId.
- `connection_generation`, scope ownership generation and revision values remain fences/order values, not event identities.
- private runtime ownership generations are not promoted into ordinary analytics dimensions.

### 2.3 DUR-01

- canonical UUIDv7-backed durable identities persist losslessly as PostgreSQL `uuid` when persistence is implemented;
- `ItemInstanceId` is available for later DUR-03 provenance;
- full-range persisted CommandId remains `numeric(20,0)` under GameSession scope;
- `EventId`, `OperationId`, `TransactionId`, `CorrelationId`, causation semantics and `AnalyticsActorId` are intentionally ANL-01-owned.

## 3. Event source IDL and serialization

### Options

1. bespoke binary event format;
2. JSON as canonical event serialization;
3. Apache Avro;
4. Protocol Buffers;
5. leave serialization entirely implementation-defined.

### Decision analysis

A common event foundation must be independently testable across Rust, persistence publication and future analytical consumers. Leaving serializer output implementation-defined would make payload fingerprints, schema compatibility and cross-language fixtures ambiguous. JSON is useful for debugging but wastes space and has canonicalization hazards. A new bespoke binary format adds unnecessary parser/evolution risk. Avro is credible but would introduce another schema model without a demonstrated requirement.

The repository already accepts Protocol Buffers/proto3 for the native protocol and has compatible cross-language/evolution practices. Reuse of the schema technology does not couple the event stream to the gameplay wire protocol: the two have separate registries, revisions and compatibility contracts.

### Decision

ANL-01 v1 uses **Protocol Buffers binary with proto3 source IDL** for the common event envelope and registered event-family payload schemas.

The broker/transport/storage backend remains undecided. Event protobuf bytes are an interchange representation, not gameplay authority and not a database table layout.

Application-level compression is prohibited at the v1 event interchange boundary. Infrastructure/storage compression may exist only behind independently bounded decompression/resource controls and cannot change event identity.

## 4. Identity catalogue

### 4.1 EventId

```text
EventId = strongly typed UUIDv7, full 128 bits
owner/issuer = authoritative event producer boundary
scope = global event identity
reuse = never
nil = invalid
```

One EventId denotes one immutable semantic event record. Redelivery/replay reuses the same EventId. The same EventId with different event type, schema revision, immutable envelope bindings or payload is a conflict, never a newer version of the event.

For best-effort telemetry, EventId is required once an event is admitted into the event-emission pipeline. A sampled/dropped observation that is rejected before event construction is represented by bounded drop counters rather than a phantom EventId.

For durable audit, EventId is allocated before/inside the owning authoritative transaction so the same committed audit record is redelivered under the same identity.

### 4.2 OperationId

```text
OperationId = strongly typed UUIDv7
owner/issuer = authoritative owner of the logical game/business operation
scope = one logical multi-step/retry-capable operation
reuse = same operation retries/reconciliation only
```

OperationId exists only when an operation needs independent durable correlation across events and/or transactions. It is not generated for every command merely because a command occurred.

A command-origin operation may carry both `CommandRef` and `OperationId`; they are not aliases. One logical operation may span multiple durable transactions. A new independent operation receives a new OperationId.

### 4.3 TransactionId

```text
TransactionId = strongly typed UUIDv7
owner/issuer = authoritative durable transaction coordinator/owner
scope = one logical atomic durable mutation transaction
reuse = reconciliation/retry of the same possibly-committed logical transaction
```

TransactionId identifies the logical atomic mutation unit, not a connection, SQL backend PID, database retry attempt or outbox row.

If commit outcome is ambiguous, retry/reconciliation retains the same TransactionId until the outcome is proven. A new TransactionId is allowed only after the prior transaction is proven terminal and the owning domain intentionally starts a new logical transaction.

Physical DB attempt IDs remain implementation-local metadata.

### 4.4 CorrelationId

```text
CorrelationId = strongly typed UUIDv7
owner/issuer = trusted Oteryn root/workflow boundary
scope = one bounded correlation context that may span events/operations/transactions
reuse = only within that correlation context
```

CorrelationId is optional unless an event family requires a cross-event workflow correlation. It is not authorization, order or transaction identity.

Untrusted client-provided trace/correlation text cannot become the canonical CorrelationId by assertion. External trace context may be recorded separately under bounded/redacted diagnostics; canonical CorrelationId is generated or explicitly accepted by a trusted boundary.

### 4.5 CausationRef, not a separately minted CausationId

A standalone newly generated `CausationId` would add an identity that points to nothing. ANL-01 therefore resolves the earlier conceptual `causation_id` field into a typed immediate **CausationRef**:

```text
CausationRef =
    Event(EventId)
  | Command(GameSessionId, CommandId)
  | Operation(OperationId)
  | Transaction(TransactionId)
  | absent for a genuine root event
```

The referenced identity is the cause. ANL-01 does not mint an additional causation UUID.

This preserves causal graphs without losing semantic type. A timer/system root that has no independently durable identity remains a root unless its owning domain creates an OperationId or later accepted durable occurrence identity.

### 4.6 AnalyticsActorId

```text
AnalyticsActorId = strongly typed UUIDv7
owner/issuer = analytics privacy-identity authority
canonical scope = (analytics_identity_domain, identity_epoch, AnalyticsActorId)
reuse = never for another source actor in the same domain/epoch
```

AnalyticsActorId is a pseudonymous analytical identity, not CharacterId/AccountId and not public identity.

Rules:

- it is never derived by reversible formatting/truncation of CharacterId, AccountId, name or email;
- ordinary analytical datasets use a purpose-scoped analytics identity domain rather than one universal cross-purpose pseudonym;
- `identity_epoch` is an explicit policy revision/epoch so privacy owners can limit long-term linkability;
- mapping to operational CharacterId/AccountId is restricted, separately stored/protected and access-audited;
- loss/unavailability of the pseudonym mapping may cause best-effort pseudonymous telemetry to be counted/dropped but may not cause the producer to leak CharacterId into a pseudonymous family;
- durable audit that requires raw operational identity uses an explicitly restricted privacy class instead of pretending the raw identifier is pseudonymous.

Exact epoch duration is privacy-policy owned and is not guessed by ANL-01. Production use requires a concrete accepted epoch policy.

## 5. Durability classes

ANL-01 defines two event durability classes. Operational metrics/logs are not a third game-event durability class; they remain operational observability.

### BEST_EFFORT_TELEMETRY

- analytical value only;
- bounded queue and batch limits;
- may be sampled, aggregated or dropped according to registered family policy;
- gameplay continues if analytics sink/consumer is unavailable;
- loss is counted and surfaced;
- no completeness claim for economy/security conservation;
- consumer replay/dedupe is useful but cannot upgrade incomplete telemetry into authoritative audit evidence.

### DURABLE_AUDIT

- required security/economy/state-transition evidence where the owning DUR/domain contract marks audit as mandatory;
- never sampled or silently dropped;
- for an authoritative mutation requiring audit, mutation + audit record commit atomically under DUR-02/DUR-03 transaction semantics;
- publication is retryable after commit and is at-least-once;
- EventId remains stable across publication attempts;
- consumer deduplication is mandatory;
- replay replays evidence into a consumer/projection, never the gameplay mutation;
- backlog cannot be discarded to satisfy an in-memory queue limit.

A durable security observation that records a non-mutating rejected action may be DURABLE_AUDIT without a TransactionId if its family explicitly declares `atomic_mutation_evidence=false`.

## 6. Common envelope shape

The envelope must be small and typed. Generic `actor_id`, `subject_id` and arbitrary metadata maps are rejected because they erase identity semantics and create privacy/cardinality ambiguity. Domain actor/subject identities belong to registered typed payloads, while common scope/correlation fields live in the envelope.

Common v1 fields are conceptually:

```text
envelope_revision
event_id
event_type_id
event_schema_revision
durability_class
privacy_class
retention_profile_id
occurred_at_unix_ms
world_id?
channel_id?
instance_id?
node_id?
game_session_id?
connection_generation?
runtime_execution_ordinal?
command_id?
operation_id?
transaction_id?
transaction_event_ordinal?
correlation_id?
causation_ref?
analytics_actor_ref?
protocol_major?
ruleset_revision?
content_revision?
server_build_id
payload
payload_sha256
```

Validation constraints:

- UUID fields are exact 16-byte non-nil values and require UUIDv7 where their owner contract does;
- ChannelId/InstanceId never erase WorldId semantic scope;
- CommandId requires GameSessionId and retains full nonzero uint64 semantics;
- connection_generation requires GameSessionId and is evidence/fence context, not event order;
- RuntimeExecutionOrdinal is meaningful only with its registered owner-scope context and never creates a global order;
- transaction_event_ordinal is valid only when TransactionId is present;
- revisions are bounded canonical strings where existing owners define them as strings; protocol major is numeric;
- no raw credentials/tickets/reconnect proofs/private keys are permitted in envelope or payload.

`occurred_at_unix_ms` is cross-system wall-clock correlation only. It does not define causal/transaction order.

`payload_sha256` is SHA-256 over the exact registered protobuf payload bytes. It is integrity/conflict evidence, not event identity and never substitutes for semantic validation.

## 7. Event type registry and schema evolution

ANL-01 creates a machine-readable event registry separate from the gameplay protocol registry.

Rules:

- `event_type_id = 0` invalid;
- IDs are positive uint32, globally unique within the Oteryn event family and never reused;
- every event type has a stable canonical name, owner gate/domain, durability class, privacy class requirements, retention-profile requirement and payload schema path/message;
- one event type has its own monotonic nonzero `event_schema_revision`;
- field numbers/names removed from protobuf schemas are reserved and not reused;
- additive compatible fields may advance schema revision when older consumers can safely ignore them;
- semantic changes that make old consumers unsafe require a new event type ID or explicit compatibility-major family decision;
- unknown event type/schema never activates gameplay behavior;
- durable audit with an unsupported/unregistered schema is quarantined/fails its consumer path and remains recoverable; it is never silently discarded;
- best-effort unsupported telemetry may be counted/dropped according to policy and cannot be reported as complete;
- one EventId cannot change schema revision or payload after commit/emission.

The initial ANL-01 registry intentionally contains no gameplay-domain event type IDs. Combat/item/social payload families are registered by their owning gates. ANL-01 freezes the allocation/evolution rules rather than guessing domain schemas early.

## 8. Ordering, transaction event ordinal and causality

There is no global event total order.

Canonical evidence is layered:

```text
CommandRef                        -> per GameSession command order
RuntimeExecutionOrdinal           -> owner/generation-local runtime input order
TransactionId + event ordinal     -> one durable atomic transaction's event order
CausationRef                      -> immediate causal edge
CorrelationId                     -> grouping only
state/domain revisions            -> authoritative domain state progression
EventId UUIDv7 order              -> never semantic order
wall timestamp                    -> correlation only
```

For a transaction that emits more than one durable event, `transaction_event_ordinal`:

- starts at 1;
- is unique and contiguous within the committed TransactionId event set;
- is immutable after commit;
- never becomes a cross-transaction order.

Cross-transaction operation ordering must use causation and the owning domain/state revision semantics. ANL-01 deliberately does not invent a globally synchronized OperationEventOrdinal.

## 9. Durable audit/outbox semantic boundary

ANL-01 and DUR-02 share the following semantic contract without selecting a table or broker:

### Before commit

- durable EventId and applicable TransactionId are fixed;
- required audit event set is deterministically derived from the intended authoritative mutation;
- each event has immutable type/schema/scope/privacy/retention bindings;
- the mutation and required durable audit/outbox records participate in one atomic commit boundary.

### Commit

Either:

```text
authoritative mutation + required audit records commit
```

or neither becomes authoritative.

A state in which mutation commits but mandatory audit evidence is silently absent is invalid.

### Publication

- occurs only for committed records;
- is at-least-once, not claimed exactly-once;
- retries reuse EventId and immutable content;
- publication transport attempt IDs are not EventId;
- a crash/lost response may cause redelivery, never gameplay re-execution;
- a consumer advances its checkpoint only after its own idempotent projection effect is safely accepted under that consumer's store semantics;
- exact checkpoint storage, locks and retry implementation belong to DUR-02/consumer implementation.

### Conflict

Same EventId + different immutable content is `ANL_EVENT_ID_CONFLICT` and must never be resolved by last-write-wins.

## 10. Consumer idempotency and replay

Every durable consumer uses EventId as the primary delivery dedupe identity plus any domain-specific invariant checks.

Rules:

- duplicate identical EventId produces at most one consumer projection/provenance effect;
- duplicate conflicting EventId is a hard conflict/integrity alert;
- replay from immutable events is read-only with respect to authoritative gameplay state;
- replay never submits original CommandId as a new gameplay command;
- consumer rebuild may replace a derived projection only under its own explicit rebuild checkpoint/version, never mutate canonical game state;
- out-of-order related events are buffered, deferred, rejected or reconciled using transaction ordinals/causation/domain revisions; consumers never invent missing authoritative state;
- dead-letter/quarantine is evidence requiring bounded operator handling, not silent disposal of durable audit.

## 11. Privacy classes

ANL-01 defines four privacy classes:

1. `INTERNAL_NON_PERSONAL` — no player-linked operational identity; internal service/content facts only.
2. `PSEUDONYMOUS_ANALYTICS` — ordinary analytical data using AnalyticsActorId or similarly approved pseudonymous dimensions; no raw AccountId/CharacterId by family contract.
3. `RESTRICTED_PLAYER_LINKED` — operational CharacterId/AccountId/session/item-linked evidence required for authoritative audit/admin investigation; least-privilege access and access audit required.
4. `SECURITY_SENSITIVE` — security/abuse/recovery evidence whose disclosure materially increases attack or privacy risk; strongest role separation, export/redaction and access auditing.

Privacy class is a minimum protection floor. A consumer cannot downgrade an event to a less restrictive class because it stores fewer fields.

## 12. Retention profiles and collection gate

ANL-01 does not guess jurisdiction/product-specific retention durations. Instead every registered event family must bind a non-empty `retention_profile_id` that resolves, before production collection, to an accepted policy containing at minimum:

- documented purpose;
- applicable privacy class;
- finite ordinary retention duration/ceiling;
- aggregation/anonymization transition, if any;
- permitted roles/consumers;
- export/redaction rules;
- deletion/anonymization behavior;
- legal-hold override semantics with authorization/audit;
- policy revision and rollout/rollback behavior.

`UNBOUNDED` is not a valid ordinary retention duration. Legal hold is an explicit exceptional state and cannot silently become the default retention policy.

If an event family has no current accepted purpose/privacy/retention/access policy, **production collection for that family is disabled/fails closed**. Best-effort telemetry does not get an implicit privacy fail-open exception.

## 13. Identity projection and access

Canonical restricted audit may retain operational typed IDs when required by the owning evidence contract. Ordinary analytics projection must minimize them.

Rules:

- no AccountId, CharacterId, ItemInstanceId, TransactionId, GameSessionId or other high-cardinality player-linked ID as ordinary Prometheus labels;
- PSEUDONYMOUS_ANALYTICS families may not smuggle raw IDs into free-form strings/metadata;
- mapping AnalyticsActorId -> operational identity is separated from ordinary analytical storage and every privileged lookup is audited;
- balance analysts do not automatically receive the mapping;
- security investigators receive only purpose-authorized views/evidence;
- investigation/AI credentials are read-only and cannot mutate authoritative game DB/runtime;
- exports apply the event family's privacy and retention policy and are bounded by registered resource limits.

## 14. Failure/error model

ANL-01 uses existing Foundation categories and adds stable contract-owned codes without extending the top-level category vocabulary.

Minimum codes:

| Code | Category | Disposition |
|---|---|---|
| `ANL_TELEMETRY_CAPACITY_DROPPED` | `CAPACITY_EXCEEDED` | best-effort only; counted drop, no gameplay mutation change |
| `ANL_AUDIT_DEPENDENCY_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | durable path cannot silently downgrade; owning mutation follows DUR policy |
| `ANL_EVENT_MALFORMED` | `INVALID_INPUT` | reject event, no consumer effect |
| `ANL_EVENT_SCHEMA_UNSUPPORTED` | `UNSUPPORTED_REVISION` | no reinterpretation/downgrade |
| `ANL_EVENT_ID_CONFLICT` | `CONFLICT` | preserve existing event/evidence; no overwrite |
| `ANL_EVENT_ORDER_BLOCKED` | `CONFLICT` | buffer/defer/quarantine; never invent state |
| `ANL_REPLAY_CONFLICT` | `CONFLICT` | stop affected replay/projection partition; no game mutation |
| `ANL_PRIVACY_POLICY_REJECTED` | `INVALID_INPUT` or `CONFLICT` by caller context | production collection/projection denied |
| `ANL_INVESTIGATION_ACCESS_DENIED` | `AUTHENTICATION_FAILED` or `CONFLICT` by authz boundary | no evidence disclosure |
| `ANL_EVIDENCE_INTEGRITY_FAILURE` | `INTERNAL_UNAVAILABLE` | fail safe, preserve bounded evidence, operator investigation |

Public diagnostics redact restricted IDs/payloads and never contain credentials.

## 15. Required resource boundaries

ANL-01 must register hard maxima that prevent event/analytics inputs from becoming unbounded allocation/amplification surfaces. These are security ceilings, not throughput promises or tuned defaults.

The initial profile uses bounded event bytes, payload bytes, in-process best-effort queue entries/bytes, publication/replay batch counts/bytes, query page/result bytes and export/evidence-package bytes. Configurations may be lower after PERF/OPS evidence; they may not exceed the absolute hard maxima without a reviewed contract revision.

Durable backlog is not capped by dropping committed evidence. Storage/backlog operational thresholds and recovery policy are DUR-02/OPS-owned.

## 16. Foundation failure scenarios

| Scenario | ANL-01 disposition |
|---|---|
| `FS-ANALYTICS-TELEMETRY-OVERFLOW` | `PASS` — bounded best-effort queue; counted loss; no completeness claim. |
| `FS-AUDIT-OUTBOX-BACKLOG` | `PASS` at semantic level — committed durable evidence is never silently dropped; publication is retryable; physical backlog/storage recovery is DUR-02-owned. |
| `FS-EVENT-DUPLICATE-DELIVERY` | `PASS` — EventId idempotency; duplicate delivery never replays gameplay. |
| `FS-EVENT-OUT-OF-ORDER` | `PASS` — transaction ordinal/causation/domain revisions; deterministic buffer/defer/reject/reconcile, no invented state. |
| `FS-AUDIT-MUTATION-MISMATCH` | `PASS` at semantic boundary — mandatory mutation+audit atomicity is required; physical proof belongs DUR-02/DUR-03. |
| `FS-ANALYTICS-PRIVACY-POLICY` | `PASS` — no accepted purpose/privacy/retention/access profile means no production collection for that family. |
| `FS-DETECTOR-FALSE-POSITIVE` | `DEFERRED_BY_ACCEPTED_GATE` — ANL-03 detector/case behavior; ADR-0006 already forbids automatic sanction. |
| `FS-INVESTIGATION-MUTATION-ATTEMPT` | `DEFERRED_BY_ACCEPTED_GATE` — ANL-04 implementation must prove least-privilege read-only enforcement; ANL-01 data boundary grants no write authority. |
| `FS-DB-OUTBOX-BOUNDARY` | `PASS` at semantic boundary / physical evidence deferred to DUR-02 — commit cannot validly contain mutation without required audit record. |

No architecture `PASS` claims implementation evidence exists.

## 17. Required implementation/conformance evidence

Before an implementation claims ANL-01 conformance it must prove at least:

1. protobuf golden round-trip for envelope v1 and each registered payload revision;
2. malformed/oversized/unknown-field/nesting/resource-limit rejection;
3. UUIDv7/non-nil/strong-type validation and CommandRef scoping;
4. EventId duplicate-identical idempotency and duplicate-conflict rejection;
5. transaction event ordinal contiguity/uniqueness and no cross-transaction order inference;
6. crash/lost-response publication redelivery without gameplay replay;
7. consumer checkpoint crash tests around projection commit;
8. out-of-order causal/transaction event tests;
9. unsupported schema quarantine/drop behavior by durability class;
10. best-effort queue overflow with exact drop counters and no gameplay effect;
11. durable backlog without silent audit loss;
12. privacy-family fixtures proving raw IDs cannot enter pseudonymous families;
13. pseudonym mapping access audit and identity-domain/epoch separation;
14. missing/expired/unbound retention policy prevents production collection;
15. bounded query/export/evidence package tests;
16. read-only replay/investigation credentials cannot mutate authoritative runtime/database when ANL-04 is implemented.

Property/fuzz tests are required for envelope/payload decoders where untrusted or cross-component bytes are decoded.

## 18. Closed decisions

ANL-01 closes the following architecture questions:

1. Oteryn game-event source IDL: protobuf/proto3, transport/broker independent.
2. Durable identity catalogue: EventId, OperationId, TransactionId, CorrelationId and AnalyticsActorId are strong UUIDv7 identities under explicit owners; causation is a typed reference, not a new UUID.
3. Durability: BEST_EFFORT_TELEMETRY versus DURABLE_AUDIT only; operational observability stays separate.
4. Envelope: typed bounded common v1 context, no generic actor/subject ID or arbitrary metadata map.
5. Ordering: no global event order; transaction-local ordinal + causation + existing command/runtime/domain revisions.
6. Durable publication: atomic mutation/audit commit, at-least-once publication, EventId dedupe, read-only replay.
7. Privacy: purpose-scoped pseudonymous actor IDs, restricted raw audit, no silent privacy downgrade.
8. Retention: every family requires a concrete finite accepted profile before production collection; no default unlimited retention.
9. Failure handling: stable ANL codes mapped to existing Foundation categories.
10. Resource safety: absolute security ceilings registered without claiming tuned throughput.

No remaining ANL-01 semantic uncertainty blocks DUR-02/DUR-03 architecture consumption. Physical PostgreSQL/broker/storage topology, exact retention durations, domain payload families and analytics products remain downstream.