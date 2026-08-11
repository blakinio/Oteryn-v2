# DUR-02 — Profile-Neutral Core Character Schema Decision Packet

- Status: **PRE-DECISION ARCHITECTURE / NOT ACCEPTED**
- Date: 2026-08-12
- Gate: `DUR-02 — Persistence v1`
- Scope: profile-neutral core Character persistence architecture only
- Trusted repository base: `blakinio/Oteryn-v2@2913201186d0e38cfc0bf0c9e2c5b83f981a61c6`
- Decision owner: product/architecture owner
- Consumes: ADR-0004, DUR-01, ANL-01, accepted GAME-CHAR Stage A/B, FND-04A/B/C, ADR-0012 and the Character Authority / Platform boundary
- Runtime authority: **NONE**
- Does not authorize: PostgreSQL DDL/migrations, database provisioning, runtime persistence code, item/currency persistence, production backup configuration, Platform writes, profile-specific PvP Character state or unresolved Reference values/formulas

## 1. Decision required

Accepted GAME-CHAR now answers **what Character semantics must be durable**. DUR-02 must next answer **how the profile-neutral core is physically structured and transactionally protected** without letting persistence convenience become gameplay policy.

The decision required here is intentionally narrower than a full production database implementation:

```text
semantic ownership accepted
-> choose physical relation/transaction/fencing architecture
-> preserve typed extension points
-> keep unknown profile/ruleset values outside schema invariants
-> later implementation proves SQL/migration/runtime behavior
```

### Must this architecture be decided now?

**YES.**

It directly blocks:

- final paper-only Character persistence architecture;
- future implementation of native Character Authority persistence;
- safe admission/lease persistence integration;
- durable Character mutation audit/outbox;
- migration and recovery design;
- later VSL-PERSISTENCE-01 implementation planning.

### Must SQL DDL or every profile-specific child table be decided now?

**NO.**

This gate should freeze relation ownership, keys, fencing, transaction boundaries, lock order and extension rules. Exact SQL syntax, migration framework/library, connection pool, index storage parameters and profile-specific tables remain implementation or owning-profile decisions.

## 2. Accepted constraints

### 2.1 Database and ownership

- authoritative native game persistence targets PostgreSQL;
- game and Platform use separate logical databases, owners, credentials and migration histories;
- no cross-database foreign keys;
- Platform may store/calculate commercial workflow state but may not directly mutate native Character tables;
- Character Authority is the only semantic writer for Character ownership/lifecycle/name/progression/build state.

### 2.2 Identity representation

Native UUIDv7 identities persisted by the game use PostgreSQL `uuid`, full 128 bits, nil invalid and no semantic reuse.

Relevant examples include:

- AccountId;
- CharacterId;
- WorldId;
- GameSessionId where durable continuity requires it.

Persisted `CommandId` retains FND-02's full nonzero uint64 range as PostgreSQL `numeric(20,0)` and is scoped by GameSessionId.

UUID ordering is never semantic chronology, revision or authority.

### 2.3 Character and session fencing are distinct

Accepted architecture requires separate concepts:

```text
CharacterRevision
!= CharacterLease generation
!= GameSessionId
!= connection_generation
!= RuntimeScopeAuthority ownership generation
```

Every durable Character-owned mutation validates the current Character revision/fence. FND-04 separately fences who may control/write through the current lease/session/runtime authority.

### 2.4 Audit/outbox

For a mutation requiring durable audit:

```text
authoritative mutation + mandatory immutable durable audit evidence
commit together
OR
neither is authoritative
```

Publication is at-least-once. Event replay never replays gameplay mutation. Same EventId retry preserves exact immutable event semantics and exact payload bytes.

### 2.5 GAME-CHAR profile-neutral boundary

Accepted GAME-CHAR permits a profile-neutral persistence core plus typed/versioned later profile extensions.

It explicitly forbids:

- treating current Global/OTS behavior as unresolved July-28 truth;
- one universal PvP/death profile;
- an untyped JSON/KV miscellaneous-state bag used to avoid semantic ownership;
- claiming one core schema complete for every future profile.

## 3. Options considered

### Option A — one wide `characters` row

Store identity, ownership, lifecycle, name, progression, skills, vocation, offline training, Wheel, charms, tasks, proficiency, session/lease and future state in one increasingly wide row.

**Rejected.**

Reasons:

- couples independent subdomains to one migration hotspot;
- turns every new profile capability into root-row churn;
- encourages nullable columns and accidental universal semantics;
- mixes Character semantic revision with FND-04 authority state;
- increases write contention and makes privacy/retention boundaries harder;
- cannot preserve the accepted child-aggregate option cleanly.

### Option B — generic EAV/JSON character state

Use one generic relation or JSON document for arbitrary Character fields/extensions.

**Rejected.**

Reasons:

