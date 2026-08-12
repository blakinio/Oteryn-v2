# DUR-03 — Item Transaction and Anti-Duplication Contract

- Date: 2026-08-12
- Gate: `DUR-03`
- Delivery task: `OTV2-20260812-dur-03-item-transaction-architecture`
- Delivery PR: #207
- Status on delivery branch: **CANDIDATE / NONBINDING**
- Canonical semantic effect: only after accepted delivery merge; programme `ACCEPTED / LIFECYCLE_CLOSED` promotion requires a separate lifecycle closeout
- ImplementationStatus: **NOT_STARTED**
- Runtime authority: **NONE**
- PostgreSQL DDL/migration authority: **NONE**
- Production authority: **NONE**
- Analysis source: `DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_ANALYSIS.md`

## 1. Purpose

Freeze the minimum native transaction and anti-duplication semantics required before any implementation may claim authoritative durable item/currency/value correctness.

This contract owns:

- one authoritative immediate location for every live ItemInstance;
- create/retire/split/merge/quantity-transfer/transform ItemInstanceId transition rules;
- item/currency/value transfer, mint, burn, transform and conversion conservation semantics;
- stable transaction/operation identity through retry and ambiguous commit;
- durable idempotency and reconciliation obligations;
- authority/fencing requirements for durable value mutation;
- bounded atomic participant/effect rules;
- safe typed custody for multi-transaction workflows;
- mandatory durable provenance/evidence sufficient for independent anti-duplication reconciliation;
- restore/recovery item/value integrity gates;
- cross-world and cross-authority fail-closed behavior.

It does **not** own runtime code, physical PostgreSQL schema, wire payloads, item legality, market/trade business policy, exact Reference formulas/rates or production rollout.

## 2. Authority chain

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

Where older coordination prose conflicts with later accepted FND-02/FND-04 authority semantics, the accepted component contracts and current-status overlay govern; DUR-03 does not revive historical `session_generation` or Gateway-issued canonical GameSession assumptions.

## 3. Core safety theorem

For every committed logical durable value transaction `T`, a conforming implementation must prove:

1. `T` has exactly one semantic TransactionId.
2. Every pre-existing live ItemInstance touched by `T` is accounted for exactly once in the committed effect set.
3. Every surviving live ItemInstance has exactly one authoritative immediate location after `T`.
4. Every newly created concrete ItemInstance has a fresh ItemInstanceId allocated to `T` and never assigned to another logical transaction/lifecycle.
5. Every retired ItemInstanceId is never reused.
6. Pure transfer/split/merge operations create or lose no conserved units/value.
7. Mint/burn/transform/conversion occurs only under an explicit typed authorized cause/rule and complete lineage.
8. Mandatory durable receipt/audit evidence commits atomically with the authoritative mutation.
9. Retry, duplicate command, stale authority, crash, timeout or lost response cannot create a second authoritative effect for the same logical transaction/operation.
10. Failed/aborted transactions leave no partial authoritative value mutation.

If one property cannot be proven for an operation class, that operation class is not DUR-03-conforming.

## 4. Canonical immediate-location model

### 4.1 Exactly one immediate location

Every live concrete ItemInstance has exactly one authoritative immediate location:

```text
ItemInstanceId -> exactly one ItemLocationRef
```

This is a semantic relation and does not freeze SQL table layout.

### 4.2 Typed location families

The model must be able to represent, as accepted owners require:

```text
CharacterInventory {
  character_id: CharacterId
  position: typed inventory position
}

CharacterEquipment {
  character_id: CharacterId
  occupancy: complete semantic equipment claim
}

Container {
  parent_item_instance_id: ItemInstanceId
  entry: typed container entry/position
}

Ground {
  world_id: WorldId
  runtime_scope: ChannelRef or InstanceRef
  spatial_position: typed world position
}
```

Future world-shared spatial state or downstream custody such as house/trade/market/depot/mail/reward custody is introduced only as a separately typed/versioned location/custody family with a named semantic owner and explicit WorldId/scope semantics.

### 4.3 `TypedDomainCustody` is not a generic escape hatch

`TypedDomainCustody` is an architecture registry concept, not one generic runtime record carrying arbitrary strings, JSON or EAV.

Each accepted custody family must define its own:

- stable semantic type/key;
- owner;
- scope;
- legal reference shape;
- lifecycle/compatibility semantics;
- authorization boundary.

### 4.4 Prohibited competing authorities

The following are rejected as canonical item-location authority:

- arbitrary location strings;
- generic JSON location objects;
- free-form EAV location fields;
- multiple independent nullable owner/location columns treated as peer authorities;
- a generic `owner_id` whose meaning changes by subsystem.

