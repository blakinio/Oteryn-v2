# GAME-ABILITY-01 — Whole-Gate Gap Analysis

- Status: **WORKER CANDIDATE ANALYSIS / NONCANONICAL UNTIL ARCHITECTURE COORDINATOR AUDIT**
- Date: 2026-08-15
- Gate: `GAME-ABILITY-01`
- Worker issue: #260
- Worker branch: `docs/arch-b-game-ability-gap`
- Trusted worker base: `main@088b46638ac014cd7928d6b0b75cee44902fe22c`
- DecisionStatus proposed by this analysis: **`CANDIDATE`**
- ImplementationStatus: **`NOT_STARTED`**
- Runtime/client/protocol/content/DDL/Platform/production authority: **NONE**
- Merge authority: **ARCHITECTURE_COORDINATOR_ONLY**

## Executive conclusion

`GAME-ABILITY-01` does not need another redesign of targeting, cast timing, cooldowns, conditions, damage/healing or effect-family ownership. Those subjects already have binding partial baselines. The remaining whole-gate architecture gap is narrower: the partial contracts need one explicit closure envelope for **future occurrences**, **reactive/proc descendants**, **commit-group boundaries**, **continuation declaration**, **resource-bound obligations**, **client-authority separation** and **implementation/parity evidence readiness**.

The analysis therefore supports a bounded whole-gate contract candidate. That candidate can make the architecture coherent without deciding exact Reference spell values, target geometry, formula arithmetic, cooldown durations, condition values, persistence schema, protocol messages or executable content.

Architecture acceptance and mechanic parity must remain separate:

```text
whole GAME-ABILITY architecture accepted
!= any concrete Reference mechanic parity confirmed
!= executable runtime implemented
!= Alpha content complete
```

The current four registered `ABILITY_COMBAT` Reference cases remain fail-closed evidence/implementation dependencies. This worker does not promote, rewrite or own them.

## Problem

The current architecture is strong locally but still leaves several composition questions at the seams between accepted partial baselines:

1. channel pulses and condition ticks are bounded, but there is no single whole-gate statement covering delayed/periodic/future mutating occurrences generally;
2. damage/heal reactions are bounded, but the gate still needs a general deterministic proc/trigger lineage and loop-prevention rule;
3. an `Effect Plan` has an authoritative commit concept, while cross-domain effects deliberately do not create a global transaction; the whole gate needs to say how partial/ordered consequences are represented without hidden partial mutation;
4. cooldown/condition baseline deliberately defers survival across logout/recovery/migration; the gate needs a declaration boundary so implementation cannot silently choose persistence behavior;
5. multiple partial baselines require bounded work, but GAME-ABILITY-specific resource dimensions and failure obligations have not yet been collected into one implementation-readiness rule;
6. client cast bars/prediction remain non-authoritative, but the whole gate needs one explicit server/client authority statement so presentation work cannot become a second legality/commit engine;
7. Reference catalogue/manifest work and executable fixtures need a clear prerequisite ladder so architecture acceptance is not conflated with evidence or runtime parity.

Leaving these seams entirely to implementation would allow incompatible timer, proc, partial-failure, client-prediction and resource-exhaustion semantics to emerge while still claiming conformance to each individual partial baseline.

## Constraints

The closure must preserve, not reopen:

- one data-first Ability Definition model with typed bounded Effect Plans and proposal-only DUR-04 Wasm/WIT extensions;
- one authoritative Target Resolver, deterministic resolved target sets, separate legality evaluation and no hidden retargeting during effect application;
- explicit ability lifecycle, logical `PRIMARY COMMIT`, named ancillary commitment anchors, explicit reservations/compensation and bounded channel occurrences;
- typed cooldown/charge state and `ConditionDefinition != ConditionInstance`, deterministic stack/conflict transitions and condition ticks re-entering the authoritative pipeline;
- staged deterministic damage/heal composition, separate damage/heal semantics, SIM-owned RNG identity and bounded reactive descendants;
- a small typed effect-family vocabulary, domain-owned cross-domain transitions, no generic state patch and Reference catalogue metadata separate from executable content/effect vocabulary;
- FND-03 one-writer/order/generation authority and FND-04 fencing;
- accepted SIM-DETERMINISM arithmetic/RNG/order/replay/revision semantics;
- accepted DUR-04 deterministic content and capability-bounded proposal-only scripting;
- GAME-ITEM/DUR-03 conservation and idempotency for item/currency/value consequences;
- ANL-01 observational/audit authority only;
- the accepted immutable first Reference target and fail-closed evidence/parity manifest semantics;
- no new protocol family, global mutation owner, global gameplay order, process-global timer/RNG/condition registry or hidden distributed transaction.

