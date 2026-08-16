# OTV2-20260816-game-atlas-physical-profile-readiness

```yaml
task_id: OTV2-20260816-game-atlas-physical-profile-readiness
title: Benchmark Game -> Atlas physical profile readiness
mode: AUDIT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: research/game-atlas-physical-profile-readiness
issue: 291
pr: 292
base_sha: 8722e565c6a0556934209820e3c14ee4f2dc6093
spike_evidence_head_sha: 700365199044c15ef22aaa9336d72dd103715a76
spike_run_id: 31938708639
spike_job_id: 95144635706
spike_report_sha256: c2ae672821f389ca4a13b72ce07c1b945e8bca550970148753582308ae4ec19d
final_head_sha: null
final_head_frozen_at: null
owner: SENIOR OTERYN ECOSYSTEM ARCHITECT / MIGRATION COORDINATOR
created_at: 2026-08-16T11:05:23+02:00
updated_at: 2026-08-16T11:22:00+02:00
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
  - canonical Oteryn-Game spatial/coordinate profile v1
  - first executable Game -> Atlas physical profile contract
  - Game-owned Atlas exporter implementation
  - Atlas consumer implementation
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1-PHYSICAL-READINESS
external_repositories: []
readiness_verdict: EVIDENCE_GAP
repair_cycles_for_current_gate: 1
```

## Outcome

Produce a bounded, reproducible, proprietary-data-free evidence package that determines whether the first executable Game -> Atlas physical profile can now be authored without inventing canonical coordinate semantics.

**Result: `EVIDENCE_GAP`.** The corrected synthetic physical-packaging spike is successful and narrows encoding/chunk/floor-layout and text-review trade-offs, but accepted Game -> Atlas semantics require coordinate/floor/order/anchor authority the current canonical Game implementation/contract set does not yet freeze at executable-profile precision.

Smallest missing owner evidence: one canonical Oteryn-Game spatial/coordinate profile v1 defining axes/orientation, numeric coordinate domain/bounds, floor identity/domain/order, point/bounds validity and inclusion, deterministic same-position stack/layer ordering, and presentation anchor/displacement semantics where canonical presentation references require them.

## Architecture and source of truth

- **PROVEN** — accepted `OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md` requires a versioned `coordinate_profile` before executable producer/consumer compatibility and deliberately defers physical bytes, coordinate ceilings, chunk dimensions, compression and digest profile.
- **PROVEN** — ADR-0005 makes canonical World/Content independent from OTBM and leaves final technical chunk dimensions / vertical packing benchmark-sensitive.
- **PROVEN** — DUR-04 requires bounded physical-format evidence and says unknown physical details / numeric limits fail closed rather than becoming unlimited implementation defaults.
- **PROVEN** — `RESOURCE_LIMITS_REGISTRY.json` requires externally controlled counts, depths, lengths and byte sizes to have absolute hard maxima before implementation acceptance.
- **PROVEN** — current executable `crates/client-domain::Position { x: i32, y: i32, floor: i16 }` belongs to a module explicitly documented as a protocol-neutral **non-authoritative client projection**; it is not canonical Game coordinate authority.
- **PROVEN** — entry `Cargo.toml` has no current `world-schema`, `world-project`, `world-bundle` or `world-spatial` implementation member; the repository map marks those names as planned target layout, not current proof.
- **PROVEN** — multichannel scope makes public map definition one immutable World revision shared across channels while channel runtime overlays remain channel-local state and are not Atlas static-source authority.
- **PROVEN** — corrected dedicated spike run `31938708639`, job `95144635706`, on exact head `700365199044c15ef22aaa9336d72dd103715a76` completed `SUCCESS`; generated full report SHA-256 is `c2ae672821f389ca4a13b72ce07c1b945e8bca550970148753582308ae4ec19d`.
- **DERIVED** — synthetic results strongly favor per-floor locality over packing unrelated floors, but do not select a permanent layout because real floor domain/workload remains unfrozen.
- **DERIVED** — `32x32` versus `64x64` is a real locality/file-count/aggregate-size trade-off; synthetic evidence does not identify one globally superior size.
- **DERIVED** — JSON and JSONL are essentially size-equivalent after gzip; corrected diff evidence shows JSONL has dramatically smaller review lines in this synthetic matrix, but reviewability alone does not select the distribution serializer.
- **DERIVED** — binary baseline is smaller, but synthetic size alone cannot justify a public binary schema/dependency; binary text-diff metrics are intentionally `null`.
- **UNKNOWN** — canonical coordinate numeric domain/bounds, floor count/domain, production Atlas resource ceilings, public serializer, compression/container and representative browser/cache workload.
- **CONFLICT** — none identified; current authorities consistently forbid promoting unknown physical choices by inference.

