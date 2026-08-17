# Oteryn v2 Foundation Programme — Current Status

- Status: **Canonical current execution-status overlay**
- Date: 2026-08-17
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Applies to: current DecisionStatus / DeliveryStatus / ImplementationStatus and the next safe execution gate

## 1. Reading rule

This document is the maintained current-status source. Accepted ADRs/contracts/owner baselines remain semantic authority for their owned scope. Historical backlog/proposal/candidate prose is not current execution truth when it conflicts with this file or a later explicit owner-acceptance baseline.

`ARCHITECTURE_STATUS_MODEL.md` remains normative:

```text
DecisionStatus != DeliveryStatus != ImplementationStatus
```

Architecture acceptance and prompt release never imply runtime implementation, Reference parity or production enablement.

## 2. Programme headline

The native foundation, durability/content/determinism architecture, the complete first gameplay/client/analytics architecture wave, and the bounded Stage-C movement/combat/content architecture are owner-accepted and lifecycle-closed.

Canonical recent deliveries:

- `GAME-ABILITY-01`: PR #306 / merge `e2bb284f56f39d8fa01a843d098bcb21d17d77ac`; closeout #307 / `dfc75d1332f710d6ac85009653579f7bc51ccc59`;
- remaining first-wave acceptance: PR #309 / merge `bf2a2ae279516f62626a5d8f4dc1aeb587535c62`; its final bookkeeping archive/removal is consolidated into PR #314;
- Stage-C acceptance: PR #311 / merge `e0ea9ef87c01dec720a22e8df6d54bfd669cb62c`;
- Stage-C genuinely independent review: review `4949739986`, zero material findings on exact head `c5d9f839abd8998d42f4f37b203882f03bb51ce0`;
- Stage-C lifecycle/status closeout: PR #318 / merge `a6a5180d98cf7791e40d9e1d08b25a5c8b4eff96`;
- final implementation-prompt handoff: PR #314. When this file reaches `main` through #314, the prompt package is released for explicit owner invocation.

No accepted gameplay/runtime gate below is implemented merely because its architecture or prompt is released.

## 3. Current three-axis status

