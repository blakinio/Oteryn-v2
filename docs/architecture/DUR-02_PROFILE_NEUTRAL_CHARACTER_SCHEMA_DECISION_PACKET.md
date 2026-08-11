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

Accepted GAME-CHAR answers **what Character semantics must be durable**. DUR-02 must answer **how the profile-neutral core is physically structured and transactionally protected** without allowing persistence convenience to become gameplay policy.

```text
accepted semantic ownership
-> choose relation / transaction / fencing architecture
-> preserve typed extension points
-> keep unresolved profile/ruleset values outside schema invariants
-> later implementation proves SQL / migration / runtime behavior
```

### Must this architecture be decided now?

**YES.** It blocks final paper-only Character persistence architecture, native Character Authority implementation planning, FND-04 admission/recovery persistence integration, mandatory audit/outbox design, migration/restore architecture and VSL-PERSISTENCE-01 planning.

### Must SQL DDL or every profile child table be decided now?

**NO.** Freeze relation ownership, keys, fences, authority transitions, lock order, migration discipline and typed extension rules. Exact SQL names/syntax, migration library, connection pool and profile-specific child schemas remain implementation or owning-profile work.

## 2. Accepted constraints

### Database ownership

- authoritative native game persistence targets PostgreSQL;
- game and Platform use separate logical databases, owners, credentials and migration histories;
- no cross-database foreign keys;
- Platform never directly mutates native Character tables;
- Character Authority is the semantic writer for Character lifecycle/ownership/name/progression/build state.

### Identity representation

Native UUIDv7 identities persist as PostgreSQL `uuid`, full 128 bits, nil invalid and no semantic reuse. Persisted `CommandId` preserves the full FND-02 nonzero uint64 range as `numeric(20,0)` in `(GameSessionId, CommandId)` scope. UUID ordering is never semantic chronology/revision/authority.

### Independent fences

```text
CharacterRevision
!= CharacterLease generation
!= GameSessionId
!= connection_generation
!= RuntimeScopeAuthority ownership generation
```

Every durable Character-owned mutation validates Character state/revision. FND-04 independently validates session/lease/transport/runtime authority.

### Durable audit

For a mutation requiring durable audit:

```text
authoritative mutation + mandatory durable audit evidence
commit together
OR
neither is authoritative
```

Publication is at-least-once. Event replay never replays gameplay mutation. Same EventId retains the same semantic event and exact payload bytes while retained.

### Profile-neutral boundary

Accepted GAME-CHAR forbids:

- current Global/OTS behavior becoming unresolved July-28 truth;
- one universal PvP/death profile;
- an untyped JSON/KV miscellaneous-state bag;
- claiming one core schema complete for every future profile.

## 3. Options considered

### A — one wide Character row

**Rejected.** It couples unrelated state/lifecycles, creates nullable migration churn, mixes Character and FND-04 authority and undermines typed child aggregates.

### B — generic EAV/JSON state

**Rejected.** It weakens constraints/ownership/migrations and becomes a bypass around future semantic gates.

### C — event sourcing as Character source of truth

**Rejected for Persistence v1.** ADR-0004 chooses current-state tables + revisions + idempotent operations + transactional outbox + bounded audit. ANL events remain evidence, not gameplay authority.

### D — normalized current-state core + typed child relations/extensions

**RECOMMENDED.** One root/revision anchor, separate name and FND-04 authority relations, typed children, durable receipts, immutable audit journal plus mutable publication state, and explicit profile extension boundaries.

## 4. Profile-neutral Character relation map

Logical names below explain architecture; they are not final SQL identifiers.

### 4.1 `character_root`

One row per CharacterId containing only profile-neutral root facts:

- CharacterId;
- current owner AccountId (external reference, no cross-DB FK);
- current WorldId;
- lifecycle `ACTIVE | DELETION_SCHEDULED | RETIRED`;
- monotonic CharacterRevision;
- active profile/ruleset interpretation revision references required to interpret Character state;
- creation/starter context revision references required for deterministic interpretation/migration;
- accepted lifecycle timestamps/evidence where policy requires them.

It does **not** own items/currency, quest aggregates, Platform entitlements, lease/session generations, generic extension JSON or exact Reference arithmetic.

#### CharacterRevision

Every committed Character-owned semantic mutation:

1. locks/revalidates `character_root`;
2. validates expected CharacterRevision when the operation uses optimistic expected state;
3. rejects/reconciles stale state;
4. advances CharacterRevision exactly once for that Character transaction;
5. records resulting revision in durable receipt/audit evidence.

