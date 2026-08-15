# OTV2-20260815-game-ai-successor

```yaml
task_id: OTV2-20260815-game-ai-successor
title: Re-scope GAME-AI-01 final architecture findings after predecessor repair-budget exhaustion
mode: PAPER_ONLY_SUCCESSOR_RESCOPED
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-c-game-ai-successor
issue: 275
pr: null
base_sha: cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: agent-c-game-ai-successor
created_at: 2026-08-15T12:00:00+02:00
updated_at: 2026-08-15T12:00:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
stable_architecture_gate: GAME-AI-01
predecessor_issue: 261
predecessor_pr: 272
predecessor_branch: docs/arch-c-game-ai
predecessor_final_reviewed_head: f977a2865c6210f2962a24fa9c00d556acf76122
predecessor_final_disposition: BLOCKED
repair_cycles_for_current_gate: 5
successor_task_repair_cycles: 0
repair_budget_history: predecessor recorded five repair cycles; successor exists because continuing repair under predecessor task ID is prohibited
readiness_state_model:
  - investigating
  - implementing
  - validating
  - ready
  - blocked
  - completed
merge_authority: ARCHITECTURE_COORDINATOR_ONLY
implementation_authority: NONE
owner_funded_ai_authorized: false
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-game-ai-successor.md
  - docs/architecture/GAME-AI-01_CREATURE_AI_SPAWN_PATHFINDING_ANALYSIS.md
  - docs/architecture/GAME-AI-01_CREATURE_AI_SPAWN_PATHFINDING_CONTRACT_CANDIDATE.md
public_contracts:
  - docs/architecture/GAME-AI-01_CREATURE_AI_SPAWN_PATHFINDING_CONTRACT_CANDIDATE.md
depends_on:
  - FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_CONTRACT.md
  - DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - accepted GAME-ABILITY-01 partial owner baselines
  - DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md
  - predecessor issue #261 / PR #272 final reviewed head f977a2865c6210f2962a24fa9c00d556acf76122
blocks:
  - Architecture Coordinator re-audit of the GAME-AI-01 worker package
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Produce a new, narrowly re-scoped `GAME-AI-01` worker package that resolves only the five final findings recorded on predecessor PR #272 while preserving the predecessor's correct ownership, determinism, provenance, proposal-only and fail-closed decisions.

This task does **not** create a new stable architecture gate. The stable gate remains `GAME-AI-01`.

## Successor / repair-budget governance

This task is not a sixth repair cycle of `OTV2-20260815-game-ai-architecture`.

Verified predecessor state:

- issue #261: open;
- PR #272: open draft;
- predecessor final reviewed head: `f977a2865c6210f2962a24fa9c00d556acf76122`;
- predecessor task field: `repair_cycles_for_current_gate: 5`;
- coordinator final disposition: `BLOCKED` because the three-cycle repair stop had already been exceeded.

The historical count remains recorded above as `repair_cycles_for_current_gate: 5`. `successor_task_repair_cycles: 0` is a separate task-local fact and MUST NOT be interpreted as resetting the gate's predecessor history.

This worker MUST NOT close, supersede, merge, archive or otherwise lifecycle-transition #261/#272. Those actions belong to the Architecture Coordinator.

## Bounded findings to resolve

1. **Decision timing for typed bounded FSM**
   - apply the mandatory five-part decision-timing test;
   - decide whether FSM representation itself must be frozen now;
   - do not confuse bounded semantic execution invariants with physical framework/model identity.
2. **Over-budget resolution atomicity**
   - no authoritative action may commit before a semantic-resolution plan has passed the applicable complete validation/budget preflight;
   - prefer all-or-nothing owner-local commit/reject for one semantic resolution.
3. **Spawn occupancy retries**
   - support policy-defined finite retry count/window/deadline/cadence/order with a hard maximum;
   - prohibit unbounded immediate/random retry;
   - keep exact Reference retry behavior evidence-gated.
4. **Readiness truth**
   - use only `investigating`, `implementing`, `validating`, `ready`, `blocked`, `completed` for this task's readiness state;
   - `ready` is forbidden until exact-head self-review and required CI/check evidence pass on the unchanged final head.
5. **Repair-cycle history**
   - preserve explicit predecessor linkage and five-cycle history; no reset-by-renaming.

## Preserved predecessor decisions

The successor MUST preserve:

- current `ChannelRuntime` / `InstanceRuntime` authority over local AI/spawn mutation;
- bounded pathfinding/planning as proposal-only auxiliary work with current-owner revalidation;
- bounded deterministic perception/target pipeline and stable tie-break requirements;
- no GAME-AI loot/XP/item/currency/value authority;
- DUR-04 script components as bounded proposals only;
- stable spawn/source occurrence provenance and explicit recovery class semantics;
- GAME-CHANNEL multiplicity/eligibility obligations for value-producing sources;
- controlled-actor principal/control provenance and stale-control rejection;
- mandatory resource-limit dimensions before executable acceptance;
- Reference `UNKNOWN/CONFLICT/PENDING` fail-closed behavior;
- disconnect/re-entry PvE protection as downstream legality input: protected players are temporarily ineligible for new monster offensive actions, without erasing threat/aggro/encounter state or rolling back committed effects.

## Explicitly excluded scope

- runtime implementation;
- concrete AI framework/library;
- concrete pathfinding library/algorithm;
- DDL/migrations/persistence schema;
- Platform or external repositories;
- production operations;
- coordinator-only global overlays/registers/backlog/horizon;
- GAME-ABILITY formula/effect ownership;
- GAME-INTERACTION semantics;
- Reference parity claims not backed by evidence.

## Acceptance criteria

- [x] New successor issue exists and explicitly links #261/#272.
- [x] New branch starts from trusted current `main`.
- [x] New active task records predecessor repair history without resetting it.
- [ ] GAME-AI analysis applies mandatory decision timing and removes premature FSM representation freeze if not required now.
- [ ] Candidate contract defines staged/preflighted all-or-nothing semantic-resolution atomicity.
- [ ] Candidate contract replaces one-retry freeze with policy-defined finite retry policy and hard maximum.
- [ ] Preserved predecessor decisions remain present.
- [ ] Disconnect/re-entry suppression is represented only as downstream target/action legality input.
- [ ] Draft PR exists and remains draft.
- [ ] Full successor diff is self-reviewed on exact final head with zero open material findings.
- [ ] Required exact-head CI/checks pass on the unchanged final head.
- [x] No owner-funded AI/Codex/OpenAI workflow is authorized or invoked by this worker.
- [ ] Final immutable checkpoint records exactly one next action: `ARCHITECTURE_COORDINATOR_AUDIT`.

## Readiness truth and freeze rule

Repository content MUST NOT claim `ready` before exact-head evidence exists. During authoring this task is `implementing`; after the final content mutation it becomes `validating`.

Because a commit cannot contain truthful evidence about its own future SHA/check results, the final exact-head self-review/CI outcome and any resulting `ready` transition are recorded as immutable PR/issue evidence **without moving the reviewed head**. No post-validation commit may be created merely to copy check state back into this file.

## Validation plan

### Focused

- compare the successor diff against current `main` and verify only the three owned paths changed;
- search the candidate for prohibited normative FSM/framework freeze;
- search for any `execute -> bound exceeded -> retain partial mutation` wording;
- search spawn occupancy policy for finite count/window/cadence/hard maximum and prohibition of unbounded immediate/random retry;
- verify predecessor linkage and repair count remain explicit;
- verify all preserved predecessor invariants are represented;
- verify no runtime/DDL/Platform/coordinator-overlay path changed.

### Repository / CI

Docs-only task: runtime/component E2E is `N/A` because no executable code is authorized. Repository governance/link/schema checks and the repository's always-required merge gate remain applicable and MUST be evaluated on the exact final head.

### Self-review

The worker performs a full-diff exact-head review for scope, architectural consistency, contradictory norms, missing decision timing, unsafe partial mutation, retry unboundedness, readiness truth and predecessor-history integrity. PASS requires zero unresolved material finding.

## Context checkpoint

```yaml
status: implementing
completed:
  - read #261, #272, all final review threads and coordinator BLOCKED disposition
  - read root/agent governance and decision/closeout policies
  - read FND-03, SIM-DETERMINISM-01, GAME-CHANNEL-01, DUR-04, accepted GAME-ABILITY partials and disconnect/re-entry owner decision
  - created successor issue #275
  - created branch docs/arch-c-game-ai-successor from main cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e
in_progress:
  - authoring bounded successor analysis and candidate
blocked: []
validation_pending:
  - draft PR metadata
  - full diff review
  - exact-head self-review
  - exact-head required checks
repair_cycles_for_current_gate: 5
successor_task_repair_cycles: 0
last_head_sha: null
next_action: AUTHOR_SUCCESSOR_CONTRACT
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
