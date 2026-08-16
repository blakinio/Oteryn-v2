# Game -> Atlas physical-profile readiness evidence

Task: `OTV2-20260816-game-atlas-physical-profile-readiness`  
Issue: #291  
Delivery PR: #292  
Coordination ID: `OTERYN-GAME-ATLAS-V1-PHYSICAL-READINESS`

## Verdict

**`EVIDENCE_GAP`**

The synthetic physical-packaging spike is successful and materially narrows the later profile decision, but the first executable Game -> Atlas physical-profile contract is **not yet safe to freeze** because canonical Game spatial/coordinate authority is still incomplete at the level required by the accepted semantic export contract.

The smallest missing owner evidence is a canonical Oteryn-Game spatial/coordinate profile defining axes/orientation, numeric coordinate domain and bounds, floor identity/domain/order, point/bounds validity, deterministic same-position ordering/stack-layer semantics and presentation anchor/displacement semantics where canonical presentation references require them.

## Exact trusted basis

Audit/spike entry base: `blakinio/Oteryn-v2@8722e565c6a0556934209820e3c14ee4f2dc6093`.

### PROVEN — semantic Game -> Atlas contract

`docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md` requires an explicit versioned `coordinate_profile` before executable producer/consumer compatibility. That profile must define horizontal axes/orientation, numeric domain/bounds, floor identity/order, point/area semantics, position validity, deterministic same-position ordering, stack/layer semantics and displacement/anchor semantics. The same accepted contract deliberately leaves exact numeric ceilings and physical encoding deferred.

### PROVEN — canonical World architecture is not yet a frozen physical coordinate implementation

`docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md` keeps OTBM behind a bounded legacy-import boundary and treats the Oteryn World/Content model as native authority. Its chunking direction remains benchmark-sensitive: `32x32` and `64x64` are candidates and final dimensions/vertical packing are not frozen merely from legacy conventions.

`docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md` keeps the typed semantic graph independent from its serializer, explicitly says unknown physical details/numeric limits fail closed, and requires bounded spike evidence before final World Project/World Bundle physical-format acceptance. That World-format gate is related evidence, not permission to treat this Atlas-export spike as a final World-format decision.

### PROVEN — executable workspace does not yet provide canonical world-schema authority

At entry `Cargo.toml` contains the current 19-member workspace but no `world-schema`, `world-project`, `world-bundle`, `world-spatial` or equivalent canonical World implementation crate. `docs/agents/REPOSITORY_MAP.md` lists those names only as a planned target layout and explicitly says planned paths are not proof of current existence.

The existing executable `crates/client-domain::Position` is declared inside a module whose crate documentation says `Protocol-neutral, non-authoritative client projection model`; its `x: i32`, `y: i32`, `floor: i16` representation therefore cannot be promoted into canonical Game/Atlas coordinate authority by inference.

### PROVEN — world/channel scope

`docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md` assigns the public map definition World scope with one immutable revision shared across channels. Channel runtime map overlays are channel-local authoritative runtime state. The static Atlas export therefore must project immutable Game World/Content facts, not channel runtime overlays.

### PROVEN — numeric production limits remain an owning decision

`docs/contracts/RESOURCE_LIMITS_REGISTRY.json` requires externally controlled counts/depths/lengths/byte sizes to have absolute hard maxima before implementation acceptance. The spike's internal caps protect only the synthetic research harness; they are not production limits and are not added to the registry.

## Spike implementation and provenance

Exact spike head: `f35c28375abaa7339f3f74a4d19966c36393eee1`.

GitHub Actions evidence:

- workflow run: `31938342334`;
- job: `95143702307` — `Game Atlas Physical Profile Spike / validate`;
- runner: GitHub-hosted `ubuntu-24.04`;
- Python: `3.12.13`;
- conclusion: **SUCCESS**;
- generated full report SHA-256: `c5dbb377e7808d088fa22645f3d91905423d973530aeaeb8de13454ec8e6f25e`;
- matrix cells: `24`;
- `spike_checks_pass=true`.

The workflow checked out exactly `f35c28375abaa7339f3f74a4d19966c36393eee1`, verified `HEAD`, compiled the Python file, ran the self-test, emitted the summary and printed the complete machine-readable report into the workflow log.

Persisted normalized machine evidence: `docs/agents/evidence/OTV2-20260816-game-atlas-physical-profile-report.json`.

## Synthetic fixture boundary

Two deterministic project-owned fixtures were generated, each `128 x 128 x 6 = 98,304` records:

- `synthetic-sparse-v1`, semantic SHA-256 `d91d031d8c129f9310fe15188914969d9e35aa4eb44be283d61751d4eb0043a2`;
- `synthetic-dense-v1`, semantic SHA-256 `045a4b698e5e43e251b040e04da29641b631e14b9c59c8487c0333897e0f6b6c`.

