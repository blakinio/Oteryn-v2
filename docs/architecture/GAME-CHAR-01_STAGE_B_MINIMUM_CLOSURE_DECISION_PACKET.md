# GAME-CHAR-01 — Stage B Minimum Closure Decision Packet

- Status: **PRE-DECISION SYNTHESIS / NOT ACCEPTED**
- Date: 2026-08-11
- Gate: `GAME-CHAR-01` Stage B
- Reference target: **Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary**
- Trusted repository base: `blakinio/Oteryn-v2@4dce1e4da5c7c9e442abe99975aac3e7913b46b4`
- Evidence inputs: Stage A owner baseline + #183 general Stage-B reconciliation + #185 B1-B3 acquisition + #187 B4-B8 delta
- Decision owner: product owner
- Runtime authority: **NONE**
- Does not authorize: runtime/client/protocol/physical persistence/content/Platform implementation, production rollout, unproven Reference formulas/values, first Reference PvP world-type selection or any intentional Reference difference not separately accepted

## 1. Executive result

### Is the evidence sufficient to claim complete Reference character parity?

**NO.**

Several target-visible values/formulas remain `UNKNOWN` or only current-state evidence:

- exact naming normalization/repertoire/recycling;
- 60-day deletion / total-30 / deleted-name-hold target continuity;
- exact starter template and some creation-flow details;
- exact XP/skill arithmetic;
- promotion fee and Premium-lapse target edges;
- full PvP/Twist/fair-fight/skull/Death Redemption edge matrix;
- offline-training effectiveness arithmetic;
- some modern-definition migration details.

None of these may be guessed or presented as `PARITY_CONFIRMED`.

### Is the evidence sufficient to close the **durable semantic Character architecture**?

**RECOMMENDATION: YES — if the owner accepts the closure boundary in this packet.**

The evidence now supports a stable answer to the architecture questions that determine:

- who owns character state;
- which state is character-specific versus another authority;
- which semantic lifecycle/progression/build facts durability must be able to represent;
- how naming, creation, promotion, death, offline training and modern progression are versioned;
- which unknowns are policy/ruleset/content/SIM values rather than database topology;
- how to keep those unknowns fail-closed without blocking formula-neutral durable architecture.

This is a scope refinement, **not a reduction of the Reference parity standard**.

## 2. Decision-discipline test

### Must durable semantic ownership be decided now?

**YES.**

Final character-bearing `DUR-02` architecture is blocked until GAME-CHAR tells it what durable Character semantics must exist and which authorities remain outside Character.

### Must every exact Reference value/formula be decided now?

**RECOMMENDATION: NO — not when the value/formula does not determine identity, authority, transaction atomicity, irreversible representation or migration topology.**

Such values remain mandatory before the corresponding Reference behavior is implemented, enabled, tested as parity or included in an external Reference evaluation.

### What becomes expensive if we keep treating all unknown numbers as schema blockers?

- persistence starts encoding gameplay formulas merely to unblock itself;
- current Global or OTS values may leak into the July-28 target by convenience;
- unrelated SIM/content/PvP evidence becomes a prerequisite for basic ownership/revision design;
- future rule correction can require schema churn instead of a versioned policy/fixture update;
- Stage B never closes despite having enough evidence to define durable semantic boundaries.

### What becomes dangerous if we defer too much?

- a generic schema may omit state that later cannot be added/migrated safely;
- name uniqueness may be implemented with an irreversible wrong comparison model;
- character-specific progression may be accidentally stored under item/account/content authority;
- world/profile-sensitive death state may be hard-coded as universal;
- parity gaps may be silently treated as implementation defaults.

The recommended package therefore freezes **semantic envelopes and ownership**, while keeping unproven target values hard-gated.

## 3. Closure model

The recommended boundary is:

```text
GAME-CHAR Stage B
owns / freezes
-> Character semantic catalogue
-> Character-specific ownership scope
-> version/revision/migration envelopes
-> policy boundaries and fail-closed unknown handling
-> which decisions DUR-02 may represent generically

Reference ruleset / SIM / content / world-profile gates
own / freeze later where applicable
-> exact arithmetic
-> exact numeric policy values not yet evidenced
-> exact starter content
-> exact PvP/world-type edge matrix
-> target-specific deterministic fixtures

DUR-02
owns later
-> physical schema/constraints/indexes/transactions/migrations
-> only after consuming accepted semantic architecture
```

Architecture acceptance therefore remains distinct from `PARITY_CONFIRMED` implementation evidence.

## 4. Recommended Stage-B decision 1 — naming semantic envelope

### Evidence basis

#185 establishes strong continuity evidence for a Tibia-wide/global name namespace, long-lived technical naming restrictions and separate rename-history semantics. Exact July-28 canonicalization/recycling remains incomplete.

### RECOMMENDATION

Freeze:

1. Reference character names occupy one **logical global Character Authority namespace**, not independent per-world namespaces.
2. Character has a player-visible display name and an authoritative **canonical comparison key** produced by a versioned naming policy.
3. The canonical comparison key is a semantic value used for uniqueness/conflict decisions; its exact normalization algorithm is not hard-coded into GAME-CHAR while target evidence is incomplete.
4. Current name, searchable former-name alias/history and deleted-name reservation are distinct semantics.
5. A naming-policy revision change requires explicit validation/migration/conflict handling and may not silently reinterpret existing names.
6. CharacterId remains identity through rename; names are not identities.

### Remains parity-pending

- exact Unicode/case/space normalization;
- exact repertoire / 29-letter continuity;
- reserved/restricted-pattern revision;
- deleted-name release algorithm and duration.

### DUR-02 consequence

DUR-02 may design a formula/implementation-neutral authoritative name registry/key representation, but may not choose collation/normalization semantics by database convenience.

## 5. Recommended Stage-B decision 2 — lifecycle policy values are versioned policy, not lifecycle topology

Stage A already accepts:

```text
ACTIVE -> DELETION_SCHEDULED -> RETIRED
```

#185 strongly supports active-character quota `25`, while exact July-28 continuity for deletion grace `60 days`, total `30`, undelete interaction and deleted-name hold remains incomplete.

### RECOMMENDATION

Freeze:

1. the Stage-A semantic lifecycle unchanged;
2. account/world eligibility and quota checks as Character Authority policy evaluated atomically with lifecycle operations;
3. **25 active characters** as the recommended Reference target active-character quota based on strong primary continuity evidence;
4. deletion grace, scheduled-deletion total quota, undelete conditions and name-hold/recycling timings as versioned Reference lifecycle/name-policy values;
5. unknown target values remain `PARITY_PENDING_EVIDENCE` and must not be filled from current Global by assumption.

Unknown policy values do not require new lifecycle states or database topology.

## 6. Recommended Stage-B decision 3 — creation uses a versioned policy/template boundary

### Evidence basis

#185 establishes Newhaven as the production entry point before target, strong tutorial/Newhaven/vocation-selection continuity and Targuna as the post-Newhaven continuation before July 28. Exact starter stats/items/home state remain unresolved.

### RECOMMENDATION

Freeze:

1. Character creation remains the atomic/idempotent Character Authority operation accepted in Stage A.
2. Creation records explicit profile/ruleset/content/starter-template revision context sufficient to reproduce/migrate the initial semantic state.
3. Exact starter inventory/equipment, early route/quest data and tutorial content are **content/ruleset template semantics**, not hard-coded Character-constructor defaults.
4. Character build state must support the target's pre-vocation/selection lifecycle; a universal schema invariant that every newly created character already has a final vocation is forbidden.
5. World/route/quest ownership remains content/world authority even when those facts are presented on a character page.
6. Exact target starter template remains a Reference content/parity fixture gate before the corresponding flow is claimed complete.

This allows DUR-02 to represent initialization context without inventing the unknown starter package.

## 7. Recommended Stage-B decision 4 — progression catalogue versus arithmetic

### Evidence basis

