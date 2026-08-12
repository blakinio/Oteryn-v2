# OTV2-20260812-dur-04-content-world-scripting

```yaml
task_id: OTV2-20260812-dur-04-content-world-scripting
title: DUR-04 content world and scripting architecture
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-dur-04-content-world-scripting
pr: null
base_sha: c0b7b3b5928b194f8b51a4a51d9eb2d01e32ce44
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T23:21:00+02:00
updated_at: 2026-08-12T23:21:00+02:00
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
  - VSL-CONTENT-01 final content/bundle implementation contract
cross_repository_coordination_id: OTV2-NATIVE-WORLD-CONTENT
external_repositories:
  - blakinio/Otheryn
```

## Outcome

Produce one bounded paper-only `DUR-04 — Content, World Detail and Scripting Contract` candidate that completes the architecture left deliberately open by ADR-0005 without implementing the World Project, compiler, World Bundle, loader, Studio or scripting runtime.

The gate must freeze semantic source/package identity, deterministic compilation, immutable bundle/activation rules, safe loader behavior, content migration/provenance and a capability-bounded deterministic scripting host contract. It must preserve downstream gameplay/domain ownership and all accepted FND/DUR/ANL/GAME-CHANNEL invariants.

No Rust/runtime/client implementation, PostgreSQL DDL/migrations, Studio implementation, production configuration/deployment, Platform write or entitlement activation is authorized.

Maintained current-status/register/horizon/index/handoff files remain outside this delivery PR. They may be promoted only in a separate lifecycle closeout after an accepted delivery merge.

## Architecture/source facts

- `PROVEN`: post-GAME-CHANNEL `main@c0b7b3b5928b194f8b51a4a51d9eb2d01e32ce44` selects `DUR-04 = PROPOSED / PLANNED / NOT_STARTED` as the one next bounded paper-only architecture gate.
- `PROVEN`: no active DUR-04 task and no open DUR-04 PR existed at task start.
- `PROVEN`: ADR-0005 already accepts a project-owned native world/content model from zero, separate editable World Project/canonical model/runtime World Bundle, stable namespaced content keys, static authored state separate from dynamic authoritative state, semantic geography separate from technical chunks, bounded legacy conversion and one future integrated Oteryn Studio.
- `PROVEN`: ADR-0005 deliberately leaves exact physical encodings/chunk dimensions/compression details behind a bounded non-canonical format/compiler/loader spike; DUR-04 must not invent unsupported final numbers.
- `PROVEN`: GAME-ITEM rejects arbitrary authoritative JSON/EAV/free-form script state and gives DUR-04 ownership of concrete item source/bundle/compiler/scripting representation without allowing scripts to bypass item legality or DUR-03.
- `PROVEN`: DUR-03 owns item/currency/value conservation, idempotency, stale-authority rejection and durable transaction mechanics; scripts/content cannot become a second mutation path.
- `PROVEN`: GAME-CHANNEL requires every Channel-sensitive value-producing source/encounter family to have an explicit compiled/validated multiplicity class and separates simulation scope from durable eligibility scope.
- `PROVEN`: FND-03 requires bounded work, one logical authoritative writer and stale-result rejection; unbounded scripts cannot execute on the writer.
- `PROVEN`: current governance forbids Codex/owner-funded AI review or execution without explicit owner permission for that specific use. This task will not invoke such services.
- `UNKNOWN`: exact source serialization/file extension, final World Bundle container encoding, chunk/floor packing, compression codec, numeric resource ceilings and exact Wasmtime crate version are not accepted by current evidence and must not be guessed.

## Candidate decision goals

