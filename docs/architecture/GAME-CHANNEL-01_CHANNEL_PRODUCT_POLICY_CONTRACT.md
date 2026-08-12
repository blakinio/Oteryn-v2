# GAME-CHANNEL-01 — Channel Product Policy Contract

- Date: 2026-08-12
- Gate: `GAME-CHANNEL-01`
- Delivery task: `OTV2-20260812-game-channel-01-architecture`
- Delivery PR: #209
- Status on delivery branch: **CANDIDATE / NONBINDING**
- Canonical semantic effect: only after accepted delivery merge; programme `ACCEPTED / LIFECYCLE_CLOSED` promotion requires a separate lifecycle closeout
- ImplementationStatus: **NOT_STARTED**
- Runtime/client authority: **NONE**
- PostgreSQL DDL/migration authority: **NONE**
- Production authority: **NONE**
- Analysis source: `GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_ANALYSIS.md`

## 1. Purpose

Freeze the minimum Oteryn product policy required before the already accepted multichannel technical model may become a player-visible product feature.

This contract owns:

- public Channel identity/presentation semantics at product boundaries;
- automatic recommendation versus explicit player target selection;
- bounded target-channel queue meaning;
- party/friend co-location policy boundary;
- voluntary channel-switch and anti-hopping semantics;
- channel multiplicity versus ordinary source/high-impact reward eligibility policy;
- world-global event/reward scope requirements;
- cross-channel PvP consequence rules;
- world-community/social fragmentation safeguards;
- player-facing drain/recovery semantics;
- product-policy boundary with runtime capacity/orchestration and later domain gates.

It does **not** own GameNode/ChannelRuntime implementation, process/container orchestration, FND admission/session/lease mechanics, DUR value conservation, exact gameplay/PvP/reward formulas, PostgreSQL schema, Platform implementation or production rollout.

## 2. Authority chain

```text
World/Channel identity and multichannel baseline      -> FND-ID-01 + ADR-0001
GameNode/ChannelRuntime lifecycle/capacity baseline   -> ADR-0009 + FND-03
fresh admission / GameSession / CharacterLease        -> FND-04
minimum product/economy/party/PvP direction           -> GAME-VISION-01
Character lifecycle/progression/profile facts         -> GAME-CHAR-01
item semantic legality                                -> GAME-ITEM-01
item/currency/value conservation and anti-duplication -> DUR-03
channel player/economy/social/PvP product policy      -> GAME-CHANNEL-01
runtime capacity numbers                              -> PERF-01
process/channel orchestration                         -> OPS-CHANNEL-01
exact PvP/combat/reward/event/economy business rules  -> owning gameplay/product gates
```

No lower layer may redefine a higher semantic owner for convenience.

Where older coordination prose conflicts with later accepted FND-04/DUR-03 semantics, the accepted component contracts and current-status overlay govern.

## 3. Canonical channel model

A Channel is one parallel public-world simulation inside one logical World.

```text
WorldId
= one product/economy/community/ruleset boundary

ChannelRef = WorldId + ChannelId
= one durable semantic public-world simulation identity

current Character channel placement
= current admitted GameSession/lease/runtime placement
!= Character identity
!= economy namespace
!= progression namespace
!= social namespace
```

Rules:

- every public Channel belongs to exactly one WorldId;
- all channels in one World consume the compatible world/ruleset/content/map policy required by accepted contracts;
- different ruleset/profile families remain different WorldId values rather than special Channels;
- InstanceId is not ChannelId and an Instance is not a hidden Channel;
- house/instance entry/exit never silently changes ChannelId;
- Character/world-shared durable state is not duplicated per Channel unless its owning contract explicitly says otherwise.

## 4. Channel identity and display identity

Canonical identity is `ChannelRef = WorldId + ChannelId` exactly as FND-ID-01 defines it.

Human-facing labels/ordinals are presentation only.

Binding rules:

- ChannelId is strongly typed and never inferred from a label such as `Channel 2`;
- restart/recovery/relocation of the same semantic Channel preserves ChannelId;
- a retired ChannelId is never reused for another semantic Channel;
- display name/ordinal may change without changing ChannelId;
- whether a retired display ordinal is later reused is a presentation/directory decision and must never change durable identity, audit, queue or reward semantics;
- client-visible directory state may use an opaque canonical channel reference but presentation strings never become mutation/admission authority;
- NodeId, ownership generation and infrastructure placement are not player-facing Channel identity.

## 5. Public channel directory semantics