## Evidence basis reviewed

The worker consumed the following repository truth as read-only input:

- `GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md`;
- `GAME-ABILITY-01_TARGETING_AND_LEGALITY_BOUNDARY_OWNER_BASELINE.md`;
- `GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md`;
- `GAME-ABILITY-01_COOLDOWN_CHARGE_CONDITION_OWNER_BASELINE.md`;
- `GAME-ABILITY-01_EFFECT_COMPOSITION_DAMAGE_HEAL_OWNER_BASELINE.md`;
- `GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md`;
- `GAME-ABILITY-01_REFERENCE_MECHANIC_CATALOGUE_ENTRY_PARITY_FIXTURE_CONTRACT.md` together with the later accepted Reference-manifest pin/current programme overlays that supersede its historical statement that the manifest was still candidate;
- `GAME-ABILITY-01_FIRST_REFERENCE_EVIDENCE_FIXTURE_PACKAGE.md` and manifest revision 3 as read-only evidence state;
- accepted FND-03/FND-04, GAME-CHANNEL-01, GAME-CHAR-01, GAME-ITEM-01, DUR-02/DUR-03/DUR-04, SIM-DETERMINISM-01 and ANL-01 constraints as applicable;
- `RESOURCE_LIMITS_REGISTRY.json` as the existing repository mechanism for hard implementation limits;
- `GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md`, `GLOBAL_ARCHITECTURE_DECISION_REGISTER.md` and `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` as coordinator-owned read-only status/ordering context.

No external source is used to promote Reference behavior or to claim runtime implementation.

## Reconciliation of accepted partial baselines

| Partial baseline | Binding result consumed | Whole-gate implication | Reopened? |
|---|---|---|---:|
| Typed effect pipeline | definitions are versioned data; invocation produces bounded typed proposals; only authoritative owner commits | every new closure rule must re-enter the same plan/validation/commit authority | NO |
| Targeting and legality | target discovery is deterministic, authoritative and separate from legality; no hidden effect-stage retarget | future/reaction occurrences either reuse an explicitly retained target policy or invoke the same bounded resolver at a declared anchor | NO |
| Cast/channel/commit | explicit lifecycle, logical primary commit, named ancillary anchors, no hidden rollback, channel pulses are bounded occurrences | delayed/periodic work must use the same occurrence/commit semantics; committed parents are never erased by child failure | NO |
| Cooldown/charge/condition | typed owner-local state, deterministic transitions, condition ticks re-enter pipeline, persistence survival deferred | whole gate needs only a declaration/continuation boundary, not persistence policy or schema | NO |
| Damage/heal composition | staged read-only calculation, explicit RNG anchors, bounded reactive descendants | general proc/trigger semantics can extend the same descendant model without creating an event-bus mutation engine | NO |
| Effect families/catalogue | small typed vocabulary; foreign invariants stay with owning domains; catalogue is provenance metadata | whole gate must preserve typed domain routing and refuse invented global atomicity | NO |
| Catalogue/fixture binding | parity is case/scenario scoped and revision/evidence bound | whole gate needs a readiness ladder, not a second evidence registry | NO |

## Remaining-gap classification

`ARCH-BLOCKER` below means the gap must be resolved for a coherent whole-gate architecture candidate. `IMPLEMENTATION/PARITY` means it can remain unresolved after architecture acceptance but blocks the affected executable/parity claim.

