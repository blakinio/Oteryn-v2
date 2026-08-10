# ANL-01 — Game Event and Audit Foundation Contract

- Status: Candidate; canonical only when the owning ANL-01 delivery merges
- Date: 2026-08-10
- Gate: `ANL-01`
- Issue: #135
- Trusted base: `main@ef42fa47ab054ab8aa304c017307c1945f931b59`
- Scope: event/audit semantics, interchange, privacy and evidence foundation only

## 1. Purpose and authority

ANL-01 freezes the event/audit evidence contract required by ADR-0006 before DUR-02/DUR-03 may finalize transactional outbox and critical economy/security evidence.

It is not event sourcing and never becomes a second gameplay authority.

```text
gameplay/runtime/session authority -> FND/gameplay owners
physical persistence/transactions  -> DUR-02
item/currency conservation         -> DUR-03
event/audit evidence semantics     -> ANL-01
analytics/security consumers       -> ANL-02/03
investigation/AI                   -> ANL-04 read-only
```

## 2. Event interchange profile v1

```text
family:             oteryn-game-events
envelope revision:  1
serialization:      Protocol Buffers binary
source IDL syntax:  proto3
source IDL:         docs/contracts/game-events/v1/foundation.proto
registry:           docs/contracts/GAME_EVENT_FOUNDATION_REGISTRY.json
application compression: none
```

The event family is independent from `protocol-oteryn`. No broker, DB schema, warehouse, lake or dashboard product is selected.

Protobuf serialization is **not treated as canonical semantic serialization**. The committed exact event bytes are immutable delivery evidence; see Section 10.

## 3. Canonical identities

### EventId

```text
representation: UUIDv7, full 128 bits
owner/issuer: authoritative event producer boundary
scope: global one-event identity
nil: invalid
reuse: never
```

One EventId denotes one immutable event. Delivery retry/redelivery/replay reuses EventId. Same EventId with different immutable record bytes/bindings is an integrity conflict, never an update.

A best-effort observation dropped before event admission need not mint EventId. A durable audit EventId is fixed before/inside the owning transaction.

### OperationId

```text
representation: UUIDv7
owner/issuer: authoritative owner of the logical operation
scope: one independently durable multi-step/retry-capable operation
```

Optional; not every command gets one. Same-operation retries/reconciliation reuse it. A new independent operation receives a new ID. `CommandRef` remains distinct.

### TransactionId

```text
representation: UUIDv7
owner/issuer: authoritative durable transaction coordinator/owner
scope: one logical atomic durable mutation transaction
```

Ambiguous commit/retry of the same logical transaction retains TransactionId. Physical DB attempts are not canonical TransactionIds. A new TransactionId requires the prior logical transaction to be proven terminal and a new logical transaction intentionally started.

### CorrelationId

```text
representation: UUIDv7
owner/issuer: trusted Oteryn root/workflow boundary
scope: one bounded correlation context
```

Optional unless a family requires it. It is grouping only, never authorization, causality or order. Untrusted external trace/correlation input does not become canonical CorrelationId by assertion.

### CausationRef

ANL-01 intentionally defines **no separately minted CausationId UUID**.

```text
CausationRef =
  Event(EventId)
  | Command(GameSessionId, CommandId)
  | Operation(OperationId)
  | Transaction(TransactionId)
  | absent for a genuine root event
```

The existing typed cause identity is the causal reference.

### AnalyticsActorId

```text
representation: UUIDv7
owner/issuer: analytics privacy-identity authority
scope: analytics_identity_domain + identity_epoch + AnalyticsActorId
```

It is pseudonymous analytical identity, never AccountId/CharacterId/public identity.

Mandatory rules:

- no reversible/truncated derivation from operational identity/name/email;
- purpose/domain-scoped pseudonyms, not one universal cross-purpose ID;
- nonzero explicit identity epoch;
- mapping to operational identity is separately protected and every privileged lookup audited;
- pseudonymous event families never fall back to raw CharacterId if mapping is unavailable;
- durable audit needing operational identity uses a restricted privacy class instead.

