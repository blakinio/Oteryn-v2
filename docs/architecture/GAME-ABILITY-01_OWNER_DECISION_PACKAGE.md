# GAME-ABILITY-01 — Whole-Gate Owner Decision Package

- Package status: `OWNER_DECISION_REQUIRED`
- Prepared: 2026-08-16
- Trusted base: `main@d2af53855046df25b4e52edbd5ec14e0513a63ec`
- Decision target: merged `GAME-ABILITY-01_WHOLE_GATE_CONTRACT_CANDIDATE.md`
- Current gate state: `CANDIDATE / LIFECYCLE_CLOSED / NOT_STARTED`
- Coordinator recommendation: **`ACCEPT` for the explicit architecture scope defined below**
- Runtime/client/server/protocol/content/DDL/Platform/production authority: **NONE**
- Owner disposition: **NOT YET PROVIDED**

This package does not itself promote `GAME-ABILITY-01` to `ACCEPTED`. Only an explicit owner disposition followed through normal repository governance may change the canonical decision state.

## 1. Decision in one page

### Problem

The owner-accepted GAME-ABILITY partial baselines already define the core execution model, but implementation needs one binding rule at the seams between them. Without that closure, delayed work, repeated timers, reactions/procs, partial commits, continuation, resource exhaustion and client prediction could acquire incompatible implementation-local semantics while each local component still appeared to conform to an individual partial baseline.

### Verified current state

- `PROVEN` — the merged whole-gate candidate remains `CANDIDATE`; its delivery lifecycle is closed and implementation is `NOT_STARTED`.
- `PROVEN` — accepted partial baselines already bind one data-first typed Effect Plan pipeline, authoritative targeting/legality, explicit cast/channel/commit anchors, typed cooldown/charge/condition state, staged deterministic damage/heal composition and small typed effect-family/domain-routing boundaries.
- `PROVEN` — Agent A promoted `0/4` registered `ABILITY_COMBAT` cases. Target evidence remains `UNKNOWN`; source/case provenance and legal review remain `PENDING`; implementation remains `NOT_STARTED`; parity remains `PARITY_PENDING_EVIDENCE`.
- `PROVEN` — historical material review findings on the whole-gate candidate were repaired before its final merged head. The final PR #268 head `a65680d9504b3a4e6394ad3bb3dc25c6630cd098` recorded clean self-review, green exact-head repository gates and a final owner-authorized independent review with no major issue.
- `PROVEN` — current GAME-AI, GAME-INTERACTION and ALPHA-CLIENT proposal/candidate packages are merged and lifecycle-closed but remain unaccepted as whole gates.
- `DERIVED` — those newer packages preserve server authority, deterministic ordering, owner-local mutation and typed cross-domain proposal boundaries; no material semantic contradiction with the GAME-ABILITY candidate is present on the trusted base.
- `CONFLICT` — no material conflict between accepted sources was found.
- `UNKNOWN` — exact Reference values/formulas/timing, provenance clearance, concrete resource ceilings, concrete survival policies and executable foreign-domain APIs remain unresolved by design.

### Recommendation

`RECOMMENDATION — ACCEPT` the merged whole-gate candidate **only as binding architecture for its explicit semantic-closure scope**.

Acceptance should mean:

```text
GAME-ABILITY semantic architecture closed for the declared scope
!= runtime implemented
!= Alpha gameplay complete
!= Reference parity confirmed
!= foreign-domain contracts accepted
!= production authorized
```

No current unknown needs to be guessed in order to make this architecture decision. The candidate deliberately converts those unknowns into explicit implementation/parity blockers rather than architecture defaults.

## 2. Exact scope proposed for ACCEPT

Owner acceptance would bind the following clauses together with all previously accepted GAME-ABILITY partial baselines.

### A. One authoritative typed execution pipeline

`PROVEN` — every player, AI, NPC or system-origin mechanic consequence remains within the same authoritative GAME-ABILITY pipeline. Content, scripts, AI and clients may originate bounded intent/proposals only; none receives direct gameplay mutation authority.

### B. Revision-bound semantic occurrence envelope

