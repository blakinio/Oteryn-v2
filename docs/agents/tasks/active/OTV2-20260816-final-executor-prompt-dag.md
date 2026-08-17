# OTV2-20260816-final-executor-prompt-dag

```yaml
task_id: OTV2-20260816-final-executor-prompt-dag
title: Build canonical implementation executor prompt DAG
mode: COORDINATE
status: blocked_on_independent_review
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: 314
base_sha: bf2a2ae279516f62626a5d8f4dc1aeb587535c62
owner: Architecture Coordinator
created_at: 2026-08-16T21:35:59+02:00
updated_at: 2026-08-17T08:35:00+02:00
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
  - docs/agents/tasks/active/OTV2-20260816-remaining-first-wave-owner-decisions.md
  - docs/agents/tasks/archive/OTV2-20260816-remaining-first-wave-owner-decisions.md
public_contracts:
  - docs/agents/programs/OTERYN_V2_IMPLEMENTATION_EXECUTOR_DAG.md
blocks:
  - Stage-C PR #311 genuinely independent exact-head review
  - Stage-C PR #311 merge/lifecycle/status reconciliation
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
- The owner accepted VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 on PR #311. That acceptance is not yet canonical on main because root `AGENTS.md` requires genuinely independent exact-head review for the durable loot/value semantics in VSL-COMBAT-01.
- Automatic Codex Review and the supported manual `@codex review` trigger were both attempted under explicit PR #311 authorization; both returned usage-limit notices and produced no review.
- Existing `Architecture semantic audit` executes on exact head but returns `NOT_APPLICABLE` for Stage-C and therefore is not qualifying independent review evidence.
- Direct collaborators contain only the repository owner; no second qualified GitHub collaborator is available.

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

Material findings repaired:

1. hidden accepted-but-unimplemented SIM/Domain/Ability/Interaction/AI dependencies;
2. missing hard `Movement -> Combat` integration order;
3. implicit worker lifecycle/budget/handover requirements;
4. implicit trusted-source order/evidence classification/unmerged-sibling rules.

Final package-content verdict remains valid because subsequent consolidation changed only task bookkeeping, not execution prompt content:

```text
17/17 execution prompts: PASS
Authority / Resolution / Ownership / Architecture / Completeness / Evidence / Validation / Autonomy / Handover / Safety: PASS
OPEN MATERIAL PROMPT FINDINGS: 0
PROMPT_QUALITY: PASS
EXECUTOR_PROMPTS: HOLD
```

## Lifecycle consolidation

The already-merged first-wave decision task from PR #309 is now archived inside #314. Bookkeeping-only draft PR #312 is therefore redundant and may be closed as superseded without merge. This consolidation changes no architecture semantics and avoids an extra future ready/merge transition.

## Current work completed

- [x] canonical implementation DAG written and corrected;
- [x] implementation coordinator prompt written;
- [x] all bounded worker/evidence-lane prompts written;
- [x] prompt README/aliases registered;
- [x] draft PR #314 opened;
- [x] full prompt evaluation completed;
- [x] four material evaluation findings repaired;
- [x] prompt evaluation evidence persisted;
- [x] stale PR #305 terminally superseded and closed without merge;
- [x] redundant first-wave closeout PR #312 consolidated into #314 at the content level;
- [ ] fresh exact-head #314 CI/self-review after bookkeeping consolidation;
- [ ] Stage-C #311 genuinely independently reviewed and merged;
- [ ] Stage-C task/current status/register/index reconciled after #311 merge;
- [ ] #314 reconciled against exact post-Stage-C main;
- [ ] #314 merged/closed out and executor release state flipped from HOLD only if every release gate still passes.

## Release conditions

The prompt package remains `HOLD` until:

1. VSL-MOVE-01, VSL-COMBAT-01 and VSL-CONTENT-01 acceptance delivery is independently reviewed, merged and lifecycle-closed;
2. current status/register/index no longer list Stage-C architecture as an executor blocker;
3. #314 is reconciled to that exact main;
4. any post-reconciliation prompt-content delta is re-evaluated;
5. final exact-head #314 governance/merge gates and self-review pass;
6. no prompt grants entitlement, production, external-repository or Reference-parity authority.

## Independent reviewer handoff

A fresh separate reviewer/session must independently inspect PR #311 exact head:

`c5d9f839abd8998d42f4f37b203882f03bb51ce0`

It must not trust coordinator summaries as evidence. Review scope is durable loot/value identity and anti-duplication first, then Movement authority, Content-format non-freezing, Reference fixture discipline, resource-limit fail-closed behavior and scope/authority leakage. The reviewer must post exact-head review evidence identifying material findings or explicit zero material findings.

## Context checkpoint

```yaml
last_progress: final executor package is prompt-evaluated; #305 closed; #312 closeout content consolidated into #314; all available Codex review paths for #311 attempted and returned usage-limit
status: blocked_on_independent_review
branch: docs/final-executor-prompt-dag-20260816
issue: 313
pr: 314
owner_action_required: fresh separate reviewer/session for PR #311 exact head; no new architecture decision is required
blocker: mandatory genuinely independent exact-head review for PR #311 is unavailable in the current session/toolset
next_action: independent reviewer audits PR #311 exact head c5d9f839abd8998d42f4f37b203882f03bb51ce0 and records PASS/findings; coordinator then resumes merge -> reconciliation -> #314 finalization
executor_prompts: HOLD
```

`IMPLEMENTATION_AUTHORITY: NONE`