### 4.5 Binding, custody and authorization are distinct

An item's:

```text
WorldId value scope
binding/restrictions
immediate location/custody
current gameplay authorization
presentation ownership
```

remain distinct. Possession, CharacterId equality, binding or custody does not grant mutation authority.

## 5. Container immediate-parent semantics

GAME-ITEM-01 owns containment legality. DUR-03 freezes the transaction consequence:

- a contained item is immediately located in its parent container;
- moving a container changes the container's own immediate location, not each descendant relation;
- descendants remain located in their immediate parents;
- affected GAME-ITEM capacity/weight/type/nesting constraints required by the proposed operation validate before commit;
- destroying/replacing a container that still has live descendants is invalid unless the same bounded transaction explicitly relocates/transforms/retires every affected descendant required by the operation;
- no committed transaction may leave an orphaned live descendant or create a containment cycle.

## 6. Item lifecycle and identity transitions

### 6.1 Same concrete lifecycle preserves identity

A legal typed-state mutation on the same concrete item lifecycle preserves ItemInstanceId.

Examples, only where the owning item/ruleset semantics permit:

- charge change;
- durability change;
- binding/restriction change;
- compatible upgrade/modifier change;
- quantity adjustment of an existing stack when no additional independently locatable stack lifecycle is created;
- an explicitly identity-preserving one-to-one transform.

A state mutation that consumes or creates a bounded resource such as charges/durability still requires its owning typed cause/rule and before/after evidence; `STATE_MUTATION` is not permission for unexplained value drift.

### 6.2 New concrete lifecycle gets fresh identity

A fresh ItemInstanceId is mandatory whenever an operation creates a new independently locatable concrete ItemInstance lifecycle.

Examples:

- new non-stackable item;
- new stack object;
- split output stack;
- replacement transform output;
- concrete multi-output crafting/transform output.

### 6.3 Transaction-scoped output identities

Every new ItemInstanceId planned by a logical TransactionId is allocated before the first durable commit attempt that could make it authoritative and remains assigned to that logical transaction/output slot across physical retry.

Rules:

- a serialization/deadlock retry does not replace planned output ItemInstanceIds merely because the DB attempt aborted;
- an ambiguous commit must reconcile the same exact output identities;
- an output ID allocated to one TransactionId is never reassigned to another logical transaction, even if the original transaction later terminates without commit;
- no uncommitted output is exposed as an authoritative live item before commit.

This prevents retry identity drift from becoming duplicate-mint ambiguity.

### 6.4 Retirement

When a concrete lifecycle ceases to exist, its ItemInstanceId becomes terminal and is never reused.

Retention of retirement/tombstone evidence follows DUR-01/ANL/privacy requirements; DUR-03 does not require unlimited history solely to enforce the concept of non-reuse.

### 6.5 Quantity zero

GAME-ITEM-01 forbids quantity zero as live stack state. A transaction reducing a stack to zero retires that ItemInstance in the same atomic outcome.

## 7. Split semantics

For live stack `S` quantity `q` and split amount `x`:

```text
0 < x < q
```

Committed outcome:

```text
S:
  same ItemInstanceId
  quantity = q - x
  remains live

N:
  fresh transaction-scoped ItemInstanceId
  quantity = x
  independently locatable
```

Rules:

- `x == 0` invalid;
- `x >= q` is not a valid split;
- moving all quantity is a move of the existing instance, not split/new identity;
- source + output quantity equals pre-split quantity exactly;
- item revision/location/stack constraints validate atomically.

## 8. Quantity transfer and merge

For compatible live stacks A and B and exact amount `x` transferred A -> B:

- B retains B's ItemInstanceId;
- B quantity increases by `x` within accepted bounds;
- A quantity decreases by `x`;
- A retains A's ItemInstanceId if post-state quantity is positive;
- A retires if post-state quantity is zero;
- no temporary ItemInstance is required solely to represent fungible units between existing stacks;
- total conserved units are identical before/after a pure transfer/merge.

Client ordering or UUID ordering never selects semantic survivor/receiver.

## 9. Create/mint semantics

### 9.1 New concrete instance mint

A new concrete item/stack uses its transaction-scoped fresh ItemInstanceId from section 6.3.

### 9.2 Quantity mint into existing stack

A typed authorized source may increase quantity on an existing compatible stack without creating a temporary ItemInstance solely for newly produced fungible units.

Exact source/cause, quantity delta and resulting state remain part of transaction lineage/evidence.

### 9.3 Stable source occurrence

