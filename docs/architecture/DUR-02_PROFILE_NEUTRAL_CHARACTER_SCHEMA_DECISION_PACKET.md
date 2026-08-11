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

Accepted GAME-CHAR now answers **what Character semantics must be durable**. DUR-02 must next answer **how the profile-neutral core is physically structured and transactionally protected** without allowing persistence convenience to become gameplay policy.

The decision required here is intentionally narrower than a production database implementation:

```text
accepted semantic ownership
-> choose physical relation / transaction / fencing architecture
-> preserve typed extension points
-> keep unresolved profile/ruleset values outside schema invariants
-> later implementation proves SQL / migration / runtime behavior
```

### Must this architecture be decided now?

**YES.**

It directly blocks:

- final paper-only Character persistence architecture;
- future native Character Authority persistence implementation;
- safe FND-04 admission/lease/session persistence integration;
- durable Character mutation audit/outbox design;
- migration and restore architecture;
- later VSL-PERSISTENCE-01 planning.

### Must SQL DDL or every profile-specific child table be decided now?

**NO.**

This gate should freeze relation ownership, keys, fencing, transaction boundaries, lock order, migration discipline and typed extension rules. Exact SQL syntax, migration library, connection pool, index storage parameters and profile-specific child schemas remain implementation or owning-profile decisions.

## 2. Accepted constraints

### 2.1 Database and ownership

- authoritative native game persistence targets PostgreSQL;
- game and Platform use separate logical databases, owners, credentials and migration histories;
- there are no cross-database foreign keys;
- Platform may own commercial/product workflow state but may not directly mutate native Character tables;
- Character Authority is the only semantic writer for Character identity/lifecycle/name/ownership/progression/build state.

### 2.2 Identity representation

Native UUIDv7 identities persisted by the game use PostgreSQL `uuid`, full 128 bits, nil invalid and no semantic reuse.

Relevant examples include:

- AccountId;
- CharacterId;
- WorldId;
- GameSessionId when durable continuity requires it.

Persisted `CommandId` preserves FND-02's full nonzero uint64 range as PostgreSQL `numeric(20,0)` in `(GameSessionId, CommandId)` scope.

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

Every durable Character-owned mutation validates the current Character revision/fence. FND-04 separately fences which session/lease/runtime authority may act.

### 2.4 Audit/outbox

For a mutation requiring durable audit:

```text
authoritative mutation + mandatory durable audit evidence
commit together
OR
neither is authoritative
```

Publication is at-least-once. Event replay never replays gameplay mutation. Same EventId retry preserves the same immutable semantic event and exact payload bytes while that event is retained.

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
- makes every new profile capability root-row churn;
- encourages nullable columns and accidental universal semantics;
- mixes Character semantic revision with FND-04 authority state;
- increases write contention and weakens retention/privacy boundaries;
- undermines the accepted child-aggregate option.

### Option B — generic EAV/JSON character state

Use one generic relation or JSON document for arbitrary Character fields/extensions.

**Rejected.**

Reasons:

- violates the accepted prohibition on generic miscellaneous state;
- weakens constraints, semantic ownership, migration review and queryability;
- allows gameplay systems to bypass dedicated architecture decisions;
- turns compatibility failures into opaque payload problems;
- increases silent reinterpretation risk across ruleset/content revisions.

### Option C — event sourcing as Character source of truth

Treat immutable domain events as primary authoritative Character state and rebuild current state by replay.

**Rejected for Persistence v1.**

ADR-0004 selects current-state tables + revisions + idempotent operations + transactional outbox + bounded append-only critical audit rather than full event sourcing. ANL-01 makes events evidence, not gameplay authority.

### Option D — normalized profile-neutral core + typed child relations/extensions

Use:

- one Character root relation as identity/lifecycle/ownership/global-revision lock anchor;
- a separate global name registry/history relation family;
- separate FND-04 presence/lease/session/control-loss relations;
- durable operation receipts and bounded durable command dedup where required;
- immutable audit journal + separate mutable publication state;
- typed Character-owned child relations for accepted capabilities;
- explicit typed/versioned profile extension boundaries;
- no generic payload escape hatch.

**RECOMMENDED.**

This preserves one semantic Character authority and one global CharacterRevision while allowing physical decomposition where lifecycle, size, contention or migration requirements differ.

