# DUR-03 — Item Transaction and Anti-Duplication Analysis

- Date: 2026-08-12
- Gate: `DUR-03`
- Delivery task: `OTV2-20260812-dur-03-item-transaction-architecture`
- Delivery PR: #207
- Status: **ANALYSIS / CANDIDATE INPUT; nonbinding while PR #207 is open**
- Scope: paper-only item/currency/value transaction semantics and anti-duplication invariants
- Runtime authority: **NONE**
- PostgreSQL DDL/migration authority: **NONE**

## 1. Executive summary

`DUR-03` must close the correctness gap between accepted item semantics and any future implementation that moves, creates, destroys, transforms or exchanges durable gameplay value.

The accepted upstream architecture already gives Oteryn-v2 most prerequisites:

- `GAME-ITEM-01` defines what an ItemType and ItemInstance mean, legal typed item state, equipment/container legality, world scope and definition compatibility;
- `DUR-01` gives every concrete ItemInstance a strong non-reused UUIDv7 identity;
- `DUR-02` gives a common PostgreSQL transaction, retry, durable-audit/outbox, acknowledgement, PITR and schema-evolution discipline;
- `ANL-01` gives stable OperationId/TransactionId/EventId semantics and a durable audit complete-set model;
- `FND-02` gives ordered CommandRef semantics and prevents a reserved command from executing twice in one GameSession;
- `FND-03`/`FND-04` give runtime ownership, GameSession/CharacterLease and recovery fencing.

What remains is the item/value-specific proof:

```text
one live concrete item
-> exactly one authoritative immediate location

one logical atomic durable mutation
-> exactly one TransactionId
-> same semantic intent through retry / ambiguous commit

pure movement / split / merge
-> no unauthorized creation or disappearance of units/value

mint / burn / transform / conversion
-> explicit typed cause + complete input/output lineage

stale authority / duplicate command / crash / lost response
-> cannot cause a second authoritative effect
```

The recommended architecture therefore uses:

1. a **typed immediate-location graph** rather than ambiguous owner/location columns;
2. explicit **lifecycle transition rules** for create, retire, split, merge, quantity transfer and type transform;
3. a **closed transaction mutation set** with stable TransactionId and optional cross-transaction OperationId;
4. conservation by **asset/item lineage and authorized source/sink classification**, not by economic-price equality;
5. one game-owned PostgreSQL atomicity boundary for v1 durable value transactions, with no implicit cross-database distributed transaction;
6. explicit typed custody for staged workflows that span multiple transactions;
7. mandatory ANL-compatible durable evidence fixed before any possibly ambiguous commit;
8. restore/recovery gates that prove uniqueness, lineage, receipt and authority invariants before mutation resumes.

## 2. Verified source facts

### 2.1 GAME-ITEM-01

**PROVEN:** `GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md` establishes:

- stable versioned ItemType definitions versus concrete ItemInstances;
- one `ItemInstanceId` per live concrete instance;
- StaticItemPlacement is not automatically a durable ItemInstance;
- one stack is one ItemInstance; stack units do not get separate IDs solely because quantity > 1;
- quantity zero is not a live stack state;
- equipment legality is a complete atomic occupancy claim;
- container legality requires an acyclic bounded containment graph;
- ItemInstance current location is deliberately DUR-03-owned;
- create/destroy/split/merge/transform identity transitions are deliberately DUR-03-owned;
- world scope, binding/restriction, current location, authorization and presentation ownership are distinct;
- physical currency items and non-item ledger value are distinct models;
- transfer-surface eligibility is not a transaction implementation;
- exact Reference item behavior remains parity-gated where not evidenced.

### 2.2 DUR-01

**PROVEN:** `DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md` establishes:

```text
ItemInstanceId
= strong UUIDv7
= full 128 bits
= nil invalid
= never reused
= restricted/internal by default
```

It explicitly forbids using UUIDv7 ordering as authority/chronology and leaves lifecycle transitions to DUR-03.

### 2.3 DUR-02

**PROVEN:** `DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md` establishes:

