# OTV2-20260815-alpha-client-architecture

```yaml
task_id: OTV2-20260815-alpha-client-architecture
title: ALPHA-CLIENT-01 native client architecture
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/arch-e-alpha-client
pr: 273
base_sha: 088b46638ac014cd7928d6b0b75cee44902fe22c
head_sha: d9786582e7f3a15c60a3796f2eb6189ed9d7b222
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

`head_sha` above records the previously reviewed exact head before the current bounded P2 repair. The exact repaired final head is intentionally recorded in immutable PR/check/review evidence after the repair commit exists; this task file does not create a self-referential follow-up commit merely to copy its own SHA.

## Outcome

Delivered the bounded `ALPHA-CLIENT-01` architecture analysis and implementation-guiding candidate contract for the native Windows-first client. Two earlier P1 findings remain repaired, and the current bounded repair addresses the two independently confirmed P2 findings: the missing technology-neutral audio architecture boundary and the overstated Platform-directory field-rejection claim. Runtime implementation status remains `NOT_STARTED`; no executable client/Platform code was modified.

Draft PR: `#273`.

## Architecture and source of truth

- `PROVEN` — issue #263 and `docs/agents/programs/OTERYN_V2_ARCHITECTURE_PARALLEL_WORK_ALLOCATION.md` allocate worker E, this branch, this task record and the two ALPHA-CLIENT-01 architecture paths.
- `PROVEN` — trusted worker start ref is `main@088b46638ac014cd7928d6b0b75cee44902fe22c`; the previously reviewed PR head before this repair is `d9786582e7f3a15c60a3796f2eb6189ed9d7b222`.
- `PROVEN` — ADR-0003 requires Platform Identity -> one-time Game Login Ticket -> Platform-owned Game Gateway ticket redemption/World Registry route selection -> selected endpoint/channel/revisions + short-lived pre-admission material -> `protocol-oteryn` gameplay connection -> final game-owned admission/CharacterLease/GameSession authority. Gateway remains pre-admission/control-plane and does not own canonical `GameSessionId`.
- `PROVEN` — ADR-0011 requires a launchable, fail-closed `pre-native-protocol` client and forbids Canary/native-protocol placeholders or one-shot credential consumption for a path that cannot complete.
- `PROVEN` — ADR-0016 and `PROTOCOL_OTERYN_TRANSPORT_POLICY.json` record gameplay transport/client entry and every named player transport mode as runtime-unavailable until separately implemented and proven.
- `PROVEN` — current `apps/client` composition exposes `GameplayAvailability::PreNativeProtocol` and fails gameplay entry before route or credential use.
- `PROVEN` — current `crates/platform-client/src/lib.rs` recursively rejects only the 12 literal forbidden JSON keys `host`, `port`, `endpoint`, `endpoint_uri`, `protocol`, `protocol_profile`, `ticket`, `credential`, `game_session`, `admission`, `route`, `address`. It does not prove complete-schema or generic unknown-gameplay-field rejection; compound keys such as `game_session_id`, `admission_token` and `selected_endpoint` are not covered by that denylist.
- `PROVEN` — FND-02 requires generation fencing, ordered server sequencing, state revisions and snapshot/delta/resync; revision mismatch causes resync rather than speculative application.
- `PROVEN` — FND-02 and `ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-07.md` require independent wire correctness evidence beyond a shared production codec, including canonical byte goldens, malformed/adversarial corpus, property/invariant tests, parser/decoder fuzzing, cross-version fixtures, explicit limits and stable failure classes as applicable; this does not require a second production protocol stack.
- `PROVEN` — FND-04 retains final gameplay admission/control authority in Oteryn-v2 game-domain authority; client evidence is non-authoritative.
- `PROVEN` — DUR-04 requires client-safe allowlisted content projection and keeps client data non-authoritative; the repaired ALPHA-CLIENT-01 boundary applies the same projection/revision discipline to audio assets.
- `PROVEN` — ADR-0007 requires distinct Tier 1 headless system, Tier 2 native-client and Tier 3 release-binary E2E evidence.
- `PROVEN` — workspace boundaries classify `client-domain`, `client-simulation` and `synthetic-client-harness` as synthetic rather than production.
- `UNKNOWN` — exact future gameplay transport/protocol implementation APIs, Game Gateway client API/token representation, release updater/signing mechanism, renderer/UI/audio implementation libraries, installer technology, secure credential storage and production numeric limits beyond accepted parent contracts are not authorized or proven by this task and were deliberately not invented.