Every value-producing operation has an authoritative typed source/cause identity sufficient to prevent duplicate application.

Conceptual later-owned causes include:

- loot resolution occurrence;
- reward grant occurrence;
- crafting operation;
- StaticItemPlacement materialization occurrence;
- system source;
- administrative compensation.

DUR-03 does not decide whether the business cause is valid. It requires:

- one logical occurrence cannot mint twice through retry/crash;
- duplicate same occurrence reconciles the original result;
- same occurrence with conflicting output intent is an integrity conflict;
- repeatable sources use distinct authoritative occurrence identities.

## 10. Destroy/burn semantics

A burn/destruction transaction identifies:

- affected ItemInstance/quantity/value asset;
- typed sink/cause;
- whether the instance survives with reduced quantity/state or retires;
- required lineage/audit evidence.

Silent row deletion, persisted `quantity = 0`, or disappearance during error recovery is not a valid sink.

## 11. Transform semantics

### 11.1 Internal identity policy is explicit and versioned

Every executable type-changing transform edge has an Oteryn lifecycle identity policy:

```text
PRESERVE_INSTANCE
REPLACE_INSTANCE
```

This policy is an internal Oteryn integrity decision. It is **not** inferred from Global/Tibia ItemInstanceId behavior because the external Reference does not expose Oteryn's UUID identity.

Reference evidence constrains observable transform inputs/outputs and player-visible behavior. If observable transform semantics are unknown, that transform remains parity-pending/unsupported for claimed Reference execution; the internal UUID policy is not “discovered” from nonexistent Reference IDs.

### 11.2 `PRESERVE_INSTANCE`

Allowed only when:

- one concrete input maps to one concrete output;
- the versioned Oteryn transform rule explicitly declares the same lifecycle;
- resulting ItemType/capability state is fully defined/compatible;
- no second live output is created from the same ID.

### 11.3 `REPLACE_INSTANCE`

The old instance retires and each concrete output uses a fresh transaction-scoped ItemInstanceId.

### 11.4 Multi-input/multi-output

Every input has one explicit disposition: survives/mutates, quantity decreases, or retires.

Every concrete output is either:

- the one explicitly permitted identity-preserving survivor; or
- a fresh lifecycle with a fresh transaction-scoped ItemInstanceId.

One ItemInstanceId may never become two live outputs.

## 12. Conservation classifications

Every authoritative value mutation line has exactly one explicit semantic class:

```text
TRANSFER
SPLIT_MERGE_QUANTITY
STATE_MUTATION
MINT
BURN
TRANSFORM
CONVERSION
```

A generic unclassified signed value delta is prohibited.

### 12.1 `TRANSFER`

Existing live value changes immediate location/custody with no source/sink creation.

### 12.2 `SPLIT_MERGE_QUANTITY`

Units of one conserved stackable asset/type redistribute among stack instances; exact units are preserved.

### 12.3 `STATE_MUTATION`

One concrete lifecycle changes legal typed state under an explicit owning cause/rule. It cannot silently change stack quantity or non-item ledger balance outside their owning conservation class.

### 12.4 `MINT` / `BURN`

Value enters/leaves the live system only under explicit typed source/sink cause.

### 12.5 `TRANSFORM`

A versioned rule maps explicit inputs to explicit outputs and identity outcomes.

### 12.6 `CONVERSION`

A versioned rule maps exact asset-A inputs/debits to exact asset-B outputs/credits.

DUR-03 never infers conservation/conversion from market price or historical economy state.

## 13. Non-item fungible value

Non-item balances are not forced into ItemInstance.

For each authoritative non-item fungible asset:

- the owning domain defines stable asset identity/denomination and legal account/custody scopes;
- arithmetic uses bounded exact representation;
- binary floating point is not authoritative conservation arithmetic;
- pure transfer balances exact debits/credits for the same asset;
- net creation/destruction requires explicit mint/burn source/sink;
- conversion requires explicit versioned input/output asset rule;
- retry/ambiguous commit follows the same TransactionId/OperationId contract.

Exact SQL scalar and business semantics are deferred.

## 14. World-scope conservation

Every live ItemInstance belongs to one WorldId gameplay-value scope under GAME-ITEM-01.

- direct cross-world item/currency/value transfer is forbidden by default;
- burn in world A plus mint in world B is still semantically a cross-world transfer and cannot bypass the rule;
- a future dedicated world-transfer contract must define value/identity lineage, balance policy, custody, retry, rollback/recovery and authority fencing explicitly;
- DUR-03 does not authorize that feature.

## 15. Transaction identity