`RECOMMENDATION` — accept the candidate requirement that delayed, repeated and reactive work remains attributable to stable parent/provenance context and exact behavior-affecting revisions. Retry/recovery may not silently reinterpret the logical occurrence using a newer incompatible revision.

### C. Owner-scoped commit groups; no invented distributed transaction

`RECOMMENDATION` — accept all-or-nothing validation before an owner-local candidate commit group. Intentional partial/sequential effects must be explicit ordered sub-occurrences. A shared Effect Plan never creates cross-domain atomicity; when stronger atomicity is required but not accepted by all owners, that executable mechanic fails closed.

### D. Future and repeated gameplay work

`RECOMMENDATION` — accept one bounded future-occurrence model for channel pulses, condition ticks, delayed hits, recharges and other future mutating work.

Every behavior-affecting repeated timer family must choose explicit FND-03-compatible catch-up semantics. In particular:

- `RUN_EACH_BOUNDED` is hard-bounded and fair;
- coalescing requires deterministic semantic equivalence;
- `SKIP_TO_LATEST` is permitted only for explicitly non-semantic maintenance/AI-think-like work where skipping cannot alter required gameplay outcomes;
- required periodic ability/combat/damage/healing occurrences cannot be silently dropped by scheduler convenience.

### E. Explicit continuation semantics

`RECOMMENDATION` — any cooldown, charge, condition, cast/channel or future state that can affect later authoritative outcomes must explicitly declare what happens at each lifecycle boundary the mechanic exercises. A remaining duration does not imply persistence; session end does not imply removal. FND/DUR/Channel/Character owners retain fencing, transfer, recovery and persistence authority.

### F. Typed deterministic reactions and proc lineage

`RECOMMENDATION` — pre-commit modifiers remain typed contributions. Post-commit reactions/procs become explicit descendants that re-enter the applicable authoritative pipeline, with deterministic ordering, stable provenance, explicit re-entry/cycle policy and hard work/depth/cardinality bounds.

### G. Resource-limit obligation without speculative numbers

`RECOMMENDATION` — implementation acceptance requires explicit hard maxima, units, failure categories, allocation impact and boundary tests for every content/external-controlled work dimension. The architecture should bind the **obligation and failure posture now**, while exact numeric ceilings remain measurement-driven implementation evidence.

Missing required limits mean the executable path is blocked, never “unlimited”.

### H. Client presentation is never ability authority

`RECOMMENDATION` — the client may predict/present cast progress, targeting previews, cooldowns, statuses and pending actions, but server state remains authoritative for admission, targets, legality, interruption, costs, cooldowns/charges/conditions, damage/healing, RNG/procs and commit results. Prediction must reconcile to authoritative revisions/results.

### I. Architecture acceptance remains separate from Reference evidence/parity

`RECOMMENDATION` — accept the candidate’s strict separation between architecture, implementation evidence and Reference parity. The current `0/4` Agent-A result remains unchanged. Catalogue presence, content similarity, source-code similarity or one passing scenario cannot promote evidence or aggregate parity.

## 3. Accepted upstream invariants that remain binding

Acceptance must preserve, not supersede:

- `PROVEN` — server-authoritative gameplay and client-intent-only trust boundary;
- `PROVEN` — native Rust / `protocol-oteryn` target architecture;
- `PROVEN` — FND-03 authoritative owner/order/generation, repeated-timer semantics and asynchronous-work boundaries;
- `PROVEN` — FND-04 fencing/recovery authority;
- `PROVEN` — SIM-DETERMINISM arithmetic, RNG identity/purpose, ordering, normalized time, revision and replay rules;
- `PROVEN` — GAME-ITEM/DUR-03 item/value conservation, idempotency and owner authority;
- `PROVEN` — DUR-04 bounded proposal-only content/Wasm capability model;
- `PROVEN` — GAME-INTERACTION and GAME-AI remain owners of their own foreign-domain semantics when/if accepted; GAME-ABILITY cannot absorb those authorities;
- `PROVEN` — ANL remains observational/read-only and cannot become mutation or gameplay-order authority;
- `PROVEN` — Reference evidence remains fail-closed and separate from implementation/parity.

Acceptance of this package must not weaken any of these invariants.

