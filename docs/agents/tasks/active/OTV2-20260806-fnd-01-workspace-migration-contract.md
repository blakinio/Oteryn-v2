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
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-06T08:13:00+02:00
updated_at: 2026-08-06T08:13:00+02:00
execution_budget_minutes: 120
large_budget_reason: FND-01 requires an exact source-SHA inventory, per-member migration dispositions, target workspace membership, dependency policy, toolchain/CI policy and reconciliation of protocol-free migration constraints.
owned_paths:
  - docs/architecture/FND-01_WORKSPACE_AND_RUST_MIGRATION_CONTRACT.md
  - docs/agents/tasks/active/OTV2-20260806-fnd-01-workspace-migration-contract.md
public_contracts:
  - docs/architecture/FND-01_WORKSPACE_AND_RUST_MIGRATION_CONTRACT.md
depends_on:
  - ADR-0001
  - ADR-0002
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

Produce the owner-reviewable `FND-01` contract for the exact current Rust-client workspace. The contract must classify every current workspace member and relevant non-member subsystem, define the minimal consumer-backed destination graph and establish toolchain, dependency, feature, CI and machine-enforcement policy without implementing or moving code.

## Architecture and source of truth

### PROVEN

- `blakinio/Oteryn-v2@cbc2150024d98bbdbfa9b1c17bc9b9df16bcd9f2` is the destination architecture baseline.
- `blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590` is the exact source revision being inventoried.
- The source Rust workspace has 26 members and uses Rust `1.94.0`, edition 2024, resolver 3 and one lockfile.
- The source binary and technical-login integration tests depend on `protocol-canary`.
- ADR-0008 prohibits Canary from the destination production workspace, dependency graph, binaries, negotiation, fallback and translation paths.
- ADR-0011 permits a launchable `pre-native-protocol` client but forbids a speculative `protocol-oteryn` implementation and requires gameplay entry to fail closed before credential consumption or gameplay endpoint connection.
- The source `protocol-core` and `transport` impose `u16::MAX`-sized protocol/frame ceilings, while later native protocol limits remain owned by `FND-02`; these source limits cannot silently become the native contract.
- Open source PRs #23, #48 and #97 do not modify `oteryn-client` Rust workspace members, but VSL-02 must still reconcile their terminal cutover disposition.

### DERIVED

- The current account/directory/game-entry boundary is over-fragmented across `account-session`, `world-directory`, `game-session`, `platform`, `identity` and `app-runtime` and contains Canary-specific entry policy.
- Current `game-domain` and `simulation-core` are client projection/simulation contracts, not sufficient evidence for an authoritative server domain/runtime.
- Current asset crates implement synthetic test-fixture formats, not the future production Oteryn asset/content contract.
- The initial destination graph should preserve tested client foundations while making client-only, synthetic and provisional semantics explicit.

### UNKNOWN

- Final public identifier representations remain owned by `FND-ID-01`.
- Native protocol framing, limits and transport composition remain owned by `FND-02`.
- Exact Platform Game Session/admission contract remains owned by `FND-04`.
- VSL-02 will pin the cutover revision and reconcile changes after this inventory.

## Acceptance criteria

- [ ] Every source workspace member has exactly one migration disposition.
- [ ] Relevant non-member assets, Canary contracts, docs and root workspace policy files are classified.
- [ ] The exact minimal destination workspace and package names are defined.
- [ ] Every initial member has a named product, tool or test consumer and observable acceptance.
- [ ] `protocol-canary`, current Canary-shaped protocol helpers and unsupported gameplay transport are absent from the initial production graph.
- [ ] The `pre-native-protocol` application state is preserved without empty native-protocol crates.
- [ ] Client projection/simulation types are not misrepresented as authoritative server domain/runtime.
- [ ] Synthetic asset code and fixtures are visibly test/development-only and excluded from release artifacts.
- [ ] Legal and forbidden dependency directions are defined for machine enforcement.
- [ ] Toolchain, lockfile, feature, target and CI matrices are fixed.
- [ ] Canonical contract/registry locations and crate-evolution criteria are fixed.
- [ ] No source or destination runtime code is changed.
- [ ] Independent architecture audit reports zero open material findings before owner acceptance.

## Excluded scope

- No physical client migration or root Cargo workspace creation.
- No source-repository write, freeze or moved marker.
- No `protocol-oteryn` schema, codec or transport implementation.
- No server runtime, persistence, admission, content or Studio implementation.
- No final identifier representations.
- No merge of the contract as accepted architecture before the proposed dispositions and unresolved policy points are reviewed.

## Implementation / findings

- Exact source and destination revisions pinned for analysis.
- All 26 source member manifests inventoried.
- Canary and native-contract incompatibilities identified in the source protocol/transport layer.
- Candidate target graph and per-member dispositions are being audited.

## Validation

### Focused

- command/run: exact source manifest/API review and complete contract diff review
- result: in progress

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only contract
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial review against ADR-0001, ADR-0002, ADR-0007, ADR-0008, ADR-0011, the complete source workspace graph and later FND-ID-01/FND-02/FND-04 ownership boundaries
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #38 is unrelated lifecycle cleanup; source PRs #23, #48 and #97 remain VSL-02 reconciliation inputs
- merge commit/result: pending owner acceptance
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Created the bounded FND-01 architecture package after exact source and destination revision verification.
status: investigating
branch: docs/fnd-01-workspace-migration-contract
head_sha: null
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
next_action: Draft the complete source-member disposition matrix and minimal destination workspace, then perform an adversarial dependency and gate-ownership audit.
```
