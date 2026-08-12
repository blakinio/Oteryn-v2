# GAME-CHANNEL-01 — Channel Product Policy Analysis

- Date: 2026-08-12
- Gate: `GAME-CHANNEL-01`
- Delivery task: `OTV2-20260812-game-channel-01-architecture`
- Delivery PR: #209
- Status: **analysis for a paper-only candidate; nonbinding until accepted delivery + lifecycle closeout**
- ImplementationStatus: **NOT_STARTED**
- Runtime/client authority: **NONE**
- PostgreSQL DDL/migration authority: **NONE**
- Production authority: **NONE**

## 1. Problem

Oteryn already has a strong technical multichannel foundation:

```text
one logical WorldId
-> one economy / community / ruleset family
-> multiple ChannelId values
-> one independent public-world simulation per channel
-> one logical mutation owner per ChannelRuntime
```

That is not yet a complete **product policy**.

Without GAME-CHANNEL-01, a technically correct implementation could still make materially wrong player/product decisions by accident:

- always auto-assigning players and breaking parties/friends apart;
- exposing channels but allowing unlimited hopping for fresh spawns/loot/PvP escape;
- multiplying boss/reward eligibility because every channel has a simulation copy;
- treating a full-channel queue as a GameSession or gameplay reservation;
- silently moving a player to a different channel when the current channel fails;
- changing spawn/loot rates inversely with active channel count as hidden economy tuning;
- making Channel display number a durable identity;
- letting runtime autoscaling decide product/economy policy merely from CPU/player count;
- exposing exact friend/player channel placement without the owning presence/privacy policy;
- making instances/houses a hidden channel-switch path.

GAME-CHANNEL-01 therefore has to freeze the **player/economy/social/PvP semantics around an already accepted runtime model**, while not taking over runtime orchestration, capacity engineering, persistence, economy business rules or Reference gameplay formulas.

## 2. Source facts and precedence

### 2.1 ADR-0001 — accepted multichannel foundation

`PROVEN`:

- one logical World is one product/economy/community boundary;
- one Channel is an independent public-world simulation;
- `WorldId`, `ChannelId`, `InstanceId`, `NodeId` and `GameSessionId` are different meanings;
- all channels in one World use the same ruleset/map/content family/revisions required by accepted compatibility policy;
- world-shared Character/social/economy domains remain shared across channels;
- positions, creatures/spawns, combat, ground items/corpses/local loot, local NPC runtime and local speech are channel-local;
- channel change is already defined as a safe session transition, not teleport/rebind;
- a completed channel transition creates fresh destination admission/session authority;
- combat lock, direct trade, unresolved item mutation, protected encounter and instance transition already block channel switching;
- channel hopping may not evade consequences or repeat account/character rewards.

GAME-CHANNEL must consume these rules, not redesign them.

### 2.2 FND-ID-01 — Channel identity

`PROVEN`:

```text
ChannelId  = strongly typed UUIDv7
ChannelRef = WorldId + ChannelId
```

Platform World Registry/topology authority owns and issues canonical ChannelId. Restart, recovery or GameNode relocation of one semantic channel preserves ChannelId. A display ordinal/name is not identity. A retired ChannelId is never reused for another semantic channel.

Consequence: a UI label such as `Channel 2` is presentation. Queue, admission, switching, audit and policy must resolve canonical ChannelRef rather than trust label equality.

### 2.3 ADR-0009 / FND-03 — runtime lifecycle and capacity

`PROVEN`:

- GameNode and ChannelRuntime topology/runtime lifecycle is already owned outside GAME-CHANNEL;
- a ChannelRuntime has one current logical writer;
- GameNodes may host multiple channels;
- channel activation/closure can be dynamic;
- exact capacity values and trigger thresholds require PERF evidence;
- operational lifecycle includes Open/Full/Degraded/Draining/Recovering/Fenced/etc.;
- no active-channel live migration in the first implementation;
- a failed ChannelId is recovered as the **same ChannelId**;
- players are not silently moved to another live channel after failure.

GAME-CHANNEL may map these states to product-facing eligibility, but must not redefine the runtime state machine or choose orchestrator technology.

### 2.4 FND-04 — admission authority

`PROVEN`:

- Platform/Gateway/World Registry may advertise and authorize one bounded attempt;
- game-domain authority makes final admission decision;
- a fresh admission grant binds one specific `WorldId + ChannelId` and current revision/ownership evidence;
- no silent retarget to another Channel is allowed;
- a canonical GameSessionId is game-domain issued only after successful admission;
- queue/recommendation therefore cannot itself be GameSession/CharacterLease/gameplay authority.

### 2.5 GAME-VISION-01 — product/economy/fairness

`PROVEN`:

- ordinary progression is solo viable while coordinated party play is materially rewarded;
- PvP is a supported secondary pillar;
- conservation precedes balance tuning;
- Reference uses mechanical source/sink parity, not historical market-price parity;
- hidden macro economy tuning is rejected;
- group rewards cannot rely on duplicated eligibility;
- player-facing channel friction is a later measurable product-health dimension.

### 2.6 DUR-03 — durable value safety

`PROVEN`:

- one durable ItemInstance has one semantic location;
- stale runtime/session authority cannot commit value mutation;
- retry/ambiguous commit cannot duplicate item/currency effects;
- reward/source occurrences require stable idempotency where relevant;
- direct cross-world value transfer is forbidden by default;
- Game Intelligence may investigate but never mutate/repair authority.

GAME-CHANNEL owns **whether channel multiplicity is product-allowed for a source/eligibility shape**. DUR-03 owns the conservation and anti-duplication mechanics once value is created/moved.

### 2.7 Reference evidence boundary

`DERIVED`:

Multichannel public-world selection itself is an Oteryn product/platform layer rather than an externally observable Oteryn ItemInstance/PvP/Global Tibia mechanic that can be copied from the accepted Reference target.

Therefore:

- intra-channel Reference gameplay remains subject to the accepted 2026-07-28 Reference target;
- GAME-CHANNEL must explicitly define Oteryn channel policy instead of filling it from current Global/OTS convention;
- exact Reference PvP/loot/boss formulas remain their owning parity questions and are not invented by this gate.

## 3. Decision timing

### Must decide now?

**YES.**

The owner-accepted 2026-08-10 programme refinement explicitly requires GAME-CHANNEL-01 before multichannel becomes a product feature.

### Concrete downstream work blocked

Without this gate, the project cannot safely claim:

- player-visible channel selection/assignment;
- a channel queue UX;
- party/friend co-location behavior;
- a safe voluntary channel-switch product flow;
- anti-hopping policy that survives session changes;
- economically intentional dynamic channel multiplicity;
- multichannel boss/event/reward semantics;
- PvP-safe channel selection/switching;
- player-visible channel drain/recovery behavior;
- product correctness for `VSL-MULTICHANNEL-01`.

### What becomes expensive if wrong later?

Late correction could require migration/rework of:

- channel directory and selection semantics;
- Gateway/World Registry offers and queue integration;
- durable character-world switch-guard state;
- reward eligibility/idempotency keys;
- event scope definitions;
- presence/privacy and client UX;
- economy telemetry interpretation;
- channel activation policy;
- support/incident handling;
- multichannel E2E fixtures.

### Evidence that may supersede decisions

Reopening a GAME-CHANNEL clause should require named evidence such as:

- playtests showing channel choice/queue/co-location creates unacceptable friction;
- economy telemetry showing channel multiplicity causes unacceptable source/sink distortion;
- PvP abuse evidence showing current anti-hopping policy is insufficient;
- recovery evidence showing same-channel-first product behavior cannot meet accepted availability;
- capacity/OPS evidence requiring a different public-channel exposure model;
- privacy/security evidence around channel-presence disclosure;
- explicit product-owner strategy change.

Implementation convenience or one OTS convention is insufficient.

## 4. Fundamental product model

Recommended canonical model:

```text
WorldId
= durable product/economy/community/ruleset identity

ChannelId within WorldId
= durable identity of one parallel public-world simulation

current channel placement
= one GameSession/lease/runtime placement fact
!= Character identity
!= economy namespace
!= social namespace
!= progression namespace
```

Consequences:

- Character progression/items/bank/depot/market/guild identity are not copied per channel;
- ordinary local positions/monsters/combat/ground state are not shared merely because WorldId is shared;
- a player may change channels only through accepted session/admission transition;
- `InstanceId` is not a hidden `ChannelId` and cannot be used to bypass channel policy;
- house/instance transitions never silently change the character's channel.

