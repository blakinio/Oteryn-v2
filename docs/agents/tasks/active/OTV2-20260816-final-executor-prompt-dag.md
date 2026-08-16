# OTV2-20260816-final-executor-prompt-dag

```yaml
task_id: OTV2-20260816-final-executor-prompt-dag
title: Build canonical implementation executor prompt DAG
mode: COORDINATE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: 314
base_sha: bf2a2ae279516f62626a5d8f4dc1aeb587535c62
owner: Architecture Coordinator
created_at: 2026-08-16T21:35:59+02:00
updated_at: 2026-08-16T22:45:00+02:00
execution_budget_minutes: 120
owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-final-executor-prompt-dag.md
  - docs/agents/evidence/OTV2-20260816-final-executor-prompt-evaluation.md
  - docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md
  - docs/agents/prompts/OTV2_IMPLEMENTATION_COORDINATOR.md
  - docs/agents/prompts/OTV2_IMPL_WORKSPACE_BOOTSTRAP.md
  - docs/agents/prompts/OTV2_IMPL_FOUNDATION_RUNTIME.md
  - docs/agents/prompts/OTV2_IMPL_SIMULATION.md
  - docs/agents/prompts/OTV2_IMPL_DOMAIN_CORE.md
  - docs/agents/prompts/OTV2_IMPL_DURABILITY.md
  - docs/agents/prompts/OTV2_IMPL_VSL_CONTENT.md
  - docs/agents/prompts/OTV2_IMPL_GAME_ABILITY.md
  - docs/agents/prompts/OTV2_IMPL_GAME_INTERACTION.md
  - docs/agents/prompts/OTV2_IMPL_GAME_AI.md
  - docs/agents/prompts/OTV2_IMPL_NATIVE_CLIENT.md
  - docs/agents/prompts/OTV2_IMPL_QA_E2E.md
  - docs/agents/prompts/OTV2_IMPL_VSL_MOVEMENT.md
  - docs/agents/prompts/OTV2_IMPL_VSL_COMBAT.md
  - docs/agents/prompts/OTV2_IMPL_GAME_CHANNEL.md
  - docs/agents/prompts/OTV2_CONTENT_FORMAT_SPIKE.md
  - docs/agents/prompts/OTV2_IMPL_ANALYTICS.md
  - docs/agents/prompts/README.md
public_contracts:
  - docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md
blocks:
  - Stage-C PR #311 independent-review/merge/lifecycle reconciliation
  - post-Stage-C exact-main reconciliation before executor release
cross_repository_coordination_id: OTV2-NATIVE-IMPLEMENTATION
external_repositories: []
```

## Outcome

Prepare the reusable implementation prompt DAG now, but keep it explicitly unreleased until Stage-C architecture acceptance is merged/lifecycle-closed and the package is reconciled against that exact main.

## Live repository facts driving the DAG

- Current trusted base remains `main@bf2a2ae279516f62626a5d8f4dc1aeb587535c62` while Stage-C #311 is unmerged.
- No authoritative Rust server application exists yet; only `apps/client` exists as an application.
- `workspace-boundaries.toml`, `tools/architecture-check` and Rust CI encode the current pre-native 19-member boundary and must be atomically reconciled by Bootstrap when real server/protocol components enter.
- FND-02 protocol registry intentionally has empty gameplay `command_types`, `state_domains` and capabilities; owning gameplay lanes register them later.
- `GAME_EVENT_FOUNDATION_REGISTRY.json` intentionally has `event_types: []`; producer domains register concrete families before Analytics may consume them.
- Owner has accepted VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 in PR #311. That acceptance is not yet canonical on main because required independent review for durable loot/value integration is unsatisfied after Codex returned a usage-limit notice and the deterministic semantic workflow returned `NOT_APPLICABLE`.

## Final prepared DAG

```text
OTV2-IMPL-COORD
  -> OTV2-IMPL-BOOTSTRAP [serial]
      -> FOUNDATION + SIM + DOMAIN + CONTENT + QA
      -> DURABILITY after Foundation/Domain
      -> ABILITY + INTERACTION + AI after Foundation/SIM/Domain/Content
      -> CLIENT after compatible production Foundation seam
      -> MOVE after Foundation/SIM/Domain/Content/Interaction/Client/QA
      -> COMBAT only after merged MOVE + Foundation/SIM/Domain/Content/Ability/Interaction/Durability/Client/QA

CHANNEL = later after Foundation/Domain/Durability
CONTENT-FORMAT-SPIKE = evidence-only after Content
ANALYTICS = later after concrete producer event registrations
```

Normal user entry point after release is only:

```text
Oteryn: implementation coordinator
```

Direct worker aliases are allocation-gated recovery/manual entry points. Without a live coordinator allocation they remain read-only.

## Prompt evaluation

Canonical evidence:

`docs/agents/evidence/OTV2-20260816-final-executor-prompt-evaluation.md`

Prompt-content head evaluated: `80e09b83c4215ff4378e8cc8e25f85dff7db4b2d` plus the subsequent repair-only commits described in that evidence before the evidence file itself was committed.

Material findings repaired:

1. hidden accepted-but-unimplemented SIM/Domain/Ability/Interaction/AI dependencies;
2. missing hard `Movement -> Combat` integration order;
3. implicit worker lifecycle/budget/handover requirements;
4. implicit trusted-source order/evidence classification/unmerged-sibling rules.

Final package-content verdict after repairs:

```text
17/17 execution prompts: PASS
Authority / Resolution / Ownership / Architecture / Completeness / Evidence / Validation / Autonomy / Handover / Safety: PASS
OPEN MATERIAL PROMPT FINDINGS: 0
PROMPT_QUALITY: PASS
EXECUTOR_PROMPTS: HOLD
```

## Current work completed

- [x] canonical implementation DAG written and corrected;
- [x] implementation coordinator prompt written;
- [x] all bounded worker/evidence-lane prompts written;
- [x] prompt README/aliases registered;
- [x] draft PR #314 opened;
- [x] full prompt evaluation completed;
- [x] four material evaluation findings repaired;
- [x] prompt evaluation evidence persisted;
- [ ] stale PR #305 terminally superseded;
- [ ] final #314 full-diff self-review and exact-head CI completed on the post-evaluation checkpoint;
- [ ] Stage-C #311 independently reviewed/merged/lifecycle-closed;
- [ ] #314 reconciled against exact post-Stage-C main;
- [ ] #314 merged/closed out and executor release state flipped from HOLD only if all release gates still pass.

## Release conditions

The prompt package remains `HOLD` until:

1. VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 acceptance delivery is merged and lifecycle-closed;
2. current status/register/index no longer list Stage-C architecture as an executor blocker;
3. #314 is reconciled to that exact main;
4. any post-reconciliation prompt-content delta is re-evaluated;
5. stale #305 is terminally superseded;
6. final exact-head #314 governance/merge gates and self-review pass;
7. no prompt grants entitlement, production, external-repository or Reference-parity authority.

## Context checkpoint

```yaml
last_progress: 17-prompt package passes formal 10-gate evaluation after four material repairs; evaluation evidence committed on #314
status: validating
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: 314
owner_action_required: false for remaining nonblocked prompt-package work
blocker: Stage-C #311 required independent exact-head review remains unavailable; Codex returned usage-limit and existing deterministic semantic workflow is NOT_APPLICABLE
next_action: terminally supersede stale #305, then perform final #314 full-diff self-review/thread/drift/exact-head CI while keeping executor release HOLD
executor_prompts: HOLD
```

`IMPLEMENTATION_AUTHORITY: NONE`
