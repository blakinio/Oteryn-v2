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

Oteryn already accepts the technical multichannel model:

```text
one logical WorldId
-> one economy / community / ruleset family
-> multiple ChannelId values
-> independent public-world simulation per Channel
-> one logical mutation owner per ChannelRuntime
```

What is still missing is the **product policy** around that capability.

Without a dedicated gate, an implementation could be technically race-free but product-incorrect, for example by:

- always auto-assigning players and breaking parties/friends apart;
- allowing repeated channel hopping for fresh local opportunities or PvP escape;
- multiplying boss/reward eligibility simply because several ChannelRuntime copies exist;
- treating queue state as a GameSession or reserved gameplay authority;
- silently rerouting a failed Channel A player into live Channel B;
- making autoscaling secretly divide/multiply spawn or loot rates;
- using `Channel 2` text as durable identity;
- letting a crash after destination admission skip durable anti-hopping state;
- letting a channel-local runtime object silently imply per-channel durable reward semantics.

GAME-CHANNEL-01 therefore freezes only the **player/economy/social/PvP semantics around channels**, while preserving FND runtime/admission, DUR conservation, OPS/PERF orchestration/capacity and downstream gameplay owners.

## 2. Binding inputs

### ADR-0001 / FND-ID-01

`PROVEN`:

- World is one product/economy/community boundary;
- Channel is one parallel public-world simulation;
- `ChannelRef = WorldId + ChannelId` is canonical;
- ChannelId is topology-owned, durable and never reused for a different semantic Channel;
- positions/creatures/combat/ground runtime are channel-local;
- Character progression, selected economy/social state and reward eligibility may be world/Character scoped;
- completed channel change is already a safe fresh-session/admission transition, not teleport/rebind;
- combat lock, direct trade, unresolved item mutation, protected encounter and unsafe instance/house transitions already block switching.

### ADR-0009 / FND-03

`PROVEN`:

- GameNode/ChannelRuntime lifecycle and one-writer semantics are already accepted;
- Channel activation/closure may be dynamic;
- numeric capacity and trigger thresholds need PERF evidence;
- same semantic ChannelId is recovered after failure;
- players are not silently moved to another live Channel after failure;
- process/container orchestration is not GAME-CHANNEL ownership.

### FND-04

`PROVEN`:

- directory/Gateway/control-plane may authorize one bounded attempt;
- game domain owns final admission;
- fresh admission material binds one exact WorldId + ChannelId and current revisions;
- same grant cannot be silently retargeted;
- canonical GameSessionId is game-issued after successful admission.

### GAME-VISION-01

`PROVEN`:

- solo viable, party rewarded;
- PvP secondary pillar;
- conservation before tuning;
- no hidden macro economy tuning;
- group rewards may not rely on duplicate eligibility;
- channel friction/social distribution should become measurable product evidence.

### DUR-03

`PROVEN`:

- one durable ItemInstance has one semantic location;
- stale session/runtime authority cannot commit durable value;
- retry/ambiguous commit cannot duplicate value;
- source/reward occurrences can carry stable idempotency;
- Game Intelligence is read-only toward authority.

GAME-CHANNEL decides **channel multiplicity/eligibility policy**. DUR-03 remains the value transaction/conservation owner.

## 3. Reference boundary

`DERIVED`:

Public multichannel selection/hopping is an Oteryn product layer; Global Tibia does not expose Oteryn ChannelId policy.

Therefore:

- in-channel Reference mechanics still target the accepted 2026-07-28 behavior cut;
- channel policy is explicit Oteryn product policy, not inferred from current Global or OTS convention;
- exact PvP/loot/boss formulas stay with their parity/gameplay owners.

## 4. Decision timing

### Must decide now?

**YES.** The owner-accepted programme refinement requires GAME-CHANNEL-01 before multichannel becomes a product feature.

### Blocks

- public channel directory/selection;
- queue semantics;
- party/friend co-location;
- safe voluntary channel switching;
- anti-hopping that survives GameSession changes;
- channel multiplicity/economy intent;
- multichannel boss/event/reward scope;
- PvP-safe switching;
- drain/recovery UX;
- `VSL-MULTICHANNEL-01` product-policy proof.

### Late-change cost

Potential rework/migration of Gateway offers, switch-guard state, queue semantics, reward keys, event scopes, client UX, presence/privacy, economy telemetry, support tooling and E2E fixtures.

### Supersession evidence

Playtests, economy telemetry, PvP abuse findings, recovery/availability evidence, privacy/security findings, PERF/OPS evidence or explicit product-owner strategy change. Implementation convenience alone is insufficient.

## 5. Product identity model

Recommended:

```text
WorldId
= persistent product/economy/community/ruleset identity

ChannelRef = WorldId + ChannelId
= persistent identity of one parallel public-world simulation

current Channel placement
= session/lease/runtime fact
!= Character identity
!= economy namespace
!= social namespace
!= progression namespace
```

