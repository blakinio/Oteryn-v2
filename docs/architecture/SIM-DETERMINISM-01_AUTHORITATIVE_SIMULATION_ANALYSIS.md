# SIM-DETERMINISM-01 — Authoritative Simulation Determinism Analysis

- Status: `PROPOSED / IN_REVIEW / NOT_STARTED`
- Date: 2026-08-13
- Gate: `SIM-DETERMINISM-01`
- Coordination ID: `OTV2-GLOBAL-ARCHITECTURE`
- Scope: paper-only architecture analysis; no runtime, combat, AI, script, DDL or production implementation is authorized.

## 1. Purpose

`SIM-DETERMINISM-01` closes the cross-domain simulation semantics deliberately left after FND-03, GAME-CHAR, GAME-ITEM, DUR-03 and DUR-04.

FND-03 already defines **who and in what owner-local order may mutate authoritative runtime state**. DUR-03 already defines **how item/currency/value conservation and durable transaction authority remain exact**. DUR-04 already defines **how authoritative scripts execute as bounded deterministic proposal components**.

SIM therefore answers a narrower question:

> Given one accepted authoritative starting state, one exact revision set and one exact normalized owner-local input sequence, what numeric, random, time/order and replay rules guarantee that the same authoritative semantic result can be reproduced and divergences can be localized?

Determinism here does **not** mean recreating live OS thread interleaving, socket wake-up order, CPU scheduling or wall-clock jitter.

## 2. Binding inputs

### FND-03 — runtime ownership/order

SIM must preserve:

- one logical authoritative mutation owner per Channel/Instance scope;
- one `RuntimeExecutionOrdinal` scoped to `(semantic runtime scope, scope ownership generation)`;
- no global runtime total order;
- per-GameSession CommandId ordering from FND-02;
- normalized commands/timers/control/handoff/service/worker/recovery inputs entering one owner resolution boundary;
- wall clock, process-local monotonic time and authoritative execution order as distinct concepts;
- no universal fixed tick requirement;
- deterministic gameplay RNG/replay evidence requirement;
- worker/service results as proposals/new normalized inputs, never direct mutation;
- stale-generation/revision rejection.

SIM refines the deterministic semantics inside and around those accepted inputs. It does not create a second scheduler or ordering counter.

### GAME-CHAR-01

Character persistence retains authoritative progression facts without freezing every formula representation. Exact XP/skill/derived-stat arithmetic and rounding remain ruleset/SIM parity work where they do not constrain identity/ownership/migration.

SIM therefore defines the **formula-semantics envelope**, not Tibia values that remain `PARITY_PENDING_EVIDENCE`.

### GAME-ITEM-01

GAME-ITEM requires deterministic modifier contribution ordering and delegates exact numeric arithmetic/rounding to SIM/ruleset owners.

SIM must not change item legality or identity semantics.

### DUR-03

DUR-03 conservation is stricter than ordinary formula arithmetic:

- exact item/asset quantities and lineage;
- bounded exact non-item value arithmetic;
- no market-price equality masquerading as conservation;
- idempotent transaction authority.

SIM may define damage, progression, chance and modifier arithmetic, but it cannot introduce approximate arithmetic into a DUR-03 exact conservation line.

### DUR-04

DUR-04 binds authoritative script determinism through:

- immutable invocation snapshot;
- logical simulation time;
- invocation-local deterministic RNG;
- stable host-query order;
- deterministic floating/NaN policy where floating is permitted;
- deterministic fuel/resource behavior under `script_execution_profile_revision`;
- proposal-only mutation.

SIM must define how script invocation identity/randomness/proposals compose with core simulation order without making the script execution profile a second core-simulation authority.

### GAME-VISION-01

Reference-sensitive arithmetic remains evidence-gated. A deterministic formula is not automatically the correct Global formula. `UNKNOWN/CONFLICT` behavior remains fail-closed until evidenced or explicitly declared different.

## 3. Determinism contract shape

The target invariant is:

```text
same authoritative starting state
+ same semantic scope/generation cut
+ same ordered normalized authoritative inputs
+ same content/ruleset/world-policy revisions
+ same SimulationDeterminismProfileRevision
+ same applicable DUR-04 script artifact/execution profiles
+ same captured external authoritative facts
=> same normalized authoritative state/result sequence
```

The invariant deliberately excludes:

- thread IDs;
- worker placement;
- host CPU count;
- OS scheduling order;
- wall-clock timestamps that are not explicit semantic inputs;
- network packet arrival timing before FND-02/FND-03 normalization;
- telemetry/log timing.

## 4. Simulation determinism profile

Introduce one versioned semantic compatibility concept:

```text
SimulationDeterminismProfileRevision
```

It is not an entity identity and not a protocol version. It identifies the cross-cutting deterministic execution semantics that can change authoritative outcomes, including:

- numeric semantic-class rules;
- default checked-overflow/invalid-value rules;
- formula rounding-stage vocabulary;
- deterministic RNG algorithm/profile identity and stream-derivation version;
- random-decision addressing/consumption rules;
- logical-time normalization rules relevant to formulas;
- deterministic tie-break/canonical-order profiles owned by SIM;
- canonical state-hash serialization/profile;
- supported-target determinism policy;
- compatibility relationship to applicable DUR-04 `script_execution_profile_revision`.

Changing one of these semantics under an unchanged profile revision is forbidden.

This profile does **not** replace `ruleset_revision`: ruleset/content own formula definitions/values and behavior policy; SIM profile owns the deterministic machinery used to execute those definitions.

## 5. Authoritative numeric semantic classes

One universal numeric type is rejected. Every authoritative numeric field/formula declares a semantic class.

### 5.1 Exact discrete class

Use exact checked integer semantics for identities/counts/ordinals/quantities and other intrinsically discrete values.

Rules:

- no implicit wrapping on overflow;
- signedness and range are explicit;
- overflow/underflow is a deterministic error unless the owning formula explicitly specifies another evidenced behavior;
- saturating or wrapping arithmetic cannot be selected as an implementation convenience.

### 5.2 Exact conservation/value class

DUR-03 exact quantities/currency/value lines remain exact and cannot be represented by binary floating point or tolerance comparison.

SIM cannot weaken this class.

### 5.3 Formula exact/fixed-scale class

Rates, percentages, coefficients and derived formulas SHOULD use project-owned integer/fixed-scale/rational semantics where the accepted behavior can be expressed exactly or with an explicit rounding boundary.

The scale/denominator is formula/profile data rather than one project-global scale.

### 5.4 Deterministic floating class

Binary floating point MAY be used in authoritative logic only when the owning formula/profile explicitly declares it and implementation evidence proves identical normalized authoritative outcomes on every supported target.

The profile must define:

- finite-input requirements;
- NaN/infinity handling;
- conversion/serialization behavior;
- rounding/canonicalization boundary;
- whether SIMD/relaxed floating features are permitted;
- cross-target fixture expectations.

A platform-dependent NaN payload, extended-precision accident, non-associative parallel reduction or tolerance-only comparison may not decide authoritative gameplay.

### 5.5 Presentation/analytics class

Approximate floating values are permitted for renderer/UI/telemetry/analytics where they cannot feed back into authoritative gameplay. Crossing back into authority requires explicit validated conversion to an authoritative numeric class.

## 6. Formula semantics descriptor

Every authoritative formula family that can affect durable/progression/combat outcome requires a versioned descriptor or equivalent generated contract containing at least:

- formula/ruleset/content revision identity;
- input semantic classes and units;
- internal numeric class;
- operation/order rules where reassociation changes result;
- named rounding points;
- rounding mode at each point;
- conversion/clamp/min/max rules;
- overflow/underflow/divide-by-zero/invalid-value disposition;
- output semantic class and unit;
- deterministic fixtures;
- Reference evidence state when the formula claims Reference behavior.

