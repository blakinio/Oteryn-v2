# DUR-03 — Item Transaction and Anti-Duplication Analysis

- Date: 2026-08-12
- Gate: `DUR-03`
- Delivery task: `OTV2-20260812-dur-03-item-transaction-architecture`
- Delivery PR: #207
- Status: **ANALYSIS / CANDIDATE INPUT; nonbinding while PR #207 is open**
- Runtime authority: **NONE**
- PostgreSQL DDL/migration authority: **NONE**
- Production authority: **NONE**

## 1. Executive summary

`DUR-03` closes the correctness gap between accepted item semantics and any future implementation that moves, creates, destroys, transforms or exchanges durable gameplay value.

Upstream architecture is already sufficient to define this boundary without inventing SQL or runtime code:

- `GAME-ITEM-01` defines ItemType/ItemInstance/StaticItemPlacement, legal item state, equipment/container legality, world scope and definition compatibility;
- `DUR-01` defines strong non-reused `ItemInstanceId`;
- `DUR-02` defines the common PostgreSQL transaction/retry/outbox/durable-ack/PITR/evolution substrate;
- `ANL-01` defines EventId/OperationId/TransactionId/TransactionEventRef and durable evidence semantics;
- `FND-02` defines ordered `CommandRef = (GameSessionId, CommandId)` reservation and duplicate non-reexecution;
- `FND-03`/`FND-04` define runtime ownership and GameSession/CharacterLease recovery fences;
- ADR-0006 requires durable economy/security evidence for item creation/destruction, split/merge, ownership/location changes, loot, pickup, trade, market, mail, depot, rewards, currency changes and retry/commit resolution.

The recommended architecture is:

```text
LIVE ITEM
= one ItemInstanceId
+ one WorldId value scope
+ exactly one typed immediate authoritative location
+ legal GAME-ITEM state

ATOMIC DURABLE VALUE TRANSACTION
= one TransactionId
+ stable logical intent/cause
+ bounded materialized participant/effect set
+ current authority/fence proof
+ explicit TRANSFER / SPLIT_MERGE / STATE_MUTATION /
  MINT / BURN / TRANSFORM / CONVERSION classification
+ durable receipt + mandatory ANL-compatible audit

COMMIT
= all authoritative mutation + required evidence
OR none

AMBIGUOUS OUTCOME
= reconcile the same commit candidate / same TransactionId
NEVER guess a second transaction

KNOWN ABORT
= same logical TransactionId/intent may be rematerialized from current authoritative state
  under bounded retry policy, because the prior attempt is proven non-committed

MULTI-TRANSACTION WORKFLOW
= OperationId where needed
+ explicit typed custody
+ each committed step independently conservation-safe
```

## 2. Verified source facts

### 2.1 GAME-ITEM-01

**PROVEN:** accepted `GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md` establishes:

- ItemType is a stable versioned authored semantic definition;
- ItemInstance is one concrete mutable lifecycle using DUR-01 `ItemInstanceId`;
- StaticItemPlacement is not automatically a durable ItemInstance;
- one stack is one ItemInstance; units in the stack do not each receive IDs;
- quantity zero is not a live stack state;
- equipment legality is a complete atomic occupancy claim;
- container legality is a bounded acyclic immediate-parent graph;
- current authoritative item location is deliberately DUR-03-owned;
- create/destroy/split/merge/transform identity transitions are deliberately DUR-03-owned;
- world scope, binding, current location, authorization and presentation ownership remain distinct;
- physical currency items and non-item ledger value are distinct;
- exact Reference behavior remains fail-closed when evidence is missing.

### 2.2 DUR-01

**PROVEN:** accepted durable representation defines:

```text
ItemInstanceId
= strongly typed UUIDv7
= full 128 bits
= nil invalid
= never reused
= restricted/internal by default
```

UUIDv7 ordering cannot be used as authority, chronology or operation order.

### 2.3 DUR-02

**PROVEN:** accepted Persistence-v1 establishes:

- correctness-sensitive transactions require named invariants and anomaly closure;
- application-only check-then-write is insufficient;
- retries preserve semantic operation identity;
- stricter DUR-03 rules may refine the common transaction policy;
- authoritative mutation + mandatory durable evidence + publication state commit atomically;
- lost response after commit is reconciled, not blindly replayed;
- ordinary restart may not lose acknowledged committed durable mutation;
- production restore stays fail-closed until reconciliation and non-rollback authority fencing pass;
- item/currency/value conservation belongs to DUR-03.

### 2.4 ANL-01

**PROVEN:** accepted ANL-01 establishes:

- OperationId identifies a retry-capable logical operation where one is needed;
- TransactionId identifies one logical atomic durable mutation transaction;
- an ambiguous commit/retry keeps the same TransactionId;
- a new TransactionId requires the prior logical transaction to be proven terminal and an intentionally new transaction to begin;
- mandatory DURABLE_AUDIT evidence commits with the owning mutation;
- TransactionEventRef defines the bounded complete event set/order of one transaction;
- replay is read-only toward gameplay.

### 2.5 FND-02

**PROVEN:** FND-02 defines:

```text
CommandRef = (GameSessionId, CommandId)
```

and reserves each CommandId once in authoritative ingress. Lower duplicate IDs never execute again. Same-GameSession reconnect preserves pending/reserved command identity while connection_generation advances.

### 2.6 FND-03/FND-04

**PROVEN:** accepted foundation authority separates:

- GameSession identity;
- TransportBinding / connection_generation;
- CharacterLease generation/current lease authority;
- runtime scope ownership generation.

NodeId, item binding or identity equality are not mutation authority.

### 2.7 ADR-0006

**PROVEN:** durable economy/security audit includes item creation/destruction, split/merge, location/ownership change, loot/pickup, trade/market/mail/depot/reward, currency changes and retry/transaction resolution. This supports durable transaction evidence even when high-volume combat/world telemetry remains best-effort.

### 2.8 Live programme state

**PROVEN:** `main@2521882253b04287e1243c54692440120e0b6c8e` records:

```text
GAME-ITEM-01  ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
DUR-03        PROPOSED / PLANNED / NOT_STARTED
```

No implementation/DDL/production authority exists.

## 3. Problem

Without DUR-03, individually reasonable subsystem implementations can still duplicate or lose value:

- one item can be simultaneously represented as inventory and ground;
- escrow can be a side flag while the item remains spendable in inventory;
- stale channel/lease authority can commit after a newer owner exists;
- timeout can trigger a new transaction identity and double mint;
- split can reuse one ItemInstanceId for two live stacks;
- merge can retire/revive the wrong identity;
- a type transform can silently change lifecycle meaning;
- a container operation can orphan descendants;
- a currency debit can commit without a matching transfer/source/sink;
- a restore can resurrect authority that replays already-applied operations;
- analytics may detect the damage later but must not become repair authority.

## 4. Constraints

### Integrity

- no live ItemInstanceId reuse;
- no more than one immediate authoritative location per live instance;
- no item/location/binding metadata as authorization;
- no client authority for quantity, location, identity, source/sink or balance;
- no stale GameSession/CharacterLease/runtime owner commit;
- no blind retry after ambiguous durable outcome;
- no committed authoritative mutation without mandatory durable evidence where ADR-0006/DUR-03 requires it;
- no cross-world gameplay value transfer by default;
- no implicit cross-database distributed transaction;
- no binary floating-point conservation arithmetic;
- no unbounded participant/custody/container/evidence graph.

### Product/parity

- first Reference target remains the accepted 2026-07-28 production-observable Global cut;
- observable unknown behavior remains `PARITY_PENDING_EVIDENCE`;
- security/integrity can intentionally differ from exploitable upstream defects;
- internal Oteryn identity UUID continuity is not an observable Global mechanic and therefore is not inferred from imaginary Reference identifiers.

### Ownership

DUR-03 must not absorb item legality, loot policy, market/order-book policy, trade consent, bank/depot/mail access, reward eligibility, crafting recipes, houses, entitlements, runtime/session mechanics, SQL layout or analytics enforcement.

## 5. Immediate-location model

### Option A — subsystem-specific owner/location columns

Typical shape:

```text
inventory_character_id
container_parent_id
ground_tile
market_offer_id
mail_id
...
```