| ID | Gap | Owner | Decide now? | Whole-gate architecture | Executable/parity impact | Treatment |
|---|---|---|---:|---|---|---|
| `GA-GAP-01` | general delayed/periodic/future mutating occurrence semantics | GAME-ABILITY | YES | `ARCH-BLOCKER` | blocks timers/ticks/channels/delays | define one bounded future-occurrence envelope that re-enters the accepted pipeline |
| `GA-GAP-02` | proc/trigger/reactive ordering, lineage and cycle prevention | GAME-ABILITY + SIM ordering dependency | YES | `ARCH-BLOCKER` | blocks safe proc/reaction implementation | define deterministic post-commit descendant generation, explicit re-entry policy and bounded lineage |
| `GA-GAP-03` | plan partition, partial failure and cross-domain atomicity boundary | GAME-ABILITY + affected domain owners | YES for boundary | `ARCH-BLOCKER` | blocks multi-effect mechanics | one owner-scoped commit group is validated before its commit; sequential/partial behavior must be explicit sub-occurrences; no invented cross-domain transaction |
| `GA-GAP-04` | survival/continuation across logout, reconnect, process recovery, Channel/world transfer | GAME-ABILITY declaration + FND/GAME-CHANNEL/DUR/Character owners | YES for declaration boundary; NO for exact policies | `ARCH-BLOCKER` only if undeclared | affected mechanic blocked until policy/evidence exists | require explicit lifecycle-continuation class/policy binding; no silent default survival |
| `GA-GAP-05` | GAME-ABILITY resource limits | GAME-ABILITY semantics + implementation registry | YES for dimensions/failure rule; NO for numeric ceilings | `ARCH-BLOCKER` for obligation | implementation acceptance blocked until registered maxima/tests exist | enumerate required dimensions; exact values remain measured implementation evidence |
| `GA-GAP-06` | client prediction/presentation authority | GAME-ABILITY boundary + FND-02/ALPHA-CLIENT downstream | YES for trust boundary; NO for protocol/UX | `ARCH-BLOCKER` for authority statement | client implementation later | prediction is presentation-only; server result/commit is authority; exact messages/UI downstream |
| `GA-GAP-07` | architecture acceptance versus executable and Reference parity fixtures | GAME-ABILITY + Reference evidence + QA/runtime | YES | `ARCH-BLOCKER` | current Reference cases remain blocked | define separate invariant-fixture and Reference-parity prerequisite ladders |
| `GA-GAP-08` | exact target shapes/ranges/LoS/PvP/PZ/error precedence | ruleset/Reference policy with targeting contract | NO globally | not an architecture blocker | blocks exercised mechanics until evidenced/accepted | remain versioned per-mechanic policy; fail closed when unknown |
| `GA-GAP-09` | exact cast/cost/cooldown/charge/condition values and conflict policies | ruleset/Reference policy | NO globally | not an architecture blocker | blocks exercised mechanics | remain exact revision/evidence-bound content policy |
| `GA-GAP-10` | exact formulas, arithmetic values, RNG probabilities/order | ruleset/Reference + SIM | NO globally | not an architecture blocker | blocks affected combat parity/implementation | SIM contract supplies arithmetic/RNG envelope; formula facts stay evidence-owned |
| `GA-GAP-11` | physical content schema, serializer, Rust type graph, scheduler, Wasmtime/WIT implementation | DUR-04/tooling/runtime | NO | not an architecture blocker | implementation-specific | preserve semantic contract only |
| `GA-GAP-12` | physical persistence representation of future ability state | DUR-02 plus owning gameplay domain | NO | not an architecture blocker | required when survival policy demands durability/recovery | report as cross-domain dependency; no DDL here |
| `GA-GAP-13` | protocol result/error/prediction encoding | FND-02/protocol + client | NO | not an architecture blocker | client/server integration | only semantic authority/result requirements belong here |
| `GA-GAP-14` | AI selection/use of abilities and spawn behavior | GAME-AI-01 | NO | not an architecture blocker | AI gameplay integration | same invocation pipeline, foreign decision policy |
| `GA-GAP-15` | movement/teleport/world-object interaction effect execution | GAME-INTERACTION/world owner | NO | not an architecture blocker | affected mechanics fail closed without integration | typed proposal only; owner-domain contract required |

## Closure decision A — future occurrences

### Problem

Existing partial baselines describe channel pulses and condition ticks, but future gameplay will also require delayed hits, delayed secondary effects, timed expiries, scheduled recharge and other bounded work. Allowing each mechanic to invent a timer/callback model would reintroduce hidden mutation and replay ambiguity.

### Options

1. **One semantic future-occurrence envelope — SELECTED for candidate.** Any future mutating work is an explicit bounded occurrence/sub-occurrence with parent/provenance, exact behavior revision binding, normalized SIM time/order semantics and the same applicable target/legality/plan/commit path.
2. Private domain callbacks/timers. Rejected: hides revision, retry, ordering and mutation authority.
3. Require every future effect to be a new full client-style command. Rejected: server-origin authoritative work is already a valid invocation origin and need not masquerade as untrusted client intent.

