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
head_sha: dd692b2b78bddd6b2b76214f1b45f184e07bce2f
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT / worker E
created_at: 2026-08-15T00:19:00+02:00
updated_at: 2026-08-15T11:13:00+02:00
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
  - docs/architecture/ADR-0003-platform-identity-game-gateway-and-admission-boundary.md
  - docs/architecture/ADR-0011-native-client-pre-protocol-migration-state.md
  - docs/architecture/ADR-0016-gameplay-transport-client-mode-runtime-readiness.md
  - docs/architecture/FND-02_PROTOCOL_OTERYN_V1_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/architecture/ADR-0007-native-end-to-end-test-platform.md
  - docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md
  - docs/architecture/CLIENT_CRASH_DIAGNOSTICS_PRIVACY_OWNER_BASELINE.md
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

`head_sha` above records the verified repair-parent head. The exact repaired final head is intentionally recorded in immutable PR/check/review evidence after the repair commit exists; this task file does not create a self-referential follow-up commit merely to copy its own SHA.

## Outcome

Delivered the bounded `ALPHA-CLIENT-01` architecture analysis and implementation-guiding candidate contract for the native Windows-first client, then narrowly repaired the two P1 findings confirmed in final review of PR #273. The repaired design preserves the accepted ADR-0003 admission chain and FND-02 independent-wire-evidence requirement without changing runtime implementation status or broadening client architecture scope.

Draft PR: `#273`.

## Architecture and source of truth

- `PROVEN` — issue #263 and `docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md` allocate worker E, this branch, this task record and the two ALPHA-CLIENT-01 architecture paths.
- `PROVEN` — trusted worker start ref is `main@088b46638ac014cd7928d6b0b75cee44902fe22c`; later coordinator integration produced verified repair-parent head `dd692b2b78bddd6b2b76214f1b45f184e07bce2f` while preserving only the same three worker-E changed paths against the then-current main.
- `PROVEN` — ADR-0003 requires Platform Identity -> one-time Game Login Ticket -> Platform-owned Game Gateway ticket redemption/World Registry route selection -> selected endpoint/channel/revisions + short-lived pre-admission material -> `protocol-oteryn` gameplay connection -> final game-owned admission/CharacterLease/GameSession authority. Gateway remains pre-admission/control-plane and does not own canonical `GameSessionId`.
- `PROVEN` — ADR-0011 requires a launchable, fail-closed `pre-native-protocol` client and forbids Canary/native-protocol placeholders or one-shot credential consumption for a path that cannot complete.
- `PROVEN` — ADR-0016 and `PROTOCOL_OTERYN_TRANSPORT_POLICY.json` record gameplay transport/client entry and every named player transport mode as runtime-unavailable until separately implemented and proven.
- `PROVEN` — current `apps/client` composition exposes `GameplayAvailability::PreNativeProtocol` and fails gameplay entry before route or credential use.
- `PROVEN` — current `crates/platform-client` rejects gameplay endpoint/protocol/ticket/credential/session/admission fields in Platform directory data.
- `PROVEN` — FND-02 requires generation fencing, ordered server sequencing, state revisions and snapshot/delta/resync; revision mismatch causes resync rather than speculative application.
- `PROVEN` — FND-02 and `ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md` require independent wire correctness evidence beyond a shared production codec, including canonical byte goldens, malformed/adversarial corpus, property/invariant tests, parser/decoder fuzzing, cross-version fixtures, explicit limits and stable failure classes as applicable; this does not require a second production protocol stack.
- `PROVEN` — FND-04 retains final gameplay admission/control authority in Oteryn-v2 game-domain authority; client evidence is non-authoritative.
- `PROVEN` — DUR-04 requires client-safe allowlisted content projection and keeps client data non-authoritative.
- `PROVEN` — ADR-0007 requires distinct Tier 1 headless system, Tier 2 native-client and Tier 3 release-binary E2E evidence.
- `PROVEN` — workspace boundaries classify `client-domain`, `client-simulation` and `synthetic-client-harness` as synthetic rather than production.
- `UNKNOWN` — exact future gameplay transport/protocol implementation APIs, Game Gateway client API/token representation, release updater/signing mechanism, renderer/UI framework composition, installer technology, secure credential storage and production numeric limits beyond accepted parent contracts are not authorized or proven by this task and were deliberately not invented.

## Acceptance criteria

