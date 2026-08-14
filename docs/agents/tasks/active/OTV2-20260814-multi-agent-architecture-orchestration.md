# OTV2-20260814-multi-agent-architecture-orchestration

```yaml
task_id: OTV2-20260814-multi-agent-architecture-orchestration
title: Establish coordinator-owned parallel architecture design programme
mode: COORDINATE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/multi-agent-architecture-orchestration
issue: 258
pr: 265
base_sha: 85acd19e976943ee42b5c004ebd0ae1c40cc5fff
head_sha: 9b20fb150bc764489fd83d4b74d23ef633b35aaf
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator
created_at: 2026-08-14T16:01:00+02:00
updated_at: 2026-08-14T16:10:00+02:00
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

- [x] Add a canonical multi-agent architecture orchestration policy.
- [x] Narrow merge/lifecycle authority for assigned architecture domain workers without expanding repository/runtime/production authority.
- [x] Add a reusable self-contained domain-worker prompt aligned with `PROMPTING_STANDARD.md`.
- [x] Replace the stale single-agent coordinator prompt with the coordinator/auditor integration model.
- [x] Add first-wave allocation for issues #259–#264 with disjoint future branch names and owned-path scopes.
- [x] Preserve Agent A (#259) as the canonical Reference-evidence priority lane while allowing B–F to progress as noncanonical proposal lanes.
- [x] Forbid domain workers from editing coordinator-only overlays or triggering owner-funded Codex/OpenAI without exact authorization.
- [x] Require `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY` in every worker PR.
- [ ] Complete final exact-head full-diff/governance validation, review disposition, merge and lifecycle closeout.
- [x] Leave worker branch creation until this policy is merged, so workers start from a trusted base containing their governing rules.

## Excluded scope

No gameplay/runtime/client/server/protocol implementation; no DDL/migrations; no Platform or external-repository writes; no production changes; no domain architecture decision acceptance; no Reference evidence promotion; no Codex/OpenAI invocation unless the owner separately authorizes the exact PR/use.

## Parallel work queue

- coordinator programme: issue #258 / draft PR #265 / branch `docs/multi-agent-architecture-orchestration`;
- Agent A / Reference continuity+provenance: #259 / future branch `docs/arch-a-reference-continuity`;
- Agent B / GAME-ABILITY whole-gate gap: #260 / `docs/arch-b-game-ability-gap`;
- Agent C / GAME-AI-01: #261 / `docs/arch-c-game-ai`;
- Agent D / GAME-INTERACTION-01: #262 / `docs/arch-d-game-interaction`;
- Agent E / ALPHA-CLIENT-01: #263 / `docs/arch-e-alpha-client`;
- Agent F / ANL-02+ANL-03: #264 / `docs/arch-f-analytics-integrity`.

Issue comments now bind every A–F issue to its exact future branch, merged worker prompt/policy prerequisite and coordinator-only merge authority.

## Governance effect

The delivery is intentionally restrictive:

- general task-own PR merge authority remains unchanged outside allocated multi-agent architecture worker tasks;
- an allocated DOMAIN ARCHITECTURE DESIGN AGENT loses merge/auto-merge/lifecycle-close/global-overlay authority for that worker task;
- the Architecture Coordinator/Auditor becomes the only integration/merge/closeout role for those worker PRs, but gains no new repository/runtime/production/cross-repository authority;
- Codex/OpenAI exact-use restrictions are preserved and made explicit for draft->ready transitions;
- no hidden background-agent capability is claimed.

## Validation

### Focused

- referenced issue set #258–#264 exists: **PASS**;
- first-wave branch names are unique: **PASS**;
- worker public-contract/path ownership is disjoint by default; Agent A manifest/evidence ownership is conditional and Agent B is explicitly forbidden from those files: **PASS**;
- coordinator-only overlay list is consistent across policy, worker prompt and allocation: pending final diff audit;
- canonical `ARCHITECTURE_STATUS_MODEL` vocabulary is referenced rather than extended: pending final diff audit;
- owner-funded AI rule is narrowed/preserved, not weakened: pending final governance audit.

### Component / E2E

- runtime/component/E2E: `NOT_APPLICABLE` — governance/prompting/work-allocation only.

### Exact-head CI

Pending final resulting head.

## Self-review

Pending final full-diff review of PR #265.

## Independent review

This governance change narrows worker authority and does not expand safety/repository/production authority. Root policy does not automatically require independent review for a governance narrowing. If self-review finds unusual complexity/common-mode uncertainty or CI/repository policy requires an independent mechanism, record it honestly. Owner-funded Codex is **NOT AUTHORIZED** for PR #265 by earlier permissions.

## Context checkpoint

```yaml
last_progress: Policy, worker prompt, coordinator prompt, exact A-F work allocation and governance narrowing are implemented on draft PR #265; issues #259-#264 are bound to future branches but worker branches are intentionally deferred until this policy is merged.
status: validating
branch: docs/multi-agent-architecture-orchestration
head_sha: 9b20fb150bc764489fd83d4b74d23ef633b35aaf
pr: 265
final_head_sha: null
final_head_frozen_at: null
owner_action_required: false
blocker: null
next_action: Perform final full-diff governance/ownership/status/self-review on PR #265, run exact-head repository gates and keep the PR draft without Codex unless separately authorized.
```