## Acceptance criteria

- [x] `ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` covers screen/composition/provider boundaries, runtime/session state, protocol/reconciliation seams, renderer/UI/input integration, technology-neutral audio provider/device/content/degradation/settings/evidence boundaries, client content projection, configuration/filesystem/logging/crash/update/packaging/install, headless versus interactive paths, Windows-first assumptions, production-readiness implications and E2E evidence.
- [x] Every substantial recommendation includes the required decide-now/defer test and explicit superseding evidence.
- [x] The design preserves current `pre-native-protocol` fail-closed behavior and does not expose unavailable transport modes or invent protocol/server/gameplay authority.
- [x] P1 #1 remains repaired: ADR-0003 is an explicit consumed parent and the client flow preserves Platform Identity -> one-time Game Login Ticket -> Platform Game Gateway redemption/route selection -> selected endpoint/channel/revisions + short-lived pre-admission material -> `protocol-oteryn` -> final game-owned FND-04 admission/CharacterLease/GameSession authority, with no directory-to-FND-04 shortcut.
- [x] P1 #2 remains repaired: Tier-1/future evidence may share production schemas/codecs but requires an independent FND-02 wire oracle through canonical byte goldens, malformed/adversarial fixtures, property/invariant tests, externally controlled decoder/parser fuzzing, cross-version fixtures, explicit resource ceilings and stable failure classes; no duplicate production protocol implementation is introduced.
- [x] P2 audio boundary repaired: application composition owns provider/device lifetime; audio is non-authoritative presentation only; assets are client-safe/revision-compatible; device/asset failure degrades presentation; resource use is bounded; settings/accessibility and test/evidence ownership are explicit; no audio library/vendor is selected.
- [x] P2 Platform-directory claim repaired: current behavior is stated exactly as the recursive 12-literal-key denylist; stronger complete-schema/reject-unknown-fields behavior is a future requirement unless implementation evidence proves it.
- [x] The candidate contract is included where it materially improves later implementation guidance while leaving unproven technology/library choices reversible.
- [x] `DECISIONS_NOT_TAKEN` explicitly records foreign/deferred decisions, including audio implementation technology.
- [x] `CROSS_DOMAIN_FINDINGS` reports networking/admission/content/release/E2E/diagnostics gaps with `worker_action: REPORT_ONLY`; the admission finding now records the exact current denylist limitation without absorbing Platform authority.
- [x] Changed paths are restricted to worker E ownership; no executable client code, DDL, production activation or coordinator-only overlay is intentionally modified.
- [ ] Final repaired exact-head changed-file/full-diff self-review and ordinary PR CI/governance evidence are recorded externally after the repair commit; per `TASK_TEMPLATE.md`, the task must not create a self-referential follow-up commit merely to copy those results.
- [x] Draft PR #273 remains draft and states `MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`; exact-head coordinator review follows the repaired-head validation.

## Excluded scope

No executable client or audio implementation; no protocol/server/gameplay authority contract rewrite; no TCP/QUIC adapter/listener or client gameplay-entry implementation; no Platform/Game Gateway implementation; no runtime change to `crates/platform-client`; no production credentials/secrets; no DDL/migration or production activation; no external-repository writes; no coordinator-only architecture status/register/horizon/governance edits; no owner-funded Copilot/Codex/OpenAI review trigger; no merge, lifecycle closeout, archival or ownership release.

## Implementation / findings

