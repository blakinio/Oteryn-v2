# FND-01: Workspace, Dependency and Existing-Rust Migration Contract

- Status: Candidate for owner acceptance
- Date: 2026-08-06
- Coordination ID: `OTV2-NATIVE-FOUNDATION`
- Destination baseline: `blakinio/Oteryn-v2@cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2`
- Source inventory revision: `blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590`
- Exact source evidence: `docs/architecture/FND-01_RUST_SOURCE_INVENTORY.md`
- Applies to: `FND-01`, `VSL-02` and the one atomic destination migration/workspace pull request

## 1. Purpose and authority

This candidate contract defines the Rust workspace that may be created by the controlled native-client migration. It inventories the actual source implementation, classifies every current member, proposes the minimum consumer-backed destination graph and fixes the dependency, build, release-role and machine-enforcement rules required by the migration.

This document does not:

- move source code;
- create the root Cargo workspace;
- implement `protocol-oteryn`;
- freeze public identifier representations;
- authorize gameplay transport, Game Session credentials or admission;
- create an authoritative server runtime;
- make the candidate graph accepted before owner approval.

Physical migration remains owned by `VSL-02` and its one atomic destination pull request.

## 2. Binding decisions

The following accepted decisions constrain this candidate:

- ADR-0001: one native Rust client, one authoritative Rust server and one project-owned `protocol-oteryn`;
- ADR-0002: client/server/shared Rust ownership moves to `blakinio/Oteryn-v2` after `FND-01` and `VSL-02` through one atomic destination migration/workspace PR;
- ADR-0007: later E2E uses one shared three-tier platform with exact evidence and no hidden retry-until-green;
- ADR-0008: `protocol-canary` is `REFERENCE_ONLY` and cannot enter the destination production workspace graph, binaries, negotiation, fallback, translation or release packaging;
- ADR-0011: the migrated client may compile and launch in `pre-native-protocol`, but gameplay entry is visibly unavailable and fails before gameplay credential consumption, Game Session binding or endpoint connection;
- `FND-ID-01` owns cross-boundary identifier meaning and representation;
- `FND-02` owns native protocol framing, schema, transport limits, TLS, sequencing and compatibility;
- `FND-04` owns exact Game Session, credential, admission and character-lease behavior;
- ADR-0005 and later content gates own the production world/content/asset formats; synthetic fixture packs are not that contract.

## 3. Exact source evidence

The complete source member, dependency, consumer, direct third-party and non-member inventory is canonical evidence at:

```text
docs/architecture/FND-01_RUST_SOURCE_INVENTORY.md
```

That inventory proves:

- 26 source workspace members;
- a Windows-only target/toolchain baseline;
- direct Canary dependencies from the application and technical-login tests;
- Canary-specific entry policy in `game-session`;
- an over-fragmented account/directory/entry stack;
- client-only domain/simulation semantics;
- synthetic-only asset/resource formats;
- source `protocol-core` and `transport` ceilings that cannot become native limits by inertia;
- three open source PRs that do not currently change the Rust workspace but remain `VSL-02` reconciliation inputs.

Any source change after `c923ad8a1dff17b4933a6110931b0823cec2c590` invalidates affected inventory rows until `VSL-02` reconciles the selected cutover SHA. It does not silently amend this contract.

## 4. Proposed initial destination workspace

The atomic destination migration should create exactly these initial members:

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
tools/synthetic-client-harness
```

Proposed package names:

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
oteryn-synthetic-client-harness
```

The initial workspace deliberately excludes:

```text
services/game-server
apps/oteryn-studio
crates/protocol-canary
crates/protocol-core
crates/protocol-oteryn
crates/transport
crates/game-session
persistence, world, content, scripting and server-runtime crates
```

Their absence is intentional. Later gates may add only members with an immediate accepted consumer and an owned contract.

## 5. Why the synthetic harness is a separate executable

