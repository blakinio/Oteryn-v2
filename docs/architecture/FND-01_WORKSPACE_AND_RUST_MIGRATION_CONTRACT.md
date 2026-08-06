# FND-01: Workspace, Dependency and Existing-Rust Migration Contract

- Status: Candidate for owner acceptance
- Date: 2026-08-06
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Destination baseline: `blakinio/Oteryn-v2@cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2`
- Source inventory revision: `blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590`
- Applies to: `FND-01`, `VSL-02` and the one atomic destination migration/workspace pull request

## 1. Purpose

This contract defines the exact Rust workspace that may be created by the controlled native-client migration. It inventories the current Rust client rather than designing an unrelated greenfield tree, classifies every current workspace member, fixes the initial dependency and build policy and preserves the `pre-native-protocol` state accepted by ADR-0011.

This document does not move code, create the root Cargo workspace, implement `protocol-oteryn`, freeze public identifier representations or authorize gameplay admission. Physical migration remains owned by `VSL-02` and its one atomic destination pull request.

## 2. Governing decisions

The following accepted decisions are binding:

- ADR-0001: one native Rust client, one authoritative Rust server and one `protocol-oteryn`;
- ADR-0002: client/server/shared Rust ownership moves to `blakinio/Oteryn-v2` through one atomic destination migration/workspace PR after `FND-01` and `VSL-02`;
- ADR-0007: later E2E uses one shared three-tier platform with explicit evidence and no hidden retry-until-green;
- ADR-0008: `protocol-canary` is `REFERENCE_ONLY` and cannot enter the production workspace graph, binaries, negotiation, fallback, translation or release packaging;
- ADR-0011: the migrated client may compile and launch in `pre-native-protocol`, but gameplay entry is explicitly unavailable before credential consumption and endpoint connection; no speculative native protocol crate is permitted;
- `FND-ID-01` owns future public identifier meaning and representation;
- `FND-02` owns native wire framing, transport limits, schema and compatibility;
- `FND-04` owns exact Game Session, admission credential and lease behavior.

## 3. Evidence baseline

### 3.1 Source workspace

The source `oteryn-client/Cargo.toml` contains 26 workspace members:

```text
apps/client
crates/account-session
crates/app-runtime
crates/asset-decode
crates/asset-types
crates/asset-runtime
crates/diagnostics
crates/foundation
crates/game-domain
crates/simulation-core
crates/input-actions
crates/input-platform
crates/game-session
crates/identity
crates/platform
crates/protocol-canary
crates/protocol-core
crates/renderer
crates/renderer-resource
crates/test-support
crates/transport
crates/world-directory
tests/integration/technical-login
tests/security/auth
tools/architecture-check
tools/asset-compiler
```

The source uses:

- Rust `1.94.0`;
- edition 2024;
- resolver 3;
- one committed workspace lockfile;
- Windows target `x86_64-pc-windows-msvc`;
- `unsafe_code = "forbid"` and strict Clippy policy;
- exact direct dependency versions;
- one Windows client CI lane and one supply-chain lane.

### 3.2 Material source constraints

- `apps/client` directly depends on `protocol-canary` and currently composes a Windows renderer/technical-login spike.
- `tests/integration/technical-login` directly depends on `protocol-canary`.
- `game-session` contains the Canary-specific `EntryProfile::CanaryCurrent` lifecycle.
- `protocol-core` exposes a `u16::MAX` maximum buffer and little-endian helpers shaped by the current adapter.
- `transport` exposes a `u16::MAX` maximum complete frame, while the later native contract and resource limits remain owned by `FND-02`.
- `account-session` is one client-local identifier type and does not justify an independent crate.
- `world-directory`, `game-session`, `platform`, `identity` and `app-runtime` form an over-fragmented account/directory/entry stack with dense dependencies.
- `game-domain` and `simulation-core` are protocol-neutral client projection and client simulation code; they are not authoritative server-domain or GameNode-runtime evidence.
- `asset-types`, `asset-runtime`, `asset-decode`, `renderer-resource` and `asset-compiler` explicitly implement synthetic test assets and bounded spike infrastructure, not the final production asset/content system.
- `contracts/` contains only Canary contract material.
- `assets/` contains only test fixtures.