- [ ] Define stable `PackageKey`, immutable `PackageRevision`, stable namespaced content keys and exact dependency-lock semantics without replacing canonical semantic keys with compiled numeric IDs.
- [ ] Define authored source graph -> validation -> deterministic compilation -> immutable World Bundle -> bounded staging/loader -> explicit activation.
- [ ] Keep `content_revision`, `map_revision`, `ruleset_revision` and `world_policy_revision` distinct.
- [ ] Define deterministic compiler inputs/outputs, canonical ordering/path normalization, artifact identity and reproducibility rules while deferring physical encoding details requiring a spike.
- [ ] Define client-safe versus server-authoritative bundle views from one locked source graph without server-only data leakage.
- [ ] Define fail-closed loader validation, bounded decompression/allocation, corruption/version/dependency rejection and no partial authoritative publication.
- [ ] Define content revision staging, activation, rollback and persistence-migration interaction; never reinterpret persisted state silently under a changed definition.
- [ ] Define legacy source provenance, exact source revision/hash/license evidence, LIR conversion, deterministic reports and `COPY`/`CONVERT`/`REWRITE`/`REFERENCE_ONLY`/`REJECT` dispositions.
- [ ] Preserve the accepted Reference evidence rule: Otheryn/Canary/other OTS content is hypothesis/inventory/migration material, not proof of Global behavior.
- [ ] Select a capability-oriented scripting architecture with a project-owned stable host interface isolated from the concrete engine.
- [ ] Define scripts as bounded deterministic proposal producers over typed context, never direct owners of SQL, sockets, filesystem, process, environment, arbitrary wall clock/randomness or authoritative mutation.
- [ ] Define deterministic execution budgets, failure/trap behavior, memory/table/instance limits, explicit capabilities and fail-closed missing-resource-limit behavior.
- [ ] Define typed/versioned persistent script-owned extension state through host/domain schemas rather than opaque VM memory snapshots.
- [ ] Require GAME-CHANNEL multiplicity and event simulation/eligibility scope validation at compile time for relevant sources.
- [ ] Define migration/compatibility classes and safe hot-reload/activation semantics without in-place mutation of the currently active immutable revision.
- [ ] Define acceptance scenarios for deterministic builds, corrupt/oversized bundles, dependency/key conflicts, capability denial, infinite loops, invalid ActionPlans, migration-required activation and cross-channel revision consistency.
- [ ] Apply architecture-decision discipline: must-decide-now, blocked downstream work, future migration cost, superseding evidence and deliberate deferrals.
- [ ] Complete terminal exact-head self-review and exact-head Agent Governance / Dependency Review / CodeQL.
- [ ] Treat independent review as mandatory because DUR-04 includes scripting sandbox/security and persistence-migration boundaries. Do not invoke Codex/owner-funded AI. If no genuinely independent non-owner-funded reviewer is available, stop at the review gate with an exact owner action rather than weakening the gate.
- [ ] If delivery becomes merge-eligible, use a separate lifecycle closeout to promote maintained status/handoff and archive/release this task.

## Excluded scope

- implementation code, crates, Wasmtime dependency changes, WIT files, compiler/loader code or runtime activation;
- PostgreSQL schema/migrations;
- exact physical World Project/World Bundle encoding or chunk dimensions without the mandated bounded spike evidence;
- numeric CPU/fuel/memory/bundle/decompression/source-count limits without registry/evidence;
- final Studio UX/render/editor architecture beyond ADR-0005 boundary;
- exact gameplay/content formulas, NPC/quest/AI/business rules;
- production signing/PKI/CDN/release distribution;
- entitlement/commerce behavior.

## Validation

### Focused

- source/ownership audit: in progress
- architecture analysis/contract drafting: pending
- full-diff self-review: pending

### Component/integration/E2E

- `NOT_APPLICABLE` — paper-only architecture candidate; no executable behavior changes

### Owner-funded AI policy

- new Codex/OpenAI API/paid-review invocation: **FORBIDDEN WITHOUT SPECIFIC OWNER PERMISSION**
- current task behavior: **NONE INVOKED**
- independent review gate: must use non-owner-funded genuinely independent evidence or block/rotate

## Context checkpoint

```yaml
last_progress: Post-GAME-CHANNEL main verified; DUR-04 claimed as one dedicated paper-only architecture task with no overlapping task/PR owner. ADR-0005, historical migration task and Otheryn migration plan consumed as baseline evidence; current Wasmtime/Component Model primary-source evidence identified for a capability-oriented deterministic script-host decision.
status: investigating
branch: agent/otv2-20260812-dur-04-content-world-scripting
head_sha: null
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
owner_action_required: false
blocker: null
next_action: Draft the bounded DUR-04 analysis and candidate contract on the three owned paths, then perform adversarial pre-freeze review without invoking owner-funded AI.
```