Instances/houses are not hidden Channels and cannot be channel-switch portals.

## 6. Display identity

A label such as `Channel 1` is presentation only.

- queue/admission/audit/reward logic resolves canonical ChannelRef;
- stop/recovery of the same semantic Channel preserves ChannelId;
- retired ChannelId is never reused;
- display label/ordinal may change or later be reused only if no durable/security logic relies on it;
- NodeId/ownership generation are not player channel identity.

## 7. Entry model options

### Auto-only

Good balancing, poor agency/co-location. Rejected as sole model.

### Manual-only

Good agency, poor balancing/queue pressure. Rejected as sole model.

### Recommendation + explicit eligible override

Control plane returns eligible targets plus one recommendation. Player may accept or choose another currently eligible visible target.

Recommendation may use capacity/health, previous-channel affinity, party/friend hints subject to privacy and demand balancing. Exact scoring remains product/implementation tuning.

**Recommended.**

## 8. Explicit target failure

If explicitly selected Channel C becomes Full/Draining/Recovering/Unavailable/stale/incompatible:

```text
no admission to C
-> no silent retarget using same authorization
-> fresh directory/offer/grant for another target
```

This preserves FND-04 target binding.

## 9. Queue options

### No queue

Simple, weak UX for parties/popular channels.

### World-global queue

Does not preserve explicit target choice/co-location semantics.

### Optional bounded target-Channel pre-admission queue

Recommended.

Queue state:

```text
!= GameSession
!= CharacterLease
!= runtime ownership
!= value reservation
!= guaranteed admission
```

A short-lived FND-04 grant is minted/refreshed only when the queued attempt is ready; it is not parked in a long queue. Final admission revalidates current facts.

Queue storage/service/priority/timeouts/rate limits remain Platform/OPS implementation work.

## 10. Live-session destination queue

ADR-0001 already orders safe source exit before destination selection/admission. First generation therefore does **not** reserve/queue another Channel while the Character continues authoritative mutation in the source Channel.

A future live-session reservation would require a separate lease/capacity/failure/fairness contract.

## 11. Party/friend co-location

Recommended first generation:

- co-location is a recommendation/explicit target hint, not authority;
- every Character is admitted independently;
- no all-or-nothing party admission transaction;
- no party-owned Channel;
- no automatic teleport/migration with another party member;
- shared-exp/proximity effects require real co-location;
- exact friend/party placement disclosure remains presence/privacy-owned.

Atomic party capacity reservation is deferred until product evidence justifies it.

## 12. Reconnect versus switch

```text
same-Channel eligible reconnect/recovery
!= completed Channel switch
```

Same-Channel reconnect can preserve GameSessionId according to FND-04 and does not count as a switch.

Completed switch consumes ADR-0001 safe exit, fresh destination authorization/admission and a fresh canonical GameSessionId.

## 13. Hard switch blockers

Keep accepted blockers including:

- combat/protected PvP;
- direct trade;
- unresolved DUR-03 item/value transaction;
- protected boss/raid/event participation;
- unsafe instance/house transition;
- pending Character authority/checkpoint/handoff;
- stale/unavailable session/lease/runtime authority;
- destination revision incompatibility;
- destination Full/Draining/Recovering/Unavailable.

No client override.

## 14. Anti-hopping options

### Hard locks only

Insufficient against repeated safe-boundary hunting/resource hopping.

### GameSession-local timer

Rejected because relog/new GameSession resets it.

### Durable Character+World guard

Recommended.

Important ownership refinement:

```text
scope: CharacterId + WorldId
semantic owner: GAME-CHANNEL / world channel-policy authority
not automatically GAME-CHAR progression state
interpretation: world_policy_revision
lifetime: may outlive GameSession/connection/GameNode
```

Physical persistence stays downstream.

## 15. Switch cooldown

The first anti-hopping mechanism is a **time-based voluntary switch cooldown + hard locks**.

- exact duration is evidence/owner-owned and deliberately not guessed;
- guard survives logout/relog/fresh GameSession/reconnect/restart;
- same-Channel reconnect does not consume/reset it;
- failed destination attempt does not count;
- successful destination channel admission is the switch boundary;
- client time is never authority;
- policy revision changes use explicit migration/interpretation.

## 16. Critical atomicity: destination admission + guard advance

A crash window must not allow:

```text
destination GameSession becomes playable
BUT ChannelSwitchGuard was not advanced
```

Therefore a **voluntary switch admission** must include the guard decision/update in the same authoritative acceptance boundary as destination placement/session authority, or an equivalently proven recovery protocol with these properties:

- no playable destination authority is exposed before guard advancement is durably determined;
- ambiguous outcome reconciles the same admission/switch attempt rather than creating another switch;
- retry cannot mint a second destination session/effect;
- guard and resulting current Channel cannot disagree silently;
- destination final admission revalidates current world-scoped switch locks/guard rather than trusting source-side earlier checks.

Physical DB/session implementation belongs FND/DUR implementation. GAME-CHANNEL freezes the invariant.

No new `ChannelSwitchId` is introduced by default: existing FND admission attempt/session/ANL correlation identities are consumed unless implementation evidence proves a separate durable operation identity is needed.

## 17. Trusted forced exceptions

Maintenance/incident/admin-safe evacuation may later define a typed trusted exception to voluntary cooldown, but only when server/operator authored, audited, unforgeable by client and incapable of clearing PvP/reward/value consequences.

Changing ChannelId still uses fresh admission. No generic bypass boolean.

## 18. The multiplicity problem

More independent public Channels can mean more local monsters/spawns/loot opportunities feeding one World economy.

Rejected defaults:

- hidden inverse rate scaling by active Channel count;
- one giant world-shared lock/pool for every ordinary spawn.

Recommended: explicit **source multiplicity + eligibility classification**.

## 19. Fail-closed source classification

Runtime locality does **not** automatically decide durable reward/source multiplicity.

For every value-producing source/encounter family whose behavior can differ with Channel count, the compiled/validated content/ruleset/event policy must explicitly select a supported class. Missing classification for a value-producing source is an implementation/content validation blocker, not an implicit `CHANNEL_LOCAL_REPEATABLE` fallback.

A profile/content package may declare a reviewed default for a bounded source category, but that default itself is explicit/versioned content policy, not a hardcoded runtime assumption.

This removes the ambiguity between “monster runtime is channel-local” and “all durable value from it may always multiply per Channel.”

## 20. Multiplicity classes

### `CHANNEL_LOCAL_REPEATABLE`

- independent source/simulation per Channel;
- output may repeat independently under unchanged in-Channel ruleset mechanics;
- aggregate World supply may scale with active Channels/player demand;
- no hidden rate division by Channel count;
- exact loot/source formula remains content/Reference-owned.

### `CHANNEL_LOCAL_SHARED_ELIGIBILITY`

- simulation can occur on multiple Channels;
- durable claim eligibility is shared at declared Character/Account/World/etc. scope;
- hopping/new GameSession cannot reset eligibility.

### `WORLD_SCOPED_UNIQUE`

- one semantic World occurrence/eligibility regardless of Channel copies;
- event/world-service owner decides execution/presentation placement.

### `EXPLICIT_EVENT_POLICY_REQUIRED`

- no safe generic classification;
- high-impact boss/raid/event must declare simulation + eligibility semantics before activation.

## 21. Simulation scope != eligibility scope

Every reward-bearing event where Channels matter declares at least:

```text
simulation_scope
eligibility_scope
reset/repeat policy
stable reward/source occurrence semantics
```

Example:

```text
simulation = CHANNEL_LOCAL
eligibility = CHARACTER_WORLD_COOLDOWN
```

DUR-03 owns delivery idempotency/conservation; event/reward domain owns eligibility business rules.

## 22. Dynamic scaling boundary

GAME-CHANNEL owns:

- player-visible multiplicity model;
- permitted source/reward semantics;
- social/fairness guardrails;
- versioned World channel-policy envelope.

PERF-01 owns numeric capacities/headroom.

OPS-CHANNEL-01 owns activation/deactivation algorithm, hysteresis, placement, health/readiness and process orchestration.

Operational load cannot silently authorize new economy semantics. No client command directly creates/removes a public Channel.

## 23. Fresh/restarted Channel abuse

- stop/recover same ChannelId cannot reset durable shared eligibility;
- new ChannelId cannot erase Character/Account/World eligibility;
- display ordinal reuse cannot reset eligibility;
- one-time/high-impact sources cannot use process uptime alone as eligibility truth;
- Channel lifecycle is not a player reward-reset API;
- exact ordinary spawn initialization remains content/runtime-owned.

## 24. PvP implications

GAME-CHANNEL freezes only cross-channel consequences:

- combat execution is local to current Channel/Instance;
- world/Character-scoped PvP consequences survive GameSession/channel transition;
- active combat/protected PvP blocks voluntary switch;
- failure does not move actor into another simulation;
- client disconnect claim cannot create a trusted exception;
- exact skull/frag/Twist/fair-fight/combat-lock formulas remain parity/profile-owned.

## 25. Social/community safeguards

A World remains one community:

- guild membership not per Channel;
- market/bank/depot/rankings not separate Channel economies;
- accepted world/guild/private communication remains cross-channel;
- local speech remains channel/spatial;
- party membership may span Channels but gameplay co-location effects require same simulation;
- recommendation should reduce involuntary fragmentation;
- future client shows current World and Channel clearly.