## 4. Recommended relation ownership map

Names below are logical relation-family names for architecture clarity. They are **not SQL DDL identifiers**; exact SQL naming remains implementation-owned.

### 4.1 `character_root`

One row per CharacterId.

Owns the profile-neutral facts required to anchor all Character-owned mutations:

- `CharacterId` — canonical game-owned UUIDv7 identity;
- current owner `AccountId` — Platform-issued UUIDv7 reference, no cross-database FK;
- current `WorldId` — external/world-registry reference;
- lifecycle state — accepted `ACTIVE | DELETION_SCHEDULED | RETIRED` semantics;
- monotonic `CharacterRevision` — global Character stale-state fence and mutation sequence;
- active profile/ruleset interpretation revision references needed to interpret Character state;
- creation/starter context revision references needed to interpret/migrate initial Character-owned state;
- lifecycle timestamps/evidence where an accepted policy requires them;
- schema/migration compatibility metadata only where a later migration design proves it necessary.

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
2. validates caller-supplied expected CharacterRevision when the operation contract uses optimistic expected state;
3. rejects/reconciles stale expected state;
4. advances CharacterRevision exactly once for that committed Character transaction boundary;
5. records the resulting revision in durable operation/audit evidence.

A transaction may update several typed child rows but still advances the single CharacterRevision once.

CharacterRevision is never derived from UUID order, database transaction ID, wall clock, EventId or lease generation.

### 4.2 `account_character_guard`

A game-owned concurrency anchor keyed by AccountId.

Purpose:

- serialize every account-scoped Character Authority mutation whose correctness depends on current portfolio state;
- enforce quota-sensitive lifecycle/ownership transitions under one game-owned critical section;
- provide deterministic multi-account lock ordering for transfers.

This includes, whenever the active policy can change portfolio eligibility/count:

- create;
- schedule deletion;
- restore/cancel deletion;
- terminal retirement/finalization;
- account ownership transfer;
- any later lifecycle transition that changes quota eligibility.

It is **not**:

- a second Account record;
- proof that Platform AccountId exists or is authorized;
- a cache of Platform security/entitlement state;
- a separately authoritative active-character counter.

### Quota rule

The authoritative count/eligibility is derived from current Character Authority state under the account guard and the active lifecycle/quota policy revision.

The guard must not become an independently maintained `active_count` truth unless later performance evidence introduces a transactionally verified counter plus reconciliation invariants and an explicit superseding decision.

For account transfer, acquire both account guards in deterministic canonical full-AccountId byte order before mutating the Character.

### 4.3 `character_name_registry`

Separate relation family for:

- current authoritative name claim;
- complete canonical comparison key;
- naming-policy revision;
- current/former/reserved semantic class;
- CharacterId relation;
- effective/reservation evidence where the accepted naming policy requires it.

The **game domain computes the canonical comparison key using the accepted naming policy**. PostgreSQL enforces equality/uniqueness over the resulting complete value; PostgreSQL collation does not perform or invent semantic normalization.

Conceptual fields:

```text
display_name
canonical_key = complete canonical comparison value
naming_policy_revision
claim_class = CURRENT | FORMER_ALIAS | RESERVED
CharacterId
policy-owned effective/release evidence
```

The canonical key is stored losslessly. A truncated or hash-only key may accelerate lookup but may not be the sole authoritative equality value.

The exact normalization/repertoire/recycling algorithm remains a parity gate. Unresolved release timing may remain policy-unresolved instead of inventing a duration.

### Name-policy migration rule

One logical global namespace cannot safely have two simultaneously authoritative canonicalization universes that can disagree on equality.

Therefore a naming-policy revision migration must:

1. compute candidate canonical keys for all conflict-participating live/reserved claims under the destination policy;
2. detect and resolve/abort every new collision before cutover;
3. validate the destination authoritative uniqueness constraint/index;
4. atomically/compatibly cut readers and writers to the destination policy;
5. retain old-policy evidence/history only as non-authoritative migration/history data after cutover.

The authoritative uniqueness constraint may not be partitioned by naming-policy revision merely to avoid cross-revision conflicts unless an explicit later owner decision intentionally creates separate namespaces.

### Uniqueness rule

The database provides one authoritative conflict constraint for every claim that the active policy says participates in current-name conflict.