### 15.1 TransactionId

Every logical atomic durable item/currency/value mutation has exactly one ANL-01 TransactionId allocated before its first durable commit attempt.

TransactionId identifies logical atomic transaction **intent**, not a physical DB attempt.

Across physical attempts:

- TransactionId remains stable;
- source/cause, requested operation class, logical participants/destination semantics and transaction-scoped planned output identities remain the same logical intent;
- same TransactionId with a different business intent is an integrity conflict.

### 15.2 New TransactionId

A new TransactionId means the prior logical transaction is proven terminal and an intentionally new logical transaction begins.

A timeout alone is not proof of terminal abort.

## 16. CommandRef boundary

For player-originated commands:

```text
CommandRef = (GameSessionId, CommandId)
```

remains FND-02 authority for ordered ingress identity and duplicate non-reexecution.

DUR-03 consumes, but does not redefine:

- command reservation;
- bounded outstanding window;
- duplicate behavior;
- same-GameSession reconnect continuity.

A connection-generation change by itself does not create a new semantic command/transaction.

## 17. OperationId boundary

Use ANL-01 OperationId when the owning value workflow is logically retryable beyond one atomic transaction/CommandRef scope, including when it:

- spans multiple durable transactions;
- continues asynchronously;
- may be resumed/retried across GameSessions/processes;
- has durable workflow/custody lifecycle.

OperationId remains stable for the same logical operation.

DUR-03 does not require OperationId for every simple command whose semantics are fully bounded by CommandRef and authoritative preconditions.

## 18. Retry contract: known abort versus ambiguous commit

This distinction is binding.

### 18.1 Stable logical intent

A retry under the same TransactionId never changes the business intent, source/cause, requested mutation class, destination semantics or planned output identity slots.

### 18.2 Known non-committed abort

When a physical DB attempt is **proven non-committed** (for example a serialization/deadlock abort):

- same TransactionId and logical intent are retained;
- implementation may re-read current authoritative before-state and rematerialize legal mutable details/effect rows required to execute that same intent;
- transaction-scoped output ItemInstanceIds remain the same;
- if current state makes the same intent no longer legal, the transaction terminates/rejects instead of adapting into a different business operation;
- no external side effect from the aborted attempt may have escaped.

This allows anomaly-safe retry without creating a new semantic transaction.

### 18.3 Ambiguous commit

Once a physical commit attempt has an **ambiguous outcome**:

- its exact materialized candidate mutation set, planned output identities and mandatory evidence set are frozen for reconciliation;
- no different candidate may be attempted under that TransactionId until the ambiguous attempt is classified;
- durable receipt/state/evidence for that TransactionId is queried;
- found committed => reconcile/return that exact result;
- proven aborted/non-committed => retry same logical transaction under section 18.2;
- cannot classify safely => fail/hold; never mint a new TransactionId as a guess.

This prevents lost-response double mint while preserving valid known-abort retry.

## 19. Durable idempotency and receipts

Whenever FND-02 ingress + current authoritative state cannot alone prove replay safety, durable receipt/reconciliation state is mandatory.

It must distinguish at least semantically:

```text
NOT_APPLIED / safely retryable
COMMITTED / return original result
TERMINAL_REJECTED where owning domain persists it
AMBIGUOUS / reconciliation required
CONFLICT / same identity with different intent
```

Exact names/storage/retention durations are implementation-owned.

Retention must cover the owning replay/idempotency horizon; a once-only source/grant/occurrence key cannot be forgotten while replay remains possible.

## 20. Ambiguous outcome algorithm

```text
execute logical transaction T

if commit known successful:
    reconcile/return committed result

if attempt proven aborted and retry policy permits:
    retry same logical T / same TransactionId under current authoritative state

if commit outcome ambiguous:
    inspect durable receipt/state/evidence for the frozen candidate
    if committed:
        return/reconcile original committed result
    else if safely proven non-committed:
        retry same logical T / same TransactionId
    else:
        fail/hold
        DO NOT create a new transaction as a guess
```

## 21. Compensation after commit

Committed historical mutation/audit facts are immutable.

Correction uses a **new compensating transaction** with:

- a new TransactionId;
- causation/reference to the original transaction/operation;
- current authorization;
- complete conservation/source-sink evidence.

Direct historical row/audit rewrite is not compensation.

## 22. Atomic participant/effect set

Every physical commit attempt has a bounded closed materialized participant/effect set sufficient to prove its invariants.

It may include:

- ItemInstances and immediate locations;
- item capability/quantity state;
- equipment/container claims;
- non-item value accounts/asset lines;
- custody/workflow state;
- durable receipt/idempotency state;
- required authority/fence state;
- mandatory ANL durable audit + publication state.

The set cannot expand without bounds during commit.

## 23. Resource bounds

Before implementation acceptance, absolute security/resource ceilings are required for all variable-size transaction structures, including at minimum:

- touched ItemInstance count;
- location/custody mutation count;
- non-item value line count;
- transform input/output count;
- container graph validation expansion;
- workflow/custody participant count;
- mandatory audit event count/payload contribution;
- retry/reconciliation work per request.

Ruleset/product limits may be lower but never exceed absolute ceilings.

This paper-only candidate does not fabricate numeric ceilings without workload/security evidence. Missing mandatory ceilings block implementation; they never mean unlimited.

## 24. Isolation, locking and anomaly closure

DUR-02 remains binding:

```text
name invariant
+ identify authority rows/constraints
+ prove anomaly closure under selected isolation/locks/constraints
```

DUR-03 additionally requires:

- application-only check-then-write is insufficient for single-location/value-conservation correctness;
- deterministic lock/acquisition ordering or another proven anomaly-closing mechanism for multi-participant transactions;
- READ COMMITTED only with explicit invariant proof;
- otherwise bounded SERIALIZABLE or stricter accepted mechanism;
- deadlock/serialization retry preserves TransactionId/OperationId/CommandRef identity;
- advisory locks are not the sole durable authority for location, custody, uniqueness or conservation.

Exact SQL/lock syntax is deferred.

## 25. Player/character authority fencing

A transaction mutating Character-controlled value consumes current accepted FND authority as applicable:

- valid GameSession/CommandRef for player-originated intent;
- current CharacterLease authority/generation;
- current actor/domain preconditions;
- current runtime scope ownership generation for channel/instance-scoped participants.

Binding/location/ItemInstanceId/NodeId are not credentials. Client-supplied quantity/location/item state is intent only and is re-read/validated authoritatively.

## 26. Connection-generation nuance

FND-02/FND-04 permit eligible reconnect of the same GameSession with a newer connection_generation while preserving previously reserved pending CommandRefs.

Therefore DUR-03 does **not** require the old transport generation itself to remain current at DB commit for every valid already-reserved command.

It requires instead:

- the command was authoritatively reserved under a valid binding;
- logical GameSession/CharacterLease/runtime authority remains valid under FND continuation rules;
- no superseding/terminal authority transition invalidates the pending mutation;
- commit-time fences required by touched participants are current.

## 27. Channel/instance scope fencing

Any durable mutation touching channel/instance-scoped ground/custody state proves current runtime-scope ownership generation or an equivalently accepted durable fence at the transaction boundary.

A stale former GameNode/ChannelRuntime/InstanceRuntime owner cannot commit after authority moved. NodeId alone is not authority.

A future world-shared spatial owner such as an accepted house topology uses its own separately typed location/authority family rather than being silently encoded as channel-local ground.

## 28. Equipment atomicity

GAME-ITEM-01 owns equip legality/occupancy. DUR-03 requires equip/unequip to commit atomically with all authoritative location/occupancy consequences:

```text
all required old locations/claims released
+ complete new occupancy claim established
+ every displaced item legally located where displacement is permitted
+ required receipt/audit
OR
none becomes authoritative
```

Partial two-hand/mutually-exclusive occupancy is invalid.

## 29. Ground and inventory atomicity

Pickup/drop/move preserves:

- one immediate location before/after;
- correct WorldId/runtime scope;
- current authority/fences;
- container/inventory/equipment legality;
- no client-created item/quantity/location facts;
- same logical TransactionId across retry;
- mandatory receipt/audit where required.

Lost pickup response may reconcile committed inventory state; it can never justify a second ground/inventory copy.

## 30. Multi-transaction workflows and typed custody

A future value workflow may span multiple durable transactions only when each committed step is independently safe.

Pattern:

```text
stable OperationId where needed
-> transaction 1: move value into explicit typed custody
-> zero or more idempotent workflow steps
-> transaction N: move/transform value out of custody
```

Rules:

- custody is the immediate authoritative location/reference, not a boolean beside the old location;
- after custody commit, value is no longer spendable from its prior location;
- each step has its own TransactionId and is independently conservation-safe;
- workflow state is restartable/idempotent;
- no hidden end-to-end all-or-nothing claim spans separate commits;
- compensation is explicit new transaction;
- owning domain gate defines business lifecycle/eligibility.

## 31. Current database authority boundary