- directly violates the accepted prohibition on untyped/generic miscellaneous state;
- weakens constraints, ownership, migration review and queryability;
- lets later gameplay systems bypass dedicated semantic decisions;
- makes compatibility failures appear as data-shape problems rather than contract violations;
- increases the risk of silent reinterpretation across ruleset/content revisions.

### Option C — event sourcing as Character source of truth

Treat immutable domain events as the primary authoritative Character state and rebuild current state by replay.

**Rejected for Persistence v1.**

ADR-0004 already selects current-state tables + revisions + idempotent operations + transactional outbox + bounded append-only critical audit rather than full event sourcing. ANL-01 also makes events evidence, not gameplay authority.

### Option D — normalized profile-neutral core + typed child relations/extensions

Use:

- one Character root relation as identity/lifecycle/ownership/current-revision lock anchor;
- a separate global name registry/history relation family;
- separate FND-04 presence/lease/session/continuity relations;
- durable operation receipts and optional durable command dedup where required;
- immutable audit journal + mutable publication state;
- typed Character-owned child relations for accepted capabilities;
- explicit typed/versioned profile extension boundaries;
- no generic payload escape hatch.

**RECOMMENDED.**

This preserves one logical Character authority and one global CharacterRevision while allowing physical decomposition where lifecycle, size, contention or migration needs differ.

## 4. Recommended relation ownership map

Names below are logical relation-family names for architecture clarity. They are **not SQL DDL identifiers** and exact SQL naming remains implementation-owned.

### 4.1 `character_root`

One row per CharacterId.

Owns the profile-neutral facts required to anchor all Character-owned mutations:

- `CharacterId` — canonical game-owned UUIDv7 primary identity;
- current owner `AccountId` — Platform-issued UUIDv7 reference, no cross-database FK;
- current `WorldId` — stable external/world-registry reference, no ownership implied by storage;
- lifecycle state — accepted `ACTIVE | DELETION_SCHEDULED | RETIRED` semantics;
- monotonic `CharacterRevision` — optimistic/stale-state fence and global Character mutation sequence;
- active profile/ruleset interpretation revision references needed for Character semantic state;
- creation/starter context revision references sufficient to interpret/migrate initial Character-owned state;
- explicit lifecycle timestamps/evidence where required by accepted policy;
- row-level schema/migration compatibility metadata only where the owning migration design proves it necessary.

Does **not** own:

- item/inventory/equipment/container/currency state;
- quest/content aggregate state by default;
- Platform entitlements/commercial records;
- GameSession/lease/control generations;
- generic extension JSON;
- exact Reference arithmetic.

### CharacterRevision rule

Every committed Character-owned durable mutation that changes semantic Character state:

1. locks/revalidates the root;
2. validates any caller-supplied expected CharacterRevision when the operation contract uses optimistic state;
3. rejects/reconciles stale expected state;
4. advances CharacterRevision exactly once for that committed Character transaction boundary;
5. records resulting revision in its durable operation/audit evidence.

A transaction may update multiple typed child rows but still advances the single CharacterRevision once.

CharacterRevision is never derived from UUID order, database transaction ID, wall clock, EventId or lease generation.

### 4.2 `account_character_guard`

A game-owned concurrency anchor keyed by AccountId.

Purpose:

- serialize account-scoped Character Authority mutations whose correctness depends on the current portfolio, such as create, restore and account ownership transfer;
- enforce the accepted active-character quota under one game-owned critical section;
- provide deterministic multi-account lock ordering for transfers.

It is **not**:

- a second Account record;
- proof that Platform AccountId exists or is authorized;
- a cached source of Platform security/entitlement state;
- a drift-prone authoritative active-character counter.

### Quota rule

The authoritative count/eligibility is derived from current Character Authority rows under the account guard and the active lifecycle/quota policy revision.

The guard must not become an independently maintained `active_count` source of truth unless a later performance proof introduces a transactionally verified counter with reconciliation invariants.

For account transfer, acquire both account guards in deterministic canonical AccountId order before Character mutation.

### 4.3 `character_name_registry`

Separate physical relation family for:

- current authoritative name claim;
- canonical comparison key;
- naming-policy revision;
- current/former/reserved semantic class;
- CharacterId ownership of the claim/history relation;
- effective/reservation timestamps where the accepted naming policy requires them.

The **game domain computes the canonical comparison key using the accepted naming policy**. PostgreSQL enforces equality/uniqueness over the resulting canonical value; PostgreSQL collation must not perform or invent semantic normalization.

Recommended physical concept:

```text
display_name
canonical_key = complete canonical comparison value
naming_policy_revision
claim_class = CURRENT | FORMER_ALIAS | RESERVED
CharacterId
policy-owned effective/release evidence
```

The canonical key must be stored losslessly. A truncated/hash-only key may not be the sole authoritative equality value.

