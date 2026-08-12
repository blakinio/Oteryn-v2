# DUR-03 — Item Transaction and Anti-Duplication Contract

- Date: 2026-08-12
- Gate: `DUR-03`
- Delivery task: `OTV2-20260812-dur-03-item-transaction-architecture`
- Delivery PR: #207
- Status on delivery branch: **CANDIDATE / NONBINDING**
- Canonical semantic effect: only after accepted delivery merge; programme `ACCEPTED / LIFECYCLE_CLOSED` promotion and successor exposure require a separate lifecycle closeout
- ImplementationStatus: **NOT_STARTED**
- Runtime authority: **NONE**
- PostgreSQL DDL/migration authority: **NONE**
- Production authority: **NONE**
- Analysis source: `DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_ANALYSIS.md`

## 1. Purpose

Freeze the minimum native transaction and anti-duplication semantics required before any implementation may claim authoritative durable item/currency/value correctness.

This contract owns:

- one authoritative immediate location for each live ItemInstance;
- create/retire/split/merge/quantity-transfer/transform ItemInstanceId transition rules;
- item/currency/value transfer, mint, burn, transform and conversion conservation semantics;
- stable transaction/operation identity across retry and ambiguous commit;
- durable idempotency/reconciliation obligations;
- authority/fencing requirements for durable value mutation;
- bounded atomic transaction participant rules;
- safe typed custody for multi-transaction workflows;
- mandatory durable provenance/evidence sufficient for independent anti-duplication reconciliation;
- restore/recovery item/value integrity gates;
- cross-world/cross-authority fail-closed behavior.

It does **not** own runtime code, physical PostgreSQL schema, wire payloads, item legality, market/trade/business policy, exact Reference formulas/rates or production rollout.

## 2. Authority chain

Binding ownership is:

```text
stable authored item definitions / content identity -> ADR-0005 + DUR-04
ItemInstance semantic legality/equipment/container  -> GAME-ITEM-01
ItemInstanceId durable representation/non-reuse     -> DUR-01
common migration/transaction/outbox/PITR substrate -> DUR-02
item/currency/value transactions + conservation     -> DUR-03
event/audit identity/evidence/privacy               -> ANL-01
CommandRef ordering/duplicate ingress               -> FND-02
runtime ownership/order/fencing                     -> FND-03
GameSession/CharacterLease/recovery authority       -> FND-04
exact formulas/ruleset arithmetic                   -> SIM-DETERMINISM-01 + owning gameplay gates
loot/trade/market/bank/depot/mail/reward/house policy -> owning domain gates
```

No layer may redefine another owner's semantics for persistence convenience.

## 3. Core safety theorem

A future DUR-03-conforming implementation must be able to prove:

```text
For every committed logical durable value transaction T:

1. T has exactly one semantic TransactionId.
2. Every pre-existing live ItemInstance touched by T is accounted for exactly once.
3. Every surviving live ItemInstance has exactly one authoritative immediate location after T.
4. Every newly created concrete ItemInstance has a fresh ItemInstanceId never previously live/retired.
5. Every retired ItemInstanceId is never reused.
6. Pure transfer/split/merge operations do not create or lose units/value.
7. Mint/burn/transform/conversion occurs only under explicit typed authorized cause/rule lineage.
8. Mandatory durable receipt/audit evidence commits atomically with the authoritative mutation.
9. Retry, duplicate command, stale authority, crash, timeout or lost response cannot create a second effect for the same logical transaction/operation.
10. Failed/aborted transactions leave no partial authoritative value mutation.
```

If the implementation cannot prove one of these properties for an operation class, that operation class is not DUR-03-conforming.

## 4. Canonical immediate-location model

### 4.1 One immediate location

Every live concrete ItemInstance has exactly one authoritative immediate location.

Conceptually:

```text
ItemInstanceId
-> exactly one ItemLocationRef
```

This relation is semantic and does not freeze SQL table layout.

### 4.2 Initial typed location families

The model must be able to represent at least:

```text
CharacterInventory {
  character_id: CharacterId
  position: typed inventory position owned by the inventory/gameplay contract
}

CharacterEquipment {
  character_id: CharacterId
  occupancy: semantic equipment claim owned by GAME-ITEM-01
}

Container {
  parent_item_instance_id: ItemInstanceId
  entry: typed container entry/position
}

Ground {
  world_id: WorldId
  runtime_scope: ChannelId or InstanceId with WorldId scope
  spatial_position: typed world position owned by world/movement/content contracts
}

TypedDomainCustody {
  registered custody family
  stable domain-owned custody reference
  explicit world/scope ownership
}
```