### 3.3 Source change reconciliation

At the inventory revision, open source PRs #23, #48 and #97 concern the legacy C++/Lua client or operational asset analysis rather than Rust workspace members. They do not alter this inventory. `VSL-02` must nevertheless record their terminal cutover disposition and re-run source comparison against the selected cutover SHA.

Any source change after `c923ad8a1dff17b4933a6110931b0823cec2c590` invalidates the inventory for changed paths until reconciled. It does not silently amend this contract.

## 4. Accepted initial workspace shape

The atomic destination migration creates the following initial workspace and no additional product crates:

```text
apps/client

crates/foundation
crates/diagnostics
crates/client-runtime
crates/platform-contracts
crates/platform-client
crates/identity
crates/client-domain
crates/client-simulation
crates/input-actions
crates/input-platform
crates/renderer
crates/synthetic-assets
crates/test-support

tests/security/auth
tests/pre-native-client

tools/architecture-check
tools/synthetic-asset-compiler
```

Initial package names are:

```text
oteryn-client
oteryn-foundation
oteryn-diagnostics
oteryn-client-runtime
oteryn-platform-contracts
oteryn-platform-client
oteryn-identity
oteryn-client-domain
oteryn-client-simulation
oteryn-input-actions
oteryn-input-platform
oteryn-renderer
oteryn-synthetic-assets
oteryn-test-support
oteryn-identity-security-tests
oteryn-pre-native-client-tests
oteryn-architecture-check
oteryn-synthetic-asset-compiler
```

The initial workspace deliberately does **not** contain:

```text
services/game-server
crates/protocol-canary
crates/protocol-core
crates/protocol-oteryn
crates/transport
crates/game-session
apps/oteryn-studio
persistence/content/scripting/server-runtime crates
```

Their absence is intentional, not an incomplete bootstrap defect. Later gates add only crates with an immediate accepted consumer.

## 5. Initial member consumers and acceptance

| Member | Immediate consumer or purpose | Observable migration acceptance |
|---|---|---|
| `apps/client` | shipped native client shell | builds, launches and reaches explicit `pre-native-protocol` ready state on Windows |
| `foundation` | every lower-level client crate | unit tests for cancellation, time and generation fencing |
| `diagnostics` | client runtime, platform client and test support | deterministic redaction and bounded diagnostic tests |
| `client-runtime` | `apps/client`, pre-native tests | explicit lifecycle with gameplay unavailable before credential/endpoint boundary |
| `platform-contracts` | platform client, identity, runtime and auth tests | bounded DTO-neutral account/directory contract tests |
| `platform-client` | identity/runtime and auth tests | synthetic HTTP/DTO boundary tests; no live compatibility claim |
| `identity` | client runtime and auth tests | PKCE, callback, cancellation, stale-generation and secret-redaction tests |
| `client-domain` | client simulation and synthetic client harness | typed command/event and stale-session tests |
| `client-simulation` | synthetic client harness | deterministic event application and immutable snapshot tests |
| `input-actions` | input platform and client shell | normalized semantic-action tests |
| `input-platform` | client shell | Windows/winit adapter tests and compile evidence |
| `renderer` | client shell and synthetic harness | surface lifecycle, device-loss/recovery and bounded synthetic-scene evidence |
| `synthetic-assets` | synthetic harness and compiler | deterministic fixture-pack/decode tests; never a production asset contract |
| `test-support` | workspace integration tests | deterministic fixtures, clocks and redacted diagnostics |
| `tests/security/auth` | Identity/Platform security boundary | exact negative and lifecycle scenarios |
| `tests/pre-native-client` | ADR-0011 migration state | proves no adapter, no credential consumption, no endpoint connection and no false success |
| `architecture-check` | complete workspace | validates `workspace-boundaries.toml` against locked Cargo metadata |
| `synthetic-asset-compiler` | development/test fixture pipeline | deterministic fixture compilation and path-safety tests |

`client-domain`, `client-simulation` and `synthetic-assets` may be consumed by the client only through an explicit development/test synthetic-world harness. They are not evidence of live gameplay compatibility. Release packaging must prove they are absent from the normal dependency closure unless a later accepted gate promotes them.

## 6. Per-member source dispositions

