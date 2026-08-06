# VSL-02: Exact Rust Client Migration and Cutover Contract

- Status: implementation-ready candidate
- Date: 2026-08-06
- Coordination ID: `OTV2-RUST-CLIENT-CUTOVER-20260806`
- Destination repository: `blakinio/Oteryn-v2`
- Destination contract base: `9034bd4bfa491eac6a898b29bc8151c94a4c2b89`
- Source repository: `blakinio/otclient`
- Source subtree: `oteryn-client/`
- Selected source commit: `c923ad8a1dff17b4933a6110931b0823cec2c590`
- Selected subtree tree: `c0928dafca6df19ff11d7901e503ed85a5199439`
- Governing workspace contract: `docs/architecture/FND-01_WORKSPACE_AND_RUST_MIGRATION_CONTRACT.md`
- Source reconciliation: `docs/migration/VSL-02_SOURCE_RECONCILIATION.md`
- Machine path map: `docs/migration/rust-client-path-map.json`
- Machine provenance/rollout plan: `docs/migration/rust-client-provenance-plan.json`

## 1. Purpose and authority

This contract defines the only permitted migration of the Rust client from `blakinio/otclient/oteryn-client` into the canonical `blakinio/Oteryn-v2` Rust workspace.

It converts FND-01 into an executable cutover package:

- one immutable source commit and subtree tree;
- one exact source-to-destination path map;
- one atomic destination implementation PR;
- one root Cargo workspace and lockfile;
- truthful provenance without false cross-repository ancestry;
- product-realistic validation and disposition-specific equivalence evidence;
- no Canary, gameplay transport, Game Session or speculative native protocol;
- destination-first canonical ownership and a later source-only moved marker;
- rollback that never leaves zero or two writable canonical Rust clients.

This contract does not move code. Its merge authorizes creation of the atomic destination migration task in `blakinio/Oteryn-v2`. A later separately authorized task is required for the source-marker PR in `blakinio/otclient`.

## 2. Binding decisions

The following remain binding:

- ADR-0002: Oteryn-v2 becomes the canonical Rust client/server/shared workspace through destination-first migration.
- ADR-0008: `protocol-canary` is `REFERENCE_ONLY` and cannot enter destination Cargo membership, product binaries, fallback, negotiation, translation or packaging.
- ADR-0011: the migrated client launches in explicit `pre-native-protocol`; gameplay entry fails before gameplay credential consumption, Game Session binding or gameplay endpoint connection.
- FND-01: the initial destination workspace has exactly 19 named members and the accepted per-source dispositions.
- FND-ID-01: public identifier meanings and representations remain deferred.
- FND-02: native protocol, framing and gameplay transport remain deferred.
- FND-04: Game Session credential, routing, admission and character lease behavior remain deferred.

The old nested source task that proposed automatic dual-protocol selection, `protocol-oteryn` implementation and source transport reuse is superseded for the destination. It is historical evidence only and must be archived as such in the later source-marker PR.

## 3. Exact cutover source

The selected source is immutable:

```text
repository: blakinio/otclient
commit: c923ad8a1dff17b4933a6110931b0823cec2c590
subtree: oteryn-client/
subtree tree: c0928dafca6df19ff11d7901e503ed85a5199439
root manifest blob: 037013e8e4a762a65f0f2a30f7761ee14725a3fc
root lockfile blob: 2143408c12c50132883890f0821278320a331fde
```

The implementation imports only from this commit. It never imports from a mutable later `main`.

The source default branch may advance outside `oteryn-client/**` without blocking cutover. Before opening the atomic migration PR and again before merging it, the current source default branch must resolve `oteryn-client/` to tree `c0928daf...`.

A changed subtree, new Rust-subtree PR or new active ownership claim stops the migration. Selecting a newer source requires an owner-approved VSL-02 amendment, a new commit/tree, regenerated manifests and a fresh audit.

