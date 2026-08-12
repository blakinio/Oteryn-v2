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

Freeze the minimum product semantics required before Oteryn's accepted multichannel technical capability becomes a player-visible feature.

This contract owns channel discovery/selection, co-location, queue meaning, voluntary switching/anti-hopping, channel multiplicity and reward/source scope policy, PvP/social cross-channel consequences, player-facing drain/recovery behavior and the boundary with OPS/PERF/runtime/downstream domains.

It does not own GameNode/ChannelRuntime code, process orchestration, FND admission mechanics, DUR value mechanics, exact PvP/reward/economy formulas, physical persistence, Platform implementation or production rollout.

## 2. Authority chain

```text
World/Channel identity + multichannel foundation     -> FND-ID-01 + ADR-0001
ChannelRuntime/GameNode lifecycle                    -> ADR-0009 + FND-03
fresh admission / GameSession / CharacterLease       -> FND-04
minimum product/economy/party/PvP direction          -> GAME-VISION-01
Character semantics                                  -> GAME-CHAR-01
item legality                                        -> GAME-ITEM-01
item/currency/value conservation                     -> DUR-03
channel product policy                               -> GAME-CHANNEL-01
numeric capacity                                     -> PERF-01
activation/deactivation/process orchestration        -> OPS-CHANNEL-01
exact PvP/event/reward/economy/social business rules -> owning domain gates
```

No layer may redefine another owner's semantic authority for convenience.

## 3. Canonical channel model

```text
WorldId
= one persistent product/economy/community/ruleset boundary

ChannelRef = WorldId + ChannelId
= one persistent identity of a parallel public-world simulation

current Character Channel placement
= current GameSession/lease/runtime placement fact
!= Character identity
!= economy namespace
!= progression namespace
!= social namespace
```

Different ruleset/profile families are different Worlds, not special Channels. InstanceId is not ChannelId. House/instance transitions never silently change ChannelId.

## 4. Identity versus presentation

Canonical identity is ChannelRef.

- ChannelId is strongly typed and never inferred from display text/index;
- restart/recovery/relocation of the same semantic Channel preserves ChannelId;
- retired ChannelId is never reused for another semantic Channel;
- display label/ordinal may change or later be reused only as presentation;
- display identity never drives queue, admission, switch, audit, reward or durable eligibility;
- NodeId/ownership generation are not player Channel identity.

## 5. Directory and entry modes

A public directory/offer is a bounded control-plane view of current policy-eligible Channels. It may expose a safe reference, display label, product availability class, queue availability and privacy-permitted co-location/recommendation hints.

Accepted entry modes:

### `RECOMMENDED`

Control plane suggests one current eligible target.

### `EXPLICIT`

Player selects another current eligible visible target.

Recommendation is a hint, explicit target is a request, and FND-04 remains final admission authority.

Recommendation may use capacity/health, previous-channel affinity, party/friend hints subject to privacy, demand balancing and maintenance state. Exact scoring remains downstream.

## 6. Explicit target failure

For explicit Channel C:

```text
current eligible offer for C
-> bounded authorization for C
-> final FND-04 validation for C
```

If C becomes capacity-limited, draining, recovering, unavailable, stale or incompatible:

- no admission to C;
- no silent retarget using the same authorization;
- fresh directory/offer/grant is required for another target;
- failed target creates no GameSession/lease/value authority.

## 7. Queue contract

A World may support an optional bounded target-Channel **pre-admission queue**.

```text
queue state
!= GameSession
!= CharacterLease
!= runtime ownership
!= durable value reservation
!= guaranteed admission
```

Rules:

- one queue target resolves exactly one ChannelRef;
- priority/order is control-plane authoritative, never client-declared;
- entries/references are bounded, purpose-limited and expire/cancel explicitly;
- duplicate/cancel/expiry is idempotent and non-gameplay-mutating;
- final admission revalidates current target/security/revision/account/Character/lease facts;
- short-lived FND-04 admission material is issued/refreshed only when the queued attempt is ready, not parked for a long queue;
- queue reference is never bearer gameplay authority;
- exact storage/service/algorithm/timeouts/limits/priority remain downstream/cross-repository implementation work.

Automatic entry should normally prefer another healthy eligible Channel over needless target-specific waiting when the player did not explicitly request a target.

## 8. No first-generation live-session destination reservation

ADR-0001 safe switch flow reaches a safe source-session boundary before destination selection/admission.

GAME-CHANNEL therefore does not authorize queueing/reserving a destination while the Character continues authoritative mutation in the source Channel. A future live-session reservation requires a dedicated lease/capacity/fairness/failure contract.

## 9. Party/friend co-location

- co-location is a privacy-bounded recommendation/target preference, not authority;
- every Character is independently admitted with independent GameSession/lease;
- no all-or-nothing party admission transaction;
- no PartyId owns/reserves a Channel by itself;
- no automatic teleport/migration when another party member changes Channel;
- Full target uses ordinary queue/alternate-choice policy;
- shared-exp/proximity/combat effects require actual co-location under their owners;
- exact placement visibility remains social/privacy-owned.

Atomic group-capacity reservation is deferred.

## 10. Reconnect is not channel switch

### Same-Channel eligible reconnect/recovery

- uses FND-04 continuity;
- may preserve GameSessionId when permitted;
- keeps the same semantic ChannelId;
- does not count as voluntary Channel switch.

### Completed Channel switch

- safe source exit/checkpoint under ADR-0001;
- source session/lease authority ends or advances as required;
- fresh destination authorization;
- fresh FND-04 destination admission;
- fresh canonical GameSessionId;
- destination ChannelRuntime placement.

A switch is never an in-place transport rebind or teleport.

## 11. Hard switch locks

Voluntary switch fails closed while any accepted blocker applies, including:

- combat/protected PvP;
- direct trade;
- unresolved item/currency/value transaction;
- protected boss/raid/event participation where hopping affects eligibility;
- unsafe instance/house transition;
- pending Character checkpoint/handoff/authority transition;
- stale/unavailable session/lease/runtime evidence;
- destination incompatibility;
- destination capacity-limited/draining/recovering/unavailable state.

Client cannot override these locks.

## 12. Durable voluntary anti-hopping guard

Hard locks alone do not prevent repeated safe-boundary hopping.

GAME-CHANNEL requires durable game-domain world channel-policy state:

```text
scope: CharacterId + WorldId
semantic owner: GAME-CHANNEL / world channel-policy authority
lifetime: may outlive GameSession/connection/GameNode
interpretation: world_policy_revision
```

The guard is not automatically GAME-CHAR progression state merely because it is Character-scoped.

It must retain enough durable semantic state to classify later admissions unambiguously, including:

```text
last_successful_channel_ref
OR an equivalently unambiguous durable prior-placement representation
```

plus current switch eligibility/cooldown state and policy-version context as required.

Physical schema/storage remains downstream.

## 13. Switch classification across logout/relog

The durable prior-placement fact closes the relog loophole:

- first admission with no prior successful Channel establishes the baseline Channel without counting as a switch;
- fresh admission to the same prior Channel is not a switch;
- fresh admission to a different Channel is a switch even when the prior GameSession already ended;
- an unexpired guard still applies after logout/relog;
- failed destination attempt leaves the last successful Channel/guard unchanged;
- successful different-Channel admission updates the remembered Channel and advances the guard exactly once;
- same-Channel reconnect/recovery never rewrites the event as a switch.

A Channel retirement/maintenance/failure that forces a different destination may later use the trusted non-voluntary exception policy, but cannot make the prior placement unknowable.

## 14. Switch cooldown

The first voluntary anti-hopping mechanism is **time-based cooldown + hard locks**.