- Produced and repaired `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` with verified baseline, authority invariants, current-to-target mapping, provider/composition architecture, local session observation model, ADR-0003/FND-02/FND-04 reconciliation path, input/render/audio presentation boundaries, content/filesystem/diagnostics/update contracts, readiness gates, E2E matrix and six report-only cross-domain findings.
- Produced and repaired `docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_CONTRACT_CANDIDATE.md` with candidate normative `MUST`/`MUST NOT` boundaries and explicit non-authorization.
- Final-review P1 #1 remains addressed by restoring the full ADR-0003 pre-admission control-plane chain and explicitly retaining final `GameSessionId`/`CharacterLease` authority in game-domain/FND-04.
- Final-review P1 #2 remains addressed by requiring independent FND-02 wire evidence alongside any shared production schemas/codecs and explicitly rejecting a second production protocol stack as the solution.
- P2 audio architecture is addressed without selecting a vendor/library: provider/device lifetime belongs to `apps/client`; audio consumes presentation events and compatible client-safe assets only; failures are non-authoritative degradation; voices/buffers/queues/recovery are bounded; settings/accessibility and native-client evidence ownership are explicit.
- P2 current-state precision is addressed by direct inspection of `crates/platform-client/src/lib.rs`: documentation now names exactly the 12 recursive forbidden keys and records stronger schema/unknown-field rejection only as a future implementation requirement.
- Preserved `apps/client` as the sole production composition root and preserved `client-domain` / `client-simulation` / current synthetic harness as non-production under current workspace classification.
- Preserved UI/view/audio state and client world/session projection as non-authoritative, including no prediction or audio-timing authority.
- Preserved server-authoritative generation/sequence/revision/snapshot semantics and prohibited client-side guessed authoritative state.
- Defined release-content immutability, safe user/config/cache/diagnostics storage classes, privacy-bounded crash evidence and atomic verified update/rollback boundaries without selecting implementation technology.
- Preserved ADR-0007 three-tier E2E semantics and explicitly rejected treating the current synthetic harness or a shared codec round-trip as complete wire/system proof.
- No runtime implementation, external-repository mutation, coordinator-only overlay edit or owner-funded AI review was performed by this repair.

## DECISIONS_NOT_TAKEN

No exact UI toolkit/renderer replacement; no audio library/vendor/codec/mixer/device backend; no executable promotion/replacement of synthetic client crates; no prediction/rollback algorithm; no gameplay transport implementation or QUIC activation; no Game Gateway/pre-admission/admission/reconnect ticket/grant/token/API representation; no protocol implementation library; no content bundle/patch/CDN format; no installer/updater/signing provider; no exact Windows path/registry/install scope; no credential vault; no crash backend/retention/legal text; no release-channel/version-skew/forced-update policy; no Linux/macOS commitment; no server/gameplay/persistence/balance authority decision; no second production protocol implementation for testing.

## CROSS_DOMAIN_FINDINGS

`docs/architecture/ALPHA-CLIENT-01_NATIVE_CLIENT_ARCHITECTURE_ANALYSIS.md` records:

- `ALPHA-CLIENT-01-XD-01` / P1 / protocol-network-runtime — accepted TCP semantics exist, but gameplay transport adapter/listener/client entry are not implemented.
- `ALPHA-CLIENT-01-XD-02` / P1 / admission-session-integration — ADR-0003/FND-04 semantics require the ticket/Gateway/route/pre-admission/final-game-admission chain, while the client implementation of that handoff does not exist; final authority remains game-owned. Current directory-field enforcement is the exact recursive 12-key denylist, not complete-schema unknown-field rejection.
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
  source: earlier final review thread on PR #273
  repaired: true
  repair: restored ADR-0003 as explicit parent/consumed authority and removed the directory-selection -> FND-04 shortcut by requiring one-time ticket, Platform Game Gateway redemption/route selection, selected endpoint/channel/revisions, short-lived pre-admission material, protocol-oteryn connection and final game-owned FND-04 admission/CharacterLease/GameSession authority
```

```yaml
review_finding:
  id: PR273-P1-INDEPENDENT-WIRE-ORACLE
  severity: P1
  source: earlier final review thread on PR #273
  repaired: true
  repair: Tier-1/future protocol proof requires FND-02/2026-08-07 independent byte-level/adversarial/property/fuzz/cross-version/resource-limit/stable-failure evidence in addition to any shared production schemas/codecs; no second production protocol implementation is authorized
