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
pr: null
base_sha: bf2a2ae279516f62626a5d8f4dc1aeb587535c62
owner: Architecture Coordinator
created_at: 2026-08-16T21:35:59+02:00
updated_at: 2026-08-16T22:16:00+02:00
execution_budget_minutes: 120
owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-final-executor-prompt-dag.md
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
  - final prompt evaluation against accepted post-Stage-C main
  - stale PR #305 terminal supersession
cross_repository_coordination_id: OTV2-NATIVE-IMPLEMENTATION
external_repositories: []
```

## Outcome

Prepare the reusable implementation prompt DAG now, but keep it explicitly unreleased until Stage-C architecture acceptance is merged/lifecycle-closed and the package is revalidated against that exact main.

## Live repository facts driving the DAG

- Current `main@bf2a2ae279516f62626a5d8f4dc1aeb587535c62` remains the pre-native workspace: 19 members and only `apps/client` as an application.
- No authoritative Rust server application exists yet.
- `workspace-boundaries.toml` and `tools/architecture-check` encode the 19-member pre-native boundary and forbid package-name fragments including `protocol-oteryn`, `transport`, `game-session`, `game-server`, `persistence`.
- `.github/workflows/rust.yml` additionally enforces a client-only production-closure negative for pre-native fragments.
- ADR-0011 permits real native protocol/server members only when accepted gates and immediate consumers exist; speculative placeholders are forbidden.
- FND-02 protocol registry has foundation message types but intentionally empty `command_types`, `state_domains` and capabilities; gameplay owners register payloads later.
- `GAME_EVENT_FOUNDATION_REGISTRY.json` intentionally has `event_types: []`; gameplay/DUR producers, not analytics, must register concrete families.
- Resource limits exist for foundation protocol/ANL foundations; domain-specific executable limits must be registered by owning implementation lanes.
- Owner has accepted VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 in PR #311. That acceptance is not yet on main because required independent review for the durable loot/value integration is still unsatisfied after Codex returned a usage-limit notice.

## Corrected DAG design

The initial prompt draft was self-reviewed and found materially incomplete because it jumped from Foundation/Content directly to Movement/Combat while SIM, Character/Item domain core, GAME-ABILITY, GAME-INTERACTION and GAME-AI are also accepted-but-unimplemented dependencies.

The corrected programme now uses:

```text
OTV2-IMPL-COORD
  -> OTV2-IMPL-BOOTSTRAP [serial]
      -> FOUNDATION + SIM + DOMAIN + CONTENT + QA
      -> DURABILITY after Foundation/Domain seams
      -> ABILITY + INTERACTION + AI after Foundation/SIM/Domain/Content
      -> CLIENT after compatible production Foundation seam
      -> MOVE after Foundation/SIM/Domain/Content/Interaction/Client/QA
      -> COMBAT after Foundation/SIM/Domain/Content/Ability/Interaction/Durability/Client/QA

CHANNEL = later after Foundation/Domain/Durability
CONTENT-FORMAT-SPIKE = evidence-only after Content seam
ANALYTICS = later after concrete producer event registrations exist
```

The coordinator owns serial canonicalization and creates an implementation allocation/status record with exact paths after bootstrap makes the real workspace shape known. Worker prompts do not invent final crate names from this pre-bootstrap branch.

## Release conditions

The prompt package remains `HOLD` until:

1. VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 acceptance delivery is merged and lifecycle-closed;
2. current status/register/index no longer list Stage-C architecture as an executor blocker;
3. this package is reconciled to that exact main;
4. every prompt passes `PROMPTING_STANDARD.md` and `PROMPT_EVAL_STANDARD.md`;
5. old prompt PR #305 is terminally superseded without losing useful maintenance history;
6. no prompt grants entitlement, production, external-repository or Reference-parity authority;
7. prompt README clearly distinguishes implementation aliases from architecture aliases;
8. the final exact-head prompt-package PR passes governance/merge gates and self-review.

## Safety invariants

- Prompt files themselves grant no production/protected-environment or external-repository authority.
- Direct worker aliases require a live coordinator allocation before writes; normal user entry point is the coordinator alias.
- High-risk protocol/session/persistence/value/multichannel changes require genuinely independent final review. Codex is optional and never authorized by prompt text.
- Workers stop rather than invent an unaccepted owner boundary, permanent content format, Reference behavior or producer event schema owned by another lane.
- Coordinator must not release overlapping worker paths or stable registry ID ranges.
- No speculative empty crate may be added merely to make the target architecture look complete.

## Current work completed on branch

- [x] canonical implementation DAG written;
- [x] implementation coordinator prompt written;
- [x] serial workspace/bootstrap executor prompt written;
- [x] Foundation runtime/protocol/admission executor prompt written;
- [x] SIM deterministic-core executor prompt written;
- [x] Character/Item domain-core executor prompt written;
- [x] Durability executor prompt written;
- [x] VSL Content executor prompt written;
- [x] GAME-ABILITY executor prompt written;
- [x] GAME-INTERACTION executor prompt written;
- [x] GAME-AI executor prompt written;
- [x] native Client executor prompt written;
- [x] QA-E2E executor prompt written;
- [x] Movement VSL executor prompt written;
- [x] Combat VSL executor prompt written;
- [x] later GAME-CHANNEL executor prompt written;
- [x] content-format evidence spike prompt written;
- [x] later Analytics executor prompt written;
- [ ] prompt README/aliases updated;
- [ ] draft PR opened and full-diff prompt evaluation recorded;
- [ ] post-Stage-C reconciliation performed;
- [ ] stale #305 terminally superseded;
- [ ] final exact-head validation/merge/closeout completed.

## Context checkpoint

```yaml
last_progress: corrected executor DAG now explicitly includes SIM, Domain Core, Ability, Interaction, AI and later Channel lanes; all worker prompts drafted
status: validating
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: null
owner_action_required: false for prompt preparation
blocker: Stage-C #311 cannot merge until a genuinely independent exact-head review is obtained; Codex attempt returned usage-limit and deterministic semantic workflow was NOT_APPLICABLE
next_action: update prompt README, open draft prompt-package PR, perform full-diff PROMPT_EVAL while HOLD, and reconcile stale #305 without releasing executors
executor_prompts: HOLD
```

`IMPLEMENTATION_AUTHORITY: NONE`
