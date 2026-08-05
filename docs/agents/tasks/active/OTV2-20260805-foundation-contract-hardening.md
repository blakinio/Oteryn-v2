# OTV2-20260805-foundation-contract-hardening

```yaml
task_id: OTV2-20260805-foundation-contract-hardening
title: Harden foundation ordering, migration evidence and cross-repository contracts
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/foundation-contract-hardening-20260805
pr: 15
base_sha: 5c074ad76c52168efede31824d7f28f482f844ce
head_sha: null
owner: architecture coordinator
created_at: 2026-08-05T13:15:00+02:00
updated_at: 2026-08-05T13:25:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
  - docs/agents/prompts/OTV2_GLOBAL_ARCHITECTURE_DECISION_COORDINATOR.md
  - docs/agents/CROSS_REPO_CONTRACTS.md
  - docs/agents/BUILD_TEST_MATRIX.md
  - docs/agents/REPOSITORY_MAP.md
  - docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
  - docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-contract-hardening.md
  - .github/workflows/otv2-foundation-contract-hardening.yml
public_contracts:
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
  - docs/contracts/FOUNDATION_ERROR_VOCABULARY.md
  - docs/contracts/FOUNDATION_FAILURE_SCENARIOS.md
depends_on:
  - ADR-0001 through ADR-0005
  - merged foundation execution guardrails PRs 13 and 14
blocks:
  - FND-01 launch until ordering and evidence requirements are reconciled
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
  - blakinio/Otheryn
  - blakinio/otclient
```

## Outcome

Persist the owner-approved architecture hardening discovered during the final pre-FND-01 review: move the minimum identifier vocabulary before wire/session freezing, make FND-01 an evidence-backed migration contract for the existing Rust client workspace, require machine-readable dependency and cross-repository locks, and add durable limit, error and failure-scenario registries without implementing runtime behavior.

## Architecture and source of truth

### PROVEN

- The canonical Oteryn v2 repository has no root Cargo workspace at base SHA `5c074ad76c52168efede31824d7f28f482f844ce`.
- `blakinio/otclient/oteryn-client` already contains merged Tokio transport, deterministic simulation/snapshot, architecture checks and other reusable Rust contracts.
- The current Platform native protocol contract is being corrected under `OTS-20260804-native-protocol-selection`; unmerged PR heads are not canonical contract revisions.
- The existing order places the full identifier contract after protocol and admission contracts even though those contracts already require stable identifier semantics.

### DERIVED

- Freezing wire/session schemas before a minimum identifier vocabulary risks later incompatible wire and database changes.
- Designing FND-01 without an exact migration inventory risks duplicate crates, duplicate domain ownership and loss of already validated Rust behavior.

## Acceptance criteria

- [ ] Introduce stable gate `FND-ID-01` before `FND-02` and `FND-04`, while retaining `DUR-01` for full durable/database identity decisions.
- [ ] Expand FND-01 to require exact existing-Rust migration classification and evidence, Cargo/toolchain/feature/target policy, and a machine-readable dependency-boundary model.
- [ ] Require a machine-readable cross-repository contract lock that accepts only merged canonical revisions and represents pending corrections as unresolved.
- [ ] Add initial machine-readable resource-limit registry and normative foundation error/failure scenario catalogues without inventing runtime values.
- [ ] Add clock semantics, world-format spike and exact client cutover requirements to the correct later gates.
- [ ] Reconcile backlog, global register, programme checkpoint, coordinator prompt and agent cross-repository/build/repository maps.
- [ ] Governance validation passes on the exact final head.
- [ ] Independent full-diff audit reports zero open material findings.

## Excluded scope

- No root Cargo workspace, crate, protocol codec, runtime, database schema, client source migration or production behavior.
- No writes to external repositories.
- No acceptance of an unmerged Platform PR or mutable PR head as a canonical revision.
- No final UUID/integer, tick frequency, queue size, chunk size or error-code value selection.

## Implementation / findings

- Task, dedicated branch and draft PR #15 created from exact current `main`.
- Repository had no overlapping active package or open PR at task start.
- Bounded architecture patch reconciles order, migration evidence and shared machine-readable registries.

## Validation

### Focused

- command/run: `python tools/agents/validate_governance.py`
- result: pending

### Component/integration

- result: `NOT_APPLICABLE` — documentation and machine-readable architecture contracts only

### E2E

- result: `NOT_APPLICABLE` — no executable runtime behavior changes

### Exact-head CI

- head: pending
- workflow/run: Agent governance, pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial full-diff architecture and consistency review
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Architecture hardening patch applied and final-tree governance validation started.
status: implementing
branch: docs/foundation-contract-hardening-20260805
head_sha: null
pr: 15
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Inspect the exact PR diff, complete the independent audit and record exact-head CI.
```
