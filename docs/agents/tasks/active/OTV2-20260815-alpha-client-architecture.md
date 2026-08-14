# OTV2-20260815-alpha-client-architecture

```yaml
task_id: OTV2-20260815-alpha-client-architecture
title: ALPHA-CLIENT-01 native client architecture
mode: CONTRACT
status: ready
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-e-alpha-client
pr: 273
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: d1723028a40f28f9c18ae8e5267dc142d8da7803
final_head_sha: null
final_head_frozen_at: 2026-08-15T00:29:12+02:00
owner: DOMAIN ARCHITECTURE DESIGN AGENT / worker E
created_at: 2026-08-15T00:19:00+02:00
updated_at: 2026-08-15T00:29:12+02:00
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
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/ADR-0007-native-end-to-end-test-platform.md
  - docs/architecture/CLIENT_CRASH_DIAGNOSTICS_PRIVACY_OWNER_BASELINE.md
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

## Outcome

Delivered the bounded `ALPHA-CLIENT-01` architecture analysis and implementation-guiding candidate contract for the native Windows-first client. The design preserves accepted server/gameplay/protocol authority, makes the current `pre-native-protocol` state explicit, and defines reversible composition/readiness seams without claiming unavailable runtime capability.

Draft PR: `#273`.

## Architecture and source of truth

- `PROVEN` — issue #263 and `docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md` allocate worker E, this branch, this task record and the two ALPHA-CLIENT-01 architecture paths.
- `PROVEN` — trusted worker start ref is `main@088b46638ac014cd7928d6b0b75cee44902fe22c`; the worker branch was verified at that exact ref before work started.
- `PROVEN` — live `main` later advanced to `cb98fd32a2bb71fce83234ebf8bf69bdd1a1970e` only through the orchestration setup lifecycle closeout commit whose parent is the trusted worker start ref. Allocation policy does not authorize this worker to rebase independently.
- `PROVEN` — ADR-0011 requires a launchable, fail-closed `pre-native-protocol` client and forbids Canary/native-protocol placeholders.
- `PROVEN` — ADR-0016 and `PROTOCOL_OTERYN_TRANSPORT_POLICY.json` record gameplay transport/client entry and every named player transport mode as runtime-unavailable until separately implemented and proven.
- `PROVEN` — current `apps/client` composition exposes `GameplayAvailability::PreNativeProtocol` and fails gameplay entry before route or credential use.
- `PROVEN` — current `crates/platform-client` rejects gameplay endpoint/protocol/ticket/credential/session/admission fields in Platform directory data.
- `PROVEN` — FND-02 requires generation fencing, ordered server sequencing, state revisions and snapshot/delta/resync; revision mismatch causes resync rather than speculative application.
- `PROVEN` — FND-04 retains final gameplay admission/control authority in Oteryn-v2 game-domain authority; client evidence is non-authoritative.
- `PROVEN` — DUR-04 requires client-safe allowlisted content projection and keeps client data non-authoritative.
- `PROVEN` — ADR-0007 requires distinct Tier 1 headless system, Tier 2 native-client and Tier 3 release-binary E2E evidence.
- `PROVEN` — workspace boundaries classify `client-domain`, `client-simulation` and `synthetic-client-harness` as synthetic rather than production.
- `UNKNOWN` — exact future gameplay transport/protocol implementation APIs, release updater/signing mechanism, renderer/UI framework composition, installer technology, secure credential storage and production numeric limits are not authorized or proven by this task and were deliberately not invented.

## Acceptance criteria

- [x] `ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` covers screen/composition/provider boundaries, runtime/session state, protocol/reconciliation seams, renderer/UI/input integration, client content projection, configuration/filesystem/logging/crash/update/packaging/install, headless versus interactive paths, Windows-first assumptions, production-readiness implications and E2E evidence.
- [x] Every substantial recommendation includes the required decide-now/defer test and explicit superseding evidence.
- [x] The design preserves current `pre-native-protocol` fail-closed behavior and does not expose unavailable transport modes or invent protocol/server/gameplay authority.
- [x] The candidate contract is included where it materially improves later implementation guidance while leaving unproven technology/library choices reversible.
- [x] `DECISIONS_NOT_TAKEN` explicitly records foreign/deferred decisions.
- [x] `CROSS_DOMAIN_FINDINGS` reports networking/admission/content/release/E2E/diagnostics gaps with `worker_action: REPORT_ONLY`.
- [x] Changed paths are restricted to worker E ownership; no executable client code, DDL, production activation or coordinator-only overlay is intentionally modified.
- [ ] Final exact-head changed-file/self-review and ordinary PR CI/governance evidence are recorded externally after this freeze commit; per `TASK_TEMPLATE.md`, the task must not create a self-referential follow-up commit merely to copy those results.
- [x] Draft PR #273 is draft and states `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY` with `COORDINATOR_AUDIT` as the only worker handoff action.

## Excluded scope

No executable client implementation; no protocol/server/gameplay authority contract rewrite; no TCP/QUIC adapter/listener or client gameplay-entry implementation; no production credentials/secrets; no DDL/migration or production activation; no external-repository writes; no coordinator-only architecture status/register/horizon/governance edits; no owner-funded Copilot/Codex/OpenAI review trigger without separate exact authorization; no merge, lifecycle closeout, archival or ownership release.

## Implementation / findings