Target-era evidence establishes persistent character progression vocabulary including level, experience, HP, mana, capacity, speed and the skill family. Historical capacity migration proves not every visible stat can safely be assumed to be a pure current formula projection.

### RECOMMENDATION

Freeze:

1. Character domain owns authoritative persistent progression facts needed by the active ruleset.
2. Reference progression includes the evidenced character-level/experience/skill vocabulary and supports migration-sensitive attributes such as capacity without assuming they are always pure functions.
3. Persisted facts and deterministic derived projections remain explicitly distinguished under Stage A.
4. Every progression fact/projection is interpreted under explicit ruleset/profile revision context.
5. Exact XP→level, skill-advancement, HP/mana/capacity/speed and rounding formulas are **ruleset/SIM parity gates**, unless evidence proves a particular formula changes identity/ownership/atomicity/irreversible representation.
6. DUR-02 may choose a formula-neutral representation of authoritative facts but may not encode an unproven formula as a schema invariant.

### Hard implementation gate

No unresolved arithmetic may be implemented as Reference behavior or marked `PARITY_CONFIRMED` without target evidence + deterministic fixtures.

## 8. Recommended Stage-B decision 5 — promotion achievement versus entitlement-derived activation

### Evidence basis

#187 gives very strong primary continuity for promotion at level >=20 with Premium eligibility. Exact July-28 fee and Premium-lapse edge behavior remain incomplete.

### RECOMMENDATION

Freeze:

1. promotion/profession progression is Character-owned versioned build state;
2. achieved promotion history/state is not erased merely because an account entitlement changes;
3. current active benefits/eligibility may be derived from Character promotion state + active ruleset + Platform-owned entitlement input;
4. exact fee and exact lapse/reactivation target semantics remain versioned policy/parity gates;
5. Platform remains entitlement authority and never becomes steady-state Character mutation authority.

No monetization or Premium implementation is authorized.

## 9. Recommended Stage-B decision 6 — death/protection is profile-scoped, not one universal Character formula

### Evidence basis

#187 establishes strong base death/blessing continuity and proves material PvP/world-profile differences. The accepted GAME-VISION PvP baseline explicitly leaves exact world types and whether the first Reference proof is PvP-enabled unresolved.

### RECOMMENDATION

Freeze:

1. Character owns durable character-specific death/protection consequences and protection/progression facts required by an active profile, while item-loss/corpse/value conservation remains GAME-ITEM/DUR-03/combat owned.
2. Death/protection evaluation is under explicit Reference ruleset/world-profile policy revision.
3. Regular blessing/protection state exposed as character-specific state remains representable without hard-coding one universal formula.
4. PvP-only persistent facts are introduced only when their owning world/profile policy requires them and with explicit ownership/fencing.
5. The complete Twist/fair-fight/skull/Death Redemption edge matrix does **not** block generic Character durable architecture before exact PvP world/profile policy is selected.
6. Exact PvP/death formulas remain hard parity/implementation gates for any world/profile that exercises them.

### Important boundary

This does not choose a first Reference PvP world type. That remains a separate product/world-policy decision coordinated with `GAME-CHANNEL-01` and related PvP/recovery gates.

## 10. Recommended Stage-B decision 7 — offline-training semantic counter versus effectiveness

### Evidence basis

#187 establishes strong primary continuity for the per-character offline-training counter/timer state machine:

- >=10 minutes offline before gain;
- maximum 12 hours effective continuous training;
- 1 pool second consumed per training second;
- 1 pool second restored per second online or offline without training;
- reactivation required to consume refilled pool after depletion.

### RECOMMENDATION

Freeze:

1. offline training is a ruleset capability, not universal engine behavior;
2. when enabled by the Reference target, its activation/counter/pool state is character-specific durable progression state;
3. the strongly evidenced timer/pool semantics above are accepted as the Reference semantic counter model;
4. exact effectiveness coefficients, advancement arithmetic, rounding, modifier interaction and selectable-skill details remain ruleset/SIM parity gates where evidence is incomplete.

DUR-02 may represent the semantic counter/capability without encoding effectiveness formulas.

## 11. Recommended Stage-B decision 8 — modern character-specific progression scope