Exact PostgreSQL index/constraint syntax is implementation-owned, but application-only `check availability -> later insert` without authoritative database uniqueness is rejected.

Rename atomically changes current name claim/history with CharacterRevision. CharacterId does not change.

### 4.4 `character_build_core`

Typed child relation for profile-neutral build/profession linkage, conceptually including:

- CharacterId;
- current build/vocation definition reference where one exists;
- explicit pre-vocation/unselected state;
- promotion-achievement state/reference;
- build/ruleset definition revision;
- local child revision only if implementation evidence proves it useful.

The Character root revision remains the global stale-state fence for Character mutations.

Reference vocation names/titles are ruleset definitions, not physical engine-schema enum ordinals. Stable definition-key representation remains owned by the ruleset/content contract; DUR-02 consumes it rather than inventing a second definition identity system.

### 4.5 progression relations

The neutral core must support Character-owned authoritative progression facts without embedding unresolved arithmetic.

Recommended split:

- one typed relation for universally required scalar Character progression facts after their persisted-vs-derived classification is accepted by the owning ruleset;
- a separate typed skill-state relation family keyed by the accepted stable ruleset skill-definition key;
- additional typed child relations for modern progression systems only after their owning semantic/profile contract is accepted.

Architecture invariant:

```text
persisted authoritative fact
!= deterministic derived projection
```

DUR-02 does not persist duplicate representations merely because a formula is currently unknown unless the owning evidence/migration contract establishes that both values are independently authoritative.

Where target import/migration requires preserving a value that cannot safely be recomputed — capacity is the accepted example — the schema preserves that authoritative fact and its interpretation revision.

### Skill/profile extension boundary

The Reference eight-skill catalogue is accepted semantically, but exact advancement-state representation and stable definition-key encoding remain ruleset-owned.

Therefore this packet does **not** freeze either:

- one fixed eight-column skill table; or
- one opaque advancement-state blob.

A later physical skill extension must be typed, definition-keyed, revisioned and migration-safe.

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

use dedicated typed relation families or explicitly typed child aggregates after their physical contract is accepted.

Each extension declares:

- semantic owner;
- CharacterId relation;
- stable definition identity/key and its owner;
- schema/revision compatibility;
- transaction interaction with CharacterRevision;
- migration/rollback rules;
- retention/privacy rules where applicable;
- whether mutation must share the Character root transaction.

No extension receives a generic `type + JSON/blob payload` path merely because its final table has not yet been designed.

## 5. FND-04 persistence boundary

FND-04 authority state is physically separate from Character semantic state even though it references AccountId/CharacterId.

### 5.1 `account_presence_claim`

Keyed authoritatively by AccountId and records the game-domain account-global mandatory-presence Character relation required by FND-04.

It is an authority/exclusion relation, not a Character ownership mapping duplicate.

Requirements:

- one AccountId has at most one mandatory-presence Character;
- one CharacterId cannot simultaneously be claimed as mandatory presence for multiple accounts;
- current ownership is still revalidated against Character Authority state;
- it never substitutes for `character_root.account_id`;
- Character ownership never substitutes for current presence/control authority.

### 5.2 `character_lease`

Keyed by CharacterId and stores CharacterLease fencing state required for restart/failover safety, including at minimum:

- nonzero, monotonic, non-reused `character_lease_generation` or accepted equivalent;
- lease/control status required by FND-04;
- current holder/session/runtime-scope references where the accepted implementation contract requires them;
- restart-reconstructible freshness/expiry evidence sufficient to prove validity once numeric lease policy is accepted.

`character_lease_generation` is never CharacterRevision.

A stale lease generation can never renew, commit a controlled mutation or regain control.

Exact lease TTL/renew/safety intervals and their scalar representation remain deferred; no numeric schema constant is accepted here.

### 5.3 `game_session`

Durable continuity relation keyed by GameSessionId where required for FND-04 recovery.

It conceptually records:

- AccountId and CharacterId binding;
- session lifecycle/terminality state;
- current `connection_generation`;
- current CharacterLease generation reference/fence;
- exact binding revision set required by FND-04 recovery, including as applicable:
  - `protocol_major`;
  - `transport_profile`;
  - `ruleset_revision`;
  - `content_revision`;
  - `map_revision`;
  - `world_policy_revision`;
  - current RuntimeScopeAuthority / runtime owner generation evidence;