## 4. Current-status reconciliation

The merged candidate contains historical wording that described then-current sibling PRs as blocked/noncanonical proposals. Current `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` now records their newer truth:

- `GAME-AI-01` — merged/lifecycle-closed `PROPOSED`, not whole-gate accepted;
- `GAME-INTERACTION-01` — merged/lifecycle-closed `PROPOSED`, not whole-gate accepted;
- `ALPHA-CLIENT-01` — merged/lifecycle-closed `CANDIDATE`, not whole-gate accepted.

`DERIVED` — this is delivery/current-status staleness in a historical candidate, not a semantic conflict. The normative GAME-ABILITY rule remains correct: a foreign domain's unaccepted package cannot be used as canonical mutation authority, and a dependent executable mechanic remains blocked until the necessary owner contract is accepted and implemented.

If the owner chooses `ACCEPT`, the acceptance record/current overlay should consume **live current status**, not copy the historical sibling-state wording back into canonical status.

## 5. Cross-domain dependencies and blockers

These findings do not block acceptance of the GAME-ABILITY semantic envelope. They block the named executable claim when it depends on an unresolved owner surface.

| Dependency | Current architectural role | What remains blocked |
|---|---|---|
| FND-03 / DUR-02 / recovery owners | accepted authority/recovery envelope | claiming that future ability state survives recovery/restart/handoff without an owner-defined safe representation/restoration path |
| GAME-ITEM / DUR-03 | accepted conserved-value owner | item/currency/value-consuming or producing mechanics unless owner invariants and transaction semantics are satisfied |
| GAME-INTERACTION / world owner | merged proposal, not whole-gate accepted | executable teleport/push/pull/occupancy/world-object consequences that require its legality/commit surface |
| GAME-AI | merged proposal, not whole-gate accepted | authoritative AI selection, threat/aggro/spawn/path semantics; AI may not gain direct GAME-ABILITY mutation authority |
| SIM / Reference evidence | SIM accepted; Reference cases unresolved | exact formulas/RNG facts and any Reference parity claim without admissible evidence |
| FND-02 / ALPHA-CLIENT | protocol accepted; client whole-gate candidate unaccepted | exact ability result/error/prediction/reconciliation integration and UI contract |
| Reference evidence/provenance | accepted fail-closed evidence contract | promotion of any current `ABILITY_COMBAT` case or aggregate parity |
| ANL / producer registry | observational authority | claiming complete concrete ability telemetry/event-family coverage before producer registration exists |
| resource-limit registry | implementation safety mechanism | implementation acceptance until every exercised dimension has tested hard ceilings |

## 6. Security, determinism, exploitability and resource review

### Security / trust

- `PROVEN` — client, scripts, analytics and catalogue records receive no fallback mutation authority.
- `DERIVED` — accepting the trust boundary reduces the risk of client-side legality/result spoofing and script-owned privileged mutation.
- `UNKNOWN` — concrete protocol errors/prediction payloads remain downstream and must be reviewed when implemented.

### Determinism / replay

- `PROVEN` — candidate semantics require exact revision binding, deterministic target/order semantics, SIM-owned RNG purpose and explicit occurrence lineage.
- `DERIVED` — this avoids retry rerolls, “latest definition” reinterpretation and registration/hash/thread-order combat differences.

### Exploitability / resource exhaustion

- `PROVEN` — future/reaction work is bounded; budget exhaustion cannot silently remove committed history or bypass limits through recursive scheduling/direct scripts.
- `DERIVED` — these clauses directly address proc storms, missed-tick catch-up storms, unbounded target enumeration and recursive reactive amplification.
- `UNKNOWN` — exact ceilings are not yet measured; therefore implementation acceptance remains blocked until the resource registry contains the applicable limits and boundary tests.

### Cross-domain conservation

- `PROVEN` — GAME-ABILITY does not acquire item/value ownership or distributed transaction authority.
- `DERIVED` — this avoids a spell/effect engine becoming a side door around anti-duplication, idempotency or other owner invariants.

## 7. Player, producer and operational impact

### Player-visible impact

`DERIVED` benefits of acceptance:

- fairer deterministic ordering of casts, ticks and reactions;
- no scheduler-dependent loss or burst replay of required periodic gameplay effects;
- committed outcomes are not silently rewritten after later failure;
- client prediction cannot override server truth;
- unknown Reference behavior stays fail-closed instead of being guessed for convenience.

`DERIVED` cost: some mechanics remain unavailable longer when evidence, foreign-owner integration or resource ceilings are missing. That is intentional safety/product truth, not a hidden failure mode.

### Producer/content impact

`DERIVED` benefits:

- one compositional execution model for player, AI, NPC and system origins;
- explicit typed places for timing, continuation, reaction and resource policy;
- safer Studio/content validation and version migration;
- new mechanics generally compose existing effect families instead of adding bespoke mutation code.

`DERIVED` costs:

- authors/tooling must carry more explicit revision, continuation, catch-up and bound metadata;
- unusual mechanics may require a reviewed owner integration or bounded DUR-04 extension rather than a quick arbitrary callback.

### Operational impact

`DERIVED` benefits:

- replayable occurrence/reaction lineage and explicit failure disposition improve incident, exploit and balance analysis;
- fail-closed unsupported integrations make capability gaps visible;
- bounded work provides a clear basis for capacity tests and overload protection.

`UNKNOWN` — production SLOs, concrete capacity numbers and observability retention are not decided by this architecture package.

## 8. Real alternatives and trade-offs

### Option 1 — ACCEPT the explicit whole-gate semantic closure — **RECOMMENDED**

**Benefits:** removes implementation ambiguity at the high-risk seams while preserving deliberate deferrals; aligns with accepted partial baselines; enables later implementation planning without pretending parity/runtime exists.

**Costs:** requires disciplined typed metadata, explicit failure paths and resource-limit work before executable acceptance.

**Risk posture:** fail closed on unaccepted foreign integrations, unknown Reference behavior or missing limits.

### Option 2 — REWORK

Use only if the owner identifies a material semantic objection to one or more closure clauses, for example occurrence identity, timer catch-up, commit-group failure semantics, continuation, reaction lineage, resource obligations, client trust or evidence separation.

**Benefits:** avoids binding a disputed architecture rule.

**Costs:** whole-gate remains candidate and implementation should not invent a local substitute for the disputed seam.

`RECOMMENDATION` — do not select `REWORK` merely because exact mechanic values, formulas, persistence schema, resource ceilings or foreign APIs are absent; the candidate intentionally and safely defers those subjects.

### Option 3 — DEFER

Use when the owner does not want to bind the whole-gate now even though no material defect is identified.

**Benefits:** maximum near-term reversibility.

**Costs:** any broad GAME-ABILITY implementation must remain blocked or bounded to already accepted partial-baseline proofs; otherwise timer/reaction/continuation/resource/client semantics risk diverging before a common rule is accepted.

## 9. Mandatory decision-timing test

### Must decide now?

**YES** for the whole-gate seam rules listed in section 2.

### What concrete downstream work is blocked?

`DERIVED` — safe GAME-ABILITY implementation architecture, representative executable combat/condition/timer/reaction fixtures, resource-limit registration strategy, client reconciliation contract consumption and broader content authoring cannot safely assume one coherent whole-gate model until these seam semantics are binding.

### What becomes harder or impossible later?

`DERIVED` — deferring until multiple spells/conditions/procs exist risks:

- incompatible timer catch-up semantics;
- callback-specific revision/retry behavior;
- hidden partial commits or rollback assumptions;
- recursive/event-bus reaction authority;
- implicit survival/persistence behavior;
- inconsistent resource exhaustion and client prediction authority.

Normalizing those after content/runtime exists would require migration, fixture/replay reconstruction and potentially gameplay-visible compatibility work.

### What evidence would justify superseding the accepted decision later?

Concrete evidence such as:

- representative Reference/Evolved mechanics cannot be represented safely without pathological complexity or primitive proliferation;
- deterministic replay/retry evidence disproves the occurrence/revision/catch-up model;
- accepted owner workflows cannot express required cross-domain atomicity;
- measured performance remains unacceptable after semantics-preserving optimization;
- Studio/content-production evidence demonstrates unacceptable authoring complexity at scale;
- security/abuse findings show the reaction/capability/resource model is insufficient;
- a later accepted FND/SIM/DUR/domain contract materially changes an authority boundary consumed here.

