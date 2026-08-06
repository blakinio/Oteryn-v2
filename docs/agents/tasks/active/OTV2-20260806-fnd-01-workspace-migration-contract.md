# OTV2-20260806-fnd-01-workspace-migration-contract

```yaml
task_id: OTV2-20260806-fnd-01-workspace-migration-contract
title: Define the canonical Rust workspace and existing-client migration dispositions
mode: CONTRACT
status: ready
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd-01-workspace-migration-contract
pr: 46
base_sha: cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-06T08:13:00+02:00
updated_at: 2026-08-06T08:47:00+02:00
execution_budget_minutes: 120
large_budget_reason: FND-01 requires an exact source-SHA inventory, per-member migration dispositions, target workspace membership, dependency policy, toolchain/CI policy and reconciliation of protocol-free migration constraints.
owned_paths:
  - docs/architecture/FND-01_WORKSPACE_AND_RUST_MIGRATION_CONTRACT.md
  - docs/architecture/FND-01_RUST_SOURCE_INVENTORY.md
  - docs/agents/tasks/active/OTV2-20260806-fnd-01-workspace-migration-contract.md
public_contracts:
  - docs/architecture/FND-01_WORKSPACE_AND_RUST_MIGRATION_CONTRACT.md
  - docs/architecture/FND-01_RUST_SOURCE_INVENTORY.md
depends_on:
  - ADR-0001
  - ADR-0002
  - ADR-0005
  - ADR-0007
  - ADR-0008
  - ADR-0011
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
blocks:
  - VSL-02 exact client migration and cutover contract
  - the atomic destination migration/workspace pull request
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/otclient (read-only source evidence)
```

## Outcome

Produce the owner-reviewable `FND-01` contract for the exact current Rust-client workspace. The package inventories every current member and relevant non-member subsystem, proposes a minimal consumer-backed destination graph and establishes toolchain, dependency, release-role, CI and machine-enforcement policy without implementing or moving code.

## Architecture and source of truth

### PROVEN

- Destination baseline: `blakinio/Oteryn-v2@cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2`.
- Source inventory revision: `blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590`.
- The exact source workspace has 26 members, Rust `1.94.0`, edition 2024, resolver 3 and one lockfile.
- Source application and technical-login tests depend on `protocol-canary`.
- Source `game-session` contains Canary-specific entry policy.
- Source account/directory/entry responsibilities are fragmented across tightly coupled crates.
- Source domain/simulation are client projection/snapshot contracts, not authoritative server runtime.
- Source asset/resource packages implement synthetic fixtures.
- Source protocol/transport limits cannot silently become the native contract.
- Open source PRs #23, #48 and #97 do not alter the inspected Rust workspace but remain `VSL-02` reconciliation inputs.

### DERIVED CANDIDATE

- Proposed destination has one production-shaped pre-native client and a separate non-release synthetic harness.
- `protocol-canary`, `protocol-core`, gameplay `transport` and `game-session` do not enter the initial workspace.
- Client domain/simulation and synthetic assets remain only because separate test/tool consumers prove immediate value.
- Platform values and I/O split into `platform-contracts` and `platform-client`.
- Gameplay host/port, credentials, routes and admission state are absent from pre-native client contracts.
- Platform/Identity I/O is asynchronous, cancellation-safe and owned by the application Tokio runtime.
- Provisional source identifiers are renamed so they cannot be confused with `FND-ID-01` identities.

### UNKNOWN / DEFERRED

- Owner acceptance of the proposed 19-member graph and per-member dispositions.
- Exact async HTTP/TLS crate/features remain a `VSL-02` dependency selection under the accepted boundary.
- Public identifiers remain `FND-ID-01`.
- Native protocol/transport remains `FND-02`.
- Game Session/admission remains `FND-04`.

## Acceptance criteria

- [x] Every source workspace member appears exactly once in the inventory.
- [x] Direct internal edges, direct consumers and direct third-party dependencies are recorded at the exact source SHA.
- [x] Relevant non-member assets, Canary contracts, docs and root policy files are inventoried.
- [x] Every source member has exactly one candidate migration disposition.
- [x] A minimal 19-member destination graph and package names are proposed.
- [x] Every proposed member has a named product, tool or test consumer.
- [x] Production client and synthetic harness have separate packages and release closures.
- [x] Canary, source protocol helpers, gameplay transport and Game Session code are absent from the initial workspace.
- [x] Client projection/simulation is not presented as authoritative server domain/runtime.
- [x] Synthetic asset code is explicitly non-release fixture infrastructure.
- [x] Gameplay host/port/routing cannot enter pre-native Platform contracts.
- [x] Platform/Identity I/O is asynchronous and cancellation-safe; source `ureq` is reference-only.
- [x] Category and package-specific dependency allowlists are complete and acyclic.
- [x] Toolchain, lockfile, target, release-role and CI matrices are defined.
- [x] Provisional identifier collision with `FND-ID-01` is prevented.
- [x] Independent architecture audit reports zero open material findings.
- [x] Governance, Dependency Review and CodeQL passed on exact candidate head before this status checkpoint.
- [ ] Owner accepts the proposed graph/dispositions.
- [ ] Final owner-accepted head is synchronized with `main`, revalidated and merged.