Exact epoch duration is privacy-policy owned; production requires an accepted concrete policy.

## 4. Durable physical representation

Where ANL-owned UUIDv7 identities are stored in native game PostgreSQL, DUR-01 applies unchanged: PostgreSQL `uuid`, full 128 bits, strong type, nil invalid, no reuse.

FND-02 CommandId remains nonzero full uint64 scoped by GameSessionId; DUR-01 `numeric(20,0)` applies if persisted.

ANL-01 does not design tables/indexes.

## 5. Durability classes

### BEST_EFFORT_TELEMETRY

- bounded asynchronous collection;
- registered sampling/aggregation/drop policy permitted;
- gameplay fails open when analytics dependency is unavailable;
- accepted/dropped/retried/lag evidence is counted;
- gaps remain explicit;
- never sole proof of item/currency/security conservation.

### DURABLE_AUDIT

- never sampled or silently dropped;
- mandatory mutation evidence participates in the same accepted atomic transaction as the authoritative mutation;
- publication only after commit;
- at-least-once delivery;
- immutable EventId/content across retry;
- consumer EventId dedupe required;
- replay never replays gameplay mutation;
- committed backlog is never discarded to satisfy an in-memory limit.

A non-mutating security decision/rejection may be DURABLE_AUDIT without TransactionId only when its registered event type says `atomic_mutation_evidence=false`.

Operational observability is separate, not a third event durability class.

## 6. Envelope v1

Normative source: `docs/contracts/game-events/v1/foundation.proto`.

### Required

- `envelope_revision = 1`;
- EventId;
- registered nonzero event type ID;
- registered nonzero event schema revision;
- durability class;
- privacy class;
- accepted non-empty retention profile ID before production collection;
- trusted-server wall timestamp;
- bounded server build ID;
- registered protobuf payload bytes;
- exact SHA-256 of those exact payload bytes.

### Optional typed context

- WorldId;
- WorldId + ChannelId;
- WorldId + InstanceId;
- NodeId;
- GameSessionId;
- connection_generation with GameSessionId;
- RuntimeOrderRef;
- CommandId with GameSessionId;
- OperationId;
- TransactionId;
- transaction event ordinal/count;
- CorrelationId;
- CausationRef;
- AnalyticsActorRef;
- protocol major;
- ruleset/content revisions.

Generic actor/subject/object IDs and arbitrary metadata maps are excluded. Domain identities belong to typed payloads.

## 7. RuntimeOrderRef

FND-03 RuntimeExecutionOrdinal is meaningful only in its exact owner-generation scope. Therefore the event envelope never carries a naked ordinal.

```text
RuntimeOrderRef =
  scope_ownership_generation (nonzero)
  + runtime_execution_ordinal (nonzero)
```

Validation additionally requires a concrete semantic runtime scope in the envelope:

```text
WorldId + ChannelId
OR
WorldId + InstanceId
```

RuntimeOrderRef is internal evidence. It is stripped from ordinary public/pseudonymous projections unless their accepted purpose explicitly requires it. It never becomes protocol/client authority and never creates cross-generation/global order.

## 8. Transaction event completeness

When a registered `atomic_mutation_evidence=true` event carries TransactionId, it also carries:

```text
transaction_event_ordinal
transaction_event_count
```

Rules:

- both are nonzero;
- `1 <= ordinal <= count`;
- every event for the same committed TransactionId declares the same count;
- committed ordinals are exactly contiguous `1..count`;
- an ordinal cannot occur twice in one TransactionId;
- count/ordinal are immutable;
- count/ordinal never create cross-transaction order.

This lets consumers distinguish “event 2 has not arrived yet” from a complete one-event transaction and detect incomplete sets deterministically.

Non-atomic observation families may omit both.

## 9. Event type registry and schema evolution

`GAME_EVENT_FOUNDATION_REGISTRY.json` is the machine-readable allocation/evolution registry.