Under ADR-0004/DUR-02, current atomic DUR-03 v1 value mutation uses one game-owned PostgreSQL transaction inside the current `oteryn_game` persistence authority.

This contract does not authorize or define:

- Platform/game distributed 2PC;
- cross-database foreign keys;
- mirrored dual-authority item ownership;
- implicit remote-service atomicity.

A future external persistence/service custody boundary requires a dedicated safe handoff/custody contract before direct value transfer becomes supported.

## 32. StaticItemPlacement materialization

When gameplay materializes an authored StaticItemPlacement occurrence into durable mutable state:

- authoritative occurrence/cause identity is stable enough to deduplicate crash/retry;
- new concrete output uses transaction-scoped fresh ItemInstanceId;
- same one-shot occurrence cannot mint a second output;
- same occurrence with conflicting output intent is an integrity conflict;
- repeatable respawn/reset behavior uses distinct authorized occurrence identities under its owning content/gameplay contract.

DUR-03 does not define respawn/reset business policy.

## 33. Loot/reward/crafting source boundary

DUR-03 does not determine what loot drops, who is eligible, reward schedules, crafting recipes, market prices or entitlement benefits.

Any owning domain that produces/consumes durable value must provide a stable authoritative cause/rule context such that retry/recovery cannot apply the same logical output twice.

A transaction fixes its intended output/input identity slots and source/cause before durable commit. Physical retries preserve them.

## 34. Surface ownership boundary

| Surface | DUR-03 owns | Downstream owner retains |
|---|---|---|
| pickup/drop/ground/inventory | atomic location/conservation | movement/interaction eligibility |
| loot | mint/transfer idempotency/lineage | kill/loot generation/eligibility |
| trade | atomic exchange/custody safety | consent/lifecycle/policy |
| market | conservation/escrow safety | offer/fill/fee/pricing state machine |
| bank | exact item/ledger transfer/conversion | banking/economy policy |
| depot | item move/custody conservation | access/depot semantics |
| mail | item custody/move conservation | address/delivery lifecycle |
| rewards | mint/transfer idempotency | eligibility/schedule |
| houses | placement/move conservation | ownership/access/rent/topology |
| crafting/upgrades | input/output lineage | recipes/formulas/eligibility |
| entitlements | game-value delivery conservation if later accepted | Platform/payment/consumer activation policy |

No surface becomes accepted merely because DUR-03 supplies transaction/custody primitives.

## 35. Mandatory durable evidence

ADR-0006 classifies security-relevant item/currency mutations as durable economy/security audit. Therefore every authoritative DUR-03 item/value transaction emits ANL-01-compatible durable evidence sufficient to reconcile its effects.

The evidence may aggregate multiple touched mutation lines into one or more **bounded** transaction events/payloads. DUR-03 does not require one event per item/line.

If required evidence cannot fit accepted hard ceilings, the operation must use a safe bounded/staged design or reject. It may not emit an unbounded audit event.

Minimum semantic evidence, as applicable:

- TransactionId;
- OperationId and/or CommandRef/cause;
- WorldId and relevant channel/instance/runtime scope;
- exact ruleset/content/item-definition revisions needed to interpret the mutation;
- touched ItemInstanceIds;
- lifecycle disposition of each touched instance: survived/minted/retired or equivalent typed meaning;
- immediate before/after location for moved/surviving instances;
- ItemType/revision transition when changed;
- exact quantity/non-item asset lines;
- mutation classification: transfer/split-merge/state/mint/burn/transform/conversion;
- typed source/sink/transform/conversion cause/rule;
- conservation summary sufficient for independent validation;
- relevant safe authority/fence references without secret credential/proof material.

The exact materialized evidence candidate for a physical commit attempt is fixed before that attempt can become ambiguous and commits atomically with authoritative state.

## 36. ANL event-schema boundary

This architecture candidate does not allocate speculative gameplay event IDs or select final protobuf payload layout.

Before implementation claims DUR-03 conformance, the owning implementation/contract package must register concrete ANL-01 event types/schema revisions and resource ceilings implementing section 35.

That registration preserves:

- EventId immutability;
- TransactionEventRef complete-set rules;
- exact payload-byte retry stability;
- privacy/retention policy;
- replay read-only behavior;
- no high-cardinality ItemInstanceId metrics labels.

## 37. Durable acknowledgement

For a DUR-03 mutation declared durable:

```text
success acknowledged
=> owning PostgreSQL transaction committed
=> required durable receipt/audit committed
=> ordinary process/GameNode restart can reconstruct the committed result
```

Runtime checkpoint, network send or in-memory state is not durable success.