### Required candidate invariant

A future mutating occurrence must have enough semantic state to reconstruct why it exists, which revision set governs it, when/order-wise it is eligible, which bounded occurrence index/lineage it represents and which target/revalidation policy applies. The exact Rust structure and persistence layout are deferred.

If future work survives a recovery/transfer boundary, the owning recovery/persistence contract must preserve this semantic state. If it cannot, the mechanic cannot claim survival across that boundary.

## Closure decision B — reactions, procs and loop prevention

### Problem

The damage/heal baseline already rejects hidden recursive mutation and requires bounded reactive descendants. The whole gate still needs a general rule for conditions/items/abilities that react to committed outcomes.

### Candidate model

```text
validated owner-scoped occurrence
-> COMMIT
-> typed committed result/event surface
-> deterministic reaction eligibility evaluation
-> ordered bounded descendant proposals
-> each accepted descendant becomes a new occurrence/sub-occurrence
-> applicable target/legality/effect-plan/commit pipeline
```

Pre-commit formula contributions are not post-commit reactions. A modifier that changes the current calculation must participate at an accepted typed calculation/admission stage. A proc that creates a new consequence is a descendant occurrence. This prevents a single callback mechanism from mutating both before and after commit.

Every reactive edge must have stable semantic provenance/policy identity, parent lineage and an explicit versioned re-entry/cycle rule. Undeclared re-entry is fail-closed. Ordering must be deterministic and may not depend on handler registration, hash/container iteration, pointer identity, plugin load order, worker completion or wall-clock timing.

The architecture requires hard bounds on at least reaction depth, descendant cardinality and total reaction work for one root occurrence. Exact maxima are not selected here.

Budget exhaustion cannot erase a committed parent or already committed descendants. It deterministically prevents further uncommitted descendant work, records a bounded failure/invariant result and follows the owning fail-closed policy. Valid authored mechanics must be statically/provably within accepted limits where possible; a safety limit must not be used as an undocumented balance rule.

## Closure decision C — commit groups and partial behavior

### Problem

A plan may contain several consequences. The effect-family baseline correctly refuses to invent one cross-domain database transaction. Without a clearer whole-gate rule, implementation could still apply half of one logical owner-local plan and call it a successful partial result.

### Candidate rule

Within one accepted authoritative owner/transaction scope, the candidate plan/commit group is validated as a bounded unit before that group's commit. A mechanic that intentionally resolves targets/hits/effects sequentially or permits partial success represents those semantics as explicit ordered sub-occurrences/commit groups with deterministic failure policy; it does not rely on iteration accidentally committing a prefix.

When one mechanic crosses owner domains, GAME-ABILITY may correlate and order typed proposals but cannot claim atomicity wider than the participating accepted owner contracts. If the mechanic semantically requires stronger atomicity than those contracts provide, that mechanic remains fail-closed until a separately accepted workflow/transaction contract exists.

This is a boundary decision, not a database transaction design.

## Closure decision D — continuation and persistence declaration

### Problem

`ConditionInstance`, cooldown/charge state, in-progress cast/channel state and scheduled future occurrences can affect future authoritative outcomes. The partial baselines deliberately leave logout/reconnect/restart/migration survival undecided.

### Candidate rule

Every definition/policy that can create future-authoritative ability state must explicitly bind its continuation behavior for each relevant lifecycle boundary it exercises. At minimum the semantic model must be capable of distinguishing:

- owner-local continuity while the authoritative scope remains alive;
- reconnect/same-scope recovery eligibility where an accepted recovery contract supports it;
- durable/restart survival where an accepted persistence contract supports it;
- Channel/Instance/world transfer behavior where an accepted handoff/transfer contract supports it;
- explicit non-survival/removal where that is the accepted ruleset behavior.

These are semantic capabilities, not a frozen enum. There is no implicit rule that a condition or cast survives because its remaining duration is positive, and there is no implicit rule that all such state is session-local. Missing required policy/evidence blocks that exercised continuation path.

GAME-ABILITY owns the meaning of the gameplay state; persistence/recovery/transfer owners own how an accepted surviving state is safely carried, fenced and restored.

