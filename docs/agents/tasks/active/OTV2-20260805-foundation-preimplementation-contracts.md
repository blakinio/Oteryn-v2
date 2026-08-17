# OTV2-20260805-foundation-preimplementation-contracts

```yaml
task_id: OTV2-20260805-foundation-preimplementation-contracts
title: Coordinate Oteryn v2 foundation contracts and staged implementation gates
mode: COORDINATE
status: ready_for_owner_initiated_implementation
repository: blakinio/Oteryn-v2
base_branch: main
branch: null
pr: null
owner: unassigned
created_at: 2026-08-05T08:49:00+02:00
updated_at: 2026-08-17
owned_paths: []
public_contracts:
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/README.md
  - docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md
continuation_prompt: docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
implementation_prompt: docs/agents/prompts/OTV2_IMPLEMENTATION_COORDINATOR.md
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
```

## Outcome

Maintain a truthful **non-owning** programme checkpoint. This record owns no architecture or implementation path. Every material implementation lane requires its own bounded task/branch/PR/evidence lifecycle and a live coordinator allocation.

## Current accepted architecture

Consume, do not restart, the owner-accepted foundation/gameplay/client/analytics architecture recorded in `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` and `GLOBAL_ARCHITECTURE_DECISION_REGISTER.md`.

Current bounded first-wave and Stage-C state:

```yaml
GAME-ABILITY-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
GAME-INTERACTION-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
ALPHA-CLIENT-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
GAME-AI-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
ANL-02: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
ANL-03: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
VSL-MOVE-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
VSL-COMBAT-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
VSL-CONTENT-01: ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED
```

Stage-C owner acceptance merged through PR #311 / `e0ea9ef87c01dec720a22e8df6d54bfd669cb62c`. Its genuine independent exact-head review is `4949049662` with zero material findings. Lifecycle/status closeout merged through PR #318 / `a6a5180d98cf7791e40d9e1d08b25a5c8b4eff96`.

Reference evidence remains 0/4 promoted and fail closed. Architecture acceptance does not imply parity.

## Released implementation handoff

The evaluated implementation prompt package merged through PR #314 / `88f4fb754b5ae11243afd38a9e0b6a8e3b0a5815`.

Formal prompt-package result:

```text
17/17 execution prompts: PASS
10/10 prompt-evaluation gates: PASS
open material prompt findings: 0
```

Release semantics:

```text
EXECUTOR_PROGRAMME: RELEASED
DEFAULT_ENTRYPOINT: Oteryn: implementation coordinator
DIRECT_WORKERS: ALLOCATION_GATED
IMPLEMENTATION_WORKERS_STARTED: NO
IMPLEMENTATION_AUTHORITY_OUTSIDE_LIVE_COORDINATOR_ALLOCATION: NONE
```

PR #314 merge did not create a Bootstrap allocation and did not start any implementation worker.

## Canonical implementation order

```text
BOOTSTRAP [serial]
  -> FOUNDATION + SIM + DOMAIN + CONTENT + QA
  -> DURABILITY after Foundation/Domain
  -> ABILITY + INTERACTION + AI after Foundation/SIM/Domain/Content
  -> CLIENT after compatible Foundation seam
  -> MOVE after Foundation/SIM/Domain/Content/Interaction/Client/QA
  -> COMBAT only after merged MOVE + Foundation/SIM/Domain/Content/Ability/Interaction/Durability/Client/QA

CHANNEL = later after Foundation/Domain/Durability
CONTENT-FORMAT-SPIKE = evidence only
ANALYTICS = later after concrete producer event families exist
```

Stable workspace/registry/stable-ID mutations remain serialized.

## Lane-specific holds preserved

- `PROD-ENTITLEMENTS-01` remains unaccepted on the Oteryn-v2 consumer/enforcement side; Premium/VIP/game-consumed entitlement implementation/activation remains blocked.
- Exact Reference formulas/mechanics/values remain evidence-gated; test fixtures cannot establish parity.
- Permanent World Project/Bundle physical encoding remains blocked on the DUR-04 format spike plus later owner decision.
- Missing required resource ceilings fail closed.
- High-risk protocol/session/admission/persistence/item/loot/value/multichannel/fencing implementation changes require genuinely independent exact-head review.
- QA-E2E real-boundary evidence remains required for terminal vertical-slice proof.
- Production/protected-environment/live data/session/account, Platform/external-repository and owner-funded AI authority remain separately governed.

## Current execution boundary

There is no remaining Stage-C or prompt-package blocker to starting the bounded implementation coordinator programme.

Implementation does **not** begin automatically. When the owner explicitly wants implementation to start, invoke:

```text
Oteryn: implementation coordinator
```

The coordinator must first verify live `main`, current governance and the released DAG, then create the serial Bootstrap allocation. Direct worker aliases remain read-only until allocated.

## Context checkpoint

```yaml
last_progress: first-wave and Stage-C architecture lifecycle closed; evaluated executor DAG merged via #314 and programme released
status: ready_for_owner_initiated_implementation
owner_action_required: explicit invocation of `Oteryn: implementation coordinator` only when implementation should start
blocker: null for starting the bounded coordinator programme; lane-specific evidence/authority/resource holds remain binding
authorized_implementation_started: false
next_action: owner invokes `Oteryn: implementation coordinator`; coordinator then verifies live main and creates the serial Bootstrap allocation
executor_programme: RELEASED
```

`IMPLEMENTATION_WORKERS_STARTED: NO`
`IMPLEMENTATION_AUTHORITY_OUTSIDE_LIVE_COORDINATOR_ALLOCATION: NONE`
`PRODUCTION_AUTHORITY: NONE`
