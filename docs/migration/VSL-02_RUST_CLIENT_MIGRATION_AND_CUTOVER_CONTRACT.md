# VSL-02: Exact Rust Client Migration and Cutover Contract

- Status: candidate for exact-head audit and merge
- Date: 2026-08-06
- Coordination ID: `OTV2-RUST-CLIENT-CUTOVER-20260806`
- Destination repository: `blakinio/Oteryn-v2`
- Destination contract base: `9034bd4bfa491eac6a898b29bc8151c94a4c2b89`
- Source repository: `blakinio/otclient`
- Source subtree: `oteryn-client/`
- Selected cutover commit: `c923ad8a1dff17b4933a6110931b0823cec2c590`
- Governing workspace contract: `docs/architecture/FND-01_WORKSPACE_AND_RUST_MIGRATION_CONTRACT.md`
- Machine path map: `docs/migration/rust-client-path-map.json`
- Machine provenance/rollout plan: `docs/migration/rust-client-provenance-plan.json`

## 1. Purpose and authority

This contract determines the only permitted migration of the existing Rust client from `blakinio/otclient/oteryn-client` into the canonical `blakinio/Oteryn-v2` Rust workspace.

It converts the accepted FND-01 dispositions into an exact cutover package:

- one immutable source revision;
- one source-to-destination path map;
- one atomic destination implementation pull request;
- one root Cargo workspace and lockfile;
- truthful provenance without false cross-repository ancestry;
- a product-realistic validation and equivalence matrix;
- no Canary, gameplay transport or speculative native protocol;
- destination-first rollout and a later source-only moved marker;
- rollback that never leaves zero or two writable canonical Rust clients.

This contract does not move code. The implementation task created after this contract merges owns the atomic destination PR. A later separately authorized task owns the source-marker PR in `blakinio/otclient`.

## 2. Binding decisions

The following remain binding:

- ADR-0002: `blakinio/Oteryn-v2` becomes the canonical Rust client/server/shared workspace through destination-first migration.
- ADR-0008: `protocol-canary` is `REFERENCE_ONLY` and cannot enter destination Cargo membership, product binaries, fallback, negotiation, translation or packaging.
- ADR-0011: the migrated client launches in explicit `pre-native-protocol`; gameplay entry fails before gameplay credential consumption, Game Session binding or gameplay endpoint connection.
- FND-01: the initial destination workspace has exactly 19 named members and the accepted per-source dispositions.
- `FND-ID-01`: later public identifier meanings and representations remain unfrozen.
- `FND-02`: native protocol/framing/gameplay transport remains absent.
- `FND-04`: Game Session credential, routing, admission and character lease behavior remains absent.

VSL-02 may select migration tooling and dependencies needed to implement FND-01, but it may not capture later protocol, runtime, admission or durable-gameplay contracts.

## 3. Exact cutover source

The selected and frozen source is:

```text
repository: blakinio/otclient
commit: c923ad8a1dff17b4933a6110931b0823cec2c590
subtree: oteryn-client/
root manifest blob: 037013e8e4a762a65f0f2a30f7761ee14725a3fc
root lockfile blob: 2143408c12c50132883890f0821278320a331fde
```

`VSL-02_SOURCE_RECONCILIATION.md` proves that the source default branch still equals the FND-01 inventory revision and that no open PR changes the Rust subtree.

The implementation task must not silently use a newer commit, PR head, local working tree, archive generated from another revision or mutable URL. Any source-subtree drift blocks the atomic import until this contract is explicitly amended and re-audited.

## 4. Atomic destination implementation package

The implementation uses one dedicated branch:

```text
migrate/rust-client-cutover-c923ad8
```

and one destination PR targeting `blakinio/Oteryn-v2:main`.

The single PR must contain all of the following or it is incomplete:

1. the canonical root Cargo workspace with the 19 accepted members;
2. all accepted source migrations, merges, splits, renames and rewrites;
3. explicit omission of every `REFERENCE_ONLY` source path;
4. the launchable Windows `pre-native-protocol` client state;
5. the separate non-release synthetic client harness;
6. root `Cargo.lock`, `rust-toolchain.toml`, `rustfmt.toml`, `deny.toml` and `workspace-boundaries.toml`;
7. the machine-enforced FND-01 dependency and release-role graph;
8. destination Rust workflows and exact Windows/Linux matrices;
9. finalized per-file provenance, path map and dependency delta;
10. source/destination equivalence and transformation evidence;
11. exact negative closure evidence proving Canary, gameplay transport, Game Session and synthetic/test packages are absent from the production client dependency closure;
12. migration/rollback documentation and the exact later source-marker handoff.