A channel directory/offer is a control-plane view of currently policy-eligible public Channels.

For each exposed target it must provide enough bounded semantic information for intentional selection, including as applicable:

- canonical ChannelRef or a safe opaque reference resolving exactly to it;
- human display label;
- product-facing availability class;
- whether target queueing is supported when capacity-limited;
- compatibility/offer evidence required by the existing Gateway/FND contract;
- optional co-location/recommendation context under the owning privacy/social policy.

The directory does not expose or grant:

- NodeId as gameplay identity;
- ownership-generation authority;
- private lease/session state;
- internal health/security details;
- hidden presence;
- gameplay admission merely because a target appears in the list.

All lists/responses are bounded before implementation acceptance.

## 6. Entry modes

GAME-CHANNEL accepts a hybrid player-entry model:

### `RECOMMENDED`

The control plane identifies one currently eligible recommended Channel from the current directory/offer.

### `EXPLICIT`

The player selects another currently eligible visible Channel.

The player may accept recommendation or exercise explicit choice when product policy allows it.

There is no third client-authoritative mode that bypasses current directory/offer eligibility.

## 7. Recommendation semantics

Recommendation is a non-authoritative bounded control-plane hint.

Recommendation may consider accepted policy inputs such as:

- current capacity/availability category;
- current health/drain eligibility;
- previous Channel affinity;
- party co-location hint;
- friend co-location hint when presence/privacy permits;
- demand balancing;
- maintenance state.

Rules:

- exact scoring/weights remain implementation/product-tuning choices;
- client-provided load/presence facts are not authoritative recommendation inputs;
- recommendation never bypasses FND-04 final validation;
- recommendation does not reserve capacity unless a separately accepted queue/reservation mechanism explicitly does so;
- recommendation cannot silently override a player explicit target;
- recommendation cannot select an internal/fenced/recovering target for ordinary fresh admission;
- stale recommendation requires a fresh offer rather than guessed continuation.

## 8. Explicit target semantics

When a player explicitly selects ChannelRef C:

```text
current authoritative directory/offer permits C
-> bounded pre-admission authorization targets C
-> FND-04 final admission validates C
```

If C becomes full, draining, unavailable, stale or revision-incompatible before admission:

- no admission occurs to C;
- the same authorization cannot be silently retargeted to another Channel;
- the player/control plane obtains a fresh offer for a different target;
- no CharacterLease/GameSession/value authority is created merely from the failed target choice.

This rule applies whether the original selection came from manual choice, party co-location or automatic recommendation.

## 9. Queue contract

A World may support a **bounded target-Channel pre-admission queue**.

Queue semantics are:

```text
queue intent
!= GameSession
!= CharacterLease
!= runtime ownership
!= item/value reservation
!= guaranteed admission
```

Binding rules:

- queueing is optional by World/product policy;
- queue target resolves one exact ChannelRef;
- queue priority/order is authoritative control-plane policy, never client-declared authority;
- queue entries/references are bounded, purpose-specific and expire/cancel under an explicit policy;
- final admission performs current FND-04 validation again;
- a short-lived FND-04 admission grant is not treated as a long-lived queue credential;
- admission material is issued/refreshed only when the queued attempt is actually ready to proceed under current target facts;
- leaving/cancelling/expiring a queue creates no gameplay mutation;
- exact queue storage, service placement, algorithm, timeout, maximum size, priority classes and rate limits remain separate implementation/cross-repository work;
- any future queue priority class requires explicit product/fairness reasoning and cannot be client-forged.

When a player used `RECOMMENDED` entry and another healthy eligible Channel is available, the default product policy should recommend an available target rather than force a needless target queue. An explicit target choice may prefer waiting.

## 10. Queue and current gameplay authority

ADR-0001 channel-switch order remains binding: a voluntary channel change reaches a safe source session boundary before destination selection/admission.

Therefore GAME-CHANNEL does not create a first-generation feature where an actively authoritative Character reserves/queues a destination Channel while continuing mutation in the source Channel.

A future live-session destination reservation would require a dedicated contract proving:

- capacity fairness;
- current lease/session authority interaction;
- switch blockers at offer/commit time;
- no dual placement;
- expiry/cancellation;
- failure/recovery;
- abuse resistance.

It is deliberately deferred.

## 11. Party/friend co-location

Co-location is a product preference, not authority.

Binding first-generation rules:

- an eligible party/friend Channel may be presented as a recommendation or explicit target when the owning presence/privacy policy permits disclosure;
- recommendation should prefer party co-location when target capacity/eligibility permits;
- every Character independently passes FND-04 admission and owns an independent GameSession/lease;
- no all-or-nothing multi-Character admission transaction is introduced;
- no PartyId owns or reserves a Channel by itself;
- no party member is silently teleported/migrated when another member switches;
- a full party target follows the same queue/alternate-choice policy as other explicit targets;
- proximity/shared-experience/combat mechanics requiring co-location activate only when the characters actually share the same current authoritative Channel/Instance as their owning gameplay contracts require.

Atomic party-capacity reservation is deferred until product evidence justifies the additional admission/lease complexity.

## 12. Presence/privacy boundary

GAME-CHANNEL does not define the full social/privacy visibility matrix.

It requires:

- Channel placement disclosure only through the accepted presence/privacy owner;
- hidden/private/offline status cannot be bypassed through channel selection/co-location lookup;
- arbitrary users are not entitled to exact Character Channel placement merely because the directory exposes public Channels;
- party/friend relationship may enable bounded placement hints only under accepted social/privacy policy;
- operational NodeId/generation/queue/security detail is never a social presence field.

## 13. Reconnect versus channel switch

These are different operations.

### Same-channel eligible reconnect/recovery

- consumes FND-04 reconnect/recovery semantics;
- may preserve the same GameSessionId when FND-04 permits;
- advances connection_generation as required;
- targets the same semantic ChannelId;
- does not count as a voluntary Channel switch.

### Completed Channel switch

- follows the ADR-0001 safe source-exit sequence;
- closes/terminates source GameSession as the owning contract requires;
- obtains fresh destination pre-admission authorization;
- performs fresh destination FND-04 admission;
- creates a fresh canonical GameSessionId;
- establishes destination ChannelRuntime placement.

A Channel switch is never an in-place transport rebind or teleport.

## 14. Hard channel-switch locks

A voluntary switch must fail closed while any accepted blocker applies, including at minimum:

- combat lock or protected PvP state;
- direct player trade;
- unresolved item/currency/value transaction;
- protected boss/raid/event participation where hopping changes eligibility;
- active instance without a safe accepted exit;
- house mutation/topology transition where applicable;
- pending Character checkpoint/authority/handoff transition;
- stale/unavailable GameSession/lease/required authority evidence;
- incompatible destination ruleset/content/map/world-policy/protocol/transport/offer revisions;
- destination Full/Draining/Recovering/Unavailable state.

A client cannot override these locks.

## 15. Voluntary anti-hopping guard

Hard locks alone are insufficient for repeated safe-boundary farming/competition manipulation.

GAME-CHANNEL therefore requires one durable Character+World anti-hopping guard for voluntary Channel changes.

Conceptually:

```text
(ChannelSwitchGuard)
scope = CharacterId + WorldId
interpretation = versioned world_policy_revision
lifetime = may outlive GameSession/connection/GameNode
```

This is a semantic requirement, not a physical persistence schema.

## 16. Voluntary switch cooldown

The initial anti-hopping mechanism is a **time-based switch cooldown** plus hard locks.

Binding semantics:

- public voluntary switching is subject to a non-session-local cooldown/eligibility guard;
- exact numeric duration is deliberately deferred to owner/product/playtest/economy/PvP evidence before implementation activation;
- the guard survives logout, relog, fresh GameSession, transport reconnect and GameNode restart;
- first admission to a World/Character with no active prior switch guard is not itself a switch;
- reconnect/recovery to the same ChannelId is not a switch and does not consume/reset the guard;
- failed destination selection/queue/admission does not record a successful switch;
- the successful completed destination admission/entry boundary records the voluntary Channel change and starts/advances the guard;
- a later fresh login to a different Channel remains subject to an unexpired guard;
- client wall time is not authoritative;
- policy revision changes cannot silently reinterpret active guard state.

An implementation claiming multichannel switching is not conforming until a concrete accepted duration and trusted durable time interpretation exist.

## 17. Channel-switch policy evolution

Switch guard state that survives GameSession must carry enough semantic revision context to remain deterministic across policy change.

For every incompatible world-policy update affecting the guard, rollout must explicitly select a transition rule such as:

- preserve existing deadline under prior policy;
- deterministic version-aware migration to a new deadline;
- new policy applies only to switches committed after activation.

Silent retroactive extension/shortening is prohibited.

The exact persistence fields/storage remain downstream.

## 18. Trusted non-voluntary exceptions

Maintenance, incident handling or a trusted operator-directed safe evacuation may require a Channel change that is not voluntary hopping.