- session-scoped continuity fields only.

Actor-wide ControlLoss state is **not duplicated here**. It belongs to the separate `control_loss_continuity` authority below.

A terminal GameSessionId never revives.

GameSessionId is identity, not bearer proof.

### 5.4 `control_loss_continuity`

Typed actor-wide FND-04 continuity relation keyed by the accepted Character/actor continuity scope.

It stores restart-safe authority needed to preserve ControlLoss behavior, such as:

- non-reused ControlLossEpoch discriminator/ordinal or accepted equivalent;
- authoritative epoch origin;
- original same-session grace deadline where the accepted recovery policy requires it;
- protection eligibility/consumption state;
- exact accepted four-second protection activation/expiry evidence;
- protection re-arm state/deadline where applicable;
- relation to current/terminal GameSession only as reference/context, never as duplicate owner of actor-wide state.

Persisted deadlines are restart-stable and do not restart/extend because a process restarts.

Process-local monotonic timer values cannot be serialized as if they remain meaningful after restart. A later implementation contract must define a restart-stable trusted-time representation plus required clock-uncertainty/fail-closed behavior.

### 5.5 reconnect proof material

This packet does not freeze secret hashing/encryption/KMS representation because FND-04B explicitly leaves it deferred.

Required physical boundary only:

- secret/verifier material is separate from ordinary Character rows and analytics;
- never appears in plaintext logs/audit/telemetry;
- generation/predecessor fencing remains provable after permitted restart;
- exact storage/rotation is frozen by a later security/implementation contract before runtime enablement.

## 6. Idempotency and durable receipts

### 6.1 Character Authority operation receipts

Retryable cross-system Character mutations require durable operation identity and result reconciliation.

Recommended relation family: `character_operation_receipt`, keyed by ANL-owned `OperationId` for operations that need an independently durable retry identity.

It stores a bounded typed envelope such as:

- OperationId;
- operation family/kind;
- authenticated caller/semantic request fingerprint sufficient to detect conflicting reuse;
- target CharacterId where known;
- terminal/nonterminal operation state;
- bounded stable result category;
- resulting CharacterRevision where applicable;
- TransactionId for a committed atomic mutation where applicable;
- created/completed evidence timestamps.

It does not store arbitrary result JSON as the canonical operation contract.

Rules:

- same OperationId + same semantic request -> same logical operation/reconciliation result;
- same OperationId + conflicting request -> conflict, never overwrite/reinterpret;
- timeout is not success/failure proof;
- create retry before CharacterId exists resolves through OperationId to the one created CharacterId or stable terminal result;
- world/account transfer retry cannot apply the mutation twice.

### 6.2 persisted gameplay command dedup

Do **not** persist every gameplay CommandId universally merely because DUR-01 defines its scalar form.

Where a command crosses an ambiguous durable mutation boundary and FND-02/DUR requires durable command dedup, its identity is exactly:

```text
(GameSessionId, CommandId)
```

A durable receipt may store request fingerprint/result/TransactionId/revision as required. Equal numeric CommandId in another GameSession is a different command.

Retention is bounded and operation-owned; exact retention periods remain implementation/policy evidence.

### 6.3 TransactionId

Each logical atomic durable mutation transaction requiring ANL transaction evidence uses one stable TransactionId across ambiguous physical commit retry/reconciliation.

Database attempt IDs, WAL positions and local surrogate keys never replace TransactionId.

## 7. Transaction architecture

### 7.1 One Character mutation anchor

Every Character-owned durable mutation locks/revalidates `character_root` before changing Character-owned state.

This intentionally serializes durable mutation **per Character**, matching the accepted single CharacterRevision fence. It does not serialize unrelated characters globally.

### 7.2 Account-scoped operations

Every lifecycle/ownership operation whose policy may change quota eligibility acquires the relevant `account_character_guard` before evaluating portfolio state.

For transfer between two AccountIds:

1. acquire both account guards in canonical full-AccountId byte order;
2. revalidate current Character owner;
3. acquire/validate Character root;
4. evaluate destination and source policy under the active policy revision;
5. revalidate required quiescence/presence/lease state;
6. commit owner rebinding + CharacterRevision + receipt + mandatory audit atomically.

This prevents opposing transfer/create/restore/lifecycle races without relying on a drift-prone counter.

### 7.3 Name operations

