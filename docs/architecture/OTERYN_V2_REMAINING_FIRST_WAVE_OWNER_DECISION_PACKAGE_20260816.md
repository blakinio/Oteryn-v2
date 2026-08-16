# Oteryn v2 — Remaining First-Wave Owner Decision Package

- Package status: `OWNER_DECISIONS_REQUIRED`
- Date: 2026-08-16
- Coordination issue: #308
- Trusted base: `main@dfc75d1332f710d6ac85009653579f7bc51ccc59`
- Precondition satisfied: `GAME-ABILITY-01 = ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED`
- Runtime/client/server/protocol/content/DDL/Platform/production authority: **NONE**
- Executor prompt state: **HOLD**

## 1. Purpose

This package performs the coordinator re-evaluation required after GAME-ABILITY owner acceptance and asks the repository owner for one bounded disposition across the four remaining first-wave decision rows:

1. `GAME-INTERACTION-01`;
2. `ALPHA-CLIENT-01`;
3. `GAME-AI-01`;
4. paired `ANL-02` + `ANL-03`.

It does **not** infer acceptance from their merged delivery status, prior reviews, coordinator recommendation or the owner's instruction to continue architecture work. Historical candidate/proposal files remain preserved.

## 2. Verified common state

- `PROVEN` — GAME-ABILITY acceptance delivery #306 merged as `e2bb284f56f39d8fa01a843d098bcb21d17d77ac`; lifecycle closeout #307 merged as `dfc75d1332f710d6ac85009653579f7bc51ccc59`.
- `PROVEN` — Agent-A Reference evidence remains 0/4 promoted: target `UNKNOWN`, source/case/legal provenance `PENDING`, implementation `NOT_STARTED`, parity `PARITY_PENDING_EVIDENCE`.
- `PROVEN` — GAME-INTERACTION #277, GAME-AI #276, ALPHA-CLIENT #273 and ANL-02/03 #270 are merged and lifecycle-closed, but their DecisionStatus values remain `PROPOSED` or `CANDIDATE` until explicit owner disposition.
- `PROVEN` — final delivery evidence for those packages is clean: their recorded final self/independent semantic review mechanisms and repository gates passed, with no unresolved final material review thread.
- `PROVEN` — maintained current-status/register/index wording still includes pre-#306 execution text. This is coordination-status drift, not authority to undo the later accepted GAME-ABILITY baseline.
- `CONFLICT` — no material accepted-semantic conflict was found between GAME-ABILITY owner acceptance and the remaining package semantics.
- `UNKNOWN` — concrete runtime APIs/types, numeric resource ceilings, producer event schemas, several foreign-owner workflows and Reference facts remain downstream by design.

## 3. Recommended decision order

```text
1. GAME-INTERACTION-01
2. ALPHA-CLIENT-01
3. GAME-AI-01
4. ANL-02 + ANL-03
```

`RECOMMENDATION` — use this order for serial canonicalization, but allow one bundled owner response now. The order determines how acceptance baselines and final coordination state are recorded; it does not grant executable authority.

Why this order:

- GAME-INTERACTION defines retry/idempotency/reconciliation identity across owner boundaries and is a named dependency for GAME-AI environment/route interaction;
- ALPHA-CLIENT blocks early real-boundary vertical-slice client composition and authority/projection/testing without depending on concrete AI/analytics runtime;
- GAME-AI can then consume accepted GAME-ABILITY + GAME-INTERACTION boundaries while keeping its concrete representation deliberately unfrozen;
- ANL-02/03 are read-only consumers; accepting them last keeps analytical attribution explicitly downstream of the gameplay owners while producer event registration remains a later implementation task.

## 4. GAME-INTERACTION-01 owner decision

### Current state

```yaml
DecisionStatus: PROPOSED
DeliveryStatus: LIFECYCLE_CLOSED
ImplementationStatus: NOT_STARTED
Delivery: PR #277 / merge c8d8ae20471acf004db7bbf6015a2d1b710aa8af
Final reviewed head: 2a13f789bb988a7e8eeca1c387173960708d506a
```

### What the package binds

`PROVEN` from the merged successor candidate:

- stable recursive semantic child occurrence identity rooted in an authoritative source occurrence and exact semantic revision context;
- deterministic canonical child ordering and retry-stable RNG identity;
- at-most-once authoritative child commit with explicit `PENDING / COMMITTED / REJECTED` outcome semantics;
- timeout/cancellation/stale-completion rules that do not invent rollback or duplicate a possibly committed foreign operation;
- `PENDING` forbids a blind fresh semantic attempt/CommandRef for the same intent;
- named accepted workflow contracts are required for multi-owner operations where partial success matters;
- foreign owners retain their own mutation/commit/reconciliation authority;
- bounded public failure mapping must not expose raw infrastructure failures as semantic API.

### Effect of GAME-ABILITY acceptance

The candidate contains historical delivery-time wording saying GAME-ABILITY PR #268 was noncanonical/unmerged and therefore blocked effect integration. That status wording is now stale.

`DERIVED` — the semantic boundary is now satisfied at architecture level: GAME-INTERACTION may correlate/delegate to an accepted GAME-ABILITY occurrence/effect owner but does not acquire formula, legality, damage/heal or effect-commit authority. This removes the historical GAME-ABILITY **architecture** blocker without inventing a physical API.

### Remaining non-acceptance blockers

These do **not** require rejection of the interaction identity/retry architecture, but still block affected executable mechanics:

- movement/relocation/handoff owner contract remains unresolved for mechanics that need it;
- durable writable-text owner remains unresolved;
- client-visible interaction payload/error registration remains FND-02-owned future work;
- concrete cascade/retry/resource maxima require resource/performance evidence;
- named coupled workflows must exist before implementing multi-owner partial-success mechanics.

### Mandatory decision timing

- Must decide now? **YES**.
- Concrete downstream blocked: safe world-interaction implementation, retry-safe trigger/effect delegation, AI environment-trigger interaction and interaction-aware vertical-slice work.
- Harder later: child identity and retry rules become persisted/networked/runtime conventions; changing them after content exists risks duplicate effects/value and replay instability.
- Superseding evidence: representative mechanics cannot express safe identity/reconciliation without pathological complexity; accepted foreign owner protocols require a stronger equivalent workflow model; deterministic replay/failover evidence disproves the current identity model.
- Deliberately not decided: physical Rust types, storage, wire IDs, movement/handoff owner, writable-text owner, numeric limits.

### Recommendation

**`ACCEPT`** the merged successor semantic architecture, preserving all remaining implementation blockers.

Owner choice: `ACCEPT | REWORK | DEFER`.

## 5. ALPHA-CLIENT-01 owner decision

### Current state

```yaml
DecisionStatus: CANDIDATE
DeliveryStatus: LIFECYCLE_CLOSED
ImplementationStatus: NOT_STARTED
Delivery: PR #273 / merge b7f239a32081fc43f5d3306517eadde850b5be6b
Final head: fe85600806979812f63dfb7b2c2a7e85cfecc943
```

### What the package binds

`PROVEN` from the merged candidate:

- `apps/client` is the production composition root unless a real process/security/deployment boundary is later accepted;
- hard separation of Platform Identity/directory, one-time login ticket, Platform Game Gateway pre-admission routing, FND-02 gameplay transport and final FND-04 game-owned session/lease authority;
- runtime capabilities are exposed only when implementation evidence exists; architecture names do not make TCP/QUIC/gameplay entry usable;
- local session state and world projection remain non-authoritative observations;
- protocol ingress is generation/sequence/revision/snapshot fenced; egress accepts semantic player intent rather than raw UI/input callbacks;
- scene/camera/animation/effects/audio are presentation-only, reconstructable and bounded;
- client-safe content is revision/compatibility governed and authoring-only/server-only state cannot leak into shipping projection;
- client/Studio sharing is limited to representation-neutral non-authoritative low-level components;
- durable settings have explicit ACCOUNT/OS_USER/INSTALLATION/DEVICE scopes, deterministic precedence and privacy-fail-closed override semantics;
- crash diagnostics remain optional/privacy-bounded and non-authoritative;
- release activation is verified/atomic/outside active authority-bearing gameplay mutation;
- ADR-0007 Tier 1/2/3 evidence remains distinct and FND-02 requires an independent wire oracle in addition to shared production codec E2E.

### Effect of GAME-ABILITY acceptance

`DERIVED` — no material client architecture contradiction exists. GAME-ABILITY strengthens, rather than changes, the candidate's rule that prediction/presentation cannot become legality, combat/RNG/effect or result authority.