- no blanket isolation level replaces an invariant/anomaly proof;
- application-only check-then-write is insufficient for correctness-sensitive ownership/value invariants;
- retries preserve semantic operation identity;
- stricter DUR-03 transaction rules may refine the common baseline;
- authoritative mutation + required durable evidence + publication state commit in one owning PostgreSQL transaction;
- acknowledged durable success means committed state recoverable across ordinary restart;
- ambiguous/lost response after commit is reconciled, not blindly re-executed;
- production persistence must be PITR-capable/restore-tested and authority remains closed until post-restore reconciliation passes;
- schema evolution is expand/migrate/validate/cut-over/contract;
- item/currency/value conservation is moved explicitly to DUR-03.

### 2.4 ANL-01

**PROVEN:** `ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md` establishes:

- `OperationId` = one retry-capable logical operation;
- `TransactionId` = one logical atomic durable mutation transaction;
- ambiguous commit/retry retains the same TransactionId;
- a new TransactionId requires the prior logical transaction to be proven terminal and a new logical transaction to begin intentionally;
- `TransactionEventRef` describes the complete ordered durable event set of one transaction;
- all mandatory DURABLE_AUDIT evidence commits atomically with the owning mutation;
- same EventId retry/redelivery preserves exact immutable event semantics;
- replay never replays gameplay mutation;
- analytics/investigation are observational/read-only, never gameplay repair authority.

### 2.5 FND-02

**PROVEN:** `FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md` establishes:

```text
CommandRef = (GameSessionId, CommandId)
```

with monotonic CommandId reservation, exactly one authoritative execution identity, bounded outstanding commands, duplicate non-reexecution, ordered authoritative commit and safe reconciliation across eligible same-GameSession reconnect.

A connection-generation change does not create a new CommandRef namespace because the same GameSession survives eligible reconnect.

### 2.6 FND-03/FND-04

**PROVEN:** accepted runtime/admission architecture separates:

- GameSession identity;
- current TransportBinding / connection_generation;
- CharacterLease generation;
- runtime scope ownership generation.

Identity or item binding alone never grants mutation authority.

### 2.7 Current programme status

**PROVEN:** `main@2521882253b04287e1243c54692440120e0b6c8e` records:

```text
GAME-ITEM-01  ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
DUR-03        PROPOSED / PLANNED / NOT_STARTED
```

DUR-03 is the next eligible paper-only item/value architecture gate. No runtime/DDL/production authority exists.

## 3. Problem statement

Without DUR-03, multiple individually reasonable implementations can still duplicate or lose value:

- one item can appear in inventory and ground state simultaneously;
- stale runtime ownership can commit after a newer channel/lease owner exists;
- a lost DB response can cause a retry with a new transaction identity and double mint;
- a split can accidentally reuse one ItemInstanceId for two live stacks;
- a merge can retire the wrong instance and resurrect it later;
- a transform can silently reinterpret identity across incompatible item types;
- a container move can leave descendants orphaned or cyclic;
- trade/market/reward flows can treat “escrow” as a flag while the item remains usable in inventory;
- a bank/currency update can debit one side without a matching credit/source/sink lineage;
- restore can resume old sessions that repeat operations committed before the restored point;
- analytics can detect a duplicate after the fact but cannot undo gameplay safely.

The architecture must prevent these failures before production code exists.

## 4. Constraints

### 4.1 Safety constraints

- no live ItemInstanceId reuse;
- no item can have two authoritative immediate locations after commit;
- no location/custody metadata may be treated as authorization;
- no client-supplied item state, quantity, value or location is authoritative;
- no stale GameSession/CharacterLease/runtime owner may commit item mutation;
- no blind retry after an ambiguous durable outcome;
- no committed mutation may omit mandatory durable audit evidence;
- no cross-world gameplay value transfer by default;
- no cross-database item/value transaction is assumed atomic;
- no binary floating-point arithmetic may be the authoritative conservation basis;
- no unbounded transaction participant set, nested container expansion or audit payload.

### 4.2 Product/parity constraints

- first Reference target remains the accepted production-observable Global Tibia cut after 2026-07-28;
- unknown exact target behavior remains `PARITY_PENDING_EVIDENCE`;
- anti-duplication/security/integrity overrides defect compatibility;
- market prices or historical economy state are not the conservation oracle;
- future Evolved behavior must remain explicit/versioned, not a hidden branch in persistence code.

