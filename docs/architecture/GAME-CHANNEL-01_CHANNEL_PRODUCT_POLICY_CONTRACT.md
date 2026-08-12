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

Freeze the minimum Oteryn product policy required before the accepted multichannel technical capability may become a player-visible feature.

GAME-CHANNEL owns:

- public Channel identity/presentation semantics at product boundaries;
- recommendation versus explicit player target selection;
- target-Channel queue meaning;
- party/friend co-location policy boundary;
- voluntary switch/anti-hopping semantics;
- channel multiplicity versus durable source/reward eligibility policy;
- world-global event/reward scope requirements;
- cross-channel PvP consequence rules;
- social/community fragmentation safeguards;
- player-facing drain/failure/recovery behavior;
- product-policy boundary with OPS/PERF/runtime and downstream domains.

It does not own runtime code, process orchestration, FND admission/session/lease mechanics, DUR value transaction mechanics, physical persistence, exact gameplay formulas or production rollout.

## 2. Authority chain

```text
World/Channel identity + multichannel foundation     -> FND-ID-01 + ADR-0001
ChannelRuntime/GameNode lifecycle                    -> ADR-0009 + FND-03
fresh admission / GameSession / CharacterLease       -> FND-04
minimum product/economy/party/PvP direction          -> GAME-VISION-01
Character semantics                                  -> GAME-CHAR-01
item legality                                        -> GAME-ITEM-01
item/currency/value conservation                     -> DUR-03
channel player/economy/social/PvP product policy     -> GAME-CHANNEL-01
numeric capacity                                     -> PERF-01
activation/deactivation/process orchestration        -> OPS-CHANNEL-01
exact PvP/event/reward/economy/social business rules -> owning domain gates
```

No layer may redefine another owner's semantic authority for convenience.

## 3. Canonical model

```text
WorldId
= one persistent product/economy/community/ruleset identity

ChannelRef = WorldId + ChannelId
= one persistent identity of a parallel public-world simulation

current Character Channel placement
= current GameSession/lease/runtime placement fact
!= Character identity
!= economy namespace
!= progression namespace
!= social namespace
```

Rules:

- every public Channel belongs to exactly one WorldId;
- Channels of one World consume compatible ruleset/content/map/world-policy semantics as required by accepted contracts;
- different profile/ruleset families are different WorldId values, not special Channels;
- InstanceId is not ChannelId;
- house/instance transitions cannot silently change ChannelId;
- world/Character durable state is not cloned per Channel merely because simulation is parallel.

## 4. Identity versus display

Canonical identity is `ChannelRef`.

- ChannelId is strongly typed and never inferred from `Channel 1`, `Quiet`, an array index or a UI slot;
- restart/recovery/relocation of the same semantic Channel preserves ChannelId;
- retired ChannelId is never reused for another semantic Channel;
- display label/ordinal may change without changing ChannelId;
- display alias reuse is allowed only as presentation and can never drive admission, queue, audit, switch, eligibility or reward identity;
- NodeId and ownership generation are not player Channel identity.

## 5. Directory semantics

A public Channel directory/offer is a bounded control-plane view.

It may expose, as applicable:

- canonical/opaque reference resolving exactly one ChannelRef;
- human label;
- product-facing availability class;
- queue availability;
- recommendation/co-location hints under privacy policy;
- compatibility/offer data required by existing Gateway/FND contracts.

It does not itself grant gameplay admission or reveal hidden presence, private lease/session facts, NodeId, ownership generation or security internals.

## 6. Entry modes

Accepted first-generation modes:

### `RECOMMENDED`

Control plane suggests one current eligible target.

### `EXPLICIT`

Player selects another current eligible visible target.

Recommendation is a hint; explicit target is a request. FND-04 final game authority still decides admission.

## 7. Recommendation

Recommendation may consider capacity/health, previous-channel affinity, party/friend co-location subject to privacy, maintenance/drain and demand balancing.

- exact scoring/weights are not frozen;
- client-provided load/presence is not authoritative;
- recommendation cannot bypass FND-04;
- recommendation cannot silently replace explicit target;
- recovering/fenced/internal targets are not ordinary fresh-admission recommendations;
- stale recommendation requires fresh offer.

## 8. Explicit target failure

For explicit Channel C:

```text
current eligible offer for C
-> bounded authorization for C
-> final FND-04 validation for C
```

If C becomes Full/Draining/Recovering/Unavailable/stale/incompatible:

- no admission to C;
- no silent fallback under the same grant;
- obtain a fresh directory/offer/grant for another target;
- failed choice creates no GameSession/lease/value authority.

## 9. Queue contract

A World may support an optional **bounded target-Channel pre-admission queue**.

```text
queue state
!= GameSession
!= CharacterLease
!= runtime ownership
!= durable value reservation
!= guaranteed admission
```

Rules:

- one queue target resolves one exact ChannelRef;
- queue priority/order is control-plane authoritative, never client-declared;
- queue entries/references are bounded and purpose-limited;
- queue duplicate/cancel/expiry is idempotent and produces no gameplay mutation;
- final admission revalidates current target/security/revision/account/Character/lease facts;
- short-lived FND-04 admission material is issued/refreshed only when the queued attempt is actually ready, not kept as a long-lived queue credential;
- exact storage/service/algorithm/timeout/max length/priority/rate limits remain implementation/cross-repository work;
- queue reference is never gameplay bearer authority.

For automatic entry, when another healthy eligible Channel exists, normal recommendation should prefer an available target rather than force target-specific waiting. Explicit target choice may prefer a queue.

## 10. No first-generation live-session destination queue

ADR-0001 safe switch order reaches a safe source-session boundary before destination selection/admission.

GAME-CHANNEL therefore does not authorize queueing/reserving another public Channel while the Character continues authoritative mutation in the source Channel.

Any future live-session reservation requires a separate lease/capacity/fairness/failure contract.

## 11. Party/friend co-location

- co-location is recommendation/target preference, not authority;
- every Character is independently admitted and has independent GameSession/lease;
- no all-or-nothing multi-Character admission transaction;
- no PartyId owns/reserves a Channel by itself;
- no automatic teleport/migration when another party member moves;
- target Full follows ordinary queue/alternate-choice policy;
- proximity/shared-exp/combat effects activate only with real co-location under their owners;
- exact friend/party Channel visibility remains social/privacy-owned.

Atomic group capacity reservation is deferred.

## 12. Presence/privacy boundary

- exact Character Channel placement is disclosed only through the owning presence/privacy policy;
- hidden/private/offline state cannot be inferred via co-location endpoints;
- public Channel directory does not imply public Character placement;
- party/friend relations may have bounded placement hints only when accepted by social/privacy policy;
- operational NodeId/generation/queue/security internals are never social placement fields.

## 13. Reconnect is not switch

### Same-Channel eligible reconnect/recovery

- uses FND-04 continuity;
- may preserve GameSessionId when permitted;
- keeps the same ChannelId;
- does not count as voluntary switch.

### Completed Channel switch

- uses ADR-0001 safe source exit;
- source GameSession/lease authority ends/advances as required;
- fresh destination pre-admission authorization is obtained;
- fresh FND-04 destination admission occurs;
- fresh canonical GameSessionId is created;
- destination ChannelRuntime becomes current placement.

A switch is never an in-place transport rebind or teleport.

## 14. Hard switch locks

Voluntary switch fails closed while any accepted blocker applies, including:

- combat/protected PvP;
- direct trade;
- unresolved item/currency/value transaction;
- protected boss/raid/event participation where hopping affects eligibility;
- unsafe instance/house transition;
- pending Character checkpoint/handoff/authority transition;
- stale/unavailable GameSession/lease/runtime evidence;
- destination incompatibility;
- destination Full/Draining/Recovering/Unavailable.

The client cannot override these.

## 15. Durable voluntary anti-hopping guard

Hard locks alone do not prevent repeated safe-boundary hopping.

GAME-CHANNEL requires a durable guard:

```text
scope: CharacterId + WorldId
semantic owner: GAME-CHANNEL / game-domain world channel-policy authority
interpretation: world_policy_revision
lifetime: may outlive GameSession/connection/GameNode
```

The guard is **not automatically GAME-CHAR progression state** merely because it is Character-scoped.

Physical schema/storage belongs downstream.

## 16. Switch cooldown

The first voluntary anti-hopping mechanism is **time-based cooldown + hard locks**.