Changing arithmetic semantics requires a new compatible formula/ruleset/SIM revision rather than silently changing helper code.

## 7. Rounding discipline

“Round somewhere at the end” is not a contract.

Each formula identifies exact semantic rounding boundaries such as:

```text
input normalization
-> intermediate exact/fixed calculation
-> optional evidenced intermediate rounding
-> modifiers in explicit order
-> final evidenced rounding/conversion
-> output validation
```

Permitted rounding modes are named/versioned, not host-language defaults. Candidate vocabulary may include toward-zero, floor, ceiling, ties-to-even and explicitly evidenced custom rules.

No rounding mode is assumed to match Global until evidence proves it.

## 8. Invalid numeric state

Unless an owning evidenced rule explicitly says otherwise:

- integer overflow/underflow: reject/fail authoritative resolution before partial mutation;
- division by zero: deterministic domain failure before mutation;
- NaN/infinity in an authoritative field: invalid state, fail closed;
- conversion outside target range: fail rather than truncate/wrap;
- negative value in non-negative semantic domain: fail validation;
- impossible postcondition: invariant failure under FND-03 fail-closed handling.

Error behavior is deterministic and observable in test evidence; it must not differ between debug/release builds.

## 9. Gameplay RNG ownership

A single mutable process-global RNG stream is rejected.

Authoritative randomness belongs to a named semantic simulation/domain scope and is fenced by current runtime authority. `NodeId`, OS thread, worker identity and scheduler placement are never RNG identity.

RNG semantics distinguish:

- **security randomness** — cryptographic, nondeterministic, owned by auth/security contracts; never gameplay RNG;
- **authoritative gameplay randomness** — deterministic/replayable under SIM;
- **presentation randomness** — client/visual only and non-authoritative.

## 10. RNG stream isolation

Unrelated random consumers must not perturb each other's future authoritative sequence merely because one feature added an extra draw.

Every authoritative random decision belongs to a stable `RngPurposeKey`/equivalent semantic path such as:

```text
combat.hit
combat.damage_roll
loot.table.<stable-key>
spawn.variant
ai.choice.<stable-node>
quest.random_branch.<stable-key>
```

The exact textual syntax is not frozen, but the purpose identity is stable/versioned and cannot depend on source-code line number or container iteration order.

Two implementation models remain compatible with this semantic requirement:

1. keyed/counter-style random decisions addressed from a stable decision identity and draw index;
2. isolated stateful substreams with explicit authoritative checkpoint/replay state.

The RNG algorithm/library remains an implementation-profile choice, but its algorithm ID/parameters/stream derivation are immutable under one `SimulationDeterminismProfileRevision` and require cross-target fixtures before acceptance.

## 11. Random decision identity and retry

A random outcome must not change merely because the same logical authoritative operation was physically retried.

Random decision addressing therefore derives from stable semantic input/operation identity available to the owning domain, for example:

- `CommandRef` where the random decision is part of one player command;
- durable OperationId/TransactionId where the random decision belongs to a durable workflow;
- stable timer/event occurrence identity where a repeated/durable occurrence exists;
- parent accepted authoritative input identity plus stable purpose/effect path for owner-local internal decisions.

`RuntimeExecutionOrdinal` may be retained as order/evidence, but transient ordinal/generation changes alone must not force a different random result for the same idempotently retried semantic occurrence.

If a domain cannot establish a stable decision identity, replay evidence must record enough accepted RNG state/decision output to reproduce the original result before that path can claim deterministic retry safety.

## 12. RNG consumption is authoritative state

For stateful stream implementations, advancing RNG state is an authoritative state transition even when the gameplay resolution ultimately produces no visible mutation.

Therefore:

- rejected work before authoritative acceptance consumes no gameplay RNG;
- speculative worker computations cannot consume owner RNG state;
- an aborted/retried resolution cannot silently advance the future stream twice;
- committed stream advancement is included in checkpoint/replay state;
- random draw count/order is deterministic under one purpose stream.