The exact normalization/repertoire/recycling algorithm remains a parity gate. The relation can retain `release_at = NULL / unresolved by policy` rather than inventing a duration.

### Uniqueness rule

The database must provide a single authoritative conflict constraint for currently conflict-participating canonical keys. The exact PostgreSQL index/constraint syntax is implementation-owned, but application-only "check then insert" without an authoritative database constraint is rejected.

Rename atomically changes current name claim/history semantics with the Character revision. CharacterId does not change.

### 4.4 `character_build_core`

Typed child relation for profile-neutral build/profession linkage, conceptually including:

- CharacterId;
- current build/vocation-definition reference where one exists;
- explicit pre-vocation/unselected state;
- promotion-achievement state/reference;
- build/ruleset definition revision;
- local child revision only if implementation evidence proves it useful.

The Character root revision remains the authoritative global stale-state fence for Character mutations.

Reference vocation names/titles are ruleset definitions, not physical enum values embedded into the engine schema. Physical representation of stable ruleset definition keys remains owned by the ruleset/content contract; DUR-02 must consume that representation rather than invent a second identity system.

### 4.5 progression relations

The neutral core must support Character-owned authoritative progression facts without embedding unresolved arithmetic.

Recommended split:

- one typed relation for universally required scalar Character progression facts once their persisted-vs-derived status is accepted by the relevant ruleset;
- separate typed skill-state relation family keyed by the accepted stable ruleset skill-definition key;
- additional typed child relations for modern progression systems only when their owning semantic/profile contract is accepted.

Architecture invariant:

```text
persisted authoritative fact
!= deterministic derived projection
```

DUR-02 must not persist duplicate representations merely because a formula is currently unknown unless the owning migration/evidence contract establishes both values are separately authoritative.

Where target import/migration requires preserving a value that cannot safely be recomputed (capacity is the accepted example), the schema must preserve that authoritative fact and its interpretation revision.

### Skill/profile extension boundary

The Reference eight-skill catalogue is accepted semantically, but exact advancement-state representation and stable definition-key encoding are ruleset-owned. Therefore this packet does **not** freeze a fixed eight-column table or an opaque advancement blob.

A later physical extension must be typed, definition-keyed, revisioned and migration-safe.

### 4.6 typed Character-owned profile extensions

Character-specific progression systems such as:

- Weapon Proficiency Progress;
- charms/charm points/charm expansion;
- Hunting Task Points;
- permanent Hunting Task slots;
- permanent Prey slots;
- Wheel/Promotion Point state;
- Animus Mastery;
- future profile-specific PvP Character facts;

must use dedicated typed relation families or explicitly typed child aggregates when their physical contract is accepted.

Each extension must declare:

- semantic owner;
- CharacterId relation;
- stable definition identity/key and its owner;
- schema/revision compatibility;
- transaction interaction with CharacterRevision;
- migration/rollback rules;
- retention/privacy rules where applicable;
- whether mutation must share the Character root transaction.

No extension receives a generic `type + JSON/blob payload` persistence path merely because its final table has not yet been designed.

## 5. FND-04 persistence boundary

FND-04 authority state must be physically separate from Character semantic state even though it references CharacterId.

### 5.1 `account_presence_claim`

Keyed by AccountId and records the game-domain account-global mandatory-presence Character relation required by FND-04.

It is an authority/exclusion relation, not a Character ownership mapping duplicate.

It must never substitute for `character_root.account_id`, and the Character ownership relation never substitutes for current presence/control authority.

### 5.2 `character_lease`

Keyed by CharacterId and stores the current CharacterLease fencing state needed for restart/failover safety, including at minimum:

- nonzero, monotonic, non-reused `character_lease_generation` or accepted equivalent;
- current lease/control status needed by FND-04;
- current holder/session/runtime-scope references where the accepted FND-04 implementation contract requires them;
- restart-stable lease deadline/freshness evidence once its numeric policy is accepted.

`character_lease_generation` is never CharacterRevision.

Stale lease generation can never renew, commit a mutation or regain control.

Exact TTL/renew/safety deadlines remain deferred and must not appear as schema constants in this packet.

### 5.3 `game_session`

Durable continuity relation keyed by GameSessionId when required for FND-04 recovery. It conceptually records:

- AccountId and CharacterId binding for the accepted session;
- session lifecycle state;
- current `connection_generation`;
- current lease generation reference/fence;
- current actor/control continuity state needed for recovery;
- exact ruleset/content/world-policy compatibility revisions needed by the recovery contract;
- terminality evidence.

A terminal GameSessionId never revives.

GameSessionId is identity, not bearer proof.

### 5.4 `control_loss_continuity`

Typed FND-04 continuity relation, keyed by the relevant Character/actor continuity scope, for restart-safe state such as:

- non-reused ControlLossEpoch discriminator/ordinal or equivalent;
- authoritative epoch origin;
- original same-session grace deadline once policy is accepted;
- protection-used/eligible state;
- exact four-second protection activation/expiry evidence;
- protection re-arm state/deadline once accepted;
- relation to current/terminal session as FND-04 requires.

Persisted deadlines must be restart-stable and may not restart/extend because a process restarts.

Process-local monotonic timer values cannot be serialized as if they remained meaningful after restart. The implementation contract must use a restart-stable trusted time representation and preserve any required clock-uncertainty semantics.

### 5.5 reconnect proof material

This packet does not freeze secret hashing/encryption/KMS representation because FND-04B explicitly leaves it deferred.

Required physical boundary only:

- secret/verifier material is separate from ordinary Character rows and analytics;
- never stored in plaintext logs/audit/telemetry;
- generation/predecessor fencing remains provable after permitted restart;
- a later security contract must freeze exact storage/rotation before runtime implementation.

## 6. Idempotency and durable receipts

### 6.1 Character Authority operation receipts

Retryable cross-system Character mutations require a durable operation identity and result reconciliation.

Recommended relation family: `character_operation_receipt`, keyed by ANL-owned `OperationId` for operations that need independent durable retry identity.

It records a bounded typed envelope such as:

- OperationId;
- operation family/kind;
- authenticated caller/semantic request fingerprint sufficient to detect conflicting reuse;
- target CharacterId where known;
- terminal/nonterminal operation state;
- bounded stable result category;
- resulting CharacterRevision where applicable;
- TransactionId for committed atomic mutation where applicable;
- created/completed evidence timestamps.

It must not store arbitrary result JSON as the canonical operation contract.

Rules:

- same OperationId + same semantic request -> same logical operation/reconciliation result;
- same OperationId + conflicting request -> conflict, never overwrite/reinterpret;
- timeout is not success/failure proof;
- create retry before CharacterId is known resolves through OperationId to the single created CharacterId or stable terminal result;
- ownership/world transfer retries cannot apply the mutation twice.

### 6.2 persisted gameplay command dedup

Do **not** persist every gameplay CommandId universally merely because DUR-01 defines its scalar form.

Where a command crosses an ambiguous durable mutation boundary and FND-02/DUR contract requires durable command dedup, its identity is exactly:

```text
(GameSessionId, CommandId)
```

A durable receipt may record request fingerprint/result/TransactionId/revision as required. Equal numeric CommandId in another GameSession is a different command.

Retention is bounded and operation-owned; exact retention durations remain later implementation/policy evidence.

### 6.3 TransactionId

Each logical atomic durable mutation transaction requiring ANL transaction evidence uses one stable TransactionId across ambiguous physical commit retry/reconciliation.

Database attempt IDs, WAL positions and local surrogate keys never replace TransactionId.

## 7. Transaction architecture

### 7.1 One Character mutation anchor

Every Character-owned durable mutation locks/revalidates `character_root` before changing Character-owned state.

This intentionally serializes durable mutation **per Character**, matching the accepted global CharacterRevision fence.

It does not serialize unrelated characters globally.

### 7.2 Account-scoped operations

Create, restore when quota-sensitive, and account transfer acquire `account_character_guard` before Character mutation/count evaluation.

For transfer between two AccountIds:

1. acquire both account guards in canonical UUID byte order;
2. revalidate current Character owner;
3. acquire/validate Character root;
4. apply current destination quota policy;
5. revalidate required quiescence/lease absence;
6. commit owner rebinding + CharacterRevision + receipt + mandatory audit atomically.

This prevents opposing transfers/create/restore races and avoids a drift-prone counter.

### 7.3 Name operations

Create/rename:

- compute canonical key under an explicit naming-policy revision outside database collation semantics;
- rely on authoritative database uniqueness for the complete key;
- never use advisory `check availability -> later insert` as correctness;
- atomically bind name claim/history with Character mutation/receipt/audit.

Same-name races produce one database-authoritative winner.

### 7.4 Quiescent high-impact operations

Stage A remains binding: terminal retirement, world transfer and account ownership transfer require the actor `ABSENT` and no current playable CharacterLease before commit in the first native architecture.

DUR-02 must lock/revalidate the relevant lease/presence rows at the final transaction boundary rather than relying on a stale precheck.

### 7.5 Death and item/economy split

DUR-02 may define the Character-owned progression consequence transaction shape, but it does **not** decide item/corpse/value conservation.

Before a Reference death path that changes both Character progression and items is implemented, `GAME-ITEM-01`/`DUR-03` must define whether those changes share one PostgreSQL transaction coordinator or another proven atomic/reconciliation boundary.

This packet must not create a silent partial-success path.

## 8. Isolation, locks and retries

### Recommended default

Use PostgreSQL `READ COMMITTED` only with **explicit locked authority anchors + database constraints** for every correctness-sensitive invariant in this packet.

Examples:

- Character root row lock -> per-Character mutation serialization and revision;
- account guard row lock -> portfolio/quota serialization;
- authoritative unique constraint -> name conflict;
- lease row lock/generation compare -> stale lease rejection;
- operation/command unique identity -> idempotency conflict.

An operation whose invariant cannot be proven under this model must either:

- introduce a dedicated accepted lock/constraint anchor; or
- use PostgreSQL `SERIALIZABLE` for that bounded transaction with a stable retry/reconciliation contract.

`READ COMMITTED` without an explicit anomaly proof is not acceptance by default.

### Advisory locks

PostgreSQL advisory locks may be used only as a performance/coordination supplement after evidence. They may not be the sole durable authority for Character ownership, name uniqueness, quotas or lease fencing.

### Deterministic lock ordering

Within one transaction, acquire same-class multi-entity locks in canonical full-identity byte order. Cross-class ordering is:

```text
account portfolio guard(s)
-> Character root(s)
-> FND-04 presence/lease/session rows required by the operation
-> name claim/history rows where existing rows are locked
-> typed Character child rows in stable definition-key order
-> operation/audit/outbox inserts
```

A unique name-key insert may race on the unique constraint rather than locking a nonexistent row.

No code may reverse this order for convenience without an explicit deadlock proof/review.

### Retry rule

Serialization failures, deadlocks, lost responses and ambiguous commit outcomes retry/reconcile with the **same semantic operation identity**.

Retries must not mint a new OperationId/TransactionId merely because the database attempt changed.

Bounded retry count/backoff values are implementation/performance policy, not frozen here.

## 9. Immutable durable audit journal and publication state

### 9.1 Reject mutable outbox-as-audit-only design

If one mutable outbox row is overwritten/deleted after publication, it cannot simultaneously be the long-lived immutable critical audit record.

### 9.2 Recommended split

Use two relation families:

#### `durable_event_journal`

Immutable canonical evidence carrying the ANL-01 semantic event record, including:

- EventId;
- registered event type/schema revision;
- durability/privacy/retention profile references;
- immutable trusted event timestamp/context;
- OperationId/TransactionEventRef/Correlation/Causation/context where applicable;
- applicable ruleset/content/domain revisions;
- **exact registered payload bytes**;
- payload SHA-256;
- Character/domain revision linkage where the event type requires it.

Same EventId cannot be updated to different immutable content.

#### `event_publication_state`

Mutable delivery state keyed/referencing EventId, used for:

- pending/published/retry/quarantine state;
- broker/transport attempt metadata;
- next-attempt timing;
- delivery checkpoint/error bookkeeping.

Mutable delivery metadata is not authoritative gameplay/audit content.

### 9.3 Atomicity

For every Character mutation requiring durable audit:

```text
Character current-state mutation
+ CharacterRevision advance
+ operation/command receipt where required
+ every mandatory durable_event_journal row
+ publication-state enqueue record
commit in one PostgreSQL transaction
```

If mandatory journal/enqueue evidence cannot commit, the Character mutation must not become authoritative.

Best-effort telemetry is explicitly excluded from this atomic transaction and cannot block gameplay.

### 9.4 Publication/replay

- publisher reads committed publication state only;
- delivery is at-least-once;
- EventId deduplicates consumer effects;
- publication retry never reconstructs event bytes from later mutable Character state;
- replay reads evidence/projections only and cannot resubmit Character mutations.

## 10. Current state versus checkpoints

### 10.1 Current-state tables are canonical Character durability

Do not create a second generic serialized Character snapshot as a parallel source of truth.

The committed root + typed Character-owned relations at a CharacterRevision are the authoritative durable Character state.

### 10.2 Checkpoint manifest when runtime domains need one

If runtime/profile systems later require a consistent recoverable checkpoint beyond normalized current-state rows, use a typed checkpoint manifest conceptually containing:

- CharacterId;
- checkpoint/CharacterRevision boundary;
- applicable ruleset/content/map/world-policy revisions;
- current runtime scope/ownership evidence where required;
- references to **typed owner-specific checkpoint components**.

The manifest cannot contain a generic arbitrary state payload. Each component must have its own accepted typed schema/owner/migration contract.

### 10.3 No acknowledged-success-before-commit

A Character mutation success response must never be emitted as authoritative before the owning PostgreSQL transaction commits.

A lost success response produces an ambiguous result that is resolved from the durable operation/command receipt and current state; it does not repeat the semantic mutation blindly.

This is a logical commit/ack invariant, not a numeric disaster-recovery RPO promise.

## 11. Restart, crash and disaster restore

### 11.1 Ordinary process crash/restart

Committed Character state, CharacterRevision, operation receipts, mandatory audit journal and required FND-04 continuity/fence state must be reconstructible from PostgreSQL before authority is resumed.

In-memory caches/Redis cannot restore authority by themselves.

