# OTV2-20260812-dur-04-content-world-scripting

```yaml
task_id: OTV2-20260812-dur-04-content-world-scripting
title: DUR-04 content world and scripting architecture
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-dur-04-content-world-scripting
pr: 212
base_sha: c0b7b3b5928b194f8b51a4a51d9eb2d01e32ce44
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T23:21:00+02:00
updated_at: 2026-08-12T23:56:00+02:00
execution_budget_minutes: 90
large_budget_reason: Bounded architecture gate spans deterministic content compilation, immutable world bundles, migration/provenance, secure loading and capability-bounded deterministic scripting; no implementation is authorized.
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-dur-04-content-world-scripting.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_ANALYSIS.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
public_contracts:
  - DUR-04
depends_on:
  - ADR-0005
  - GAME-VISION-01
  - GAME-ITEM-01
  - DUR-02
  - DUR-03
  - GAME-CHANNEL-01
  - FND-03
  - ANL-01
blocks:
  - broad content import
  - durable scripted behavior
  - final content/bundle implementation contract
cross_repository_coordination_id: OTV2-NATIVE-WORLD-CONTENT
external_repositories:
  - blakinio/Otheryn
```

## Outcome

Produce one bounded paper-only `DUR-04 — Content, World Detail and Scripting Contract` candidate completing the architecture left deliberately open by ADR-0005 without implementing World Project encoding, compiler, World Bundle, loader, Studio or scripting runtime.

No Rust/runtime/client implementation, PostgreSQL DDL/migrations, Studio implementation, production configuration/deployment, Platform write or entitlement activation is authorized.

Maintained current-status/register/horizon/index/handoff files remain outside this delivery PR and may be promoted only by a separate lifecycle closeout after an accepted delivery merge.

## Verified architecture/source facts

- `PROVEN`: post-GAME-CHANNEL `main@c0b7b3b5928b194f8b51a4a51d9eb2d01e32ce44` selected `DUR-04 = PROPOSED / PLANNED / NOT_STARTED` as the next paper-only architecture gate.
- `PROVEN`: no active DUR-04 task and no open DUR-04 PR existed at task start.
- `PROVEN`: ADR-0005 already accepts the native semantic world/content model and deliberately defers exact physical encoding/chunk/compression choices to a bounded spike.
- `PROVEN`: Resource Limits Registry makes missing externally controlled hard limits a review failure, never implicit unlimited behavior.
- `PROVEN`: GAME-ITEM/DUR-03/GAME-CHANNEL/FND-03 boundaries prohibit script-side authority bypass, unclassified per-channel value multiplication and unbounded authoritative work.
- `PROVEN`: official Wasmtime documentation distinguishes deterministic fuel from nondeterministic epoch interruption and documents other determinism hazards including nondeterministic imports and memory/table behavior.
- `PROVEN`: Component Model WIT defines typed import/export interfaces suitable for a project-owned capability ABI.
- `PROVEN`: governance forbids new Codex/OpenAI API/owner-funded AI invocation without specific owner permission. None was invoked for DUR-04.
- `UNKNOWN/DEFERRED`: final source serializer, final bundle container, chunk/floor packing, compression codec, exact numeric resource ceilings and exact Wasmtime crate version.

## Candidate decisions delivered

- [x] Stable `PackageKey`, immutable `PackageRevision`, stable `ContentKey` and exact Content Lock semantics.
- [x] Typed semantic graph independent of YAML/RON/JSON5/custom physical encoding.
- [x] Deterministic source -> validation -> lowering -> client/server projection -> immutable bundle -> staging -> activation pipeline.
- [x] Distinct content/map/ruleset/world-policy/compiler/artifact revision concepts.
- [x] Explicit allowlisted client-safe projection and server-only data non-leakage rule.
- [x] Fail-closed loader with bounded allocation/decompression and no partial authoritative publication.
- [x] Explicit staging/activation/rollback and durable migration classes.
- [x] Legacy provenance plus `COPY`/`CONVERT`/`REWRITE`/`REFERENCE_ONLY`/`REJECT` dispositions.
- [x] Reference OTS evidence cannot independently establish Global behavior.
- [x] WebAssembly Component Model + project-owned versioned WIT capability ABI selected for target authoritative scripting boundary; Wasmtime is an implementation candidate rather than ABI owner.
- [x] Scripts are bounded proposal producers and never direct SQL/domain mutation owners.
- [x] Deterministic fuel, logical time, deterministic RNG, bounded host calls/collections/action plans, stable host-query ordering and deterministic floating/NaN policy.
- [x] Typed/versioned script extension state through domain/persistence APIs; VM memory is not durable state.
- [x] GAME-CHANNEL multiplicity/eligibility classification required for relevant value-producing content.
- [x] Hot reload defined as immutable revision staging/activation, never in-place mutation.
- [x] Mandatory future implementation evidence and physical-format spike gate.

## Repair history

### Repair cycle 1

Adversarial pre-freeze review found that fuel alone does not close deterministic execution: host query result ordering and observable floating-point/NaN behavior also require a contract. The contract now requires canonical/stable host-return ordering and either project-owned deterministic numeric semantics or explicitly proven deterministic floating behavior including NaN canonicalization where observable.

No second material repair has been consumed.

## Validation

### Focused

- source/ownership audit: `PASS`
- exact changed-file scope: expected three owned paths only
- architecture analysis/contract drafting: `PASS`
- adversarial pre-freeze self-review: `PASS AFTER REPAIR 1`
- runtime/component/integration/E2E: `NOT_APPLICABLE` — paper-only architecture candidate

### Owner-funded AI policy

- new Codex/OpenAI API/paid-review invocation: **NONE**
- specific owner permission for such invocation: **NOT GIVEN**
- independent review: **MANDATORY** because scripting sandbox/security and persistence-migration boundaries are material; if no genuinely independent non-owner-funded reviewer is available, the task must block at that gate rather than weakening it.

## Context checkpoint

```yaml
last_progress: DUR-04 analysis and contract are present in PR #212. Repair cycle 1 closed deterministic host-query ordering and floating/NaN behavior. Candidate scope remains exactly three owned paper-only paths.
status: validating
branch: agent/otv2-20260812-dur-04-content-world-scripting
head_sha: null
pr: 212
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: pending
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
owner_action_required: false
blocker: independent-review availability must be proven without owner-funded AI
next_action: Freeze exact head after final live-main/diff check, run exact-head self-review and standard CI, then satisfy the mandatory independent-review gate without owner-funded AI or stop BLOCKED with exact owner action.
```