Lost response after commit reconciles committed state rather than reapplying mutation.

## 38. Restore and disaster recovery

DUR-02 PITR/recovery remains binding.

Before authoritative item/value mutation resumes after restore/integrity incident, implementation validates at least:

- supported schema/migration history;
- each live ItemInstanceId is valid/unique and consistent with available retained retirement/non-reuse evidence required by policy;
- every live ItemInstance has exactly one valid immediate location;
- parent containers/custodies exist and container graph is bounded/acyclic;
- no zero/overflow quantity or incompatible definition reinterpretation;
- TransactionId/OperationId/source-cause receipt uniqueness has no conflict;
- mandatory retained audit TransactionEventRef sets are complete where required;
- non-item asset invariants reconcile;
- restored pre-loss GameSession/CharacterLease/runtime authority is fenced by a newer accepted recovery fence;
- audit replay does not execute gameplay/remint outputs.

Integrity failure keeps affected authoritative mutation closed until an explicit safe repair/compensation path is accepted.

## 39. Analytics/Game Intelligence boundary

Game Intelligence may reconcile evidence, detect impossible duplicate location/lineage/value patterns, raise alerts/cases and reconstruct provenance.

It may not mutate item/value authority, auto-delete/merge duplicates, mint compensation, rewrite history, sanction automatically under DUR-03 or bypass domain authorization.

Correction uses a new typed authorized transaction under the appropriate gameplay/admin/security contract.

## 40. Fail-closed dispositions

| Condition | Category | Required effect |
|---|---|---|
| invalid item/location/capability/type state | `INVALID_INPUT` | no authoritative mutation |
| semantic item/equipment/container rule rejected | owning rejection category | no mutation |
| wrong WorldId/runtime scope | `CONFLICT` | no mutation |
| stale GameSession/CharacterLease/runtime owner | stale-authority `CONFLICT` subtype | no mutation |
| duplicate same semantic transaction/operation | idempotent reconciliation | no second mutation |
| same TransactionId/OperationId/source identity with conflicting intent | integrity `CONFLICT` | no overwrite/reinterpretation |
| proven serialization/deadlock abort | retryable internal/transient category | bounded retry same logical identity |
| ambiguous commit | reconciliation required | no blind new TransactionId/candidate |
| participant/resource limit exceeded | `CAPACITY_EXCEEDED` | no partial mutation |
| unsupported transform/definition/ruleset revision | `UNSUPPORTED_REVISION` | fail closed |
| mandatory audit cannot commit | `DEPENDENCY_UNAVAILABLE` or owning internal category | no authoritative mutation where audit mandatory |
| internal location/conservation/lineage violation | `INTERNAL_UNAVAILABLE` / integrity | stop affected path; preserve evidence |

Exact client-visible codes remain owning protocol/domain registry work.

## 41. Client presentation boundary

Client UI state, drag/drop source slots, optimistic visuals or cached inventory snapshots do not define transaction authority.

Server may reconcile committed state through FND-02 domain revisions/snapshots/deltas. A stale-view rejection does not change conservation semantics.

## 42. Derived/materialized state

A derived index/projection/summary is either:

1. atomically maintained when it participates in correctness; or
2. explicitly rebuildable/non-authoritative from committed source state.

No cache/projection becomes a second item-location authority.

## 43. Definition revision compatibility

Every transaction interprets touched items under explicit compatible GAME-ITEM definition/ruleset/content revisions.

- no silent reinterpretation because ItemTypeKey is unchanged;
- `MIGRATION_REQUIRED` state is not mutated under a new meaning until accepted migration/validation;
- unsupported mixed revision fails closed;
- transform/conservation evidence retains sufficient historical revision context.

## 44. Session recovery consequence

If transaction state is committed when response/session continuity fails:

- committed durable result remains authoritative;
- reconnect/recovery cannot replay it as new;
- reconciliation uses retained command/operation/transaction receipt/evidence where available;
- if same-GameSession resume cannot reconstruct command state safely, FND-02/FND-04 may terminate that session, but committed item/value state is not rolled back for session convenience.

## 45. Multichannel invariants

- Character-held durable value is not channel-owned solely because Character currently plays on one channel;
- channel/instance ground state remains runtime-scope fenced;
- stale channel owner cannot write durable ground value after ownership-generation change;
- direct durable transfer between independent live channel/instance ground authorities is unsupported without explicit one-winner handoff/custody coordinator;
- cross-channel relog/recovery cannot duplicate inventory because each live ItemInstance retains one immediate location plus current Character authority relation.

## 46. Security invariants

Mandatory:

- no client authority for item identity, quantity, location, source/sink or currency balance;
- no arbitrary authoritative transaction/location JSON/EAV escape hatch;
- no unbounded participant graph;
- no cross-world laundering by burn+mint;
- no conflicting same cause/OperationId/TransactionId last-write-wins;
- no raw SQL/admin mutation as ordinary gameplay correction;
- no ItemInstanceId reuse/reassignment;
- no binding/location metadata as session authority;
- no stale GameNode/lease owner commit;
- no mandatory audit downgrade to best-effort telemetry;
- no audit replay as gameplay replay;
- no automatic analytics repair authority.

## 47. Required implementation evidence

Any future implementation claiming DUR-03 conformance proves on exact revisions at least:

### Identity/location

- create fresh output ID and no cross-transaction reassignment;
- split source/new-ID behavior;
- partial/full merge survivor/retirement behavior;
- preserve/replace transform fixtures;
- one immediate location across inventory/equipment/container/ground/custody;
- container root move without descendant rewrite/orphan;
- cross-world rejection.

### Idempotency/concurrency

- duplicate same CommandRef no second execution;
- same TransactionId retry no second effect;
- transaction-scoped planned output IDs stable through retry;
- conflicting same TransactionId rejected;
- known serialization/deadlock abort rematerializes same logical intent safely;
- ambiguous commit freezes/reconciles exact candidate before retry;
- lost response after commit returns original result;
- stale CharacterLease rejected;
- stale runtime ownership generation rejected;
- same-GameSession reconnect does not duplicate pending valid command effect.

### Conservation

- pure move preserves instance/value;
- split/merge quantities balance exactly;
- mint/burn require cause;
- duplicate mint cause rejected/reconciled;
- transform complete input/output lineage;
- non-item ledger debit/credit exact conservation;
- conversion fixtures use exact accepted rule;
- compensation is a new causally linked transaction.

### Atomicity/failure

- crash before commit => no authoritative mutation/audit;
- crash after commit before response => committed state/evidence recoverable;
- publication crash => EventId-stable at-least-once publish, no gameplay replay;
- equipment multi-slot move all/none;
- custody transfer cannot leave old-location spendability;
- participant/evidence bound overflow rejects without partial state.

### Restore

- restore detects duplicate location/receipt/cause conflicts;
- pre-restore authority fenced;
- audit replay cannot remint;
- integrity failure keeps mutation closed.

### Evidence

- concrete registered ANL durable-audit event schemas/types;
- TransactionEventRef complete-set/gap/duplicate tests;
- bounded aggregated evidence payload/event count;
- privacy/retention profiles;
- no ItemInstanceId high-cardinality metrics labels.

Architecture acceptance alone proves none of these runtime outcomes.

## 48. Decision timing

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

Changing after durable history exists can require migration of location authority, ItemInstanceId lineage, receipts/idempotency keys, source/sink provenance, transaction evidence interpretation, custody and restore verification.

### Supersession evidence

Reopen only with named evidence such as:

- proven externally observable Reference mechanic incompatible with the typed extension model;
- PostgreSQL anomaly/correctness proof showing accepted atomicity cannot safely close a required operation;
- measured scale evidence requiring a different bounded partition/custody architecture;
- exploit/security evidence;
- future accepted cross-service/database custody protocol with equivalent one-authority/conservation guarantees;
- privacy/legal retention constraints;
- explicit later owner world-transfer/economy policy.

OTS schema layout, framework/library preference or convenience is insufficient.

### Deliberately not decided

- physical SQL schema/index/constraint/lock syntax;
- concrete Rust transaction API/crates;
- numeric transaction/resource ceilings without evidence;
- concrete ANL event IDs/protobuf payloads;
- exact unevidenced Reference source/sink/transform/crafting/decay/trade/market/bank/depot/mail/reward rules;
- downstream business state machines;
- cross-world transfer feature;
- cross-database/service atomic transfer protocol;
- production RPO/RTO/topology/backup cadence;
- automatic remediation.

## 49. Acceptance consequence

Only after:

1. candidate delivery passes exact-head self-review;
2. required genuinely independent review has zero open material findings;
3. exact-head governance/document CI passes;
4. review threads/ownership conflicts are clean;
5. PR #207 is squash-merged unchanged; and
6. a separate lifecycle closeout atomically promotes maintained programme status/handoff,

may programme state become:

```text
DUR-03
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
Runtime authority    = NONE
DDL/migration authority = NONE
```

Architecture acceptance does **not** authorize item/value runtime implementation or production mutation. A later implementation task requires separate owner authority and the evidence in section 47.