Exact Rust/SQL encodings are deferred.

### 4.3 No generic location escape hatch

The following are prohibited as canonical authority:

- arbitrary location strings;
- generic JSON location objects;
- free-form EAV location fields;
- multiple independent nullable owner/location columns treated as peer authorities;
- a generic `owner_id` whose meaning changes by subsystem.

Every new custody/location family requires a typed versioned contract with a named semantic owner.

### 4.4 Binding, ownership and authorization remain separate

An item's:

```text
WorldId value scope
binding/restrictions
immediate location/custody
current gameplay authorization
presentation ownership
```

remain distinct concepts.

Possession, CharacterId equality, account binding or a custody reference never grants mutation authority by itself.

## 5. Container immediate-parent semantics

GAME-ITEM-01 defines containment as a bounded directed acyclic graph.

DUR-03 freezes the transaction consequence:

- a contained item is immediately located in its parent container;
- moving a container changes the container's own immediate location, not every descendant relation;
- descendants remain in their immediate parent containers;
- all affected GAME-ITEM capacity/weight/type/nesting constraints required by the proposed operation must validate before commit;
- destroying/replacing a container that still has live descendants is invalid unless the same bounded transaction explicitly relocates/transforms/retires every affected descendant required by that operation;
- no committed transaction may leave an orphaned live descendant or create a containment cycle.

This is a semantic relation model, not a physical-schema mandate.

## 6. Item lifecycle and identity transitions

### 6.1 Preserve identity for same concrete lifecycle

A legal typed-state mutation on the same concrete item lifecycle preserves ItemInstanceId.

Examples, only where the owning GAME-ITEM/ruleset semantics permit:

- charge change;
- durability change;
- binding/restriction change;
- compatible upgrade/modifier state change;
- quantity increase/decrease on an existing stack when no additional independently locatable concrete stack is created;
- an explicitly identity-preserving one-to-one transform.

### 6.2 Fresh identity for a new concrete lifecycle

A fresh ItemInstanceId is mandatory whenever an operation creates a new independently locatable concrete ItemInstance lifecycle.

Examples:

- a new non-stackable item instance;
- a new stack object;
- split output stack;
- replacement transform output;
- explicit multi-output transform/crafting output that is a concrete item instance.

### 6.3 Retirement

A concrete ItemInstance lifecycle becomes terminal when it no longer exists as a live instance.

Its ItemInstanceId:

- is never reused;
- is not reassigned to another ItemType or actor after terminal retirement;
- may remain in durable audit/provenance/tombstone evidence as required by DUR-01/ANL/privacy policy.

### 6.4 Quantity zero

GAME-ITEM-01 forbids quantity zero as live stack state.

Therefore a transaction reducing a stack to zero must retire that ItemInstance in the same atomic outcome.

## 7. Split semantics

For a live stack `S` with quantity `q` and requested split amount `x`:

```text
0 < x < q
```

Committed split outcome:

```text
S:
  same ItemInstanceId
  quantity = q - x
  remains live

N:
  fresh ItemInstanceId
  quantity = x
  independently locatable
```

Rules:

- `x == 0` invalid;
- `x >= q` is not a valid split;
- moving all quantity is a move of the existing stack instance, not a split/new-ID operation;
- source + output quantities equal the pre-split quantity exactly;
- all stack/type/revision/location constraints validate atomically.

## 8. Quantity transfer and merge semantics

For compatible live stacks A and B, an authoritative quantity transfer of `x` units from A to B:

- B retains B's ItemInstanceId;
- B quantity increases by `x` without exceeding accepted bounds;
- A quantity decreases by `x`;
- A retains A's ItemInstanceId if its post-transaction quantity is positive;
- A is terminally retired if its post-transaction quantity is zero;
- no temporary ItemInstance is required merely to represent fungible units moving between existing stacks;
- total units for the same conserved asset/type are identical before and after a pure transfer/merge.

The authoritative operation, not client list order or UUID ordering, identifies the source/receiving stack semantics.

## 9. Create/mint semantics

### 9.1 Concrete instance mint

Creating a new concrete item object/stack lifecycle requires a fresh ItemInstanceId fixed before the first possibly ambiguous durable commit.

### 9.2 Quantity mint into an existing stack

A typed authorized source may increase quantity on an existing compatible stack without creating a temporary ItemInstance solely for newly produced fungible units.

The transaction must still retain exact mint cause and quantity lineage.

### 9.3 Stable source cause

