# OTV2-20260816-game-atlas-physical-profile-readiness

```yaml
task_id: OTV2-20260816-game-atlas-physical-profile-readiness
title: Benchmark Game -> Atlas physical profile readiness
mode: AUDIT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: research/game-atlas-physical-profile-readiness
issue: 291
pr: null
base_sha: 8722e565c6a0556934209820e3c14ee4f2dc6093
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: SENIOR OTERYN ECOSYSTEM ARCHITECT / MIGRATION COORDINATOR
created_at: 2026-08-16T11:05:23+02:00
updated_at: 2026-08-16T11:07:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-game-atlas-physical-profile-readiness.md
  - docs/agents/evidence/OTV2-20260816-game-atlas-physical-profile-readiness.md
  - docs/agents/evidence/OTV2-20260816-game-atlas-physical-profile-report.json
  - tools/game-atlas-profile-spike/**
  - .github/workflows/game-atlas-profile-spike.yml
public_contracts: []
depends_on:
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
  - docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
  - docs/architecture/DUR-04_CONTENT_WORLD_AND_SCRIPTING_CONTRACT.md
  - docs/contracts/RESOURCE_LIMITS_REGISTRY.json
  - docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md
  - issue:#291
blocks:
  - first executable Game -> Atlas physical profile contract
  - Game-owned Atlas exporter implementation
  - Atlas consumer implementation
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-PHYSICAL-READINESS
external_repositories: []
```

## Outcome

Produce a bounded, reproducible, proprietary-data-free evidence package that determines whether the first executable Game -> Atlas physical profile can now be authored without inventing canonical coordinate semantics. The spike is research evidence only: it does not itself make any encoding, chunk geometry, coordinate range, compression choice or resource limit canonical.

## Architecture and source of truth

- **PROVEN** — accepted `OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md` requires an explicit versioned `coordinate_profile` before executable producer/consumer compatibility and deliberately defers physical bytes, coordinate ceilings, chunk dimensions, compression and digest profile.
- **PROVEN** — ADR-0005 makes canonical World/Content independent from OTBM and leaves final technical chunk dimensions / vertical packing benchmark-sensitive.
- **PROVEN** — DUR-04 requires bounded physical-format evidence and says unknown physical details / numeric limits fail closed rather than becoming unlimited implementation defaults.
- **PROVEN** — `RESOURCE_LIMITS_REGISTRY.json` requires every externally controlled count, depth, length and byte size to have an absolute hard maximum before implementation acceptance.
- **PROVEN** — the current executable `crates/client-domain::Position` is explicitly a non-authoritative client projection using `i32/i32/i16`; it is evidence of a client-local representation, not canonical Game coordinate authority.
- **PROVEN** — the multichannel scope matrix makes the public map definition one immutable World revision shared by all channels; channel runtime overlays remain separate and are not Atlas static-source authority.
- **DERIVED** — a synthetic export-packaging spike can measure byte determinism, locality, chunking and edit-granularity trade-offs without requiring proprietary map assets.
- **UNKNOWN** — canonical coordinate numeric domain/bounds, canonical floor count/domain, final World schema implementation, production Atlas resource ceilings and public serializer remain unfrozen.
- **CONFLICT** — none identified; current sources consistently prohibit inferring the missing physical choices.

## Decision timing

1. **Must decide now?** `YES` for whether enough evidence exists to author the *next* bounded physical-profile contract; `NO` for selecting a permanent serializer or canonical coordinate range inside this spike.
2. **Concrete downstream work blocked:** first Game Atlas profile contract, exporter implementation, Atlas parser/validator and clean Atlas extraction around a proven artifact boundary.
3. **What becomes harder later:** choosing bytes/chunks from legacy OTBM/viewer conventions would couple Atlas to the wrong source model and create avoidable migration/compatibility cost.
4. **Supersession evidence:** canonical World schema implementation, representative-world measurements, browser/consumer performance evidence or security/resource-limit findings may supersede research recommendations.
5. **Deliberately not decided:** permanent encoding, compression, chunk geometry, coordinate ceilings, storage/CDN, delta protocol, final World Project/Bundle encoding and repository migration mechanics.

## Acceptance criteria

- [ ] Exact live coordinate/world/profile evidence is inventoried and truth-classified.
- [ ] Synthetic fixtures contain no proprietary OTBM/Crystal/Canary/Tibia bytes or assets.
- [ ] Research compares canonical JSON, canonical JSONL and a clearly non-public deterministic binary lower-bound baseline.
- [ ] Research compares `32x32` versus `64x64` grid packaging and per-floor versus packed-floor grouping.
- [ ] Every candidate proves deterministic bytes and semantic round-trip for identical synthetic inputs.
- [ ] Evidence records raw/compressed size, chunk/file count, random-point bytes, viewport bytes, floor-locality impact, local-edit changed-file/diff granularity, corruption/digest detection and observed compression ratio.
- [ ] Research decoder/generator uses explicit internal safety caps that are clearly **not** promoted to production resource limits.
- [ ] Machine-readable report and human evidence review are persisted and pinned to the exact run/head that produced them.
- [ ] Final readiness verdict is exactly `PROFILE_CONTRACT_READY` or `EVIDENCE_GAP`, with explicit justification and one next action.
- [ ] Full final diff self-review has zero open material findings.
- [ ] Required exact-head repository CI passes before merge.
- [ ] Runtime/component/browser E2E is classified truthfully.

## Excluded scope

- no permanent/public Game -> Atlas schema;
- no production exporter or Atlas consumer;
- no canonical coordinate numeric range/floor count;
- no production resource-limit registry additions from synthetic measurements alone;
- no final World Project/World Bundle encoding decision;
- no OTBM/Crystal/Canary migration or history extraction;
- no repository creation/rename/transfer;
- no Platform/Otheryn/otclient writes;
- no Synology, DNS, secret, deployment or production mutation;
- no third-party/proprietary asset use;
- no Codex/owner-funded AI.

## Implementation / findings

Issue #291 and dedicated branch claim the bounded research scope. Live preflight found no open Game Atlas physical-profile issue/PR/branch and no active task owning the declared paths. Open architecture PRs #270, #273 and #276 own disjoint analytics/client/AI paths.

The spike will use deterministic project-owned synthetic records and Python standard library only. `binary-baseline-v0` is intentionally a measurement lower-bound comparator, not a candidate public schema and not an implementation recommendation.

## Validation

### Focused

- command/run: pending `python tools/game-atlas-profile-spike/spike.py --self-test --output ... --summary`
- result: pending

### Component/integration

- command/run: dedicated GitHub Actions research workflow on exact spike head
- result: pending

### E2E

- scenario: `NOT_APPLICABLE` — research-only synthetic artifact measurement; no runtime exporter, Atlas browser or user journey changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: implementing/coordinating agent
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` provisionally
- reason: this task produces non-canonical synthetic research evidence and changes no public schema, parser trust boundary, runtime, durable state, security authority, governance, production behavior or repository authority; any later contract that freezes a physical profile is reviewed separately under its own risk classification
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: issue #291; no duplicate Game Atlas physical-profile PR found
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: issue #291 and dedicated branch created after live overlap/evidence preflight
status: implementing
branch: research/game-atlas-physical-profile-readiness
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: pre-implementation
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
next_action: implement the deterministic synthetic spike and dedicated validation workflow, then open a draft PR
```