Several typed child rows may change in the same transaction; the global CharacterRevision advances once. It is never derived from UUID order, DB transaction ID, wall clock, EventId or lease generation.

### 4.2 `account_character_guard`

A game-owned lock anchor keyed by AccountId.

It serializes every account-scoped Character operation whose correctness depends on portfolio state, including whenever policy can change quota eligibility:

- create;
- schedule deletion;
- restore/cancel deletion;
- terminal retirement/finalization;
- account ownership transfer;
- any later quota-affecting lifecycle transition.

It is **not** Account authority, Platform security state or an authoritative active-count cache.

The authoritative portfolio result is derived from current Character Authority rows under the guard and the active lifecycle/quota policy revision.

An `active_count` cache is not authoritative unless a later evidence-backed superseding design proves transactional counter + reconciliation invariants.

Multi-account operations lock account guards in canonical full-AccountId byte order.

### 4.3 `character_name_registry`

Separate relation family owning:

- display name;
- complete lossless canonical comparison key;
- naming-policy revision;
- `CURRENT | FORMER_ALIAS | RESERVED` semantic class;
- CharacterId relation;
- policy-owned effective/release evidence.

The game domain computes canonical keys under the accepted naming policy. PostgreSQL enforces equality/uniqueness over the complete result; database collation never invents semantic normalization. Hashes may accelerate lookup but never replace complete-key verification.

#### Naming-policy revision cutover

A global namespace cannot have two simultaneously authoritative canonicalization universes that disagree on equality.

Before destination policy cutover:

1. recompute destination keys for every conflict-participating live/reserved claim;
2. detect and resolve/abort every new collision;
3. validate destination uniqueness;
4. compatibly cut readers/writers to the destination policy;
5. retain old-policy evidence/history only as non-authoritative history after cutover.

Authoritative uniqueness cannot be partitioned by policy revision merely to hide conflicts unless a later owner decision intentionally creates separate namespaces.

Application-only `check availability -> later insert` is not correctness. Database uniqueness decides simultaneous name races.

### 4.4 `character_build_core`

Typed child relation for profile-neutral build linkage:

- CharacterId;
- stable ruleset-owned vocation/build definition reference where one exists;
- explicit pre-vocation/unselected state;
- promotion-achievement state/reference;
- build/ruleset definition revision.

CharacterRevision remains the global fence. Reference vocation strings/ordinals are not universal engine-schema enums. Stable definition-key representation is consumed from the ruleset/content owner rather than reinvented here.

### 4.5 progression and skill relations

Use typed relations only after the owning ruleset determines persisted facts versus deterministic projections.

```text
persisted authoritative fact
!= deterministic derived projection
```

Recommended shape:

- typed scalar progression relation for universally required persisted Character facts after their status is accepted;
- typed skill relation keyed by accepted stable skill-definition key;
- dedicated typed children for later accepted progression systems.

Do not persist duplicate values merely because a formula is unknown unless evidence establishes both are independently authoritative.

Migration-sensitive facts that cannot safely be recomputed — capacity is the accepted example — preserve the authoritative value plus interpretation revision.

The first Reference eight-skill catalogue is accepted semantically, but this packet freezes neither a fixed eight-column table nor an opaque skill-advancement blob. Physical skill state remains typed, definition-keyed, revisioned and migration-safe.

### 4.6 typed Character-owned profile extensions

Weapon Proficiency, charms, Hunting Tasks, permanent Prey/Hunting slots, Wheel/Promotion Points, Animus and future profile-specific Character facts use dedicated typed relation families/child aggregates after their physical contracts are accepted.

Every extension declares:

- semantic owner;
- CharacterId relation;
- stable definition key and owner;
- schema/definition revision compatibility;
- CharacterRevision interaction;
- transaction/lifecycle boundary;
- migration/rollback;
- privacy/retention where applicable.

No generic `type + JSON/blob` persistence path is allowed as a temporary ownership escape hatch.

## 5. FND-04 authority persistence boundary

FND-04 authority state is physically distinct from Character semantic state.

### 5.1 `account_presence_claim`

Authoritatively keyed by AccountId and enforcing game-domain mandatory-presence exclusion.

Requirements:

- one AccountId has at most one mandatory-presence Character;
- one CharacterId cannot simultaneously be claimed by multiple accounts;
- current AccountId->CharacterId ownership is still revalidated against Character Authority;
- presence claim never substitutes for `character_root.account_id`;
- Character ownership never substitutes for presence/control authority.

### 5.2 `character_lease`

Keyed by CharacterId and storing restart-reconstructible lease fencing:

- nonzero monotonic non-reused CharacterLease generation or accepted equivalent;
- current lease/control state;
- holder/session/runtime-scope references required by FND-04;
- restart-reconstructible lease freshness/expiry evidence once numeric lease policy is accepted.

Lease generation is never CharacterRevision. Stale generation cannot renew, commit controlled mutation or regain control. Exact TTL/renew/safety numbers and scalar representation remain deferred.

### 5.3 `game_session`

Keyed by GameSessionId when durable recovery continuity requires it.

Stores only session-scoped truth:

- AccountId + CharacterId binding;
- session lifecycle/terminality;
- current `connection_generation`;
- current CharacterLease generation fence/reference;
- FND-04 recovery binding revision set as applicable:
  - protocol_major;
  - transport_profile;
  - ruleset_revision;
  - content_revision;
  - map_revision;
  - world_policy_revision;
  - current RuntimeScopeAuthority / runtime owner generation evidence;
- reconnect-proof/candidate metadata references where the accepted security implementation requires them.

Actor-wide ControlLoss state is **not duplicated in GameSession**. A terminal GameSessionId never revives. GameSessionId is identity, never bearer proof.

### 5.4 `control_loss_continuity`

Single actor-wide owner for restart-safe ControlLoss state:

- non-reused ControlLossEpoch discriminator/ordinal or equivalent;
- authoritative epoch origin;
- original same-session grace deadline where applicable;
- protection eligibility/consumption;
- accepted four-second protection activation/expiry;
- protection re-arm state/deadline where applicable;
- references to current/terminal GameSession only as context.

Deadlines survive restart/failover without restart/extension. Process-local monotonic timer values cannot be serialized as restart-stable time; later implementation must define trusted restart-stable deadline representation and uncertainty behavior.

### 5.5 reconnect proof material

Exact hash/encryption/KMS is deferred by FND-04B. The physical boundary requires secret/verifier material to remain separate from ordinary Character rows/analytics, absent from plaintext logs/audit, predecessor-fenced across generations and frozen by a later security implementation contract before runtime enablement.

### 5.6 atomic fresh-admission authority commit

Fresh admission is one database authority linearization boundary, not a sequence of independently authoritative row writes.

Prechecks may be performed earlier for fail-fast behavior, but immediately before/atomically with final authority creation the transaction revalidates the accepted FND-04A mutable facts, including at least:

- current AccountId->CharacterId ownership/lifecycle;
- current CharacterId->WorldId eligibility;
- AccountPresence incumbent state;
- CharacterLease/current generation state;
- current runtime owner/RuntimeScopeAuthority generation/readiness;
- protocol/transport/ruleset/content/map/world-policy/offer compatibility inputs required by the admission contract;
- GrantNonce eligibility and any mutable authenticated security/trust evidence whose final validation belongs at commit.

Only successful commit atomically:

```text
consumes GrantNonce
+ establishes/advances AccountPresenceClaim
+ establishes/acquires CharacterLease generation
+ creates canonical GameSessionId
+ marks GameSession ACTIVE
+ sets connection_generation = 1
+ establishes initial authoritative session/reconciliation boundary
```

Failure creates **none** of those candidate authority effects. Candidate/precommit GameSessionId is never reused after failure.

Success becomes externally visible only after commit.

The physical GrantNonce/security-evidence relation layout remains owned by FND/security implementation; DUR-02 freezes the atomicity requirement and required same-transaction revalidation, not their exact tables here.

### 5.7 reconnect/recovery PREPARE persistence

ReconnectAttemptRef is idempotency/correlation, not authority.

PREPARE needs a bounded typed candidate relation or equivalent durable state that binds at least:

```text
GameSessionId
ReconnectAttemptRef
predecessor connection_generation
strict-successor candidate connection_generation
exact authenticated candidate transport/binding reference
proof class
finite prepared deadline
candidate reconnect-proof metadata/reference where used
PREPARED disposition/reconciliation evidence
```

PREPARE grants **zero** gameplay/liveness/fencing authority and does not advance current connection generation.

Same eligible PREPARE retry returns/reconciles the same logical candidate rather than minting independent successor authority. Abort/expiry/supersession permanently invalidates candidate proof/state.