Keyed/counter-style implementations satisfy the same semantics without mutable stream advancement but still require stable decision identity and draw index.

## 13. Script RNG boundary

DUR-04 scripts receive invocation-local deterministic RNG; SIM owns the upstream semantic random-decision identity/seed material used for authoritative script decisions.

Rules:

- a script never receives a mutable process-global/core-simulation RNG handle;
- script RNG derives from stable invocation/decision identity and purpose under the current SIM profile;
- `script_execution_profile_revision` defines deterministic guest-engine execution semantics;
- `SimulationDeterminismProfileRevision` defines how that invocation composes with core simulation/replay/RNG identity;
- script proposal rejection/retry cannot invisibly perturb unrelated core RNG sequences.

## 14. Logical time

SIM preserves the FND-03 distinction:

```text
wall clock
!= process-local monotonic elapsed time
!= authoritative execution order
```

There is no mandatory project-global fixed tick.

Authoritative formulas consuming time receive a **normalized semantic time value** owned by their domain, not direct system-clock access. The formula contract states unit/precision/counting semantics.

Examples:

- process-local cooldown duration may originate from monotonic time and enter simulation as a due timer input;
- durable/offline/calendar behavior consumes an explicit trusted durable/calendar fact under its owning contract;
- replay consumes the recorded/injected normalized fact, never the replayer's current clock.

Wall clock cannot become an implicit hidden formula input.

## 15. Owner-local order and simultaneous inputs

`RuntimeExecutionOrdinal` remains the authoritative owner-local input linearization evidence. SIM creates no global ordinal.

For two events that are semantically simultaneous under a domain rule, the owning contract chooses one of:

1. explicit commutative/set semantics where order cannot alter accepted result;
2. stable deterministic tie-break key;
3. FND-03 owner-assigned RuntimeExecutionOrdinal with the exact chosen order retained in replay evidence.

Domain-specific tie-breakers may use stable semantic identities/revisions, never pointer addresses, hash-map iteration, worker completion timing or OS thread order.

## 16. Cross-source arbitration

Live network/service/timer arrival order can legitimately differ across executions. Determinism begins after normalization and accepted owner-local order.

When cross-source order affects gameplay, the system must retain enough evidence to replay the order actually chosen. SIM does not require unrelated clients in separate live sessions to produce the same cross-session order on another run.

This distinction prevents a false promise of network determinism while still guaranteeing deterministic resolution of the accepted input sequence.

## 17. Worker/service completions

Auxiliary worker and service results are normalized inputs under FND-03.

Before acceptance they carry enough identity/generation/revision/input-hash evidence to reject stale results.

If several eligible results become ready concurrently and order matters, either:

- the domain defines a stable comparator/tie-break; or
- the chosen FND-03 accepted order is recorded for replay.

Worker wake-up order itself is never semantic authority.

## 18. External nondeterminism capture

Any external fact that can alter authoritative simulation must cross a typed normalization boundary before use.

Examples:

- Platform-owned entitlement fact consumed by an accepted game contract;
- current ruleset/content/world-policy activation revision;
- external/admin/operator command;
- durable service/query result that affects gameplay;
- calendar/real-world schedule fact where the game mechanic explicitly depends on it;
- feature/live-operations configuration under its owning accepted contract.

Replay records the normalized behavior-affecting value/identity/revision, not live calls to the external system.

Secrets/private credentials are not replay inputs; only the accepted derived fact relevant to gameplay is retained, subject to privacy/security policy.

## 19. Replay envelope

A deterministic replay slice requires enough evidence to reconstruct one exact semantic execution interval.

Minimum conceptual envelope:

- semantic runtime scope identity;
- ownership-generation boundaries relevant to RuntimeExecutionOrdinal interpretation;
- initial canonical checkpoint/state reference and hash;
- ordered normalized authoritative inputs and RuntimeExecutionOrdinal values;
- CommandRef/OperationId/TransactionId/timer/event/work identities as applicable;
- content/ruleset/world-policy revisions;
- `SimulationDeterminismProfileRevision`;
- applicable script artifact + WIT ABI + `script_execution_profile_revision`;
- formula profile/revisions exercised;
- authoritative RNG root/substream/decision evidence required by the selected RNG implementation model;
- normalized logical-time/calendar/external facts;
- relevant domain/state revisions;
- expected canonical state/result hashes at selected cuts.