The production-shaped `oteryn-client` binary must not carry optional normal dependencies on client simulation or synthetic fixture packages merely because a feature is disabled by default. Cargo optional dependencies still enlarge the package's declared trust and maintenance surface.

Therefore deterministic renderer/domain/simulation evidence uses:

```text
tools/synthetic-client-harness
```

The harness is a separate non-release executable. It may depend on `client-domain`, `client-simulation`, `renderer`, `input-actions`, `input-platform`, `synthetic-assets`, `test-support` and `foundation`.

It must not:

- consume live Identity or gameplay credentials;
- call live Game Gateway or gameplay endpoints;
- be packaged as the production client;
- claim protocol, server, admission or native E2E compatibility;
- share a release role with `oteryn-client`.

This separation keeps the production dependency closure provably smaller than the complete workspace.

## 6. Proposed member consumers and migration acceptance

| Destination member | Immediate consumer or purpose | Observable acceptance |
|---|---|---|
| `apps/client` | production-shaped pre-native shell | builds, launches and shuts down on Windows; gameplay is explicitly unavailable before sensitive boundaries |
| `foundation` | lower client layers | deterministic cancellation, monotonic-time and local-generation tests |
| `diagnostics` | runtime, Platform client and test support | bounded/redacted diagnostic tests |
| `client-runtime` | app and pre-native tests | deterministic lifecycle and shutdown with no gameplay adapter |
| `platform-contracts` | Platform client, Identity, runtime and auth tests | bounded DTO-neutral account/directory values using explicitly provisional client references |
| `platform-client` | Identity/runtime and auth tests | validated account/directory HTTP boundary; no gameplay-ticket/admission implementation |
| `identity` | runtime and auth tests | PKCE, callback, stale-operation, cancellation and secret-redaction evidence |
| `client-domain` | client simulation and synthetic harness | typed client command/event and stale-session tests |
| `client-simulation` | synthetic harness | deterministic event application and immutable snapshot tests |
| `input-actions` | input adapter, app and harness | normalized semantic-action tests |
| `input-platform` | app and harness | target-isolated Windows/winit adapter evidence |
| `renderer` | app and harness | surface lifecycle, device/resource recovery and bounded synthetic-scene evidence |
| `synthetic-assets` | fixture compiler and harness | deterministic fixture pack/decode tests; no production asset claim |
| `test-support` | integration tests and harness | deterministic fixtures, clocks and safe diagnostics |
| `tests/security/auth` | Identity/Platform boundary | exact negative and lifecycle security scenarios |
| `tests/pre-native-client` | ADR-0011 | proves no protocol adapter, gameplay credential consumption, Game Session binding, endpoint connection or false success |
| `architecture-check` | entire workspace | validates locked Cargo metadata against `workspace-boundaries.toml` |
| `synthetic-asset-compiler` | fixture pipeline | deterministic compilation, path-safety and provenance tests |
| `synthetic-client-harness` | deterministic client foundation evidence | separate executable runs bounded domain/simulation/input/renderer scenarios without live services |

## 7. Per-member migration dispositions

The disposition vocabulary is closed:

```text
MIGRATE_AS_IS
MIGRATE_AND_RENAME
MERGE
SPLIT
REWRITE
REFERENCE_ONLY
DROP
```