## Closure decision E — resource-bound obligations

The architecture must require explicit hard implementation limits and boundary tests before executable acceptance for all externally or content-controlled dimensions that can grow work or allocation. At minimum GAME-ABILITY implementation planning must cover, where applicable:

- target candidate enumeration and resolved-target cardinality;
- target-query/geometry complexity and dynamic retarget depth;
- Effect Plan entry count and encoded/in-memory bounded size relevant to untrusted/content input;
- effect-composition contribution/stage count;
- multi-hit/multi-target sub-occurrence count;
- channel/periodic occurrence count and outstanding future occurrences;
- condition instance/stack cardinality and pending condition occurrences;
- reaction depth, descendants per parent/root and total root reaction work;
- cross-domain proposal count per occurrence;
- diagnostic/trace payload bounds where GAME-ABILITY can generate variable evidence;
- DUR-04 script/query/action-plan limits inherited by script-backed abilities.

Exact numeric ceilings are **not** an architecture decision here. Before implementation acceptance, required limits must be represented through the repository's accepted resource-limit mechanism with units, hard maxima, failure categories, allocation impact and boundary tests. Unknown required limits fail implementation review; they are not treated as unlimited.

Pre-commit over-limit plans fail before partial mutation. Post-commit descendant-limit exhaustion cannot roll back prior commits.

## Closure decision F — client presentation and prediction

The client may predict or present non-authoritative state such as cast progress, tentative target previews, cooldown countdowns, status/condition indicators, local animation and pending-command UX only from client-safe information.

The client never decides target legality, authoritative target membership, commit success, committed resource/cooldown/charge/condition state, final damage/healing, proc outcomes or interruption success. A client cancel/request remains intent until the authoritative owner orders and accepts it.

Server authoritative results/revisions must allow the client to correct or replace tentative presentation. Exact protocol messages, error codes, prediction algorithms, concealment policy and UI are downstream FND-02/ALPHA-CLIENT work. Server-only rules, hidden RNG or protected data are not exposed merely to make prediction exact.

## Closure decision G — executable-fixture prerequisites

Three evidence layers must remain separate:

1. **Architecture contract evidence** — paper consistency, dependency coverage, decision timing, scope and governance. This worker operates only here.
2. **Implementation invariant evidence** — once executable authority exists, synthetic/non-Reference fixtures may prove deterministic targeting/order, plan atomicity inside owner scope, retry stability, resource bounds, reaction-loop safety, failure isolation and replay. These prove implementation conformance, not Reference truth.
3. **Reference parity evidence** — a concrete Reference case additionally requires the accepted manifest/evidence rules, cleared required provenance/legal state, exact mechanic/revision binding, exact Oteryn implementation revision, passing bounded fixtures and complete declared in-scope case/aspect coverage before parity confirmation.

The current Light Healing/Ice Strike cases therefore do not block paper architecture closure, but their `UNKNOWN`/`PENDING`/`NOT_STARTED` state blocks any claim that those mechanics are implemented with confirmed Reference parity.

No catalogue entry, content definition, implementation similarity or happy-path test alone upgrades Reference evidence/parity.

## Options for the whole gate

### Option A — keep GAME-ABILITY architecture open until exact Reference mechanics are evidenced

**Rejected.** It conflates reusable engine architecture with mechanic-level evidence and would make the architecture gate depend on an effectively unbounded catalogue. It also creates pressure to guess missing Reference behavior merely to progress architecture.

### Option B — accept a reusable closure envelope while keeping mechanic values/evidence separately fail-closed

**SELECTED FOR CANDIDATE.** Freeze authority, ordering, occurrence, reaction, continuation-declaration, bounding and evidence-readiness semantics now. Keep exact mechanics versioned/evidence-owned.

This permits an owner-acceptable architecture without asserting runtime or parity.

### Option C — defer the remaining seams to implementation

**Rejected.** Timer, proc, partial-commit, client-prediction and resource-limit choices alter correctness, replay, exploit surface and recovery semantics. Deferring them would allow multiple incompatible implementations to satisfy the same paper partials.

### Option D — solve extensibility through a generic authoritative event bus/patch graph

**Rejected.** It would weaken the accepted typed effect/domain-owner boundaries, reintroduce registration-order coupling and make reactive recursion/ownership difficult to prove.

## Trade-offs

