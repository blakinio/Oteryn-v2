# OTV2-20260812-foundation-handoff-refresh

```yaml
task_id: OTV2-20260812-foundation-handoff-refresh
title: Refresh canonical foundation handoff for successor agent
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260812-foundation-handoff-refresh
pr: null
base_sha: 22b64e1b20cf2220828f5a3d47b30df29f9a60b6
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-12T10:20:00+02:00
updated_at: 2026-08-12T10:20:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-foundation-handoff-refresh.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/agents/reports/OTV2-20260812-foundation-handover.md
public_contracts: []
depends_on:
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md
  - docs/architecture/DUR-02_PROFILE_NEUTRAL_CHARACTER_PERSISTENCE_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_OWNER_BASELINE.md
  - docs/architecture/GAME-VISION-01_MINIMUM_OWNER_BASELINE.md
  - docs/agents/PROMPTING_HANDOVER.md
  - docs/agents/CONTEXT_HANDOFF.md
blocks: []
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Persist a self-contained successor-agent handoff after whole `DUR-02 — Persistence v1` became `ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED`, and repair stale programme/prompt text that could otherwise send a new agent back to already completed foundation gates.

This task does **not** authorize or implement Rust server/runtime code, PostgreSQL DDL/migrations, Platform writes, production changes or external-repository writes.

## PROVEN preflight

- trusted base: `main@22b64e1b20cf2220828f5a3d47b30df29f9a60b6`;
- whole DUR-02 owner acceptance delivery: PR #201 / merge `ec4b840b0742967370a4235d87094b29a802fe28`;
- whole DUR-02 lifecycle closeout: PR #202 / current main `22b64e1b20cf2220828f5a3d47b30df29f9a60b6`;
- open PR #191 is a disjoint GAME-CHAR provenance erratum and remains untouched;
- open PR #162 is disjoint CI/governance work and remains untouched;
- active lag/disconnect architecture checkpoints do not own the handoff/programme/prompt paths touched here;
- the non-owning foundation programme checkpoint is stale and still names pre-GAME-VISION/pre-GAME-CHAR/pre-DUR-02 work as current;
- the global coordinator prompt is materially stale and still describes FND-01 as the immediate gate.

## Acceptance criteria

- [ ] Add one self-contained handoff report that can replace chat history for the next agent.
- [ ] Record exact trusted main SHA and recent binding PR/merge evidence.
- [ ] Record current accepted architecture and remaining `NOT_STARTED` implementation state truthfully.
- [ ] Record that no server/runtime/DDL implementation authority has been granted in this handoff.
- [ ] Refresh the non-owning foundation programme checkpoint to current accepted state and exactly one executable `next_action`.
- [ ] Refresh the global architecture coordinator continuation prompt so it starts from current main rather than FND-01-era assumptions.
- [ ] Preserve GAME-ITEM-01/DUR-03 as the item/currency/value conservation path.
- [ ] Preserve GAME-CHANNEL-01, DUR-04, SIM-DETERMINISM-01 and Reference evidence work as separate gates.
- [ ] Preserve open PR #191/#162 and active lag/disconnect tasks without mutation.
- [ ] Complete exact-head self-review and repository-required documentation CI before squash merge.
- [ ] Archive this bounded handoff-refresh task and release ownership after merge.

## Excluded scope

- no Rust game-server implementation;
- no PostgreSQL DDL or migration files/execution;
- no transport listener/codec/runtime implementation;
- no FND-04 runtime/session/lease implementation;
- no item/currency/value persistence or DUR-03 implementation;
- no new gameplay/product semantic acceptance;
- no Platform/external-repository writes;
- no production deployment or live configuration.

## Validation

### Focused

- full diff review for stale-state removal and preservation of current accepted status;
- verify the handoff contains one exact `next_action` and no ambiguous implementation authority;
- runtime/component/E2E: `NOT_APPLICABLE` because this delivery changes only documentation/coordination state.

### Exact-head CI

Require Agent Governance, Dependency Review and CodeQL/documentation checks on the final unchanged PR head.

## Independent review

`NOT_REQUIRED` unless final diff changes semantic architecture/authority. This package should only refresh coordination/handoff text and must not expand runtime, production or repository authority.

## Context checkpoint

```yaml
status: implementing
branch: docs/OTV2-20260812-foundation-handoff-refresh
head_sha: null
pr: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-foundation-handoff-refresh.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/agents/reports/OTV2-20260812-foundation-handover.md
public_contracts: []
last_progress: Fresh handoff-refresh task claimed from main after whole DUR-02 lifecycle closeout.
validation_state: pending
 audit_state: pending self-review
 e2e_state: NOT_APPLICABLE documentation-only
ci_generation: null
run_ids: []
counters:
  repair_cycles: 0
  unchanged_state_checks: 0
blocker: null
next_action: Write the successor-agent handoff report and refresh the stale non-owning programme checkpoint and continuation prompt to the current accepted state without granting implementation authority.
```