| Source member | Disposition | Destination / rule | Reason |
|---|---|---|---|
| `apps/client` | `REWRITE` | `apps/client` | retain useful Windows shell/render composition; remove Canary and W7 entry wiring; expose explicit pre-native state |
| `crates/account-session` | `MERGE` | `platform-contracts` | one client-local correlation ID does not justify a crate |
| `crates/app-runtime` | `MIGRATE_AND_RENAME` | `client-runtime` | retain application-owned Tokio orchestration and deterministic shutdown; remove W7/Canary policy |
| `crates/asset-decode` | `MERGE` | `synthetic-assets` | synthetic decoder is fixture infrastructure |
| `crates/asset-types` | `MERGE` | `synthetic-assets` | synthetic pack schema is not a production asset contract |
| `crates/asset-runtime` | `MERGE` | `synthetic-assets` | synthetic pack runtime remains non-release fixture infrastructure |
| `crates/diagnostics` | `MIGRATE_AS_IS` | `diagnostics` | independent bounded/redacted boundary with immediate consumers |
| `crates/foundation` | `REWRITE` | `foundation` | retain clocks, cancellation and technical generations; rename/remove `SessionGeneration` semantics reserved for `FND-ID-01` |
| `crates/game-domain` | `MIGRATE_AND_RENAME` | `client-domain` | useful protocol-neutral client projection, not authoritative server domain |
| `crates/simulation-core` | `MIGRATE_AND_RENAME` | `client-simulation` | deterministic client writer/snapshots, not GameNode runtime |
| `crates/input-actions` | `MIGRATE_AS_IS` | `input-actions` | clean framework-neutral semantic boundary |
| `crates/input-platform` | `MIGRATE_AS_IS` | `input-platform` | clean target-specific adapter boundary; app/harness become named consumers |
| `crates/game-session` | `SPLIT` | safe non-secret selection/value logic into `platform-contracts`; client orchestration into `client-runtime`; credential/profile/admission code deferred | current crate mixes client lifecycle, secrets and `CanaryCurrent`; `FND-04` owns the future contract |
| `crates/identity` | `REWRITE` | `identity` | retain PKCE/browser/loopback security; remove gameplay-credential and Canary-oriented lifecycle dependencies |
| `crates/platform` | `SPLIT` | validated non-gameplay values in `platform-contracts`; account/directory I/O in `platform-client`; Game Session issuance/admission deferred | separate value contracts from I/O and later admission ownership; source blocking `ureq` adapter is not automatically accepted |
| `crates/protocol-canary` | `REFERENCE_ONLY` | source repository/provenance only | ADR-0008 |
| `crates/protocol-core` | `REFERENCE_ONLY` | reconsider under `FND-02` | current little-endian helpers and 64-KiB ceiling cannot freeze native framing |
| `crates/renderer` | `MIGRATE_AS_IS` | `renderer` | surface/device owner has a production-shell consumer; metadata and target policy are rewritten at root |
| `crates/renderer-resource` | `SPLIT` | backend-neutral generation/cache/resource logic into `renderer`; synthetic adapters/tests into `synthetic-assets` or harness tests | direct synthetic dependencies must not leak into production renderer |
| `crates/test-support` | `MIGRATE_AS_IS` | `test-support` | multiple test/harness consumers |
| `crates/transport` | `REFERENCE_ONLY` | reconsider under `FND-02` | no initial gameplay consumer and current frame ceiling conflicts with unresolved native limits |
| `crates/world-directory` | `MERGE` | `platform-contracts` | directory values and selection validation belong together; source identifiers remain provisional |
| `tests/integration/technical-login` | `REFERENCE_ONLY` | rewrite only non-Canary scenarios into `pre-native-client` and auth tests | direct Canary/transport/late-credential behavior violates the initial state |
| `tests/security/auth` | `REWRITE` | `tests/security/auth` | preserve security scenarios against consolidated boundaries |
| `tools/architecture-check` | `REWRITE` | `tools/architecture-check` | policy becomes data in `workspace-boundaries.toml`, not a hard-coded aspirational catalogue |
| `tools/asset-compiler` | `MIGRATE_AND_RENAME` | `synthetic-asset-compiler` | name must not imply ownership of the future production asset compiler |

Every source member appears exactly once. `REFERENCE_ONLY` code is not copied into Cargo membership, release packaging or destination product paths. Later selective reuse requires the owning gate and explicit provenance.

## 8. Non-member dispositions