**Reject.** Multiple fields can coexist, every subsystem creates another authority, partial updates create duplicates and generic `owner_id` semantics collapse custody/binding/authorization.

### Option B — one typed immediate-location relation

Recommended semantic model:

```text
ItemInstanceId -> exactly one ItemLocationRef
```

Location families include, conceptually:

- CharacterInventory(CharacterId, typed inventory position);
- CharacterEquipment(CharacterId, one complete GAME-ITEM occupancy claim);
- Container(parent ItemInstanceId, typed entry);
- Ground(WorldId + explicit ChannelRef/InstanceRef + typed spatial position);
- separately registered world-shared spatial/custody families when a later owner accepts them;
- separately registered trade/market/depot/mail/reward/house custody families.

`TypedDomainCustody` is a registry concept only: it does **not** mean one generic runtime variant with arbitrary strings/JSON. Each custody family must have its own stable type/schema/owner/scope.

Benefits:

- one presence truth;
- no inventory+escrow double-spend;
- container move changes only root location;
- future surfaces extend typed custody without new peer authorities.

## 6. Container semantic consequence

Contained items point to immediate parent only.

Moving a container:

- changes the container's own immediate location;
- does not rewrite every descendant relation;
- validates affected GAME-ITEM capacity/weight/nesting/type constraints;
- cannot commit if it creates cycle/orphan state;
- cannot destroy/replace a container while descendants are left without a valid bounded disposition.

This is semantic, not a SQL schema mandate.

## 7. Identity-transition model

### State mutation

Same concrete lifecycle preserves ItemInstanceId when legal typed state changes (charges, durability, binding, compatible modifiers/upgrades, quantity adjustment of an existing stack).

### New concrete lifecycle

Any new independently locatable concrete object/stack gets a fresh ItemInstanceId.

### Retirement

When the concrete lifecycle ceases to exist, its ID is terminal and never reused.

### Split

For source `S(q)` and `0 < x < q`:

```text
S keeps ID, becomes q-x
N gets fresh ID, becomes x
```

Moving all quantity is a move of S, not a split.

### Quantity transfer/merge

For amount x from compatible A to existing B:

- B keeps B's ID;
- A keeps A's ID if positive quantity remains;
- if A reaches zero, A retires;
- total units remain exact;
- no temporary ItemInstance is needed solely for fungible units.

### Type-changing transform

DUR-03 must choose lifecycle semantics explicitly per versioned transform rule:

- `PRESERVE_INSTANCE` only for one-input/one-output transform that the Oteryn semantic rule declares the same concrete lifecycle;
- `REPLACE_INSTANCE` retires input and gives fresh ID to concrete output;
- multi-output can never reuse one ID for two live outputs.

**Important clarification:** this internal UUID policy is not determined by Global's nonexistent ItemInstanceId. Reference evidence constrains observable transform input/output behavior. Oteryn's identity-preserve/replace classification is an internal integrity rule that must be explicit and versioned. If the observable transform itself is unknown, that transform remains parity-pending; the UUID policy is not “discovered” from Reference IDs.

## 8. Conservation model

Market-price equality is rejected as conservation because loot, crafting, decay and conversion can intentionally change item types/count and prices are not invariant.

Every mutation line is classified:

1. `TRANSFER` — existing value changes location/custody;
2. `SPLIT_MERGE_QUANTITY` — units redistribute exactly;
3. `STATE_MUTATION` — same concrete lifecycle changes legal state;
4. `MINT` — value enters under explicit source cause;
5. `BURN` — value leaves under explicit sink cause;
6. `TRANSFORM` — explicit versioned input/output rule;
7. `CONVERSION` — explicit exact asset-A -> asset-B rule.

No generic unclassified signed authoritative delta.

For non-item fungible assets:

- exact bounded arithmetic is mandatory;
- binary floating point is forbidden as conservation basis;
- pure same-asset transfer balances exact debits/credits;
- net creation/destruction requires typed mint/burn cause;
- conversion needs explicit versioned rule.

## 9. Provenance/source-sink model

Every mint/burn/transform/conversion must answer:

```text
what authoritative cause allowed this?
which exact inputs participated?
which outputs resulted?
which transaction committed it?
was the same logical cause already applied?
```