```

```yaml
review_finding:
  id: PR273-P2-AUDIO-BOUNDARY
  severity: P2
  source: final review thread on PR #273
  repaired: true
  repair: added technology-neutral application-owned audio provider/device lifetime, non-authoritative presentation semantics, client-safe content/revision compatibility, bounded resources, degradation, settings/accessibility and test/evidence ownership without choosing a library/vendor
```

```yaml
review_finding:
  id: PR273-P2-PLATFORM-DIRECTORY-PRECISION
  severity: P2
  source: final review thread on PR #273 plus direct inspection of crates/platform-client/src/lib.rs
  repaired: true
  repair: current state now names only the 12 literal recursively forbidden keys; compound/unknown field rejection is not claimed, and a stronger complete-schema boundary is future implementation evidence only
```

## Validation

### Focused

- command/run: repaired exact-head PR changed-file/full-diff review plus governance/authority review after the repair commit
- result: pending external exact-head inspection; no follow-up metadata commit is permitted solely to self-record its own SHA

### Component/integration

- command/run: `NOT_APPLICABLE`
- result: documentation-only allocated scope; executable client/server/protocol/Platform/audio implementation is explicitly outside this repair

### E2E

- scenario: `NOT_APPLICABLE` for this paper-only delivery
- result: no runtime was changed; the delivered architecture specifies future Tier 1/Tier 2/Tier 3, audio presentation and independent wire evidence obligations and must not claim those are currently implemented/proven

### Exact-head CI

- final head: recorded externally on PR #273 after the repair commit exists
- trigger source: ordinary GitHub PR/push checks on draft PR #273
- workflow/run/job: recorded externally on PR/check evidence
- runner assignment: recorded externally on PR/check evidence
- classification: documentation/governance exact-head validation
- result: pending current repaired-head checks

## Self-review

- exact head: recorded externally on PR #273 after the repair commit exists
- method/reviewer: full changed-file + full-patch + authority/dependency review
- material findings: two earlier P1 repairs remain in scope; the current repair targets the confirmed P2 audio boundary and Platform-directory precision findings. Any new material defect requires another repair head and review generation within the stable-gate budget.
- verdict: **PENDING CURRENT EXACT-HEAD FULL-DIFF SELF-REVIEW**

## Independent review

- required: YES — Architecture Coordinator exact-head re-audit is the handoff gate before canonicalization/merge.
- exact head: current repaired final worker head recorded externally on PR #273
- method/auditor: Architecture Coordinator; any owner-funded Codex/OpenAI review requires a fresh exact authorization for the exact current head and invocation.
- owner-funded authorization: previous authorization was consumed on older head `d9786582e7f3a15c60a3796f2eb6189ed9d7b222` and is not standing permission.
- material findings: pending current repaired-head coordinator re-audit
- verdict: pending

## PR and closeout

- changed-file review: current repaired exact-head result must be recorded externally on draft PR #273
- old review findings: two P1 findings are retained as repaired; two P2 findings are repaired in the owned architecture/task paths and remain open until exact-head proof confirms the fixes
- related/superseded PRs: none introduced by this repair
- PR state required: DRAFT / OPEN / UNMERGED until lawful coordinator integration
- protected auto-merge: not enabled
- merge commit/result: NOT PERFORMED
- ownership release: coordinator-only after any later lawful merge/lifecycle closeout
- owner-funded final review: NOT TRIGGERED; no current standing authorization exists for the repaired head

## Context checkpoint

```yaml
last_progress: confirmed P2 audio-boundary and Platform-directory-precision defects repaired within the three worker-E owned paths; exact-head full-diff review, reconciliation and CI are pending
status: validating
branch: docs/arch-e-alpha-client
head_sha: d9786582e7f3a15c60a3796f2eb6189ed9d7b222
pr: 273
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: push/pull_request
ci_check_generation: p2-repair-final-head-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 2
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: EXACT_HEAD_FULL_DIFF_SELF_REVIEW_RECONCILE_MAIN_CI_THEN_COORDINATOR_REAUDIT
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`