The following split delivery is forbidden:

```text
PR A: copy source
PR B: remove Canary
PR C: create workspace/CI
PR D: fix boundaries
```

The destination must never contain a merged intermediate state that is canonical but violates FND-01 or ADR-0011.

## 5. Initial destination workspace

The atomic PR creates exactly:

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

No other Cargo member may be introduced by the migration PR. In particular, it must not create:

```text
protocol-canary
protocol-core
protocol-oteryn
transport
game-session
game-server
session-lease
persistence
world/content/scripting production crates
```

An implementation detail placed inside an accepted member does not authorize a hidden later-gate contract. The architecture checker must reject package aliases, features or paths that recreate a forbidden member under another name.

## 6. Source-to-destination mapping

The normative machine mapping is `rust-client-path-map.json`. It records all 26 source workspace members, non-member root/config paths, new destination-only harness ownership and permanent exclusions.

Implementation requirements:

- every source workspace member appears exactly once in the finalized path map;
- every copied or transformed source file receives a source blob SHA and destination path in `rust-client-provenance.json`;
- every destination Rust source file is classified as migrated/transformed or destination-authored;
- destination-authored glue cannot be mislabeled as migrated source;
- merged/split crates use stable destination modules declared by the mapping instead of temporary import directories;
- no `legacy/`, `old/`, `_tmp`, `imported/` or duplicate source-tree staging path is committed;
- no source manifest, lockfile, workflow or governance file is copied as destination authority.

### 6.1 Reference-only exclusions

These remain reachable only through source repository links and immutable SHAs:

```text
oteryn-client/crates/protocol-canary/**
oteryn-client/crates/protocol-core/**
oteryn-client/crates/transport/**
oteryn-client/contracts/canary/**
oteryn-client/docs/architecture/**
oteryn-client/docs/agents/**
oteryn-client/AGENTS.md
```

Useful algorithms or tests in `protocol-core`/`transport` may be reconsidered only by `FND-02`. The migration PR cannot copy them into an unregistered utility module to bypass the disposition.

### 6.2 Generated/binary/private exclusions

No build output, binary, debug symbol, cache, credential, environment file or proprietary Tibia/CipSoft asset may enter the destination. The finalized provenance validator must fail on any excluded pattern listed in the machine path map.

## 7. Provenance and history truthfulness

Cross-repository Git ancestry is not preserved by a squash-merged content migration. The project therefore uses immutable, machine-readable provenance instead of a false history claim.

The atomic PR produces:

```text
docs/migration/rust-client-provenance.json
docs/migration/rust-client-path-map.json
docs/migration/rust-dependency-delta.json
```

For every destination file derived from source, provenance records:

```text
source_repository
source_commit
source_path
source_blob_sha
destination_path
disposition
transformation
license
verification
```

Rules:

- the source repository and exact commit remain permanent historical evidence;
- rewritten files are never called byte-identical;
- no fabricated co-author or copied commit author list is added;
- source copyright/license notices are preserved where applicable;
- project-authored transformations are attributed to the destination PR;
- no proprietary asset is imported merely because a source test or document referenced it;
- the final squash commit message links the coordination ID and source revision.

The source subtree is not deleted after migration. This preserves legal, design and blame evidence without pretending that destination Git ancestry contains the source commits.

## 8. Dependency selection and delta

### 8.1 Toolchain and existing reviewed runtime

The migration retains:

```text
Rust: 1.94.0
edition: 2024
resolver: 3
Tokio: =1.51.4
```

Tokio remains exact-pinned during cutover to avoid combining repository migration with a runtime upgrade. Package-specific feature policy:

```text
normal runtime: io-util, net, rt-multi-thread, sync, time
test-only where required: macros, test-util
```

Features remain least-capability and package-scoped. A test feature must not enlarge the production client closure.

### 8.2 Async Platform/Identity HTTP

The selected replacement for source blocking `ureq` is:

```toml
reqwest = {
  version = "=0.13.4",
  default-features = false,
  features = ["form", "json", "rustls", "stream"]
}
```