Prepared candidate resources are bounded; exact limits are registry/implementation values.

### 5.8 reconnect/recovery atomic COMMIT

Reconnect/recovery authority changes only at COMMIT.

The COMMIT transaction locks/revalidates the current GameSession/lease/presence/candidate authority and the accepted mutable security/revision facts immediately before switch, including:

- candidate exists, unexpired and matches exact session/attempt/candidate transport;
- predecessor connection generation still matches PREPARE source;
- session remains reconnect-eligible and original grace remains valid for same-session path;
- no healthy current controller regained authority;
- AccountPresenceClaim still denotes same CharacterId;
- CharacterLease remains current/compatible;
- RuntimeScopeAuthority owner/generation/placement remains current;
- FND-02 reconciliation boundary is safe;
- no newer handoff/takeover/fence/terminal transition supersedes candidate;
- proof-specific mutable security/trust/nonce/revision facts remain current.

Only successful COMMIT atomically:

```text
fences predecessor TransportBinding authority
+ advances/makes candidate connection_generation current
+ binds command/liveness/reconciliation authority to candidate transport
+ activates candidate successor reconnect proof and invalidates predecessor proof where applicable
+ preserves GameSessionId for same-session reconnect
+ preserves actor/gameplay state and domain revisions
+ records re-entry for current ControlLossEpoch
+ activates exact 4s protection only when that epoch has eligible unused entitlement
+ consumes RecoveryGrantNonce only when the successful path requires it
+ records stable ReconnectAttempt disposition for lost-response reconciliation
```

Failure does **not** advance generation, revive predecessor, consume nonce as success, activate proof/protection or roll authority back to PREPARE-time observations.

Lost COMMIT response reconciles from the persisted attempt/current-generation authority; it never performs a second switch.

### 5.9 post-grace recovery with new GameSession

If old GameSession is terminal but the same actor remains `PRESENT_UNCONTROLLED`, accepted post-grace recovery creates a **new** GameSessionId at one atomic boundary while preserving actor state.

The transaction revalidates ownership/world/presence/lease/runtime/recovery evidence and only on success:

```text
creates new GameSessionId
+ connection_generation = 1
+ establishes new current reconnect proof/transport authority
+ consumes required RecoveryGrantNonce
+ restores playable control to the same actor
+ preserves eligible existing ControlLossEpoch semantics without inventing a new epoch
```

It does not respawn/heal/refill/teleport/reset conditions/cooldowns/combat/threat/aggro or reuse the terminal GameSessionId.

## 6. Idempotency and durable receipts

### 6.1 Character Authority operation receipts

Retryable cross-system Character mutations use a durable OperationId receipt when an operation needs independent retry identity.

A bounded typed `character_operation_receipt` records:

- OperationId;
- operation kind;
- authenticated caller/semantic request fingerprint;
- CharacterId where known;
- terminal/nonterminal operation state;
- bounded stable result category;
- resulting CharacterRevision where applicable;
- TransactionId for committed atomic mutation where applicable;
- evidence timestamps.

No arbitrary result JSON is canonical.

Rules:

- same OperationId + same semantic request -> same logical operation/result reconciliation;
- same OperationId + conflicting request -> conflict;
- timeout is not proof of success/failure;
- create retry before CharacterId is known resolves to the one CharacterId or stable terminal result;
- world/account transfer retry cannot apply twice.

### 6.2 persisted gameplay command dedup

Do not persist every CommandId universally.

Where FND-02/DUR requires durable dedup across an ambiguous commit boundary, identity is exactly:

```text
(GameSessionId, CommandId)
```

A receipt may carry request fingerprint/result/TransactionId/revision as needed. Equal numeric CommandId in another GameSession is distinct. Retention remains bounded and operation-owned.

### 6.3 TransactionId

Each logical atomic durable mutation requiring ANL transaction evidence uses one stable TransactionId across ambiguous physical commit retry/reconciliation. DB attempt IDs/WAL positions/local surrogates never replace it.

## 7. Character transaction architecture

### 7.1 one Character mutation anchor

Every Character-owned durable semantic mutation locks/revalidates `character_root` first. This serializes durable mutation **per Character** in accordance with one CharacterRevision; unrelated characters remain independent.

FND-04-only authority transitions do not increment CharacterRevision unless they also mutate Character semantic state.

### 7.2 account-scoped operations

