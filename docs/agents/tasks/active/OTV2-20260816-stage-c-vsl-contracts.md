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
updated_at: 2026-08-16T21:23:32+02:00
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
depends_on:
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/architecture/FND-03_RUNTIME_EXECUTION_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/DUR-03_ITEM_TRANSACTION_AND_ANTI_DUPLICATION_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
  - docs/architecture/GAME-CHANNEL-01_CHANNEL_PRODUCT_POLICY_CONTRACT.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_OWNER_BASELINE.md
  - docs/architecture/GAME-ABILITY-01_WHOLE_GATE_OWNER_ACCEPTANCE_BASELINE.md
  - docs/architecture/OTERYN_V2_REMAINING_FIRST_WAVE_OWNER_ACCEPTANCE_BASELINE_20260816.md
  - docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
  - docs/architecture/ADR-0007-native-end-to-end-test-platform.md
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
- `PROVEN` — FND-02 already owns CommandRef, connection-generation fencing, server sequencing, state-domain revisions and snapshot/delta/resync semantics.
- `PROVEN` — DUR-03 owns durable item/value creation/location/transfer/idempotency; a runtime ground/corpse projection is never a second durable value authority.
- `PROVEN` — DUR-04 forbids selecting the final World Project/World Bundle physical encoding before its bounded format spike/benchmark evidence.
- `PROVEN` — Reference ABILITY_COMBAT evidence remains 0/4 promoted and fail closed; exact Global formulas/mechanics cannot be invented for the slice.
- `PROVEN` — current status/register identify `VSL-MOVE-01`, `VSL-COMBAT-01` and `VSL-CONTENT-01` as unaccepted gates that block their corresponding executors.

## Architecture strategy

```text
freeze authority / identity / commit / recovery / evidence boundaries
use explicit non-shipping fixtures where target values are unknown
measure reversible physical technology
then refine
```

The slice contracts do not reopen accepted foundation/gameplay architecture or absorb later alpha/expansion systems.

## Candidate results

### VSL-MOVE-01

Candidate names the current ChannelRuntime/InstanceRuntime as the sole local movement/relocation authority; distinguishes local step/local relocation from scope handoff; uses source-derived revision-bound occurrence identity; composes post-movement/stateful triggers with GAME-INTERACTION; derives bounded visibility/interest as server state under FND-02 reconciliation; and leaves exact Reference movement/LOS/timing evidence-gated.

### VSL-COMBAT-01

Candidate keeps GAME-ABILITY as the only combat effect pipeline; defines stable creature death identity; treats corpse as runtime projection while durable loot materializes through DUR-03; gives single-principal XP settlement to GAME-CHAR progression authority; uses GAME-INTERACTION + DUR-03 for retry-safe pickup; and permits only explicit non-shipping structural fixture profiles while Reference values remain unknown.

### VSL-CONTENT-01

Candidate freezes the minimum semantic content/compiler/projection/loader/activation seam needed by movement/combat and permits a bounded noncanonical VSL fixture/evidence artifact profile. It explicitly preserves DUR-04's mandatory format spike and later owner format-selection decision before permanent physical encoding.

## Acceptance criteria

- [x] Each contract states exact authority and identity boundaries.
- [x] Each contract applies mandatory decision timing.
- [x] Cross-domain effects use accepted owner operations/workflows; no distributed transaction is invented.
- [x] All unproven Reference values remain evidence-gated.
- [x] Resource ceilings required before implementation acceptance are explicit dimensions, not invented numbers.
- [x] VSL-CONTENT preserves DUR-04 physical-format spike requirement.
- [x] Real-boundary Tier 1/Tier 2 proof requirements are explicit and do not allow mocks to count as terminal evidence.
- [x] One owner-decision package presents `ACCEPT | REWORK | DEFER` for all three gates and recommends `ACCEPT` without inferring acceptance.
- [ ] Exact-head five-path full-diff self-review is clean.
- [ ] Agent governance / Architecture semantic audit / Merge authority audit / `Merge gate / validate` pass on one unchanged final head.
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
last_progress: three Stage-C candidates plus bundled owner-decision package persisted; draft PR #311 opened
status: validating
branch: docs/stage-c-vsl-contracts-20260816
issue: 310
pr: 311
base_sha: bf2a2ae279516f62626a5d8f4dc1aeb587535c62
owner_action_required: null until exact-head validation is complete
blocker: null
next_action: inspect full five-path diff, repair any material finding, freeze exact head, obtain required draft CI, then ask for one bundled owner disposition
executor_prompts: HOLD
```

`IMPLEMENTATION_AUTHORITY: NONE`