Create/rename:

- compute canonical key under the explicit active naming-policy revision outside database collation semantics;
- rely on authoritative database uniqueness over the complete key;
- never treat advisory `check availability -> later insert` as correctness;
- atomically bind name claim/history with Character mutation/receipt/audit.

Same-name races produce one database-authoritative winner.

### 7.4 Quiescent high-impact operations

Stage A remains binding: terminal retirement, world transfer and account ownership transfer require actor `ABSENT` and no current playable CharacterLease before commit in the first native architecture.

DUR-02 locks/revalidates relevant presence/lease rows at the final transaction boundary rather than trusting a stale earlier precheck.

### 7.5 Death and item/economy split

DUR-02 may define the Character-owned progression consequence transaction shape, but it does **not** decide item/corpse/value conservation.

Before a Reference death path that changes both Character progression and items is implemented, `GAME-ITEM-01`/`DUR-03` must define whether those changes share one PostgreSQL transaction coordinator or another proven atomic/reconciliation boundary.

This packet does not create a silent partial-success path.

## 8. Isolation, locks and retries

### Recommended default

PostgreSQL `READ COMMITTED` is acceptable only with **explicit locked authority anchors + database constraints** that close every correctness-sensitive anomaly for that operation.

Examples:

- Character root row lock -> per-Character mutation serialization/revision;
- account guard row lock -> portfolio/quota serialization;
- authoritative unique constraint -> name conflict;
- presence/lease row lock + generation compare -> stale authority rejection;
- operation/command unique identity -> idempotency conflict.

An operation whose invariant cannot be proven under this model must either:

- introduce a dedicated accepted lock/constraint anchor; or
- use PostgreSQL `SERIALIZABLE` for that bounded transaction with stable same-operation retry/reconciliation.

`READ COMMITTED` without an explicit anomaly proof is not accepted by default merely because it is PostgreSQL's default isolation.

### Advisory locks

PostgreSQL advisory locks may be a performance/coordination supplement after evidence. They are never the sole durable authority for Character ownership, name uniqueness, quotas, presence or lease fencing.

### Deterministic lock ordering

Within one transaction, same-class multi-entity locks are acquired in canonical full-identity byte order.

Cross-class ordering is:

```text
account portfolio guard(s)
-> Character root(s)
-> FND-04 presence / lease / session rows required by the operation
-> existing name claim/history rows where row locks are required
-> typed Character child rows in stable definition-key order
-> operation / audit / publication-state inserts
```

A new name-key claim may race through the unique constraint rather than attempting to lock a nonexistent row.

No implementation reverses this order for convenience without an explicit deadlock-safety proof and architecture review.

### Retry rule

Serialization failures, deadlocks, lost responses and ambiguous commit outcomes retry/reconcile with the **same semantic operation identity**.

A new database attempt does not mint a new OperationId/TransactionId for the same logical operation.

Retry count/backoff numbers remain implementation/performance policy.

## 9. Immutable durable audit journal and publication state

### 9.1 Reject mutable outbox-as-audit-only design

A mutable outbox row that is overwritten/deleted after publication cannot simultaneously be the canonical long-lived critical audit record.

### 9.2 Recommended split

Use two relation families.

#### `durable_event_journal`

Canonical retained evidence carrying the ANL-01 event record, including:

- EventId;
- registered event type/schema revision;
- durability/privacy/retention profile references;
- immutable trusted event timestamp/context;
- OperationId/TransactionEventRef/Correlation/Causation/context where applicable;
- applicable ruleset/content/domain revisions;
- **exact registered payload bytes**;
- payload SHA-256;
- Character/domain revision linkage where the event family requires it.

While an event is retained, same EventId cannot be updated to different semantic content or payload bytes.

Retention expiry, privacy erasure or legally required removal may remove/redact data only through its separately accepted privacy/retention lifecycle. Such a lifecycle action must be audited and must not silently rewrite one retained EventId into different semantic content.

#### `event_publication_state`

Mutable delivery state keyed/referencing EventId, used for:

- pending/published/retry/quarantine state;
- broker/transport attempt metadata;
- next-attempt timing;
- delivery checkpoint/error bookkeeping.

Mutable delivery metadata is not authoritative gameplay/audit content.

### 9.3 Atomicity

For each Character mutation requiring durable audit:

```text
Character current-state mutation
+ CharacterRevision advance
+ operation/command receipt where required
+ every mandatory durable_event_journal row
+ publication-state enqueue record
commit in one PostgreSQL transaction
```

If mandatory journal/enqueue evidence cannot commit, the Character mutation does not become authoritative.

Best-effort telemetry is excluded from this atomic transaction and cannot block gameplay.

### 9.4 Publication/replay

- publisher reads committed publication state only;
- delivery is at-least-once;
- EventId deduplicates consumer effects;
- publication retry never reconstructs event bytes from later mutable Character state;
- replay reads evidence/projections only and cannot resubmit Character mutations.

## 10. Current state versus checkpoints

### 10.1 Current-state relations are canonical Character durability

Do not create a second generic serialized Character snapshot as a parallel source of truth.

Committed root + typed Character-owned relations at a CharacterRevision are the authoritative durable Character state.

### 10.2 Checkpoint manifest when runtime domains need one

If runtime/profile systems later require a consistent recoverable checkpoint beyond normalized current-state rows, use a typed checkpoint manifest conceptually containing:

- CharacterId;
- checkpoint/CharacterRevision boundary;
- applicable ruleset/content/map/world-policy revisions;
- runtime scope/ownership evidence where required;
- references to **typed owner-specific checkpoint components**.

The manifest cannot contain an arbitrary generic state payload. Each component requires an accepted typed schema/owner/migration contract.

### 10.3 No acknowledged-success-before-commit

A Character mutation success response is never authoritative before the owning PostgreSQL transaction commits.

A lost success response is an ambiguous result reconciled from durable operation/command receipt + current state; the semantic mutation is not blindly repeated.

This is a logical commit/ack invariant, not a numeric disaster-recovery RPO promise.

## 11. Restart, crash and disaster restore

### 11.1 Ordinary process crash/restart

Committed Character state, CharacterRevision, operation receipts, mandatory audit journal and required FND-04 continuity/fence state must be reconstructible from PostgreSQL before authority resumes.

In-memory caches/Redis cannot reconstruct authority by themselves.

### 11.2 No authority resurrection

Restart/failover may never:

- reset CharacterRevision;
- reset/reuse CharacterLease generation;
- revive a terminal GameSession;
- reset connection generation;
- restart same-session grace/protection deadlines;
- reuse ControlLossEpoch entitlement;
- reapply an already committed operation.

If current authority cannot be proven, admission/mutation fails closed or uses the accepted fresh/recovery path.

### 11.3 Point-in-time/disaster restore

A database restored to an older point cannot safely assume pre-restore sessions/leases remain current simply because restored rows exist.

Before restored data may serve gameplay authority, the operational restore contract must:

1. keep admission/authoritative mutation closed during reconciliation;
2. establish a strictly newer non-rollback recovery/authority fence outside any value that could itself have rolled back with the restored snapshot, or prove an equivalent mechanism;
3. invalidate/fence pre-restore TransportBinding/session/lease authority that cannot be proven current;
4. reconcile Platform security/account state and current world/routing revisions;
5. verify CharacterRevision/name/operation/audit/publication integrity at the restored cut;
6. publish/replay only committed audit/outbox evidence and never replay gameplay commands;
7. open traffic only after restore validation passes.

The exact storage/issuer for the recovery-generation fence is a later DUR/OPS/security decision. This packet freezes **no authority resurrection**, not its final implementation.

### 11.4 RPO/RTO

DUR-02 requires:

- PostgreSQL backup + WAL/PITR capability appropriate to production topology;
- automated restore verification;
- integrity checks covering Character root/children, name registry, presence/leases/sessions, operation receipts and audit/publication state;
- recorded exact backup/restore artifact/revision evidence.

Numeric production RPO/RTO targets remain OPS/PERF/product-milestone decisions and are not guessed here.

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

Ruleset/profile/content definition changes that alter persisted interpretation require explicit source/destination revisions and deterministic migration/compatibility evidence.

A revision change alone does not silently reinterpret existing Character facts.

### 12.4 Migration properties

- migration IDs/revisions never reused;
- backfills are restartable, idempotent and bounded;
- partial migration has explicit resumable state;
- constraints become authoritative only after data validation;
- incompatible old writers are fenced before destructive contract phase;
- rollback order is documented before cutover;
- CharacterId/domain identities do not change because storage representation changes;
- no migration creates alternate Character identities for retry convenience.