The disposition vocabulary is closed: `MIGRATE_AS_IS`, `MIGRATE_AND_RENAME`, `MERGE`, `SPLIT`, `REWRITE`, `REFERENCE_ONLY`, `DROP`.

| Source member | Disposition | Destination / rule | Rationale |
|---|---|---|---|
| `apps/client` | `REWRITE` | `apps/client` | retain useful Windows shell/render/input composition, remove Canary and technical-login composition, implement explicit pre-native state |
| `crates/account-session` | `MERGE` | `crates/platform-contracts` | one client-local ID does not justify a crate; account correlation belongs with account/directory contracts |
| `crates/app-runtime` | `MIGRATE_AND_RENAME` | `crates/client-runtime` | preserve Tokio orchestration and deterministic shutdown, rewrite W7 technical-login assumptions |
| `crates/asset-decode` | `MERGE` | `crates/synthetic-assets` | synthetic RGBA fixture decoder is not a production asset layer |
| `crates/asset-types` | `MERGE` | `crates/synthetic-assets` | synthetic pack schema remains explicitly development/test-only |
| `crates/asset-runtime` | `MERGE` | `crates/synthetic-assets` | synthetic pack handle/runtime remains fixture infrastructure |
| `crates/diagnostics` | `MIGRATE_AS_IS` | `crates/diagnostics` | independent bounded/redacted diagnostics boundary has immediate consumers |
| `crates/foundation` | `SPLIT` | `crates/foundation` plus client-owned generation names | retain clocks, deadlines, cancellation, process/task generations; rename client-local `SessionGeneration` so `FND-ID-01` can own authoritative `SessionGeneration` |
| `crates/game-domain` | `MIGRATE_AND_RENAME` | `crates/client-domain` | useful protocol-neutral client projection; must not be mistaken for authoritative server domain |
| `crates/simulation-core` | `MIGRATE_AND_RENAME` | `crates/client-simulation` | useful deterministic client writer/snapshot model; not GameNode authoritative runtime |
| `crates/input-actions` | `MIGRATE_AS_IS` | `crates/input-actions` | clean framework-neutral semantic input boundary |
| `crates/input-platform` | `MIGRATE_AS_IS` | `crates/input-platform` | clean Windows/winit adapter boundary |
| `crates/game-session` | `SPLIT` | safe non-secret selection/value types into `platform-contracts`; client lifecycle into `client-runtime`; credential/profile/admission code deferred | current crate mixes client lifecycle, secrets and Canary profile; `FND-04` owns exact admission contract |
| `crates/identity` | `REWRITE` | `crates/identity` | retain PKCE, loopback and browser security behavior; remove dependency on game-entry credential and Canary-oriented lifecycle |
| `crates/platform` | `SPLIT` | `platform-contracts` + `platform-client` | separate validated values from HTTP/DTO implementation; Game Gateway ticket/admission paths remain deferred to `FND-04` |
| `crates/protocol-canary` | `REFERENCE_ONLY` | source repository/provenance only | ADR-0008 prohibits destination production inclusion |
| `crates/protocol-core` | `REFERENCE_ONLY` | reconsider under `FND-02` | current `u16`/little-endian API and 64 KiB ceiling cannot become native contract by inertia |
| `crates/renderer` | `MERGE` | `crates/renderer` with reusable `renderer-resource` parts | renderer surface owner remains; avoid a second unconsumed renderer crate |
| `crates/renderer-resource` | `MERGE` | reusable backend-neutral cache/resource logic into `renderer`; synthetic-specific adapters remain test-only | current separate member has no production consumer |
| `crates/test-support` | `MIGRATE_AS_IS` | `crates/test-support` | shared deterministic test infrastructure has multiple immediate consumers |
| `crates/transport` | `REFERENCE_ONLY` | reconsider under `FND-02` | no initial gameplay consumer; current frame ceiling is source-profile shaped and native limits are unresolved |
| `crates/world-directory` | `MERGE` | `crates/platform-contracts` | directory values and selection validation belong together; identifier representations remain provisional until `FND-ID-01` |
| `tests/integration/technical-login` | `REFERENCE_ONLY` | selected non-Canary scenarios rewritten into `tests/pre-native-client`; source tests remain evidence | direct Canary dependency and late credential/connection flow violate the initial state |
| `tests/security/auth` | `REWRITE` | `tests/security/auth` | preserve security scenarios while adapting to consolidated Platform/Identity boundaries |
| `tools/architecture-check` | `REWRITE` | `tools/architecture-check` | replace hard-coded future category matrix with machine-readable root contract and actual accepted members |
| `tools/asset-compiler` | `MIGRATE_AND_RENAME` | `tools/synthetic-asset-compiler` | name must not imply ownership of the future production asset compiler |