### What is deliberately not decided?

See section 10. Those subjects should remain open until their own evidence or owner gate requires them.

## 10. DECISIONS_NOT_TAKEN

This package does **not** decide or authorize:

- actual Reference spell/mechanic facts, evidence classes, provenance/legal clearance or parity promotion;
- exhaustive ability/effect/condition/proc/trigger catalogues;
- exact target grammar, geometry, range, LoS, floor/PvP/PZ/friendly-fire/immunity/error precedence;
- exact target snapshot/re-resolution choices for concrete mechanics;
- exact cast/channel timing, interruption causes, costs, refunds, cooldowns, charges, condition values/ticks/stacking/dispel precedence;
- exact damage/heal formulas, arithmetic values, RNG probabilities/order, crit/block/dodge/proc/lifesteal semantics;
- the concrete catch-up policy of an unresolved mechanic or numeric timer/backlog ceilings;
- concrete reaction priorities/re-entry values or numeric resource maxima;
- survival of any concrete cast/channel/cooldown/charge/condition across logout/reconnect/recovery/restart/transfer;
- physical content/catalogue format, Rust representation, scheduler/timer wheel, task/thread model or caches;
- physical Wasmtime/WIT implementation beyond accepted DUR-04 capability semantics;
- SQL DDL, migrations, persistence representation/checkpoint format or cross-domain transaction protocol;
- GAME-AI, GAME-INTERACTION, item/value, entity/world or Character foreign-domain APIs;
- FND-02 wire fields/message IDs/error encoding or ALPHA client prediction/UI/animation design;
- ANL event schema/retention, fixture runner/test framework or runtime crate/service decomposition;
- runtime/client/server/content implementation, deployment, capacity values, SLOs, LiveOps or production authority;
- acceptance of GAME-AI, GAME-INTERACTION, ALPHA-CLIENT or analytics candidates;
- any automatic promotion of `GAME-ABILITY-01` without the owner's explicit disposition.

## 11. Consequences of the owner choice

### If `ACCEPT`

The intended canonical result is:

```yaml
GAME-ABILITY-01:
  DecisionStatus: ACCEPTED
  DeliveryStatus: lifecycle state updated through normal acceptance/closeout governance
  ImplementationStatus: NOT_STARTED
```

Only the candidate’s declared architecture scope becomes binding. The existing partial baselines remain binding; `0/4` Reference evidence remains unchanged; foreign-domain and resource/evidence blockers remain in force. A separate explicitly authorized implementation task is still required before runtime work.

### If `REWORK`

`GAME-ABILITY-01` remains `CANDIDATE / LIFECYCLE_CLOSED / NOT_STARTED`. The owner should identify the exact material clause(s) to revise; repair must remain paper-only unless separately authorized. Current accepted partial baselines stay binding.

### If `DEFER`

The gate remains `CANDIDATE / LIFECYCLE_CLOSED / NOT_STARTED`. No semantic rejection is implied, but broad implementation should not invent the unresolved whole-gate seam rules. The decision can be revisited when a named downstream proof needs it or when new evidence changes the trade-off.

## 12. Coordinator disposition

After re-reading live accepted baselines, the merged whole-gate analysis/candidate, Agent-A evidence, current programme state, historical exact-head review/CI evidence and newer sibling packages:

```text
material accepted-source conflicts: 0
open candidate review threads from PR #268: 0
Reference case promotions: 0/4
runtime implementation authority: NONE
coordinator recommendation: ACCEPT
```

The recommendation is intentionally narrower than an implementation green light. It says the semantic closure is coherent and sufficiently fail-closed to become architecture; it does not claim the project has the evidence, limits or integrations necessary to execute every mechanic.

## 13. Owner decision boundary

Exactly one owner decision is requested:

```text
OWNER DECISION REQUIRED: ACCEPT | REWORK | DEFER
```

No choice is inferred from silence, the merge of the candidate, historical reviews, or the coordinator recommendation.