## Excluded scope

- No physical client migration or Cargo workspace creation.
- No source-repository write, freeze or moved marker.
- No `protocol-oteryn` schema, codec or transport implementation.
- No server runtime, persistence, admission, content or Studio implementation.
- No final identifier representations.
- No merge as accepted architecture before owner approval.

## Implementation / findings

Delivered candidate package:

- exact 26-member source manifest/dependency/consumer inventory;
- direct third-party and non-member source inventory;
- one candidate disposition per source member;
- proposed 19-member destination graph;
- separate production client and non-release synthetic harness;
- provisional identifier safeguards;
- async Platform/Identity boundary with no pre-native gameplay routes/credentials;
- closed category and package dependency policy;
- Windows/Linux/release-role CI matrix;
- root Cargo, lockfile, formatting, supply-chain and machine-policy contract.

Resolved audit findings:

- removed premature accepted wording;
- added exact source graph and dependency evidence;
- split `renderer-resource` so synthetic dependencies cannot leak into production renderer;
- changed `foundation` to `REWRITE` rather than a false multi-crate split;
- separated synthetic evidence from the production app binary;
- prevented provisional identifier-name collisions;
- removed gameplay routes from pre-native Platform values;
- rejected source blocking `ureq` as a production option;
- closed package-level test/tool edges;
- prevented the source synthetic-asset/compiler dev-cycle pattern: round-trip tests belong to the compiler or harness, never a reverse `synthetic-assets -> compiler` edge.

## Validation

### Focused

- command/run: exact source manifest/API review; 26-row inventory count; 26-row disposition count; 19-member consumer review; manual topological sort of category and package edges; complete three-file diff review
- result: `PASS`; no missing member, duplicate disposition, cycle, unowned member or later-gate contract capture found

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only contract
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: `NOT_APPLICABLE`

### Exact-head CI

- validated head: `dde84e0ccd85f7f2a7f18afd507cbebbf713504b`
- Agent governance: run `31078011483` — `PASS`
- Dependency review: run `31078011462` — `PASS`
- CodeQL: run `31078011574` — `PASS`
- result: `PASS`

## Independent audit

- exact architecture head: `fc2897a0d4bbde27d421bf03faf6738e1b313789`; task-only checkpoint head `dde84e0ccd85f7f2a7f18afd507cbebbf713504b` retained the same architecture files
- method/auditor: adversarial source-to-target review against ADR-0001, ADR-0002, ADR-0005, ADR-0007, ADR-0008, ADR-0011, the exact 26-member source graph and later `FND-ID-01`/`FND-02`/`FND-04` ownership; dependency graph manually topologically sorted; production and harness closures challenged separately
- resolved material findings:
  - candidate/accepted status ambiguity;
  - missing exact source dependencies/consumers;
  - synthetic renderer dependency leakage;
  - optional synthetic dependencies in the production app;
  - ambiguous client/server domain ownership;
  - canonical-looking provisional identifier names;
  - pre-native gameplay route exposure;
  - blocking Platform I/O alternative;
  - incomplete package-specific test/tool edges;
  - potential synthetic asset/compiler dev cycle.
- open material findings: none
- verdict: `PASS`

## PR and closeout

- changed-file review: three declared documentation/task files only
- unresolved review threads: 0
- related/superseded PRs: Oteryn-v2 PR #38 is unrelated lifecycle cleanup; source PRs #23, #48 and #97 remain `VSL-02` inputs
- merge commit/result: pending explicit owner acceptance
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Candidate FND-01 contract, exact source inventory, independent audit and exact-head CI are complete; draft PR #46 is ready for explicit owner acceptance.
status: ready
branch: docs/fnd-01-workspace-migration-contract
head_sha_before_checkpoint: dde84e0ccd85f7f2a7f18afd507cbebbf713504b
pr: 46
ci_check_generation: dde84e0ccd85f7f2a7f18afd507cbebbf713504b
ci_checks_for_current_head: 3
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 3
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: explicit owner acceptance required before marking PR ready or merging
next_action: Ask the owner to accept or reject the proposed 19-member graph and disposition policy; if accepted, synchronize with main, update canonical registers, revalidate and merge.
```