### 4.3 Architecture boundaries

DUR-03 must not absorb:

- GAME-ITEM item/equipment/container semantic legality;
- loot generation policy;
- market/order-book business state;
- trade consent/state machine;
- bank/depot/mail access policy;
- reward eligibility;
- house ownership/rent/placement policy;
- crafting recipes/formulas;
- entitlement purchase/activation policy;
- FND transport/session/runtime mechanics;
- physical PostgreSQL schema/driver/migration library;
- analytics enforcement or automatic repair.

## 5. Decision 1 — authoritative item location model

### 5.1 Option A — separate owner/location flags by subsystem

Example:

```text
inventory_owner_character_id
container_parent_item_id
ground_tile
market_offer_id
mail_id
...
```

Benefits:

- superficially simple subsystem queries.

Problems:

- multiple fields can be populated simultaneously;
- each new subsystem creates another source of authority;
- moving between surfaces becomes multi-authority cleanup;
- schema defaults or partial failures can duplicate presence;
- an `owner_id` field inevitably conflates custody, binding and authorization.

**REJECT.**

### 5.2 Option B — one typed immediate-location relation

Each live ItemInstance has exactly one immediate authoritative location from a registered typed location family.

Core semantic examples:

```text
CharacterInventory(CharacterId, typed inventory position)
CharacterEquipment(CharacterId, semantic equipment claim)
Container(parent ItemInstanceId, typed container entry)
Ground(WorldId, ChannelId|InstanceId, typed spatial position)
TypedDomainCustody(domain-owned stable custody reference)
```

The exact persistence representation is not frozen.

Rules:

- one live item => one immediate location;
- nested descendants point to their immediate parent container, not every ancestor;
- moving a container changes the container's own location; descendants remain located in that container;
- every location family has an explicit domain owner, validation/authorization owner and scope;
- no arbitrary free-form location string/JSON/EAV family is canonical;
- downstream custody families such as trade escrow, market escrow, depot/mail/reward custody require their owning gate before activation.

Benefits:

- one source of presence truth;
- container moves do not rewrite entire subtrees;
- prevents “still in inventory but also in escrow” designs;
- new transfer surfaces extend a registry instead of adding competing authority columns.

Risks:

- implementation must prove uniqueness and typed-reference integrity;
- queries may require joins/projections;
- cross-authority location families require explicit coordination.

**RECOMMEND.**

## 6. Decision 2 — lifecycle and ItemInstanceId transitions

DUR-01 says IDs are non-reused but does not define which operation preserves or replaces one lifecycle.

### 6.1 State mutation

A legal mutation of typed state on the same concrete item lifecycle preserves ItemInstanceId.

Examples include, where GAME-ITEM/ruleset permits:

- charge consumption/restoration;
- durability change;
- binding/restriction state;
- compatible modifier/upgrade state;
- quantity change on an existing stack when no second concrete stack lifecycle is created.

### 6.2 New concrete instance

Whenever an operation creates an additional independently locatable concrete item lifecycle, a fresh ItemInstanceId is mandatory.

Examples:

- creating a non-stackable item;
- creating a new stack object;
- splitting quantity into a new independently locatable stack;
- replacement-style transform output.

### 6.3 Retirement

When the concrete lifecycle no longer exists, its ItemInstanceId becomes terminal and is never reused.

Examples:

- destroy/burn of the final quantity/object;
- full merge consumption of a source stack;
- replacement transform of the old item;
- terminal decay outcome when item semantics remove the instance.

### 6.4 Split

For source stack `S` quantity `q` and split amount `x`:

```text
0 < x < q
S keeps ItemInstanceId, quantity q-x
new stack N gets fresh ItemInstanceId, quantity x
```

A “split” of all quantity is not a split; it is a move of the existing instance.

### 6.5 Quantity transfer / merge

When moving amount from stack A into compatible existing stack B:

- B keeps B's ItemInstanceId;
- A keeps A's ItemInstanceId if quantity remains positive;
- if A reaches zero, A is terminally retired;
- B may not exceed GAME-ITEM stack bounds;
- no temporary ItemInstance is required solely to account for fungible units, provided lineage records the quantity delta.

