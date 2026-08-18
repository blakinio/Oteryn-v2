# DYN-ATLAS-001 bounded Game Thais Z7 export fixture — 2026-08-18

## Status

**IMPLEMENTATION / exact integration evidence pending PR workflow**.

This record owns executable evidence for the first bounded Game-produced semantic Atlas fixture. It must not be interpreted as a permanent public serialization profile or full-world exporter.

## Accepted upstream authority

- Game -> Atlas semantics: `oteryn-game-atlas-export-v1`
- native spatial semantics: `oteryn-world-spatial-v1`
- CrystalServer legacy mapping: `oteryn-crystalserver-legacy-spatial-import-v1`
- appearance presentation profile: `oteryn-atlas-15-32-appearance-spatial-v1`
- current Game base: `blakinio/Oteryn-v2@457df3772a7aaf648c1a048b2db2caa409fcf974`
- migration implementation evidence: `blakinio/Otheryn@e417c5e7c22986bf4acef0495eb47f7b72c97cce`

## Exact source selection

```text
CrystalServer revision = 5e89bf8329ea406cb4ea8f4a18f32954f13e5418
world.otbm sha256 = 3bd40d14fefec41f24c4b3ae879e420be1a831ef55b95dcbec721e587a09b034
legacy bounds = X 32280..32440, Y 32155..32305, Z 7
native bounds = x [32280,32441), y [32155,32306), floor -7

Drive object = 15.32.zip
Drive file id = 1Dlo3bS4K1nS3mw4BhPZdlHT7lX5zRAvv
asset ZIP sha256 = 1a6bad8b7598cd874f534cd4aae2d249fb3d9b4458b3ccfa75754f91bb27870f
asset catalog sha256 = 35639e000c4c108665a091cfbdf699d549d995b37670bc08de575ab6cd380d85
asset appearance sha256 = dc4f4c01e3701c77877c67895168e4399837046122d6d17e3e608a12a2fed075
```

## Implementation boundary

`tools/game-atlas-thais-fixture/export.py` is the producer/import boundary. It may read pinned migration OTBM and asset metadata but emits only explicit Game-owned semantic presentation records.

Important constraints enforced by code:

- only the fixed Thais Z7 rectangle is exported;
- legacy Z maps to native floor through the accepted profile;
- ground + top-level tile items are the visible presentation source;
- container descendants are never emitted as visible spatial stack records;
- same-tile source order becomes explicit `{plane: 0, order: index}`;
- Game resolves first object frame group, declared static default phase, source pattern, layer and sprite source ID;
- source appearance/sprite IDs remain provenance/reference IDs;
- unresolved canonical Game entity identity stays explicitly unresolved;
- visual coverage is presentation-only, not gameplay occupancy/collision;
- no source pixels are placed in the semantic fixture.

## Proof-only physical profile

The executable proof uses `dyn-atlas-thais-z7-jsonl-v0` with canonical `manifest.json`, `tiles.jsonl`, `diagnostics.json` and `artifact.sha256`.

This format is deliberately scoped to DYN-ATLAS-001. It does not decide the permanent Game -> Atlas serializer, compression or chunk dimensions.

Artifact identity is domain-separated SHA-256 over canonical manifest semantics (excluding its digest field), exact tile JSONL bytes and canonical diagnostics bytes.

## Validation gates

The dedicated exact-head workflow must prove:

- pinned Game PR head checkout;
- pinned Otheryn checkout and exact map SHA;
- exact 15.32 Drive ZIP/catalog/appearance identities;
- Python compilation and pure producer self-tests;
- two independent producer runs with recursive byte identity;
- fail-closed fixture verifier on both outputs;
- deliberate corruption rejection;
- exact artifact upload;
- captured artifact digest, counts and byte sizes.

## Current evidence

Implementation paths exist on branch `feat/OTV2-20260818-dyn-atlas-thais-z7-export-fixture`.

Exact workflow run, workflow artifact ID, final artifact digest, counts and measurements are **PENDING** until the draft PR runs the exact-head integration workflow.

## Rights boundary

This fixture is semantic metadata only and does not publish decoded source pixels. Public source-pixel publication for the 15.32 asset digest remains a separate DYN-ATLAS gate and is not silently inferred from this producer implementation.