| Source subsystem | Disposition | Destination rule |
|---|---|---|
| `assets/test-fixtures` | `MIGRATE_AND_RENAME` | `tests/fixtures/synthetic-assets` with project-owned/synthetic provenance |
| `contracts/canary` | `REFERENCE_ONLY` | source history only |
| source architecture and agent docs | `REFERENCE_ONLY` | link for provenance; destination ADRs/governance are authoritative |
| source root `Cargo.toml` | `REWRITE` | one destination root manifest using the accepted FND-01 graph |
| source `Cargo.lock` | `REWRITE` | regenerate one destination lockfile; preserve source blob and produce direct/transitive dependency delta evidence |
| source `rust-toolchain.toml` | `REWRITE` | retain Rust 1.94.0; add accepted Windows and Linux targets |
| source `rustfmt.toml` | `REWRITE` | retain edition/width; normalize repository text to LF rather than target-dependent native endings |
| source `deny.toml` | `REWRITE` | product-realistic Windows default and Linux shared graphs; all-features supplemental |
| source Rust CI | `REWRITE` | destination target/product matrix and release-closure negative checks |
| source protocol fixtures | `REFERENCE_ONLY` | no Canary fixture enters destination product contracts |

## 9. Provisional identifier safeguards

The destination migration must not preserve source names that can be mistaken for accepted cross-boundary identifiers.

Before destination acceptance:

```text
AccountSessionId       -> ClientAccountContextId
DirectoryRevision      -> ClientDirectoryGeneration
GameplayChannelId      -> DirectoryChannelRef
source WorldId         -> DirectoryWorldRef
source CharacterId     -> DirectoryCharacterRef
source SessionGeneration -> ClientSessionEpoch or another explicitly client-local name
```

Exact names may be refined by the migration implementation, but every retained type must state:

- client-local or producer-opaque scope;
- no durable/global uniqueness claim;
- no authority outside the owning process/boundary;
- no commitment to future wire or database representation.

Client-domain entity/item handles remain client projection handles. No server/shared crate may depend on these provisional types before `FND-ID-01`.

## 10. Platform and Identity boundary during migration

`platform-contracts` owns validated, DTO-neutral, non-secret account and directory values used by the native client. It is not the raw JSON schema and does not independently redefine the external Platform contract.

`platform-client` owns account-authentication and account-directory HTTP adaptation only. The initial migration must not implement or retain a live gameplay-ticket/Game Session issuance path.

The source blocking `ureq` implementation is reference evidence. `VSL-02` must select one of two explicit outcomes:

1. an audited asynchronous, cancellation-safe Platform HTTP implementation owned by the application Tokio runtime; or
2. a bounded dedicated blocking worker with deadlines, cancellation, deterministic shutdown and proof that no event/render thread can block.

Silent blocking on the window/event/frame thread is forbidden. The chosen HTTP/TLS dependency, feature set and certificate-root behavior must be recorded in the migration dependency delta.

Identity may retain PKCE, system-browser and loopback callback behavior. It may not depend on gameplay protocol, gameplay transport, Game Session credential types or admission state.

## 11. Root Cargo and repository policy

The destination root owns exactly one:

```text
Cargo.toml
Cargo.lock
rust-toolchain.toml
rustfmt.toml
deny.toml
workspace-boundaries.toml
```

Root package policy:

```text
edition = 2024
rust-version = 1.94
resolver = 3
license = MIT
repository = https://github.com/blakinio/Oteryn-v2
publish = false
```

Rules:

- members inherit edition, rust-version, license, repository, workspace dependencies and lints;
- no member owns another lockfile;
- direct third-party dependencies are declared once and pinned to exact reviewed versions during migration;
- path dependencies remain inside the workspace;
- Git dependencies and unknown registries are forbidden by default;
- wildcards are forbidden;
- multiple transitive versions require a narrow documented exception with owner, reason and removal condition;
- `cargo metadata --locked` is mandatory;
- source lockfile blob `2143408c12c50132883890f0821278320a331fde` remains provenance evidence and the destination records a dependency delta;
- Rustfmt uses edition 2024, width 100 and LF-normalized repository text.