## 4. Source freeze and conflict closure

The administrative freeze starts when this contract merges:

```text
blakinio/otclient/oteryn-client/**
```

It forbids new Rust-subtree feature, refactor, dependency, protocol, formatting and documentation changes. Legacy C++/Lua work outside the subtree is unaffected.

Two source Rust programmes are explicitly closed as destination authority:

1. `OTC2-20260803-playability-p2-canary-world-protocol`
   - `protocol-canary` remains source-only reference evidence;
   - no Canary crate, fixture or compatibility path is migrated.
2. `oteryn-client/docs/agents/tasks/active/OTC2-20260805-native-protocol-single-version-completion.md`
   - its dual-protocol/native-runtime plan is superseded by ADR-0008, ADR-0011 and FND-01;
   - it cannot be resumed against the destination;
   - it is archived as `SUPERSEDED_REFERENCE_ONLY` by the source-marker PR.

## 5. Atomic destination implementation package

The implementation uses one branch:

```text
migrate/rust-client-cutover-c923ad8
```

and one PR targeting `blakinio/Oteryn-v2:main`.

That single PR must contain:

1. the canonical root Cargo workspace with exactly the 19 accepted members;
2. all FND-01 migrations, merges, splits, renames and rewrites;
3. explicit omission of every reference-only source path;
4. a launchable Windows `pre-native-protocol` client;
5. a separate non-release synthetic client harness;
6. root `Cargo.lock`, toolchain, rustfmt, cargo-deny and `workspace-boundaries.toml`;
7. executable architecture/dependency/release-role enforcement;
8. destination Rust workflows and Windows/Linux product matrices;
9. finalized provenance, path-map and dependency-delta files;
10. disposition-specific transformation/equivalence evidence;
11. production closure negatives proving no Canary, protocol, transport, Game Session, synthetic or test leakage;
12. migration, source-marker and rollback handoff documentation.

The following delivery is forbidden:

```text
PR A: copy source
PR B: remove Canary
PR C: create workspace and CI
PR D: repair boundaries
```

No merged intermediate destination may be canonical while violating FND-01 or ADR-0011.

## 6. Initial destination workspace

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

It must not create, alias or hide:

```text
protocol-canary
protocol-core
protocol-oteryn
transport
game-session
game-server
session-lease
persistence
production world/content/scripting crates
```

No placeholder or feature flag may recreate a forbidden member under another name.

## 7. Source-to-destination mapping

`rust-client-path-map.json` is normative. It covers all 26 source workspace members, non-member configs, fixtures, source governance and exclusions.

Implementation rules:

- every source member has exactly one disposition;
- every migrated or transformed source file receives source blob and destination path provenance;
- every destination Rust/config/fixture file is classified as source-derived or destination-authored;
- rewritten files are never called byte-identical;
- merged/split crates land directly in their final destination modules;
- no committed `legacy/`, `old/`, `_tmp`, `imported/` or duplicate staging tree;
- no source governance, source workspace manifest, source lockfile or source workflow is copied as destination authority.

The source technical-login tests are `REFERENCE_ONLY`: they have no destination path. `tests/pre-native-client/**` is independently destination-authored from accepted negative scenarios and cannot be described as a copied test suite.

## 8. Permanent reference-only exclusions

These remain accessible only through source links and immutable SHAs:

```text
oteryn-client/crates/protocol-canary/**
oteryn-client/crates/protocol-core/**
oteryn-client/crates/transport/**
oteryn-client/contracts/canary/**
oteryn-client/docs/architecture/**
oteryn-client/docs/agents/**
oteryn-client/AGENTS.md
```

Useful protocol/transport patterns may be reconsidered only by FND-02. The migration PR cannot copy them into another utility module to bypass their disposition.

No generated build output, binary, debug symbol, cache, secret, environment file or proprietary Tibia/CipSoft asset may enter the destination.

## 9. Provenance and history truthfulness