- [x] `ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` covers screen/composition/provider boundaries, runtime/session state, protocol/reconciliation seams, renderer/UI/input integration, client content projection, configuration/filesystem/logging/crash/update/packaging/install, headless versus interactive paths, Windows-first assumptions, production-readiness implications and E2E evidence.
- [x] Every substantial recommendation includes the required decide-now/defer test and explicit superseding evidence.
- [x] The design preserves current `pre-native-protocol` fail-closed behavior and does not expose unavailable transport modes or invent protocol/server/gameplay authority.
- [x] P1 #1 repaired: ADR-0003 is an explicit consumed parent and the client flow preserves Platform Identity -> one-time Game Login Ticket -> Platform Game Gateway redemption/route selection -> selected endpoint/channel/revisions + short-lived pre-admission material -> `protocol-oteryn` -> final game-owned FND-04 admission/CharacterLease/GameSession authority, with no directory-to-FND-04 shortcut.
- [x] P1 #2 repaired: Tier-1/future evidence may share production schemas/codecs but requires an independent FND-02 wire oracle through canonical byte goldens, malformed/adversarial fixtures, property/invariant tests, externally controlled decoder/parser fuzzing, cross-version fixtures, explicit resource ceilings and stable failure classes; no duplicate production protocol implementation is introduced.
- [x] The candidate contract is included where it materially improves later implementation guidance while leaving unproven technology/library choices reversible.
- [x] `DECISIONS_NOT_TAKEN` explicitly records foreign/deferred decisions.
- [x] `CROSS_DOMAIN_FINDINGS` reports networking/admission/content/release/E2E/diagnostics gaps with `worker_action: REPORT_ONLY`.
- [x] Changed paths are restricted to worker E ownership; no executable client code, DDL, production activation or coordinator-only overlay is intentionally modified.
- [ ] Final repaired exact-head changed-file/full-diff self-review and ordinary PR CI/governance evidence are recorded externally after the repair commit; per `TASK_TEMPLATE.md`, the task must not create a self-referential follow-up commit merely to copy those results.
- [x] Draft PR #273 remains draft and states `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`; the worker's required handoff is `ARCHITECTURE_COORDINATOR_EXACT_HEAD_REAUDIT`.

## Excluded scope

No executable client implementation; no protocol/server/gameplay authority contract rewrite; no TCP/QUIC adapter/listener or client gameplay-entry implementation; no Platform/Game Gateway implementation; no production credentials/secrets; no DDL/migration or production activation; no external-repository writes; no coordinator-only architecture status/register/horizon/governance edits; no owner-funded Copilot/Codex/OpenAI review trigger; no merge, lifecycle closeout, archival or ownership release.

## Implementation / findings

- Produced and repaired `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` with verified baseline, authority invariants, current-to-target mapping, provider/composition architecture, local session observation model, ADR-0003/FND-02/FND-04 reconciliation path, input/render boundaries, content/filesystem/diagnostics/update contracts, readiness gates, E2E matrix and six report-only cross-domain findings.
- Produced and repaired `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md` with candidate normative `MUST`/`MUST NOT` boundaries and explicit non-authorization.
- Final-review P1 #1 is addressed by restoring the full ADR-0003 pre-admission control-plane chain and explicitly retaining final `GameSessionId`/`CharacterLease` authority in game-domain/FND-04.
- Final-review P1 #2 is addressed by requiring independent FND-02 wire evidence alongside any shared production schemas/codecs and explicitly rejecting a second production protocol stack as the solution.
- Preserved `apps/client` as the sole production composition root and preserved `client-domain` / `client-simulation` / current synthetic harness as non-production under current workspace classification.
- Preserved UI/view state and client world/session projection as non-authoritative, including no prediction authority.
- Preserved server-authoritative generation/sequence/revision/snapshot semantics and prohibited client-side guessed authoritative state.
- Defined release-content immutability, safe user/config/cache/diagnostics storage classes, privacy-bounded crash evidence and atomic verified update/rollback boundaries without selecting implementation technology.
- Preserved ADR-0007 three-tier E2E semantics and explicitly rejected treating the current synthetic harness or a shared codec round-trip as complete wire/system proof.
- No runtime implementation, external-repository mutation, coordinator-only overlay edit or owner-funded AI review was performed.

## DECISIONS_NOT_TAKEN

No exact UI toolkit/renderer replacement; no executable promotion/replacement of synthetic client crates; no prediction/rollback algorithm; no gameplay transport implementation or QUIC activation; no Game Gateway/pre-admission/admission/reconnect ticket/grant/token/API representation; no protocol implementation library; no content bundle/patch/CDN format; no installer/updater/signing provider; no exact Windows path/registry/install scope; no credential vault; no crash backend/retention/legal text; no release-channel/version-skew/forced-update policy; no Linux/macOS commitment; no server/gameplay/persistence/balance authority decision; no second production protocol implementation for testing.

## CROSS_DOMAIN_FINDINGS

`docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` records:

- `ALPHA-CLIENT-01-XD-01` / P1 / protocol-network-runtime — accepted TCP semantics exist, but gameplay transport adapter/listener/client entry are not implemented.
- `ALPHA-CLIENT-01-XD-02` / P1 / admission-session-integration — ADR-0003/FND-04 semantics require the ticket/Gateway/route/pre-admission/final-game-admission chain, while the client implementation of that handoff does not exist; final authority remains game-owned.
- `ALPHA-CLIENT-01-XD-03` / P1 / content-release-toolchain — client-safe projection semantics exist, but physical artifact/patch/signing activation implementation is unresolved.
- `ALPHA-CLIENT-01-XD-04` / P1 / security-release-sre — external alpha requires signed updater/artifacts, provenance/SBOM, threat-model and rollback/operability evidence not owned by this worker.
- `ALPHA-CLIENT-01-XD-05` / P2 / qa-e2e — current synthetic harness is not ADR-0007 Tier 1 production-protocol system E2E, and future Tier 1 sharing production codecs still requires FND-02 independent wire evidence.
- `ALPHA-CLIENT-01-XD-06` / P2 / diagnostics-privacy-platform — privacy boundaries are accepted, while crash ingestion/retention production contracts remain outside this task.

All findings use `worker_action: REPORT_ONLY` in the analysis and no foreign-domain mutation was made.

## Repair review findings

```yaml
review_finding:
  id: PR273-P1-ADMISSION-CHAIN
  severity: P1
  source: final review thread on PR #273
  repaired: true
  repair: restored ADR-0003 as explicit parent/consumed authority and removed the directory-selection -> FND-04 shortcut by requiring one-time ticket, Platform Game Gateway redemption/route selection, selected endpoint/channel/revisions, short-lived pre-admission material, protocol-oteryn connection and final game-owned FND-04 admission/CharacterLease/GameSession authority
```

```yaml
review_finding:
  id: PR273-P1-INDEPENDENT-WIRE-ORACLE
  severity: P1
  source: final review thread on PR #273
  repaired: true
  repair: Tier-1/future protocol proof now requires FND-02/2026-08-07 independent byte-level/adversarial/property/fuzz/cross-version/resource-limit/stable-failure evidence in addition to any shared production schemas/codecs; no second production protocol implementation is authorized
```

## Validation

### Focused

- command/run: repaired exact-head PR changed-file/full-diff review plus governance/authority review after the repair commit
- result: to be recorded in immutable PR/review evidence for the repaired final head; no follow-up metadata commit is permitted solely to self-record its own SHA

### Component/integration

- command/run: `NOT_APPLICABLE`
- result: documentation-only allocated scope; executable client/server/protocol/Platform implementation is explicitly forbidden by issue #263 and this repair instruction

### E2E

- scenario: `NOT_APPLICABLE` for this worker delivery
- result: no runtime was changed; the delivered architecture specifies future Tier 1/Tier 2/Tier 3 and independent wire evidence obligations and must not claim those are currently proven

### Exact-head CI

- final head: recorded externally on PR #273 after the repair commit exists
- trigger source: ordinary GitHub PR/push checks on draft PR #273
- workflow/run/job: recorded externally on PR/check evidence
- runner assignment: recorded externally on PR/check evidence
- classification: documentation/governance exact-head validation
- result: recorded externally on PR/check evidence

## Self-review

- exact head: recorded externally on PR #273 after the repair commit exists
- method/reviewer: DOMAIN ARCHITECTURE DESIGN AGENT / worker E; mandatory changed-file + full-patch + authority/dependency review
- material findings: the two confirmed P1s above are the bounded repair target; any remaining material defect requires another repair head and a new exact-head review generation
- verdict: recorded externally after repaired-head inspection

## Independent review

- required: YES — Architecture Coordinator exact-head re-audit is the worker handoff gate before canonicalization/merge; the owner has separately authorized one second owner-funded final review only after that coordinator re-audit and fresh CI
- exact head: repaired final worker head recorded on PR #273
- method/auditor: Architecture Coordinator first; owner-authorized second owner-funded review is reserved for coordinator use after its own re-audit
- worker action: MUST NOT trigger owner-funded review
- material findings: pending repaired-head coordinator re-audit
- verdict: pending

## PR and closeout

- changed-file review: repaired exact-head result recorded externally on draft PR #273
- old review findings: both confirmed P1 findings are explicitly repaired in the two owned architecture documents and this task record; review-thread responses are recorded on PR #273 after exact-head verification
- related/superseded PRs: none introduced by this repair
- PR state required: DRAFT / OPEN / UNMERGED
- protected auto-merge: FORBIDDEN for this worker
- merge commit/result: NOT_AUTHORIZED
- ownership release: coordinator-only after any later authorized merge/lifecycle closeout
- owner-funded final review: NOT_TRIGGERED_BY_WORKER; reserved for coordinator after repaired exact-head re-audit and fresh CI

## Context checkpoint

```yaml
last_progress: two confirmed PR #273 P1 findings repaired within the three worker-E owned paths; repaired final SHA/self-review/CI evidence will be recorded externally without a self-referential metadata commit
status: ready
branch: docs/arch-e-alpha-client
head_sha: dd692b2b78bddd6b2b76214f1b45f184e07bce2f
pr: 273
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: push/pull_request
ci_check_generation: repaired-head-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 1
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: ARCHITECTURE_COORDINATOR_EXACT_HEAD_REAUDIT
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
