# OTV2-20260816-stage-c-vsl-contracts

```yaml
task_id: OTV2-20260816-stage-c-vsl-contracts
title: Close Stage-C movement, combat and content vertical-slice architecture
mode: COORDINATE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/stage-c-vsl-contracts-20260816
issue: 310
pr: 311
base_sha: bf2a2ae279516f62626a5d8f4dc1aeb587535c62
owner: Architecture Coordinator
created_at: 2026-08-16T21:16:12+02:00
updated_at: 2026-08-16T21:25:08+02:00
execution_budget_minutes: 120
owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-stage-c-vsl-contracts.md
  - docs/architecture/VSL-MOVE-01_MINIMAL_MOVEMENT_VISIBILITY_CONTRACT_CANDIDATE.md
  - docs/architecture/VSL-COMBAT-01_MINIMAL_COMBAT_DEATH_LOOT_CONTRACT_CANDIDATE.md
  - docs/architecture/VSL-CONTENT-01_MINIMAL_NATIVE_CONTENT_SLICE_CONTRACT_CANDIDATE.md
  - docs/architecture/OTERYN_V2_STAGE_C_VSL_OWNER_DECISION_PACKAGE_20260816.md
public_contracts:
  - docs/architecture/VSL-MOVE-01_MINIMAL_MOVEMENT_VISIBILITY_CONTRACT_CANDIDATE.md
  - docs/architecture/VSL-COMBAT-01_MINIMAL_COMBAT_DEATH_LOOT_CONTRACT_CANDIDATE.md
  - docs/architecture/VSL-CONTENT-01_MINIMAL_NATIVE_CONTENT_SLICE_CONTRACT_CANDIDATE.md
  - docs/architecture/OTERYN_V2_STAGE_C_VSL_OWNER_DECISION_PACKAGE_20260816.md
blocks:
  - explicit owner dispositions for VSL-MOVE-01, VSL-COMBAT-01, VSL-CONTENT-01
  - final lifecycle/current-status reconciliation
  - executor-prompt handoff audit
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Close only the minimum Stage-C architecture needed so implementation agents can build the first real-boundary movement/combat/content vertical slice without making architecture decisions inside code.

## Trusted starting state

- `PROVEN` — `main@bf2a2ae279516f62626a5d8f4dc1aeb587535c62` contains owner-accepted GAME-ABILITY, GAME-INTERACTION, ALPHA-CLIENT, GAME-AI and ANL-02/03 architecture.
- `PROVEN` — FND-03 already makes current `ChannelRuntime` / `InstanceRuntime` the owner of local position, visibility, creatures, combat, transient effects and ground/corpse runtime state.
- `PROVEN` — FND-02 owns CommandRef, connection-generation fencing, server sequencing, state-domain revisions and snapshot/delta/resync semantics.
- `PROVEN` — DUR-03 owns durable item/value creation/location/transfer/idempotency; a runtime ground/corpse projection is never a second durable value authority.
- `PROVEN` — DUR-04 forbids selecting the final World Project/World Bundle physical encoding before its bounded format spike/benchmark evidence.
- `PROVEN` — Reference ABILITY_COMBAT evidence remains 0/4 promoted and fail closed; exact Global formulas/mechanics cannot be invented for the slice.
- `PROVEN` — current status/register identify `VSL-MOVE-01`, `VSL-COMBAT-01` and `VSL-CONTENT-01` as unaccepted gates that block their corresponding executors.

## Candidate result

### VSL-MOVE-01

Current ChannelRuntime/InstanceRuntime remains the sole local movement/relocation authority; local step/local relocation is distinct from scope handoff; occurrence identity is source-derived and revision-bound; post-movement/stateful triggers compose with GAME-INTERACTION; visibility/interest is bounded server state under FND-02 reconciliation; exact Reference movement/LOS/timing stays evidence-gated.

### VSL-COMBAT-01

GAME-ABILITY remains the only effect pipeline; one stable creature-death descendant feeds separate idempotent DUR-03 loot and GAME-CHAR XP workflows; pickup uses GAME-INTERACTION + DUR-03; no distributed death/loot/XP transaction is invented; explicit non-shipping fixture profiles allow structural proof without guessing Reference formulas/rates.

### VSL-CONTENT-01

The slice freezes the minimum canonical semantic graph/compiler/projection/loader/activation seam and permits a bounded noncanonical VSL fixture/evidence artifact profile. DUR-04's required final-format spike and later owner format decision remain mandatory before permanent physical encoding.

## Review/repair history

- Initial draft exact head `54cfa3325027825b6b792409b013809208ff33e6`:
  - Architecture semantic audit `31967471644`: **PASS**;
  - Merge authority audit `31967471656`: **PASS**;
  - Agent governance `31967471554`: **FAIL — metadata only**.
- Exact governance finding from job `95214731885`: PR title exceeded the repository 72-character limit.
- Repair: PR #311 title changed from `docs(architecture): define Stage-C movement combat content slice contracts` to `docs(architecture): define Stage-C VSL contracts`.
- No Stage-C semantic file changed for that metadata finding.
- This task-truth checkpoint intentionally creates the next exact-head generation so fresh governance/merge checks consume the repaired metadata; it is not a no-op CI trigger.

## Acceptance criteria

- [x] Each contract states exact authority and identity boundaries.
- [x] Each contract applies mandatory decision timing.
- [x] Cross-domain effects use accepted owner operations/workflows; no distributed transaction is invented.
- [x] All unproven Reference values remain evidence-gated.
- [x] Resource ceilings required before implementation acceptance are explicit dimensions, not invented numbers.
- [x] VSL-CONTENT preserves DUR-04 physical-format spike requirement.
- [x] Real-boundary Tier 1/Tier 2 proof requirements are explicit and do not allow mocks to count as terminal evidence.
- [x] One owner-decision package presents `ACCEPT | REWORK | DEFER` for all three gates and recommends `ACCEPT` without inferring acceptance.
- [ ] Exact-head five-path full-diff self-review is clean on the post-metadata-repair generation.
- [ ] Fresh Agent governance / Architecture semantic audit / Merge authority audit / `Merge gate / validate` pass on one unchanged final head.
- [ ] Zero unresolved review threads/requested changes and `behind_by=0` before owner handoff.

## Hard exclusions

No runtime/client/server/protocol/content implementation; no PostgreSQL DDL/migration; no final World Project/Bundle physical encoding; no concrete movement/pathfinding/renderer/database framework; no exact Global movement/combat/loot/XP formula; no PvP/party/boss/quest/NPC/market breadth; no Platform write; no production/deployment; no entitlement work; no Codex/OpenAI/paid review without exact current authorization.

## Executor state

```text
EXECUTOR_PROMPTS: HOLD
IMPLEMENTATION_AUTHORITY: NONE
```

## Context checkpoint

```yaml
last_progress: Stage-C semantic audit passed; metadata-only title-length failure repaired; this checkpoint starts fresh exact-head validation generation
status: validating
branch: docs/stage-c-vsl-contracts-20260816
issue: 310
pr: 311
owner_action_required: null until fresh exact-head validation is complete
blocker: null
next_action: run fresh exact-head governance/semantic/merge checks, complete full-diff self-review/thread/drift check, then request one bundled owner disposition
executor_prompts: HOLD
```

`IMPLEMENTATION_AUTHORITY: NONE`