### 11.2 No authority resurrection

A restart or failover may never:

- reset CharacterRevision;
- reset/reuse CharacterLease generation;
- revive a terminal GameSession;
- reset connection generation;
- restart same-session grace/protection deadlines;
- reuse ControlLossEpoch entitlement;
- reapply an already committed operation.

If current authority cannot be proven, admission/mutation fails closed or proceeds through the accepted fresh/recovery path rather than guessing.

### 11.3 Point-in-time/disaster restore

A database restored to an older point cannot safely assume pre-restore sessions/leases remain current merely because their rows exist in the restored snapshot.

Before restored data may serve new gameplay authority, the operational restore contract must:

1. keep admission/authoritative mutation closed during reconciliation;
2. establish a strictly newer non-rollback recovery/authority fence outside any value that could itself have rolled back with the restored snapshot, or use an equivalently proven mechanism;
3. invalidate/fence pre-restore live TransportBinding/session/lease authority that cannot be proven current;
4. reconcile Platform security/account state and current world/routing revisions;
5. verify CharacterRevision/name/operation/audit/outbox integrity at the restored cut;
6. publish/replay only committed audit/outbox evidence and never replay gameplay commands;
7. open traffic only after restore validation passes.

The exact storage/issuer for the restore-generation fence is a later DUR/OPS security decision. This packet freezes the **no authority resurrection** requirement, not its implementation.

### 11.4 RPO/RTO

DUR-02 requires:

- PostgreSQL backup + WAL/PITR capability appropriate for the production topology;
- automated restore verification;
- integrity checks covering Character root/children, name registry, leases/sessions, operation receipts and audit/outbox;
- recorded exact backup/restore artifact/revision evidence.

Numeric production RPO/RTO targets remain OPS/PERF/product-milestone decisions and are not guessed in this packet.

## 12. Schema migration and compatibility

### 12.1 Game-owned migration history

`oteryn_game` has one game-owned migration history. Platform migrations never apply game schema changes.

### 12.2 Expand / migrate / validate / cut over / contract

Any incompatible persistence evolution follows a staged model conceptually equivalent to:

```text
EXPAND
-> resumable/idempotent BACKFILL or TRANSFORM
-> VALIDATE constraints/invariants
-> CUT OVER compatible readers/writers
-> CONTRACT obsolete representation only after rollback window closes
```

### 12.3 Semantic migrations are explicit

Ruleset/profile/content definition changes that alter persisted interpretation require explicit source and destination revisions plus deterministic migration/compatibility evidence.

A revision change alone must not silently reinterpret existing Character facts.

### 12.4 Migration properties

- migration IDs/revisions never reused;
- backfills are restartable/idempotent and bounded;
- partial migration has an explicit resumable state;
- constraints become authoritative only after data validation;
- incompatible old writers are fenced before destructive contract phase;
- rollback order is documented before cutover;
- CharacterId and other domain identities never change merely because storage representation changes;
- no migration creates alternate Character identities for retry convenience.

### 12.5 Definition-key evolution

Profile extensions referencing skill/vocation/weapon/charm/etc definitions must retain stable definition identity or an explicit deterministic mapping across incompatible revisions. Database row position or enum ordinal is never a durable definition identity.

## 13. Foreign keys, deletion and privacy

### 13.1 Internal FKs

Game-owned typed child relations should use CharacterId foreign-key/reference integrity where both sides share the same game migration authority.

Exact deferrability/cascade syntax remains implementation-owned.

### 13.2 No semantic cascade delete

Ordinary lifecycle retirement is a state transition, not a physical `DELETE CASCADE` operation.

A child row must not disappear merely because Character lifecycle becomes RETIRED unless its owning semantic/retention contract explicitly requires it.

### 13.3 CharacterId non-reuse

Physical cleanup can never make a retired CharacterId reusable. Tombstone/provenance evidence remains sufficient to prevent reuse and reconcile audit/import references.

### 13.4 Privacy erasure is separate

Privacy deletion/anonymization may later redact or remove eligible player-linked fields under `DATA-PRIVACY-01`, but it must not be modelled as semantic Character identity reuse or as implicit deletion of mandatory security/audit evidence.

Name history/alias retention and public exposure remain policy-owned and must carry explicit privacy/retention rules before production.

## 14. Index and query intent

Exact indexes are implementation-owned, but architecture requires efficient authoritative access paths for:

- CharacterId root lookup;
- current Characters by AccountId + lifecycle/policy eligibility;
- current Characters by WorldId where game operations need it;
- full canonical name-key conflict lookup;
- current CharacterLease by CharacterId;
- AccountPresenceClaim by AccountId;
- GameSession by GameSessionId and current Character where recovery requires it;
- OperationId receipt reconciliation;
- `(GameSessionId, CommandId)` durable dedup where implemented;
- pending event publication without scanning full audit history;
- audit/event lookup by EventId/TransactionId/Character revision where authorized.