- event type ID 0 invalid;
- positive uint32 IDs are never reused;
- every event type declares owner, payload schema/message, current schema revision, durability, privacy floor, retention profile and atomic-mutation-evidence flag;
- per-type schema revision is nonzero and monotonic;
- removed protobuf field numbers/names are reserved;
- compatible additive evolution is allowed only when older consumers can safely ignore additions;
- unsafe semantic change requires a new event type or reviewed family-major transition;
- unregistered production emission is forbidden;
- unsupported durable schema is quarantined/rejected without deletion/reinterpretation;
- unsupported best-effort schema may be counted/dropped but never presented as complete.

The initial registry intentionally contains no gameplay-domain event IDs; owning domain gates add them.

## 10. Exact byte stability and payload hash

Protobuf does not provide a universal canonical byte serialization. ANL-01 therefore does **not** define semantic equality by “decode then reserialize”.

For each admitted event:

1. the producer materializes the exact registered payload bytes once;
2. `payload_sha256 = SHA-256(exact payload bytes)`;
3. EventId, event type/schema and exact payload bytes become one immutable event record before the first possibly-ambiguous durable commit/publication attempt;
4. retry/reconciliation/redelivery of the same EventId reuses those exact payload bytes; it must not reconstruct/reserialize the event from mutable domain objects;
5. a durable implementation must retain exact bytes or an equivalently proven byte-preserving representation sufficient to reproduce the same committed bytes;
6. the hash is integrity/conflict evidence, not event identity and not a substitute for EventId/type/schema validation.

This rule prevents a valid protobuf alternative encoding from creating an accidental “same EventId, new event” during retry.

Envelope serialization itself may vary in field ordering, so conflict validation compares registered immutable field values plus exact payload bytes/hash, not raw serialized envelope byte equality.

## 11. Ordering model

There is no global event total order.

```text
(GameSessionId, CommandId)           per-session command identity/order
RuntimeOrderRef                      scope + ownership-generation-local runtime order
TransactionId + ordinal/count       one transaction event set/order
CausationRef                         immediate causal edge
CorrelationId                        grouping only
state/domain revisions               authoritative state progression
wall timestamp                       correlation only
EventId UUIDv7 ordering              storage/locality only
```

Cross-transaction operation order uses causation and owning domain/state revisions. ANL-01 deliberately creates no global/operation-wide synchronized ordinal.

## 12. Atomic mutation/audit boundary

For an operation whose owning contract requires durable audit, before commit the TransactionId, required EventIds, exact event bytes, event count/ordinals and immutable type/schema/scope/privacy/retention bindings are fixed.

Valid commit is:

```text
authoritative mutation + every mandatory durable audit record
```

or neither becomes authoritative.

Mutation committed while mandatory evidence is absent is invalid and must not remain silent. DUR-02/DUR-03 define physical transaction/isolation/outbox proof.

## 13. Publication, duplicate delivery and replay

Canonical durable publication is:

```text
committed record -> publish at least once -> idempotent consumer
```

- only committed records publish;
- lost ack may cause redelivery;
- EventId/exact event content never changes across attempts;
- transport delivery IDs are not EventId;
- consumer applies at most one derived effect per identical EventId;
- checkpoint advances only after the consumer projection effect is safely accepted;
- exact checkpoint persistence belongs to consumer/DUR implementation;
- no broker-level exactly-once guarantee is required or claimed.

Same EventId + same immutable record is an idempotent duplicate. Same EventId + conflicting immutable record is `ANL_EVENT_ID_CONFLICT`; never overwrite/last-write-wins.

Replay is read-only toward authoritative gameplay. It never reissues original commands/credentials or mutates canonical game state.

## 14. Out-of-order behavior

Consumers use transaction count/ordinals, CausationRef and domain revisions to buffer, defer, quarantine/reject or rebuild from an explicit derived checkpoint. They never invent missing authoritative state.

Any buffer/replay work remains under registered hard limits.

## 15. Privacy classes