This selection is compatible with the accepted Rust toolchain because the selected crate declares an MSRV below Rust 1.94. It provides the asynchronous Tokio client and explicit rustls backend required by FND-01.

Forbidden reqwest capabilities in the initial graph:

```text
blocking
cookies
gzip, brotli, zstd, deflate
multipart
socks
system-proxy
native-tls, native-tls-vendored
http2, http3
```

Required client-builder policy:

- use the rustls backend explicitly;
- automatic redirects disabled;
- automatic proxy discovery disabled;
- cookie storage disabled;
- transparent response decompression disabled;
- certificate and hostname validation cannot be disabled;
- no production custom CA or certificate pin is added during migration;
- request body, response headers, response chunks and total response body are bounded;
- connect, request and total operation deadlines are explicit;
- cancellation belongs to the application-owned Tokio runtime;
- cancellation and shutdown must terminate request tasks without leaking secrets or workers;
- secrets are redacted from `Debug`, diagnostics and errors.

The exact dependency graph is generated into the destination lockfile and reviewed by cargo-deny, Dependency Review and `rust-dependency-delta.json`.

### 8.3 Removed source dependencies

The migration removes direct production use of:

```text
ureq
native-tls used by the source blocking Platform adapter
protocol-canary dependencies
protocol-core dependencies
transport dependencies
game-session dependencies
```

A transitive package with a similar name is not automatically prohibited, but it must be explained by the lockfile delta and must not enable a forbidden runtime capability.

### 8.4 Existing source dependencies

Other direct source dependencies retain exact versions during cutover unless a target split or accepted merge makes them unnecessary. Any change beyond repository/path/package renaming must appear in `rust-dependency-delta.json` with reason, affected packages, features, license and security review.

No opportunistic broad dependency upgrade is allowed in the atomic migration PR.

## 9. Pre-native product behavior

The production `oteryn-client` binary must:

- build for `x86_64-pc-windows-msvc`;
- launch a real window/application shell;
- initialize permitted Platform account/directory and Identity boundaries;
- expose an explicit user-facing state that native gameplay is unavailable in this build;
- never advertise Canary or protocol selection;
- fail before gameplay credential request/consumption;
- fail before Game Session binding;
- fail before any gameplay endpoint DNS resolution or connection;
- never present synthetic harness success as live gameplay;
- shut down deterministically with no worker/task leak.

The production client may display bounded account/world/character directory metadata only when it contains no gameplay host, port, endpoint, protocol selector, admission token or Game Session credential.

## 10. Synthetic harness behavior

`oteryn-synthetic-client-harness` is a separate non-release executable. It is the named immediate consumer for client-domain, client-simulation, input, renderer, synthetic-assets and test-support.

It must:

- use project-owned deterministic fixtures only;
- run without Identity, Platform or gameplay network capability;
- provide bounded scenes and deterministic expected snapshots;
- exercise migrated domain/simulation/input/renderer/resource behavior;
- never enter production installer/package manifests;
- never be a production client feature;
- never claim protocol, server or shared three-tier E2E compatibility.

The production client cannot depend normally or at build time on the harness, client simulation, synthetic assets or test support.

## 11. Equivalence and transformation evidence

Migration evidence is based on disposition, not a false blanket byte-equivalence claim.

### `MIGRATE_AS_IS`

Required:

- source and destination public-item inventory;
- source test catalogue and destination test result;
- semantic diff limited to crate path/package/repository metadata and accepted identifier rename propagation;
- source blob and destination blob references.

### `MIGRATE_AND_RENAME`

Required:

- package/API rename table;
- source-to-destination symbol map;
- same focused behavioral tests or explicitly documented strengthened replacements;
- proof that client ownership terminology changed without changing the preserved behavior.

### `MERGE`

Required:

- source modules mapped into exact destination modules;
- duplicate type/error/limit reconciliation table;
- no reverse dependency/cycle introduced;
- tests retained at the new owner.

### `SPLIT`

Required:

- source public items classified as retained, rewritten, deferred or dropped;
- each retained item has exactly one destination owner;
- deferred gameplay credential/route/protocol semantics are absent from destination symbols and closures;
- no hidden compatibility shim recreates the source crate.

### `REWRITE`

Required:

- preserved security/behavior scenarios named explicitly;
- discarded assumptions named explicitly;
- destination tests prove the new boundary;
- no compatibility claim based solely on source tests.

### `REFERENCE_ONLY`