This avoids unnecessary mint/retire churn while preserving one stack = one ItemInstance.

### 6.6 Type transform

A type-changing transform cannot infer identity policy from ItemTypeKey similarity or serializer shape.

Every executable transform edge must have an explicit versioned identity transition policy:

- `PRESERVE_INSTANCE` — allowed only for a one-input/one-output transform where the owning rules prove it is the same concrete lifecycle and all resulting state is compatible;
- `REPLACE_INSTANCE` — old instance retires and output receives fresh ItemInstanceId;
- multi-input/multi-output transforms always define explicit consumed/surviving/new outputs; one ItemInstanceId can never become two live outputs.

If the identity policy for a target-sensitive transform is unevidenced, the transform remains fail-closed / parity-pending rather than guessing.

**RECOMMEND.**

## 7. Decision 3 — conservation model

### 7.1 Why “sum of market value” is wrong

Crafting, decay, loot, rewards, upgrades and currency conversion legitimately change item count/type and may not have a stable market price.

Therefore DUR-03 conservation is not:

```text
sum(price(inputs)) == sum(price(outputs))
```

### 7.2 Conservation categories

Every committed transaction classifies each mutation line as one of:

1. **TRANSFER** — existing value moves between locations/custodies; no mint/burn.
2. **SPLIT_MERGE_QUANTITY** — same asset/item-type units redistributed between stack instances; total units preserved.
3. **STATE_MUTATION** — same concrete instance changes legal typed state; no implicit mint/burn.
4. **MINT** — new item units/instances or non-item value appear under explicit typed source cause.
5. **BURN** — item units/instances or non-item value disappear under explicit typed sink cause.
6. **TRANSFORM** — explicit input set consumed/mutated and output set produced under a versioned transform rule.
7. **CONVERSION** — exact asset A debit/input and asset B credit/output under an explicit versioned conversion rule.

No generic unclassified signed “value delta” is accepted for authoritative conservation.

### 7.3 Exact arithmetic

Authoritative fungible amounts require a bounded exact representation defined by the owning asset contract. Binary floating point is forbidden as the conservation basis.

DUR-03 does not force all future assets to use one SQL scalar.

### 7.4 Lineage

Every mint/burn/transform/conversion must retain enough typed provenance to answer:

```text
what authoritative cause allowed this?
which exact input instances/quantities/value accounts participated?
which outputs were created or changed?
which transaction committed it?
was the same logical cause already applied?
```

Lineage is factual transaction provenance, not an economic valuation model.

**RECOMMEND.**

## 8. Decision 4 — transaction identity and idempotency

### 8.1 CommandRef

For player-initiated commands:

```text
CommandRef = (GameSessionId, CommandId)
```

remains the ingress identity/order owner under FND-02.

DUR-03 must not mint a different semantic operation merely because the transport reconnects or a response is lost.

### 8.2 TransactionId

Every logical atomic durable item/value mutation uses one ANL-01 TransactionId fixed before the first potentially ambiguous commit attempt.

Same logical transaction:

- same TransactionId across DB retry/serialization retry/ambiguous commit reconciliation;
- same semantic participants, causes and intended mutation set;
- conflicting reuse of the same TransactionId is an integrity conflict.

A new TransactionId means an intentionally new logical atomic transaction after the prior one is proven terminal.

### 8.3 OperationId

Use OperationId when one logical user/domain action:

- spans multiple durable transactions;
- can be retried across GameSessions/processes;
- has a domain-visible lifecycle or asynchronous continuation.

Examples may later include market/trade/mail/reward/crafting workflows, but their business semantics remain domain-owned.

CommandRef alone is sufficient only while the owning operation is semantically limited to that GameSession command namespace and state preconditions safely prevent cross-session replay.

### 8.4 Durable receipts

A correctness-sensitive item/value operation requires durable receipt/reconciliation state sufficient to determine:

- same semantic operation already committed;
- same operation currently/previously attempted but not yet safely classified;
- conflicting reuse of identity/cause;
- committed result reference necessary to prevent a second effect.

