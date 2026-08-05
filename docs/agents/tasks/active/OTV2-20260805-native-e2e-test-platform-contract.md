# OTV2-20260805-native-e2e-test-platform-contract

```yaml
task_id: OTV2-20260805-native-e2e-test-platform-contract
title: Define the native end-to-end test platform contract
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/qa-e2e-architecture-20260805
pr: null
base_sha: d4b5755cd45bfc6689f3614173f7c5701f56bb36
head_sha: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-05T17:33:00+02:00
updated_at: 2026-08-05T17:33:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260805-native-e2e-test-platform-contract.md
  - docs/architecture/ADR-0007-native-end-to-end-test-platform.md
  - docs/agents/BUILD_TEST_MATRIX.md
  - docs/agents/END_TO_END_FEATURE_COMPLETENESS.md
public_contracts:
  - docs/architecture/ADR-0007-native-end-to-end-test-platform.md
depends_on:
  - ADR-0001
  - ADR-0002
  - ADR-0003
  - ADR-0004
blocks:
  - VSL-01 completion until QA-E2E-01 is implemented and its required evidence exists
cross_repository_coordination_id: OTV2-QA-E2E-01
external_repositories:
  - blakinio/canary
  - blakinio/Oteryn-Platform
```

## Outcome

Persist an accepted architecture contract for a reusable native Oteryn v2 E2E platform that proves the complete client-to-server product path without making graphical client automation the only mechanism for failure, concurrency and recovery coverage.

## Architecture and source of truth

### PROVEN

- `blakinio/canary@f69632104888ece1d9afb801a90a66244694a627` contains a shared physical-client E2E platform, declarative scenario manifests and retained evidence for login, movement, combat, multiclient, NPC, Platform and recovery scenarios.
- Canary's `login/relog` scenario starts a disposable database, an exact controlled server and a real OTClient, then records semantic client markers, SQL assertions, logs, screenshots, session records and runtime hashes.
- Canary retained repeated-run evidence in which nine of ten physical `login/relog` attempts passed and one infrastructure/client-configuration attempt failed; the population was classified as unstable rather than silently retried into success.
- Oteryn v2 already requires named client/server E2E, character lease/relog, crash recovery, multichannel isolation, no-duplication and persistence failure evidence in `docs/agents/BUILD_TEST_MATRIX.md`.

### DERIVED

- A real native client is necessary to prove the supported product path, but using the graphical client as the only driver would make broad concurrency, protocol fault and failure-injection coverage too slow and fragile.
- A shared manifest-driven runner is preferable to feature-owned workflow copies because lifecycle, cleanup, evidence and security controls must remain consistent.

### ACCEPTED

- `QA-E2E-01` is the stable gate for the Native End-to-End Test Platform Contract.
- The platform uses three execution tiers: headless system E2E, instrumented native-client E2E and production-binary smoke E2E.
- `QA-E2E-01` blocks the claim that `VSL-01` is complete, but does not block architecture discovery, `FND-01` or the controlled `VSL-02` client migration.

## Acceptance criteria

- [ ] ADR-0007 records the three-tier execution model and its ownership boundaries.
- [ ] ADR-0007 defines scenario, evidence, cleanup, deterministic-control, failure-injection and flakiness requirements.
- [ ] The build/test matrix names `QA-E2E-01` and distinguishes the three tiers.
- [ ] End-to-end feature completeness requires evidence from the appropriate tier and forbids synthetic or environment-only success claims.
- [ ] No Rust workspace, runtime, client, protocol, Platform or CI implementation is introduced by this task.
- [ ] Governance validation passes on the exact final head.

## Excluded scope

- No test runner, test client, client adapter, workflow, container stack or fixture implementation.
- No changes to `blakinio/canary`, `blakinio/Oteryn-Platform`, `blakinio/otclient` or `blakinio/Otheryn`.
- No final choice of Rust test libraries, container orchestration library, renderer backend or CI runner fleet.
- No production credentials, endpoints, data or assets.

## Implementation / findings

- Canary is retained as architecture evidence and a migration/reference source, not as a runtime dependency.
- Direct SQL assertions are restricted to persistence/migration ownership; ordinary gameplay scenarios should prefer stable read-only probes, domain events and audit evidence.
- The instrumented client adapter may observe and submit normal product actions but may not bypass Platform admission, create authoritative sessions, mutate server state or replace server validation.

## Validation

### Focused

- command/run: `python tools/agents/validate_governance.py`
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only delivery with no executable runtime change
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — this task defines the future E2E platform and changes no executable product path
- result: pending

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: exact-diff architecture and scope review
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none identified at task start
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Dedicated branch created from main@d4b5755cd45bfc6689f3614173f7c5701f56bb36 and contract task claimed.
status: implementing
branch: docs/qa-e2e-architecture-20260805
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
blocker: null
next_action: Add ADR-0007 and align the canonical test/completeness policies.
```