## 5. Channel identity versus presentation

Canonical references use `ChannelRef = WorldId + ChannelId`.

A public directory may show a human label such as:

```text
Channel 1
Channel 2
Quiet
Busy
```

but:

- label/ordinal is never admission, queue, audit, reward or durable identity;
- client sends/retains an opaque canonical reference from a current authorized directory/offer, not authority derived from text;
- changing presentation label does not change ChannelId;
- a stopped/recovered same semantic channel keeps ChannelId;
- a retired ChannelId is never assigned to a different semantic channel;
- whether a presentation ordinal may later be reused for a new semantic ChannelId is a UI/directory policy, provided no durable logic depends on the ordinal.

## 6. Player entry model — options

### Option A — automatic assignment only

Benefits:

- simplest load balancing;
- lower risk of empty-channel fragmentation.

Costs:

- harms party/friend co-location;
- makes channel identity player-invisible while still affecting local state;
- creates confusing reconnect/meeting behavior.

Rejected as the sole model.

### Option B — explicit player choice only

Benefits:

- maximum player agency;
- easy party coordination.

Costs:

- hot-channel imbalance;
- unnecessary queues even when other channels are healthy;
- higher operational churn and social self-segregation.

Rejected as the sole model.

### Option C — recommendation + explicit override

The directory/Gateway presents an authoritative eligible set plus a **recommended** target. A player may accept recommendation or select another currently eligible visible Channel.

Recommendation may consider policy-owned signals such as:

- capacity/health category;
- previous-channel affinity;
- party co-location hint;
- friend co-location hint when permitted by presence/privacy policy;
- demand balancing;
- maintenance/drain state.

The exact scoring algorithm is implementation/product-tuning work. Recommendation is never final admission authority.

**Recommended: Option C.**

This balances agency, co-location and capacity without making the client or recommendation service authoritative.

## 7. Automatic recommendation contract

A recommendation is one bounded, revisioned control-plane hint.

Rules:

- it references one currently directory-eligible ChannelRef;
- it cannot bypass final FND-04 validation;
- it cannot override player explicit target choice silently;
- stale/full/draining/incompatible target requires a refreshed offer/recommendation;
- no client-provided load/presence claim is trusted as authoritative input;
- hidden/internal/recovering/fenced channels are not ordinary automatic targets;
- recommendation policy may change without changing Character identity or gameplay ruleset.

Player-visible UX should distinguish **recommended** from **required**.

## 8. Explicit target selection

When a player explicitly selects ChannelRef C:

```text
current directory/offer says C is selectable
-> bounded pre-admission material is issued for C
-> FND-04 final validation decides admission to C
```

If C becomes full, draining, stale, incompatible or otherwise ineligible:

```text
no silent fallback under the same grant
-> return safe target-status result
-> player/automatic policy obtains a fresh offer for another target
```

This preserves FND-04's exact Channel binding and prevents stale authorization from being retargeted opportunistically.

## 9. Queue semantics — options

### Option A — no queue

Simple but poor UX for groups/popular channels.

### Option B — world-global queue only

Good for a single destination abstraction but conflicts with explicit channel choice and does not solve target-specific co-location.

### Option C — bounded target-channel pre-admission queue, optional by world policy

A player selecting a full target may choose to wait for that Channel or choose another eligible Channel.

**Recommended: Option C**, with these constraints:

- queue state is pre-admission/control-plane state;
- queue state is not a GameSession, CharacterLease, runtime ownership claim, item/value reservation or guaranteed admission;
- queue priority is server/control-plane owned; client cannot submit authoritative priority;
- final admission still revalidates capacity/health/revisions/lease/account/character facts;
- FND-04's short-lived grant is issued/refreshed only when admission is actually ready, not treated as a long-lived queue credential;
- exact queue service placement, storage, algorithm, max length, timeout, priority classes and rate limits remain separate Platform/OPS/product implementation work;
- any queue token/reference is purpose-limited control-plane state, never gameplay bearer authority.

For automatic entry, policy should prefer another healthy eligible Channel over needless queuing when the player did not explicitly request a target. If all eligible targets are capacity-limited, the product may expose a queue/choice according to world policy.

## 10. Party and friend co-location

Goal: reduce social fragmentation without creating new authority.

Recommended first-generation policy:

- party/friend channel facts are **co-location hints**, not authority;
- party members may explicitly choose the Channel of an eligible member when presence/privacy policy permits disclosure;
- automatic recommendation should prefer co-location when it does not violate eligibility/capacity policy;
- every Character still performs independent FND-04 admission and owns an independent GameSession/lease;
- no all-or-nothing multi-character admission transaction is introduced;
- no party-owned Channel authority is introduced;
- no party member is teleported/migrated automatically merely because another member changed channel;
- if target is full, members may wait/select another target under ordinary queue policy;
- shared-experience/combat/proximity benefits requiring co-location remain available only when members actually share the same authoritative simulation, as already classified by the scope matrix.

Atomic party-capacity reservation may be revisited later only if product evidence shows best-effort co-location is insufficient and a bounded multi-admission contract can preserve FND authority safely.

## 11. Presence and privacy

GAME-CHANNEL needs enough channel placement information for co-location UX, but does not own the full presence/privacy contract.

Binding boundary:

- current ChannelId/label may be exposed only through the owning presence/privacy policy;
- hidden/offline/private presence cannot be bypassed through channel directory/co-location endpoints;
- party relationships may have a stronger co-location disclosure policy than arbitrary public players if the social/privacy owner accepts it;
- raw operational placement such as NodeId, ownership generation, queue internals or security revisions is not player-facing channel presence.

Exact visibility matrix remains social/privacy-owned.

## 12. Channel switch is not reconnect

Accepted foundation distinction:

```text
same-session transport reconnect
!= channel switch
```

Channel switch follows ADR-0001:

```text
safe gameplay exit/checkpoint
-> current GameSession closes/terminates appropriately
-> current lease is released/advanced as required
-> choose/recommend destination Channel
-> obtain fresh authorized pre-admission material for destination
-> destination FND-04 admission
-> fresh canonical GameSessionId
-> enter destination ChannelRuntime
```

GAME-CHANNEL may add product policy around this flow, but may not turn it into an in-place teleport or preserve old GameSessionId across the completed channel transition.

## 13. Hard channel-switch blockers

Existing accepted blockers remain hard:

- combat lock / protected PvP state;
- direct player trade;
- unresolved item/value transaction;
- protected boss/raid/encounter state where hopping changes eligibility;
- active instance that lacks a safe exit;
- active house mutation/topology transition where applicable;
- pending Character checkpoint/authority transition;
- stale/unavailable lease/authority evidence;
- incompatible destination revisions;
- target full/draining/unhealthy/unavailable.

GAME-CHANNEL adds no client-side override for these blockers.

## 14. Anti-hopping policy — options

### Option A — hard blockers only

Insufficient: a player can repeatedly hop immediately after every safe boundary to search for fresh local spawns/resources or avoid normal local competition.

### Option B — session-local timer

Rejected: relog/reconnect/new GameSession would reset the guard and make it trivial to bypass.

### Option C — durable Character+World switch guard

A versioned world policy maintains anti-hopping state outside one transport/GameSession lifetime.

Recommended semantic shape:

```text
CharacterId + WorldId
-> current channel-switch guard state
-> interpreted under explicit world_policy_revision
```

The physical schema is deferred.

**Recommended: Option C.**

## 15. Switch cooldown semantics

For public voluntary channel switching:

- a time-based cooldown/eligibility guard is mandatory as the first anti-hopping mechanism in addition to hard blockers;
- exact numeric duration is deliberately **not** invented here and must be accepted from product/playtest/economy/PvP evidence before implementation activation;
- the guard survives logout, relog, GameSession replacement, reconnect and GameNode restart;
- reconnect to the same ChannelId is not a switch and does not consume/reset the cooldown;
- a failed destination admission does not count as a successful switch;
- successful completed destination admission/entry is the semantic point that records the switch and starts/advances the guard;
- switching to a different Channel at a later fresh login is still subject to the same guard if it remains active;
- client time is not authoritative for eligibility;
- policy changes require version-aware interpretation/migration rather than silently reinterpreting existing active guards.

This gate freezes the **existence and semantics** of a cooldown guard, not its number.

## 16. Trusted forced-transition exceptions

Maintenance, incident recovery or administrator-directed safe evacuation may require a player to leave a Channel through no voluntary hopping intent.