Required:

- source path/SHA remains in provenance plan;
- zero destination Cargo member/source copy;
- no release artifact contains the code or fixtures.

## 12. Root workspace and machine enforcement

The atomic PR creates one root:

```text
Cargo.toml
Cargo.lock
rust-toolchain.toml
rustfmt.toml
deny.toml
workspace-boundaries.toml
```

`workspace-boundaries.toml` is generated from the accepted FND-01 graph and must list every member, package name, category, exact allowed internal normal/dev/build edge, target role and release role.

`oteryn-architecture-check` consumes both the policy and:

```text
cargo metadata --locked --format-version 1
```

It fails on:

- missing/unregistered/duplicate workspace members;
- cycles including dev/build edges;
- forbidden package/feature/dependency names;
- external path/Git/unknown registry dependencies;
- source-only Canary/protocol/transport code copied into another package;
- production dependency on client-domain, client-simulation, synthetic-assets, test-support, tests or tools;
- provisional identifier names that violate FND-01 safeguards;
- root metadata/toolchain/lockfile drift;
- production release closure mismatch.

## 13. Validation matrix for the atomic PR

All commands run with the pinned toolchain and `--locked` where Cargo supports it.

### 13.1 Source and provenance gate

- source API confirms `main == c923ad8a1dff17b4933a6110931b0823cec2c590`;
- source subtree inventory has no unclassified member/path;
- finalized JSON manifests parse and satisfy repository schema validation;
- every migrated source path/blob exists at the cutover commit;
- every destination Rust/config/fixture file appears in provenance or is destination-authored;
- excluded paths/assets/binaries are absent.

### 13.2 Workspace policy / Ubuntu

```text
cargo metadata --locked --format-version 1
cargo fmt --all --check
cargo run --locked -p oteryn-architecture-check -- workspace .
```

Plus governance, JSON schema, provenance completeness, source restriction, cycle and lockfile-delta validation.

### 13.3 Shared Linux

Target:

```text
x86_64-unknown-linux-gnu
```

Compile, Clippy and test the exact portable shared/test/tool package selection. Do not build the Windows desktop application and do not claim Linux desktop-client support.

### 13.4 Windows pre-native client

Target:

```text
x86_64-pc-windows-msvc
```

Required:

- build default production client graph;
- strict Clippy and focused unit/integration tests;
- deterministic launch, visible pre-native state and shutdown scenario;
- PKCE/callback/account-directory negative tests;
- no credential request/consumption or gameplay endpoint connection;
- renderer surface and device-loss lifecycle evidence;
- production dependency closure audit.

### 13.5 Windows synthetic harness

Build and run the separate harness with deterministic domain/simulation/input/renderer/synthetic-asset scenarios. Network calls are disabled by dependency closure and test configuration.

### 13.6 Security and supply chain

- cargo-deny on Windows-default and Linux-shared graphs;
- supplemental all-features review only;
- Dependency Review;
- CodeQL;
- secret/redaction/oversize/truncation/path-traversal negative tests;
- reqwest feature and client-builder policy tests;
- license and source provenance review.

### 13.7 Production closure negatives