The selected closure adds semantic bookkeeping: exact revision/lineage, explicit future-occurrence policy, explicit reaction budgets, explicit continuation declarations and explicit owner routing. That is deliberate complexity at architecture boundaries rather than hidden complexity in callbacks/timers.

Benefits are stronger replayability, safer content scripting, predictable proc behavior, cleaner Studio/static validation, clearer incident evidence and less risk that item/movement/AI/persistence/client concerns leak into GAME-ABILITY.

Costs are additional validator/tooling work and more explicit content metadata. Repeated evidence that authors cannot express representative mechanics without excessive boilerplate is valid supersession evidence; it is not a reason to bypass typed authority.

## Risks and mitigations

- **Primitive/policy proliferation:** keep core effect families small; use composition/domain routing and bounded DUR-04 extension.
- **Reaction graphs become expensive:** mandatory static/runtime budgets, deterministic ordering and lineage; measure before selecting maxima.
- **Safety limits accidentally alter valid gameplay:** treat limits as implementation safety boundaries backed by content/static validation and representative tests, not hidden balance knobs.
- **Continuation metadata becomes pseudo-persistence schema:** freeze semantics only; DUR/FND owners decide physical recovery/durability.
- **Cross-domain plan looks atomic when it is not:** explicit owner-scoped commit groups and fail-closed stronger-atomicity requirement.
- **Client prediction leaks authority/secrets:** only client-safe projection, reconciliation and server-authoritative commit/result.
- **Architecture acceptance is misreported as parity/implementation:** keep DecisionStatus/ImplementationStatus/evidence axes separate and require exact fixture prerequisites.
- **Agent A changes one of the four cases before integration:** coordinator must re-read the merged Agent A evidence state before accepting this candidate if that lane changes classifications/bindings; no evidence value is copied into a new authority here.

## Player, producer and operations impact

**Player:** deterministic proc/periodic behavior, no hidden client authority and explicit recovery semantics reduce inconsistent combat outcomes and rollback-like surprises. Exact behavior still follows the active ruleset/Reference evidence rather than generic engine defaults.

**Producer/game design:** reusable typed composition, explicit continuation/reaction policies and fail-closed evidence allow new mechanics to be authored without inventing a mutation engine per spell. Static validation can expose unsupported cross-domain or unbounded mechanics before runtime.

**Operations/security:** bounded target/effect/reaction work limits DoS/proc-storm risk; explicit lineage/revision/commit evidence improves exploit and divergence investigation; no analytics or script path gains repair/mutation authority.

## Recommendation

Create and send `GAME-ABILITY-01_WHOLE_GATE_CONTRACT_CANDIDATE.md` to Architecture Coordinator audit with the closure decisions above. If the coordinator finds no contradiction with accepted partials or newly merged sibling evidence, the candidate is coherent enough for owner consideration as the whole GAME-ABILITY architecture contract.

Owner/coordinator acceptance should freeze only the semantic architecture. It should leave `ImplementationStatus = NOT_STARTED` and preserve per-mechanic evidence/implementation/parity gates.

## Future impact

If accepted, broad GAME-ABILITY implementation can be sliced without reopening core authority decisions:

```text
semantic definitions + validators
-> occurrence/target/lifecycle core
-> owner-scoped Effect Plan/commit
-> cooldown/charge/condition future-state handling
-> deterministic composition + reactions
-> bounded owner-domain adapters
-> replay/invariant fixtures
-> evidence-qualified Reference mechanics
-> client presentation/reconciliation
```

Exact slice ordering remains implementation-programme work and requires separate authority.

## Decision timing

For `GA-GAP-01` through `GA-GAP-07`, **Must decide now: YES at semantic-boundary level.**

They block a stable implementation contract because changing them later would change timer identity, proc ordering, transaction/partial-failure semantics, recovery obligations, resource failure behavior, client trust or evidence acceptance after content/runtime code already exists.

The exact numeric/gameplay/physical decisions explicitly classified `NO globally` are deliberately deferred because freezing them now would guess Reference facts, select technologies without measurement or invade another owner. They become must-decide when a concrete exercised mechanic, runtime slice or cross-domain integration needs them.

Evidence that would justify superseding the candidate includes representative mechanics that cannot be expressed safely, deterministic replay failure, owner-domain atomicity requirements not representable through explicit workflows, measured performance after semantics-preserving optimization, unacceptable Studio authoring complexity, or security/abuse evidence showing the boundary is unsafe.