Cross-repository Git ancestry is not preserved by a squash-merged content migration. The project uses immutable machine-readable provenance instead of a false history claim.

The atomic PR finalizes:

```text
docs/migration/rust-client-provenance.json
docs/migration/rust-client-path-map.json
docs/migration/rust-dependency-delta.json
```

Every source-derived file records:

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

- source repository, selected commit and subtree remain permanent evidence;
- no fabricated co-author or copied author list;
- source copyright/license notices are preserved where applicable;
- destination-authored glue and rewrites are attributed to the destination PR;
- no proprietary asset is imported because a source file referenced it;
- final squash message records the coordination ID, selected source commit and subtree tree.

The source subtree remains present after migration for legal, design and blame evidence.

## 10. Dependency policy

### 10.1 Toolchain and runtime

Retain during cutover:

```text
Rust 1.94.0
edition 2024
resolver 3
Tokio =1.51.4
```

Tokio normal features are package-scoped:

```text
io-util, net, rt-multi-thread, sync, time
```

`macros` and `test-util` are test-only where required. Test features may not enlarge the production client closure.

### 10.2 Async Platform and Identity HTTP

Replace source blocking `ureq` with:

```toml
reqwest = {
  version = "=0.13.4",
  default-features = false,
  features = ["form", "json", "rustls", "stream"]
}
```

Forbidden initial capabilities:

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

Required client policy:

- explicit rustls backend;
- automatic redirects disabled;
- automatic proxy discovery disabled;
- cookie storage and transparent decompression disabled;
- certificate and hostname validation cannot be disabled;
- no production custom CA or pin introduced during migration;
- bounded request body, response headers, chunks and total body;
- explicit connect, request and total-operation deadlines;
- cancellation and shutdown owned by the application Tokio runtime;
- no leaked tasks, workers or secrets;
- redacted diagnostics and errors.

Source direct `ureq` and direct native-tls Platform usage are removed. Every remaining transitive native-tls occurrence must be explained by the lockfile delta and may not enable a forbidden production capability.

### 10.3 Upgrade restraint

All other retained direct dependencies stay exact-pinned unless a target split or accepted merge removes them. No opportunistic broad upgrade is allowed in the migration PR.

Every added, removed, version-changed or feature-changed dependency appears in `rust-dependency-delta.json` with affected packages, reason, license and security review.

## 11. Pre-native product behavior

The production `oteryn-client` must:

- build for `x86_64-pc-windows-msvc`;
- launch a real application window/shell;
- initialize only permitted Identity and account/directory boundaries;
- clearly show native gameplay unavailable in this build;
- never advertise Canary or protocol selection;
- fail before gameplay credential request or consumption;
- fail before Game Session binding;
- fail before gameplay endpoint DNS resolution or connection;
- never present synthetic harness success as live gameplay;
- shut down deterministically with no task/worker leak.

Directory metadata must contain no gameplay host, port, endpoint, protocol selector, admission token or Game Session credential.

## 12. Synthetic harness behavior

`oteryn-synthetic-client-harness` is a separate non-release executable and the named consumer for client domain, simulation, input, renderer, synthetic assets and test support.

It must:

- use only project-owned deterministic fixtures;
- have no Identity, Platform or gameplay network capability;
- run bounded deterministic scenarios and expected snapshots;
- never enter production installer/package manifests;
- never be enabled as a production-client feature;
- never claim protocol, server or shared three-tier E2E compatibility.

The production app cannot normally or at build time depend on the harness, client simulation, synthetic assets or test support.

## 13. Disposition-specific equivalence evidence

### `MIGRATE_AS_IS`

- source/destination public-item inventory;
- retained focused tests;
- semantic diff limited to repository/package/path metadata and accepted propagated renames;
- source and destination blob references.

### `MIGRATE_AND_RENAME`