### 12.5 Definition-key evolution

Profile extensions referencing skill/vocation/weapon/charm/etc definitions retain stable definition identity or an explicit deterministic mapping across incompatible revisions.

Database row position or enum ordinal is never a durable definition identity.

## 13. Foreign keys, deletion and privacy

### 13.1 Internal referential integrity

Game-owned typed child relations should use CharacterId referential integrity where both sides share game migration authority.

Exact FK deferrability/cascade syntax remains implementation-owned.

### 13.2 No semantic cascade delete

Ordinary lifecycle retirement is a state transition, not a physical `DELETE CASCADE` operation.

A child row does not disappear merely because lifecycle becomes RETIRED unless its semantic/retention contract explicitly requires removal.

### 13.3 CharacterId non-reuse

Physical cleanup can never make a retired CharacterId reusable. Sufficient tombstone/provenance evidence remains to prevent reuse and reconcile audit/import references.

### 13.4 Privacy erasure is separate

Privacy deletion/anonymization may later redact/remove eligible player-linked fields under `DATA-PRIVACY-01`, but it must not be modelled as Character identity reuse or implicit deletion of mandatory security/audit evidence.

Name history/alias retention and public exposure require explicit privacy/retention policy before production.

## 14. Index and query intent

Exact indexes are implementation-owned, but architecture requires efficient authoritative access paths for:

- CharacterId root lookup;
- current Characters by AccountId + lifecycle/policy eligibility;
- current Characters by WorldId where game operations need it;
- complete canonical name-key conflict lookup;
- current CharacterLease by CharacterId;
- AccountPresenceClaim by AccountId and uniqueness of claimed CharacterId;
- GameSession by GameSessionId and current Character where recovery requires it;
- OperationId receipt reconciliation;
- `(GameSessionId, CommandId)` durable dedup where implemented;
- pending event publication without scanning full audit history;
- authorized audit lookup by EventId/TransactionId/CharacterRevision.

Rules:

- authoritative equality uses complete identities/keys;
- UUIDv7 order may improve locality but never defines chronology;
- partial/hash-only indexes may accelerate lookup but cannot replace full equality verification;
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
| account quota/lifecycle race | serialized under account guard; no invalid portfolio commit |
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
- application architecture does not depend on manual raw SQL for normal Character correction;
- support/GM mutations eventually use typed audited domain commands.

## 17. Implementation evidence required later

This packet is paper-only. Future DUR-02 implementation claiming conformance must prove at least:

### Identity and constraints

- full UUID round trips for every implemented identity;
- full CommandId numeric range where persisted;
- no cross-semantic ID substitution;
- CharacterId non-reuse;
- canonical name-key uniqueness race;
- naming-policy migration detects destination collisions before cutover.

### Revision/fencing/concurrency

- stale CharacterRevision rejection;
- stale lease/session generation rejection;
- two concurrent Character mutations produce one serialized revision order;
- create/restore/deletion/account-transfer portfolio races cannot violate accepted quota policy;
- opposing account transfers and rename/transfer races terminate without split ownership/deadlock corruption;
- deadlock/serialization retry retains semantic operation identity.

### Idempotency

- duplicate create retry creates one Character;
- rename/delete/restore/world/account-transfer ambiguous-response retry applies one semantic mutation;
- same OperationId conflicting payload fails closed;
- durable command duplicate cannot double-apply a mutation.

### Audit/outbox

- mutation + mandatory exact audit bytes + publication enqueue are atomic;
- crash after commit/before publish redelivers same EventId/bytes;
- duplicate publish yields one consumer effect;
- same EventId conflicting retained content fails integrity checks;
- publication backlog cannot be discarded for capacity;
- replay cannot mutate gameplay;
- privacy/retention lifecycle cannot silently rewrite retained EventId semantics.

### Crash/recovery

- restart reconstructs CharacterRevision/lease/session/ControlLoss continuity without timer reset;
- actor-wide ControlLoss state has one authority and is not duplicated across session rows;
- complete FND-04 binding revision set is revalidated on recovery;
- stale transport cannot regain authority;
- lost commit response reconciles from durable state;
- terminal GameSession cannot revive.

### Migration/restore