`REFERENCE_ONLY` means the source repository and exact source SHA remain the evidence. Reference-only code is not copied into Cargo membership, release packaging or product source paths. Selective later reuse requires the owning later gate, provenance and a new disposition.

## 7. Non-member subsystem dispositions

| Source subsystem | Disposition | Destination / rule |
|---|---|---|
| `assets/test-fixtures` | `MIGRATE_AND_RENAME` | `tests/fixtures/synthetic-assets`; synthetic/legal provenance recorded |
| `contracts/canary` | `REFERENCE_ONLY` | remain in source history; not copied into destination product contracts |
| source `docs/architecture` | `REFERENCE_ONLY` | discovery/provenance only; Oteryn-v2 ADRs and contracts remain authoritative |
| source `docs/agents` and `AGENTS.md` | `REFERENCE_ONLY` | destination governance applies; source task history is linked, not imported as policy |
| source root `Cargo.toml` | `REWRITE` | one destination root manifest using accepted membership and metadata |
| source `Cargo.lock` | `REWRITE` | regenerate one destination root lockfile from accepted graph; compare dependency provenance |
| source `rust-toolchain.toml` | `REWRITE` | retain Rust 1.94.0 and add both accepted targets |
| source `rustfmt.toml` | `REWRITE` | edition 2024, 100-column policy and repository-wide LF normalization |
| source `deny.toml` | `REWRITE` | evaluate Windows client and Linux shared graphs separately; all-features remains supplemental |
| source Rust CI workflow | `REWRITE` | destination workflows use product-realistic matrices and release-closure negatives |
| source synthetic/protocol architecture fixtures | `SPLIT` | synthetic fixtures migrate under test paths; Canary fixtures remain reference-only |

## 8. Repository and Cargo policy

### 8.1 Root ownership

The destination root owns exactly one:

```text
Cargo.toml
Cargo.lock
rust-toolchain.toml
rustfmt.toml
deny.toml
workspace-boundaries.toml
```

No member owns a second lockfile or overrides repository/license/edition/rust-version without a documented exception.

### 8.2 Workspace package metadata

The root fixes:

```text
edition = 2024
rust-version = 1.94
license = MIT
repository = https://github.com/blakinio/Oteryn-v2
publish = false
resolver = 3
```

Members inherit package metadata and workspace lints. Internal crates are not published to crates.io during the initial programme.

### 8.3 Dependency versions and sources

- Direct third-party dependencies are declared once in `[workspace.dependencies]` and pinned to exact reviewed versions during migration.
- Path dependencies remain inside the repository workspace.
- Git dependencies and unknown registries are forbidden by default.
- A Git dependency requires a separate supply-chain/security decision, immutable revision and explicit allow entry.
- Wildcards are forbidden.
- Multiple versions are denied except narrow documented transitive exceptions with owner, reason and removal condition.
- `cargo metadata --locked` is mandatory for validation.

### 8.4 Local lint baseline

The workspace retains at minimum:

```text
unsafe_code = forbid
unused_must_use = deny
clippy::all = deny
clippy::dbg_macro = deny
clippy::expect_used = deny
clippy::panic = deny
clippy::todo = deny
clippy::unimplemented = deny
clippy::unwrap_used = deny
```

A crate may relax a lint only through a reviewed path-local justification. Malformed external input must not produce uncontrolled panics.

### 8.5 Formatting and line endings

- Rustfmt uses edition 2024 and maximum width 100.
- Repository text is normalized to LF through `.gitattributes`; `newline_style = "Native"` is not retained because it creates target-dependent diffs.
- Generated/binary fixture exceptions are explicit.

## 9. Feature and release-role policy

### 9.1 Features