- Produced `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` with verified baseline, authority invariants, current-to-target mapping, provider/composition architecture, local session observation model, FND-02 reconciliation path, input/render boundaries, content/filesystem/diagnostics/update contracts, readiness gates, E2E matrix and six report-only cross-domain findings.
- Produced `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md` with candidate normative `MUST`/`MUST NOT` boundaries and explicit non-authorization.
- Preserved `apps/client` as the sole production composition root and preserved `client-domain` / `client-simulation` / current synthetic harness as non-production under current workspace classification.
- Preserved the separation between Identity/Platform directory and future FND-04/FND-02 gameplay admission/transport.
- Preserved server-authoritative generation/sequence/revision/snapshot semantics and prohibited client-side guessed authoritative state.
- Defined release-content immutability, safe user/config/cache/diagnostics storage classes, privacy-bounded crash evidence and atomic verified update/rollback boundaries without selecting implementation technology.
- Preserved ADR-0007 three-tier E2E semantics and explicitly rejected treating the current synthetic harness as Tier 1 system E2E.
- Branch remains intentionally anchored to trusted worker ancestry; no worker rebase onto coordinator lifecycle bookkeeping was performed.

## DECISIONS_NOT_TAKEN

No exact UI toolkit/renderer replacement; no executable promotion/replacement of synthetic client crates; no prediction/rollback algorithm; no gameplay transport implementation or QUIC activation; no FND-04 grant/token/API shape; no protocol implementation library; no content bundle/patch/CDN format; no installer/updater/signing provider; no exact Windows path/registry/install scope; no credential vault; no crash backend/retention/legal text; no release-channel/version-skew/forced-update policy; no Linux/macOS commitment; no server/gameplay/persistence/balance authority decision.

## CROSS_DOMAIN_FINDINGS

`docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` records:

- `ALPHA-CLIENT-01-XD-01` / P1 / protocol-network-runtime — accepted TCP semantics exist, but gameplay transport adapter/listener/client entry are not implemented.
- `ALPHA-CLIENT-01-XD-02` / P1 / admission-session-integration — accepted FND-04 semantics exist, but the client Platform-selection -> admission/transport handoff is not implemented.
- `ALPHA-CLIENT-01-XD-03` / P1 / content-release-toolchain — client-safe projection semantics exist, but physical artifact/patch/signing activation implementation is unresolved.
- `ALPHA-CLIENT-01-XD-04` / P1 / security-release-sre — external alpha requires signed updater/artifacts, provenance/SBOM, threat-model and rollback/operability evidence not owned by this worker.
- `ALPHA-CLIENT-01-XD-05` / P2 / qa-e2e — current synthetic harness is not ADR-0007 Tier 1 production-protocol system E2E.
- `ALPHA-CLIENT-01-XD-06` / P2 / diagnostics-privacy-platform — privacy boundaries are accepted, while crash ingestion/retention production contracts remain outside this task.

All findings use `worker_action: REPORT_ONLY` in the analysis and no foreign-domain mutation was made.

## Validation

### Focused

- command/run: final exact-head PR changed-file/diff review plus governance/authority review after freeze commit
- result: to be recorded in immutable PR/check evidence for the final head; no follow-up metadata commit is permitted solely to self-record its own SHA

### Component/integration

- command/run: `NOT_APPLICABLE`
- result: documentation-only allocated scope; executable client/server/protocol implementation is explicitly forbidden by issue #263

### E2E

- scenario: `NOT_APPLICABLE` for this worker delivery
- result: no runtime was changed; the delivered architecture specifies future Tier 1/Tier 2/Tier 3 evidence obligations and must not claim those are currently proven

### Exact-head CI

- final head: recorded externally on PR #273 after this freeze commit exists
- trigger source: ordinary `pull_request` checks on draft PR #273
- workflow/run/job: recorded externally on PR/check evidence
- runner assignment: recorded externally on PR/check evidence
- classification: documentation/governance exact-head validation
- result: recorded externally on PR/check evidence

## Self-review

- exact head: recorded externally on PR #273 after this freeze commit exists
- method/reviewer: DOMAIN ARCHITECTURE DESIGN AGENT / worker E; mandatory changed-file + patch + authority/dependency review
- material findings: recorded externally; any material defect requires a repair commit and a new exact-head review generation
- verdict: recorded externally

## Independent review

- required: YES — multi-agent architecture policy requires Architecture Coordinator audit before canonicalization/merge; no owner-funded AI review is authorized by issue #263
- exact head: final worker head recorded on PR #273
- method/auditor: Architecture Coordinator after worker handoff
- material findings: pending coordinator audit
- verdict: pending coordinator audit

## PR and closeout

- changed-file review: final exact-head result recorded externally on draft PR #273
- unresolved review threads: none known at freeze preparation; coordinator audit pending
- related/superseded PRs: none found for worker branch before draft PR #273
- protected auto-merge: FORBIDDEN for this worker
- merge commit/result: NOT_AUTHORIZED
- ownership release: coordinator-only after any later authorized merge/lifecycle closeout

## Context checkpoint

```yaml
last_progress: ALPHA-CLIENT-01 analysis and candidate contract committed; draft PR #273 opened; worker task frozen for exact-head external validation and coordinator audit
status: ready
branch: docs/arch-e-alpha-client
head_sha: d1723028a40f28f9c18ae8e5267dc142d8da7803
pr: 273
final_head_sha: null
final_head_frozen_at: 2026-08-15T00:29:12+02:00
ci_trigger_source: pull_request
ci_check_generation: pending-final-head
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
next_action: COORDINATOR_AUDIT
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
