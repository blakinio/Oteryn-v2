# Oteryn v2 Global Architecture Decision Register

- Status: **Active coordination register**
- Date: 2026-08-17
- Coordination ID: `OTV2-GLOBAL-ARCHITECTURE`
- Current execution status: `docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md`
- Detailed gameplay/product horizon: `docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md`
- Stable foundation backlog: `docs/architecture/FOUNDATION_DECISION_BACKLOG.md`
- Architecture coordinator prompt: `docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md`
- Released implementation programme: `docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md`
- Released implementation coordinator: `docs/agents/prompts/OTV2_IMPLEMENTATION_COORDINATOR.md`

## 1. Purpose and precedence

This register preserves stable architecture gate IDs, their current decision role and the boundary between accepted architecture and later implementation/proof work.

Use with `ARCHITECTURE_STATUS_MODEL.md`:

```text
DecisionStatus != DeliveryStatus != ImplementationStatus
```

Accepted ADRs/contracts/owner baselines are semantic authority. `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` is current execution-status authority. Historical proposal/candidate and backlog prose remains evidence/history when superseded by a later owner acceptance.

Release of the implementation coordinator programme does not change any gate's `ImplementationStatus` and does not authorize production.

## 2. Accepted platform/foundation direction

The following architecture is accepted for its named scope:

| Gate / domain | DecisionStatus | ImplementationStatus | Canonical source / note |
|---|---|---|---|
| Native Rust client/server + project `protocol-oteryn` | `ACCEPTED` | mixed / gated | ADR-0001 |
| Repository ownership / client migration | `ACCEPTED` | `PROVEN` cutover | ADR-0002 + FND-01/VSL-02 |
| Platform Identity / Game Gateway / final game admission split | `ACCEPTED` | `NOT_STARTED` game runtime | ADR-0003 + FND-04 |
| PostgreSQL game ownership separation | `ACCEPTED` | `NOT_STARTED` physical game schema | ADR-0004 + DUR contracts |
| Native world/content format + Oteryn Studio boundary | `ACCEPTED` | `NOT_STARTED` executable content stack | ADR-0005 + DUR-04 |
| Game Intelligence / analytics / audit read-only direction | `ACCEPTED` | `NOT_STARTED` analytics runtime | ADR-0006 + ANL contracts |
| Native three-tier E2E evidence platform | `ACCEPTED` | `NOT_STARTED / EVIDENCE_REQUIRED` | ADR-0007 / QA-E2E-01 |
| `protocol-canary` reference-only | `ACCEPTED` | excluded from production graph | ADR-0008 |
| GameNode process / one-writer / capacity-recovery baseline | `ACCEPTED` | `NOT_STARTED` runtime/orchestration | ADR-0009 + FND-03 |
| Reference/Evolved worlds over one engine/protocol | `ACCEPTED` | `NOT_STARTED` broad profile runtime | ADR-0010 |
| Fail-closed pre-native client state | `ACCEPTED` | currently applicable | ADR-0011 |
| Character authority / Platform lifecycle split | `ACCEPTED` | `NOT_STARTED` native Character runtime | ADR-0012 |
| Platform DB independence from game PostgreSQL | `ACCEPTED` | policy | ADR-0013 |
| TCP-default / future QUIC-opt-in one-protocol strategy | `ACCEPTED` | transport runtime `NOT_STARTED` | ADR-0014 + NET-TRANSPORT-01 |
| GameNode internal implementation shape evidence-driven | `ACCEPTED` | topology not frozen | ADR-0015 |
| Transport-mode vocabulary != runtime readiness | `ACCEPTED` | all gameplay modes currently unavailable | ADR-0016 |

## 3. Accepted foundation/durability/gameplay/client/analytics gates