## Dependency matrix

| Dependency | Current relationship | What GAME-ABILITY consumes | What remains outside this worker | Blocks whole-gate architecture? |
|---|---|---|---|---:|
| FND-03 | accepted upstream | one writer, owner order/generation, stale-work rejection | runtime scheduler/queue implementation | NO; binding constraint |
| FND-04 | accepted upstream | session/lease/fence and recovery authority | admission/reconnect implementation | NO; binding constraint |
| GAME-CHANNEL-01 | accepted adjacent | Channel/Instance locality and no implicit cross-Channel state | transfer/channel product implementation | NO; cross-boundary paths fail closed until supported |
| GAME-CHAR-01 | accepted adjacent | character-owned state/progression boundaries | exact character formula/policy implementation | NO |
| GAME-ITEM-01 + DUR-03 | accepted adjacent | item/value ownership, legality, conservation/idempotency | item transactions and physical persistence/runtime | NO; affected mechanics depend on owner adapters |
| DUR-02 | accepted durability | recovery/persistence correctness envelope | physical schema/migration/runtime | NO; required only for states declared to survive relevant boundaries |
| DUR-04 | accepted content/scripting | versioned semantic definitions; bounded proposal-only Wasm/WIT | serializer/compiler/runtime/Wasmtime/WIT physical implementation | NO; binding constraint |
| SIM-DETERMINISM-01 | accepted simulation | exact revision binding, numeric/RNG/order/time/replay semantics | exact gameplay formulas/RNG algorithm/runtime implementation | NO; binding constraint |
| ANL-01 | accepted observation | typed audit/event evidence boundary | concrete GAME-ABILITY event schema/telemetry implementation | NO |
| Reference manifest v1 rev 3 | accepted evidence registry | immutable target, evidence/implementation/parity separation | continuity/provenance research and classifications owned by Agent A/evidence process | NO for architecture; YES for affected Reference parity |
| four current ABILITY_COMBAT cases | fail-closed registered cases | demonstrate evidence binding shape only | target continuity/provenance/legal/implementation remain unresolved | NO for architecture; YES for claims on those cases |
| GAME-AI-01 | sibling/future domain | server-origin invocation uses same ability pipeline | AI selection, threat, spawn/path policy | NO; integration dependency |
| GAME-INTERACTION-01/world owner | sibling/future domain | typed domain-routed consequences only | movement/teleport/world-object semantics | NO; affected mechanics fail closed |
| FND-02 / ALPHA-CLIENT-01 | protocol/client owners | server authority/result semantics and client reconciliation requirement | wire schema, prediction algorithm, UX | NO |
| RESOURCE_LIMITS_REGISTRY | accepted implementation-governance mechanism | requires named GAME-ABILITY limits before implementation acceptance | exact measured maxima and tests | NO for paper architecture; YES for executable acceptance |

## Whole-gate owner-acceptance prerequisites proposed

The architecture candidate can be owner-acceptable when all of the following are true:

1. coordinator verifies that the candidate does not contradict or weaken any accepted partial baseline;
2. future occurrences and reactive descendants have one typed bounded authoritative model with no second mutation engine;
3. owner-scoped commit-group versus cross-domain workflow boundaries are explicit;
4. every future-authoritative ability state has an explicit continuation-policy obligation rather than an implicit persistence default;
5. resource-bound dimensions/failure semantics are mandatory, while exact maxima remain implementation evidence;
6. client prediction/presentation is explicitly non-authoritative;
7. architecture, implementation-conformance and Reference-parity evidence are explicitly separate;
8. foreign-domain gaps remain dependencies/findings, not absorbed contracts;
9. current Agent A/evidence state is re-read at integration if it has changed;
10. no runtime, DDL, protocol, production or parity claim is inferred from architecture acceptance.

Executable implementation acceptance is a later gate and additionally requires concrete limits, deterministic/replay/boundary tests, exact owner-domain integrations and separately authorized runtime work. A Reference mechanic additionally requires its own sufficient evidence and parity fixtures.

## CROSS_DOMAIN_FINDINGS

### `CROSS_DOMAIN_FINDING GA-XD-01 — persistence/recovery carrying future ability state`