Exact table/layout/retention duration is deferred. Retention must cover the owning operation's replay/idempotency horizon; once-only source/grant keys cannot be forgotten while replay remains possible.

**RECOMMEND.**

## 9. Decision 5 — ambiguous commit and retry

A database/client/network timeout is not proof of rollback.

Required algorithmic contract:

```text
attempt durable transaction T
-> outcome known committed: return/reconcile committed result
-> outcome known aborted: retry T under same TransactionId when policy permits
-> outcome ambiguous: query/reconcile durable receipt/state for T
   -> found committed: return committed result
   -> proven not committed / safely aborted: retry same T
   -> cannot classify safely: fail/hold; never mint new T as a guess
```

A lost client response after commit does not authorize re-running the mutation under a new CommandRef/TransactionId without the owning domain's idempotency proof.

After commit, “rollback” is a new compensating transaction with a new TransactionId and explicit causation to the original transaction. History is not edited or deleted to pretend the first commit never happened.

**RECOMMEND.**

## 10. Decision 6 — atomic transaction participant set

Every transaction has a bounded closed participant/effect set before commit.

May include:

- existing ItemInstance states;
- immediate item locations;
- container/equipment occupancy claims;
- non-item fungible value accounts/asset lines;
- domain custody records;
- idempotency/receipt state;
- mandatory DURABLE_AUDIT evidence/publication state;
- authority/fence state necessary for correctness.

Required rules:

- participant count and nested traversal obey absolute security/resource ceilings registered before implementation acceptance;
- no unbounded “move entire arbitrary graph” transaction;
- container legality expansion is bounded by GAME-ITEM ceilings;
- implementation must define deterministic lock/acquisition ordering or use another proven anomaly-closing mechanism;
- READ COMMITTED is allowed only with an explicit DUR-02-compliant anomaly proof; otherwise SERIALIZABLE or stricter domain mechanism;
- deadlock/serialization retry preserves semantic operation and TransactionId.

Numeric transaction/item/value-line ceilings are not invented in this paper-only gate without workload/security evidence. Missing mandatory ceilings block implementation.

## 11. Decision 7 — container subtree semantics

GAME-ITEM makes containment a directed acyclic immediate-parent graph.

Recommended DUR-03 consequence:

- each contained item is immediately located in its parent container;
- moving a container changes only that container's own immediate location;
- descendants remain located in their parent containers;
- transaction validates any affected capacity/weight/policy facts required by GAME-ITEM;
- destroying/replacing a container with live descendants is illegal unless one bounded transaction explicitly relocates/transforms/retires every affected descendant required by the operation;
- no orphaned contained item may remain after commit.

This avoids rewriting large subtrees and preserves a single canonical graph.

## 12. Decision 8 — equipment transaction semantics

GAME-ITEM owns whether an equip pattern is legal. DUR-03 owns atomic value movement.

Equip/unequip transaction must make one indivisible authoritative result:

```text
old item locations/claims
+ complete new equipment occupancy claim
+ displaced item locations if any and explicitly allowed
+ affected derived/rebuildable materialized state where authoritative
+ required audit/receipt
-> commit all or none
```

No one-hand-half of a two-hand claim may commit.

Client/UI slot state is never the transaction authority.

## 13. Decision 9 — authority and stale-writer fencing

### 13.1 Player/character item operations

A mutation acting on Character-controlled value must be authorized by current accepted FND authority, including applicable:

- GameSession identity;
- CharacterLease generation/current lease ownership;
- command ingress identity/order;
- current runtime scope ownership generation where channel/instance state participates.

Item binding, CharacterId equality or possession metadata never substitutes for current authority.

### 13.2 Connection generation nuance

FND-02 permits pending reserved commands to survive an eligible reconnect of the same GameSession while connection_generation advances.

Therefore DUR-03 must **not** incorrectly require “the original transport generation is still current at DB commit” for every previously reserved command.

Instead it requires:

- command was accepted into authoritative ordered ingress under a valid binding;
- GameSession/CharacterLease/runtime authority has not become terminally invalid or superseded under FND-03/FND-04 rules;
- any domain-specific commit fence is current at the linearization point.

This preserves reconnect correctness while still rejecting stale owners.