A later OPS/admin implementation may define a typed trusted exception only when all are true:

- cause is server/operator authoritative and audited;
- source actor reaches a proven safe authority/value boundary;
- client cannot request/forge the exception;
- PvP/combat/reward eligibility is not reset or weakened;
- DUR-03 conservation/receipt state remains valid;
- changing ChannelId still requires fresh destination admission;
- exception semantics are versioned and bounded.

There is no generic client/admin boolean bypass.

## 19. Channel-local versus world-shared value

Accepted foundation remains:

### Channel-local simulation examples

- positions/visibility;
- creatures/spawns/AI;
- combat/transient effects;
- ground items/corpses/local loot runtime;
- local NPC runtime;
- local speech;
- public-map mutable overlay.

### World/Character-shared durable examples

- Character progression/items once committed to Character state;
- guild membership/world chat/private messaging under their owners;
- market/bank/depot/world economy;
- rankings;
- reward eligibility where defined at Character/Account/World scope;
- provisional one-state-per-world houses.

Channel locality never changes WorldId value scope.

## 20. Channel multiplicity policy

Additional active Channels can increase ordinary local simulation opportunities inside one shared World economy.

GAME-CHANNEL accepts this as an explicit product dimension rather than an implementation accident.

Binding rules:

- operational autoscaling cannot invent or modify game source/sink formulas silently;
- active Channel count may change under accepted topology/OPS policy without changing the underlying per-Channel ruleset mechanics;
- ordinary repeatable local sources may repeat per Channel only under the classification below;
- high-impact/limited/event/reward sources require explicit multiplicity/eligibility policy;
- economy impact is measured and reviewed rather than hidden through undocumented inverse tuning.

## 21. Multiplicity classification

Every value-significant source/encounter/reward family that can behave differently with more Channels is classified explicitly.

### `CHANNEL_LOCAL_REPEATABLE`

Meaning:

- one independent local source/simulation exists per Channel;
- repeatable output may occur independently in each Channel under the same in-Channel ruleset mechanics;
- aggregate World supply may therefore scale with active Channel count/player demand;
- no hidden automatic division of rates by active Channel count;
- DUR-03 still prevents technical duplicate transaction effects.

Ordinary public-world creature/spawn/local-loot simulation uses this baseline unless a more specific owning content/event contract classifies it differently.

### `CHANNEL_LOCAL_SHARED_ELIGIBILITY`

Meaning:

- encounter/simulation can exist on more than one Channel;
- durable reward eligibility is shared at an explicitly owned Character/Account/World/etc. scope;
- changing Channel or encountering another copy cannot reset the eligibility key;
- reward transaction remains idempotent under DUR-03/owning reward contract.

### `WORLD_SCOPED_UNIQUE`

Meaning:

- exactly one semantic world occurrence/eligibility exists regardless of active Channel count;
- event/boss/world-service owner defines where/how it is executed/presented;
- per-Channel runtime copies cannot independently mint another world occurrence.

### `EXPLICIT_EVENT_POLICY_REQUIRED`

Meaning:

- no default source/reward scope is safe;
- high-impact boss/raid/event owner must declare simulation and eligibility scope before activation.

A runtime object living in ChannelRuntime is not proof that its reward should be per Channel.

## 22. Simulation scope and eligibility scope

Reward-bearing encounters/events that matter across Channels must keep at least these concepts distinct:

```text
simulation_scope
eligibility_scope
reset/repeat policy
stable reward/source occurrence identity semantics
```

Examples are semantic only:

```text
simulation_scope = CHANNEL_LOCAL
eligibility_scope = CHARACTER_WORLD_COOLDOWN
```

or

```text
simulation_scope = WORLD_SCOPED_UNIQUE
eligibility_scope = WORLD_EVENT + domain-defined participant claims
```

GAME-CHANNEL does not define the reward formula. It requires the scopes so channel multiplication cannot decide reward multiplicity implicitly.

## 23. Reward anti-hopping

For any reward whose eligibility is Character/Account/World-scoped:

- ChannelId cannot be added to the reset/idempotency key merely to permit another claim;
- new GameSessionId cannot reset eligibility;
- channel-switch cooldown and reward eligibility are separate controls and neither substitutes for the other;
- queue/reconnect/failure cannot reset eligibility;
- stable cause/occurrence + DUR-03 transaction semantics prevent duplicate durable delivery;
- a replicated event across Channels may increase participation opportunity only as its owning event policy explicitly allows.

