# OTV2-20260805-world-format-and-studio-contract

```yaml
task_id: OTV2-20260805-world-format-and-studio-contract
title: Define the native world format and Oteryn Studio contract
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/world-format-studio-20260805
pr: null
base_sha: 27f6f930285621e5714b8b12af03a684ac9f2e1b
head_sha: null
owner: chatgpt-github-agent
created_at: 2026-08-05T11:32:00+02:00
updated_at: 2026-08-05T11:32:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/agents/REPOSITORY_MAP.md
  - README.md
  - docs/agents/tasks/active/OTV2-20260805-world-format-and-studio-contract.md
public_contracts:
  - docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
depends_on:
  - ADR-0001 native Rust and multichannel baseline
  - ADR-0002 canonical repository ownership
blocks:
  - native map/content/editor implementation
  - broad OTBM and legacy content migration
cross_repository_coordination_id: OTV2-NATIVE-WORLD-CONTENT
external_repositories:
  - blakinio/Otheryn
  - blakinio/otclient
  - opentibiabr/remeres-map-editor
  - beats-dh/Beats-Assets-Editor
```

## Outcome

Persist the owner-approved direction for a greenfield Oteryn world/content format, one integrated Oteryn Studio application and legacy OTBM/content conversion boundaries.

The accepted architecture must distinguish player-facing spatial semantics from technical streaming partitions and must provide a precise event-placement hierarchy suitable for Echo-Raid-like mechanics without making oversized subareas the runtime execution boundary.

## Architecture and source of truth

### PROVEN

- Oteryn v2 is a greenfield native Rust stack and does not use `protocol-canary` as its target runtime.
- The repository currently contains architecture/governance only and no implemented world format or editor.
- Remere's Map Editor is a mature behavioral reference for legacy OTBM map editing.
- Beats Assets Editor is a modern Rust/Tauri/Svelte reference for asset/content workflows rather than a complete native Oteryn world editor.

### ACCEPTED OWNER DIRECTION

- Build the native Oteryn world format from zero rather than evolving or hybridizing OTBM.
- Treat OTBM and other legacy formats as conversion inputs and, where practical, constrained export targets.
- Build one integrated Oteryn Studio for maps, sprites/appearances, items and related content.
- Use Remere's Map Editor and Beats Assets Editor as functional references, migration oracles and fixture producers; do not make them runtime dependencies or silently copy license-restricted code/assets.
- Model `Area` and `Subarea` as logical/player-facing geography independent of technical `Region` and `Chunk` boundaries.
- Add `EncounterZone`, `RaidCell` and `RaidAnchor` so dynamic encounters can target safe, precise areas within a large logical subarea.

## Acceptance criteria

- [ ] ADR records the native editable project, canonical world model and compiled runtime bundle.
- [ ] ADR records one integrated Oteryn Studio and its map, asset, content, validation and preview responsibilities.
- [ ] ADR records stable content keys and compiled runtime IDs.
- [ ] ADR separates static source content from dynamic PostgreSQL runtime state.
- [ ] ADR defines `Area`, `Subarea`, `Zone`, `Region`, `Chunk`, `EncounterZone`, `RaidCell` and `RaidAnchor` responsibilities.
- [ ] ADR defines safe encounter placement, compile-time eligibility masks and runtime selection policy.
- [ ] ADR defines OTBM/legacy import through a bounded intermediate representation and conversion report.
- [ ] ADR records licensing/provenance restrictions for reference tools and imported assets.
- [ ] Foundation backlog reflects accepted world-format direction while leaving scripting specifics open.
- [ ] README and repository map route future agents to the ADR.
- [ ] Governance/document validation passes on the exact final head.
- [ ] Independent full-diff audit has no open material finding.
- [ ] PR is squash-merged and the task is archived.

## Excluded scope

- no Rust workspace or editor implementation;
- no parser, compiler, renderer or server runtime code;
- no writes to external repositories;
- no proprietary Tibia/CipSoft assets;
- no final scripting-language choice;
- no final chunk dimensions before benchmarks;
- no claim of lossless round-trip export for Oteryn-native features.

## Implementation / findings

Pending.

## Validation

### Focused

- command/run: governance/document validation
- result: pending

### Component/integration

- result: `NOT_APPLICABLE` — architecture-only task with no executable workspace

### E2E

- result: `NOT_APPLICABLE` — no runtime/editor implementation in this task

### Exact-head CI

- head: pending
- workflow/run: `Agent governance`, pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial architecture and full-diff review
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none known
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Dedicated branch and architecture task created from exact main head.
status: implementing
branch: docs/world-format-studio-20260805
head_sha: null
pr: null
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Add ADR-0005 with the complete native world format and Oteryn Studio contract.
```