Every value-creating operation must have an authoritative typed source/cause identity sufficient to prevent duplicate application.

Conceptual sources include later owning-domain occurrences such as:

- loot resolution;
- reward grant;
- crafting output;
- static-placement materialization;
- system source;
- administrative compensation.

DUR-03 does not decide business eligibility for those sources.

It requires:

- one logical source occurrence cannot mint twice through retry/crash;
- repeated attempt under the same source/operation identity reconciles the original result;
- same source identity with conflicting output set is an integrity conflict;
- repeatable sources use distinct authoritative occurrence identities per occurrence.

## 10. Destroy/burn semantics

A burn/destruction transaction must explicitly identify:

- affected ItemInstance/quantity/value asset;
- typed sink/cause;
- whether the instance survives with reduced quantity/state or retires;
- required lineage/audit evidence.

Silent deletion, `quantity = 0` persistence, raw administrative row removal or disappearance during error recovery is not a valid sink.

## 11. Transform semantics

### 11.1 Identity policy is explicit

Every executable type-changing transform edge has a versioned identity transition policy.

Allowed architecture modes:

```text
PRESERVE_INSTANCE
REPLACE_INSTANCE
```

### 11.2 PRESERVE_INSTANCE

May be used only when:

- one input concrete instance maps to one output concrete instance;
- the owning transform rule explicitly proves it remains the same lifecycle;
- resulting ItemType/capability state is compatible and fully specified;
- no second live output is created from the same ItemInstanceId.

The ItemInstanceId survives.

### 11.3 REPLACE_INSTANCE

The old instance retires and every concrete output receives fresh ItemInstanceId.

### 11.4 Multi-input/multi-output

Each input has an explicit disposition:

- survives/mutates;
- quantity decreases;
- retires.

Each output is either:

- an explicitly preserved one-to-one survivor permitted by the transform policy; or
- a new concrete lifecycle with a fresh ItemInstanceId; or
- a non-item fungible value line under the owning conversion/asset contract.

One ItemInstanceId may never become two live outputs.

### 11.5 Parity unknown

If a Reference-sensitive transform's identity behavior is not established by accepted evidence, it remains `PARITY_PENDING_EVIDENCE` / unsupported for claimed Reference execution rather than choosing a convenient default.

## 12. Conservation classifications

Every authoritative value mutation line belongs to one explicit class:

```text
TRANSFER
SPLIT_MERGE_QUANTITY
STATE_MUTATION
MINT
BURN
TRANSFORM
CONVERSION
```

A generic unclassified signed delta is prohibited.

### 12.1 TRANSFER

Existing live value changes immediate location/custody without source/sink creation.

### 12.2 SPLIT_MERGE_QUANTITY

Units of one conserved stackable asset/type redistribute across stack instances; total units are exact before/after.

### 12.3 STATE_MUTATION

One concrete lifecycle changes legal typed state with no implicit value creation/destruction beyond the owning explicit semantic rule.

### 12.4 MINT/BURN

Value enters/leaves the live system only under an explicit typed source/sink cause.

### 12.5 TRANSFORM

A versioned rule explicitly maps an input set to output set and identity outcomes.

### 12.6 CONVERSION

A versioned rule explicitly maps exact asset A inputs/debits to exact asset B outputs/credits.

DUR-03 does not infer conversion rate from market price or historical economy state.

## 13. Non-item fungible value

Non-item balances such as bank/ledger/token balances are not forced into ItemInstance.

For every authoritative non-item fungible asset:

- the owning domain defines stable asset identity/denomination and valid account/custody scopes;
- arithmetic uses a bounded exact representation;
- binary floating point is not the authoritative conservation basis;
- pure transfers balance exact debits and credits for the same asset;
- net creation/destruction requires explicit MINT/BURN source/sink cause;
- conversion requires explicit input/output asset rule;
- retries and ambiguous commits follow the same DUR-03 TransactionId/OperationId semantics.

Exact SQL scalar and product/business rules are deferred.

## 14. World scope conservation

Every live ItemInstance belongs to exactly one WorldId gameplay-value scope under GAME-ITEM-01.

DUR-03 rules:

- direct cross-world item/currency/value transfer is forbidden by default;
- a burn in world A followed by mint in world B is still semantically a cross-world value transfer and cannot bypass the prohibition merely because it uses two transactions;
- a future dedicated world-transfer contract must define value/identity lineage, balance policy, custody, retry, rollback/recovery and authority fencing explicitly;
- current DUR-03 does not authorize such a feature.

## 15. Transaction identity

### 15.1 TransactionId