Potential causes are domain-owned occurrences such as kill/loot resolution, reward grant, craft, static placement materialization, system source/sink or later admin compensation.

DUR-03 does not accept those business causes. It requires stable cause identity/output lineage sufficient to deduplicate replay.

## 10. CommandRef, TransactionId and OperationId

### CommandRef

FND-02 remains player-command identity/order inside one GameSession.

### TransactionId

Every atomic durable item/value mutation receives one ANL TransactionId before the first durable commit attempt.

TransactionId identifies the **logical atomic transaction intent**, not a physical DB attempt.

### OperationId

Use OperationId when one logical workflow is retryable beyond one command/transaction/process/GameSession or spans multiple durable commits.

Simple state-precondition-safe commands need not mint OperationId merely for uniformity.

## 11. Retry semantics — known abort vs ambiguous outcome

This is a critical distinction.

### Known abort

If the DB attempt is proven non-committed (for example serialization/deadlock abort):

- same TransactionId and logical intent are retained;
- implementation may rematerialize authoritative before-state and a legal effect set under current state;
- no external side effect from the aborted attempt may have escaped;
- if the rematerialized current state makes the intent no longer legal, transaction terminates/rejects rather than adapting into a different business intent.

This avoids turning every serialization retry into a new semantic transaction while allowing correct re-read under concurrency.

### Ambiguous commit

Once a commit attempt outcome is ambiguous:

- its exact materialized candidate mutation/evidence set is frozen for reconciliation;
- no different effect set may be attempted under that TransactionId until the ambiguous attempt is classified;
- receipt/state is queried;
- committed => return/reconcile original result;
- proven aborted/non-committed => retry same logical TransactionId under known-abort rules;
- unclassifiable => fail/hold; never issue a new TransactionId as a guess.

This distinction prevents double mint without unnecessarily forbidding anomaly-safe retries.

## 12. Durable receipts

Value-sensitive operations need durable receipt/reconciliation state whenever FND-02 ingress + current state alone cannot prove retry safety.

Receipt semantics distinguish:

- not applied / safely retryable;
- committed / original result;
- terminal durable rejection where owning domain needs it;
- unresolved ambiguous outcome;
- conflicting reuse of operation/transaction/source identity.

Exact table/layout/retention duration is deferred. Retention must cover replay/idempotency horizon; once-only cause keys cannot be forgotten while replay remains possible.

## 13. Atomic participant set and isolation

A transaction has a bounded closed participant/effect set for each commit attempt, including as needed:

- ItemInstances and immediate locations;
- item capability/quantity state;
- equipment/container claims;
- non-item value accounts/asset lines;
- custody/workflow state;
- receipt/idempotency state;
- authority/fence rows/state;
- mandatory audit/publication state.

Requirements:

- absolute participant/traversal/evidence ceilings before implementation acceptance;
- no unbounded “move arbitrary graph”;
- deterministic lock/acquisition plan or another proven anomaly-closing mechanism;
- READ COMMITTED only with explicit DUR-02 invariant proof;
- otherwise SERIALIZABLE or stricter accepted mechanism;
- advisory locks cannot be sole durable authority;
- deadlock/serialization retry uses the same logical transaction identity.

Numeric ceilings are intentionally not invented here.

## 14. Authority/fencing

Character-controlled value mutation consumes current accepted FND authority:

- GameSession/CommandRef where player-originated;
- current CharacterLease authority/generation;
- current runtime scope ownership generation for channel/instance-scoped participants;
- domain state preconditions.

Binding/location/ItemInstanceId/NodeId are not credentials.

### Connection-generation nuance

A previously reserved command may survive eligible reconnect of the same GameSession while connection_generation advances. Therefore DUR-03 must not require the old transport generation itself to remain current at DB commit.

It instead requires that:

- the command was authoritatively reserved under valid binding;
- GameSession/CharacterLease/runtime authority has not become terminally invalid/superseded;
- commit-time fences required by touched participants are current.

## 15. Ground and multichannel safety

Core ground state is explicitly WorldId + ChannelRef/InstanceRef scoped.

A future world-shared spatial location (for example an accepted house topology) must be a separately typed location family with one named authority; DUR-03 does not silently model world-shared ground as channel-local.