Every lifecycle/ownership operation whose policy may alter portfolio eligibility acquires `account_character_guard` before portfolio evaluation.

Account transfer:

1. lock both account guards in canonical order;
2. revalidate current owner;
3. lock/revalidate Character root;
4. evaluate source/destination policy;
5. revalidate required ABSENT/no-playable-lease state;
6. commit AccountId rebinding + CharacterRevision + receipt + mandatory audit atomically.

### 7.3 name operations

Create/rename compute canonical key under the active naming policy outside DB collation, rely on full-key DB uniqueness, and atomically bind claim/history with Character mutation/receipt/audit. Simultaneous name races have one DB-authoritative winner.

### 7.4 quiescent high-impact operations

Stage A remains binding: terminal retirement, world transfer and account ownership transfer require actor `ABSENT` and no current playable CharacterLease in the first architecture. The final transaction locks/revalidates presence/lease instead of trusting a stale precheck.

### 7.5 death/item split

DUR-02 may define the Character progression consequence shape but does not decide item/corpse/value conservation. `GAME-ITEM-01`/`DUR-03` must later prove the cross-domain atomic/reconciliation boundary before a death path that changes both Character and items can be implemented. No silent partial success is accepted.

## 8. Isolation, locks and retries

### Recommended default

`READ COMMITTED` is acceptable only with **explicit authority anchors + DB constraints** closing every correctness-sensitive anomaly for that operation.

Examples:

- Character root lock -> per-Character revision order;
- account guard -> quota/portfolio serialization;
- unique canonical key -> name conflict;
- presence/lease locks + generation compare -> authority conflict;
- unique OperationId / durable command identity -> idempotency.

If an invariant cannot be proven under this model, add an accepted lock/constraint anchor or use bounded PostgreSQL `SERIALIZABLE` with same-operation retry/reconciliation.

PostgreSQL default isolation is not itself a correctness proof.

Advisory locks may supplement performance/coordination but are never sole authority.

### Lock ordering

Same-class multi-entity locks use canonical full-identity byte order.

Cross-class order for Character-domain transactions:

```text
account portfolio guard(s)
-> Character root(s)
-> FND-04 presence / lease / session rows required for final revalidation
-> existing name rows where row locks are needed
-> typed Character child rows in stable definition-key order
-> receipts / audit / publication inserts
```

Fresh-admission/reconnect transactions follow their own FND-04 authority-row order but must remain consistent with any Character root revalidation they perform; implementation must publish one executable lock-order matrix before SQL code is accepted.

A new unique name claim may race on the unique constraint instead of locking a nonexistent row.

Retries after serialization/deadlock/lost response retain the same semantic OperationId/TransactionId. Retry count/backoff numbers remain downstream.

## 9. Durable audit journal and publication state

A mutable outbox row cannot simultaneously be the retained canonical audit record.

### `durable_event_journal`

Stores retained ANL semantic evidence such as EventId, event/schema/profile references, trusted timestamp/context, correlation/causation/operation/transaction links, applicable domain revisions, **exact registered payload bytes**, payload SHA-256 and required CharacterRevision linkage.

While retained, same EventId cannot be rewritten to different semantic content/payload bytes.

Accepted retention/privacy lifecycle may remove/redact data only through a separately governed/audited lifecycle and may not silently rewrite one retained EventId into different semantics.

### `event_publication_state`

Separate mutable state keyed by EventId for pending/published/retry/quarantine status, attempt metadata, retry timing and delivery errors/checkpoints. It is not gameplay/audit truth.

### Atomicity

For each mutation requiring durable audit:

```text
current-state mutation
+ CharacterRevision when Character state changes
+ receipt where required
+ mandatory durable_event_journal rows
+ publication enqueue state
commit in one PostgreSQL transaction
```

If mandatory journal/enqueue cannot commit, the audited mutation does not become authoritative. Best-effort telemetry is asynchronous and non-blocking.

Publisher uses committed rows only, delivery is at-least-once, EventId deduplicates effects, retries reuse retained exact event bytes, and replay cannot mutate gameplay.

## 10. Current state and checkpoints

Normalized root + typed current-state relations at CharacterRevision are canonical Character durability. Do not create a second generic serialized Character snapshot.

If later runtime/profile systems need an additional consistent checkpoint, use a manifest containing CharacterId, CharacterRevision boundary, relevant content/ruleset/map/world-policy/runtime-owner revisions and references to **typed owner-specific checkpoint components**. No arbitrary payload blob.