- package/API/symbol rename map;
- same behavioral tests or explicitly stronger replacements;
- proof ownership terminology changed without unsupported behavior change.

### `MERGE`

- source modules mapped to final destination modules;
- duplicate type/error/limit reconciliation;
- tests retained at the new owner;
- no reverse dependency or cycle.

### `SPLIT`

- every source public item classified retained, rewritten, deferred or dropped;
- each retained item has one destination owner;
- deferred gameplay credential/route/protocol semantics absent from symbols and closures;
- no hidden compatibility shim recreates the source crate.

### `REWRITE`

- preserved security/behavior scenarios named;
- discarded assumptions named;
- destination tests prove the new boundary;
- no compatibility claim based only on source tests.

### `REFERENCE_ONLY`

- exact source path/SHA remains in evidence;
- zero destination source copy/member;
- zero release artifact inclusion.

## 14. Root workspace and enforcement

The atomic PR creates one root:

```text
Cargo.toml
Cargo.lock
rust-toolchain.toml
rustfmt.toml
deny.toml
workspace-boundaries.toml
```

`workspace-boundaries.toml` lists every member, package, category, allowed normal/dev/build edge, target role and release role.

`oteryn-architecture-check` consumes that policy and `cargo metadata --locked`. It fails on:

- missing, duplicate or unregistered members;
- cycles including dev/build edges;
- forbidden names, features or dependencies;
- external path, Git or unknown registry dependencies;
- source-only Canary/protocol/transport code hidden in another package;
- production dependency on client domain/simulation, synthetic assets, test support, tests or tools;
- provisional identifier violations;
- root metadata, toolchain or lockfile drift;
- production closure mismatch.

## 15. Validation matrix for the atomic PR

### 15.1 Source and provenance

- selected commit remains reachable;
- selected subtree tree equals `c0928daf...`;
- current source default branch has the same subtree tree;
- no unclassified member/path or new Rust ownership claim;
- all finalized JSON manifests parse and pass schema checks;
- every source-derived path/blob exists at the selected commit;
- every destination file is provenance-classified;
- exclusions, binaries, secrets and proprietary assets are absent.

### 15.2 Workspace policy on Ubuntu

```text
cargo metadata --locked --format-version 1
cargo fmt --all --check
cargo run --locked -p oteryn-architecture-check -- workspace .
```

Also run governance, source restriction, cycle, root-lock and dependency-delta validators.

### 15.3 Shared Linux

For `x86_64-unknown-linux-gnu`, compile, Clippy and test the named portable shared/test/tool selection. Do not build or claim a Linux desktop client.

### 15.4 Windows pre-native client

For `x86_64-pc-windows-msvc`:

- default production build and strict Clippy;
- deterministic launch, visible pre-native state and shutdown;
- PKCE/callback/account-directory negative tests;
- proof of no gameplay credential or endpoint operation;
- renderer surface/device-loss lifecycle evidence;
- production dependency closure audit.

### 15.5 Windows synthetic harness

Build/run deterministic domain, simulation, input, renderer and synthetic-asset scenarios. Network capability is absent by dependency closure.

### 15.6 Security and supply chain

- cargo-deny for Windows-default and Linux-shared graphs;
- supplemental all-features review only;
- Dependency Review and CodeQL;
- secret/redaction/oversize/truncation/path-traversal tests;
- reqwest feature/client-builder policy checks;
- license and provenance review.

### 15.7 Production closure negatives

The Windows production normal/build closure must not contain packages, aliases, features, paths, artifacts or release entries corresponding to:

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

## 16. Implementation PR merge gate

Merge only when:

- selected commit/tree and current source subtree are reverified;
- exactly 19 workspace members exist;
- mapping, provenance and dependency records are final;
- full diff is within declared migration scope;
- no prohibited asset, binary, secret or generated output exists;
- all focused, Linux, Windows client, harness, security and supply-chain gates pass on the exact unchanged head;
- independent migration audit has zero material findings;
- no unresolved review/requested change or ownership conflict remains;
- destination branch is current with `main`;
- rollback remains executable and no later-gate contract is captured;
- squash merge is used.

