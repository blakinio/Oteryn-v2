# Game -> Atlas physical-profile readiness evidence

Task: `OTV2-20260816-game-atlas-physical-profile-readiness`  
Issue: #291  
Delivery PR: #292  
Coordination ID: `OTERYN-GAME-ATLAS-V1-PHYSICAL-READINESS`

## Verdict

**`EVIDENCE_GAP`**

The corrected synthetic physical-packaging spike is successful and materially narrows the later profile decision, but the first executable Game -> Atlas physical-profile contract is **not yet safe to freeze** because canonical Game spatial/coordinate authority is still incomplete at the level required by the accepted semantic export contract.

The smallest missing owner evidence is a canonical Oteryn-Game spatial/coordinate profile defining axes/orientation, numeric coordinate domain and bounds, floor identity/domain/order, point/bounds validity, deterministic same-position ordering/stack-layer semantics and presentation anchor/displacement semantics where canonical presentation references require them.

## Exact trusted basis

Audit/spike entry base: `blakinio/Oteryn-v2@8722e565c6a0556934209820e3c14ee4f2dc6093`.

### PROVEN — semantic Game -> Atlas contract

`docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md` requires an explicit versioned `coordinate_profile` before executable producer/consumer compatibility. That profile must define horizontal axes/orientation, numeric domain/bounds, floor identity/order, point/area semantics, position validity, deterministic same-position ordering, stack/layer semantics and displacement/anchor semantics. Exact numeric ceilings and physical encoding remain deliberately deferred.

### PROVEN — canonical World architecture is not yet a frozen physical coordinate implementation

`docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md` keeps OTBM behind a bounded legacy-import boundary and treats Oteryn World/Content as native authority. Its chunking direction remains benchmark-sensitive: `32x32` and `64x64` are candidates and final dimensions/vertical packing are not frozen from legacy conventions.

`docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md` keeps the typed semantic graph independent from its serializer, says unknown physical details/numeric limits fail closed, and requires bounded spike evidence before final World Project/World Bundle physical-format acceptance. That World-format gate is related evidence, not permission to turn this Atlas-export spike into a final World-format decision.

### PROVEN — executable workspace does not yet provide canonical world-schema authority

At entry `Cargo.toml` contains the current workspace but no `world-schema`, `world-project`, `world-bundle`, `world-spatial` or equivalent canonical World implementation crate. `docs/agents/REPOSITORY_MAP.md` lists such names only as planned target layout and explicitly says planned paths are not proof of current existence.

The existing executable `crates/client-domain::Position` lives in a module documented as `Protocol-neutral, non-authoritative client projection model`; its `x: i32`, `y: i32`, `floor: i16` representation therefore cannot be promoted into canonical Game/Atlas coordinate authority by inference.

### PROVEN — world/channel scope

`docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md` assigns the public map definition World scope with one immutable revision shared across channels. Channel runtime map overlays are channel-local authoritative runtime state. Static Atlas export must therefore project immutable Game World/Content facts, not channel runtime overlays.

### PROVEN — numeric production limits remain an owning decision

`docs/contracts/RESOURCE_LIMITS_REGISTRY.json` requires externally controlled counts/depths/lengths/byte sizes to have absolute hard maxima before implementation acceptance. The spike's internal caps protect only the synthetic research harness; they are not production limits and are not added to the registry.

## Corrected spike provenance

Exact corrected spike head: `700365199044c15ef22aaa9336d72dd103715a76`.

GitHub Actions evidence:

- workflow run: `31938708639`;
- job: `95144635706` — `Game Atlas Physical Profile Spike / validate`;
- runner: GitHub-hosted `ubuntu-24.04`;
- Python: `3.12.13`;
- conclusion: **SUCCESS**;
- generated full report SHA-256: `c2ae672821f389ca4a13b72ce07c1b945e8bca550970148753582308ae4ec19d`;
- matrix cells: `24`;
- `spike_checks_pass=true`.

The workflow checked out exactly `700365199044c15ef22aaa9336d72dd103715a76`, verified `HEAD`, compiled the spike, ran the self-test, emitted the summary and printed the complete machine-readable report into immutable workflow logs.

Persisted normalized machine evidence: `docs/agents/evidence/OTV2-20260816-game-atlas-physical-profile-report.json`.

## Self-review repair history

Initial successful measurement head `f35c28375abaa7339f3f74a4d19966c36393eee1` / run `31938342334` / job `95143702307` proved the core determinism/locality matrix, but self-review found two measurement defects before delivery freeze:

1. `binary-baseline-v0` could accidentally decode as UTF-8, causing a meaningless textual `diff_lines=2` observation;
2. textual diff-line count alone made compact one-line JSON appear as reviewable as record-oriented JSONL even when the changed JSON line was hundreds of KiB or MiB.

Repair cycle 1 explicitly sets both binary text metrics to `null` and records `local_edit_text_max_line_bytes` for text encodings. Corrected run `31938708639` reran all 24 matrix cells on the repaired code and passed. The initial report digest is superseded for final evidence rather than silently reused.

## Synthetic fixture boundary