## 24. Dynamic channel creation versus economy policy

GAME-CHANNEL owns this constraint:

> The operational controller may activate/deactivate public Channels only inside the accepted versioned World channel-multiplicity policy. Operational capacity need does not grant authority to invent gameplay/economy semantics.

Division of responsibility:

### GAME-CHANNEL owns

- player-facing multiplicity model;
- whether independent public simulation is product-enabled;
- source/reward multiplicity invariants;
- allowed semantic policy envelope;
- social/fairness guardrails.

### PERF-01 owns

- measured players/channel, players/GameNode and players/World capacity;
- safe headroom and benchmark evidence;
- latency/queue/resource objectives.

### OPS-CHANNEL-01 owns

- actual activation/deactivation algorithm;
- hysteresis/cooldown for operational scaling;
- process/container placement;
- health/readiness orchestration;
- recovery concurrency;
- numeric operational thresholds.

No client gameplay command directly activates/deactivates a public Channel.

## 25. Fresh-channel/restart source safety

Channel lifecycle must not become a reward-reset primitive.

Binding rules:

- ordinary `CHANNEL_LOCAL_REPEATABLE` content may initialize/recover according to its normal runtime/content semantics;
- one-time/world-limited/high-impact sources cannot use process/channel uptime alone as eligibility truth;
- stopping/recovering the same ChannelId cannot reset durable Character/Account/World reward eligibility;
- a fresh ChannelId cannot erase prior shared eligibility;
- display-label reuse cannot reset eligibility;
- OPS lifecycle cause is not a player reward occurrence;
- exact ordinary spawn initialization timing remains content/runtime-owned.

## 26. PvP/channel contract

GAME-CHANNEL owns cross-channel product implications, not exact PvP arithmetic.

Binding rules:

- direct PvP execution remains current Channel/Instance-local;
- Character/World PvP consequences declared world/Character-scoped by the profile survive GameSession/channel transition;
- combat/protected PvP state blocks voluntary switching;
- Channel switching cannot clear/re-arm/reduce a PvP consequence merely by producing a new GameSession;
- failure/recovery cannot silently relocate an actor to another simulation to escape PvP;
- client claims of disconnect/failure do not create a trusted switch/cooldown exception;
- current destination profile/world policy is revalidated before fresh admission;
- exact skull/frag/Twist/fair-fight/Death Redemption/combat-lock values remain PvP/ruleset parity-owned.

## 27. One World community

Channels must not fragment semantic world identity.

Binding rules:

- guild membership/identity is not per Channel;
- market/bank/depot/rankings are not copied into separate channel economies;
- world/guild/private communication remains cross-channel where its accepted owner says so;
- local speech remains spatial/channel-local;
- party membership may span Channels while gameplay effects requiring co-location require actual shared simulation;
- recommendation/co-location should reduce involuntary party/friend fragmentation under capacity/privacy constraints;
- current World and current Channel must be understandable in future client UX;
- Channel does not become a new ruleset fork, protocol mode or account namespace.

## 28. Product-facing availability classes

GAME-CHANNEL defines semantic classes; client wording/UI remains downstream.

### `SELECTABLE`

Target may receive a fresh admission attempt subject to final FND-04 validation.

### `CAPACITY_LIMITED`

Target cannot admit immediately under current capacity policy. Queue may be offered if supported.

### `DRAINING`

No new ordinary admission. Existing actors progress to a safe lifecycle boundary under accepted runtime/OPS policy.

### `RECOVERING`

Same ChannelId recovery is in progress. Affected players use recovery/reconnect semantics rather than ordinary alternate-channel selection.

### `UNAVAILABLE`

Not currently selectable/routable.

Internal runtime states may map into these product classes without exposing NodeId/generation/security internals.

## 29. Full/capacity-limited behavior

`CAPACITY_LIMITED`/Full means:

- existing valid sessions continue under their owning runtime contract;
- new ordinary admissions do not bypass capacity simply because the client selected the target explicitly;
- explicit target may be offered a queue;
- automatic recommendation may select another eligible Channel;
- exact capacity threshold is PERF/OPS-owned;
- no hidden kick/move of existing players solely to make space for a new target.

## 30. Drain behavior

When a Channel is draining:

- remove it from ordinary selectable/recommended targets;
- stop new ordinary admissions;
- expose bounded player-facing maintenance/drain state once client UX exists;
- let existing actors reach accepted safe exit/checkpoint/session boundaries;
- a hard operational deadline may terminate sessions only through the owning safe shutdown/recovery contract;
- never silently move an actor to another Channel;
- after safe source termination the player can receive a fresh target offer and perform fresh admission;
- trusted maintenance exceptions to voluntary cooldown remain typed/audited and cannot reset PvP/reward/value consequences.