Rules:

- authoritative equality uses full identity/key values;
- UUIDv7 order can improve locality but never defines chronology;
- partial/hash-only indexes can accelerate lookup but cannot replace full equality verification;
- high-cardinality gameplay identities are not ordinary metrics labels.

## 15. Failure contract for future implementation

A later implementation must produce bounded semantic outcomes for at least:

| Condition | Required disposition |
|---|---|
| stale CharacterRevision | conflict; no mutation |
| stale CharacterLease generation | conflict; no mutation/control |
| duplicate identical OperationId | reconcile/replay same logical operation result |
| same OperationId with conflicting request | conflict; no reinterpretation |
| duplicate durable `(GameSessionId, CommandId)` | same command identity; no second effect |
| same numeric CommandId in another GameSession | distinct command identity |
| canonical name-key conflict | one authoritative winner; loser conflict |
| account quota race | serialized under account guard; no over-quota commit |
| database unavailable | no authoritative Character mutation; no Redis/in-memory fallback |
| deadlock/serialization failure | bounded same-operation retry/reconciliation |
| mandatory audit journal unavailable in transaction | mutation does not commit |
| publication dependency unavailable after commit | durable backlog/retry; committed gameplay not rolled back |
| unsupported schema/profile/definition revision | fail closed; no reinterpretation |
| ambiguous commit response | reconcile from receipt/current authoritative state |
| restored stale session/lease authority | fenced; no authority resurrection |

Raw PostgreSQL errors are not public contracts.

## 16. Security boundaries

- game DB runtime credentials cannot write Platform DB;
- Platform runtime credentials cannot write Character relations;
- read projections use explicit read-only APIs/views/contracts, not mutation-capable ORM access;
- reconnect secrets/credentials never enter ordinary audit/analytics;
- AccountId/CharacterId knowledge is never authorization;
- database administrators remain operationally privileged but application architecture does not depend on manual raw SQL for normal Character correction;
- support/GM mutations must eventually use typed audited domain commands.

## 17. Implementation evidence required later

This packet is paper-only. A future DUR-02 implementation claiming conformance must prove at least:

### Identity and constraints

- full UUID round trips for every implemented identity;
- full CommandId numeric range where persisted;
- no cross-semantic ID substitution;
- CharacterId non-reuse;
- canonical name-key uniqueness race.

### Revision/fencing/concurrency

- stale CharacterRevision rejection;
- stale lease/session generation rejection;
- two concurrent Character mutations produce one serialized revision order;
- create/restore/account-transfer quota races cannot exceed accepted policy;
- opposing account transfers and rename/transfer races terminate without split ownership/deadlock corruption;
- deadlock/serialization retry retains semantic operation identity.

### Idempotency

- duplicate create retry creates one Character;
- rename/delete/restore/world/account-transfer ambiguous-response retry applies one semantic mutation;
- same OperationId conflicting payload fails closed;
- durable command duplicate cannot double-apply a mutation.

### Audit/outbox

- mutation + mandatory exact audit bytes + enqueue are atomic;
- crash after commit/before publish redelivers same EventId/bytes;
- duplicate publish yields one consumer effect;
- same EventId conflicting content fails integrity checks;
- publication backlog cannot be discarded for capacity;
- replay cannot mutate gameplay.

### Crash/recovery

- process restart reconstructs CharacterRevision/lease/session/ControlLoss continuity without timer reset;
- stale transport cannot regain authority;
- lost commit response reconciles from durable state;
- terminal GameSession cannot revive.

### Migration/restore

- expand/backfill/validate/cutover/contract fixture;
- interrupted backfill resumes idempotently;
- incompatible writer is fenced before contract phase;
- restore drill verifies Character/name/receipt/audit/outbox integrity;
- PITR/restore cannot resurrect pre-restore session/lease authority;
- rollback/recovery evidence is retained.

### Privacy/access

- Platform write credentials rejected from game Character tables;
- public/read projection cannot expose unauthorized AccountId-to-character relation;
- analytics pseudonym rules cannot fall back to raw CharacterId.

## 18. Decision package

### RECOMMENDATION — NOT OWNER-ACCEPTED

Accept the following as the minimum DUR-02 profile-neutral Character persistence architecture:

1. **Normalized current-state architecture**, not full event sourcing: `character_root` is the Character identity/lifecycle/ownership/global-revision lock anchor; typed child relations hold physically distinct state.
2. **One global CharacterRevision** advances once per committed Character-owned transaction and is independent from FND-04 lease/session/runtime generations.
3. **Game-owned AccountId guard rows** serialize quota-sensitive Character operations without becoming Account authority or a second active-count truth.
4. **Separate global name registry/history** stores the complete domain-generated canonical key + naming-policy revision and relies on database uniqueness; DB collation never invents canonicalization.
5. **FND-04 authority relations remain separate**: AccountPresenceClaim, CharacterLease generation, GameSession/connection generation and ControlLoss continuity are physically distinct from Character semantic revision/state.
6. **Typed profile extensions only**: dedicated child relations/aggregates for accepted Character-specific systems; no generic JSON/KV/EAV misc-state escape hatch.
7. **Durable operation receipts** use OperationId for retryable Character Authority workflows; persisted `(GameSessionId, CommandId)` dedup exists only where a durable gameplay command boundary actually requires it.
8. **Transaction model** serializes each Character mutation through the root, uses account guards for portfolio/quota operations, revalidates lease/presence at commit for quiescent high-impact operations, and relies on authoritative constraints for name/idempotency races.
9. **Isolation policy** uses explicit lock/constraint proofs; `READ COMMITTED` is acceptable only when those anchors close the anomaly, otherwise bounded `SERIALIZABLE` + same-operation retry is required. Advisory locks are never sole authority.
10. **Audit architecture** separates immutable `durable_event_journal` from mutable publication state; mandatory audit/journal/enqueue commits atomically with the Character mutation, while best-effort telemetry stays asynchronous.
11. **Current-state relations are the Character checkpoint**; no redundant generic snapshot blob. Any additional checkpoint uses a manifest referencing typed owner-specific components.
12. **No acknowledged-success-before-commit**; ambiguous results reconcile from durable receipts/current state rather than repeating mutations blindly.
13. **Restore safety** prohibits authority resurrection: PITR/disaster restore cannot trust rolled-back session/lease rows and requires a newer non-rollback recovery fence/equivalent proof before admission resumes.
14. **Schema evolution** follows expand -> migrate/backfill -> validate -> cut over -> contract, with explicit semantic migration and incompatible-writer fencing.
15. **Retirement != physical deletion != privacy erasure**; CharacterId is never reused and ordinary lifecycle does not use cascade hard delete.
16. **Profile-neutral core only**: unresolved Reference values/formulas and profile-specific PvP/world facts remain outside core schema invariants; a profile extension becomes complete only after its owning semantic gate is accepted.
17. **Operational numbers remain downstream**: exact lease TTL, reconnect/grace/re-arm timings except already accepted four-second protection, retry limits, retention, backup frequency and numeric RPO/RTO require their owning evidence/policy before implementation.

## 19. Effect if owner later accepts

Recommended status after a separate owner-baseline delivery lifecycle:

```text
DUR-02
DecisionStatus       = ACCEPTED — profile-neutral Character persistence architecture scope
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
Runtime authority    = NONE
DDL/migrations       = NOT_AUTHORIZED
```

Acceptance would unblock a **separately authorized implementation design/package** for the profile-neutral Character persistence core and would provide a stable consumer contract for later profile extensions.

It would **not**:

- create or migrate PostgreSQL tables;
- accept `GAME-ITEM-01` or `DUR-03`;
- define item/currency atomicity;
- select first Reference PvP/world profile;
- make unresolved Reference arithmetic/content/profile behavior true;
- authorize runtime Character persistence;
- define production RPO/RTO or backup frequency;
- authorize Platform or production changes.

## 20. Supersession / reopening

A later proposal may reopen an accepted DUR-02 clause only with named evidence such as:

- a proven correctness anomaly not closed by the accepted lock/constraint model;
- measured contention/scale evidence showing the single Character root revision anchor is an unacceptable bottleneck and an equivalent safe partitioned-revision model is proven;
- an accepted profile-specific semantic contract requiring additional typed durable state;
- evidence that a deferred Reference formula/value constrains physical representation or transaction atomicity;
- a PostgreSQL feature/limitation discovered during implementation that requires an equivalent safer relation/locking design;
- security/privacy/restore evidence requiring a stronger fence or data separation model;
- an explicit later architecture decision superseding ADR-0004's Persistence-v1 direction.

Convenience, ORM defaults, current Global schema, Canary/crystalserver tables or generic JSON flexibility are not sufficient supersession evidence.

## 21. Deliberately not decided

- exact SQL table/column/index/constraint names;
- exact schema namespace names;
- exact migration framework/library;
- ORM/query builder or Rust database crate;
- connection-pool technology/settings;
- exact stable ruleset/content definition-key scalar representation where its owner has not frozen it;
- profile-specific progression child table layouts;
- item/currency/market/house schema;
- exact PostgreSQL partitioning/sharding strategy;
- exact operational retention/backup/RPO/RTO values;
- exact retry/backoff limits;
- reconnect-secret hashing/KMS representation;
- production deployment topology;
- runtime implementation.

Until the owner accepts or modifies section 18, this document remains **PRE-DECISION ARCHITECTURE / NOT ACCEPTED** and `DUR-02` remains `PROPOSED / PLANNED / NOT_STARTED`.
