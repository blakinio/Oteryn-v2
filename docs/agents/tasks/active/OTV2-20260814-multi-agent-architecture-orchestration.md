# OTV2-20260814-multi-agent-architecture-orchestration

```yaml
task_id: OTV2-20260814-multi-agent-architecture-orchestration
title: Establish coordinator-owned parallel architecture design programme
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/multi-agent-architecture-orchestration
issue: 258
pr: null
base_sha: 85acd19e976943ee42b5c004ebd0ae1c40cc5fff
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator
created_at: 2026-08-14T16:01:00+02:00
updated_at: 2026-08-14T16:01:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - AGENTS.override.md
  - docs/agents/AGENTS.md
  - docs/agents/MULTI_AGENT_ARCHITECTURE_ORCHESTRATION.md
  - docs/agents/prompts/OTV2_DOMAIN_ARCHITECTURE_DESIGN_AGENT.md
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md
  - docs/agents/tasks/active/OTV2-20260814-multi-agent-architecture-orchestration.md
public_contracts: []
depends_on:
  - PR #257 merge 85acd19e976943ee42b5c004ebd0ae1c40cc5fff
  - owner instruction to parallelize Architecture Continuation with coordinator-only integration/merge authority
blocks:
  - creation of first-wave worker branches for issues #259 through #264
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Create a durable hub-and-spoke architecture workflow in which domain agents work concurrently on disjoint proposal/evidence scopes and produce draft PRs, while one Architecture Coordinator/Auditor is the only role allowed to integrate, mark accepted work canonical, merge, lifecycle-close and reconcile global coordination surfaces.

## Acceptance criteria

- [ ] Add a canonical multi-agent architecture orchestration policy.
- [ ] Narrow merge/lifecycle authority for assigned architecture domain workers without expanding repository/runtime/production authority.
- [ ] Add a reusable self-contained domain-worker prompt aligned with `PROMPTING_STANDARD.md`.
- [ ] Replace the stale single-agent coordinator prompt with the coordinator/auditor integration model.
- [ ] Add first-wave allocation for issues #259–#264 with disjoint branch names and owned-path scopes.
- [ ] Preserve Agent A (#259) as the canonical Reference-evidence priority lane while allowing B–F to progress as noncanonical proposal lanes.
- [ ] Forbid domain workers from editing coordinator-only overlays or triggering owner-funded Codex/OpenAI without exact authorization.
- [ ] Require `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY` in every worker PR.
- [ ] Validate governance and full diff on exact final head.
- [ ] Leave worker branch creation until this policy is merged, so workers start from a trusted base containing their governing rules.

## Excluded scope

No gameplay/runtime/client/server/protocol implementation; no DDL/migrations; no Platform or external-repository writes; no production changes; no domain architecture decision acceptance; no Reference evidence promotion; no Codex/OpenAI invocation unless the owner separately authorizes the exact PR/use.

## Parallel work queue

- coordinator programme: issue #258;
- Agent A / Reference continuity+provenance: #259;
- Agent B / GAME-ABILITY whole-gate gap: #260;
- Agent C / GAME-AI-01: #261;
- Agent D / GAME-INTERACTION-01: #262;
- Agent E / ALPHA-CLIENT-01: #263;
- Agent F / ANL-02+ANL-03: #264.

## Context checkpoint

```yaml
last_progress: PR #257 lifecycle closeout merged as 85acd19e976943ee42b5c004ebd0ae1c40cc5fff; coordinator umbrella #258 and worker issues #259-#264 are open; orchestration branch claimed from exact post-closeout main.
status: implementing
branch: docs/multi-agent-architecture-orchestration
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
owner_action_required: false
blocker: null
next_action: Add governance narrowing, orchestration policy, worker/coordinator prompts and first-wave allocation, then open one draft coordinator PR for issue #258.
```
