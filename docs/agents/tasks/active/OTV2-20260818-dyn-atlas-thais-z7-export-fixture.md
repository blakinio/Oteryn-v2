# OTV2-20260818-dyn-atlas-thais-z7-export-fixture

```yaml
task_id: OTV2-20260818-dyn-atlas-thais-z7-export-fixture
title: Produce bounded deterministic Thais Z7 semantic Atlas export fixture
mode: IMPLEMENTATION
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: feat/OTV2-20260818-dyn-atlas-thais-z7-export-fixture
pr: pending
base_sha: 457df3772a7aaf648c1a048b2db2caa409fcf974
owner: ChatGPT autonomous execution
created_at: 2026-08-18T10:35:00+02:00
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

- [ ] Game-owned exporter code exists under `tools/game-atlas-thais-fixture/`.
- [ ] OTBM is used only in the producer/import boundary; output contains no OTBM-shaped authoritative model.
- [ ] legacy Z7 maps to native `floor=-7` through the accepted importer profile.
- [ ] visible ground/top-level tile source order maps to explicit `PresentationOrderKey {plane:0, order:index}`.
- [ ] nested container children are not emitted as visible spatial presentation records.
- [ ] producer resolves concrete appearance frame, default static phase, pattern, layer and sprite source IDs.
- [ ] appearance visual anchor/coverage/displacement follows `oteryn-atlas-15-32-appearance-spatial-v1`.
- [ ] source appearance/sprite IDs remain provenance IDs; no canonical Game entity identity is invented.
- [ ] proof output uses explicitly non-production `dyn-atlas-thais-z7-jsonl-v0` physical packaging.
- [ ] canonical output excludes wall-clock timestamps, runner paths and other nondeterministic metadata.
- [ ] identical declared inputs produce byte-identical output in two independent runs.
- [ ] verifier recomputes artifact/file digests and validates ordering, bounds, identities and primitive constraints.
- [ ] corruption/negative test fails closed.
- [ ] exact workflow artifact ID, semantic artifact digest, counts and sizes are captured in durable evidence.
- [ ] no raw source asset pixels are committed to Game.
- [ ] exact-head governance/architecture/merge gates pass before Ready/merge.

## Explicit non-goals

- permanent Game -> Atlas serializer selection;
- production resource-limit registry freeze;
- full-world conversion;
- browser renderer or Atlas indexing;
- live state, NPC conversations, interactions or analytics;
- source-pixel publication/redistribution;
- production object storage/CDN/deployment;
- promoting legacy numeric IDs to canonical Game content identity.

## Evidence classification

### PROVEN

- spatial/importer/15.32 appearance profiles are accepted on Game main;
- exact Thais legacy/native selection is accepted;
- exact map and 15.32 asset identities are pinned and independently verified;
- pinned legacy semantic parser/renderer behavior is available as migration conversion evidence.

### DERIVED IMPLEMENTATION CHOICE

- `dyn-atlas-thais-z7-jsonl-v0` is a proof-only deterministic packaging chosen to make exact output inspectable and reproducible without freezing the future public serializer;
- exported placement record IDs are deterministic proof-scope identities derived from explicit source selection/position/presentation order while canonical entity identity remains unresolved where no Game identity exists.

### UNKNOWN / outside this task

- exact-digest public pixel publication authorization for the 15.32 ZIP;
- permanent serializer/chunk profile and production resource ceilings;
- generalized animation/live appearance semantics.

## Validation plan

1. unit/self-tests for canonical encoding, record identity and verifier failure behavior;
2. exact pinned integration workflow checks out Otheryn migration source and verifies map SHA;
3. workflow downloads exact `15.32.zip`, verifies ZIP/catalog/appearance identities;
4. exporter run A and B with identical producer/input revision;
5. recursive byte comparison A vs B;
6. verifier validates both outputs;
7. deliberate corruption must be rejected;
8. upload metadata/semantic fixture as workflow artifact and record exact artifact/digest/size/count evidence;
9. repository merge gates validate exact final PR head.

## Context checkpoint

```yaml
checkpoint_version: 1
updated_at: 2026-08-18T10:35:00+02:00
head: pending
branch: feat/OTV2-20260818-dyn-atlas-thais-z7-export-fixture
pr: pending
status: implementing
context_routes:
  - architecture
  - agent-governance
  - testing
  - implementation
proven:
  - canonical input and conversion-profile authority is complete
  - latest appearance source is exact Drive object 15.32.zip, not uploaded 15.25 fixture
derived:
  - proof-only JSONL physical package is suitable for bounded deterministic artifact evidence
unknown:
  - runtime measurements and final semantic artifact digest until exact integration workflow runs
conflicts: []
first_failure:
  marker: bounded-game-export-artifact-missing
  evidence: accepted semantic profiles exist but no Game-owned executable Thais fixture has yet been produced
rejected_hypotheses:
  - let Atlas parse OTBM directly
  - emit nested container items as visible stack records
  - invent canonical content identity from legacy numeric IDs
  - treat proof JSONL packaging as permanent serializer selection
changed_paths:
  - docs/agents/tasks/active/OTV2-20260818-dyn-atlas-thais-z7-export-fixture.md
validation: []
blockers: []
next_action: implement exporter/verifier/self-tests and exact-source integration workflow, then open draft PR and capture deterministic artifact evidence
```

## Source branch closeout

```yaml
source_branch_disposition: auto_delete_after_merge
source_branch_reason: ordinary same-repository implementation task
source_branch_evidence: pending
```