Minimum lint baseline:

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

A local relaxation requires a path-scoped documented reason. Malformed external input must not produce an uncontrolled panic.

## 12. Closed dependency policy

Initial categories:

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

### 12.1 Allowed normal category edges

The following normal workspace edges are the complete initial allowlist. Absence means forbidden.

| Source category | Allowed normal target categories |
|---|---|
| `app` | `foundation`, `diagnostics`, `client-runtime`, `input-platform`, `renderer` |
| `foundation` | none |
| `diagnostics` | `foundation` |
| `client-runtime` | `foundation`, `diagnostics`, `identity`, `platform-contracts`, `platform-client` |
| `platform-contracts` | `foundation` |
| `platform-client` | `foundation`, `diagnostics`, `platform-contracts` |
| `identity` | `foundation`, `diagnostics`, `platform-contracts`, `platform-client` |
| `client-domain` | `foundation` |
| `client-simulation` | `foundation`, `client-domain` |
| `input` | none |
| `input-platform` | `input` |
| `renderer` | `foundation`, `diagnostics` |
| `test-fixture` | `foundation` |
| `test-support` | `foundation`, `diagnostics` |
| `test` | every product category plus `test-fixture` and `test-support` |
| `tool` | `foundation`, `diagnostics`, `client-domain`, `client-simulation`, `input`, `input-platform`, `renderer`, `test-fixture`, `test-support` |

Package-specific policy further narrows tool edges:

- `architecture-check` has no normal workspace dependency;
- `synthetic-asset-compiler` depends only on `synthetic-assets` among workspace members;
- `synthetic-client-harness` may depend only on the exact client foundation packages named in Section 5.

### 12.2 Development and build edges

- Product crates may use `test-support` and `synthetic-assets` only as development dependencies.
- Tests and tools may normally depend on product/test packages according to the allowlist.
- No workspace build dependency is accepted initially.
- Production crates cannot normally or at build time depend on `test`, `test-support`, `test-fixture` or `tool` categories.
- Dev dependencies participate in cycle detection; no cycle is accepted merely because one edge is dev-only.

### 12.3 Permanent and gate-specific forbidden edges

Permanent:

- any package/feature/dependency named `protocol-canary` or unrestricted `canary` compatibility;
- external path dependencies;
- workspace cycles;
- `foundation` to any workspace crate;
- `client-domain`/`client-simulation` to Tokio, TCP, TLS, HTTP, SQL, Platform I/O, renderer implementation, winit or wgpu;
- renderer to Identity, Platform, protocol, transport or mutable simulation implementation;
- input actions to winit/OS APIs;
- production to test/tool/fixture code.

Before later gates:

- production app to gameplay protocol, gameplay transport or Game Session/admission crates;
- any server/shared public crate to provisional client identifier types;
- production renderer to synthetic asset packages.

## 13. Machine-readable enforcement

The root `workspace-boundaries.toml` is the canonical Cargo dependency/release-role policy. It records:

- schema version;
- FND-01 source inventory revision;
- every package name, path, category and release role;
- allowed normal/dev/build category edges;
- package-specific narrowed edges;
- forbidden names/features/sources;
- production release-closure exclusions;
- metadata/toolchain/lockfile rules.

Minimum shape:

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

`tools/architecture-check` reads this file and `cargo metadata --locked`. It must not duplicate an aspirational future crate catalogue in Rust source.

The validator fails for:

- unregistered/missing/duplicate members;
- unknown categories or release roles;
- forbidden or undeclared edges;
- cycles across normal/dev/build edges;
- external path, Git or unknown-registry dependencies;
- forbidden package/feature names;
- test/tool/fixture packages in the production release closure;
- protocol, gameplay transport or Game Session dependencies in the pre-native app closure;
- synthetic assets in the production renderer/client closure;
- metadata, toolchain or root-lockfile drift.