A later runtime/ops/admin contract may define a typed trusted exception that can avoid or compensate the voluntary-switch cooldown only when:

- source cause is server/operator authoritative;
- action is audited;
- Character/value state reaches a safe boundary;
- it cannot be requested or forged by the client;
- it cannot reset PvP/combat/reward eligibility or DUR-03 safety;
- destination still uses fresh admission if the actor changes ChannelId.

There is no generic `ignore_channel_cooldown=true` client/admin convenience flag.

## 17. The economic multiplicity problem

Foundation architecture makes ordinary public-world simulation independent per Channel. Therefore:

```text
more active Channels
-> potentially more monsters/spawns/local loot/resource opportunities
-> one shared World economy
```

This effect must be intentional and measurable. It cannot be hidden inside OPS autoscaling.

Rejected strategies:

### Hidden inverse rate scaling

Automatically divide spawn/loot rates by active channel count.

Rejected because it silently changes ruleset behavior and makes Reference mechanics/load-dependent.

### One giant world-shared pool for all ordinary spawns

Would reduce supply multiplication but couples independent simulations and creates substantial world-shared coordination/latency complexity.

Rejected as the default for ordinary public-world content.

### Explicit multiplicity/eligibility classification

Keep ordinary local simulation independent but require every value-significant encounter/source/reward family to declare how channel multiplicity interacts with simulation and durable eligibility.

**Recommended.**

## 18. Source and eligibility classification

GAME-CHANNEL defines architecture vocabulary, not content tables or formulas.

### `CHANNEL_LOCAL_REPEATABLE`

- independent simulation/source exists per Channel;
- ordinary repeatable output may occur independently under the same ruleset mechanics;
- aggregate World supply can grow with active Channel count and player demand;
- this is an explicit product consequence, not a duplication defect;
- no hidden inverse rate adjustment is allowed unless a later explicit ruleset/product decision supersedes it.

Foundation ordinary creatures/spawns/local loot fit this default unless an owning content/encounter contract classifies them differently.

### `CHANNEL_LOCAL_SHARED_ELIGIBILITY`

- local simulation/encounter may exist independently on multiple Channels;
- durable claim/reward eligibility is shared at a declared World+Character/Account/other owner scope;
- hopping/copy count cannot reset the eligibility key.

Useful for replicated encounters or reward surfaces where access may scale but durable reward frequency must not.

### `WORLD_SCOPED_UNIQUE`

- one world-level semantic occurrence/eligibility exists regardless of number of Channels;
- execution/presentation placement is explicitly owned by the event/boss/world-service contract;
- Channel copies cannot independently mint another world-unique occurrence.

### `EXPLICIT_EVENT_POLICY_REQUIRED`

- no safe default is inferred;
- boss/raid/high-impact event owner must declare both simulation scope and eligibility scope before activation.

New high-impact content may not fall through to an accidental per-channel default merely because its runtime object lives in ChannelRuntime.

## 19. Simulation scope and eligibility scope are different

Every reward-bearing encounter/event that matters across Channels declares at least:

```text
simulation_scope
eligibility_scope
reset/repeat policy
stable reward/source occurrence identity shape
```

Examples:

```text
simulation_scope = CHANNEL_LOCAL
eligibility_scope = CHARACTER_WORLD_DAILY
```

or:

```text
simulation_scope = WORLD_UNIQUE
eligibility_scope = WORLD_EVENT + per-character participation rules
```

The exact reward eligibility business rules remain the reward/event owner. GAME-CHANNEL requires the dimensions not to be conflated.

DUR-03 then supplies transaction/idempotency/conservation mechanics for any resulting item/currency value.

## 20. Dynamic channel opening is not invisible economy tuning

GAME-CHANNEL owns a product invariant:

> Operational capacity control may open/close public Channels only inside an accepted World channel-multiplicity policy; capacity pressure does not grant authority to invent economy rules.

Consequences:

- product/world policy defines whether dynamic public channel multiplicity is enabled and its allowed semantic envelope;
- exact minimum/maximum channel counts and occupancy/load thresholds remain product/PERF evidence and are not guessed here;
- OPS-CHANNEL-01 owns orchestrator, hysteresis, health/capacity signals, process placement and activation mechanics;
- PERF-01 owns supported capacity numbers;
- GAME-CHANNEL requires economy/social/channel-friction effects to be observable before production scaling claims;
- no single player/client command directly opens/closes a public Channel;
- channel activation is not a reset API for high-value/world-limited content.