A Character success response is never authoritative before PostgreSQL commit. Lost success response is reconciled from durable receipt/current state rather than blindly repeated. This is a commit/ack invariant, not a numeric DR RPO promise.

## 11. Restart, crash and disaster restore

### Ordinary restart

Committed Character state/revision, required FND-04 authority continuity, operation receipts and mandatory audit/publication evidence are reconstructible from PostgreSQL before authority resumes. Redis/in-memory state cannot restore authority by itself.

Restart/failover never resets/reuses CharacterRevision, lease generation, connection generation, ControlLossEpoch, grace/protection deadlines or terminal GameSession; nor replays committed operations.

If authority cannot be proven, fail closed or use the accepted fresh/recovery path.

### PITR/disaster restore

A restored old snapshot cannot assume restored sessions/leases remain current.

Before gameplay authority resumes:

1. keep admission/mutation closed;
2. establish a strictly newer non-rollback recovery/authority fence outside values that could have rolled back with the snapshot, or prove an equivalent mechanism;
3. fence pre-restore TransportBinding/session/lease authority that cannot be proven current;
4. reconcile Platform security/account state and current routing/world revisions;
5. verify Character/name/operation/audit/publication integrity;
6. publish/replay committed evidence only, never gameplay commands;
7. reopen traffic only after restore validation passes.

Exact recovery-fence issuer/storage is deferred to DUR/OPS/security. The accepted candidate property here is **no authority resurrection**.

### Backup/RPO/RTO

Require PostgreSQL backup + WAL/PITR capability, automated restore verification, integrity checks across Character/name/FND-04/receipt/audit/publication state and exact artifact/revision evidence. Numeric production RPO/RTO remains OPS/PERF/milestone-owned.

## 12. Schema migration and compatibility

Game DB has one game-owned migration history; Platform migrations never apply it.

Incompatible change follows:

```text
EXPAND
-> resumable/idempotent BACKFILL or TRANSFORM
-> VALIDATE
-> CUT OVER compatible readers/writers
-> CONTRACT only after rollback window closes
```

Ruleset/profile/content changes that alter persisted interpretation require explicit source/destination revisions and deterministic migration/compatibility evidence. A revision number change never silently reinterprets state.

Migration IDs are never reused; backfills are resumable/bounded; constraints become authoritative only after validation; incompatible writers are fenced before destructive contract; rollback order is known before cutover; domain identities never change due to storage migration.

Definition references keep stable identity or explicit deterministic mapping; DB row positions/enum ordinals are never durable definition identity.

## 13. Foreign keys, retirement and privacy

Game-owned typed child relations use CharacterId referential integrity where both sides share game migration authority. Exact FK deferrability/cascade syntax is implementation-owned.

Ordinary Character retirement is a state transition, not `DELETE CASCADE`. Child data does not disappear solely because lifecycle becomes RETIRED unless its semantic/retention contract requires removal.

Physical cleanup never makes CharacterId reusable; sufficient tombstone/provenance evidence remains.

Privacy deletion/anonymization is separately owned by DATA-PRIVACY-01 and cannot be modelled as Character identity reuse or implicit removal of mandatory security/audit evidence. Name-history retention/public exposure needs explicit privacy/retention policy before production.

## 14. Query/index intent

Implementation must provide authoritative access paths for:

- CharacterId root;
- Characters by AccountId + lifecycle/policy eligibility;
- Characters by WorldId where required;
- complete canonical name-key conflict lookup;
- CharacterLease by CharacterId;
- AccountPresenceClaim by AccountId plus unique claimed CharacterId;
- GameSession by GameSessionId/current Character where recovery requires it;
- ReconnectAttempt candidate/disposition reconciliation;
- OperationId receipt;
- `(GameSessionId, CommandId)` durable dedup where implemented;
- pending publication without scanning full audit history;
- authorized EventId/TransactionId/CharacterRevision audit lookup.

Full identities/keys are authoritative. UUIDv7 order may improve locality but never defines chronology. Hash-only/partial indexes never replace full equality verification. High-cardinality IDs do not become normal metrics labels.

## 15. Required future failure outcomes