## 14. Features and release roles

Features are additive capabilities, not product identities, environments, protocol selectors or security-boundary bypasses.

- There is no Canary feature.
- There is no empty native-protocol feature or crate.
- Platform-specific dependencies use Cargo target sections where practical.
- Every optional dependency belongs to one named feature and one explicit CI lane.
- The synthetic harness is a separate package, not a feature that changes the production binary's identity.

Initial release/validation roles:

### `client-windows-pre-native`

- target `x86_64-pc-windows-msvc`;
- builds `oteryn-client` default graph;
- excludes protocol, gameplay transport, Game Session, synthetic fixtures, test support, tests and tools;
- launches to explicit gameplay-unavailable state.

### `synthetic-client-harness`

- target `x86_64-pc-windows-msvc` initially;
- separate non-release executable;
- deterministic client domain/simulation/input/renderer/fixture scenarios;
- no live credential or endpoint access.

### `shared-linux-validation`

- target `x86_64-unknown-linux-gnu`;
- builds/tests portable shared crates, tests and tools selected by policy;
- proves Windows dependencies remain target-isolated;
- does not claim a Linux desktop-client release or GameNode implementation.

`--all-features` is supplemental supply-chain/compile evidence only.

## 15. CI matrix

Required lanes:

1. **Workspace policy / Ubuntu**
   - pinned Rust 1.94.0;
   - locked metadata;
   - `workspace-boundaries.toml` validation;
   - package metadata, source, feature, cycle and root-lockfile checks;
   - format and repository governance.

2. **Shared Linux validation**
   - `x86_64-unknown-linux-gnu`;
   - compile, Clippy and tests for the named portable/shared/test/tool selection;
   - no Linux desktop-runtime claim.

3. **Windows pre-native client**
   - `x86_64-pc-windows-msvc`;
   - default client build/tests;
   - deterministic launch/shutdown and renderer lifecycle;
   - ADR-0011 negative entry evidence;
   - production dependency-closure audit.

4. **Windows synthetic harness**
   - separate harness build/run;
   - deterministic domain/simulation/input/renderer/asset fixtures;
   - explicit synthetic labeling and no live-network capability.

5. **Security and supply chain**
   - advisory/license/source checks for Windows default and Linux shared graphs;
   - all-features supplemental check;
   - auth/secret/redaction negative tests;
   - repository-required Dependency Review and CodeQL.

The production release lane fails if `cargo tree`/metadata shows any normal or build dependency from `oteryn-client` to:

```text
protocol-canary
protocol-core
protocol-oteryn
transport
game-session
client-domain
client-simulation
synthetic-assets
test-support
any tests or tools package
```

A later accepted gate may change only entries it owns. Canary remains forbidden unless a new owner-approved ADR reverses ADR-0008.

## 16. Protocol and transport source treatment

The initial workspace contains no gameplay protocol or transport member.

Useful source evidence retained for `FND-02` includes:

- bounded reader/writer patterns;
- Tokio full-duplex task ownership, queues, cancellation and deterministic joined shutdown;
- malformed/truncated/saturation tests;
- protocol-neutral adapter-domain mapping cases.

`FND-02` must re-evaluate any reused file against accepted native framing, maximums, endianness, TLS, sequencing, acknowledgement, replay and error contracts. This candidate grants no wire compatibility claim.

## 17. Synthetic asset and renderer policy

Synthetic assets remain only because they provide deterministic, legally bounded renderer and client-simulation evidence before production content exists.

They must:

- use synthetic/project-owned fixtures;
- live under explicit fixture/test/tool names;
- be absent from production client and renderer dependency closures;
- never claim to implement ADR-0005 World Project, World Bundle, Content Registry or production asset format;
- avoid identifiers that freeze future content identity;
- retain bounded allocation, dimensions, paths and provenance;
- be removable without changing production contracts.

