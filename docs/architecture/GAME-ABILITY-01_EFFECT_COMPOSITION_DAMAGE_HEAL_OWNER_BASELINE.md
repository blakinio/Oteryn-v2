# GAME-ABILITY-01 — Effect Composition and Damage/Heal Owner Baseline

- Status: **OWNER-ACCEPTED PARTIAL BASELINE / GAME-ABILITY-01 REMAINS OPEN**
- Date: 2026-08-13
- Gate: `GAME-ABILITY-01`
- Scope: effect composition, damage/heal magnitude resolution, deterministic RNG and bounded reactive mechanics
- Runtime/client/protocol/DDL/Platform/production authority: **NONE**

## Decision

Damage and healing use one **typed, staged, deterministic composition framework**, while remaining distinct gameplay semantics. Calculation is read-only and produces bounded typed proposals; authoritative state changes only through the existing Effect Plan / `PRIMARY COMMIT` boundary.

```text
Typed Damage / Heal Intent
-> Base Magnitude
-> Source Contributions
-> Context / Ruleset Contributions
-> Target Contributions
-> typed mitigation / resistance / absorb as applicable
-> explicit versioned RNG decision points as applicable
-> normalized bounded final result
-> typed Effect Plan
-> authoritative validation
-> PRIMARY COMMIT
-> bounded explicit reactive descendants [optional]
```

This is a semantic framework, not one universal hard-coded formula order. A versioned formula/ruleset descriptor selects applicable stages, their exact order where behavior requires it, RNG anchors, arithmetic, rounding and clamps.

## Core boundaries

- Damage and healing are distinct typed intents/results; negative damage is not an implicit heal and negative healing is not implicit damage.
- Abilities, content and Wasm/WIT may provide bounded typed inputs/contributions but may not own an authoritative `calculate_and_mutate()` path.
- Magnitude calculation may not directly mutate HP, resources, conditions, cooldowns, items or world state.
- State-consuming absorbs/shields must express correlated consequences as typed Effect Plan entries or another already accepted typed transition; resource consumption cannot hide inside a calculator callback.
- Contribution ordering may not depend on registration order, hash iteration, pointer address, thread completion, plugin load order or unspecified database order.
- Exact numeric representation is deferred, but authoritative arithmetic/rounding/overflow/clamp/invalid handling remains subordinate to `SIM-DETERMINISM-01` formula/profile semantics.
- Crit, block, dodge, proc, variance and similar gameplay randomness use SIM-owned stable occurrence/purpose identity, purpose isolation and retry-stable evidence. Exact Reference roll order/chances remain deferred.
- Effect/damage type taxonomy is typed/versioned, not free-form strings; the exhaustive taxonomy remains deferred.

## Multi-hit and multi-target

Multi-hit and multi-target mechanics must have explicit bounded semantics. A later versioned policy states whether results use one stabilized snapshot, ordered sequential sub-occurrences, or another named bounded mode. Worker/loop scheduling may not accidentally decide whether earlier results affect later ones.

Per-hit/per-target ordering, RNG identity, caps and partial-failure semantics are deterministic when behavior-affecting. This baseline does not select one universal Reference policy for AoE, chains, beams or multi-hit abilities.

## Reactive effects

Reflect, thorns, lifesteal, on-hit/on-damage/on-heal procs and similar dependent mechanics may not recurse through hidden authoritative mutation inside the active calculator.

A dependent mechanic creates a typed **reactive descendant occurrence** (or equivalent bounded typed descendant) with stable parent lineage and re-enters the applicable targeting/legality/effect-plan/commit machinery.

Reactive processing requires deterministic ordering plus explicit depth/cardinality/work budgets and cycle/re-entry policy. Same-tick execution may be allowed by policy, but it remains a distinct semantic occurrence. Exact Reference precedence remains deferred.

## Snapshot, revision and failure discipline

One calculation consumes an explicitly defined authoritative occurrence/snapshot context. It may not opportunistically re-read changing state because another worker completed first. Intentional observation of prior committed state uses explicit sequential occurrences/sub-occurrences.

Every behavior-affecting formula/ruleset/SIM/content/script revision needed for reproduction remains bound to the logical occurrence. Retry may not silently reroll or reinterpret under a newer revision.

Invalid numeric state, missing revision, invalid RNG evidence, illegal component or reaction-budget exhaustion fails deterministically before unauthorized partial mutation. No fallback to client results, alternate formulas, direct script mutation or nondeterministic arithmetic is permitted.

After a parent effect commits, failure of a reactive descendant does not erase the parent; compensation remains an explicit later typed action/effect.