### 13.3 Channel/instance-scoped ground state

A durable mutation of channel/instance-scoped ground/custody state must be fenced by the current runtime scope ownership generation or an equivalently proven persisted authority fence.

A stale GameNode/channel owner may not commit after ownership changes.

## 14. Decision 10 — one game-owned atomic DB boundary for v1

For the current `oteryn_game` persistence authority, a transaction claiming atomic item/currency/value mutation uses one game-owned PostgreSQL atomic transaction boundary under DUR-02.

DUR-03 does not invent distributed two-phase commit across Platform or future external services.

If a future transfer surface is owned by another database/service authority, it is `UNSUPPORTED` for direct atomic value transfer until a dedicated contract defines a safe custody/handoff protocol.

No cross-database foreign key or “best effort mirrored ownership” may create two simultaneous authorities.

**RECOMMEND.**

## 15. Decision 11 — multi-transaction workflows and custody

Some future business flows may intentionally span multiple durable transactions.

DUR-03 permits this only with:

- one stable OperationId for the logical workflow where needed;
- each committed sub-transaction independently conservation-safe;
- explicit typed intermediate custody/escrow location owned by the relevant domain;
- item no longer usable from its old location after custody transfer commits;
- restartable/idempotent workflow state;
- compensation as a new transaction, not hidden state rewind;
- no claim of end-to-end all-or-nothing atomicity across separate transactions unless a later contract proves it.

This allows safe market/trade/mail/reward workflows later without predesigning their business state machines.

## 16. Decision 12 — cross-world and cross-scope safety

Accepted default:

- a live ItemInstance stays in one WorldId value scope;
- direct cross-world item/currency/value transfer is forbidden;
- burning in world A and minting in world B is still a value transfer and cannot bypass the rule by being expressed as two transactions;
- a future world-transfer contract must explicitly preserve lineage, identity/value rules, balance policy, rollback/recovery and scope fencing.

Cross-channel character movement is not automatically an item transfer: Character inventory items remain located with the Character-level inventory/custody state unless an owning contract says otherwise.

Direct ground-to-ground movement between independent channel authorities is unsupported without an explicit handoff/custody owner.

## 17. Decision 13 — source/sink and materialization idempotency

Any operation that can create durable gameplay value needs a stable authoritative cause.

Examples conceptually include:

- loot output from one authoritative kill/loot-resolution operation;
- reward grant from one accepted reward occurrence;
- crafting output from one accepted craft operation;
- static placement materialization from one accepted placement occurrence;
- administrative compensation under later OPS-GM policy;
- explicit system source/sink policy.

DUR-03 does not decide whether those causes are valid business/gameplay causes. It requires that once a cause is accepted:

- retry cannot apply it twice;
- output lineage/ordinals are deterministic enough to reconcile duplicate attempts;
- duplicate cause + conflicting outputs is a conflict;
- materialization from StaticItemPlacement cannot duplicate the same one-shot placement occurrence through crash/retry;
- repeatable spawns/rewards require distinct authoritative occurrence identities rather than reusing one cause key indefinitely.

## 18. Decision 14 — mandatory durable evidence

DUR-03 should require one or more registered ANL-01 `DURABLE_AUDIT` records that make each committed item/value transaction independently reconcilable.

Minimum semantic evidence must identify, as applicable:

- TransactionId;
- OperationId and/or CommandRef/cause reference;
- WorldId and scoped runtime context where relevant;
- ruleset/content/item-definition revisions needed to interpret the mutation;
- every touched ItemInstanceId with before/after lifecycle disposition;
- immediate before/after location for moved/surviving instances;
- before/after ItemTypeKey/revision when transform changes it;
- exact stack/fungible quantity deltas where relevant;
- minted/retired/surviving identity outcomes;
- non-item asset/account debit/credit lines;
- source/sink/transform/conversion classification and rule/cause reference;
- transaction conservation summary sufficient for independent validation;
- relevant durable authority/fence references without exposing secrets/private proof material.

The event/evidence set is fixed before the first ambiguous commit and commits atomically with authoritative state.

This analysis does **not** select concrete protobuf event IDs or physical tables. Before implementation acceptance, the owning implementation/contract package must register concrete ANL event types/schema revisions and resource ceilings that implement this semantic evidence.