### Remaining implementation blockers

- gameplay transport/client protocol implementation is absent;
- server counterpart/admission integration is absent;
- exact FND-02 gameplay messages and capability registry integration remain implementation work;
- client-safe content and scene/audio providers need concrete implementation + limits;
- Tier 1/Tier 2/Tier 3 evidence is not yet produced for native gameplay;
- concrete UI/renderer/network/updater/audio libraries remain deliberately unfrozen;
- external-alpha release/security/SRE/privacy package remains downstream.

### Mandatory decision timing

- Must decide now? **YES** for ownership/composition/projection/content/settings/update/test boundaries; **NO** for concrete libraries/frameworks.
- Concrete downstream blocked: native gameplay client vertical slice, safe protocol reducer, scene/render/audio composition, client-safe content activation and real-boundary E2E design.
- Harder later: direct UI-to-network coupling, duplicate client world authority, Studio/client type entanglement and nondeterministic user/privacy state scope become expensive to unwind.
- Superseding evidence: a later client/protocol/content design proves equivalent or stronger one-way authority, reconstruction, privacy and real-boundary evidence with lower complexity.
- Deliberately not decided: concrete frameworks, prediction algorithm, transport activation, exact wire/API types, packaging/updater vendor, cross-platform roadmap.

### Recommendation

**`ACCEPT`** the merged client architecture baseline; keep runtime readiness explicitly false until separately proven.

Owner choice: `ACCEPT | REWORK | DEFER`.

## 6. GAME-AI-01 owner decision

### Current state

```yaml
DecisionStatus: PROPOSED
DeliveryStatus: LIFECYCLE_CLOSED
ImplementationStatus: NOT_STARTED
Delivery: PR #276 / merge f1bd64a62b9392223589e6b0609149570f5a76b5
Final reviewed head: 200267c946e0c78b15ce0d17c82454622d036abc
```

### What the package binds

`PROVEN` from the merged successor candidate:

- current authoritative runtime owner retains local AI/spawn mutation authority;
- AI representation is deliberately representation-neutral: concrete FSM/behavior-tree/planner technology is **not** frozen;
- each authoritative AI semantic resolution is bounded, deterministic and staged/preflighted before one AI-local authoritative commit;
- perception/target selection and tie-breaks are deterministic and bounded;
- pathfinding/planning is auxiliary proposal work and must be revalidated by the current owner before mutation;
- spawn retries have finite count/window/deadline/cadence/order with stable occurrence provenance;
- scripts/content remain proposal-only under DUR-04;
- controlled actors preserve principal/control provenance and stale-control rejection;
- AI has no item/currency/loot/XP value authority;
- concrete resource hard maxima are mandatory before executable acceptance;
- Reference unknowns remain fail closed.

### Effect of GAME-ABILITY and recommended GAME-INTERACTION acceptance

`DERIVED` — accepted GAME-ABILITY supplies the binding combat/effect owner boundary required by `GAME-AI-XD-01`: AI chooses/proposes intent; it does not perform authoritative ability mutation.

`RECOMMENDATION` — record GAME-INTERACTION acceptance first. That supplies the stable child/retry/reconciliation semantics consumed by dynamic environment/interaction consequences and keeps AI from inventing a second retry authority.

### Remaining implementation blockers

- exact typed AI-intent/result API is not frozen as a physical contract;
- dynamic route/environment integration must consume accepted interaction/world owner semantics;
- controlled-actor reward attribution + one-occurrence settlement/dedup must consume GAME-ITEM/DUR/reward owners;
- concrete resource ceilings/boundary tests remain required;
- world-shared multi-actor event/encounter occurrence/eligibility owner remains a separate domain dependency;
- concrete AI/pathfinding frameworks and algorithms require implementation evidence.

### Mandatory decision timing

- Must decide now? **YES** for authority/determinism/bounded-resolution/spawn-provenance semantics; **NO** for concrete AI representation/library.
- Concrete downstream blocked: creature/spawn implementation, deterministic combat-intent integration, safe failover/replay and bounded path/perception work.
- Harder later: framework-specific mutable callbacks, unbounded retries and AI-owned effect/value mutations become de facto public contracts/content assumptions.
- Superseding evidence: representative AI/content cannot express safely under the semantic envelope; measured performance proves the representation-neutral envelope itself prevents required scale; accepted gameplay contracts materially change ownership.
- Deliberately not decided: FSM/BT/planner/pathfinding library, numeric limits, exact API structs, concrete encounter system.