- exact duration is not guessed by architecture and must be accepted from product/playtest/economy/PvP evidence before activation;
- guard survives logout, relog, fresh GameSession, reconnect and restart;
- first admission with no active prior switch guard is not itself a switch;
- same-Channel reconnect/recovery does not consume/reset guard;
- failed destination directory/queue/admission attempt does not count;
- successful destination admission is the semantic switch boundary;
- later fresh login to a different Channel obeys an unexpired guard;
- client time is not authoritative;
- policy evolution is version-aware.

An implementation cannot claim voluntary Channel switching conformance until a concrete accepted duration and trusted durable time interpretation exist.

## 17. Switch admission atomicity/recovery invariant

This outcome is invalid:

```text
new destination GameSession/placement becomes playable
AND durable ChannelSwitchGuard did not advance
```

For a voluntary switch, destination final admission must include guard evaluation/advance in the **same authoritative acceptance boundary** as destination session/placement authority, or use an equivalently proven recovery protocol satisfying all of:

1. no playable destination authority is exposed before guard advancement is durably determined;
2. destination final admission revalidates current world-scoped switch locks/guard rather than trusting old source checks;
3. ambiguous outcome reconciles the same admission/switch attempt;
4. retry cannot create a second destination authority or skip guard;
5. resulting current Channel and guard cannot disagree silently;
6. crash after durable acceptance recovers both as one semantic outcome.

Physical transaction/session persistence mechanics remain FND/DUR implementation work.

GAME-CHANNEL introduces no mandatory `ChannelSwitchId`; existing FND admission-attempt/session and ANL correlation/operation identities are reused unless later evidence proves a separate durable identity is required.

## 18. Policy evolution of guard

An incompatible world-policy change affecting active guard state selects an explicit transition rule, for example:

- preserve prior deadline;
- deterministic version-aware migration;
- new policy applies only to switches committed after activation.

Silent retroactive reinterpretation is prohibited.

## 19. Trusted non-voluntary exception

Maintenance/incident/admin-safe evacuation may later define a typed trusted exception to voluntary cooldown only if:

- server/operator authored and audited;
- client cannot request/forge it;
- source actor reaches a safe authority/value boundary;
- PvP/combat/reward eligibility is not cleared/weakened;
- DUR-03 state remains valid;
- different ChannelId still uses fresh admission;
- exception is versioned/bounded.

No generic bypass boolean exists.

## 20. Channel-local simulation versus durable value scope

Foundation locality remains unchanged:

Channel-local examples: position, creatures/spawns/AI, combat, ground runtime, local NPC, local speech.

World/Character-shared examples under their owners: Character progression/committed items, guild/world communication, market/bank/depot/economy, rankings, shared reward eligibility, provisional world house state.

Runtime locality does not by itself decide durable source/reward multiplicity.

## 21. Multiplicity invariant

Additional public Channels may increase local gameplay opportunities feeding one World economy. This must be explicit and measurable.

- no hidden inverse spawn/loot scaling by active Channel count;
- no default world-global lock around every ordinary local spawn;
- operational autoscaling cannot invent economy rules;
- value-producing source/encounter policy uses explicit classification below.

## 22. Fail-closed value-source classification

For every value-producing source/encounter family whose behavior can differ with Channel count, compiled/validated content/ruleset/event policy must explicitly select a supported multiplicity class.

**No runtime fallback class is allowed for a value-producing source.**

Missing classification blocks activation/implementation of that source under multichannel product policy.

A reviewed profile/content package may define an explicit default for a bounded source category, but the default itself is versioned authored policy, never an implicit runtime assumption.

This preserves the distinction:

```text
runtime object is Channel-local
!= durable reward/source is automatically per-Channel repeatable
```

## 23. Multiplicity classes

### `CHANNEL_LOCAL_REPEATABLE`

- independent source/simulation per Channel;
- output may repeat independently under unchanged in-Channel ruleset mechanics;
- aggregate World supply may scale with active Channel count/player demand;
- no hidden automatic division of rates by Channel count;
- exact source/loot formula remains content/Reference-owned;
- DUR-03 prevents duplicate transaction effects.

### `CHANNEL_LOCAL_SHARED_ELIGIBILITY`