| Gate | DecisionStatus | DeliveryStatus | ImplementationStatus | Note |
|---|---|---|---|---|
| `FND-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` | workspace/dependency cutover applied |
| `VSL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` | exact Rust client migration/cutover complete |
| `FND-ID-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | identity vocabulary |
| `FND-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | protocol semantics/registry boundary |
| `NET-TRANSPORT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | gameplay transport architecture |
| `FND-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | runtime execution/ownership |
| `FND-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | admission/session/lease/recovery |
| `DUR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | durable ID representation |
| `DUR-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Persistence-v1 architecture |
| `DUR-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | value transaction/conservation/anti-duplication |
| `DUR-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | content/world/compiler/bundle/scripting |
| `ANL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | event/audit foundation |
| `GAME-VISION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | product direction + immutable first Reference target |
| `GAME-CHAR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Character Stage A/B |
| `GAME-ITEM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | item/equipment/container semantics |
| `GAME-CHANNEL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | player-visible Channel policy/lifecycle/multiplicity |
| `SIM-DETERMINISM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | deterministic numeric/RNG/order/replay/state-hash boundary |
| `GAME-ABILITY-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance PR #306; no Reference parity implied |
| `GAME-INTERACTION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance #309; lifecycle bookkeeping consolidated by #314 |
| `ALPHA-CLIENT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance #309; lifecycle bookkeeping consolidated by #314 |
| `GAME-AI-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance #309; lifecycle bookkeeping consolidated by #314 |
| `ANL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | read-only gameplay/balance/world analytics; lifecycle bookkeeping consolidated by #314 |
| `ANL-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | read-only economy/integrity/security analytics; lifecycle bookkeeping consolidated by #314 |
| `QA-E2E-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED / EVIDENCE_REQUIRED` | Tier 1/2/3 product evidence contract |
| `VSL-MOVE-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Stage-C local movement/collision/visibility/reconciliation architecture; #311/#318 |
| `VSL-COMBAT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Stage-C combat/death/loot/XP/pickup architecture; durable-value review passed on #311 |
| `VSL-CONTENT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Stage-C semantic/compiler/loader evidence slice; permanent physical format remains undecided |

The remaining first-wave and Stage-C architecture delivery lifecycles are closed. PR #314 merged the evaluated implementation coordinator/DAG package as `88f4fb754b5ae11243afd38a9e0b6a8e3b0a5815`; this changed programme availability, not implementation status.

## 4. Reference evidence/parity registry

Reference evidence/parity manifest v1 is accepted/pinned. `ABILITY_COMBAT` contains four Light Healing/Ice Strike cases. Agent A PR #271 promoted **0/4**.

Current state:

```yaml
target: Global Tibia after 2026-07-28 server-save boundary
registered_cases: 4
promoted_cases: 0
target_evidence: UNKNOWN
source_case_provenance: PENDING
legal_review: PENDING
oteryn_implementation: NOT_STARTED
parity: PARITY_PENDING_EVIDENCE
```

No architecture acceptance or implementation similarity may silently promote parity.

## 5. Stage-C vertical-slice architecture

The three former Stage-C architecture blockers are owner-accepted and lifecycle-closed. `VSL-01` remains the proof programme and is not itself an implementation-completeness claim.

| Gate | Current role | DecisionStatus | DeliveryStatus | Remaining boundary |
|---|---|---|---|---|
| `VSL-01` | foundation vertical-slice proof programme | `PLANNED` | `PLANNED` | executable implementation/E2E evidence remains future work |
| `VSL-MOVE-01` | movement slice architecture | `ACCEPTED` | `LIFECYCLE_CLOSED` | implementation, exact Reference values and wider cross-scope handoff remain separately gated |
| `VSL-COMBAT-01` | combat/value slice architecture | `ACCEPTED` | `LIFECYCLE_CLOSED` | implementation, exact Reference formulas/values and broader reward models remain separately gated |
| `VSL-CONTENT-01` | native content slice architecture | `ACCEPTED` | `LIFECYCLE_CLOSED` | implementation and permanent World Project/Bundle physical-format selection remain separately gated |

Canonical acceptance is `OTERYN_V2_STAGE_C_VSL_OWNER_ACCEPTANCE_20260816.md`; candidate contracts define the exact accepted bounded scope. PR #311 merged that acceptance as `e0ea9ef87c01dec720a22e8df6d54bfd669cb62c`. The genuine independent exact-head review is `4949049662`. Lifecycle/status reconciliation is PR #318 / `a6a5180d98cf7791e40d9e1d08b25a5c8b4eff96`.

`QA-E2E-01` architecture is accepted, but executable E2E implementation/evidence remains required before any terminal `VSL-01 complete` claim.

## 6. Alpha/product gates still registered

The following stable gates remain in the horizon and are **not silently accepted by Stage-C or executor-programme release**:

| Gate | Role / current disposition |
|---|---|
| `ALPHA-RULESET-01` | `REQUIRED_FOR_ALPHA`; ruleset/profile composition beyond accepted core semantics |
| `ALPHA-CONTENT-01` | `REQUIRED_FOR_ALPHA`; NPC/quest/shop/content-runtime completeness |
| `ALPHA-QUALITY-01` | `REQUIRED_FOR_ALPHA`; product quality/performance/evidence completeness |
| `ALPHA-MILESTONE-01` | `REQUIRED_FOR_ALPHA`; milestone outcomes/exclusions |
| `PERF-01` | `REQUIRED_FOR_ALPHA`; measured resource/capacity/latency/headroom ceilings |
| `OPS-CHANNEL-01` | `BLOCKS_LAYER_IMPLEMENTATION`; automatic production channel scaling/recovery |
| `PROD-LIVEOPS-01` | `REQUIRED_FOR_ALPHA`; LiveOps/runtime configuration authority |
| `PROD-COMPAT-01` | `REQUIRED_FOR_ALPHA`; release compatibility/version train |
| `SEC-CLIENT-01` | `REQUIRED_FOR_ALPHA`; client integrity/anti-cheat boundary |
| `DATA-PRIVACY-01` | `REQUIRED_FOR_ALPHA`; product privacy/data lifecycle completion |
| `UX-I18N-A11Y-01` | `REQUIRED_FOR_ALPHA`; localization/input/onboarding/accessibility product completeness |
| `OPS-GM-01` | `REQUIRED_FOR_ALPHA`; support/moderation/GM operations |