The renderer retains production-usable surface/device/resource lifecycle code. Any source resource code directly coupled to synthetic assets is split so the adapter remains test/harness-only.

## 18. Crate evolution criteria

A new crate is justified only when at least one is true:

- distinct trust/security boundary;
- distinct target or release role;
- prevents heavy/unsafe/platform dependency leakage;
- owns a stable public contract with at least two immediate consumers;
- executable, tool, platform/FFI adapter or separately governed boundary.

Split when one crate mixes value contracts with I/O, target-specific code leaks downward, production depends on fixtures/tests, or client projection is confused with server authority.

Merge when a crate owns one trivial type, has one consumer without a meaningful trust/release boundary, mirrors an aspirational layer or always changes with another crate.

No empty crate, future placeholder or one-type convenience crate is accepted.

## 19. Canonical supporting locations

Existing canonical contracts remain:

```text
docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json
docs/contracts/RESOURCE_LIMITS_REGISTRY.json
docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
```

Workspace policy:

```text
workspace-boundaries.toml
```

`VSL-02` migration evidence:

```text
docs/migration/rust-client-provenance.json
docs/migration/rust-client-path-map.json
docs/migration/rust-dependency-delta.json
```

The manifests record exact source SHA/range, paths, transformations, exclusions, license/provenance, dependency changes and final destination merge. They do not claim cross-repository Git ancestry under squash merge.

## 20. VSL-02 handoff

After owner acceptance and merge of `FND-01`, `VSL-02` is the mandatory next gate.

It must:

1. compare source `main` with the FND-01 inventory revision;
2. pin the exact cutover SHA and reconcile every changed Rust/non-member path;
3. classify all open PRs and active tasks and establish a source freeze;
4. produce exact provenance, path-map and dependency-delta manifests;
5. plan one atomic destination PR implementing every accepted disposition;
6. define rollback before the source is marked non-canonical;
7. validate exact Windows/Linux/product-role matrices;
8. prove the pre-native production closure and fail-closed entry state;
9. merge the destination first;
10. only then create the source-marker PR in `blakinio/otclient`.

No separate import-only destination PR and no post-import workspace-cleanup destination PR are allowed.

## 21. Rejected alternatives

### Copy the source workspace unchanged

Rejected because it imports Canary, Canary-shaped protocol/transport assumptions, fragmented session layers and synthetic systems under production-sounding names.

### Keep client simulation/fixtures as optional dependencies of the production app

Rejected because optional normal dependencies still enlarge the production package's declared graph and can be accidentally enabled or packaged. A separate harness provides cleaner proof.

### Delete all non-binary crates until native protocol exists

Rejected because tested client domain, simulation, renderer, input, security and synthetic foundations have immediate test/tool consumers when accurately labeled.

### Create empty server or native-protocol crates during migration

Rejected because no accepted immediate contract/consumer exists.

### Keep source transport/protocol-core as generic production foundations

Rejected initially because their current limits/API are source-programme shaped and there is no pre-native production consumer. `FND-02` owns selective reuse.

### Treat client domain/simulation as authoritative server crates

Rejected because their source contracts model client projection and render snapshots, not GameNode authority, persistence or command execution.

### Treat synthetic packs as production assets

Rejected because ADR-0005 and later content gates own those formats.

## 22. Acceptance conditions

This candidate is ready for owner acceptance only when:

- all 26 source members and relevant non-members are inventoried exactly once;
- proposed dispositions cover each member exactly once;
- the target graph is acyclic and every member has an immediate consumer;
- production and synthetic executables have separate dependency/release closures;
- no provisional identifier can be confused with an accepted FND-ID-01 identifier;
- blocking Platform I/O cannot reach the frame/event thread;
- protocol, transport, admission and content gate ownership remains intact;
- the machine-readable policy is implementable without hidden package exceptions;
- independent audit finds zero open material contradictions or accidental implementation authorization;
- the owner explicitly accepts the proposed graph and disposition policy.
