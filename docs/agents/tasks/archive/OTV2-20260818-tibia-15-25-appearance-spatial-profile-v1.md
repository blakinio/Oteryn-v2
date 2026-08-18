# OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1 — COMPLETED

```yaml
task_id: OTV2-20260818-tibia-15-25-appearance-spatial-profile-v1
title: Define Tibia 15.25 appearance spatial profile v1
mode: CONTRACT
status: completed
repository: blakinio/Oteryn-v2
pr: 331
base_sha: ade3005cdf9ad6daeb87dc20a6546d5c29ee61da
final_head_sha: 819f14306c9dc26fd5b25da56f460f4cf7c92a8d
merge_sha: f90b99bee9567800a430ca1a703843d647dc01b8
closed_at: 2026-08-18T10:04:00+02:00
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-APPEARANCE
public_contracts:
  - oteryn-tibia-15-25-appearance-spatial-v1
```

## Terminal result

PR #331 merged the bounded Game-owned appearance presentation profile for the exact owner-authorized Tibia client asset archive.

Direct source verification established the fixture as **15.25.bd5a04**, not 15.32, with archive SHA-256 `01c45146e2fcec3f4087844e0cbc1817fb1d60b310a35ac5d88c07aab6f73d1a`.

The accepted profile defines:

- `units_per_tile = 32`;
- owning tile as the south-east/bottom-right **visual anchor cell** for the bounded legacy presentation mapping;
- decoded sprite visual coverage extending west/north by integral tile units;
- effective 2D presentation displacement `(-(shift_x + height), -(shift_y + height))`;
- explicit producer ownership of concrete frame/phase/layer/sprite resolution;
- a hard boundary that pixel-derived visual coverage is **not** gameplay occupancy, collision, movement blocking, item ownership or interaction area;
- source appearance/sprite IDs as provenance identifiers, not canonical Game entity identity.

## Evidence

Direct deterministic archive inspection recorded:

- package version `15.25.bd5a04`;
- package SHA-256 `01c405e8f72bc4bbf2009052cdccc10510a5664ab8b81713b78c804422c3db3b`;
- catalog SHA-256 `93ea5888174ef44b352d7c2b1f8061573a4a260bfaba4b7ec32ea836b9e411ab`;
- appearance SHA-256 `aa44a154f30c7ed59acc25f246286396e4043851ef0b54ef3cf3951e46d1ce50`;
- 42,107 object appearances;
- 4,927 sprite sheets;
- 75,623 unique object-referenced sprite IDs.

These counts reconcile with the pinned Otheryn 15.25 legacy Atlas evidence.

Owner rights evidence is intentionally classified as `OWNER_ATTESTED / PROJECT_AUTHORIZED` for the exact archive digest, not independently verified third-party copyright ownership.

## Self-review

The first contract draft used `footprint` for pixel-derived sprite coverage. Self-review found that terminology could leak presentation geometry into gameplay occupancy authority. The final head repairs this by using **visual coverage** and explicitly forbidding gameplay inference from pixel dimensions.

Final self-review result: **PASS**, zero unresolved material findings.

## Exact-head validation

```yaml
final_head: 819f14306c9dc26fd5b25da56f460f4cf7c92a8d
changed_files: 3
changed_path_scope: PASS
agent_governance:
  run_number: 1620
  result: SUCCESS
architecture_semantic_audit:
  run_number: 210
  result: SUCCESS
merge_authority_audit:
  run_number: 430
  result: SUCCESS
merge_gate:
  run_number: 472
  validate_job: SUCCESS
review_threads: 0
review_submissions: 0
runtime_component_e2e: NOT_APPLICABLE_DOCS_ONLY
```

## Merge evidence

```yaml
pr: 331
merge_method: squash
merge_sha: f90b99bee9567800a430ca1a703843d647dc01b8
```

## DYN-ATLAS effect

The appearance anchor/visual-coverage/displacement authority gate is closed for the exact 15.25.bd5a04 fixture.

The next Game-owned dependency for DYN-ATLAS-001 is the bounded deterministic Thais semantic export fixture/artifact under the accepted Game -> Atlas, spatial, legacy-import and appearance profiles.