Every logical atomic durable item/currency/value mutation has exactly one ANL-01 TransactionId.

It is fixed before the first potentially ambiguous durable commit attempt.

For the same logical atomic transaction:

- retry preserves TransactionId;
- serialization/deadlock retry preserves TransactionId;
- ambiguous commit reconciliation preserves TransactionId;
- semantic participants/effects/cause remain identical;
- same TransactionId with conflicting semantic intent is an integrity conflict, never last-write-wins.

### 15.2 New TransactionId

A new TransactionId means:

- the prior logical transaction is proven terminal; and
- an intentionally new logical atomic mutation is beginning.

Timeout alone is not proof of terminal abort.

## 16. CommandRef boundary

For player-originated commands:

```text
CommandRef = (GameSessionId, CommandId)
```

remains FND-02 authority for ordered command identity and duplicate non-reexecution.

DUR-03 consumes but does not redefine:

- monotonic command reservation;
- bounded outstanding window;
- duplicate CommandId behavior;
- same-GameSession reconnect command continuity.

A connection-generation change by itself does not create a new semantic command/transaction.

## 17. OperationId boundary

An ANL-01 OperationId is required when the owning value workflow is logically retryable beyond one atomic transaction/CommandRef scope, including when it:

- spans multiple durable transactions;
- continues asynchronously;
- may be resumed/retried across GameSessions/processes;
- has explicit durable workflow lifecycle/custody.

OperationId remains stable for the same logical operation.

DUR-03 does not require OperationId for every simple command whose semantics are fully bounded by CommandRef and authoritative state preconditions.

## 18. Durable idempotency and receipts

For every operation class whose safe retry cannot be proven solely from FND-02 ingress + current authoritative state, durable receipt/reconciliation state is mandatory.

It must be sufficient to classify:

```text
NOT_SEEN / safely retryable
COMMITTED / return original authoritative result
TERMINAL_REJECTED when the owning domain makes rejection durable
AMBIGUOUS / reconciliation still required
CONFLICT / same identity used with different semantic intent
```

Exact names/storage are implementation-defined; the semantic distinctions are binding.

Receipt retention must cover the full owning replay/idempotency horizon. Once-only mint/grant/source identities cannot be forgotten while the same source can be replayed.

## 19. Ambiguous commit algorithm

A transport/DB timeout or lost response is not evidence that a durable transaction aborted.

Required behavior:

```text
execute logical transaction T

if commit is known successful:
    reconcile/return committed result

if attempt is known aborted and retry policy permits:
    retry same T with same TransactionId

if commit outcome is ambiguous:
    inspect durable receipt/state/evidence for T
    if committed:
        reconcile/return original committed result
    else if safely proven not committed/aborted:
        retry same T
    else:
        fail/hold safely
        DO NOT create a new transaction as a guess
```

A lost client response after commit never justifies duplicate effect.

## 20. Compensation after commit

Once a transaction is committed, its historical authoritative/audit fact is immutable.

Undo/correction uses a **new compensating transaction** with:

- new TransactionId;
- explicit causation/reference to the original transaction/operation;
- current authorization;
- complete conservation/source-sink evidence.

Direct historical row/audit rewrite is not compensation.

## 21. Atomic participant set

Before commit, every logical atomic transaction has a bounded closed participant/effect set sufficient to prove its invariants.

May include:

- pre-existing ItemInstances;
- immediate locations/custodies;
- item capability/quantity state;
- equipment/container claims;
- non-item value accounts and asset lines;
- durable idempotency/receipt state;
- domain workflow/custody state;
- required authority/fence state;
- mandatory ANL durable audit + publication state.

The participant/effect set cannot expand without bounds during commit.

## 22. Resource bounds

DUR-03 implementation requires absolute security/resource ceilings for all variable-size transaction structures, including at minimum:

- touched ItemInstance count;
- location/custody mutation count;
- non-item value line count;
- transform input/output count;
- container graph validation expansion;
- workflow/custody participant count;
- mandatory audit event/payload contribution size;
- retry/reconciliation work per request.

Ruleset/product limits may be lower but never exceed absolute ceilings.

This architecture candidate does not invent numeric values without workload/security evidence. Missing mandatory ceilings are an implementation blocker, not “unlimited”.

## 23. Isolation, locking and anomaly closure

DUR-02 remains binding:

```text
name invariant
+ identify authority rows/constraints
+ prove anomaly closure under selected isolation/locks/constraints
```

DUR-03 adds:

- application-only check-then-write is insufficient for single-location/value-conservation correctness;
- deterministic lock/acquisition ordering or another proven deadlock/anomaly-closing mechanism is required for multi-participant transactions;
- READ COMMITTED is permitted only with explicit invariant proof;
- otherwise bounded SERIALIZABLE or stricter accepted domain mechanism applies;
- deadlock/serialization retry preserves TransactionId/OperationId/Command identity;
- advisory locks are not the sole durable authority for location, custody, uniqueness or conservation.

Exact SQL syntax/lock ordering implementation is deferred.

## 24. Player/character authority fencing

A transaction mutating Character-controlled value must consume current FND authority.

Applicable proof may include:

- valid GameSession identity/command ingress;
- current CharacterLease generation/authority;
- current actor/domain state preconditions;
- current runtime scope ownership generation for channel/instance-scoped participants.

Rules:

- binding/ownership/location metadata is not authority;
- stale lease/session/runtime owner cannot commit new value mutation;
- ItemInstanceId itself is not a credential;
- client-supplied quantity/location/item state is intent only and must be re-read/validated authoritatively.

## 25. Connection generation nuance

FND-02/FND-04 allow eligible reconnect of the same GameSession with a newer connection_generation while preserving previously reserved pending CommandRefs.

Therefore DUR-03 does not require that the **old transport generation itself** still be current at DB commit for every valid command already accepted into authoritative ingress.

It requires instead:

- command was reserved under valid authoritative binding;
- the logical GameSession/CharacterLease/runtime authority remains valid under FND-03/FND-04 continuation rules;
- no superseding/terminal authority event invalidates the pending mutation;
- commit-time domain/runtime fences required by the affected participants are current.

This prevents stale writers without breaking same-session reconnect correctness.

## 26. Channel/instance scope fencing

Any durable mutation touching channel/instance-scoped ground or custody state must prove current runtime-scope ownership generation or an equivalently accepted durable fence at the transaction boundary.

A stale former GameNode/ChannelRuntime/InstanceRuntime owner cannot commit after ownership transfer/recovery.

DUR-03 does not use NodeId alone as authority.

## 27. Equipment atomicity

GAME-ITEM-01 owns equip legality and complete occupancy claims.

DUR-03 requires equip/unequip to commit atomically with all authoritative item locations/occupancy consequences.

Valid result:

```text
all old locations/claims released as required
+ complete new occupancy claim established
+ every displaced item placed legally if operation permits displacement
+ required durable evidence
OR
none of those changes become authoritative
```

A partial two-handed/mutually-exclusive occupancy commit is invalid.

## 28. Ground and inventory atomicity

Pickup/drop/move transactions must preserve:

- one immediate location before/after;
- world/runtime scope correctness;
- current authority/fences;
- container/inventory/equipment legality;
- no client-created quantity/item/location facts;
- one transaction identity across retry;
- mandatory audit/receipt where required.

A lost pickup response may reconcile a committed inventory result; it must not leave both ground and inventory copies.

## 29. Multi-transaction workflows and typed custody

A future value workflow may span multiple durable transactions only when each committed step is itself safe.

Required pattern:

```text
logical OperationId where needed
-> transaction 1: transfer value into explicit typed custody
-> zero or more idempotent workflow steps
-> transaction N: transfer/transform value out of custody
```

Rules:

- custody is an immediate authoritative location/reference, not a boolean flag beside the old location;
- after custody transfer commits, the item/value cannot remain spendable from the prior location;
- every step has its own TransactionId and is independently conservation-safe;
- workflow state is restartable/idempotent;
- no hidden end-to-end all-or-nothing assumption spans separate transactions;
- compensation is explicit new transaction;
- the owning domain gate defines business state transitions/eligibility.

## 30. Current database boundary

Under accepted ADR-0004/DUR-02 current architecture, atomic DUR-03 v1 value mutation is one game-owned PostgreSQL transaction inside the current `oteryn_game` persistence authority.

This contract does not authorize or define:

- Platform/game distributed two-phase commit;
- cross-database foreign keys;
- dual-authority mirrored item ownership;
- implicit remote-service atomicity.

If a future custody surface belongs to another database/service authority, direct atomic transfer is unsupported until a dedicated contract proves a safe handoff/custody protocol.

## 31. StaticItemPlacement materialization

GAME-ITEM-01 establishes that authored StaticItemPlacement is not automatically a durable ItemInstance.

When gameplay materializes a placement/occurrence into durable mutable item state:

- the authoritative occurrence/cause identity must be stable enough to deduplicate retry/crash;
- every new concrete ItemInstance receives fresh ItemInstanceId;
- same one-shot materialization occurrence cannot mint a second output on retry;
- same occurrence with conflicting outputs is an integrity conflict;
- repeatable respawn/reset behavior requires distinct authorized occurrences under its owning content/gameplay contract;
- DUR-03 does not invent the respawn/reset business rule.

## 32. Loot/reward/crafting cause boundary

DUR-03 does not determine:

- what loot drops;
- who is eligible;
- reward schedules;
- crafting recipes;
- market prices;
- entitlement benefits.

It requires any owning domain that produces/consumes durable value to provide a stable authoritative cause/rule context such that retry/recovery cannot apply the same logical output twice.

A future loot/craft/reward transaction must fix its exact output/input mutation set before ambiguous commit.

## 33. Trade/market/depot/mail/bank/house boundary

DUR-03 supplies reusable transaction/custody/conservation rules only.

| Surface | DUR-03 owns | Domain owner retains |
|---|---|---|
| trade | atomic item/value exchange + custody safety | consent/state machine/eligibility |
| market | value conservation + escrow/custody mechanics | offers, pricing, fills, fees, cancellation policy |
| depot | item move/custody conservation | access/depot semantics |
| mail | item custody/move conservation | addressing/delivery lifecycle |
| bank | exact item/ledger transfer/conversion conservation | banking/economy product policy |
| rewards | mint/transfer idempotency/provenance | reward eligibility/schedule |
| houses | item placement/move conservation | house ownership/access/rent/topology |

No surface becomes accepted merely because DUR-03 provides a transaction substrate.

## 34. Mandatory durable evidence

Every committed transaction whose item/value mutation is authoritative requires ANL-01-compatible `DURABLE_AUDIT` evidence sufficient for independent reconciliation.

Minimum semantic evidence, as applicable:

- TransactionId;
- OperationId and/or CommandRef/cause reference;
- WorldId and relevant channel/instance/runtime scope;
- exact ruleset/content/item-definition revisions required to interpret the mutation;
- touched ItemInstanceIds;
- each touched instance before/after lifecycle disposition: `EXISTING_SURVIVED`, `MINTED`, `RETIRED` or equivalent typed semantics;
- immediate before/after location for moved/surviving instances;
- ItemType/revision transition when changed;
- exact quantity deltas for stackable units;
- non-item asset/account debit/credit lines;
- mutation classification: transfer/split-merge/state/mint/burn/transform/conversion;
- typed source/sink/transform/conversion cause/rule reference;
- conservation summary sufficient to independently validate transaction closure;
- relevant authority/fence references where safe and necessary, excluding secret credential/proof material.

The evidence set is fixed before the first possibly ambiguous commit and commits atomically with authoritative state.

## 35. ANL event-schema boundary

This architecture contract deliberately does not allocate speculative gameplay event type IDs or select final protobuf payload layout.

Before any implementation claims DUR-03 conformance, the implementation/contract package must register concrete ANL-01 event types/schema revisions and resource ceilings implementing the mandatory evidence semantics in section 34.

That registration must preserve:

- EventId immutability;
- TransactionEventRef complete-set rules;
- exact payload-byte retry stability;
- privacy class/retention policy;
- replay read-only behavior;
- no high-cardinality ItemInstanceId metrics labels.

## 36. Durable acknowledgement

For a DUR-03 mutation declared durable:

```text
success acknowledged
=> owning PostgreSQL transaction committed
=> mandatory durable receipt/audit committed
=> ordinary process/GameNode restart can reconstruct the committed result
```

A runtime checkpoint, network send or in-memory state change is not durable success.

If response delivery is lost after commit, reconciliation returns/proves the committed result rather than reapplying the mutation.

## 37. Restore and disaster recovery

DUR-02 PITR/recovery rules remain binding.

Before authoritative item/value mutation resumes after restore, implementation must validate at least:

- supported schema/migration history;
- each live ItemInstanceId is unique/non-nil/valid and not known retired;
- each live ItemInstance has exactly one valid immediate location;
- parent containers/custodies exist and container graph remains bounded/acyclic;
- no quantity zero/overflow or incompatible item definition reinterpretation;
- TransactionId/OperationId/source-cause receipt uniqueness has no conflict;
- mandatory committed audit TransactionEventRef sets are complete where required;
- non-item asset invariants reconcile;
- restored pre-loss GameSession/CharacterLease/runtime authority is fenced by a newer accepted recovery fence;
- audit replay does not execute gameplay mutation/remint outputs.