## 21. Fresh-channel reset abuse

A newly activated/recovered public Channel may reconstruct channel-local state according to its owning runtime/content policy. That must not turn lifecycle operations into a farmable reset primitive.

Rules:

- ordinary `CHANNEL_LOCAL_REPEATABLE` simulation may become available according to its normal channel-runtime initialization semantics;
- one-time/world-limited/high-impact encounters/rewards require shared or explicit event policy rather than relying on channel process uptime;
- repeated stop/start/recover of the same ChannelId cannot reset durable Character/Account/World eligibility;
- a fresh semantic ChannelId cannot inherit or erase reward eligibility merely because its display ordinal looks new/old;
- OPS lifecycle decisions are not player-authorized reward reset events.

Exact spawn initialization timers remain content/runtime-owned.

## 22. PvP implications

GAME-CHANNEL does not define exact Reference PvP formulas/world types. It freezes cross-channel consequences:

- PvP combat execution remains channel-local;
- Character/world PvP consequences owned by the active profile (combat lock, skull/frag/war consequence where applicable) are not reset by channel transition or new GameSession;
- active combat/protected PvP state blocks voluntary switching;
- channel hopping cannot erase target/reward/consequence state that the PvP owner declares world/Character-scoped;
- destination admission revalidates current world/profile policy;
- a different Channel is not a safe fallback during an unresolved failed combat runtime;
- client cannot claim disconnect/failure to obtain a cooldown/PvP exception.

Exact lock duration, skull/frag formulas, fair-fight/Twist/Death Redemption behavior and first Reference PvP type remain their existing parity/profile gates.

## 23. Social/community safeguards

A World remains one community even when its public simulation is split.

Binding safeguards:

- guild identity/membership is not per Channel;
- market/bank/depot/rankings are not duplicated per Channel merely for simulation locality;
- world/guild/private communication remains cross-channel where already accepted;
- local speech remains channel/spatial;
- party membership may remain world-shared while proximity/shared-experience effects require actual co-location;
- channel recommendation should reduce involuntary party/friend fragmentation where privacy/capacity permit;
- client should always make current World and current Channel understandable to the player;
- product analytics should measure queue wait, switch rejection, co-location success and population fragmentation before channel-policy tuning.

GAME-CHANNEL does not select chat/social service topology.

## 24. Player-visible lifecycle classes

Runtime has more internal states than players need.

GAME-CHANNEL recommends the following semantic presentation classes, with exact UI wording deferred:

### `SELECTABLE`

Current directory/revisions/health/capacity permit a fresh admission attempt subject to FND-04 final validation.

### `CAPACITY_LIMITED`

Channel is not admitting immediately because product/OPS capacity is full/limited. A target queue may be offered if policy supports it.

### `DRAINING`

No new ordinary admissions. Existing players proceed toward a safe lifecycle boundary under OPS/FND policy. No silent alternate-channel migration.

### `RECOVERING`

Same ChannelId is being recovered. Affected players follow same-channel reconnect/recovery behavior rather than normal new-channel selection.

### `UNAVAILABLE`

Not selectable/routable. A later fresh offer may expose it again when it becomes valid.

Internal `Suspected`, `Fenced`, ownership-generation, NodeId and similar operational states are mapped safely and need not be exposed verbatim.

## 25. Drain product behavior

When a public Channel enters drain:

- it leaves ordinary selectable/recommended targets;
- no new ordinary admissions enter;
- current sessions receive bounded product-visible maintenance/drain state when client UX exists;
- players progress to a safe exit/checkpoint/session boundary under accepted FND/DUR/OPS rules;
- hard operational deadline may terminate sessions only through the owning safe shutdown/recovery contract;
- no actor is silently inserted into another Channel;
- after safe source termination, a player may explicitly choose/recommend a destination through fresh admission;
- trusted maintenance cause may later qualify for the typed cooldown-exception policy, never a client-selected bypass.

## 26. Failure and recovery product behavior

Default rule remains accepted ADR-0009:

```text
Channel failure
-> reconnect/recover same ChannelId
-> no invisible fallback to another Channel
```

GAME-CHANNEL makes the player-facing consequence explicit:

- client may show `RECOVERING` for the same Channel;
- old/stale Channel simulation cannot resume authority after fencing;
- recovery preserves ChannelId while NodeId/ownership generation may change;
- if recovery cannot continue within the owning accepted operational policy, the actor must first reach a proven safe offline/terminal authority state;
- only then may the player receive a fresh channel directory and intentionally select/recommend a different Channel under normal channel-switch/fresh-admission rules;
- system-caused failure does not itself erase combat/reward/value consequences;
- there is never `failed Channel A -> silently continue in live Channel B`.

## 27. Channel creation/removal product boundary

GAME-CHANNEL does not own process orchestration.

It owns only the player/product constraints on public channel multiplicity:

- public channels are explicitly registered semantic ChannelIds issued by topology authority;
- channels may be temporarily inactive and later recover/reactivate with the same ChannelId under accepted topology/runtime rules;
- retired ChannelId is never reused;
- public selection only sees policy-eligible channels;
- opening/closing must respect allowed world multiplicity and economy/social guardrails;
- closure requires accepted drain/safe-state semantics;
- no client directly creates/deletes a Channel;
- display labels/ordinals are presentation and cannot become lifecycle identity.

OPS-CHANNEL-01 owns actual dynamic creation/removal orchestration, triggers, hysteresis and placement. PERF-01 owns supported capacity thresholds.

## 28. World-policy revision ownership

GAME-CHANNEL does **not** introduce a new mandatory protocol revision dimension merely for channel policy.

Channel product policy is part of the already accepted versioned `world_policy_revision` boundary consumed by FND-04 admission.

Consequences:

- a stale grant cannot silently enter under superseded channel policy;
- switch-guard/eligibility semantics retain enough policy-version context for deterministic interpretation/migration;
- changing a channel rule does not require a new protocol major unless wire/core-protocol semantics independently change;
- exact policy storage/registry remains downstream implementation/content/control-plane work.

## 29. Channel switch policy evolution

Because cooldown/eligibility may outlive one GameSession, a world-policy change cannot reinterpret active state ambiguously.

A later implementation must define one explicit transition strategy per incompatible policy change, such as:

- preserve existing eligible-at deadline under prior policy;
- deterministically migrate to a new deadline under an accepted rule;
- apply only to switches committed after new policy activation.

Silent retroactive extension/shortening without a versioned rule is rejected.

## 30. Error/disposition semantics

Concrete protocol numeric error IDs remain FND/domain registry work. GAME-CHANNEL requires stable semantic distinctions at minimum:

- target not eligible/unavailable;
- target capacity-limited/full;
- target draining;
- target recovering;
- target revision/policy stale/incompatible;
- channel-switch hard lock active;
- channel-switch cooldown/guard active;
- queue unsupported/expired/cancelled;
- current offer stale;
- channel placement undisclosed by privacy/presence policy.

Errors do not reveal hidden presence, NodeId, generation, private queue internals or security evidence.

## 31. Security and abuse review

Required invariants:

- client cannot forge Channel eligibility/capacity/priority;
- client cannot turn queue state into admission authority;
- explicit target never silently retargets under same grant;
- relog/reconnect/new GameSession cannot reset anti-hopping guard;
- client-declared disconnect/maintenance cannot unlock trusted exception;
- Channel label/ordinal is never canonical identity;
- no second Character session exists on another Channel;
- no stale Channel owner writes durable Character/value state;
- no active trade/item transaction/encounter/instance bypass through switch;
- no per-channel duplication of world-shared reward eligibility;
- no hidden inverse spawn/loot tuning based only on active channel count;
- no automatic failed-channel relocation into a different combat/spawn/loot simulation;
- presence/co-location lookup cannot bypass privacy policy;
- instances/houses cannot become channel-switch portals;
- channel lifecycle operations cannot reset durable reward/source eligibility.

## 32. Resource limits before implementation

Architecture deliberately does not guess numeric limits. Implementation cannot claim GAME-CHANNEL conformance until bounded values exist for applicable externally influenced structures such as:

- maximum public channels exposed in one directory response;
- queue entries/bytes and per-account/Character queue requests;
- directory refresh/result size;
- co-location hint count;
- switch-attempt/rate-control state;
- channel-policy serialized size/version complexity;
- event/reward eligibility correlation inputs where channel multiplicity expands work;
- control-plane pending offers/queue references.