### Evidence basis

#187 materially strengthens character-specific ownership evidence:

- Weapon Proficiency Progress is explicitly character-bound and non-transferable;
- Character Bazaar transfer contract classifies charms/charm points/charm expansion, Hunting Task Points and permanent Hunting Task/Prey slots as character-specific;
- Wheel/Promotion Points have strong character-build ownership evidence;
- Animus Mastery has strong character-specific progression alignment.

### RECOMMENDATION

Freeze:

1. Character **domain ownership scope** includes character-specific progression/capability facts required by the active target, including the evidenced systems above.
2. Character-specific does not imply one giant Character aggregate, table or transaction boundary.
3. DUR-02 may use dedicated character-owned child aggregates where size, independent lifecycle, contention or migration evidence justifies them.
4. ruleset/content definitions own trees, thresholds, perk/mastery definitions, formulas and compatibility rules;
5. GAME-ITEM/DUR-03 owns item-instance/resource conservation and value transfers;
6. Platform owns commercial entitlement source;
7. character-specific progression refers to stable versioned definition identities and requires explicit migration when definitions become incompatible.

This closes ownership scope without prematurely fixing physical decomposition.

## 12. Recommended Stage-B decision 9 — unresolved Reference values become explicit parity gates

### RECOMMENDATION

Introduce the following architecture rule for this gate:

```text
UNKNOWN / CONFLICT target rule
-> may have a safe versioned semantic/policy envelope
-> may NOT be filled by current Global, OTS code or implementation convenience
-> may NOT be enabled as claimed Reference behavior
-> may NOT be PARITY_CONFIRMED
-> must be evidenced, explicitly declared different, or kept out of the exercised release scope
```

This applies to remaining naming, lifecycle-value, starter-content, arithmetic, promotion-edge, PvP-edge, offline-effectiveness and definition-migration gaps.

### External Reference evaluation rule

Any character behavior exercised by an external Reference milestone must be either:

- `PARITY_CONFIRMED`; or
- an explicit owner-accepted `DECLARED_DIFFERENCE`.

A known `UNKNOWN`/`CONFLICT` cannot silently pass as Reference fidelity.

## 13. Recommended Stage-B decision 10 — refine the gate boundary, not the parity standard

Current horizon wording can be read as requiring every exact formula before durable Character architecture may close.

Evidence now shows this conflates two different proof obligations.

### RECOMMENDATION

Refine `GAME-CHAR-01` so its architecture acceptance requires:

- complete semantic ownership boundaries;
- lifecycle/build/progression semantic catalogue sufficient for durability;
- revision/version/migration/fencing rules;
- safe policy envelopes for target-specific values;
- explicit hard gates for every unresolved Reference value/formula.

It does **not** require exact numeric arithmetic that belongs to a later ruleset/SIM/content/world-profile contract **unless that arithmetic constrains durable identity, ownership, atomicity, irreversible representation or migration**.

The Reference parity standard itself remains unchanged and fail-closed.

## 14. What remains deliberately unresolved after recommended closure

The following may remain unresolved without silently becoming defaults:

### Naming / lifecycle policy

- exact canonicalization/repertoire/29-letter target continuity;
- deleted-name release algorithm;
- deletion grace `60 days`, total `30` and related July-28 continuity.

### Creation/content

- exact starter inventory/equipment/stats/home/route content;
- remaining target-specific creation validation details.

### Progression/arithmetic

- exact XP/level and skill curves;
- exact derived-stat arithmetic/rounding where still unproven.

### Promotion/entitlement

- exact 20,000 gp target continuity;
- exact Premium-lapse benefit semantics.

### Death/PvP

- first Reference PvP world type;
- complete Twist/fair-fight/skull/PvP edge matrix;
- exact target Death Redemption history/window semantics;
- exact death arithmetic beyond evidenced/accepted portions.

### Offline training

- effectiveness coefficients and detailed advancement arithmetic.

### Modern progression

- exact formulas/definitions;
- physical child-aggregate/table placement;
- migration details for future incompatible definition revisions.

