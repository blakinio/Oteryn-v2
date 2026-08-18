# OTV2-20260818-crystalserver-legacy-spatial-import-v1

```yaml
task_id: OTV2-20260818-crystalserver-legacy-spatial-import-v1
title: Define CrystalServer legacy spatial import profile v1
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: architecture/OTV2-20260818-crystalserver-legacy-spatial-import-v1
pr: pending
base_sha: 16c665223c1256cc7e4a8a97cf2bc34cd278423c
owner: ChatGPT autonomous execution
created_at: 2026-08-18T09:31:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/contracts/OTERYN_CRYSTALSERVER_LEGACY_SPATIAL_IMPORT_PROFILE_V1.md
  - docs/agents/evidence/OTV2-20260818-crystalserver-legacy-spatial-import-readiness.md
  - docs/agents/tasks/active/OTV2-20260818-crystalserver-legacy-spatial-import-v1.md
public_contracts:
  - oteryn-crystalserver-legacy-spatial-import-v1
depends_on:
  - docs/contracts/OTERYN_WORLD_SPATIAL_COORDINATE_PROFILE_V1.md
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
  - blakinio/Otheryn@e417c5e7c22986bf4acef0495eb47f7b72c97cce
blocks:
  - DYN-ATLAS-001 legacy Thais Z7 coordinate/floor/presentation-order gate
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-LEGACY-IMPORT
external_repositories:
  - Oteryn/Oteryn-Atlas
  - blakinio/Otheryn
```

## Goal

Define one bounded Game-owned importer profile that maps the pinned CrystalServer/Tibia legacy spatial representation used by the historical Otheryn Atlas pipeline into `oteryn-world-spatial-v1` without making OTBM/Tibia semantics canonical.

## Acceptance criteria

- [x] Current Game main, root governance, active tasks and overlapping PRs were refreshed.
- [x] The accepted native spatial profile remains authoritative.
- [x] Legacy source revision/parser/render evidence is pinned.
- [x] Horizontal x/y mapping is explicit and representation-only.
- [x] Legacy z mapping is explicit and preserves the native vertical-order rule.
- [x] Legacy same-position visible stack order maps to explicit `PresentationOrderKey` values without consumer inference.
- [x] Container descendants are explicitly excluded from static spatial presentation ordering.
- [x] The Thais legacy regression selection has an exact native half-open rectangle/floor mapping.
- [x] Asset anchor/displacement/redistribution decisions remain separate and fail-closed.
- [ ] Exact-head repository governance/architecture checks pass.

## Architecture/evidence basis

### PROVEN

- `OTERYN_WORLD_SPATIAL_COORDINATE_PROFILE_V1` requires explicit versioned legacy conversion profiles and defines native +X east, +Y south, larger `FloorId` = geometrically higher, half-open rectangles, explicit presentation ordering, and no special meaning for floor zero.
- Otheryn legacy evidence pins CrystalServer `zimbadev/crystalserver@5e89bf8329ea406cb4ea8f4a18f32954f13e5418`, `world.otbm` SHA-256 `3bd40d14fefec41f24c4b3ae879e420be1a831ef55b95dcbec721e587a09b034`, and the historical Thais region `X=32280..32440`, `Y=32155..32305`, `Z=7`.
- Otheryn `tools/otbm_atlas/semantic.py` preserves legacy x/y/z and constructs one visible tile sequence as optional ground followed by top-level tile items in source order; nested item children are represented separately.
- Otheryn `tools/otbm_atlas/render.py` renders optional ground followed by top-level tile items, explicitly excluding nested container contents from visible map stack entries.
- The legacy renderer projects increasing x to the right and increasing y downward, matching the native profile axis orientation.

### DERIVED

- Native floor mapping `FloorId = -legacy_z` preserves the required vertical ordering without assigning any universal meaning to floor zero or treating legacy `Z=7` as canonical surface authority.
- For the observed populated legacy z-domain `0..15`, the corresponding native valid floor set is `[-15, -14, ..., -1, 0]` in strictly increasing native order.
- Legacy Thais `Z=7` maps to native `FloorId=-7`.
- Legacy inclusive Thais bounds map to native half-open `x=[32280,32441)`, `y=[32155,32306)`, `floor=-7`.
- Assigning one importer presentation plane `0` and monotonically increasing `order` over the visible legacy sequence preserves the observed reference draw order while keeping presentation identity separate from gameplay interaction/collision authority.

### UNKNOWN / deliberately deferred

- Asset pixel redistribution rights.
- A canonical Game appearance spatial-unit profile for the pinned Tibia asset set.
- Whether all future/non-CrystalServer legacy inputs can use this profile unchanged.
- Physical Game->Atlas serialization/chunking.

## Excluded scope

- no OTBM parser/runtime implementation in Game;
- no Atlas/browser implementation;
- no permanent serializer/chunk-size/floor packing decision;
- no asset redistribution;
- no production deployment;
- no reinterpretation of legacy ids as canonical Game identities;
- no collision/interaction/movement semantics.

## Validation

Documentation-only contract task. Runtime/component/E2E are `NOT_APPLICABLE` for this change; exact-head governance/architecture checks and full-diff self-review remain mandatory.

## Context checkpoint

```yaml
checkpoint_version: 1
updated_at: 2026-08-18T09:31:00+02:00
head: pending
branch: architecture/OTV2-20260818-crystalserver-legacy-spatial-import-v1
pr: pending
status: implementing
context_routes:
  - architecture
  - agent-governance
  - testing
owned_paths:
  - docs/contracts/OTERYN_CRYSTALSERVER_LEGACY_SPATIAL_IMPORT_PROFILE_V1.md
  - docs/agents/evidence/OTV2-20260818-crystalserver-legacy-spatial-import-readiness.md
  - docs/agents/tasks/active/OTV2-20260818-crystalserver-legacy-spatial-import-v1.md
proven:
  - Native Game spatial semantics are accepted in oteryn-world-spatial-v1.
  - Legacy Otheryn source/parser/render evidence is pinned and preserves source x/y/z plus visible top-level item sequence.
derived:
  - FloorId = -legacy_z preserves native vertical order and maps Thais legacy Z7 to FloorId -7.
unknown:
  - asset rights and appearance spatial-unit profile
conflicts: []
first_failure:
  marker: dyn-atlas-legacy-import-profile-missing
  evidence: DYN-ATLAS-001 cannot promote legacy Z7/source order into native semantic fixture without a Game-owned importer profile
rejected_hypotheses:
  - use legacy z and item order directly as Atlas authority
  - define legacy z=7 as universal native floor zero
  - copy Tibia assets as part of this contract task
changed_paths: []
validation:
  - command: live Game/Otheryn/Atlas authority preflight
    result: PASS
    evidence: pinned revisions and no overlapping Game task/PR found
blockers: []
next_action: add the bounded importer contract and readiness evidence, then open a draft PR and run exact-head checks
```

## Source branch closeout

```yaml
source_branch_disposition: auto_delete_after_merge
source_branch_reason: ordinary same-repository contract task
source_branch_evidence: pending
```