Integrity failure keeps affected authoritative mutation closed until an explicit safe repair/compensation path is accepted.

## 38. Analytics/Game Intelligence boundary

Game Intelligence/ANL consumers may:

- reconcile transaction evidence;
- detect impossible duplicate location/lineage/value patterns;
- raise alerts/cases;
- reconstruct provenance for investigation.

They may not:

- mutate item/value authority;
- delete/merge duplicate rows automatically;
- mint compensation;
- ban/sanction automatically under DUR-03;
- rewrite history;
- bypass domain authorization.

Confirmed correction uses a new typed authorized gameplay/admin compensation transaction under later OPS-GM/security policy.

## 39. Fail-closed error dispositions

Minimum semantic dispositions:

| Condition | Category | Required effect |
|---|---|---|
| invalid item/location/capability/type state | `INVALID_INPUT` | no authoritative mutation |
| semantic item/equipment/container rule rejected | owning rejection category | no mutation |
| wrong WorldId/runtime scope | `CONFLICT` | no mutation |
| stale GameSession/CharacterLease/runtime owner | `CONFLICT` / stale-authority subtype | no mutation |
| duplicate same semantic transaction/operation | idempotent replay/reconciliation | no second mutation |
| same TransactionId/OperationId/source identity with conflicting intent | `CONFLICT` / integrity | no overwrite/reinterpretation |
| serialization/deadlock retryable abort | transient internal/dependency category | bounded retry same semantic identity |
| ambiguous commit | reconciliation required | no blind new TransactionId |
| participant/resource limit exceeded | `CAPACITY_EXCEEDED` | no partial mutation |
| unsupported transform/definition/ruleset revision | `UNSUPPORTED_REVISION` | fail closed |
| mandatory audit cannot commit | `DEPENDENCY_UNAVAILABLE` or owning internal category | no authoritative mutation where audit mandatory |
| internal location/conservation/lineage violation | `INTERNAL_UNAVAILABLE` / integrity | stop affected path; preserve evidence |

Exact client-visible error codes belong to owning protocol/domain registries when implementation payloads are introduced.

## 40. Transaction state versus client presentation

Client UI state, optimistic visuals, drag/drop source slots or cached inventory snapshots do not define transaction authority.

The server may reconcile client-visible state through FND-02 domain revisions/snapshots/deltas after commit.

A client stale-view rejection does not alter durable conservation semantics.

## 41. Derived/materialized state

If implementation maintains derived/materialized state such as:

- inventory indexes;
- equipment projections;
- weight summaries;
- search views;
- client projection rows;

then it must be either:

1. atomically consistent with the authoritative transaction when the field itself participates in correctness; or
2. explicitly rebuildable/non-authoritative from committed source state.

No duplicate cache/projection becomes a second item-location authority.

## 42. Definition revision compatibility

Every transaction must interpret touched items under compatible explicit definition/ruleset/content revisions per GAME-ITEM-01.

Rules:

- no silent reinterpretation because ItemTypeKey is unchanged;
- `MIGRATION_REQUIRED` item state cannot be mutated under new meaning until accepted migration/validation completes;
- unsupported mixed revision fails closed;
- transform/conservation evidence retains enough revision context to interpret historical lineage.

## 43. Concurrency with session recovery

If an item/value transaction is already committed when transport/session response continuity fails:

- the committed durable result remains authoritative;
- reconnect/recovery cannot replay the mutation as new;
- client/session reconciliation uses retained command/operation/transaction result/evidence as available;
- if same-GameSession resume cannot safely reconstruct command state, FND-02/FND-04 may terminate that session, but committed item/value state is not rolled back merely for session convenience.

## 44. Multi-channel invariants

- Character-held durable value is not made channel-owned solely because the Character is currently attached to one channel.
- channel/instance ground state remains explicitly runtime-scope fenced.
- no stale channel owner writes durable ground value after ownership generation changes.
- a direct durable transfer between two independent live channel/instance authorities is unsupported unless a later contract introduces an explicit one-winner handoff/custody coordinator.
- cross-channel relog/recovery cannot duplicate character inventory because inventory ItemInstances retain one immediate location and one current Character authority relation.

## 45. Security and abuse invariants

Mandatory:

- no client authority for item identity, quantity, location, source/sink or currency balance;
- no arbitrary authoritative transaction JSON/EAV payload interpreted as domain semantics;
- no unbounded transaction participant graph;
- no cross-world value laundering by burn+mint;
- no same cause/OperationId/TransactionId conflict resolved by last-write-wins;
- no raw SQL/admin mutation path as ordinary gameplay correction;
- no ItemInstanceId reuse;
- no binding/location metadata as session authority;
- no stale GameNode/lease owner commit;
- no mandatory audit downgrade to best-effort telemetry;
- no audit replay as gameplay replay;
- no automatic analytics repair authority.