No OTBM, Crystal, Canary, Tibia/CipSoft asset, official client byte, legacy map file or external fixture is used.

The research matrix compares:

- `canonical-json-v0`;
- `canonical-jsonl-v0`;
- `binary-baseline-v0`, explicitly research-only and not a proposed public schema;
- `32x32` and `64x64` spatial chunks;
- `per-floor` and `packed-floors` packaging.

The spike uses deterministic gzip only as a measurement mechanism. It does not accept gzip or SHA-256 as production Game -> Atlas profile decisions.

## Direct spike results

### PROVEN — all 24 matrix cells satisfy the spike invariants

Every cell proved:

- byte-identical output for identical synthetic inputs;
- semantic encode/decode round-trip identity;
- raw SHA-256 corruption detection;
- gzip corruption detection;
- one synthetic record edit changes exactly one data chunk;
- one point lookup requires exactly one data chunk under the tested layout.

### DERIVED — JSON versus JSONL is not a size decision

For `32x32/per-floor`, JSONL gzip bytes are only about `0.11%` above canonical JSON in both synthetic fixtures. Similar near-equivalence appears across the matrix. Size evidence therefore does not justify choosing JSON over JSONL or vice versa; streaming, parser, diagnostics, compatibility and consumer implementation evidence must decide that later.

### DERIVED — per-floor packaging is the stronger browser locality baseline

For canonical JSON `32x32`, packing six synthetic floors together reduces total gzip by about `7.5%` on sparse data and `6.4%` on dense data, but increases one-floor point and representative viewport bytes by roughly `5.6x`.

This is strong evidence against packing unrelated floors together by default for a floor-oriented Atlas consumer unless later representative workload evidence proves a compensating benefit. It is **not** a canonical floor-packing decision because the real canonical floor domain and browser workload are not yet frozen/proven.

### DERIVED — `32x32` versus `64x64` remains a real trade-off

For canonical JSON/per-floor, `64x64` reduces aggregate gzip by about `6.0%` on sparse data and `4.1%` on dense data and reduces chunk count from `96` to `24`. However:

- one-point compressed bytes rise by about `3.8x` to `3.9x`;
- the representative viewport compressed bytes rise by about `1.69x` to `1.72x`.

This evidence narrows the decision but does not identify one globally superior chunk size. A later profile decision needs representative consumer/viewer access patterns, cache behavior and canonical World scale.

### DERIVED — binary size advantage does not justify a public binary schema

At `32x32/per-floor`, the research binary baseline reduces gzip total versus canonical JSON by about `21.4%` for sparse data and `10.6%` for dense data; raw bytes fall much more. This is useful as a lower-bound comparator, but it does not measure schema evolution, browser decoding cost, dependency/supply-chain cost, diagnostics, compatibility tooling or parser attack surface. The spike therefore does not recommend or accept the binary baseline as a public format.

## Safety / limit findings

The research tool itself enforces internal caps:

- max synthetic records: `200,000`;
- max research chunk bytes: `64 MiB`;
- max research string bytes: `1,024`.

These are harness safety caps only. **They are not production recommendations or `RESOURCE_LIMITS_REGISTRY.json` evidence.** Production limits require the owning profile/implementation evidence against representative and adversarial artifacts.

## Readiness decision

### `PROFILE_CONTRACT_READY`: NO

The packaging evidence is sufficient to reject several unsupported shortcuts and to shape the next decision, but the accepted export contract requires coordinate semantics that the current canonical Game implementation/contract set does not yet freeze at executable-profile precision.

### `EVIDENCE_GAP`: YES

Smallest missing owner evidence:

> **Canonical Game spatial/coordinate profile v1** owned by Oteryn-Game, defining axes/orientation, numeric coordinate domain/bounds, floor identity/domain/order, point/bounds inclusion/validity, deterministic ordering/stack-layer semantics and anchor/displacement semantics required for public presentation references.

That owner contract must not copy the non-authoritative client `Position` type or Tibia/OTBM conventions as authority. Once accepted, the Game -> Atlas physical-profile contract can combine it with this spike evidence and separately justified production resource limits.

## What this task intentionally does not decide

- public serializer/IDL;
- production compression/container;
- permanent `32x32` or `64x64` chunking;
- packed versus per-floor canonical layout;
- coordinate/floor numeric ranges;
- production resource ceilings;
- World Project/World Bundle serializer;
- asset redistribution;
- storage/CDN;
- Atlas framework;
- delta protocol;
- repository creation/rename/transfer/extraction.

## Single next action

Create one bounded Oteryn-Game architecture task for the **canonical spatial/coordinate profile v1**. It should freeze only the coordinate/floor/order/anchor semantics required by the accepted World model and Game -> Atlas contract, using the architecture decision-timing test and preserving physical serializer/chunk/resource-limit choices as separate evidence-gated decisions.