A stale runtime scope owner cannot commit durable ground mutation after ownership generation changes.

Character-held inventory is not made channel-owned solely because the character currently plays on one channel.

Direct live channel-to-channel ground transfer is unsupported without an explicit one-winner custody/handoff owner.

## 16. One game-owned atomic DB boundary for v1

Current atomic DUR-03 mutation belongs inside one `oteryn_game` PostgreSQL transaction under accepted ADR-0004/DUR-02.

Reject as unaccepted:

- Platform/game distributed 2PC;
- cross-database foreign keys;
- mirrored dual item authority;
- implicit remote-service atomicity.

A future external persistence/service custody boundary requires its own safe handoff/custody contract.

## 17. Multi-transaction workflows

When a business workflow intentionally spans multiple transactions:

- stable OperationId is used where the workflow can resume/retry across boundaries;
- each committed transaction is independently conservation-safe;
- intermediate value moves into explicit typed custody;
- after custody commit the value is no longer usable in the previous location;
- workflow state is restartable/idempotent;
- compensation is a new transaction;
- no end-to-end atomicity is claimed across separate commits unless explicitly proven later.

Trade/market/mail/reward business state machines remain downstream.

## 18. Cross-world safety

- ItemInstance remains in one WorldId value scope by default;
- direct cross-world item/currency/value transfer is forbidden;
- burn in world A + mint in world B is still a cross-world transfer and cannot bypass policy;
- future world transfer requires explicit lineage, balance, custody, authority and recovery architecture.

## 19. Static placement and repeatable sources

StaticItemPlacement materialization needs a stable occurrence/cause identity sufficient to prevent crash/retry double mint.

A one-shot occurrence cannot produce a second output under duplicate retry.

Repeatable spawn/reward behavior needs distinct authorized occurrence identities; DUR-03 does not define respawn schedule/business rules.

## 20. Mandatory durable audit

ADR-0006 intentionally classifies item/currency ownership/location changes and source/sink activity as durable economy/security audit.

Therefore every authoritative DUR-03 mutation must produce ANL-compatible durable transaction evidence sufficient to reconcile its item/value effects.

The event set may aggregate multiple touched mutation lines into a **bounded** transaction event/payload; DUR-03 does not require one event per item/line. If evidence cannot fit configured hard ceilings, the operation must use a safe bounded/staged design or reject — never emit an unbounded event.

Minimum semantic evidence includes as applicable:

- TransactionId;
- OperationId/CommandRef/cause;
- World/runtime scope;
- ruleset/content/item-definition revisions needed for interpretation;
- touched ItemInstanceIds;
- before/after lifecycle disposition;
- before/after immediate location;
- type/revision transition;
- exact quantity/value lines;
- source/sink/transform/conversion classification/rule;
- conservation summary;
- safe authority/fence references without secrets.

Concrete ANL event IDs/protobuf payloads are not selected here. They must be registered before implementation claims conformance.

## 21. Restore/recovery

Before authoritative value mutation resumes after restore/integrity incident, verify at least:

- supported schema/migration revision;
- live ItemInstance uniqueness and non-reuse consistency with retained retirement evidence;
- one immediate location per live item;
- valid parent custody/container graph;
- legal quantities/capabilities/definition revisions;
- no TransactionId/OperationId/source-cause receipt conflict;
- complete mandatory retained audit event sets where required;
- non-item asset invariants;
- newer recovery fencing prevents pre-restore session/lease/runtime authority resurrection;
- audit replay cannot execute gameplay or remint outputs.

Failure keeps mutation closed. Analytics can diagnose but not auto-repair.

## 22. Compensation

After commit, historical fact is immutable.

Undo/correction is a new authorized compensating transaction with:

- new TransactionId;
- causation/reference to original transaction;
- current authority;
- complete source/sink/conservation evidence.

Raw row deletion/history rewrite is not compensation.

## 23. Downstream surface boundaries

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

## 24. Threat model

### Duplicate command

FND-02 CommandRef prevents second same-session execution; DUR-03 receipt/OperationId covers operation classes requiring crash/cross-session continuation.

### Lost-response double mint

Same TransactionId + ambiguous reconciliation; no guessed new transaction.

### Stale writer