- Features are additive capabilities, not mutually exclusive product identities.
- Security boundaries, protocol selection and environment selection are not hidden behind unrestricted user features.
- `protocol-canary` cannot exist as a feature.
- There is no empty `protocol-oteryn` feature or crate.
- Platform-specific dependencies use Cargo target sections rather than broad optional features where possible.
- Every optional dependency is reachable from one named feature and every feature has an explicit test lane.

### 9.2 Product profiles

Initial profiles are:

1. `client-windows-pre-native`
   - builds `oteryn-client` for `x86_64-pc-windows-msvc`;
   - contains no gameplay protocol adapter, gameplay transport or synthetic fixture dependency in the release closure;
   - launches to the explicit unavailable gameplay state.

2. `client-windows-synthetic-harness`
   - development/test only;
   - enables deterministic client-domain, client-simulation and synthetic asset/render evidence;
   - cannot consume live gameplay credentials or connect to live gameplay endpoints;
   - cannot be packaged as the production client.

3. `shared-linux-validation`
   - builds and tests portable/shared crates and tools for `x86_64-unknown-linux-gnu`;
   - does not claim a Linux desktop client release;
   - prepares the repository for later Linux GameNode members without creating them.

`--all-features` is supplemental supply-chain/compile evidence only. It cannot be the sole product acceptance.

## 10. Dependency boundaries

### 10.1 Categories

`workspace-boundaries.toml` defines these initial categories:

```text
app
foundation
diagnostics
client-runtime
platform-contracts
platform-client
identity
client-domain
client-simulation
input
input-platform
renderer
test-fixture
test-support
test
tool
```

### 10.2 Required direction

```text
apps/client
  -> client-runtime
  -> identity / platform-client / platform-contracts

apps/client
  -> renderer
  -> foundation / diagnostics

apps/client
  -> input-platform
  -> input-actions

client-simulation
  -> client-domain
  -> foundation

synthetic/test consumers
  -> client-domain / client-simulation / renderer / synthetic-assets
```

### 10.3 Mandatory forbidden edges

- `foundation` depends only on the standard library.
- `platform-contracts` cannot depend on HTTP, TLS, Tokio, renderer, input or UI/window code.
- `platform-client` cannot own domain simulation or renderer state.
- `identity` cannot depend on gameplay protocol, gameplay transport or renderer.
- `client-domain` cannot depend on Tokio, TCP, TLS, HTTP, SQL, Platform clients, renderer, assets, winit or wgpu.
- `client-simulation` cannot depend on protocol adapters, TCP, HTTP, Platform clients, renderer implementation, winit or wgpu.
- `renderer` cannot depend on Platform, Identity, protocol, transport or mutable simulation implementation.
- `input-actions` cannot depend on winit or operating-system APIs.
- production crates cannot depend normally or at build time on `test`, `test-support` or `test-fixture` categories.
- no package or feature may contain, depend on or activate `protocol-canary`.
- no dependency path may leave the repository workspace.
- cycles are forbidden across all normal/build/dev workspace edges; dev-only test edges may target product crates but product crates cannot target tests.

## 11. Machine-readable boundary contract

The root `workspace-boundaries.toml` is the canonical dependency policy for Cargo members. At minimum it contains:

```toml
schema_version = 1
source_inventory_revision = "c923ad8a1dff17b4933a6110931b0823cec2c590"

[workspace]
required_prefix = "oteryn-"
forbid_external_path_dependencies = true
forbid_git_dependencies = true
forbid_cycles = true
forbidden_package_names = ["oteryn-protocol-canary"]
forbidden_feature_names = ["protocol-canary", "canary"]

[[package]]
name = "oteryn-client"
path = "apps/client"
category = "app"
release_role = "client-windows-pre-native"
```

The complete file also records every member, release role, allowed normal/dev/build category edges and release-closure exclusions.

`tools/architecture-check` must read this file and `cargo metadata --locked`. The accepted policy is data, not a duplicated hard-coded future package catalogue inside the validator.

The validator must fail for:

- missing/unregistered members;
- duplicate package names or paths;
- unknown categories or release roles;
- forbidden category edges;
- dependency cycles;
- external path dependencies;
- unapproved source/registry/git dependencies;
- forbidden package/feature names;
- test/synthetic crates in the production release closure;
- `protocol-canary`, current Canary contracts or fixtures in any destination Cargo member or release path;
- a production client dependency on protocol, transport or game-session crates before later gates add them;
- package metadata, toolchain or lockfile drift.