## Decision timing

1. **Must decide now?** `YES` for readiness verdict; `NO` for permanent serializer/chunk/coordinate decisions inside this task.
2. **Concrete downstream work blocked:** canonical coordinate profile, first Game Atlas physical-profile contract, exporter, Atlas parser/validator and clean extraction around that executable boundary.
3. **What becomes harder later:** adopting OTBM/client projection/viewer conventions as authority would create a second world truth and migration lock-in.
4. **Supersession evidence:** accepted canonical World spatial contract/implementation, representative-world measurements, browser/cache performance and security/resource-limit evidence.
5. **Deliberately not decided:** permanent encoding, compression, chunk geometry, coordinate ceilings, storage/CDN, delta protocol, final World Project/Bundle format and repository migration mechanics.

## Acceptance criteria

- [x] Exact live coordinate/world/profile evidence is inventoried and truth-classified.
- [x] Synthetic fixtures contain no proprietary OTBM/Crystal/Canary/Tibia bytes or assets.
- [x] Research compares canonical JSON, canonical JSONL and a clearly non-public deterministic binary lower-bound baseline.
- [x] Research compares `32x32` versus `64x64` grid packaging and per-floor versus packed-floor grouping.
- [x] Corrected run proves all 24 matrix cells deterministic and semantic-round-trip stable.
- [x] Evidence records raw/compressed size, chunk/file count, point/viewport bytes, floor-locality, local-edit changed-file and corrected text-review granularity, plus corruption/digest behavior.
- [x] Binary text-diff metrics are explicitly `null`; textual rows include maximum line byte length.
- [x] Research decoder/generator uses explicit internal safety caps that are clearly not promoted to production resource limits.
- [x] Machine-readable normalized report and human evidence review are persisted and pinned to exact corrected run/head evidence.
- [x] Final readiness verdict is `EVIDENCE_GAP`, with exact smallest missing owner evidence and one next action.
- [ ] Full final diff self-review has zero open material findings.
- [ ] Required exact-head repository CI passes before merge.
- [x] Runtime/component/browser E2E is `NOT_APPLICABLE` with concrete reason.

## Excluded scope

- no permanent/public Game -> Atlas schema or serializer;
- no production exporter or Atlas consumer;
- no canonical coordinate numeric range/floor count;
- no production resource-limit registry additions from synthetic measurements;
- no final World Project/World Bundle encoding decision;
- no OTBM/Crystal/Canary migration or history extraction;
- no repository creation/rename/transfer;
- no Platform/Otheryn/otclient writes;
- no Synology, DNS, secret, deployment or production mutation;
- no third-party/proprietary asset use;
- no Codex/owner-funded AI.

## Implementation / findings

Issue #291 and PR #292 own the bounded research scope. Live preflight found no duplicate Game Atlas physical-profile issue/PR/branch or overlapping active owned paths; concurrent #270/#273/#276 use disjoint analytics/client/AI paths.

The stdlib-only spike uses two deterministic `128 x 128 x 6` fixtures (`98,304` records each) and evaluates 24 combinations of three encodings, two chunk dimensions and two floor-packings. Corrected run `31938708639` proves every row passes byte determinism, semantic round-trip, raw-digest corruption detection, gzip corruption detection, one-data-chunk local edit and one-data-chunk point lookup.

Observed canonical-JSON examples remain unchanged after the measurement repair:

- `32x32/per-floor` sparse: `409,911` gzip bytes, point `4,264`, viewport `37,762`;
- `64x64/per-floor` sparse: `385,180` gzip bytes, point `16,273`, viewport `63,905`;
- `32x32/per-floor` dense: `536,246` gzip bytes, point `5,581`, viewport `49,696`;
- `64x64/per-floor` dense: `514,097` gzip bytes, point `21,760`, viewport `85,428`.

Thus `64x64` saves roughly 4-6% aggregate gzip but costs roughly 3.8-3.9x point bytes and 1.7x representative viewport bytes. Packing all six floors saves roughly 6-8% aggregate gzip at `32x32` but multiplies one-floor access bytes by about 5.6x. Compact JSON changed-line length ranges from `95,514` to `3,291,861` bytes while JSONL remains `160-198` bytes across the corrected matrix.

### Repair cycle 1

Initial successful run `31938342334` / job `95143702307` on `f35c28375abaa7339f3f74a4d19966c36393eee1` was superseded after self-review found two measurement defects: accidental UTF-8 interpretation of binary bytes and missing maximum-text-line evidence. Code/README were repaired, then the full 24-cell spike reran on `700365199044c15ef22aaa9336d72dd103715a76`; the corrected run is the only accepted spike evidence for this delivery.

Initial standalone Agent governance run `31938342362` also failed only PR metadata preflight because the first draft title used unsupported type `research`. The title was corrected to `test(atlas): benchmark physical profile readiness`; no repository validation step was reached in that failed generation and it is not successful final evidence.

## Validation

### Focused / synthetic spike

- exact corrected spike head: `700365199044c15ef22aaa9336d72dd103715a76`
- workflow run: `31938708639`
- job: `95144635706` (`Game Atlas Physical Profile Spike / validate`)
- Python: `3.12.13`
- compile: PASS
- self-test: PASS
- matrix: `24/24` PASS
- generated report SHA-256: `c2ae672821f389ca4a13b72ce07c1b945e8bca550970148753582308ae4ec19d`
- result: PASS

### Component/integration

The corrected dedicated workflow checked out and verified the exact spike head, executed the complete synthetic matrix and emitted the full machine-readable report to immutable workflow logs. Result: PASS.

### E2E

- scenario: `NOT_APPLICABLE` — research-only synthetic artifact measurement; no runtime exporter, Atlas browser or user journey changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final delivery head: pending final evidence/task composition
- trigger source: pull_request
- required context: `Merge gate / validate`
- result: pending final head

## Self-review

- exact head: pending freeze after final evidence/task composition
- method/reviewer: SENIOR OTERYN ECOSYSTEM ARCHITECT / MIGRATION COORDINATOR
- material findings: initial measurement defect repaired in cycle 1; final whole-diff review pending
- verdict: pending

## Independent review

- required: `NO`
- reason: this task creates non-canonical synthetic research evidence and changes no public schema, runtime parser trust boundary, durable state, security authority, governance safety gate, production behavior or repository authority; any later contract that freezes a physical profile must receive its own risk classification/review
- exact head: `NOT_APPLICABLE`
- method/auditor: `NOT_APPLICABLE`
- material findings: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- delivery PR: #292
- changed-file review: pending final exact-head review
- unresolved review threads: pending final query
- related/superseded PRs: issue #291; no duplicate physical-profile delivery found
- merge result: pending
- ownership release: separate post-merge lifecycle closeout required

## Context checkpoint

```yaml
last_progress: corrected 24-cell spike PASS and EVIDENCE_GAP evidence persisted
status: validating
branch: research/game-atlas-physical-profile-readiness
spike_evidence_head_sha: 700365199044c15ef22aaa9336d72dd103715a76
pr: 292
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: pending-final
ci_checks_for_current_head: 0
ci_run_ids:
  - 31938708639
ci_job_ids:
  - 95144635706
runner_assignment_state: completed-for-corrected-spike
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 1
ci_recovery_actions_for_current_head: 1
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: freeze final delivery head, perform whole-diff self-review, require exact-head Merge gate PASS, merge #292, then archive/release task in a separate closeout PR
```