- exact duration is deliberately not guessed and must be accepted from product/playtest/economy/PvP evidence before activation;
- guard survives logout/relog/fresh GameSession/reconnect/GameNode restart;
- client wall time is not authoritative;
- policy evolution is version-aware;
- implementation cannot claim voluntary switch conformance until a concrete accepted duration and trusted durable time interpretation exist.

## 15. Destination admission + guard atomicity/recovery invariant

This outcome is invalid:

```text
new destination GameSession/placement becomes playable
AND durable ChannelSwitchGuard / last successful Channel did not advance consistently
```

For a voluntary different-Channel admission, final destination admission must include guard classification/update in the **same authoritative acceptance boundary** as destination session/placement authority, or an equivalently proven recovery protocol satisfying all of:

1. no playable destination authority before durable switch outcome is determined;
2. final admission revalidates current world-scoped locks/guard instead of trusting earlier source checks;
3. ambiguous outcome reconciles the same admission/switch attempt;
4. retry cannot create a second destination authority or skip guard;
5. current Channel, remembered successful Channel and guard cannot disagree silently;
6. crash after durable acceptance reconstructs one semantic outcome.

Physical transaction/session persistence mechanics remain FND/DUR implementation work.

No mandatory `ChannelSwitchId` is introduced: existing FND admission-attempt/session and ANL correlation/operation identities are reused unless later evidence proves a separate durable lifecycle identity is necessary.

## 16. Guard policy evolution

Incompatible world-policy change affecting guard state explicitly chooses transition semantics, such as preserving prior deadline, deterministic version-aware migration or applying new policy only to later switches. Silent retroactive reinterpretation is prohibited.

## 17. Trusted non-voluntary exception

Maintenance/incident/admin-safe evacuation may later define a typed exception only when:

- server/operator authored and audited;
- client cannot request/forge it;
- source actor reaches a safe authority/value boundary;
- PvP/combat/reward eligibility is not cleared/weakened;
- DUR-03 state remains valid;
- different ChannelId still uses fresh admission;
- remembered successful Channel/guard transition remains deterministic;
- exception is versioned/bounded.

No generic bypass boolean exists.

## 18. Channel locality is not durable source multiplicity

Channel-local runtime examples include position, creatures/spawns/AI, combat, ground runtime, local NPC and local speech. World/Character-shared durable examples include committed Character state, world economy domains and shared reward eligibility under their owners.

Critical rule:

```text
runtime object is Channel-local
!= durable reward/source is automatically repeatable per Channel
```

## 19. Fail-closed source multiplicity classification

For every value-producing source/encounter family whose durable output can differ with active Channel count, compiled/validated authored policy must explicitly select a supported class.

**There is no runtime fallback class for a value-producing source.**

Missing classification blocks that source's multichannel activation/implementation.

A reviewed content/profile package may define a default for a bounded source category, but that default itself is explicit/versioned authored policy, not a runtime assumption.

## 20. Multiplicity classes

### `CHANNEL_LOCAL_REPEATABLE`

- independent source/simulation per Channel;
- output may repeat independently under unchanged in-Channel ruleset mechanics;
- aggregate World supply may scale with active Channel count/player demand;
- no hidden automatic rate division by Channel count;
- exact source/loot formula remains content/Reference-owned;
- DUR-03 prevents duplicate transaction effects.

### `CHANNEL_LOCAL_SHARED_ELIGIBILITY`

- simulation can exist in multiple Channels;
- durable eligibility is shared at declared Character/Account/World/etc. scope;
- Channel change/new GameSession cannot reset eligibility;
- durable delivery uses owning reward + DUR-03 idempotency.

### `WORLD_SCOPED_UNIQUE`

- one semantic World occurrence/eligibility regardless of Channel count;
- event/world-service owner defines execution/presentation placement;
- Channel copies cannot independently mint another world occurrence.