Current CharacterLease/runtime generation fences at transaction boundary.

### Escrow double-spend

Custody is immediate authoritative location, not a side flag.

### Split/merge duplicate identity

Explicit survivor/new-ID/retirement rules.

### Cross-world laundering

No default transfer; burn+mint remains classified transfer.

### Restore remint

New recovery fence + receipt/cause reconciliation + read-only audit replay.

### Analytics repair authority

Prohibited; compensation is a new authoritative transaction.

## 25. Player/producer trade-offs

### Player

Benefits:

- progress safe under retries/lost responses/crashes;
- no half-equips or inventory+ground duplicates;
- reliable compensation/audit trail;
- fail-closed ambiguous operation rather than silent value corruption.

Cost:

- unsafe/oversized/parity-unknown operations may reject instead of “best effort” completing.

### Producer

Benefits:

- one location and conservation substrate for later systems;
- typed custody prevents every business subsystem from reinventing ownership;
- durable evidence supports item-dup investigation/Game Intelligence;
- immediate-parent containers avoid large subtree rewrites.

Costs:

- implementation must prove anomaly closure and bounded transaction design;
- durable audit volume must be engineered within explicit hard bounds;
- high-risk workflows require durable idempotency receipts.

## 26. Rejected alternatives

- subsystem-specific peer location fields — duplicate authority risk;
- generic JSON/EAV transaction/location payload — untyped authority escape hatch;
- market-price equality as conservation — semantically wrong;
- CommandId alone for all retries — too narrow for multi-step/cross-session operations;
- event sourcing as mutation authority — contradicts ANL-01;
- blind new TransactionId on timeout — double-effect risk;
- UUID ordering as survivor/authority — DUR-01 forbids semantic inference;
- implicit Platform/game distributed transaction — no accepted atomic protocol;
- analytics automatic repair — violates ADR-0006/ANL-01.

## 27. Decision timing

### Must decide now?

**YES.**

### Blocked downstream work

- durable inventory/equipment/container/ground implementation;
- item/currency anti-duplication implementation;
- durable loot/pickup persistence slice;
- future safe custody for trade/market/depot/mail/rewards/houses;
- Game Intelligence item/value reconciliation;
- item/value crash/recovery/concurrency E2E.

### Hard future migration cost

Changing after durable item history exists affects location authority, identity lineage, receipts, source/sink provenance, transaction evidence interpretation, custody and restore proof.

### Supersession evidence

Valid reopening evidence includes:

- proven externally observable target mechanic incompatible with this typed extension model;
- PostgreSQL anomaly/correctness evidence;
- measured scale showing the bounded atomic/custody architecture cannot meet safety/performance;
- accepted cross-service/database custody protocol with equivalent one-authority proof;
- exploit/security evidence;
- privacy/legal retention change;
- explicit owner world-transfer/economy policy.

OTS schemas, framework preference and convenience are insufficient.

### Deliberately not decided

- SQL tables/indexes/lock syntax/isolation implementation;
- Rust libraries/APIs;
- numeric participant/resource ceilings without evidence;
- concrete ANL event IDs/protobuf payloads;
- exact unevidenced Reference transform/crafting/loot/reward/decay/business rules;
- trade/market/bank/depot/mail/house state machines;
- cross-world transfer feature;
- external service/database custody protocol;
- production topology/RPO/RTO/backup cadence;
- automatic remediation.

## 28. Recommendation

Adopt a DUR-03 candidate contract whose irreducible proof is:

```text
one live item -> one immediate location
new lifecycle -> fresh ItemInstanceId
retired lifecycle -> ID never reused

one atomic durable mutation -> one TransactionId
known abort -> retry/rematerialize same logical intent under same ID
ambiguous commit -> freeze/reconcile exact candidate before any new attempt

pure movement -> no unauthorized source/sink
mint/burn/transform/conversion -> typed rule/cause + complete lineage

all authoritative mutation + required durable evidence -> commit together
or none

multi-step -> typed custody + OperationId where needed
restore -> fail closed until identity/location/receipt/audit/authority invariants reconcile
```

This is sufficient to unblock a later separately authorized durable item/value implementation without prematurely selecting physical schema or downstream business policy.