## Observability

ANL-01 stays read-only. Evidence should be able to correlate source/target, occurrence/reaction lineage, ability/mechanic/formula/ruleset/SIM revisions, effect family/type, final normalized magnitude, relevant random decisions and commit/reaction result. Deep stage traces may be test/debug/parity evidence rather than unbounded production telemetry. Security-sensitive RNG roots/seeds must not be exposed.

## Problem and constraints

Oteryn needs one combat-calculation architecture for Reference and Evolved rulesets, items, conditions, AI and future content without allowing each ability to invent formula order, random behavior or mutation timing.

Constraints: one typed Effect Plan/commit engine; separate target/legality boundary; explicit cast/commit and condition transitions; SIM deterministic numeric/RNG semantics; proposal-only bounded DUR-04 scripting; Reference-sensitive unknowns fail closed; no runtime implementation is authorized here.

## Realistic options

### A — typed staged composition — **SELECTED**

Versioned formula descriptors + typed contributions + bounded Wasm escape hatch.

Benefits: deterministic replay/parity, static validation, Studio support, analytics, consistent AI/player mechanics and safe optimization. Cost: more up-front semantic vocabulary/tooling and risk of primitive/stage proliferation.

### B — per-ability authoritative callbacks

Fast and flexible locally, but duplicates ordering/RNG/mutation semantics, weakens replay/parity/Studio validation and creates a second mutation engine. Rejected.

### C — generic modifier/event bus

Extensible, but invites registration-order coupling, recursion/proc storms and hard-to-explain results. Making it deterministic would effectively recreate option A with less explicit contracts. Rejected.

### D — closed data-only expression DSL

Highly analyzable, but exceptional mechanics force DSL growth into a hidden programming language. Existing bounded Wasm/WIT makes a strict data-only restriction unnecessary. Rejected.

## Trade-offs, risks and impact

The selected model spends more design/tooling effort before broad combat work to gain deterministic authority and long-term scalability.

Main risks: stage/primitive explosion, Reference order mismatch, numeric/rounding drift, reactive cycles, multi-target race coupling, hidden state consumption in shields and abstraction overhead. Mitigations: bounded Wasm escape hatch, per-formula versioned stage/RNG order, SIM formula descriptors/fixtures, reaction budgets, explicit snapshot-vs-sequential modes, typed companion consequences and semantic-preserving runtime fusion/precompilation.

Player impact: more consistent/fair combat outcomes, bounded proc chains and better support/debug evidence. Producer impact: reusable balancing surfaces and safer ruleset evolution, at the cost of disciplined typed authoring. Operational impact: deterministic lineage and no process-global modifier/RNG authority improve postmortem and abuse analysis.

## Decision timing

**Must decide now: YES.** Reference combat/formula fixtures, broad `GAME-ABILITY-01` combat work, AI combat integration, item/condition modifier composition and Studio authoring need one magnitude-resolution boundary.

**Downstream blocked:** Reference formula catalogue/fixtures, broad combat implementation acceptance, `GAME-AI-01` combat-result reasoning and typed item/condition combat modifiers.

**Harder later:** once content depends on custom callbacks, implicit ordering, hidden RNG draws or recursive reactions, migration requires reconstructing stages, RNG identity and lineage for every mechanic.

**Supersession evidence:** representative mechanics that cannot be expressed safely; cross-target determinism failures; measured performance after semantic-preserving optimization; Studio production evidence; security/replay findings showing a safer boundary.

**Deliberately not decided:** exact damage/heal formulas/values; exhaustive damage/effect taxonomy; physical formula DSL/serializer; exact Reference stage/RNG order; armor/resistance/absorb/crit/block/dodge/proc/lifesteal rules; multi-hit snapshot policy; reactive precedence; numeric physical representation; protocol/client UI; persistence/runtime layout.

Unresolved Reference-sensitive behavior remains fail-closed.

## Current status

```text
GAME-ABILITY-01 overall
-> REQUIRED_FOR_ALPHA / OPEN

accepted partial baselines
-> data-first typed Effect Plan + bounded Wasm proposals
-> deterministic Target Resolver + separate Legality
-> explicit cast/channel lifecycle + PRIMARY COMMIT
-> cooldown / ChargePool / Condition lifecycle
-> typed staged damage/heal composition
-> SIM-owned explicit RNG decisions
-> no mutation during magnitude calculation
-> bounded reactive descendant occurrences

next paper-only decision
-> exhaustive typed effect families and Reference combat/formula catalogue boundaries
```