### `EXPLICIT_EVENT_POLICY_REQUIRED`

- no generic classification is safe;
- high-impact boss/raid/event must declare exact simulation/eligibility model before activation.

## 21. Simulation scope != eligibility scope

Any reward-bearing event where Channels matter declares at least:

```text
simulation_scope
eligibility_scope
reset/repeat policy
stable reward/source occurrence semantics
```

ChannelId is not silently inserted into Character/Account/World reward reset/idempotency keys.

GAME-CHANNEL defines scope requirements; event/reward domains define business rules; DUR-03 defines transaction/conservation.

## 22. Dynamic scaling boundary

### GAME-CHANNEL

Owns player-visible multiplicity model, source/reward classification requirement, social/PvP/fairness guardrails and versioned World policy envelope.

### PERF-01

Owns numeric players/Channel/GameNode/World capacities, headroom and benchmark objectives.

### OPS-CHANNEL-01

Owns activation/deactivation algorithm, hysteresis, GameNode placement, health/readiness orchestration, recovery concurrency and numeric operational thresholds.

Operational load cannot silently authorize economy semantics. No client gameplay command directly creates/removes a public Channel.

## 23. Fresh/recovered Channel abuse prevention

- stop/recover same ChannelId cannot reset durable shared eligibility;
- new ChannelId cannot erase Character/Account/World eligibility;
- display-label reuse cannot reset eligibility;
- one-time/high-impact sources cannot use process/channel uptime alone as eligibility truth;
- OPS lifecycle is not a player reward occurrence;
- exact ordinary spawn initialization timing stays content/runtime-owned.

## 24. PvP implications

- direct PvP execution is current Channel/Instance-local;
- Character/World-scoped PvP consequences survive Channel/GameSession transition;
- active combat/protected PvP blocks voluntary switch;
- switching cannot clear/re-arm/reduce consequences merely through new GameSession;
- channel failure cannot silently relocate actor to another combat simulation;
- client disconnect claim cannot create trusted exception;
- exact PvP/skull/frag/combat formulas remain profile/parity-owned.

## 25. One World community

- guild identity/membership is not per Channel;
- market/bank/depot/rankings are not separate Channel economies;
- accepted world/guild/private communication remains cross-channel;
- local speech remains channel/spatial;
- party membership may span Channels while gameplay co-location effects require shared simulation;
- recommendation should reduce involuntary fragmentation;
- future client clearly exposes current World/Channel;
- Channel is not protocol/ruleset/account namespace.

## 26. Product-facing availability classes

- `SELECTABLE` — fresh attempt may proceed subject to FND-04;
- `CAPACITY_LIMITED` — no immediate admission, queue may be offered;
- `DRAINING` — no new ordinary admission, existing actors approach safe boundary;
- `RECOVERING` — same ChannelId recovery path for affected actor;
- `UNAVAILABLE` — not selectable/routable.

Internal NodeId/generation/Fenced/Suspected detail may map to these without verbatim exposure.

## 27. Drain

- remove from ordinary selectable/recommended targets;
- stop new admission;
- current actors reach safe FND/DUR lifecycle boundary;
- no silent cross-channel migration;
- after safe source termination, fresh target selection/admission may occur;
- maintenance exception cannot clear combat/reward/value state.

## 28. Failure and same-Channel recovery

```text
failed Channel A
-> recover same semantic ChannelId A
-> never silently continue in Channel B
```

ChannelId survives eligible recovery while NodeId/ownership generation may change. Stale owner cannot regain authority. If recovery cannot safely continue, actor first reaches proven safe offline/terminal state; only then can fresh selection/admission target another Channel. Failure does not erase combat/reward/value consequences.

## 29. Channel lifecycle identity

Temporary stop/recovery/reactivation preserves semantic ChannelId. Retirement differs from stop. Retired ChannelId is never reused. Display aliases are non-authoritative. Topology authority issues/retires canonical Channel identity.