- simulation can exist in multiple Channels;
- durable reward eligibility is shared at declared Character/Account/World/etc. scope;
- Channel change/new GameSession cannot reset eligibility;
- durable delivery uses owning reward + DUR-03 idempotency.

### `WORLD_SCOPED_UNIQUE`

- one semantic World occurrence/eligibility regardless of Channel count;
- event/world-service owner defines execution/presentation placement;
- ChannelRuntime copies cannot independently mint new World occurrences.

### `EXPLICIT_EVENT_POLICY_REQUIRED`

- no generic class is safe;
- high-impact boss/raid/event owner must declare its exact simulation/eligibility model before activation.

## 24. Simulation scope and eligibility scope

Any reward-bearing event where channel multiplicity matters declares at least:

```text
simulation_scope
eligibility_scope
reset/repeat policy
stable reward/source occurrence semantics
```

ChannelId is not implicitly added to a Character/Account/World eligibility reset key.

GAME-CHANNEL requires the dimensions. Event/reward owners define business rules. DUR-03 defines transaction/conservation mechanics.

## 25. Reward anti-hopping

For shared eligibility:

- new Channel cannot create another claim merely due to ChannelId;
- new GameSession cannot reset eligibility;
- queue/reconnect/failure cannot reset eligibility;
- channel-switch cooldown is not a substitute for durable reward idempotency;
- stable source/occurrence + DUR-03 mechanics prevent duplicate delivery;
- replicated simulation can increase participation only when owning event policy explicitly allows it.

## 26. Dynamic channel scaling boundary

### GAME-CHANNEL owns

- public multiplicity product semantics;
- source/reward multiplicity classification requirements;
- player/social/PvP fairness guardrails;
- versioned World channel-policy envelope.

### PERF-01 owns

- players/Channel/GameNode/World capacity numbers;
- benchmark evidence/headroom;
- latency/resource objectives.

### OPS-CHANNEL-01 owns

- activation/deactivation algorithm;
- scaling hysteresis;
- GameNode/container placement;
- health/readiness orchestration;
- recovery concurrency;
- numeric operational thresholds.

No client gameplay command directly opens/closes a public Channel.

## 27. Fresh/recovered Channel abuse prevention

- stop/recover same ChannelId cannot reset durable shared eligibility;
- new ChannelId cannot erase Character/Account/World eligibility;
- display-label reuse cannot reset eligibility;
- one-time/high-impact sources cannot use process/channel uptime alone as eligibility truth;
- OPS lifecycle is not a player reward occurrence;
- ordinary spawn initialization timing stays content/runtime-owned.

## 28. PvP implications

- direct PvP execution remains current Channel/Instance-local;
- Character/World-scoped PvP consequences survive Channel/GameSession transition;
- active combat/protected PvP blocks voluntary switch;
- Channel switching cannot clear/re-arm/reduce consequences simply via fresh GameSession;
- channel failure cannot silently relocate actor to another combat simulation;
- client disconnect claim cannot create trusted exception;
- exact PvP/skull/frag/combat formulas remain profile/parity-owned.

## 29. One World community

- guild identity/membership is not per Channel;
- market/bank/depot/rankings are not separate Channel economies;
- accepted world/guild/private communication remains cross-channel;
- local speech remains channel/spatial;
- party membership may span Channels, while co-location effects require shared simulation;
- recommendation should reduce involuntary fragmentation;
- future client UX makes current World/Channel understandable;
- Channel is not protocol/ruleset/account namespace.

## 30. Product-facing availability classes

### `SELECTABLE`

Fresh attempt may proceed subject to FND-04.

### `CAPACITY_LIMITED`

No immediate admission; target queue may be offered.

### `DRAINING`

No new ordinary admission; current actors progress to safe boundary.

### `RECOVERING`

Same ChannelId recovery path; not ordinary alternate selection for affected actor.

### `UNAVAILABLE`

Not selectable/routable.

Internal NodeId/generation/Fenced/Suspected details may map to these without being exposed verbatim.

## 31. Full/capacity-limited behavior

- existing valid sessions continue under runtime policy;
- new admission cannot bypass capacity because user selected target explicitly;
- explicit target may queue;
- recommendation may choose another eligible target;
- exact threshold remains PERF/OPS-owned;
- existing players are not silently moved/kicked merely to admit another target.