If a cast/channel, cooldown, charge, condition or scheduled occurrence survives logout, GameNode recovery, restart or migration, DUR/FND owners must carry the exact behavior-affecting state/revision/fence required to continue without duplication, shortening, extension or reinterpretation. GAME-ABILITY defines the semantic payload obligation only; it does not define DDL/checkpoint/handoff mechanics.

### `CROSS_DOMAIN_FINDING GA-XD-02 — movement/world interaction consequences`

Teleport/push/pull/occupancy/tile-object consequences need GAME-INTERACTION/world-owner legality, ordering and commit semantics. GAME-ABILITY may propose only approved typed operations; affected mechanics remain fail closed if the owner integration is absent.

### `CROSS_DOMAIN_FINDING GA-XD-03 — item/value costs and consequences`

Consumables, item charges, stack changes, equipment, loot/currency and other conserved value remain GAME-ITEM/DUR-03 owned. Cost anchors in GAME-ABILITY do not grant mutation authority or cross-domain atomicity.

### `CROSS_DOMAIN_FINDING GA-XD-04 — AI-triggered use and AI state`

Creature/NPC/system ability origin may use the same invocation pipeline, but target choice strategy, threat/aggro/state and spawn/pathfinding behavior belong to GAME-AI/world domains.

### `CROSS_DOMAIN_FINDING GA-XD-05 — SIM formula/RNG realization`

GAME-ABILITY requires staged deterministic semantics but does not select exact numeric representation, formula constants, RNG algorithm/probabilities or Reference draw order. SIM/ruleset/evidence must supply those before affected execution/parity claims.

### `CROSS_DOMAIN_FINDING GA-XD-06 — client/protocol realization`

FND-02/ALPHA-CLIENT must decide wire/result/error/prediction UX while preserving server authority. No ability content or client code may invent authoritative success from local prediction.

### `CROSS_DOMAIN_FINDING GA-XD-07 — Reference continuity/provenance`

Agent A/evidence owners retain exclusive authority over current four-case continuity/provenance classifications. This candidate is intentionally insensitive to whether those cases later promote or remain unknown: it consumes the manifest contract and exact current classifications at integration, never creates its own parity truth.

### `CROSS_DOMAIN_FINDING GA-XD-08 — analytics/event schemas`

ANL-01 remains read-only. Future event-family/schema work should expose sufficient bounded lineage/revision/commit/failure evidence for audit and Game Intelligence without giving analytics mutation or gameplay-order authority.

## DECISIONS_NOT_TAKEN

This analysis deliberately does **not** decide:

- any actual Reference spell/mechanic behavior, evidence promotion or parity result;
- exact target grammar, range metric/value, geometry, LoS, floor, PvP/PZ/friendly-fire/immunity or error precedence;
- exact mana/stamina/health/item/currency costs or their per-mechanic anchor values;
- exact cast/channel time, channel cadence, cooldown group/duration, charge capacity/recharge timing;
- exact condition family catalogue, stack/refresh/replace/suppression/dispel precedence, duration or tick cadence;
- exact damage/heal formulas, armor/resistance/absorb/crit/block/dodge/proc/lifesteal values/order or RNG probabilities;
- exact reaction priority values, trigger catalogue or re-entry policy for any concrete mechanic;
- exact numeric resource limits; these require measured implementation evidence and registry entries;
- physical ability/content schema, JSON/RON/YAML/custom syntax, serializer, Rust type graph, memory layout, scheduler/timer wheel or database schema;
- exact Wasmtime/WIT host implementation beyond accepted DUR-04 capability semantics;
- survival of any concrete condition/cast/cooldown/charge across logout/reconnect/restart/Channel/world transfer;
- cross-domain movement/item/entity/AI/world APIs or a distributed transaction protocol;
- protocol message IDs/layout, client prediction algorithm, UI/animation/status presentation or error wording;
- runtime/client/server implementation, executable content population, DDL/migrations, Platform behavior, production rollout or operational capacity values;
- architecture owner acceptance, merge or lifecycle closeout.

## Worker handoff

This analysis supports the companion `GAME-ABILITY-01_WHOLE_GATE_CONTRACT_CANDIDATE.md`. Both remain worker proposals. The only lifecycle next action is Architecture Coordinator/Auditor review, including exact-head diff/CI evidence and reconciliation with any merged Agent A classification change.

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