## 30. World-policy revision

GAME-CHANNEL uses existing `world_policy_revision` for channel product policy compatibility rather than inventing a new protocol major/revision dimension.

- stale grants/offers cannot silently apply superseded policy;
- guard retains enough policy context for deterministic migration;
- ChannelId does not change because policy changed;
- exact policy registry/storage remains downstream.

## 31. Cross-world boundary

Changing WorldId is not a Channel switch. It remains a separate Character/world lifecycle/transfer/admission concern and cannot use channel policy to bypass world-scoped value/profile isolation.

## 32. Client authority boundary

Client may display/select/request/queue, but cannot decide target eligibility/capacity, queue priority, switch eligibility/time, hard locks, reward eligibility, Channel health/lifecycle, recovery target, final admission or current lease/runtime authority.

## 33. Platform/control-plane boundary

Future implementation may require separate explicitly authorized Platform/Gateway/World Registry work for recommendation, eligible-set, queue and target-bound grant issuance. This Oteryn-v2 delivery writes no Platform repository and grants no cross-repository/production authority.

## 34. DUR-03 boundary

GAME-CHANNEL owns product eligibility/multiplicity. DUR-03 retains durable item/currency/value atomicity, transaction idempotency, one semantic item location, source/sink lineage, typed custody, stale-authority rejection, ambiguous commit reconciliation and durable audit/restore anti-duplication.

GAME-CHANNEL never authorizes value creation by itself.

## 35. Downstream boundaries

- party/social business rules remain social/party owner;
- trade/market/bank/depot/mail business rules remain economy owners;
- boss/event participation/reward formulas remain event/reward owner;
- exact PvP formulas remain PvP/ruleset owner;
- house/instance topology remains owning contracts;
- `PROD-ENTITLEMENTS-01` remains unaccepted; no paid queue/switch priority is accepted.

## 36. Failure dispositions

| Condition | Required effect |
|---|---|
| stale/ineligible target | no admission; fresh offer |
| capacity-limited target | no admission; queue/alternate policy |
| draining target | no new admission |
| recovering target | same-Channel recovery for affected actor |
| revision/policy mismatch | no admission |
| hard switch lock | no voluntary switch |
| cooldown active | no voluntary switch |
| queue expiry/cancel | no gameplay/session/value effect |
| privacy-hidden co-location | no placement disclosure bypass |
| missing source multiplicity class | fail content/implementation validation |
| duplicate shared reward occurrence | owning reward/DUR reconciliation; no second value |
| Channel lifecycle reset | no shared eligibility reset |
| Channel failure | same-Channel recovery; no silent alternate |

## 37. Security invariants

Must prevent:

- client-forged Channel eligibility/capacity/queue priority;
- queue reference as bearer authority;
- silent explicit-target retarget;
- GameSession/relog reset of switch guard;
- loss of prior successful Channel across logout/restart;
- destination authority without recovery-safe guard/prior-placement update;
- client-forged maintenance exception;
- Channel label as authority;
- dual active Character across Channels;
- stale Channel owner durable write;
- switch bypass of combat/trade/item/event/instance locks;
- runtime-locality fallback to per-Channel durable output;
- per-Channel reset of shared eligibility;
- hidden rate tuning by Channel count;
- silent alternate-channel failure recovery;
- co-location privacy bypass;
- Channel lifecycle reward reset;
- GAME-CHANNEL weakening DUR-03 conservation.

## 38. Resource ceilings

Before implementation acceptance, concrete bounds must exist for applicable directory results, queue entries/bytes, per-account/Character queue requests, pending offers, co-location hints, refresh work, switch attempt state, policy size/complexity, multiplicity fan-out and pending recovery/queue references.

Numeric values are deliberately not invented here. Missing limits block implementation rather than mean unlimited.

## 39. Analytics