## 12. CI and target matrix

The initial exact target triples are:

```text
x86_64-pc-windows-msvc
x86_64-unknown-linux-gnu
```

No Linux desktop-client, macOS, ARM or WebAssembly compatibility claim is made by this contract.

Required CI lanes:

### 12.1 Workspace policy — Ubuntu

- install pinned Rust 1.94.0;
- `cargo metadata --locked --format-version 1`;
- validate `workspace-boundaries.toml`;
- verify package metadata inheritance and root-only lockfile;
- reject forbidden source paths, package names and features;
- run formatting and repository governance.

### 12.2 Shared Linux validation

- target `x86_64-unknown-linux-gnu`;
- compile, Clippy and test all portable/shared/tool/test packages under the named shared profile;
- prove Windows-only dependencies remain target-isolated;
- do not present this as Linux desktop runtime evidence.

### 12.3 Windows client default

- target `x86_64-pc-windows-msvc`;
- build and test `oteryn-client` with its default pre-native graph;
- validate launch/shutdown and renderer surface lifecycle;
- prove the normal dependency closure excludes protocol, gameplay transport and synthetic fixture packages.

### 12.4 Windows synthetic harness

- enable only the named synthetic harness;
- exercise client-domain, client-simulation, renderer and synthetic assets with deterministic fixtures;
- prove no live credential, Gateway game-entry or gameplay endpoint path exists;
- evidence is labeled synthetic and not native E2E.

### 12.5 Security and supply chain

- cargo-deny/advisory/license/source checks for Windows default and Linux shared target graphs;
- all-features check as additional evidence;
- secret/redaction and auth negative tests;
- dependency review and CodeQL/repository checks required by repository policy.

### 12.6 Release-closure negative checks

The release lane fails if `cargo metadata`/`cargo tree` shows any normal/build dependency from `oteryn-client` to:

```text
protocol-canary
protocol-core
protocol-oteryn
transport
game-session
synthetic-assets
test-support
any tests/tools package
```

A later accepted gate may change this list only for its owned capability. `protocol-canary` remains permanently forbidden unless a new owner-approved ADR reverses ADR-0008.

## 13. Canonical supporting contracts

The following destination locations remain canonical:

```text
docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json
docs/contracts/RESOURCE_LIMITS_REGISTRY.json
docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
```

Workspace dependency policy is canonical at:

```text
workspace-boundaries.toml
```

`VSL-02` creates the migration provenance and source-to-destination path mapping under:

```text
docs/migration/rust-client-provenance.json
docs/migration/rust-client-path-map.json
```

Those manifests record source repository, exact source SHA/range, included paths, transformations, exclusions, licenses and final destination merge commit. They do not claim cross-repository Git ancestry under squash merge.

## 14. Identifier ownership during migration

The migration may preserve provisional client representations only inside client/platform boundaries required to compile and test the migrated shell.

It must not claim that current source representations are the canonical meanings of future:

```text
AccountId
CharacterId
WorldId
ChannelId
GameSessionId
SessionGeneration
EntityId
```

Specific safeguards:

- source `AccountSessionId` is client-local correlation and merges into `platform-contracts`;
- source `DirectoryRevision` remains client-local generation evidence;
- source `GameplayChannelId` is not accepted as the final `ChannelId` representation;
- source `SessionGeneration` is renamed to a client-local type before destination acceptance;
- client-domain entity/item handles remain session-local client projection handles;
- no server/shared public crate may depend on these provisional client types before `FND-ID-01`.

## 15. Protocol and transport ownership during migration

The initial workspace contains no gameplay protocol or gameplay transport member.

The following source code remains reference evidence for `FND-02`:

- bounded reader/writer patterns from `protocol-core`;
- Tokio full-duplex lifecycle, queueing, cancellation and deterministic shutdown patterns from `transport`;
- malformed-input and saturation test cases;
- Canary adapter mapping tests where legally and architecturally useful.

`FND-02` must re-evaluate every reused file against the accepted native framing, size limits, endianness, TLS, sequencing and error vocabulary. It may selectively migrate, rewrite or reject those patterns. This contract grants no compatibility claim.