1. `INTERNAL_NON_PERSONAL` — internal facts without player-linked identity.
2. `PSEUDONYMOUS_ANALYTICS` — ordinary analytics through approved AnalyticsActorRef; raw AccountId/CharacterId forbidden by family contract.
3. `RESTRICTED_PLAYER_LINKED` — operational player/session/item-linked audit/admin evidence; least privilege + access audit.
4. `SECURITY_SENSITIVE` — abuse/recovery/security evidence; strongest role separation/export/redaction/access auditing.

Privacy class is a minimum protection floor and cannot be silently downgraded by projections.

## 16. Retention/production collection gate

Every concrete event type binds a non-empty retention profile before production collection. The accepted profile defines at minimum:

- purpose;
- privacy class;
- finite ordinary retention duration/ceiling;
- allowed roles/consumers;
- aggregation/anonymization transition if used;
- deletion/anonymization behavior;
- export/redaction behavior;
- explicit legal-hold authorization/audit;
- policy revision/rollout/rollback.

Ordinary `UNBOUNDED` retention is forbidden. Legal hold is an explicit exceptional state, not the default.

Unresolved purpose/privacy/retention/access => production collection/projection rejected. Privacy never fails open because telemetry is best-effort.

ANL-01 intentionally does not guess jurisdiction/product-specific duration values.

## 17. Pseudonym/access boundary

AnalyticsActorId mapping:

- is separated from ordinary analytics datasets;
- is not available to every analyst/operator;
- requires least-privilege purpose authorization;
- every privileged lookup is audited;
- never grants gameplay authority;
- follows accepted deletion/rotation/anonymization policy;
- never silently reuses an old epoch as a new epoch.

If pseudonym resolution is unavailable for best-effort pseudonymous telemetry, policy may count/drop. It may never substitute raw identity.

ANL-04 investigation/AI credentials remain read-only and cannot mutate runtime/database, sanction, balance, rollback or deploy.

## 18. Observability/cardinality boundary

AccountId, CharacterId, AnalyticsActorId, ItemInstanceId, TransactionId, EventId, GameSessionId and similar high-cardinality/player-linked IDs are forbidden as ordinary Prometheus labels.

Operational logging uses bounded/redacted correlation references only under logging policy. Credentials/private event payloads are never logged merely for debugging.

## 19. Error contract

| Code | Foundation category | Required disposition |
|---|---|---|
| `ANL_TELEMETRY_CAPACITY_DROPPED` | `CAPACITY_EXCEEDED` | best-effort counted loss; gameplay unchanged |
| `ANL_AUDIT_DEPENDENCY_UNAVAILABLE` | `DEPENDENCY_UNAVAILABLE` | no downgrade; owning DUR policy decides fail/hold |
| `ANL_EVENT_MALFORMED` | `INVALID_INPUT` | no consumer effect |
| `ANL_EVENT_SCHEMA_UNSUPPORTED` | `UNSUPPORTED_REVISION` | no reinterpretation/downgrade |
| `ANL_EVENT_ID_CONFLICT` | `CONFLICT` | no overwrite/merge |
| `ANL_EVENT_ORDER_BLOCKED` | `CONFLICT` | bounded defer/quarantine; no invented state |
| `ANL_REPLAY_CONFLICT` | `CONFLICT` | stop affected replay/projection; gameplay unchanged |
| `ANL_PRIVACY_POLICY_REJECTED` | `CONFLICT` | no collection/projection/disclosure |
| `ANL_INVESTIGATION_ACCESS_DENIED` | `CONFLICT` after caller authentication | no evidence disclosure |
| `ANL_EVIDENCE_INTEGRITY_FAILURE` | `INTERNAL_UNAVAILABLE` | fail safe; retain bounded evidence |

Authentication failure at an investigation boundary remains the existing `AUTHENTICATION_FAILED`; `ANL_INVESTIGATION_ACCESS_DENIED` is the authenticated-but-not-authorized policy denial.

Diagnostics redact restricted IDs/payloads and never contain credentials.

## 20. Resource limits

`RESOURCE_LIMITS_REGISTRY.json` is normative for ANL-01 ceilings.

