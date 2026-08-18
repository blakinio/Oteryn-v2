# OTV2-20260818-dyn-atlas-thais-z7-export-fixture

```yaml
task_id: OTV2-20260818-dyn-atlas-thais-z7-export-fixture
title: Produce bounded deterministic Thais Z7 semantic Atlas export fixture
mode: IMPLEMENTATION
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: feat/OTV2-20260818-dyn-atlas-thais-z7-export-fixture
pr: 335
base_sha: 457df3772a7aaf648c1a048b2db2caa409fcf974
reviewed_content_head: 999dd7fd60aa8923479a7e87d4b61531cfe471f4
owner: ChatGPT autonomous execution
created_at: 2026-08-18T10:35:00+02:00
updated_at: 2026-08-18T10:58:00+02:00
execution_budget_minutes: 120
owned_paths:
  - tools/game-atlas-thais-fixture/**
  - .github/workflows/game-atlas-thais-fixture.yml
  - docs/agents/evidence/OTV2-20260818-dyn-atlas-thais-z7-export-fixture.md
  - docs/agents/tasks/active/OTV2-20260818-dyn-atlas-thais-z7-export-fixture.md
public_contracts: []
depends_on:
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
  - docs/contracts/OTERYN_WORLD_SPATIAL_COORDINATE_PROFILE_V1.md
  - docs/contracts/OTERYN_CRYSTALSERVER_LEGACY_SPATIAL_IMPORT_PROFILE_V1.md
  - docs/contracts/OTERYN_ATLAS_15_32_APPEARANCE_SPATIAL_PROFILE_V1.md
  - Oteryn/Oteryn-Atlas@0b56d9a95279f1ec02fddd0dfcf8bd6ffd16b539
  - blakinio/Otheryn@e417c5e7c22986bf4acef0495eb47f7b72c97cce
blocks:
  - DYN-ATLAS-001 Game-owned bounded semantic export artifact/digest
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-THAIS-Z7
external_repositories:
  - Oteryn/Oteryn-Atlas
  - blakinio/Otheryn
```

## Goal

Produce a deterministic bounded Game-owned semantic export artifact for the canonical DYN-ATLAS-001 Thais Z7 selection without making OTBM, the legacy Atlas renderer, source asset files or a proof serializer canonical Oteryn World authority.

## Fixed proof inputs

```text
legacy map source repository = blakinio/Otheryn@e417c5e7c22986bf4acef0495eb47f7b72c97cce
canonical world.otbm sha256 = 3bd40d14fefec41f24c4b3ae879e420be1a831ef55b95dcbec721e587a09b034
legacy bounds = X 32280..32440, Y 32155..32305, Z 7
native bounds = x [32280,32441), y [32155,32306), floor -7
asset source name = 15.32.zip
asset Drive file id = 1Dlo3bS4K1nS3mw4BhPZdlHT7lX5zRAvv
asset zip sha256 = 1a6bad8b7598cd874f534cd4aae2d249fb3d9b4458b3ccfa75754f91bb27870f
asset catalog sha256 = 35639e000c4c108665a091cfbdf699d549d995b37670bc08de575ab6cd380d85
asset appearance sha256 = dc4f4c01e3701c77877c67895168e4399837046122d6d17e3e608a12a2fed075
```

## Acceptance criteria

- [x] Game-owned exporter exists under `tools/game-atlas-thais-fixture/`.
- [x] OTBM is used only in the producer/import boundary; output contains no OTBM-shaped authoritative model.
- [x] legacy Z7 maps to native `floor=-7` through the accepted importer profile.
- [x] visible ground/top-level tile source order maps to explicit `PresentationOrderKey {plane:0, order:index}`.
- [x] nested container children are not emitted as visible spatial presentation records; exact proof observes three excluded descendants.
- [x] producer resolves concrete appearance frame, default static phase, pattern, layer and sprite source IDs.
- [x] appearance visual anchor/coverage/displacement follows `oteryn-atlas-15-32-appearance-spatial-v1`.
- [x] source appearance/sprite IDs remain provenance IDs; no canonical Game entity identity is invented.
- [x] proof output uses explicitly non-production `dyn-atlas-thais-z7-jsonl-v0` physical packaging.
- [x] canonical output excludes wall-clock timestamps, runner paths and other nondeterministic metadata.
- [x] identical declared inputs produced byte-identical output in two independent runs.
- [x] verifier recomputes artifact/file digests and validates ordering, bounds, identities and primitive constraints.
- [x] deliberate corruption/negative test fails closed.
- [x] semantic counts, canonical sizes and stable tile/diagnostic file digests are captured in durable evidence.
- [x] workflow uses repository-policy-compliant exact action SHAs.
- [x] no raw source asset pixels are committed to Game.
- [ ] final frozen PR head passes the dedicated exact-head fixture workflow and yields terminal semantic artifact/workflow artifact identities.
- [ ] final frozen PR head passes Agent Governance, Architecture Semantic Audit, Merge Authority Audit and Merge Gate before Ready/merge.

## First complete integration proof

Pre-hardening exact workflow run `32117767429` / job `95651058334` completed **SUCCESS** against producer head `ee242eb10b0d91cc1d6a0a812bc6f9d8af3d4711`.

