# OTV2-20260818-world-spatial-coordinate-profile-v1

```yaml
task_id: OTV2-20260818-world-spatial-coordinate-profile-v1
title: Freeze canonical World spatial / coordinate profile v1
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: architecture/OTV2-20260818-world-spatial-coordinate-profile-v1
pr: 327
base_sha: 5577f6fc7c1f7ddef482f0f7b08039047704e36b
head_sha: 2d8a4ee4e46578849db27d9248adee83fb3634de
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT autonomous execution
created_at: 2026-08-18T06:39:00+02:00
updated_at: 2026-08-18T06:47:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/contracts/OTERYN_WORLD_SPATIAL_COORDINATE_PROFILE_V1.md
  - docs/agents/evidence/OTV2-20260818-game-atlas-coordinate-profile-readiness.md
  - docs/agents/tasks/active/OTV2-20260818-world-spatial-coordinate-profile-v1.md
public_contracts:
  - oteryn-world-spatial-v1
depends_on:
  - docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
  - docs/agents/evidence/OTV2-20260816-game-atlas-physical-profile-readiness.md
blocks:
  - first executable Game -> Atlas physical-profile decision
  - DYN-ATLAS-001 coordinate/floor/order preflight gate
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-SPATIAL
external_repositories:
  - blakinio/Oteryn-Platform (read-only programme authority/evidence)
  - future Oteryn-Atlas (repository coordinate UNKNOWN)
```

## Outcome

Merge one bounded Game-owned semantic spatial profile that gives native World/Content, Game -> Atlas export and later Atlas consumers explicit coordinate axes, bounds, floors/order, same-position presentation ordering and anchor/displacement semantics without promoting OTBM/Tibia/client projection conventions or a physical serializer into canonical authority.

## Architecture and source of truth

- **PROVEN:** ADR-0005 owns the native World/Content model and keeps OTBM behind bounded importer/Legacy IR boundaries.
- **PROVEN:** `OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md` requires an explicit `coordinate_profile` before executable producer/consumer compatibility.
- **PROVEN:** `OTV2-20260816-game-atlas-physical-profile-readiness.md` records `EVIDENCE_GAP` and names the exact missing spatial semantics.
- **PROVEN:** targeted preflight searches returned no open Atlas/spatial/coordinate PR or Issue, and the inspected active-task inventory exposed no task owning the target paths.
- **DERIVED:** a semantic profile can close this authority gap while leaving serializer/chunk/resource-limit decisions evidence-gated.
- **UNKNOWN:** the physical `Oteryn-Atlas` implementation repository remains unavailable/unproven and is not created or assumed by this task.

## Acceptance criteria

- [ ] One Game-owned profile defines horizontal axes/orientation and discrete coordinate numeric domain.
- [ ] Per-world bounds and point/rectangle inclusion are explicit and unambiguous.
- [ ] Floor identity/domain/order are explicit without copying legacy `z` semantics.
- [ ] Same-position presentation ordering is explicit and fail-closed for duplicates.
- [ ] Anchor/footprint/displacement meaning is explicit and renderer-resolution independent.
- [ ] Legacy import requires an explicit versioned mapping and cannot directly promote OTBM/Tibia conventions.
- [ ] Serializer, compression, permanent chunk size/floor packing and production resource ceilings remain deferred.
- [ ] DYN-ATLAS readiness evidence truthfully distinguishes the closed coordinate-semantic gate from remaining Atlas-repository/fixture/assets/physical-profile gates.
- [ ] Full changed-file self-review finds no authority expansion outside this bounded Game contract.
- [ ] Exact-head documentation/governance merge gate passes.

## Excluded scope

- no Rust/runtime implementation;
- no World Project / World Bundle physical serializer;
- no Atlas browser implementation;
- no OTBM parser/importer implementation;
- no legacy Tibia `z=7` mapping decision;
- no chunk-size/floor-packing production decision;
- no asset redistribution or licensing decision;
- no production/staging/deployment mutation;
- no Platform/Otheryn writes;
- no repository create/rename/transfer/extraction.

## Implementation / findings

The profile is intentionally semantic. It uses explicit native Oteryn coordinates and ordering while requiring future legacy adapters to state their mapping. Historical `EVIDENCE_GAP` evidence remains immutable; a new readiness delta records the closure condition after merge.

Material design choices:

- signed `i32` horizontal tile coordinates;
- +X east/right and +Y south/down in canonical north-up projection;
- finite per-world half-open bounds with `i64` semantic bounds values so the full `i32` position domain can be represented without positive-edge overflow;
- signed `i16` canonical `FloorId`, with larger values higher/above, no universal meaning for floor zero and an explicit valid floor set;
- half-open rectangular inclusion;
- unique `(i32 plane, u32 order)` same-position presentation keys;
- explicit anchor-relative footprint offsets;
- presentation displacement direction/meaning fixed by the world profile while precision is bound by an explicit versioned appearance/asset `units_per_tile` profile rather than frozen here.

The profile does not assign concrete world extents or a legacy source-floor mapping.

### Self-review repair before final-head freeze

Initial PR head `2d8a4ee4e46578849db27d9248adee83fb3634de` exposed two material design defects during full semantic review:

1. half-open bounds encoded with the same `i32` type as positions could not represent an exclusive upper edge after `i32::MAX`;
2. hard-coding `1/256 tile` displacement precision unnecessarily froze an asset/render detail without evidence.

The repair widens only the semantic bounds envelope to `i64` while retaining `i32` positions, removes any universal special meaning from floor zero, widens presentation order fields to avoid a premature tight semantic ceiling, and moves displacement precision into a required versioned appearance/asset `units_per_tile` profile. These changes preserve the required direction/anchor semantics while keeping physical/render precision evidence-gated.

## Validation

### Focused

- command/run: GitHub exact changed-path/diff inspection plus repository governance validation selected by PR merge gate
- result: in progress; initial semantic self-review produced the repair above

### Component/integration

- command/run: `NOT_APPLICABLE` — documentation-only semantic contract; no executable component changes
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime/browser behavior is implemented by this task
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull request to `main`
- workflow/run/job: pending
- runner assignment: pending
- classification: architecture/contracts-only
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent
- material findings: two pre-freeze design findings repaired; final pass pending
- verdict: pending

## Independent review

- required: `NO` — bounded documentation-only semantic contract under existing ADR/export authority; no runtime, protocol wire, persistence, auth/security, production or authority-relaxation implementation changes. Owner explicitly authorized this blocking architecture task; exact-head self-review and normal merge gate remain mandatory.
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: 3 owned paths; final post-repair inspection pending
- unresolved review threads: pending
- related/superseded PRs: none found at preflight
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: PR #327 opened; semantic self-review found and prepared bounds/displacement/floor/order repair
status: implementing
branch: architecture/OTV2-20260818-world-spatial-coordinate-profile-v1
head_sha: 2d8a4ee4e46578849db27d9248adee83fb3634de
pr: 327
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: initial
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 1
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: commit the bounded semantic repair, then perform exact changed-path/full-diff self-review
```
