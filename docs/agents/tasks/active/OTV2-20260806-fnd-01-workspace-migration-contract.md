# OTV2-20260806-fnd-01-workspace-migration-contract

```yaml
task_id: OTV2-20260806-fnd-01-workspace-migration-contract
title: Define the canonical Rust workspace and existing-client migration dispositions
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd-01-workspace-migration-contract
pr: null
base_sha: cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2
head_sha: 6ccb5c59261648d8055c479a5695ca346bb71bf3
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-06T08:13:00+02:00
updated_at: 2026-08-06T08:32:00+02:00
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

Produce the owner-reviewable `FND-01` contract for the exact current Rust-client workspace. The contract classifies every current workspace member and relevant non-member subsystem, proposes the minimal consumer-backed destination graph and establishes toolchain, dependency, feature, release-role, CI and machine-enforcement policy without implementing or moving code.

## Architecture and source of truth

### PROVEN

- Destination baseline: `blakinio/Oteryn-v2@cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2`.
- Source inventory revision: `blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590`.
- The exact source workspace has 26 members, Rust `1.94.0`, edition 2024, resolver 3 and one lockfile.
- Source application and technical-login integration tests depend on `protocol-canary`.
- Source `game-session` contains Canary-specific entry policy.
- Source account/directory/entry responsibilities are fragmented across five tightly coupled crates plus application orchestration.
- Source domain/simulation are explicitly client projection/snapshot contracts, not authoritative server runtime.
- Source asset/resource packages implement synthetic fixture formats.
- Source protocol/transport limits cannot silently become the native protocol contract.
- Open source PRs #23, #48 and #97 do not alter the inspected Rust workspace, but remain `VSL-02` reconciliation inputs.

### DERIVED CANDIDATE

- Proposed destination has one production-shaped pre-native client and a separate non-release synthetic harness.
- `protocol-canary`, `protocol-core`, gameplay `transport` and `game-session` do not enter the initial workspace.
- Client domain/simulation and synthetic assets remain only because separate test/tool consumers prove immediate value.
- Platform values and Platform I/O split into `platform-contracts` and `platform-client`.
- Provisional source identifiers must be renamed so they cannot be confused with future `FND-ID-01` identifiers.
- Source blocking Platform HTTP is not an accepted production implementation.

### UNKNOWN / OPEN AUDIT POINTS

- Final owner acceptance of the proposed 19-member graph and per-member dispositions.
- Exact async Platform HTTP/TLS crate and feature selection remains a `VSL-02` dependency decision after the FND-01 boundary is accepted.
- Final public identifier representations remain `FND-ID-01`.
- Native protocol/transport implementation remains `FND-02`.
- Game Session/admission remains `FND-04`.

## Acceptance criteria

- [x] Every source workspace member appears exactly once in the source inventory.
- [x] Direct internal edges, direct consumers and direct third-party dependencies are recorded at the exact source SHA.
- [x] Relevant non-member assets, Canary contracts, docs and root policy files are inventoried.
- [x] Every source member has exactly one candidate migration disposition.
- [x] A minimal 19-member destination graph and package names are proposed.
- [x] Every proposed member has a named product, tool or test consumer.
- [x] Production client and synthetic harness use separate packages and release closures.
- [x] Canary, current protocol helpers, gameplay transport and Game Session code are absent from the initial production/workspace graph.
- [x] Client projection/simulation types are not presented as authoritative server domain/runtime.
- [x] Synthetic asset code is explicitly non-release fixture infrastructure.
- [x] Legal and forbidden dependency directions are expressed as a closed machine-enforceable policy.
- [x] Toolchain, lockfile, target, release-role and CI matrices are proposed.
- [x] Provisional identifier collision with `FND-ID-01` is prevented by required renaming.
- [ ] Platform directory contracts explicitly omit gameplay host/port routing before `FND-04`.
- [ ] Platform/Identity I/O is fixed to an asynchronous cancellation-safe boundary; source `ureq` is reference-only.
- [ ] Package-specific test/tool dependency allowlists are complete and non-circular.
- [ ] Independent architecture audit reports zero open material findings.
- [ ] Owner accepts the proposed graph/dispositions.
- [ ] Exact-head documentation/governance validation passes after owner acceptance edits.

## Excluded scope

- No physical client migration or Cargo workspace creation.
- No source-repository write, freeze or moved marker.
- No `protocol-oteryn` schema, codec or transport implementation.
- No server runtime, persistence, admission, content or Studio implementation.
- No final identifier representations.
- No merge as accepted architecture before owner approval.

## Implementation / findings

Completed:

- exact source and destination revision verification;
- complete 26-member manifest/dependency/consumer inventory;
- direct third-party dependency treatment;
- non-member source inventory;
- candidate dispositions for all 26 source members;
- proposed 19-member destination graph;
- separation of the production client from a synthetic harness executable;
- provisional identifier safeguards;
- closed category-edge and release-closure policy;
- Windows/Linux/product-role CI proposal;
- root Cargo, lockfile, formatting, supply-chain and machine-policy proposal.

Resolved audit findings:

- candidate wording no longer labels the graph as accepted before owner approval;
- `renderer-resource` is split so synthetic dependencies cannot leak into production renderer;
- `foundation` is rewritten rather than incorrectly classified as a multi-crate split;
- exact source edges/consumers/dependencies moved into a dedicated evidence inventory;
- synthetic domain/simulation evidence moved to a separate executable rather than optional dependencies of the production app.

Open material audit findings are limited to the Platform routing/I/O clarifications and exact package-specific test/tool allowlists listed above.

## Validation

### Focused

- command/run: exact source manifest/API review; member-count and disposition-count review; candidate dependency/release-role audit
- result: `PASS` for source inventory and coverage; contract audit still in progress for listed open points

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only contract
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending final candidate head
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending final candidate head
- method/auditor: adversarial review against ADR-0001, ADR-0002, ADR-0005, ADR-0007, ADR-0008, ADR-0011, the exact source inventory and later `FND-ID-01`/`FND-02`/`FND-04` ownership
- resolved material findings: premature accepted wording; missing exact source graph; renderer synthetic dependency leakage; production-app synthetic optional dependencies; ambiguous client/server domain ownership
- open material findings: Platform routing exposure, async I/O requirement and package-specific allowlists
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: Oteryn-v2 PR #38 is unrelated lifecycle cleanup; source PRs #23, #48 and #97 remain `VSL-02` inputs
- merge commit/result: pending owner acceptance
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Exact source inventory and hardened candidate FND-01 contract drafted; adversarial audit reduced open findings to Platform routing/I/O and package-specific dependency allowlists.
status: investigating
branch: docs/fnd-01-workspace-migration-contract
head_sha: 6ccb5c59261648d8055c479a5695ca346bb71bf3
pr: null
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: none
next_action: Close the Platform routing/I/O and package-specific edge findings, then open a draft PR for owner review without merging.
```