These gates do not all block the **first technical vertical slice**. They do block a later claim of playable/external alpha completeness in their named scope.

## 7. Deferred / lane-specific gate

### `PROD-ENTITLEMENTS-01`

- current DecisionStatus: `PROPOSED / DEFERRED` for unrelated foundation work;
- Platform producer-side finite-authority prerequisite: **SATISFIED** and pinned;
- Oteryn-v2 game-consumer/enforcement contract: **NOT_ACCEPTED**;
- implementation: `NOT_STARTED`;
- Premium/VIP/game-consumed entitlement executor/activation: **BLOCKED**.

This gate does not block unrelated admission/movement/combat/content vertical-slice work.

## 8. Expansion/deferred horizon retained

The detailed scope remains in `GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md`. Stable IDs retained include:

- `GAME-META-01` — recurring progression/collections/achievements (`EXPANSION`);
- `GAME-INSTANCES-01` — dungeons/arenas/matchmaking/spectating (`EXPANSION`);
- `GAME-WORLD-LIFECYCLE-01` — world lifecycle/transfer/merge (`EXPANSION`);
- `INTEGRATION-API-01` — external APIs/notifications/integrations (`EXPANSION`);
- `MOD-ECOSYSTEM-01` — modding/plugin ecosystem (`DEFERRED`);
- `EXP-EVENTS-01` — dynamic events/raids/bosses (`EXPANSION`);
- `EXP-HOUSES-01` — houses (`DEFERRED`);
- `EXP-SOCIAL-01` — party/guild/chat/friends/presence (`EXPANSION`);
- `EXP-ECONOMY-01` — market/trade/economy (`EXPANSION`);
- `EXP-SECURITY-01` — broader abuse/admin/security (`EXPANSION`);
- `EXP-UPDATE-01` — launcher/updater/distribution (`DEFERRED`);
- `EXP-OPS-01` — broader operations (`EXPANSION`);
- `EXP-OBS-01` — broader observability (`EXPANSION`);
- `EXP-SCALE-01` — advanced scaling/prediction/live migration (`DEFERRED`).

Registration prevents omission; it does not authorize implementation.

## 9. Progressive execution policy

1. Do not re-open accepted architecture without named superseding evidence.
2. Do not use proposal/candidate delivery status as a substitute for owner acceptance.
3. Do not let implementation choose cross-domain ownership, idempotency, durability, authority or public protocol semantics that belong to an unaccepted gate.
4. Technology/library choices remain deferred when accepted architecture intentionally leaves them reversible.
5. Resource values belong to accepted registries/PERF/OPS evidence, not arbitrary executor constants.
6. Cross-repository authority pins immutable merged revisions, never mutable PR heads.
7. Reference parity remains an evidence claim, never an architecture-status side effect.
8. Any runtime/DDL/production work requires a separate explicit implementation allocation/authority.
9. Stage-C implementation must consume the accepted `VSL-MOVE-01`, `VSL-COMBAT-01` and `VSL-CONTENT-01` contracts and preserve their remaining evidence/resource/foreign-owner gates.
10. Entitlement implementation remains excluded until `PROD-ENTITLEMENTS-01` is separately accepted.
11. A released worker prompt does not grant write authority without a current coordinator allocation.

## 10. Current next architecture/execution action

No owner decision remains to accept the bounded first-wave or Stage-C architecture, and no prompt-release blocker remains.

The evaluated coordinator-led implementation programme merged via PR #314 / `88f4fb754b5ae11243afd38a9e0b6a8e3b0a5815`.

When implementation should begin, the explicit entry point is:

```text
Oteryn: implementation coordinator
```

The coordinator must re-read live `main`, current governance and the released DAG before creating the serial Bootstrap allocation. No direct worker may self-start.

## 11. Executor programme state

```text
EXECUTOR_PROGRAMME: RELEASED
DEFAULT_ENTRYPOINT: Oteryn: implementation coordinator
DIRECT_WORKERS: ALLOCATION_GATED
IMPLEMENTATION_WORKERS_STARTED: NO
IMPLEMENTATION_AUTHORITY_OUTSIDE_LIVE_COORDINATOR_ALLOCATION: NONE
PRODUCTION_AUTHORITY: NONE
```