These remain hard-gated at their owning implementation/parity boundary.

## 15. Effect if owner accepts this package

### GAME-CHAR status

Recommended effect after delivery lifecycle closes:

```text
GAME-CHAR-01
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
Runtime authority    = NONE
```

Stage A remains binding and Stage B becomes the accepted semantic Reference/durability closure layered on top of it.

### DUR-02

`DUR-02` may proceed from bounded discovery to final **paper-only character schema architecture** using the accepted GAME-CHAR semantics.

It still may not:

- implement PostgreSQL schema/migrations without separate implementation authority;
- hard-code unproven Reference formulas/values;
- choose name normalization by database convenience;
- collapse child progression systems into one aggregate without evidence;
- encode one universal PvP/death profile;
- treat current Global as July-28 truth.

### Runtime / content

No runtime, content, client, protocol, Platform or production implementation is authorized by GAME-CHAR acceptance itself.

### Reference implementation

Each unresolved target rule remains blocked until the owning evidence/ruleset/SIM/content/world-profile gate resolves it.

## 16. Alternative: keep GAME-CHAR open until every exact value is known

This is possible but **NOT RECOMMENDED**.

It would preserve a single monolithic gate at the cost of:

- blocking durable ownership/schema architecture on historical values that may require different evidence channels;
- pressuring persistence to infer or embed gameplay policy;
- delaying GAME-ITEM/DUR and vertical-slice architecture for reasons unrelated to durable topology;
- encouraging accidental current-Global/OTS substitution.

A strict parity gate still exists under the recommended split — it simply lives at the feature/ruleset/fixture boundary where exact behavior actually matters.

## 17. Owner decision package

### RECOMMENDATION — NOT OWNER-ACCEPTED

Accept sections 4–13 as the minimum GAME-CHAR Stage-B semantic closure and accept the effect in section 15.

In compact form:

1. global logical character-name namespace + versioned canonical comparison policy; exact normalization/recycling remains parity-pending;
2. Stage-A lifecycle retained; active quota `25` accepted as strong Reference candidate; other unresolved lifecycle values become versioned parity-pending policy;
3. creation uses versioned ruleset/content/starter context; exact starter content is not schema policy and pre-vocation state must be representable;
4. progression ownership/catalogue closes independently from exact formulas when storage remains formula-neutral/versioned;
5. promotion achievement is Character-owned; active benefits may depend on Platform-owned entitlement/ruleset; unresolved fee/lapse edges stay parity-pending;
6. death/protection is profile-scoped; generic Character architecture does not require a complete PvP edge matrix before world-profile selection;
7. offline-training counter/capability state is Character-owned with evidenced 10-min/12-h/1:1 counter semantics; effectiveness stays ruleset/SIM-pending;
8. modern character-specific progression belongs to Character domain scope but may use child aggregates; definitions/content/item/economy/Platform authorities remain separate;
9. every remaining `UNKNOWN/CONFLICT` is an explicit hard parity gate, never an implementation default;
10. refine GAME-CHAR architecture scope to semantic ownership/versioning/migration; exact arithmetic remains mandatory before Reference implementation/parity claim when it does not constrain durable topology.

If accepted, overall `GAME-CHAR-01` may become `ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED` after the owner-baseline delivery lifecycle, and final paper-only `DUR-02` character schema architecture may proceed.

## 18. What acceptance does not mean

Acceptance would **not** mean:

- all July-28 character behavior is known;
- all listed current values are accepted as July-28 values;
- Reference character runtime may be implemented without additional gates;
- unknown formulas may be guessed;
- PostgreSQL DDL/migrations are authorized;
- first Reference PvP world type is selected;
- GAME-CHANNEL, GAME-ITEM, SIM or content gates are accepted;
- Premium/VIP implementation is authorized;
- any external repository may be modified.

Until the owner explicitly accepts or modifies section 17, this document remains **PRE-DECISION SYNTHESIS / NOT ACCEPTED** and `GAME-CHAR-01` remains `PROPOSED / PLANNED / NOT_STARTED`.