## 19. Decision 15 — restore/recovery reconciliation

Before authoritative item/value mutation resumes after disaster restore or integrity incident, reconciliation must prove at minimum:

- schema/migration revision supported;
- no duplicate live ItemInstanceId;
- each live ItemInstance has exactly one valid immediate location;
- container graph remains acyclic/bounded;
- no item references a retired/nonexistent required parent/custody;
- quantity/capability bounds remain valid;
- no TransactionId/OperationId receipt conflict;
- mandatory committed audit TransactionEventRef sets are complete where required;
- once-only source/cause keys are not duplicated;
- known non-item asset invariants reconcile;
- pre-restore GameSession/CharacterLease/runtime owners are fenced by DUR-02/FND recovery rules;
- no replay path re-executes gameplay commands or remints outputs from audit events.

If an invariant fails, recovery is fail-closed. Analytics may diagnose but may not auto-repair authority.

## 20. Error/failure categories required by the contract

DUR-03 needs stable semantic dispositions, with exact protocol/error IDs remaining later registry work where client-visible.

Minimum categories:

- invalid item/location/type/capability state -> `INVALID_INPUT` / no mutation;
- semantic eligibility rejected -> operation terminal rejection / no mutation;
- stale GameSession/CharacterLease/runtime authority -> conflict/stale-authority / no mutation;
- wrong world/scope -> conflict / no mutation;
- duplicate idempotent transaction/operation -> return/reconcile original result, no second mutation;
- same identity with conflicting intent -> integrity conflict, no overwrite;
- serialization/deadlock transient -> retry same semantic transaction within bounded policy;
- ambiguous commit -> reconciliation required, never blind new transaction;
- mandatory audit unavailable -> no commit where audit is mandatory;
- resource/participant bound exceeded -> capacity rejection, no partial mutation;
- unsupported transform/definition/ruleset revision -> unsupported revision, fail closed;
- internal conservation/location/lineage invariant violation -> internal unavailable/integrity failure, stop affected mutation path and preserve evidence.

## 21. Security threats and mitigations

### Duplicate command replay

Mitigation: FND-02 CommandRef reservation + DUR-03 durable operation/transaction receipts where cross-crash/cross-session idempotency requires them.

### Lost-response double mint

Mitigation: same TransactionId through ambiguous retry; reconcile receipt/state before retry/new operation.

### Stale server writer

Mitigation: CharacterLease/runtime ownership fencing at transaction boundary; stale owner cannot commit.

### Escrow double-use

Mitigation: escrow/custody is the immediate authoritative location, not a side flag.

### Container cycle/orphan exploit

Mitigation: GAME-ITEM acyclic legality + atomic immediate-parent transitions + no commit leaving orphan descendants.

### Split/merge ID duplication

Mitigation: explicit source-survivor/new-ID/retirement rules.

### Cross-world laundering

Mitigation: no default cross-world transfer; burn+mint does not bypass classification.

### Restore replay/remint

Mitigation: non-rollback authority fencing, receipt/cause reconciliation, audit replay read-only.

### Analytics-as-repair authority

Mitigation: ANL remains observational; compensation requires a new authorized domain transaction.

## 22. Player and producer review

### Player perspective

Benefits:

- progress/items are resilient to lag, reconnect, crash and retries;
- trade/equipment/container operations cannot visibly half-commit;
- lost responses reconcile instead of duplicating or deleting value;
- rollback/compensation history remains auditable;
- cross-world isolation protects economy integrity.

Potential cost:

- ambiguous or oversized operations may fail closed instead of “best effort” completing;
- unsupported/parity-unknown transforms may remain unavailable until evidence is known.

### Producer/developer perspective

Benefits:

- one location/transaction/lineage model avoids subsystem-specific anti-dup logic;
- later market/trade/mail/reward systems can consume typed custody rather than invent ownership;
- strong receipts/evidence make crash bugs reproducible;
- immediate-parent container semantics avoid large subtree rewrites.

Costs:

- requires disciplined transaction planning and bounded participant sets;
- requires durable idempotency semantics for high-risk multi-step operations;
- implementation must register real resource ceilings and event schemas before production acceptance.