## 16. Synthetic asset and renderer policy

The synthetic asset subsystem is retained only because it provides deterministic, legally bounded renderer and client-simulation evidence before production content exists.

It must:

- use synthetic/project-owned fixtures only;
- live under explicit test/development package and fixture names;
- be absent from the normal release dependency closure and packaging;
- never claim to be the ADR-0005 World Project, World Bundle, Content Registry or production asset format;
- avoid public keys/numeric IDs that could freeze future content identity;
- retain strict allocation, dimension, path and provenance limits;
- be removable without changing production gameplay contracts.

The renderer keeps reusable surface/device/resource lifecycle behavior. Synthetic upload adapters remain test-only. Production asset integration belongs to later content/client gates.

## 17. Crate evolution criteria

A new crate is justified only when at least one is true:

- it owns a distinct trust or security boundary;
- it has a distinct release/target role;
- it prevents a forbidden heavy dependency from leaking into lower layers;
- it owns a stable public contract with at least two immediate consumers;
- it is an executable, tool, platform adapter or FFI boundary that cannot be represented cleanly as a module.

A split is required when:

- one crate mixes producer contracts with I/O implementation;
- target-specific dependencies leak into portable layers;
- production code depends on test/synthetic code;
- client projection types are being mistaken for authoritative server types;
- independent lifecycle, trust, performance or release ownership emerges.

A merge is required when:

- a crate has one trivial type or one consumer;
- the split does not enforce a meaningful dependency/trust/release boundary;
- the crate exists only to mirror an aspirational layer;
- two crates share the same lifecycle and always change together.

No empty crate, future placeholder or one-type convenience crate is accepted.

## 18. VSL-02 handoff

After owner acceptance and merge of `FND-01`, `VSL-02` is the mandatory next gate.

`VSL-02` must:

1. compare source `main` with `c923ad8a1dff17b4933a6110931b0823cec2c590`;
2. select the exact cutover SHA and reconcile every changed Rust path;
3. classify open source PRs/tasks and establish the source freeze;
4. produce exact source-to-destination path and transformation manifests;
5. plan one atomic destination PR implementing every disposition in this document;
6. define rollback before the source is marked non-canonical;
7. validate the destination workspace on exact Windows/Linux matrices;
8. prove the `pre-native-protocol` release closure and fail-closed entry state;
9. merge the destination first;
10. only then create the source-marker PR in `blakinio/otclient`.

No separate import-only destination PR and no post-import workspace cleanup PR are allowed.

## 19. Rejected alternatives

### Copy the source workspace unchanged

Rejected because it imports Canary, Canary-shaped protocol/transport assumptions, fragmented session layers and synthetic systems under production-sounding names.

### Delete all non-binary crates until native protocol exists

Rejected because tested domain, simulation, renderer, input, security and synthetic validation foundations would be lost. They remain only where a named test/tool/product consumer proves immediate value.

### Create empty server or `protocol-oteryn` crates during migration

Rejected because they have no accepted contract or immediate consumer and would falsely imply progress beyond the current gate.

### Keep `transport` and `protocol-core` as generic production foundations

Rejected for the initial graph because their current ceilings and APIs were selected under the source compatibility programme and no pre-native production consumer exists. `FND-02` must decide selective reuse.

### Treat `game-domain` and `simulation-core` as shared authoritative server crates

Rejected because their source contracts explicitly model client projection/session state and immutable render snapshots, not authoritative GameNode state, persistence or command execution.

### Treat synthetic asset packs as the production Oteryn asset format

Rejected because ADR-0005 and later content contracts own the production format, registry, compiler and World Bundle.

## 20. Acceptance checklist

This contract is ready for acceptance only when:

- all 26 source members and relevant non-members are covered exactly once;
- the target graph has no hidden protocol, transport, server or production asset placeholder;
- every initial member has a named consumer and observable acceptance;
- the production release closure is strictly smaller than the complete workspace;
- `workspace-boundaries.toml` requirements are implementable and non-circular;
- Windows/Linux target and product matrices are exact;
- later gate ownership is preserved;
- source revision and open-PR reconciliation are explicit;
- independent review finds no unowned public contract, circular dependency, false compatibility claim or accidental implementation authorization.