Two deterministic project-owned fixtures are generated, each `128 x 128 x 6 = 98,304` records:

- `synthetic-sparse-v1`, semantic SHA-256 `d91d031d8c129f9310fe15188914969d9e35aa4eb44be283d61751d4eb0043a2`;
- `synthetic-dense-v1`, semantic SHA-256 `045a4b698e5e43e251b040e04da29641b631e14b9c59c8487c0333897e0f6b6c`.

No OTBM, Crystal, Canary, Tibia/CipSoft asset, official client byte, legacy map file or external fixture is used.

The research matrix compares canonical JSON, canonical JSONL, a research-only deterministic binary lower-bound baseline, `32x32` versus `64x64`, and per-floor versus packed-floor packaging. Deterministic gzip and SHA-256 are measurement mechanisms only; neither is accepted as the production profile by this task.

## Direct corrected spike results

### PROVEN — all 24 matrix cells satisfy the spike invariants

Every cell proves byte-identical output, semantic encode/decode round-trip identity, raw digest corruption detection, gzip corruption detection, one synthetic record edit changing exactly one data chunk, and one point lookup requiring exactly one data chunk under the tested layout.

For every textual row the one-record edit produces two changed text lines. For every binary row textual diff metrics are now correctly `null`.

### DERIVED — JSON versus JSONL is not a size decision

For `32x32/per-floor`, JSONL gzip bytes are only about `0.11%` above canonical JSON in both synthetic fixtures. Similar near-equivalence appears across the matrix. Size evidence does not justify choosing JSON or JSONL.

However, corrected diff-review evidence distinguishes them materially: compact JSON's changed-file maximum line ranges from roughly `95 KiB` through `3.29 MiB` across this matrix, while JSONL stays at `160-198` bytes. This is meaningful source-review evidence in favor of record-oriented text, but a published Atlas artifact may not be reviewed as ordinary Git source, so it is not sufficient by itself to select the distribution serializer.

### DERIVED — per-floor packaging is the stronger browser locality baseline

For canonical JSON `32x32`, packing six synthetic floors together reduces total gzip by about `7.5%` on sparse data and `6.4%` on dense data, but increases one-floor point and representative viewport bytes by roughly `5.6x`.

This is strong evidence against packing unrelated floors together by default for a floor-oriented Atlas consumer unless later representative workload evidence proves a compensating benefit. It is not a canonical floor-packing decision because the real floor domain and browser workload remain unfrozen.

### DERIVED — `32x32` versus `64x64` remains a real trade-off

For canonical JSON/per-floor, `64x64` reduces aggregate gzip by about `6.0%` on sparse data and `4.1%` on dense data and reduces chunk count from `96` to `24`. One-point compressed bytes rise about `3.8x-3.9x`, and the representative viewport bytes rise about `1.69x-1.72x`.

This narrows the decision but does not identify one globally superior chunk size. A later profile decision needs representative consumer/viewer access patterns, cache behavior and canonical World scale.

### DERIVED — binary size advantage does not justify a public binary schema

At `32x32/per-floor`, the research binary baseline reduces gzip total versus canonical JSON by about `21.4%` for sparse data and `10.6%` for dense data; raw bytes fall much more. This does not measure schema evolution, browser decoding cost, dependency/supply-chain cost, diagnostics, compatibility tooling or parser attack surface. The spike therefore does not recommend or accept the binary baseline as a public format.

## Safety / limit findings

Research-only harness caps are `200,000` records, `64 MiB` per research chunk, and `1,024` bytes per research string. These values are **not** production recommendations or `RESOURCE_LIMITS_REGISTRY.json` evidence.

## Readiness decision

### `PROFILE_CONTRACT_READY`: NO

Packaging evidence is sufficient to reject unsupported shortcuts and shape the next decision, but the accepted export contract requires coordinate semantics the current canonical Game implementation/contract set does not yet freeze at executable-profile precision.

### `EVIDENCE_GAP`: YES

Smallest missing owner evidence:

> **Canonical Game spatial/coordinate profile v1** owned by Oteryn-Game, defining axes/orientation, numeric coordinate domain/bounds, floor identity/domain/order, point/bounds inclusion/validity, deterministic ordering/stack-layer semantics and anchor/displacement semantics required for public presentation references.

That owner contract must not copy the non-authoritative client `Position` type or Tibia/OTBM conventions as authority. Once accepted, the Game -> Atlas physical-profile contract can combine it with this spike evidence and separately justified production resource limits.

## What this task intentionally does not decide

No public serializer/IDL, production compression/container, permanent chunk size/floor packing, coordinate/floor numeric range, production resource ceiling, World Project/World Bundle serializer, asset redistribution, storage/CDN, Atlas framework, delta protocol or repository create/rename/transfer/extraction is accepted here.

## Single next action

Create one bounded Oteryn-Game architecture task for the **canonical spatial/coordinate profile v1**. Freeze only coordinate/floor/order/anchor semantics required by the accepted World model and Game -> Atlas contract; keep physical serializer/chunk/resource-limit decisions as separate evidence-gated decisions.
