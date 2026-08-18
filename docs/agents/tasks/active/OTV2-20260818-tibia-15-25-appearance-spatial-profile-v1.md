# OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1

```yaml
task_id: OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1
title: Define Tibia 15.25 appearance spatial profile v1
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: architecture/OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1
pr: pending
base_sha: ade3005cdf9ad6daeb87dc20a6546d5c29ee61da
owner: ChatGPT autonomous execution
created_at: 2026-08-18T09:51:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/contracts/OTERYN_TIBIA_15_25_APPEARANCE_SPATIAL_PROFILE_V1.md
  - docs/agents/evidence/OTV2-20260818-tibia-15-25-appearance-spatial-readiness.md
  - docs/agents/tasks/active/OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1.md
public_contracts:
  - oteryn-tibia-15-25-appearance-spatial-v1
depends_on:
  - docs/contracts/OTERYN_WORLD_SPATIAL_COORDINATE_PROFILE_V1.md
  - docs/contracts/OTERYN_CRYSTALSERVER_LEGACY_SPATIAL_IMPORT_PROFILE_V1.md
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
  - blakinio/Otheryn@e417c5e7c22986bf4acef0495eb47f7b72c97cce
blocks:
  - DYN-ATLAS-001 appearance anchor/footprint/displacement gate
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-APPEARANCE
external_repositories:
  - Oteryn/Oteryn-Atlas
  - blakinio/Otheryn
```

## Goal

Define the smallest Game-owned appearance spatial profile required for `DYN-ATLAS-001` using the exact owner-authorized Tibia client package, without promoting Tibia asset files or the legacy renderer into canonical World authority.

## Acceptance criteria

- [x] Exact asset archive digest and package metadata verified directly.
- [x] Package version identified from `package.json` as `15.25.bd5a04`, not 15.32.
- [x] Catalog/appearance digests and deterministic object/sprite counts recorded.
- [x] Pinned Otheryn decoder/renderer behavior used only as source-conversion evidence.
- [x] `units_per_tile`, anchor, footprint and effective displacement mapping explicit.
- [x] Concrete frame/phase/layer/sprite resolution remains producer-owned and explicit to Atlas.
- [x] Asset IDs remain provenance/source IDs rather than canonical Game entity identity.
- [x] Owner rights attestation is scoped to the exact archive digest and labelled as owner-supplied evidence.
- [x] Permanent GPU packing, serializer/chunk format and final animation contract remain deferred.
- [x] Full owned-path semantic self-review finds no unresolved authority/scope finding before CI.
- [ ] Exact-head repository governance/architecture/merge checks pass.

## Evidence classification

### PROVEN

- Owner-supplied archive SHA-256 is `01c45146e2fcec3f4087844e0cbc1817fb1d60b310a35ac5d88c07aab6f73d1a`.
- Root package metadata reports version `15.25.bd5a04`.
- Direct hashing records package/catalog/appearance digests in the readiness evidence.
- Direct decoding yields 42,107 object appearances, 4,927 sprite sheets and 75,623 unique sprite IDs referenced by object appearances, matching pinned legacy Otheryn evidence.
- Pinned legacy renderer uses a 32-pixel tile scale and subtracts multi-tile excess, shift and height from the source draw origin.

### DERIVED

- `units_per_tile=32` is the bounded native spatial unit mapping for this source profile.
- The owning tile is mapped as the south-east/bottom-right anchor cell; larger sprite footprints extend west/north.
- Effective native displacement is `(-(shift_x + height), -(shift_y + height))`.
- Atlas should receive producer-resolved concrete primitives rather than reproduce legacy subtype/pattern/animation heuristics.

### UNKNOWN / deliberately deferred

- final generalized animation contract beyond the bounded static proof;
- permanent Game -> Atlas physical serializer/chunk profile;
- production asset CDN/GPU packing.

## Rights boundary

Owner attestation authorizes decoding, derivation, rendering, deduplication and publication of the exact asset archive digest for public Oteryn Atlas use. This task does not claim independent third-party copyright verification and does not extend the authorization to another digest.

## Validation

Focused archive inspection and deterministic metadata decoding: **PASS**.

Runtime/component/E2E: **NOT_APPLICABLE** for this documentation-only Game semantic contract. The downstream fixture/export and Atlas renderer tasks own executable evidence.

Full three-file semantic/scope self-review: **PASS**, zero unresolved material findings before exact-head CI.

## Context checkpoint

```yaml
checkpoint_version: 1
updated_at: 2026-08-18T09:51:00+02:00
head: pending
branch: architecture/OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1
pr: pending
status: validating
context_routes:
  - architecture
  - agent-governance
  - testing
owned_paths:
  - docs/contracts/OTERYN_TIBIA_15_25_APPEARANCE_SPATIAL_PROFILE_V1.md
  - docs/agents/evidence/OTV2-20260818-tibia-15-25-appearance-spatial-readiness.md
  - docs/agents/tasks/active/OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1.md
proven:
  - exact owner-supplied asset archive is Tibia client package 15.25.bd5a04 with reconciled legacy Atlas counts
  - pinned renderer evidence establishes the bounded 32-pixel source projection behavior
derived:
  - source profile maps anchor/footprint/displacement into explicit native appearance semantics
unknown:
  - bounded Game Thais semantic export artifact remains the next implementation dependency
conflicts: []
first_failure:
  marker: dyn-atlas-appearance-profile-missing
  evidence: Atlas could not truthfully preserve anchor/footprint/displacement without Game-owned source conversion semantics
rejected_hypotheses:
  - treat archive as 15.32 based on assumption
  - let Atlas reimplement legacy asset heuristics as authority
  - generalize owner attestation to unrelated asset archives
changed_paths:
  - docs/contracts/OTERYN_TIBIA_15_25_APPEARANCE_SPATIAL_PROFILE_V1.md
  - docs/agents/evidence/OTV2-20260818-tibia-15-25-appearance-spatial-readiness.md
  - docs/agents/tasks/active/OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1.md
validation:
  - command: direct asset archive/package/catalog/appearance verification
    result: PASS
    evidence: exact digests, version, appearance/sprite counts recorded in readiness evidence
  - command: runtime/component/E2E
    result: NOT_APPLICABLE
    evidence: documentation-only Game semantic contract; executable proof belongs to downstream fixture/Atlas tasks
blockers: []
next_action: open draft PR, review exact three-file diff and require exact-head governance/architecture/merge checks before squash merge
```

## Source branch closeout

```yaml
source_branch_disposition: auto_delete_after_merge
source_branch_reason: ordinary same-repository contract task
source_branch_evidence: pending
```