| Gate | DecisionStatus | DeliveryStatus | ImplementationStatus | Current note |
|---|---|---|---|---|
| `FND-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` | repository/workspace cutover already applied |
| `VSL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `PROVEN` | native-client repository migration/cutover complete |
| `FND-ID-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | identity runtime implementation remains future work |
| `FND-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | `protocol-oteryn` foundation architecture accepted |
| `NET-TRANSPORT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | TCP-default / future QUIC-opt-in architecture accepted |
| `FND-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | one-writer runtime architecture accepted |
| `FND-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | admission/GameSession/CharacterLease/reconnect architecture accepted |
| `DUR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | durable identifier representation accepted |
| `DUR-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Persistence-v1 architecture accepted |
| `DUR-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | item/value conservation/idempotency/anti-dup architecture accepted |
| `DUR-04` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | content/world/compiler/bundle/scripting architecture accepted |
| `ANL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | event/audit foundation accepted |
| `GAME-VISION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | immutable first Reference target accepted |
| `GAME-CHANNEL-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Channel product/lifecycle policy accepted |
| `GAME-CHAR-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | Character Stage A/B semantics accepted |
| `GAME-ITEM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | item/equipment/container semantics accepted |
| `SIM-DETERMINISM-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | deterministic numeric/RNG/order/replay boundary accepted |
| `GAME-ABILITY-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | one typed authoritative effect pipeline accepted |
| `GAME-INTERACTION-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance #309; lifecycle archive consolidated into #314 |
| `ALPHA-CLIENT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance #309; lifecycle archive consolidated into #314 |
| `GAME-AI-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | owner acceptance #309; lifecycle archive consolidated into #314 |
| `ANL-02` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | read-only gameplay/balance/world analytics architecture accepted |
| `ANL-03` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | read-only economy/integrity/security analytics architecture accepted |
| `QA-E2E-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED / EVIDENCE_REQUIRED` | Tier 1/2/3 proof platform architecture accepted |
| `VSL-MOVE-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | bounded movement/collision/visibility/reconciliation architecture accepted |
| `VSL-COMBAT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | bounded combat/death/loot/XP/pickup architecture accepted |
| `VSL-CONTENT-01` | `ACCEPTED` | `LIFECYCLE_CLOSED` | `NOT_STARTED` | bounded native content/compiler/loader evidence slice accepted |
| `VSL-01` | `PLANNED` | `PLANNED` | `NOT_STARTED` | vertical-slice proof programme, not an implementation claim |
| `PERF-01` | `PLANNED` | `PLANNED` | `NOT_STARTED` | measured numeric capacity/resource evidence remains required |
| `OPS-CHANNEL-01` | `PLANNED` | `PLANNED` | `NOT_STARTED` | production channel scaling/recovery remains separately gated |
| `PROD-ENTITLEMENTS-01` | `PROPOSED` | `PLANNED` | `NOT_STARTED` | Oteryn-v2 entitlement consumer/enforcement contract remains unaccepted |

## 4. Reference evidence/parity state

The accepted Reference evidence/parity manifest remains paper-only evidence authority. `ABILITY_COMBAT` remains exactly:

```yaml
registered_cases: 4
promoted_cases: 0
target_evidence: UNKNOWN
source_case_provenance: PENDING
legal_review: PENDING
oteryn_implementation: NOT_STARTED
parity: PARITY_PENDING_EVIDENCE
canonical_digest: null
```

Agent A #271 promoted **0/4**. No architecture acceptance or prompt release changes that result.

## 5. Binding implementation boundary

The released implementation programme must consume the accepted contracts rather than make architecture decisions inside code.

The normal owner entry point after PR #314 merges is:

```text
Oteryn: implementation coordinator
```

The coordinator then creates/resumes bounded allocations. Direct worker aliases remain read-only without a live coordinator allocation naming their exact lane, paths, dependencies and merge order.

Canonical dependency order:

```text
BOOTSTRAP [serial]
  -> FOUNDATION + SIM + DOMAIN + CONTENT + QA
  -> DURABILITY after Foundation/Domain
  -> ABILITY + INTERACTION + AI after Foundation/SIM/Domain/Content
  -> CLIENT after a compatible Foundation protocol seam
  -> MOVE after Foundation/SIM/Domain/Content/Interaction/Client/QA
  -> COMBAT only after merged MOVE + Foundation/SIM/Domain/Content/Ability/Interaction/Durability/Client/QA

CHANNEL = later after Foundation/Domain/Durability
CONTENT-FORMAT-SPIKE = evidence only
ANALYTICS = later after concrete producer event families exist
```

Stable workspace/registry/ID mutations remain serialized even when implementation code lanes otherwise overlap.

## 6. Holds that remain real after prompt release

Prompt release does not remove lane-specific evidence or authority gates:

- `PROD-ENTITLEMENTS-01` still blocks Premium/VIP/game-consumed entitlement implementation/activation only;
- exact Reference movement/combat/loot/XP formulas and values remain evidence-gated;
- permanent World Project/World Bundle physical encoding still requires the DUR-04 format spike and later owner format decision;
- concrete finite resource ceilings are required before affected executable acceptance; missing values fail closed;
- concrete producer event families must exist before ANL-02/03 can claim real metric/detector coverage;
- protocol/admission/server/client/persistence implementations remain `NOT_STARTED`;
- `QA-E2E-01` executable Tier 1/2/3 evidence remains mandatory for terminal vertical-slice proof;
- `PERF-01` / `OPS-CHANNEL-01` retain measured production capacity/orchestration authority;
- high-risk protocol/session/admission/persistence/item/loot/value/multichannel/fencing changes require genuinely independent exact-head review under root `AGENTS.md`.

## 7. Executor prompt state

When this document is merged as part of PR #314:

```text
EXECUTOR_PROMPTS: RELEASED
DEFAULT_ENTRYPOINT: Oteryn: implementation coordinator
DIRECT_WORKERS: ALLOCATION_GATED
IMPLEMENTATION_STARTED: NO
```

Merging #314 does not itself start implementation. Implementation begins only when the owner explicitly invokes the released coordinator prompt.

## 8. Runtime / production authority

Nothing in this status overlay or prompt release authorizes production deployment, protected-environment approval, live data/session/account mutation, production PostgreSQL migration execution, Platform writes, external-repository mutation, entitlement activation, Reference parity claims or owner-funded AI use.

```text
IMPLEMENTATION_AUTHORITY: NONE_UNTIL_OWNER_INVOCATION
```