## 26. Product-facing availability

Recommended semantic classes:

- `SELECTABLE` — fresh attempt may proceed subject to FND-04;
- `CAPACITY_LIMITED` — no immediate admission, queue may exist;
- `DRAINING` — no new ordinary admission;
- `RECOVERING` — same ChannelId recovery path;
- `UNAVAILABLE` — not selectable/routable.

Internal NodeId/generation/Fenced/Suspected details are not necessarily player-visible.

## 27. Drain

- leave ordinary selectable/recommended set;
- stop new admission;
- current actors reach safe FND/DUR lifecycle boundary;
- no silent cross-channel migration;
- after safe termination a fresh target/admission may occur;
- maintenance exception cannot clear combat/reward/value consequence.

## 28. Failure/recovery

Default:

```text
failed Channel A
-> recover same ChannelId A
-> never silently continue in B
```

If recovery cannot continue, first prove actor safe/offline/terminal. Only then fresh directory/selection/admission may target another Channel. Failure does not erase combat/reward/value state.

## 29. World-policy revision

GAME-CHANNEL uses existing `world_policy_revision`; it does not invent a new protocol major/revision dimension solely for channel policy.

Stale grants/offers cannot silently apply superseded policy. Durable switch guard retains enough revision context for deterministic migration.

## 30. Cross-world boundary

Selecting another WorldId is **not** a Channel switch. It remains a separate world/lifecycle/transfer/admission concern under existing world-profile/Character contracts. GAME-CHANNEL cannot use channel selection to bypass default world-scoped value isolation.

## 31. Security review

Must prevent:

- client-forged target eligibility/capacity/queue priority;
- queue token as gameplay bearer authority;
- silent target retarget;
- GameSession reset of cooldown;
- crash window where destination authority exists without guard advance;
- client-forged maintenance exception;
- Channel label as identity;
- dual active Character across Channels;
- stale owner durable writes;
- switch through combat/trade/item/event/instance blockers;
- per-Channel reset of shared reward eligibility;
- runtime-locality defaulting durable source multiplicity;
- hidden inverse spawn/loot scaling;
- silent alternate-channel failure recovery;
- privacy bypass via co-location;
- Channel lifecycle reward reset.

## 32. Resource limits before implementation

Numeric values are deliberately deferred, but implementation requires hard bounds for applicable externally influenced structures: directory size, public Channels per result, queue entries/bytes, queue requests per Account/Character, pending offers, co-location hints, switch attempts, policy object size and event/reward multiplicity fan-out.

Missing bounds block implementation rather than mean unlimited.

## 33. Analytics

Measure without becoming authority:

- active Channel count/player distribution;
- recommendation acceptance/override;
- queue wait/cancel;
- co-location success;
- switch success/rejection/cause;
- source/sink composition by Channel-hours/player population;
- reward conflicts;
- social fragmentation;
- same-Channel recovery success.

Game Intelligence may recommend human policy changes but never open/close Channels, change rates, waive locks, alter eligibility or move players automatically.

## 34. Recommendation summary

| Subject | Recommendation |
|---|---|
| entry | recommendation + explicit eligible override |
| explicit target stale/full | fail closed + fresh offer/grant |
| queue | optional bounded target pre-admission queue |
| live-session destination queue | deferred |
| co-location | best-effort hints + independent admission |
| switch | ADR-0001 fresh session transition |
| anti-hopping | GAME-CHANNEL-owned durable Character+World guard |
| cooldown | mandatory semantic mechanism, numeric value evidence-owned |
| switch commit | guard advance + destination admission one recovery-safe authoritative boundary |
| source multiplicity | explicit fail-closed classification; no runtime fallback |
| boss/event reward | explicit simulation scope + eligibility scope |
| scaling | product envelope here; numbers PERF; orchestration OPS |
| failure | same-Channel recovery, later explicit fresh switch only from safe state |
| policy revision | existing world_policy_revision |

## 35. Deliberately not decided

- numeric switch cooldown;
- queue lengths/timeouts/priority weights;
- min/max public Channel count;
- capacity/autoscaling thresholds;
- orchestrator/service topology;
- exact client UI;
- full presence privacy matrix;
- exact PvP/boss/reward/spawn/loot formulas;
- market/trade/bank/depot/mail logic;
- physical persistence/control-plane schema;
- protocol numeric errors/messages;
- production admin exception implementation;
- monetization/Premium/VIP/paid queue priority.

## 36. Acceptance consequence

If companion contract passes delivery + lifecycle closeout:

```text
GAME-CHANNEL-01
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
runtime/client authority = NONE
DDL/migration        = NONE
production authority = NONE
```

It would unblock later channel-product implementation/VSL policy work, not prove or authorize runtime behavior.
