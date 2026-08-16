# OTV2-20260816-final-executor-prompt-dag

```yaml
task_id: OTV2-20260816-final-executor-prompt-dag
title: Build canonical implementation executor prompt DAG
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: null
base_sha: bf2a2ae279516f62626a5d8f4dc1aeb587535c62
owner: Architecture Coordinator
created_at: 2026-08-16T21:35:59+02:00
updated_at: 2026-08-16T21:35:59+02:00
execution_budget_minutes: 120
owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-final-executor-prompt-dag.md
  - docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md
  - docs/agents/prompts/OTV2_IMPLEMENTATION_COORDINATOR.md
  - docs/agents/prompts/OTV2_IMPL_WORKSPACE_BOOTSTRAP.md
  - docs/agents/prompts/OTV2_IMPL_FOUNDATION_RUNTIME.md
  - docs/agents/prompts/OTV2_IMPL_DURABILITY.md
  - docs/agents/prompts/OTV2_IMPL_VSL_CONTENT.md
  - docs/agents/prompts/OTV2_IMPL_NATIVE_CLIENT.md
  - docs/agents/prompts/OTV2_IMPL_QA_E2E.md
  - docs/agents/prompts/OTV2_IMPL_VSL_MOVEMENT.md
  - docs/agents/prompts/OTV2_IMPL_VSL_COMBAT.md
  - docs/agents/prompts/OTV2_CONTENT_FORMAT_SPIKE.md
  - docs/agents/prompts/OTV2_IMPL_ANALYTICS.md
  - docs/agents/prompts/README.md
public_contracts:
  - docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md
blocks:
  - Stage-C VSL contracts owner acceptance and lifecycle closeout
  - final prompt evaluation against accepted post-Stage-C main
  - stale PR #305 terminal supersession
cross_repository_coordination_id: OTV2-NATIVE-IMPLEMENTATION
external_repositories: []
```

## Outcome

Prepare the reusable implementation prompt DAG now, but keep it explicitly unreleased until Stage-C architecture is owner-accepted/lifecycle-closed and the package is revalidated against that exact main.

## Live repository facts driving the DAG

- Current workspace contains 19 members and only one application: `apps/client`.
- No authoritative Rust server application exists yet.
- `workspace-boundaries.toml` and `tools/architecture-check` enforce the 19-member pre-native boundary and forbid package-name fragments including `protocol-oteryn`, `transport`, `game-session`, `game-server`, `persistence`.
- `.github/workflows/rust.yml` additionally enforces a client-only production-closure negative for those pre-native fragments.
- ADR-0011 permits real native protocol/server members only when accepted gates and immediate consumers exist; it forbids speculative placeholder crates.
- FND-02 protocol registry has foundation message types but intentionally empty `command_types`, `state_domains` and capabilities; gameplay owners register their payloads later.
- `GAME_EVENT_FOUNDATION_REGISTRY.json` intentionally has `event_types: []`; gameplay/DUR owners, not analytics, must register concrete producer payloads.
- Resource limits exist for foundation protocol/ANL foundations; Stage-C domain limits remain implementation-evidence owned.

## DAG design

```text
OTV2-IMPL-COORD
  -> OTV2-IMPL-BOOTSTRAP                  [serial gate]
      -> OTV2-IMPL-FOUNDATION             [server/protocol/admission]
      -> OTV2-IMPL-DURABILITY              [can overlap after allocation]
      -> OTV2-IMPL-CONTENT                 [can overlap after allocation]
      -> OTV2-IMPL-CLIENT                  [can overlap after protocol contracts/codegen seam]
      -> OTV2-IMPL-QA                      [can overlap after production wire seam exists]
          -> OTV2-IMPL-MOVE                [after foundation+durability+content+client+QA readiness]
              -> OTV2-IMPL-COMBAT          [after MOVE + durability/content/client/QA]

OTV2-CONTENT-FORMAT-SPIKE                  [after VSL content semantic compiler seam]
  -> evidence / owner format decision only; no permanent format by itself

OTV2-IMPL-ANALYTICS                        [later; only after concrete producer event families exist]
```

The coordinator owns serial canonicalization and creates an implementation allocation/status record with exact paths after the bootstrap layout is real. Worker prompts do not invent final crate names from this pre-bootstrap branch.

## Release conditions

The prompt package remains `HOLD` until:

1. VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 are owner-accepted and lifecycle-closed;
2. current status/register/index no longer list Stage-C architecture as an executor blocker;
3. this package is rebased/reconciled to that exact main;
4. every prompt passes `PROMPTING_STANDARD.md` and `PROMPT_EVAL_STANDARD.md`;
5. old prompt PR #305 is classified/superseded without losing useful maintenance history;
6. no prompt grants entitlement, production, external-repository or Reference-parity authority;
7. prompt README clearly distinguishes implementation aliases from architecture aliases.

## Safety invariants

- The prompt files themselves grant no implementation authority. An explicit owner invocation of a named implementation alias is the task request for that lane; it still does not grant production/protected-environment or external-repository authority.
- High-risk protocol/session/persistence/value/multichannel changes require genuinely independent final review. Codex is optional and never authorized by prompt text.
- Workers must stop rather than invent an unaccepted owner boundary, permanent content format, Reference behavior or producer event schema owned by another lane.
- Coordinator must not release overlapping worker paths.
- No speculative empty crate may be added merely to make the target architecture look complete.

## Context checkpoint

```yaml
last_progress: executor DAG derived from real main workspace/governance/protocol/event registries; branch created
status: implementing
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: null
owner_action_required: false
blocker: Stage-C PR #311 remains owner-decision pending
next_action: write programme + reusable coordinator/worker prompts, open draft PR, evaluate while HOLD, then reconcile after Stage-C acceptance
executor_prompts: HOLD
```

`IMPLEMENTATION_AUTHORITY: NONE`