## 31. Failure and same-Channel recovery

ADR-0009 same-ChannelId recovery remains mandatory.

```text
Channel failure
-> recover/reconnect same ChannelId
-> no invisible fallback into another Channel
```

Rules:

- same semantic ChannelId survives eligible restart/recovery;
- NodeId and scope ownership generation may change;
- stale owner cannot resume authority;
- client may display same-Channel `RECOVERING` state;
- no alternate Channel becomes authoritative merely because it is healthy;
- if same-Channel recovery ultimately cannot continue under the owning operational contract, affected actor must first reach a proven safe offline/terminal authority state;
- only after that safe state may a fresh directory/offer let the player intentionally select/recommend another Channel;
- a system failure does not erase combat, reward or durable value consequences.

## 32. Channel lifecycle identity

GAME-CHANNEL consumes FND-ID/ADR-0009:

- temporary stop/recovery/reactivation of the same semantic Channel preserves ChannelId;
- ownership generation advances/fences as runtime contracts require;
- retiring a Channel is different from stopping it;
- retired ChannelId never identifies a new semantic Channel;
- public display labels may be presentation aliases but never lifecycle identity;
- Channel creation/retirement remains topology authority, not a GameNode self-issued identity operation.

## 33. World-policy revision

GAME-CHANNEL channel product policy is versioned under the already accepted `world_policy_revision` compatibility dimension.

It does not introduce a new protocol major or mandatory independent `channel_policy_revision` solely for this gate.

Consequences:

- FND-04 fresh admission revalidates current channel policy through world-policy compatibility;
- stale grants cannot silently enter under superseded channel policy;
- durable switch-guard state retains enough policy context for deterministic migration/interpretation;
- channel policy change does not change ChannelId;
- exact policy registry/storage is implementation/control-plane owned.

## 34. Policy updates and active sessions

A world-policy update affecting channel selection/switching/rewards must define version-skew behavior rather than assume every current session instantly restarts.

At minimum later rollout policy states:

- whether current admitted sessions remain valid until a bounded lifecycle point;
- whether new switch attempts use only the new policy;
- how active switch guards are interpreted/migrated;
- how stale queue entries/offers are invalidated;
- whether a changed multiplicity/event eligibility rule requires new event/ruleset/content revision instead of only world policy.

This contract does not choose deployment mechanism.

## 35. Client authority boundary

The client may:

- display current World/Channel and product availability;
- accept recommendation;
- select another currently visible eligible target;
- join/cancel a supported queue;
- request a voluntary safe channel change;
- show switch lock/cooldown/recovery states.

The client may **not** decide:

- target eligibility/capacity;
- queue priority;
- switch cooldown expiry;
- combat/trade/item/event switch-lock legality;
- reward eligibility;
- Channel lifecycle/health;
- recovery target;
- admission authority;
- current lease/session/runtime ownership.

## 36. Platform/control-plane boundary

Architecture may require Platform/Gateway/World Registry producer behavior at a contract level, but this delivery writes only Oteryn-v2.

A future cross-repository implementation may need separate Platform tasks for:

- recommendation/eligible-set material;
- optional queue state;
- target selection UX/API;
- current channel directory projection;
- fresh bound admission material issuance.

Those writes require explicit separate repository authority and one task/PR per repository. GAME-CHANNEL acceptance alone does not mutate Platform or production.

## 37. DUR-03 boundary

GAME-CHANNEL answers:

- whether a source/encounter/reward is channel-local, shared-eligibility, world-unique or explicit-policy-required;
- whether a voluntary Channel switch is product-eligible;
- what product guards must survive relog/session change.

DUR-03 remains sole owner of:

- durable item/currency/value atomicity;
- transaction identity/idempotency;
- one semantic item location;
- source/sink lineage;
- typed custody;
- stale-authority rejection for value mutation;
- ambiguous commit reconciliation;
- durable audit/restore anti-duplication invariants.

GAME-CHANNEL cannot authorize value creation by itself.

## 38. Downstream domain boundaries

### Party/social

GAME-CHANNEL owns co-location preference only. Party membership/leadership/shared-experience formulas/chat/friend policy remain social/party owners.

### Economy/trade/market

GAME-CHANNEL owns channel multiplicity and switch eligibility only. Prices, offers, fees, trades, bank/depot/mail lifecycle and economic business policy remain their owners.