```text
tiles = 24311
ground_items = 24292
top_level_tile_items = 14990
source_item_tree_without_ground = 14993
presentation_records = 39282
resolved_primitives = 39282
unique_appearance_source_ids = 862
unique_sprite_source_ids = 990
canonical manifest bytes = 2357
canonical tiles bytes = 28040344
canonical diagnostics bytes = 19
tiles sha256 = ff14efee3fc376d8f18432c628294c64ffe89450a59aaa498a28e6d705815984
diagnostics sha256 = 60326e4e048106d4366a2fd8fe472ccfdf06667fcd0f234977febfeaa38f31b8
```

Two independent runs were byte-identical and deliberate corruption was rejected. The first run also uploaded artifact ID `9317706518`.

Repository policy then correctly found unpinned GitHub Action tags in the new workflow. The workflow has since been hardened to the repository's exact pinned action SHAs. That policy failure was a control-plane hardening finding, not an exporter semantic failure.

## Evidence classification

### PROVEN

- accepted spatial/importer/15.32 appearance authority is complete;
- exact Thais legacy/native selection and exact map/asset identities are pinned;
- exporter/verifier/self-tests execute successfully against the exact source;
- all 24,311 coordinates in the selected rectangle are present as source tile records in this exact source;
- 39,282 visible presentation records resolve successfully with zero diagnostics;
- three nested source item descendants are preserved in source counts but excluded from visible spatial presentation;
- two-run byte determinism and corruption rejection are proven;
- semantic fixture contains no source pixel payload.

### DERIVED IMPLEMENTATION CHOICE

- `dyn-atlas-thais-z7-jsonl-v0` remains proof-only deterministic packaging rather than permanent serializer selection;
- exported placement record IDs are deterministic proof-scope identities while canonical entity identity remains unresolved where Game identity has not been established.

### UNKNOWN / outside this task

- exact-digest public pixel publication authorization for the 15.32 ZIP;
- permanent serializer/chunk profile and production resource ceilings;
- generalized animation/live appearance semantics.

## Final-head evidence rule

The manifest contains `producer_repository_sha`; therefore any commit that records a just-produced terminal artifact digest changes the producer SHA and would create a recursive digest loop.

The final frozen-head workflow run ID, semantic artifact digest and workflow artifact ID are written to PR #335 metadata after the final head is fixed. They are then copied into the post-merge archived task record. PR metadata mutation does not change the producer commit.

## Validation

- pure self-tests: **PASS (7/7)**;
- exact source digest validation: **PASS**;
- deterministic double export: **PASS**;
- fixture verifier: **PASS**;
- deliberate corruption rejection: **PASS**;
- Architecture Semantic Audit on hardened workflow head `8d529464c3857000957901e2b09164b1c956bfd4`: **PASS (#220)**;
- Merge Authority Audit on hardened workflow head `8d529464c3857000957901e2b09164b1c956bfd4`: **PASS (#437)**;
- Agent Governance on hardened workflow head `8d529464c3857000957901e2b09164b1c956bfd4`: **PASS (#1633)**;
- final current-head rerun after evidence/checkpoint freeze: **PENDING**.

## Context checkpoint

```yaml
checkpoint_version: 2
updated_at: 2026-08-18T10:58:00+02:00
reviewed_content_head: 999dd7fd60aa8923479a7e87d4b61531cfe471f4
branch: feat/OTV2-20260818-dyn-atlas-thais-z7-export-fixture
pr: 335
status: validating
context_routes:
  - architecture
  - agent-governance
  - testing
  - implementation
proven:
  - exact source integration produces complete bounded semantic Thais Z7 fixture with deterministic double-build and fail-closed corruption behavior
  - stable semantic counts and file identities are recorded
  - GitHub Actions are now exact-SHA pinned per repository policy
derived:
  - terminal producer-SHA-dependent artifact identity must live in frozen-head PR metadata then closeout, not a self-mutating pre-merge evidence file
unknown:
  - final frozen-head artifact digest/run/artifact id until current head workflow finishes
conflicts: []
first_failure:
  marker: unpinned-workflow-actions
  evidence: first PR head semantic workflow passed but repository policy rejected unpinned action tags; repaired with exact SHAs
rejected_hypotheses:
  - let Atlas parse OTBM directly
  - emit nested container items as visible stack records
  - invent canonical content identity from legacy numeric IDs
  - treat proof JSONL packaging as permanent serializer selection
  - record producer-SHA-dependent final digest in a pre-merge commit and create recursive self-reference
changed_paths:
  - .github/workflows/game-atlas-thais-fixture.yml
  - tools/game-atlas-thais-fixture/README.md
  - tools/game-atlas-thais-fixture/export.py
  - tools/game-atlas-thais-fixture/self_test.py
  - tools/game-atlas-thais-fixture/verify.py
  - docs/agents/evidence/OTV2-20260818-dyn-atlas-thais-z7-export-fixture.md
  - docs/agents/tasks/active/OTV2-20260818-dyn-atlas-thais-z7-export-fixture.md
validation:
  - command: Game Atlas Thais Z7 fixture run 32117767429
    result: PASS
    evidence: deterministic double build, verifier pass, corruption rejection, exact artifact upload
  - command: repository policy on hardened action-pinned workflow
    result: PASS
    evidence: Agent Governance #1633 and Merge Authority Audit #437 on 8d529464c3857000957901e2b09164b1c956bfd4
blockers: []
next_action: freeze this checkpoint head, require final exact-head fixture + repository gates, update PR metadata with terminal identities only, then Ready/squash-merge if all green
```

## Source branch closeout

```yaml
source_branch_disposition: auto_delete_after_merge
source_branch_reason: ordinary same-repository implementation task
source_branch_evidence: pending
```