Measure privacy-safely: active Channel count/player distribution, recommendation override, queue wait/cancel, co-location success, switch success/rejection/cause, source/sink composition by Channel-hours/player population, reward conflicts, social fragmentation and same-Channel recovery outcomes.

Game Intelligence cannot automatically open/close Channels, change source rates, waive guards, change reward eligibility, move players or repair value.

## 40. Required implementation evidence

Architecture acceptance alone proves no runtime behavior.

Future conformance proves at least:

### Selection/queue

- recommendation remains non-authoritative;
- explicit target cannot silently retarget;
- stale/full/draining/recovering/incompatible targets fail safely;
- queue creates no GameSession/lease/value authority;
- queue admission revalidates fresh facts;
- queue duplicate/cancel/expiry is idempotent;
- priority forgery and bounded overload fail safely.

### Co-location/privacy

- party/friend hint only when visible/eligible;
- independent admissions preserve one-session rule;
- hidden placement is not leaked;
- unadmitted member gains no authority.

### Switching

- hard blockers fail closed;
- guard survives logout/new GameSession/reconnect/restart;
- first admission establishes prior Channel without counting as switch;
- same prior Channel fresh login is not switch;
- different Channel fresh login is switch even after prior GameSession ended;
- failed target leaves prior Channel/guard unchanged;
- different-Channel destination admission + prior-Channel/guard update survive crash as one semantic outcome;
- ambiguous retry cannot skip guard or duplicate session;
- same-Channel reconnect does not count;
- trusted exception is unforgeable and consequence-preserving.

### Multiplicity/reward

- every channel-sensitive value source has explicit compiled class;
- missing class fails closed;
- repeatability only when explicitly authored;
- shared eligibility does not repeat on new Channel/GameSession;
- world-unique occurrence cannot mint per Channel;
- stop/restart/new Channel/display alias cannot reset shared eligibility.

### Drain/recovery/community

- Full blocks new admission without moving existing actors;
- Draining stops new admission and never silently migrates;
- recoverable failure returns same ChannelId;
- stale owner cannot resume;
- alternate Channel only after safe state + fresh admission;
- failure does not erase combat/reward/value state;
- world-shared social/economy domains remain shared while local speech/combat/position remain Channel-local.

## 41. Decision timing

**Must decide now: YES.** Blocks player-visible multichannel selection, queue/co-location, voluntary switching, multiplicity/reward policy, PvP-safe switching, recovery UX and VSL multichannel product proof.

Late changes can force migration/rework of Gateway offers, guard/prior-placement persistence, reward keys, event definitions, presence/client UX, telemetry, support and E2E.

Supersession requires named playtest/channel-friction, economy, PvP abuse, availability/recovery, privacy/security, PERF/OPS or explicit product-strategy evidence.

## 42. Deliberately deferred

- numeric switch cooldown;
- queue limits/timeouts/priority;
- min/max public Channel count;
- capacity/autoscaling thresholds;
- orchestrator/service topology;
- exact client UI;
- complete presence visibility matrix;
- exact PvP/boss/reward/spawn/loot formulas;
- market/trade/bank/depot/mail rules;
- physical DB/control-plane schema;
- concrete ANL/protocol IDs;
- production admin exception implementation;
- Premium/VIP/commerce or paid queue priority.

## 43. Acceptance consequence

Only after exact-head self-review, required independent review, exact-head documentation/governance CI, clean threads/ownership, unchanged squash merge of #209 and separate lifecycle closeout may programme state become:

```text
GAME-CHANNEL-01
DecisionStatus       = ACCEPTED
DeliveryStatus       = LIFECYCLE_CLOSED
ImplementationStatus = NOT_STARTED
runtime/client authority = NONE
DDL/migration authority  = NONE
production authority     = NONE
```

Architecture acceptance does not authorize multichannel runtime, Gateway queue/recommendation, switch persistence, client UI, autoscaling, PvP/reward implementation or production activation.