The destination merge commit becomes the canonical Rust workspace commit used by the later source marker.

## 17. Forward rollout

1. merge and archive this VSL-02 contract;
2. verify selected source commit/tree and current source subtree again;
3. create the atomic destination migration task/branch/PR;
4. complete all migration, rewrite, workspace, CI, provenance and validation work in that PR;
5. squash-merge destination implementation;
6. verify destination `main` and immutable provenance;
7. create a separately authorized source-marker task/branch/PR in `blakinio/otclient`;
8. mark the Rust subtree moved/non-canonical and archive both conflicting Rust active tasks;
9. validate and squash-merge source marker;
10. release coordination ownership and proceed to FND-ID-01.

The source marker cannot merge before the destination implementation. FND-ID-01 cannot freeze identifiers against an unmerged destination workspace.

## 18. Rollback

### Before destination merge

Close the destination PR. Source remains canonical and unchanged.

### After destination merge, before source marker

Source remains intact. Revert the destination merge only when no dependent destination change has merged. Preserve failed migration/provenance evidence.

### After source marker

1. revert source marker first, restoring explicit source canonical status;
2. then revert destination migration before dependent destination work remains;
3. update coordination records and reopen migration analysis.

Never revert destination first while source remains explicitly non-canonical. Never enable normal Rust development in both repositories as a rollback shortcut.

## 19. Source-marker requirements

The separate marker PR changes ownership documentation and task lifecycle only. Exact paths are in `VSL-02_SOURCE_RECONCILIATION.md`.

It records:

- selected source commit and subtree tree;
- destination implementation PR and merge commit;
- finalized path/provenance/dependency manifests;
- date canonical ownership changed;
- no Canary migration claim;
- both archived source Rust tasks and their reference/superseded status;
- rollback order and destination governance.

It preserves the source subtree and Git history as historical evidence.

## 20. Completion and next gate

VSL-02 is complete when this contract, reconciliation and machine plans are independently audited, exact-head validated, squash-merged and archived.

Its merge authorizes the atomic destination migration task. It does not authorize source writes, partial workspace bootstrap or native protocol implementation.

After the destination migration and source marker are terminal, the next architecture gate is:

```text
FND-ID-01 — Foundation Identifier Vocabulary
```

## 21. Rejected alternatives

- use mutable latest source at implementation time;
- copy all 26 crates unchanged;
- claim preserved cross-repository ancestry;
- import first and clean later;
- retain Canary temporarily;
- create empty `protocol-oteryn`;
- keep blocking `ureq`;
- upgrade broadly during migration;
- delete/move source before destination merge;
- require whole source `main` to remain unchanged despite unrelated legacy work;
- leave the nested dual-protocol task resumable;
- develop in both repositories after cutover.

## 22. Acceptance checklist

- [x] Exact source commit and subtree tree are pinned.
- [x] Source drift, open PRs, root tasks and nested Rust task are reconciled.
- [x] All 26 source members and relevant non-members have machine dispositions.
- [x] Technical-login reference-only semantics do not imply a copied destination path.
- [x] Provenance/history truthfulness policy is fixed.
- [x] Atomic 19-member destination PR scope is complete.
- [x] Tokio retention and reqwest/rustls replacement are exact.
- [x] Production and synthetic closures are separate.
- [x] Equivalence evidence is disposition-specific.
- [x] Windows/Linux/security/source/provenance validation matrices are fixed.
- [x] Subtree freeze and source-marker scope/order are fixed.
- [x] Rollout and rollback prevent zero/dual canonical ownership.
- [ ] Independent exact-diff audit reports zero material findings.
- [ ] Required exact-head GitHub checks pass.
- [ ] Contract is squash-merged and task archived.