- limits are security/allocation ceilings, not capacity guarantees or tuned defaults;
- implementations may configure lower values;
- sizes/counts checked before allocation/decode/amplification;
- no application event compression in v1;
- no arbitrary metadata maps;
- committed durable backlog is not dropped to enforce in-memory limits;
- replay/query/export is paged/batched.

## 21. Failure scenarios

| Scenario | Status | Invariant |
|---|---|---|
| `FS-ANALYTICS-TELEMETRY-OVERFLOW` | `PASS` | bounded counted best-effort loss, no gameplay effect/completeness claim |
| `FS-AUDIT-OUTBOX-BACKLOG` | `PASS` semantic / DUR-02 physical | committed evidence never silently dropped; retryable publication |
| `FS-EVENT-DUPLICATE-DELIVERY` | `PASS` | immutable EventId dedupe, no gameplay replay |
| `FS-EVENT-OUT-OF-ORDER` | `PASS` | count/ordinal + causation + revisions, no invented state |
| `FS-AUDIT-MUTATION-MISMATCH` | `PASS` semantic / DUR-02+03 physical | mandatory mutation+audit atomicity |
| `FS-ANALYTICS-PRIVACY-POLICY` | `PASS` | unresolved policy blocks production collection |
| `FS-DETECTOR-FALSE-POSITIVE` | `DEFERRED_BY_ACCEPTED_GATE` | ANL-03; ADR-0006 forbids automatic sanction |
| `FS-INVESTIGATION-MUTATION-ATTEMPT` | `DEFERRED_BY_ACCEPTED_GATE` | ANL-04 must prove read-only least privilege |
| `FS-DB-OUTBOX-BOUNDARY` | `PASS` semantic / DUR-02 physical | no valid mutation commit without mandatory audit set |

Architecture PASS does not claim runtime implementation evidence.

## 22. Required implementation evidence

Before ANL-01 implementation conformance claim:

- protobuf golden/cross-language envelope and payload fixtures;
- malformed/oversized/nesting/resource-limit negative corpus + fuzz/property tests;
- UUID type/version/nil/scope tests and CommandId/GameSession scope tests;
- exact payload-byte preservation across ambiguous commit/publication retry and SHA-256 verification;
- same EventId identical redelivery idempotency + conflicting redelivery rejection;
- RuntimeOrderRef requires scope + ownership generation and survives generation transitions without ordinal ambiguity;
- transaction event count/ordinal complete-set, duplicate/gap/inconsistent-count tests;
- crash before/after transaction commit and publication ack;
- consumer checkpoint crash recovery;
- out-of-order causal/revision behavior;
- unsupported schema behavior by durability class;
- best-effort queue overflow/drop counters;
- durable backlog without audit loss;
- raw-ID rejection in pseudonymous families;
- analytics identity domain/epoch isolation + privileged mapping access audit;
- unresolved retention policy blocks collection;
- bounded replay/query/export/evidence handling;
- replay/investigation cannot mutate authoritative gameplay.

Physical PostgreSQL atomicity evidence belongs to DUR-02/DUR-03 once implementation is authorized.

## 23. Downstream gates

After ANL-01 acceptance/lifecycle closeout:

- DUR-02 may finalize PostgreSQL schema/transactions/outbox/checkpoints using these semantics;
- DUR-03 may define item/currency event families and prove conservation + atomic evidence;
- ANL-02/03/04 may refine consumers/detectors/investigation under their own gates;
- ANL-01 alone authorizes no production collection.

## 24. Non-goals

No database layout/isolation/locks/migrations/RPO/RTO; no broker/warehouse/lake/dashboard product; no runtime collector; no exact legal/product retention durations; no speculative gameplay payload catalogue; no detector thresholds/auto-bans; no AI mutation; no Platform writes; no deployment/production collection.

## 25. Acceptance rule

ANL-01 is accepted only when the analysis/contract/IDL/registry/resource-limit package is internally consistent with ADR-0006/FND/DUR-01, exact-head governance/CI pass, terminal architecture/security/privacy/data-integrity review has zero material findings, zero material review threads remain, the accepted head is squash-merged unchanged, and a separate lifecycle closeout archives ownership and closes Issue #135.