Limits require machine-readable registration or an explicitly accepted equivalent, boundary tests and safe failure behavior.

## 33. Observability and Game Intelligence

Product/channel policy should become measurable without becoming authority.

Useful dimensions include:

- active public Channel count over time;
- players per Channel and World;
- recommendation acceptance versus explicit override;
- queue wait/cancellation/alternate-choice rates;
- party/friend co-location success;
- voluntary switches, cooldown rejections and hard-lock rejections;
- switch causes including trusted maintenance/recovery categories;
- source/sink composition normalized by active Channel count/channel-hours/player population;
- reward duplicate/conflict detections;
- population fragmentation and social activity distribution;
- same-channel recovery success and cases that required later explicit new-channel admission.

High-cardinality player/session/item IDs remain outside ordinary metrics labels. Analytics informs human policy decisions and cannot automatically open channels, change rates, waive locks or repair value.

## 34. Player perspective

The preferred behavior should feel predictable:

- player knows which World and Channel they are on;
- new login normally receives a sensible recommended Channel but can choose another eligible one;
- party/friend co-location is easy when capacity/privacy permit;
- choosing a full Channel may offer a queue instead of silently moving the player;
- changing Channel is a deliberate safe session transition and cannot be spammed for farming/PvP escape;
- maintenance/recovery state is understandable;
- a server failure reconnects to the same simulation rather than dropping the player into a different monster/loot/combat state;
- World chat/economy/community remains coherent across Channels.

## 35. Producer/operator perspective

The model preserves operational flexibility:

- ChannelRuntime/GameNode placement remains OPS/PERF-owned;
- capacity scaling may add public simulations without changing Character/economy namespace;
- ordinary local capacity can scale while high-impact rewards use explicit shared/unique eligibility;
- no need for one distributed global lock around every ordinary monster spawn;
- economy effects are observable rather than hidden in autoscaling;
- same server binary can host one or many channels;
- recovery and drain do not require silent gameplay migration.

## 36. Options summary and recommendation

| Subject | Rejected/Deferred alternatives | Recommended architecture |
|---|---|---|
| entry | auto-only; manual-only | recommendation + explicit eligible override |
| target failure | silent alternate using same grant | fail closed + fresh directory/offer/grant |
| queue | GameSession-like reservation; unbounded queue | optional bounded pre-admission target queue |
| party admission | hidden teleport; all-or-nothing multi-character authority | best-effort co-location hints + independent admission |
| switch guard | blockers only; session-local timer | durable Character+World cooldown/guard + hard blockers |
| cooldown number | guessed constant | evidence-owned numeric value before activation |
| source scaling | hidden inverse rate scaling; one giant shared spawn pool | explicit channel multiplicity + eligibility classes |
| boss/event | per-channel by accidental runtime placement | explicit simulation scope + eligibility scope |
| failure | silent alternate-channel failover | same-ChannelId recovery; later explicit fresh switch only from safe state |
| channel creation | client/runtime convenience | topology-issued identity + OPS orchestration inside product multiplicity policy |
| policy revision | new protocol fork/dimension | existing world_policy_revision |

## 37. Deliberately not decided

GAME-CHANNEL-01 should not freeze:

- exact numeric voluntary switch cooldown;
- exact queue length/timeout/priority/rate limits;
- exact min/max public Channel count;
- exact player/channel or GameNode capacity thresholds;
- autoscaling algorithm/hysteresis;
- orchestrator/service topology;
- exact client UI labels/layout;
- exact party/friend presence visibility matrix;
- exact PvP/skull/frag/combat-lock formulas;
- exact boss/event/reward definitions;
- exact spawn/loot rates/probabilities;
- market/trade/bank/depot/mail business rules;
- concrete PostgreSQL/Platform queue/policy schema;
- protocol numeric message/error IDs;
- production rollout or admin exception workflow implementation.

## 38. Acceptance consequence

If the companion contract is accepted and lifecycle-closed:

```text
GAME-CHANNEL-01
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
runtime authority    = NONE
DDL/migration        = NONE
production authority = NONE
```

That acceptance would make channel product semantics ready for later implementation/VSL planning. It would not make multichannel runtime, Gateway queue, Channel UI, autoscaling, PvP profile, rewards or production behavior implemented/proven.