- expand/backfill/validate/cutover/contract fixture;
- interrupted backfill resumes idempotently;
- incompatible writer is fenced before contract phase;
- restore drill verifies Character/name/receipt/audit/publication integrity;
- PITR/restore cannot resurrect pre-restore session/lease authority;
- rollback/recovery evidence is retained.

### Privacy/access

- Platform write credentials are rejected from game Character tables;
- public/read projection cannot expose unauthorized AccountId-to-character relation;
- a pseudonymous analytics family cannot silently fall back to raw CharacterId/AccountId; restricted player-linked audit remains governed by its explicit privacy class.

## 18. Decision package

### RECOMMENDATION — NOT OWNER-ACCEPTED

Accept the following as the minimum DUR-02 profile-neutral Character persistence architecture:

1. **Normalized current-state architecture**, not full event sourcing: `character_root` is the Character identity/lifecycle/ownership/global-revision lock anchor; typed child relations hold physically distinct state.
2. **One global CharacterRevision** advances once per committed Character-owned transaction and is independent from FND-04 lease/session/runtime generations.
3. **Game-owned AccountId guard rows** serialize every quota-sensitive portfolio/lifecycle operation without becoming Account authority or a second active-count truth.
4. **Separate global name registry/history** stores the complete domain-generated canonical key + naming-policy revision and relies on database uniqueness; DB collation never invents canonicalization, and a naming-policy migration must prove collision-free destination keys before cutover.
5. **FND-04 authority relations remain separate**: AccountPresenceClaim, CharacterLease generation, GameSession/connection generation and actor-wide ControlLoss continuity are physically distinct from Character semantic revision/state and from one another.
6. **Typed profile extensions only**: dedicated child relations/aggregates for accepted Character-specific systems; no generic JSON/KV/EAV misc-state escape hatch.
7. **Durable operation receipts** use OperationId for retryable Character Authority workflows; persisted `(GameSessionId, CommandId)` dedup exists only where a durable gameplay command boundary actually requires it.
8. **Transaction model** serializes each Character mutation through the root, uses account guards for every quota-affecting portfolio/lifecycle operation, revalidates presence/lease at commit for quiescent high-impact operations, and relies on authoritative constraints for name/idempotency races.
9. **Isolation policy** uses explicit lock/constraint proofs; `READ COMMITTED` is acceptable only when those anchors close the anomaly, otherwise bounded `SERIALIZABLE` + same-operation retry is required. Advisory locks are never sole authority.
10. **Audit architecture** separates retained immutable `durable_event_journal` semantics from mutable publication state; mandatory audit/journal/enqueue commits atomically with the Character mutation while best-effort telemetry stays asynchronous. Privacy/retention lifecycle is separately governed and audited.
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
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
Accepted scope       = profile-neutral Character persistence architecture
Runtime authority    = NONE
```

DDL/migrations remain **NOT AUTHORIZED** by architecture acceptance.

Acceptance would unblock a separately authorized implementation-design/package for the profile-neutral Character persistence core and provide a stable consumer contract for later profile extensions.

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
- security/privacy/restore evidence requiring a stronger fence or data-separation model;
- an explicit later architecture decision superseding ADR-0004's Persistence-v1 direction.

Convenience, ORM defaults, current Global schema, Canary/crystalserver tables or generic JSON flexibility are not sufficient supersession evidence.

## 21. Deliberately not decided

- exact SQL table/column/index/constraint names;
- exact PostgreSQL schema namespace names;
- exact migration framework/library;
- ORM/query builder or Rust database crate;
- connection-pool technology/settings;
- exact scalar representation of CharacterRevision/lease/session generations where accepted semantics allow equivalent non-reused representations;
- exact stable ruleset/content definition-key scalar representation where its owner has not frozen it;
- profile-specific progression child table layouts;
- item/currency/market/house schema;
- exact PostgreSQL partitioning/sharding strategy;
- exact operational retention/backup/RPO/RTO values;
- exact retry/backoff limits;
- reconnect-secret hashing/KMS representation;
- exact non-rollback disaster-recovery fence implementation/issuer;
- production deployment topology;
- runtime implementation.

Until the owner accepts or modifies section 18, this document remains **PRE-DECISION ARCHITECTURE / NOT ACCEPTED** and `DUR-02` remains `PROPOSED / PLANNED / NOT_STARTED`.