## 32. Drain behavior

- remove from ordinary selectable/recommended targets;
- stop new admission;
- current actors reach safe FND/DUR lifecycle boundary;
- future client receives bounded maintenance/drain state;
- no silent cross-channel migration;
- after safe source termination, fresh target selection/admission may occur;
- maintenance exception cannot clear combat/reward/value state.

## 33. Failure and same-Channel recovery

Default:

```text
failed Channel A
-> recover same semantic ChannelId A
-> never silently continue in Channel B
```

- ChannelId survives eligible recovery while NodeId/ownership generation may change;
- stale owner cannot regain authority;
- affected player may observe `RECOVERING`;
- if recovery cannot safely continue, actor must first reach proven safe offline/terminal authority state;
- only then may fresh selection/admission target another Channel;
- failure does not erase combat/reward/value consequences.

## 34. Channel lifecycle identity

- temporary stop/recovery/reactivation preserves semantic ChannelId;
- retirement differs from stop;
- retired ChannelId is never reused;
- display aliases are non-authoritative;
- topology authority issues/retires canonical Channel identity, not GameNode convenience.

## 35. World-policy revision

GAME-CHANNEL uses existing `world_policy_revision` for channel product policy compatibility; it does not create a new protocol major or mandatory independent channel-policy revision dimension.

- stale grants cannot silently enter under superseded policy;
- switch guard retains enough policy context for deterministic migration;
- ChannelId does not change because policy changed;
- policy storage/registry remains downstream.

## 36. Active-session policy update boundary

Later rollout must explicitly define:

- whether existing sessions remain valid to a bounded lifecycle point;
- new-switch policy after activation;
- active guard migration;
- stale queue/offer invalidation;
- whether an event/reward semantic change requires an owning content/ruleset/event revision rather than only world policy.

## 37. Cross-world boundary

Changing WorldId is not a Channel switch. It remains a separate Character/world lifecycle/transfer/admission concern. Channel selection cannot bypass world-scoped value isolation or profile boundaries.

## 38. Client authority boundary

Client may display/select/request/queue, but cannot decide:

- target eligibility/capacity;
- queue priority;
- switch guard expiry;
- hard-lock legality;
- reward eligibility;
- Channel health/lifecycle;
- recovery target;
- final admission;
- current lease/runtime authority.

## 39. Platform/control-plane boundary

Future implementation may require separate authorized Platform/Gateway/World Registry work for recommendation, eligible-set, optional queue and target-bound grant issuance.

This Oteryn-v2 architecture delivery writes no Platform repository and grants no cross-repository/production authority.

## 40. DUR-03 boundary

GAME-CHANNEL owns product **eligibility/multiplicity**. DUR-03 retains:

- durable item/currency/value atomicity;
- transaction identity/idempotency;
- one semantic item location;
- source/sink lineage;
- typed custody;
- stale-authority rejection;
- ambiguous commit reconciliation;
- durable audit/restore anti-duplication.

GAME-CHANNEL never authorizes value creation by itself.

## 41. Downstream boundaries

- party/social business rules remain social/party owner;
- trade/market/bank/depot/mail business rules remain economy owners;
- boss/event spawn/participation/reward formulas remain event/reward owner;
- exact PvP formulas remain PvP/ruleset owner;
- house/instance topology remains owning contracts;
- `PROD-ENTITLEMENTS-01` remains unaccepted; no paid queue/switch privilege is accepted.

## 42. Failure dispositions

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
| missing multiplicity class for value source | fail content/implementation validation |
| duplicate shared reward occurrence | idempotent owning reward/DUR reconciliation |
| Channel lifecycle reset | no shared eligibility reset |
| Channel failure | same-Channel recovery; no silent alternate |

Concrete protocol error IDs remain downstream.

## 43. Security invariants

A future implementation must preserve:

- no client-forged Channel eligibility/capacity/queue priority;
- no queue reference as bearer authority;
- no silent explicit-target retarget;
- no relog/reconnect/GameSession reset of switch guard;
- no destination authority without recovery-safe guard advance;
- no client-forged maintenance exception;
- no Channel label authority;
- no dual active Character across Channels;
- no stale Channel owner durable write;
- no switch bypass of combat/trade/item/event/instance locks;
- no runtime-locality fallback to per-Channel durable reward/source semantics;
- no per-Channel reset of shared eligibility;
- no hidden rate tuning by Channel count;
- no silent alternate-channel failure recovery;
- no co-location privacy bypass;
- no Channel lifecycle reward reset;
- no Channel policy weakening DUR-03 conservation.