### Recommendation

**`ACCEPT`** the merged successor semantic architecture after GAME-INTERACTION is recorded first.

Owner choice: `ACCEPT | REWORK | DEFER`.

## 7. ANL-02 + ANL-03 paired owner decision

### Current state

```yaml
ANL-02:
  DecisionStatus: CANDIDATE
  DeliveryStatus: LIFECYCLE_CLOSED
  ImplementationStatus: NOT_STARTED
ANL-03:
  DecisionStatus: CANDIDATE
  DeliveryStatus: LIFECYCLE_CLOSED
  ImplementationStatus: NOT_STARTED
Delivery: PR #270 / merge 32ff2ae75530cb9334463833462eb02c44dc435b
Final head: e78cb7ff5151876643206324cf7e6d2ca8cde8da
```

### ANL-02 binding scope

- metric identity/revision and explicit cohort/denominator/window/source/revision lineage;
- deterministic analytical session/hunt grouping without creating FND gameplay-session authority;
- deterministic UTC half-open reporting windows based on accepted event occurrence time, not arrival/query time;
- explicit multidimensional evidence quality;
- no hidden zero for missing/unknown/suppressed data;
- material dashboard warnings for partial/unknown/mixed/reconciliation/privacy states;
- versioned regression disposition separate from visualization;
- fail-closed rule: attempted material regression evaluation with any unsatisfied applicable quality/sample/comparability/reconciliation/privacy/provenance prerequisite results in `REGRESSION_EVIDENCE_INSUFFICIENT`, never green acceptance;
- read-only SIM corroboration and privacy/resource limits.

### ANL-03 binding scope

- read-only economy/integrity/security evidence only; never gameplay/DB mutation, sanction, confiscation, rollback or deployment authority;
- deterministic invariant catalogue over complete authoritative evidence for item/value integrity;
- detector/signal identity and source-quality provenance;
- immutable signal/case/reviewer lifecycle;
- no-case triage still requires an auditable substantive disposition;
- referral is routing only after a substantive evidentiary disposition;
- `SUPPORTED_SECURITY_FINDING` remains non-sanctioning and does not convert statistical evidence into deterministic proof;
- optional client diagnostics opt-out/absence is non-adverse and cannot increase suspicion/risk/enforcement priority;
- least-privilege read-only investigation credentials and bounded detector/query/evidence work.

### Effect of upstream gameplay acceptance

`DERIVED` — GAME-ABILITY acceptance makes one attribution owner explicit and reduces ambiguity, but analytics still must consume producer-owned typed event semantics rather than infer them. Accepting analytics does not require those events to exist now because the candidates explicitly fail closed when producer coverage is absent.

### Remaining implementation blockers

- `GAME_EVENT_FOUNDATION_REGISTRY.json` lacks concrete producer event families required for real metric/detector coverage;
- gameplay/content/ability/AI/interaction/quest/event producer owners must register typed events and attribution semantics;
- DUR/FND/security producer coverage is missing for complete integrity/security detectors;
- exact thresholds, minimum samples, retention/suppression values, resource ceilings and late-data horizons remain owner/evidence driven;
- warehouse/broker/dashboard/detector/case-management technology is deliberately unfrozen;
- enforcement/GM/account-remediation contract remains a foreign owner and is not created by ANL-03.

### Mandatory decision timing

- Must decide now? **YES** for read-only authority/evidence-quality/privacy/regression/invariant/human-disposition semantics; **NO** for technology/thresholds/concrete event IDs until producers exist.
- Concrete downstream blocked: trustworthy Game Intelligence/analytics implementation and producer event-contract design that knows what evidence consumers require.
- Harder later: dashboards can normalize incomplete data as truth, detector scores can become de facto sanction authority and producer schemas can omit irrecoverable provenance.
- Superseding evidence: production analytics evidence shows unusable operational cost/authoring burden or a stronger accepted data-governance model preserves the same non-authority/privacy/evidence properties.
- Deliberately not decided: concrete producer events, storage/stream/dashboard vendors, algorithms, thresholds, enforcement policy.

### Recommendation

**`ACCEPT` both ANL-02 and ANL-03 together** as read-only architecture, preserving all producer/evidence/runtime blockers.