## 46. Implementation evidence requirements

Any future implementation claiming DUR-03 conformance must prove, on exact revisions, at least:

### Identity/location

- create fresh ID/non-reuse;
- split source/new-ID behavior;
- partial/full merge survivor/retirement behavior;
- preserve/replace transform fixtures;
- one immediate location across inventory/equipment/container/ground/custody;
- container subtree move without descendant rewrite/orphan;
- cross-world rejection.

### Idempotency/concurrency

- duplicate same CommandRef no second execution;
- same TransactionId retry no second effect;
- conflicting same TransactionId rejected;
- lost response after commit reconciles original result;
- serialization/deadlock retry preserves semantic identity;
- stale CharacterLease rejected;
- stale runtime ownership generation rejected;
- same-GameSession reconnect does not duplicate valid pending command effect.

### Conservation

- pure move preserves instance/value;
- split/merge quantities balance exactly;
- mint/burn require cause;
- duplicate mint cause rejected/reconciled;
- transform complete input/output lineage;
- non-item ledger debit/credit conservation;
- conversion fixtures use exact accepted rule;
- compensation is new transaction with causation.

### Atomicity/failure

- crash before commit => no authoritative mutation/audit;
- crash after commit before response => committed state/evidence recoverable;
- crash around publication => EventId-stable at-least-once publish, no gameplay replay;
- equipment multi-slot move commits all/none;
- custody transfer cannot leave item spendable in old location;
- participant/resource overflow rejects without partial state.

### Restore

- restore detects duplicate location/receipt/cause conflicts;
- pre-restore authority fenced;
- audit replay cannot remint;
- mandatory integrity failures keep mutation closed.

### Evidence

- concrete registered ANL durable-audit event schemas/types;
- TransactionEventRef complete-set/gap/duplicate validation;
- privacy/retention profiles;
- no ItemInstanceId high-cardinality metrics labels.

Architecture acceptance alone proves none of these runtime outcomes.

## 47. Decision timing

### Must decide now?

**YES.**

### Downstream work blocked

- durable inventory/equipment/container/ground implementation;
- item/currency anti-duplication implementation;
- durable loot/pickup persistence slice;
- safe typed custody substrate for later trade/market/depot/mail/reward/house flows;
- Game Intelligence item/value reconciliation;
- item/value concurrency/crash/recovery E2E.

### Future migration cost if changed late

Changing after durable data exists can require migration of:

- location authority representation;
- ItemInstanceId lineage semantics;
- receipts/idempotency keys;
- source/sink provenance;
- transaction evidence interpretation;
- custody ownership;
- restore verification.

### Supersession evidence

Reopen only with named evidence such as:

- proven first-Reference behavior incompatible with the typed extension model;
- a PostgreSQL anomaly/correctness proof showing accepted atomicity cannot safely close a required operation;
- measured scale evidence requiring a different bounded partition/custody architecture;
- security/exploit evidence;
- a future accepted cross-service/database custody protocol with equivalent one-authority/conservation guarantees;
- privacy/legal retention constraints;
- explicit later owner world-transfer/economy policy.

OTS schema layout, library preference or convenience is insufficient.

### Deliberately not decided

- physical SQL schema/index/constraint/lock syntax;
- concrete Rust transaction API/crates;
- numeric transaction/resource ceilings without evidence;
- concrete ANL event IDs/protobuf payloads;
- exact Reference source/sink/transform/crafting/decay/trade/market/bank/depot/mail/reward rules not evidenced;
- business state machines of downstream surfaces;
- cross-world transfer feature;
- cross-database/service atomic transfer protocol;
- production RPO/RTO/topology/backup cadence;
- automatic remediation.

## 48. Acceptance consequence

Only after:

1. this candidate delivery passes exact-head self-review;
2. required genuinely independent review has zero open material findings;
3. exact-head governance/document CI passes;
4. review threads/ownership conflicts are clean;
5. PR #207 is squash-merged unchanged; and
6. a separate lifecycle closeout atomically promotes maintained programme status/handoff,

may canonical programme state become:

```text
DUR-03
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
Runtime authority    = NONE
DDL/migration authority = NONE
```

That acceptance does **not** authorize item/value runtime implementation or production mutation. It only allows a later separately authorized implementation task to consume the contract.