Replay does not require original NodeId, thread IDs, CPU count or wall-clock scheduling.

## 20. Replay authority

Replay/test/investigation is **read-only evidence reconstruction**.

A replay result cannot itself:

- mutate live game state;
- repair a character/item/economy discrepancy;
- re-emit a gameplay command into production as trusted historical authority;
- bypass DUR-03 or ANL audit rules.

Any correction uses a separately authorized audited domain transaction.

## 21. Canonical state hashing

State hashes are divergence evidence, not gameplay authority.

Hash input must use canonical semantic serialization independent of:

- memory address;
- struct padding;
- Rust/ABI layout;
- hash-map/set iteration order;
- machine path;
- non-authoritative presentation/cache state.

Hash scope is hierarchical, for example:

```text
scope checkpoint
 -> domain hashes
 -> aggregate/entity component hashes
```

This supports first-divergence localization without requiring one enormous opaque world hash.

The concrete hash algorithm is versioned inside the SIM profile/evidence format and may be replaced by explicit migration; an unchanged profile cannot silently change canonicalization/hash semantics.

## 22. Hash cadence and storage

The architecture does not require production hashing after every input.

Implementation/test profiles may use:

- every-ordinal hashing in deterministic tests;
- periodic checkpoint/domain hashing in soak/replay;
- on-demand high-detail hashing after a divergence is detected.

Cadence/storage/retention are QA/ANL/PERF/resource-policy decisions. All retained replay evidence remains bounded and privacy-classified.

## 23. First-divergence procedure

A deterministic comparison reports at least:

1. first mismatching owner-local RuntimeExecutionOrdinal or checkpoint cut;
2. normalized input identity/type at that cut;
3. revision/profile set;
4. first mismatching domain hash;
5. narrower component/entity semantic path where available;
6. RNG decision/stream evidence relevant to the mismatching effect;
7. formula descriptor/rounding boundary exercised;
8. script artifact/profile if script output contributed.

This is diagnostic evidence, not an automatic repair action.

## 24. Supported-target determinism

Authoritative normalized outcomes must be identical across every **supported authoritative server target** for the same replay envelope.

Rules:

- exact discrete/conservation/fixed-scale outputs are exact;
- RNG decisions/stream results are exact under one SIM profile;
- state hashes of canonical authoritative state are exact;
- floating implementations are permitted only if the normalized authoritative result is identical across supported targets and fixtures prove it;
- renderer/presentation/analytics floating differences are outside this contract unless fed back into authority;
- a server target that cannot satisfy the current SIM profile is incompatible and must fail build/activation/readiness rather than silently diverge.

Client-side simulation/prediction does not become authoritative merely by sharing formulas. Client comparison may use protocol/reconciliation semantics rather than requiring the renderer/client platform to reproduce every server intermediate bit pattern.

## 25. Formula and ruleset compatibility

A FormulaDefinition/Ruleset revision claims compatibility with one or more SIM profile revisions.

Activation must fail if:

- a formula requires a numeric/rounding/RNG capability absent from the active SIM profile;
- an implementation changes arithmetic/RNG/order semantics without a new compatible profile/revision;
- Reference formula behavior remains `UNKNOWN/CONFLICT` for an exercised claimed-Reference path;
- supported-target fixtures for required deterministic floating behavior are missing.

A newer SIM profile does not silently reinterpret old content/rulesets during replay or migration.

## 26. Failure and recovery

On deterministic arithmetic/RNG invariant failure:

- current authoritative resolution fails before partial authoritative mutation where rollback/no-commit remains possible;
- unexpected invariant failures follow FND-03 fail-closed runtime handling rather than continuing blindly;
- durable transactions follow their owning DUR rules;
- no “best effort” clamp/wrap/random retry is invented unless the owning formula explicitly defines it;
- diagnostics include profile/revision/input identity without leaking sensitive data.

Recovery onto a new NodeId/ownership generation preserves semantic gameplay/RNG/replay state through accepted checkpoint/replay evidence; process restart must not reseed gameplay from current wall clock or entropy merely because placement changed.

## 27. Resource safety

Before implementation acceptance, resource limits must cover applicable:

- replay input/event count/bytes;
- replay interval/checkpoint size;
- RNG purpose/stream count and retained state;
- formula expression/depth/operation bounds if data-authored formulas exist;
- state-hash component count/bytes/work budget;
- divergence evidence size;
- deterministic test/replay execution budget.

Missing limits block implementation; they do not mean unlimited.

## 28. Security and abuse boundary

Deterministic gameplay RNG is not a security RNG and its internal seed/state must not be exposed to clients when prediction would enable abuse.

Deterministic replay artifacts may contain sensitive player/world/security evidence. Access, retention and export follow ANL/privacy/security policy.

Determinism must not require logging reusable credentials, secret keys or raw security randomness.

## 29. Architecture decision tests

### Must decide now? — YES

The semantic numeric/RNG/order/replay boundaries must be frozen before broad combat/AI/progression implementation. Otherwise helper/library/scheduler choices become implicit public gameplay behavior and later replay/parity migration becomes expensive.

### Concrete work blocked

- broad combat/damage/healing formula implementation;
- production creature AI decisions that consume authoritative randomness;
- exact progression/skill arithmetic delegated from GAME-CHAR;
- ruleset formula package freeze;
- deterministic replay/state-hash implementation contract;
- parity-confirmed claims for unresolved formula/rounding behavior.

### Future migration cost if wrong

A later incompatible change can require:

- versioning/migrating every affected formula/ruleset;
- preserving legacy RNG algorithms/stream derivation for replay;
- invalidating/rebuilding golden fixtures;
- changing checkpoint/replay evidence;
- replay/state-hash migration;
- retesting all supported server targets;
- reconciling durable progression results created under older arithmetic semantics;
- compatibility bridges for old content/script execution profiles.

### Superseding evidence

A later explicit contract may supersede a SIM choice with named evidence such as:

- Reference behavior proving a different rounding/numeric rule;
- cross-target divergence fixtures;
- fault/replay evidence showing current stream/order model is insufficient;
- representative performance evidence proving a deterministic profile cannot meet required budgets;
- new product requirements requiring a different deterministic simulation model;
- security evidence showing deterministic RNG exposure/derivation creates abuse risk.

A library preference or benchmark alone cannot weaken exact conservation, owner authority or replay correctness.

### Deliberately not decided

- Rust numeric/RNG/hash library;
- exact gameplay RNG algorithm;
- exact fixed-point scale per formula;
- exact combat/XP/skill/item formulas or Global values;
- global fixed tick rate;
- scheduler implementation/weights;
- worker/thread counts or CPU affinity;
- state-hash algorithm implementation until the SIM profile implementation artifact is reviewed;
- replay storage backend/retention;
- production tracing/analytics backend.

## 30. Recommendation

Accept a **profiled deterministic simulation kernel** rather than one magic numeric type, one process-global RNG or one global tick.

Core principles:

```text
FND-03 owner/order remains authority
+ formula numeric semantics are explicit/versioned
+ random decisions are purpose-isolated and replay-stable
+ external nondeterminism becomes normalized input
+ replay reproduces accepted semantic order, not OS scheduling
+ canonical hierarchical state hashes localize divergence
+ supported authoritative targets must agree on normalized outcome
+ DUR-04 script determinism nests under, not beside, core SIM semantics
```

This architecture allows Reference parity to preserve evidenced quirks through explicit formula profiles while keeping Oteryn's engine deterministic, testable and migration-safe.