## 23. Alternatives rejected

### “Database unique constraints are enough”

Rejected because uniqueness alone does not define legitimate mint/burn/transform, stale authority, retry identity, source-cause duplication or multi-item atomicity.

### “FND-02 CommandId alone solves idempotency”

Rejected because CommandRef scope is one GameSession; asynchronous/cross-session/multi-step value operations need domain OperationId/TransactionId/receipt semantics.

### “Event sourcing fixes duplicates”

Rejected. ANL-01 explicitly is not gameplay event sourcing; replay is read-only toward gameplay.

### “Use one generic transaction JSON blob”

Rejected because it creates untyped authoritative semantics, poor compatibility and unsafe hidden state expansion.

### “Every transform always keeps ItemInstanceId”

Rejected because replacement/crafting semantics can create genuinely new lifecycles.

### “Every transform always gets new ItemInstanceId”

Rejected because compatible one-to-one in-place lifecycle transformations may legitimately preserve identity; exact behavior must be explicit per transform rule/evidence.

### “Distributed transaction across Platform/game by default”

Rejected because Platform/game are separate authority/database boundaries and no accepted cross-database atomic commit protocol exists.

## 24. Architecture decision timing

### Must decide now?

**YES.**

### Concrete downstream work blocked

- durable inventory/equipment/container/ground transaction implementation;
- anti-duplication persistence implementation;
- durable loot/pickup vertical slice;
- safe future trade/market/depot/mail/reward item custody;
- item/currency Game Intelligence reconciliation proof;
- authoritative item/value failure/recovery tests.

### What becomes harder later?

Changing after durable item data exists would force migration of:

- item location authority representation;
- ItemInstanceId lifecycle lineage;
- idempotency receipts;
- source/sink provenance;
- transaction/audit interpretation;
- escrow/custody semantics;
- restore/recovery invariants.

A weak first model could permanently contaminate economy evidence and make duplicate cleanup ambiguous.

### Evidence that may justify supersession

- a proven Reference mechanic impossible to represent under explicit typed extension;
- PostgreSQL concurrency evidence showing an accepted invariant cannot be closed efficiently/safely under the current atomicity model;
- measured workload evidence requiring a different bounded custody/partition design;
- a future accepted cross-database/service custody architecture with equivalent single-authority/conservation proof;
- security/exploit evidence;
- legal/privacy requirements changing retained provenance;
- a later explicit owner decision changing world transfer/economy policy.

Convenience, OTS schema layout or market-price assumptions are insufficient.

### Deliberately not decided

- SQL tables/constraints/indexes/isolation statements/lock syntax;
- exact Rust crates/transaction APIs;
- numeric transaction participant/resource ceilings without evidence;
- concrete ANL event IDs/protobuf payloads;
- exact Reference transform/split/merge/crafting/reward/decay policies not evidenced;
- market/trade/bank/depot/mail/reward/house business state machines;
- cross-world transfer feature policy;
- external service/database custody protocol;
- production RPO/RTO/backup cadence;
- automatic anomaly remediation.

## 25. Recommendation

Accept a DUR-03 contract with the following irreducible core:

```text
LIVE ITEM
= one ItemInstanceId
+ one WorldId value scope
+ one typed immediate authoritative location
+ legal GAME-ITEM state

ATOMIC VALUE TRANSACTION
= one stable TransactionId
+ optional stable OperationId / CommandRef / cause
+ bounded closed participant set
+ current authority/fence proof
+ exact legal before/after mutation set
+ explicit transfer/mint/burn/transform/conversion classification
+ atomic durable receipt + mandatory audit evidence

COMMIT
= all authoritative state + required evidence
OR none

RETRY / LOST RESPONSE
= reconcile same semantic transaction
NEVER guess a second transaction

MULTI-STEP WORKFLOW
= explicit typed custody + OperationId
+ each committed step independently conservation-safe

RECOVERY
= fail closed until location/identity/receipt/lineage/authority invariants reconcile
```

This closes the architecture needed for durable item/value implementation while keeping business gameplay policy, physical schema and production rollout appropriately downstream.