Owner choice: `ACCEPT | REWORK | DEFER` for the pair. If the owner wishes to split them, that is a material alternative and should be stated explicitly.

## 8. Player / producer / operations review

### Player impact

`DERIVED` — accepting these boundaries improves fairness and trust by making retries exactly-once/reconcilable, keeping client/AI non-authoritative, and preventing analytics or detector confidence from silently becoming gameplay/sanction authority. The cost is deliberate fail-closed behavior where owner contracts/evidence are absent.

### Producer/developer impact

`DERIVED` — the contracts increase explicit metadata and boundary work: semantic revisions, child/provenance identity, event-quality lineage and resource limits. In exchange they prevent bespoke callback semantics from becoming irreversible hidden APIs and preserve freedom to choose concrete frameworks later.

### Operations/security impact

`DERIVED` — bounded work, explicit stale/retry semantics, immutable evidence and separation of gameplay vs analytics/enforcement reduce incident ambiguity. Concrete SLO/capacity/retention values remain measurement-driven and are not smuggled into architecture.

## 9. Decisions deliberately not taken

This package does not decide or authorize:

- Reference mechanic facts/parity/provenance promotion;
- exact movement/handoff or writable-text owner APIs;
- exact AI representation/pathfinding library;
- concrete client UI/render/network/audio/updater libraries;
- physical protocol message IDs/types or SQL schemas;
- producer event IDs/payload schemas;
- analytics/detector/storage/dashboard technology;
- GM/enforcement/account remediation policy;
- numeric resource ceilings, statistical thresholds or product tuning values;
- Premium/VIP entitlement consumer semantics/activation;
- runtime implementation, deployment or production traffic.

## 10. PROD-ENTITLEMENTS-01 boundary

The Platform producer prerequisite is proven, but the Oteryn-v2 consumer/enforcement contract remains unaccepted under issue #115.

Decision timing:

```text
unrelated foundation / VSL work -> DEFERRED, does not block
Premium/VIP or game-consumed entitlement executor -> MUST DECIDE FIRST
```

Therefore a final implementation prompt handoff must not include/green-light an entitlement executor until `PROD-ENTITLEMENTS-01` has its own accepted consumer contract and security/rollout evidence plan.

## 11. Consequences of owner choices

For each `ACCEPT`:

```text
DecisionStatus -> ACCEPTED
ImplementationStatus -> NOT_STARTED
```

The later owner-acceptance record binds only the declared semantic scope, preserves historical candidates and does not grant implementation authority.

For each `REWORK`, the owner should identify the material clause(s); the current decision status remains proposal/candidate and downstream implementation may not invent a substitute.

For each `DEFER`, no semantic rejection is implied; implementation that depends on the unaccepted whole-gate semantics remains blocked or restricted to already accepted narrower baselines.

## 12. Executor readiness gate

The coordinator MUST NOT tell the owner to run executor prompts until:

- explicit dispositions for all four owner-decision rows are durably applied;
- acceptance/rework lifecycles are closed;
- `FOUNDATION_PROGRAMME_CURRENT_STATUS.md`, `GLOBAL_ARCHITECTURE_DECISION_REGISTER.md`, architecture `README.md` and the non-owning foundation checkpoint agree with final state;
- stale prompt PR #305 is closed/superseded/rebuilt from current main;
- the final prompt set is audited for exact current prerequisites and per-lane implementation authority;
- unresolved architecture blockers are reflected as lane-specific exclusions rather than silently ignored.

Until then:

```text
EXECUTOR_PROMPTS: HOLD
```

## 13. Owner decision boundary

After this package is exact-head validated and merged, one bundled owner response is required:

```text
GAME-INTERACTION-01: ACCEPT | REWORK | DEFER
ALPHA-CLIENT-01:     ACCEPT | REWORK | DEFER
GAME-AI-01:          ACCEPT | REWORK | DEFER
ANL-02 + ANL-03:     ACCEPT | REWORK | DEFER
```

Coordinator recommendation:

```text
GAME-INTERACTION-01: ACCEPT
ALPHA-CLIENT-01:     ACCEPT
GAME-AI-01:          ACCEPT
ANL-02 + ANL-03:     ACCEPT
```

No owner choice is inferred from silence, continued work, previous merge approval or this recommendation.

`IMPLEMENTATION_AUTHORITY: NONE`
