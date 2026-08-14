# OTV2-20260815-alpha-client-architecture

```yaml
task_id: OTV2-20260815-alpha-client-architecture
title: ALPHA-CLIENT-01 native client architecture
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-e-alpha-client
pr: null
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT / worker E
created_at: 2026-08-15T00:19:00+02:00
updated_at: 2026-08-15T00:19:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260815-alpha-client-architecture.md
  - docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md
  - docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md
public_contracts:
  - docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md
depends_on:
  - issue:#263
  - docs/architecture/ADR-0011-native-client-pre-protocol-migration-state.md
  - docs/architecture/ADR-0016-gameplay-transport-client-mode-runtime-readiness.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Produce the bounded `ALPHA-CLIENT-01` architecture analysis and an implementation-guiding candidate contract for the native Windows-first client. The delivery must preserve accepted server/gameplay/protocol authority, make the current `pre-native-protocol` state explicit, and define reversible client composition/readiness seams without claiming unavailable runtime capability.

## Architecture and source of truth

- `PROVEN` — issue #263 and `docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md` allocate worker E, this branch, this task record, and the two ALPHA-CLIENT-01 architecture paths.
- `PROVEN` — trusted worker start ref is `main@088b46638ac014cd7928d6b0b75cee44902fe22c`; the worker branch was verified at that exact ref before work started.
- `PROVEN` — live `main` later advanced to `cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e` only through the orchestration setup lifecycle closeout commit whose parent is the trusted worker start ref. Allocation policy does not authorize this worker to rebase independently.
- `PROVEN` — ADR-0011 requires a launchable, fail-closed `pre-native-protocol` client and forbids Canary/native-protocol placeholders.
- `PROVEN` — ADR-0016 records every gameplay transport client mode as runtime-unavailable until separately implemented and proven.
- `PROVEN` — current `apps/client` composition exposes `GameplayAvailability::PreNativeProtocol` and fails gameplay entry before route or credential use.
- `PROVEN` — FND-04 retains final gameplay admission/control authority in Oteryn-v2 game-domain authority; client evidence is non-authoritative.
- `PROVEN` — DUR-04 requires client-safe allowlisted content projection and keeps client data non-authoritative.
- `UNKNOWN` — exact future gameplay transport/protocol implementation APIs, release updater/signing mechanism, renderer/UI framework composition, installer technology, and production numeric limits are not authorized or proven by this task and must not be invented.

## Acceptance criteria

- [ ] `ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` covers screen/composition/provider boundaries, runtime/session state, protocol/reconciliation seams, renderer/UI/input integration, client content projection, configuration/filesystem/logging/crash/update/packaging/install, headless versus interactive paths, Windows-first assumptions, production-readiness implications and E2E evidence.
- [ ] Every substantial recommendation includes the required decide-now/defer test and explicit superseding evidence.
- [ ] The design preserves current `pre-native-protocol` fail-closed behavior and does not expose unavailable transport modes or invent protocol/server/gameplay authority.
- [ ] The optional candidate contract is included only where it materially improves later implementation guidance while remaining reversible on unproven technology/library choices.
- [ ] `DECISIONS_NOT_TAKEN` explicitly records foreign/deferred decisions.
- [ ] `CROSS_DOMAIN_FINDINGS` reports any networking, server/gameplay, security, content or release gaps with `worker_action: REPORT_ONLY`.
- [ ] Changed paths remain within worker E ownership and no executable client code, DDL, production activation or coordinator-only overlay is modified.
- [ ] Final exact-head self-review and ordinary PR CI/governance evidence are recorded outside the frozen commit where self-reference would otherwise be required.
- [ ] Draft PR remains draft and states `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY` with `COORDINATOR_AUDIT` as the only next action.

## Excluded scope

No executable client implementation; no protocol/server/gameplay authority contract rewrite; no TCP/QUIC adapter/listener or client gameplay-entry implementation; no production credentials/secrets; no DDL/migration or production activation; no external-repository writes; no coordinator-only architecture status/register/horizon/governance edits; no owner-funded Copilot/Codex/OpenAI review trigger without separate exact authorization; no merge, lifecycle closeout, archival or ownership release.

## Implementation / findings

- Worker branch and issue ownership verified with no existing PR for `docs/arch-e-alpha-client`.
- Research is reading accepted architecture, migrated client provenance and current destination Rust client composition before freezing any new ALPHA-CLIENT-01 recommendation.
- The current branch is intentionally anchored to the trusted start ref; the one-commit `main` drift is a coordinator lifecycle bookkeeping commit, not authority for this worker to rewrite its base.

## Validation

### Focused

- command/run: pending architecture/governance validation on final changed set
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` unless non-document paths unexpectedly change
- result: pending; allocated scope is documentation-only and executable changes are forbidden

### E2E

- scenario: `NOT_APPLICABLE` for this delivery; runtime implementation is explicitly out of scope. The architecture output will define future E2E obligations.
- result: pending

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: DOMAIN ARCHITECTURE DESIGN AGENT / worker E (mandatory exact-head review)
- material findings: pending
- verdict: pending

## Independent review

- required: YES — multi-agent architecture policy requires Architecture Coordinator audit before canonicalization/merge; no owner-funded AI review is authorized by issue #263
- exact head: pending
- method/auditor: Architecture Coordinator after worker handoff
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none found for worker branch at task start
- protected auto-merge: FORBIDDEN for this worker
- merge commit/result: NOT_AUTHORIZED
- ownership release: coordinator-only after any later authorized merge/lifecycle closeout

## Context checkpoint

```yaml
last_progress: worker task opened after verifying issue #263, trusted start ref and branch ownership
status: implementing
branch: docs/arch-e-alpha-client
head_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: null
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: complete bounded ALPHA-CLIENT-01 architecture research and design
```