### Bosses/events/rewards

GAME-CHANNEL requires simulation/eligibility scope declaration. Spawn schedule, participation, contribution, reward formula and reset logic remain event/reward owners.

### PvP

GAME-CHANNEL preserves consequences across switching. Exact formulas/profile semantics remain PvP/ruleset owner.

### Houses/instances

GAME-CHANNEL prohibits them from becoming implicit Channel switches. Their topology/lifecycle remain own contracts.

### Entitlements

No Premium/VIP/paid privilege or queue/switch priority is accepted. `PROD-ENTITLEMENTS-01` remains separately gated.

## 39. Failure dispositions

Semantic conditions and required outcomes:

| Condition | Required effect |
|---|---|
| stale/ineligible explicit target | no admission; fresh offer required |
| target capacity-limited | no admission; queue/alternate choice by policy |
| target draining | no new ordinary admission |
| target recovering | same-Channel recovery path for affected actor; no ordinary silent alternate |
| target revision incompatible | no admission; fresh compatible offer |
| hard switch lock active | no voluntary switch |
| cooldown guard active | no voluntary switch until authoritative eligibility |
| queue expired/cancelled | no gameplay/session/value effect |
| co-location target undisclosed | no privacy bypass; ordinary selection only |
| same reward occurrence already claimed | owning reward/DUR idempotent reconciliation; no second value |
| active Channel lifecycle resets | no reset of shared Character/Account/World eligibility |
| channel failure | same-Channel recovery; no automatic alternate-channel continuation |

Stable protocol error IDs remain later protocol/domain registration.

## 40. Security invariants

A conforming future implementation must preserve:

- no client-forged Channel eligibility, capacity or queue priority;
- no queue reference treated as gameplay bearer authority;
- no silent retarget of a bound explicit target;
- no relog/reconnect/GameSession reset of voluntary switch guard;
- no client-forged maintenance/failure cooldown exception;
- no Channel label/ordinal authority;
- no one Character authoritative on two Channels;
- no stale Channel owner durable write;
- no active combat/trade/item/event/instance bypass through Channel switch;
- no per-Channel reset of world/Character/account reward eligibility unless a dedicated repeatable policy explicitly owns it;
- no hidden rate change based solely on active Channel count;
- no silent alternate-channel failure recovery;
- no privacy bypass through co-location lookup;
- no Channel lifecycle reward-reset primitive;
- no instance/house Channel-switch portal;
- no Channel policy weakening DUR-03 conservation.

## 41. Resource ceilings

No unbounded user/load-controlled Channel structure is accepted.

Before implementation conformance, concrete absolute ceilings must exist for applicable structures including:

- public Channels per directory result;
- queue entries and bytes;
- queue requests per Account/Character;
- current offers/recommendation candidates;
- co-location hints;
- directory refresh/result size;
- switch attempt/rate-control state;
- policy object size/revision complexity;
- event/reward multiplicity fan-out work;
- recovery/queue pending control references.

This paper-only gate deliberately does not invent numeric ceilings without evidence. Missing required ceilings block implementation rather than mean unlimited.

## 42. Observability and analytics

Future implementation should produce privacy-safe evidence sufficient to evaluate channel policy, including:

- active public Channel count;
- players per Channel/World;
- recommendation acceptance/override;
- target Full/Draining/Unavailable selection failures;
- queue wait/cancel/alternate-choice;
- party/friend co-location success;
- successful voluntary switches;
- hard-lock/cooldown switch rejections;
- trusted maintenance/recovery switch causes;
- source/sink composition relative to active Channels/channel-hours/player population;
- reward duplicate/conflict evidence;
- population/social fragmentation;
- same-Channel recovery success/failure.

Game Intelligence remains observational/read-only. It may recommend policy changes to humans but may not automatically:

- open/close Channels;
- change spawn/loot rates;
- waive switch locks/cooldowns;
- change reward eligibility;
- move players;
- repair item/currency state.

## 43. Required implementation evidence

Architecture acceptance alone proves no runtime behavior.

A future implementation claiming GAME-CHANNEL conformance must prove at least:

### Selection/admission

- recommended target is only a hint and final FND-04 authority still decides;
- explicit target grant cannot be silently retargeted;
- stale/full/draining/incompatible target fails safely;
- client cannot submit a hidden/ineligible target as authority;
- world-policy revision changes invalidate stale target offers as accepted.

### Queue