## 44. Resource ceilings

Before implementation acceptance, bounded values must exist for applicable externally influenced structures including:

- public Channels per directory result;
- queue entries/bytes and per-account/Character requests;
- pending offers/recommendation candidates;
- co-location hints;
- directory response/refresh work;
- switch attempt/rate-control state;
- policy serialized size/complexity;
- event/reward multiplicity fan-out;
- pending queue/recovery control references.

Numeric values are deliberately not invented by this paper gate. Missing limits block implementation, never mean unlimited.

## 45. Analytics

Measure privacy-safely:

- active Channel count/player distribution;
- recommendation acceptance/override;
- queue wait/cancel;
- co-location success;
- switch success/rejections/causes;
- source/sink composition by Channel-hours/player population;
- reward conflicts;
- social fragmentation;
- same-Channel recovery success.

Game Intelligence cannot automatically open/close Channels, change source rates, waive guards, change reward eligibility, move players or repair value.

## 46. Required implementation evidence

Architecture acceptance alone proves no runtime behavior.

Future conformance proves at least:

### Selection/admission

- recommendation is only hint;
- explicit target cannot be silently retargeted;
- stale/full/draining/recovering/incompatible targets fail safely;
- client cannot select hidden/ineligible target as authority;
- stale world-policy offer/grant is rejected.

### Queue

- no GameSession/lease/value authority while queued;
- final queued admission revalidates current facts;
- duplicate/cancel/expiry idempotent;
- queue overload bounded;
- priority client-forgery rejected.

### Co-location

- party hint can influence recommendation only when visible/eligible;
- independent admissions preserve one-session rule;
- hidden presence not leaked;
- unadmitted member gains no gameplay authority.

### Switching

- all hard blockers fail closed;
- cooldown survives logout/new GameSession/reconnect/restart;
- failed target does not count;
- same-Channel reconnect does not count;
- destination admission + guard advancement survive crash as one semantic outcome;
- ambiguous admission/switch retry cannot skip guard or duplicate session;
- trusted exception unforgeable and does not clear consequences.

### Multiplicity/reward

- every value-producing channel-sensitive source has explicit compiled classification;
- missing class fails closed;
- `CHANNEL_LOCAL_REPEATABLE` repeats only when explicitly authored;
- shared eligibility does not repeat on new Channel/GameSession;
- world-unique occurrence cannot mint per Channel;
- stop/restart/new Channel/display alias cannot reset shared eligibility.

### Drain/recovery

- Full blocks new admission without moving existing actors;
- Draining stops new admission and never silently migrates;
- recoverable failure returns same ChannelId;
- stale owner cannot resume;
- alternate Channel only after safe actor state + fresh admission;
- failure does not erase combat/reward/value state.

### Community/economy evidence

- world-shared social/economy domains remain shared;
- local speech/combat/position remain Channel-local;
- channel-count source/sink effects are measurable without analytics becoming authority.

## 47. Decision timing

### Must decide now?

**YES.**

### Blocks

Player-visible multichannel selection, queue/co-location, voluntary switching/anti-hopping, multiplicity/reward policy, PvP-safe switching, drain/recovery UX and VSL multichannel product proof.

### Migration cost if changed late

Gateway offers, guard persistence, queue/control-plane contracts, reward keys/event definitions, presence/client UX, telemetry, support and E2E fixtures.

### Supersession evidence

Named playtest/channel-friction, economy, PvP abuse, availability/recovery, privacy/security, PERF/OPS or explicit product-strategy evidence.

## 48. Deliberately deferred

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

## 49. Acceptance consequence

Only after:

1. exact-head implementing-agent full-diff self-review passes;
2. required genuinely independent review has zero open material findings;
3. exact-head documentation/governance CI passes;
4. review threads/ownership conflicts are clean;
5. PR #209 squash-merges unchanged; and
6. separate lifecycle closeout promotes maintained programme status/handoff,

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