For `oteryn-client`, inspect normal and build dependencies for the Windows production target. The closure must not contain destination packages or aliases corresponding to:

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
any test package
any tool package
```

The check also searches package names, features, source paths, compiled artifact names and release manifests for Canary/native placeholder leakage.

## 14. Implementation PR review and merge gate

The destination implementation PR is ready only when:

- source SHA still matches the contract;
- all 19 members and no others exist;
- every mapping/provenance/dependency record is final;
- full changed-file list is within declared migration scope;
- no proprietary asset, binary, secret or generated output is present;
- focused, Linux, Windows client, synthetic harness, security and supply-chain gates pass on the exact unchanged head;
- independent migration audit has zero material findings;
- no review thread/requested change remains;
- destination branch is current with `main`;
- rollback remains executable and no later-gate contract is captured;
- squash merge is used.

The implementation merge commit becomes the canonical Rust-workspace commit recorded in the later source-marker PR.

## 15. Source development freeze

The source freeze defined in `VSL-02_SOURCE_RECONCILIATION.md` becomes active when this contract merges.

It is an administrative migration hold, not a deletion or runtime change. The implementation task rechecks the source SHA immediately before import and immediately before destination merge. Any unexpected source-subtree change stops the cutover.

Legacy C++/Lua PRs and tasks outside `oteryn-client/**` remain independent and are not transferred into Oteryn-v2.

## 16. Forward rollout order

The exact rollout is:

1. merge this VSL-02 contract in `blakinio/Oteryn-v2`;
2. verify source SHA and destination base again;
3. create the atomic destination migration task/branch/PR;
4. complete all import, rewrite, workspace, CI, provenance and validation work in that PR;
5. squash-merge the destination PR;
6. verify destination `main`, canonical workspace and provenance at the merge commit;
7. create a separate owner-authorized source-marker task/branch/PR in `blakinio/otclient`;
8. update source README/AGENTS, add moved record and archive the stale Rust/Canary task;
9. validate and squash-merge the source marker;
10. release coordination ownership and proceed to `FND-ID-01`.

The source marker cannot merge before step 5. FND-ID-01 cannot freeze identifiers against an unmerged destination workspace.

## 17. Rollback

### Before destination merge

Close the destination PR. No source file or canonical ownership state changed.

### After destination merge, before source marker

The source remains intact and explicitly unmarked. The destination merge may be reverted only when no dependent destination change has merged. Re-run destination governance after revert and preserve the failed migration PR/provenance as evidence.

### After source marker

Rollback is coordinated and uses two PRs:

1. revert the source marker first, restoring explicit source canonical status;
2. then revert the destination migration before any dependent destination contract/code remains;
3. update coordination records and reopen migration analysis.

Never revert the destination first while leaving the source explicitly non-canonical. Never enable normal development in both repositories as a rollback shortcut.

## 18. Later source-marker contract

The marker PR changes ownership/documentation only. Exact required paths are listed in `VSL-02_SOURCE_RECONCILIATION.md`.

It must record:

- selected source SHA;
- destination implementation PR and merge commit;
- finalized path/provenance/dependency manifests;
- date canonical ownership changed;
- no Canary migration claim;
- rollback order;
- destination repository path and governance.

It must preserve the source subtree and Git history as historical evidence.

## 19. Completion and next gate

VSL-02 is complete when this contract and machine plans are audited, exact-head validated, squash-merged and archived.

Its merge authorizes creation of the atomic destination migration task. It does not itself authorize partial workspace bootstrap or source-repository writes.

After the destination migration and source marker are terminal, the ordered next architecture gate is:

```text
FND-ID-01 — Foundation Identifier Vocabulary
```

## 20. Rejected alternatives

- **Use latest source at implementation time:** destroys exact inventory/provenance reproducibility.
- **Copy 26 crates unchanged:** imports Canary, fragmented session ownership and source-shaped protocol limits.
- **Preserve history with a misleading squash/subtree claim:** cross-repository ancestry would be false.
- **Import first, clean later:** creates a canonical invalid intermediate workspace.
- **Keep `protocol-canary` temporarily:** contradicts ADR-0008 and risks permanent fallback coupling.
- **Create empty `protocol-oteryn`:** creates a false compatibility surface before FND-02.
- **Keep blocking `ureq`:** violates accepted async/cancellation ownership.
- **Upgrade all dependencies during migration:** obscures equivalence and increases rollback risk.
- **Move/delete the source subtree immediately:** removes evidence and makes rollback unsafe.
- **Mark source moved before destination merge:** can leave no canonical Rust implementation.
- **Develop in both repositories after cutover:** creates divergent authority and duplicate work.

## 21. Acceptance checklist

- [x] Exact source SHA is pinned and equals current source `main`.
- [x] Source drift, open PRs and active tasks are reconciled.
- [x] All 26 source members have exact machine path dispositions.
- [x] Non-member roots/configs/fixtures/exclusions are mapped.
- [x] Provenance/history truthfulness policy is fixed.
- [x] The 19-member atomic destination PR scope is complete.
- [x] Tokio retention and reqwest/rustls replacement are exact.
- [x] Production and synthetic release closures are separated.
- [x] Equivalence evidence is disposition-specific.
- [x] Windows/Linux/security/source/provenance validation matrices are fixed.
- [x] Source freeze and exact marker scope/order are fixed.
- [x] Forward rollout and rollback prevent zero/dual canonical ownership.
- [ ] Independent exact-diff audit reports zero material findings.
- [ ] Required exact-head GitHub checks pass.
- [ ] Contract is squash-merged and task archived.