| Condition | Required disposition |
|---|---|
| stale CharacterRevision | conflict; no Character mutation |
| stale lease/session/runtime generation | conflict; no stale control/mutation |
| duplicate identical OperationId | same logical result/reconciliation |
| same OperationId + different request | conflict; no reinterpretation |
| duplicate durable `(GameSessionId, CommandId)` | same command; no second effect |
| same numeric CommandId in another GameSession | distinct command |
| canonical name conflict | one DB-authoritative winner |
| naming-policy migration collision | cutover blocked until resolved |
| quota/lifecycle race | serialized under account guard |
| concurrent fresh admissions | at most one atomic authority winner |
| reconnect PREPARE retry | same logical candidate/disposition |
| stale/failed reconnect COMMIT | no authority switch/nonce success/protection manufacture |
| lost reconnect COMMIT response | reconcile persisted attempt/current generation; no second switch |
| DB unavailable | no authoritative mutation; no Redis/in-memory fallback |
| deadlock/serialization failure | bounded same-operation retry |
| mandatory audit unavailable in transaction | mutation does not commit |
| publication dependency down after commit | durable backlog/retry; committed gameplay stays committed |
| unsupported schema/profile/definition revision | fail closed |
| ambiguous Character commit response | reconcile receipt/current state |
| restored stale session/lease authority | fenced; no authority resurrection |

Raw PostgreSQL errors are not public contracts.

## 16. Security boundaries

- game DB runtime credentials cannot write Platform DB;
- Platform credentials cannot write Character/FND-04 game relations;
- read projections use explicit read-only APIs/views/contracts;
- reconnect secrets never enter ordinary audit/analytics;
- knowing AccountId/CharacterId/GameSessionId is never authorization;
- ordinary corrections do not depend on manual raw SQL; later GM/support mutation uses typed audited domain commands.

## 17. Implementation evidence required later

This packet is paper-only. Future implementation must prove at least:

### Identity / constraints

- full UUID and persisted CommandId round trips;
- no cross-semantic ID substitution;
- CharacterId non-reuse;
- canonical name race and naming-policy migration collision detection.

### Character revision / quota

- stale CharacterRevision rejection;
- concurrent Character mutations produce one revision order;
- every quota-affecting lifecycle/create/transfer race respects policy;
- opposing transfers/rename-transfer do not split ownership or corrupt state.

### FND-04 authority

- concurrent fresh admissions have one final-boundary winner and no partial candidate authority;
- stale lease/runtime/session generation is rejected;
- PREPARE has zero authority and same retry returns same logical candidate;
- COMMIT atomically switches binding/generation/proof/attempt disposition and activates protection at most once;
- failed/stale COMMIT changes no authority;
- lost COMMIT response reconciles without a second switch;
- post-grace recovery creates a new GameSession and preserves actor state;
- actor-wide ControlLoss has one authority, survives restart and does not reset deadlines;
- full FND-04 binding revision set is revalidated at recovery.

### Idempotency

- duplicate create/rename/delete/restore/world-transfer/account-transfer has one effect;
- conflicting OperationId payload fails closed;
- durable gameplay command duplicate cannot double-apply.

### Audit/publication

- mutation + exact mandatory audit bytes + enqueue are atomic;
- crash after commit/before publish redelivers same EventId/bytes;
- duplicate publish yields one consumer effect;
- conflicting retained EventId content fails integrity checks;
- backlog cannot be discarded for capacity;
- replay cannot mutate gameplay;
- retention/privacy lifecycle cannot silently rewrite retained event semantics.

### Crash / restore / migration

- restart preserves Character/FND-04 fences and deadlines;
- terminal GameSession never revives;
- stale transport cannot regain authority;
- expand/backfill/validate/cutover/contract is demonstrated;
- interrupted backfill resumes idempotently;
- restore drill verifies Character/name/FND-04/receipt/audit/publication integrity;
- PITR/restore cannot resurrect pre-restore authority.

### Access/privacy

- Platform write credentials rejected from game authority tables;
- public/read projection cannot leak unauthorized ownership mapping;
- pseudonymous analytics family cannot silently fall back to raw CharacterId/AccountId; restricted player-linked audit remains controlled by its explicit privacy class.

## 18. Decision package

### RECOMMENDATION — NOT OWNER-ACCEPTED

Accept these seventeen rules as the minimum DUR-02 profile-neutral Character persistence architecture:

1. **Normalized current-state**, not event sourcing: `character_root` is identity/lifecycle/owner/world/global-revision lock anchor; typed children hold distinct state.
2. **One CharacterRevision** advances once per committed Character semantic transaction and remains independent from FND-04 authority generations.
3. **Account guard rows** serialize every quota-affecting portfolio/lifecycle operation without becoming Account authority or count truth.
4. **Global name registry** stores complete domain-generated canonical key + policy revision; DB uniqueness decides races; naming-policy cutover validates all destination collisions before one new authoritative policy becomes active.
5. **Separate FND-04 relations** keep AccountPresenceClaim, CharacterLease, GameSession and actor-wide ControlLoss continuity as distinct authorities; no duplicated ControlLoss truth.
6. **Atomic fresh admission** commits GrantNonce/presence/lease/new GameSession/connection generation as one revalidated authority boundary; failed admission leaves no partial authority.
7. **Reconnect/recovery PREPARE has zero authority** and uses bounded typed candidate/disposition state; same retry reconciles same candidate.
8. **Reconnect/recovery COMMIT is the only binding switch** and atomically fences predecessor, advances connection generation, binds candidate transport/proof, preserves actor/session continuity as applicable, records attempt outcome and activates the one eligible 4s protection entitlement at most once.
9. **Post-grace recovery uses a new GameSessionId** while preserving the same authoritative actor and existing eligible ControlLossEpoch semantics.
10. **Typed profile extensions only**; no generic JSON/KV/EAV misc-state escape hatch.
11. **Durable receipts** use OperationId for retryable Character workflows; `(GameSessionId, CommandId)` is persisted only where a real durable gameplay boundary needs it.
12. **Explicit lock/isolation proof**: Character root + account/FND-04/name constraints close anomalies; READ COMMITTED is acceptable only with proof, otherwise bounded SERIALIZABLE; advisory locks are never sole authority.
13. **Immutable retained audit semantics + separate mutable publication state** commit atomically with mandatory audited mutations; privacy/retention lifecycle remains separately governed.
14. **Normalized current state is the Character checkpoint**; additional checkpoints reference typed owner-specific components; no generic snapshot blob and no acknowledged success before commit.
15. **No authority resurrection after restore**: PITR/disaster restore requires a newer non-rollback recovery fence/equivalent proof before admission resumes.
16. **Staged migration** uses expand -> migrate/backfill -> validate -> cut over -> contract; retirement, physical deletion and privacy erasure remain separate; CharacterId is never reused.
17. **Profile-neutral core only**: unresolved Reference values/formulas/profile-specific PvP/world facts and numeric operational policies stay outside core schema invariants and remain gated by their owners.

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

Acceptance would unblock a separately authorized implementation-design/package for the profile-neutral Character persistence core and stable typed profile-extension contracts.

It would **not** create/migrate tables, accept GAME-ITEM/DUR-03, define item/currency atomicity, select a PvP/world profile, make unresolved Reference behavior true, authorize runtime persistence or set production RPO/RTO/backup frequency.

## 20. Supersession / reopening

A later proposal may reopen an accepted clause only with named evidence such as:

- a proven correctness anomaly not closed by the lock/constraint/authority-transition model;
- measured contention showing one Character root revision is an unacceptable bottleneck plus a proven equivalent partitioned fence;
- an accepted profile semantic requiring new typed durable state;
- evidence that a deferred formula/value constrains physical representation/atomicity;
- a PostgreSQL limitation discovered during implementation requiring an equivalent safer design;
- security/privacy/restore evidence requiring stronger separation/fencing;
- explicit later architecture superseding ADR-0004 Persistence-v1 direction.

ORM defaults, convenience, current Global schema, Canary/crystalserver tables or generic JSON flexibility are not sufficient evidence.

## 21. Deliberately not decided

- exact SQL table/column/index/constraint/schema names;
- migration framework/library;
- ORM/query builder/Rust DB crate;
- connection-pool settings;
- exact scalar representation of CharacterRevision/lease/session generations where accepted semantics allow equivalent non-reused forms;
- exact stable ruleset/content definition-key scalar representation where its owner has not frozen it;
- profile-specific child table layouts;
- item/currency/market/house schema;
- partitioning/sharding;
- operational retention/backup/RPO/RTO/retry values;
- reconnect-secret hashing/KMS;
- exact non-rollback disaster-recovery fence implementation/issuer;
- physical GrantNonce/security-evidence relation layout;
- production topology;
- runtime implementation.

Until the owner accepts or modifies section 18, this document remains **PRE-DECISION ARCHITECTURE / NOT ACCEPTED** and `DUR-02` remains `PROPOSED / PLANNED / NOT_STARTED`.