- queue creates no GameSession/lease/value authority;
- queued admission revalidates fresh target/security/revisions;
- queue duplicate/cancel/expiry is idempotent;
- bounded queue overload fails safely;
- priority cannot be client-forged.

### Co-location

- recommendation favors party target when eligible;
- independent Character admissions preserve one-session rule;
- no partial co-location state grants authority to an unadmitted member;
- privacy-hidden placement cannot be discovered through join lookup.

### Switch/anti-hopping

- accepted hard blockers reject switch;
- durable cooldown survives logout/new GameSession/reconnect/restart;
- failed target attempt does not consume successful-switch cooldown;
- successful destination entry records cooldown boundary exactly once;
- same-Channel reconnect does not count as switch;
- trusted maintenance exception cannot be client-forged or clear PvP/reward state.

### Multiplicity/reward

- ordinary `CHANNEL_LOCAL_REPEATABLE` sources may independently occur per active Channel under unchanged ruleset mechanics;
- shared eligibility does not duplicate on another Channel/new GameSession;
- world-unique occurrence cannot mint per Channel;
- event with explicit simulation/eligibility scopes uses the correct stable reward/source identity;
- Channel stop/restart/new Channel/display-label reuse does not reset shared durable eligibility.

### Recovery/drain

- Full blocks new admission without disrupting existing sessions;
- Draining stops new admission and never silently migrates current actors;
- GameNode/Channel failure reconnects same ChannelId when recoverable;
- stale recovered owner cannot resume authority;
- alternate Channel becomes possible only after source actor state is safely terminal/offline and fresh admission occurs;
- failure does not erase combat/reward/item consequences.

### Economy/social evidence

- source/sink/channel-count evidence can identify multiplicity effects without high-cardinality metrics abuse;
- world/guild/private communication and world economy remain shared as accepted;
- local speech/combat/position remains Channel-local;
- Channel policy analytics cannot mutate gameplay.

## 44. Decision timing

### Must decide now?

**YES.**

### Downstream work blocked

- player-visible multichannel product behavior;
- channel directory/selection UX/API contracts;
- party/friend co-location behavior;
- queue semantics;
- voluntary switch implementation and VSL fixtures;
- channel scaling economy/fairness acceptance;
- multi-channel boss/event/reward semantics;
- PvP-safe switching;
- same-channel failure UX;
- `VSL-MULTICHANNEL-01` product-policy proof.

### Future migration cost if changed late

Late changes can require migration of switch-guard state, queue/control-plane contracts, reward eligibility keys, event definitions, presence UX, Channel directory semantics, economy telemetry interpretation, support tooling and cross-repository Gateway/World Registry behavior.

### Supersession evidence

A later explicit contract may change a clause with named evidence such as:

- channel-friction/co-location playtest evidence;
- economy/source/sink telemetry;
- PvP hopping abuse;
- availability/recovery failure evidence;
- privacy/security findings;
- PERF/OPS evidence requiring a different public multiplicity model;
- explicit product-owner strategy change.

OTS convention, framework preference or implementation convenience is insufficient.

## 45. Deliberately deferred

This contract does not decide:

- numeric voluntary switch cooldown;
- numeric queue limits/timeouts/priority weights;
- min/max public Channel count;
- players/Channel/GameNode/World capacity thresholds;
- autoscaling thresholds/hysteresis;
- orchestrator/service topology;
- exact client UI/channel labels;
- complete presence/privacy visibility matrix;
- exact PvP formulas/world type;
- exact boss/event/reward schedules/contribution formulas;
- exact spawn/loot probabilities/rates;
- market/trade/bank/depot/mail business rules;
- exact PostgreSQL/control-plane schema;
- concrete ANL event IDs/payloads;
- protocol numeric errors/messages;
- production admin exception implementation;
- Premium/VIP/commerce or paid queue priority.

## 46. Acceptance consequence

Only after:

1. this candidate delivery passes exact-head implementing-agent full-diff self-review;
2. required genuinely independent review has zero open material findings;
3. exact-head documentation/governance CI passes;
4. review threads and ownership conflicts are clean;
5. PR #209 is squash-merged unchanged; and
6. a separate lifecycle closeout atomically promotes maintained programme status/handoff,

may programme state become:

```text
GAME-CHANNEL-01
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
runtime/client authority = NONE
DDL/migration authority  = NONE
production authority     = NONE
```

Architecture acceptance does not authorize multichannel runtime, Gateway queue/recommendation implementation, switch persistence, client UI, autoscaling, PvP/reward implementation or production activation.
