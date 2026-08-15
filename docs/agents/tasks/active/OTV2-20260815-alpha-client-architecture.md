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
head_sha: c3eeb3e736cb9459c658534c1c2eca0123e662bf
final_head_sha: null
final_head_frozen_at: null
owner: DOMAIN ARCHITECTURE DESIGN AGENT / worker E
created_at: 2026-08-15T00:19:00+02:00
updated_at: 2026-08-15T22:25:00+02:00
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
  - docs/architecture/ARCHITECTURE_ANALYSIS_GAP_REGISTER.md
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
blocks: []
cross_repository_coordination_id: null
external_repositories: []
```

`head_sha` is the immediately preceding repaired candidate revision. The exact final self-referential SHA is recorded externally on the PR/check/review evidence after this task commit exists.

## Outcome

Delivered the bounded `ALPHA-CLIENT-01` architecture package and completed the **third and final ordinary repair cycle for the stable gate**. Earlier repairs remain preserved, and this final bounded repair closes the two findings from the owner-authorized review of `b660a4e05c48bf6ac96d783573b81b3f227515ae`:

1. Tier 1 headless E2E now **must** exercise the same production transport, protocol schemas, production codecs, sequencing and admission contracts as the native client; the independent byte/adversarial/property/fuzz/cross-version evidence remains an additional oracle rather than a replacement codec path.
2. The normative candidate now defines a technology-neutral visual scene/presentation boundary for scene state, camera, animation, lighting, particles and effects, keeping all of it derived, reconstructable, revision-compatible, resource-bounded and non-authoritative.

Runtime/client/Platform implementation remains `NOT_STARTED`; no executable code, DDL or production state was modified.

PR: `#273`.

## Architecture and source of truth

- `PROVEN` — issue #263 and the parallel-work allocation assign worker E and exactly the three paths listed above.
- `PROVEN` — live canonical Agent-A result has merged on `main` and does not change ALPHA-CLIENT authority; this branch was reconciled with that main before the final repair.
- `PROVEN` — ADR-0003 requires Platform Identity -> one-time Game Login Ticket -> Platform-owned Game Gateway -> selected endpoint/channel/revisions + short-lived pre-admission material -> `protocol-oteryn` -> final game-owned FND-04 admission/CharacterLease/GameSession authority.
- `PROVEN` — ADR-0011/ADR-0016 preserve current fail-closed `pre-native-protocol` behavior and runtime-unavailable gameplay transports.
- `PROVEN` — current `crates/platform-client/src/lib.rs` recursively rejects only the 12 literal keys `host`, `port`, `endpoint`, `endpoint_uri`, `protocol`, `protocol_profile`, `ticket`, `credential`, `game_session`, `admission`, `route`, `address`; complete-schema/unknown-field rejection is not currently proven.
- `PROVEN` — FND-02 requires generation/sequence/revision/snapshot reconciliation and independent wire evidence against common-mode codec defects.
- `PROVEN` — ADR-0007 Tier 1 must speak the production transport and use the same production schemas, codecs, sequencing and admission contracts as the native client.
- `PROVEN` — `ARCHITECTURE_ANALYSIS_GAP_REGISTER.md` registers renderer/scene boundaries and camera/animation/lighting/particles/effects as part of `ALPHA-CLIENT-01`.
- `PROVEN` — DUR-04 client-safe content/revision discipline applies to visual and audio presentation assets.
- `UNKNOWN` — exact gameplay transport implementation APIs, scene graph/animation/lighting/particle technology, renderer/UI/audio libraries, updater/signing, installer, secure credential storage and numeric resource maxima remain deliberately unfrozen.

## Acceptance criteria

- [x] Screen/composition/provider, runtime/session, protocol/reconciliation, renderer/UI/input, content, filesystem/config, diagnostics, update/install, Windows-first and E2E boundaries remain defined.
- [x] Current `pre-native-protocol` behavior remains fail closed and no unavailable transport is exposed as runtime-ready.
- [x] ADR-0003 ticket/Gateway/pre-admission/final-game-authority chain remains explicit with no directory shortcut.
- [x] Independent FND-02 wire evidence remains required in addition to product-path E2E.
- [x] Tier 1 now explicitly exercises the supported **production transport and production schemas/codecs/sequencing/admission path**; test-only codecs cannot substitute for shipping-codec coverage.
- [x] Audio remains application-owned, client-safe/revision-compatible, bounded and presentation-only without a selected library/vendor.
- [x] Platform-directory current-state claim remains narrowed to the exact 12-key recursive denylist.
- [x] Visual scene/presentation ownership is explicit: scene/camera/animation/lighting/particles/effects derive from non-authoritative projection/content/presentation state, do not become a second world model, remain reconstructable and bounded, and cannot confer gameplay authority.
- [x] Scene/presentation implementation technology remains reversible; required evidence and decision timing are explicit.
- [x] `DECISIONS_NOT_TAKEN` continues to record deferred implementation choices.
- [x] Foreign-domain findings remain report-only; no runtime/client/server/protocol/DDL/Platform/production or coordinator-overlay path is intentionally modified.
- [x] Changed paths remain within worker-E ownership.
- [ ] Exact-final-head full-diff self-review and exact-head CI are recorded externally after this commit.
- [ ] Final independent review on the unchanged exact head is clean.

## Excluded scope

No executable client, scene, renderer, audio, networking, protocol, server or Platform implementation; no gameplay authority rewrite; no DDL/migration; no production activation; no credential/token representation; no concrete scene graph, camera, animation, lighting, particle/effects, audio, UI or renderer library selection; no coordinator-only global overlay edit; no lifecycle archive/ownership release before lawful merge.

## Implemented architecture repairs

### Earlier P1 — admission chain

Preserved explicit ADR-0003 fresh-entry chain through Game Login Ticket and Platform-owned Game Gateway before FND-02 transport and final game-owned FND-04 authority.

### Earlier P1 — independent wire oracle

Preserved canonical byte goldens, malformed/adversarial fixtures, properties, fuzzing, cross-version fixtures, resource ceilings and stable failure classes as independent evidence against common-mode production-codec defects.

### Earlier P2 — audio boundary

Preserved application-owned audio provider/device lifecycle, client-safe/revision-compatible assets, bounded resources, non-authoritative degradation, settings/accessibility and evidence ownership without choosing technology.

### Earlier P2 — Platform-directory precision

Preserved exact current 12-key denylist truth and future-only complete-schema/reject-unknown-field requirement.

### Current P1 — production codec path in Tier 1

Repaired. The candidate now states that Tier 1 must traverse the supported production gameplay transport and use the same production schemas, **production codecs**, sequencing and admission contracts as the native client. Independent wire evidence supplements rather than replaces that product code path.

### Current P2 — visual scene/presentation boundary

Repaired. The candidate now gives `apps/client` composition ownership of scene/presentation lifetime; camera/animation/lighting/particles/effects consume one-way non-authoritative projection/content/presentation inputs; renderer/scene caches cannot become a second authoritative world; revision replacement invalidates/rebuilds presentation state as required; visual failures degrade presentation only; resources must be bounded; concrete scene/render technology remains deferred; implementation/test evidence ownership is explicit.

## DECISIONS_NOT_TAKEN

No exact UI toolkit; scene graph/entity-presentation framework; camera algorithm; animation runtime; lighting model; particle/effects engine; shader architecture; renderer backend; audio library/vendor; promotion/replacement of synthetic client crates; prediction/rollback algorithm; gameplay transport implementation or QUIC activation; Gateway/admission/reconnect token/API shape; protocol/TLS/protobuf library; content bundle/patch/CDN format; installer/updater/signing provider; exact Windows paths; credential vault; crash backend/retention; release-channel/version-skew policy; Linux/macOS commitment; numeric scene/effect/audio/network/cache limits; server/gameplay/persistence/balance authority.

## CROSS_DOMAIN_FINDINGS

The companion analysis retains the existing report-only findings for protocol runtime, admission/session integration, content/release tooling, security/release/SRE, QA/E2E and diagnostics/privacy. The final candidate repairs do not grant authority to mutate those owners.

## Repair review findings

```yaml
review_finding:
  id: PR273-P1-ADMISSION-CHAIN
  repaired: true
  source: earlier owner-funded review
```

```yaml
review_finding:
  id: PR273-P1-INDEPENDENT-WIRE-ORACLE
  repaired: true
  source: earlier owner-funded review
```

```yaml
review_finding:
  id: PR273-P2-AUDIO-BOUNDARY
  repaired: true
  source: owner-funded review of d9786582e7f3a15c60a3796f2eb6189ed9d7b222
```

```yaml
review_finding:
  id: PR273-P2-PLATFORM-DIRECTORY-PRECISION
  repaired: true
  source: owner-funded review of d9786582e7f3a15c60a3796f2eb6189ed9d7b222
```

```yaml
review_finding:
  id: PR273-P1-TIER1-PRODUCTION-CODECS
  severity: P1
  repaired: true
  source: owner-funded review of b660a4e05c48bf6ac96d783573b81b3f227515ae
  repair: Tier 1 now must execute production transport plus the same production schemas/codecs/sequencing/admission contracts; independent oracle remains additional evidence
```

```yaml
review_finding:
  id: PR273-P2-VISUAL-SCENE-BOUNDARY
  severity: P2
  repaired: true
  source: owner-funded review of b660a4e05c48bf6ac96d783573b81b3f227515ae
  repair: added application-owned, non-authoritative, reconstructable, client-safe/revision-compatible and resource-bounded scene/camera/animation/lighting/particles/effects boundary with explicit evidence and decision timing
```

## Validation

### Focused

- final changed-file/full-diff review: pending exact-final-head inspection after this commit
- parent-source reconciliation: ADR-0007 and native-client gap register independently verified before repair

### Component/integration

- `NOT_APPLICABLE` — paper-only architecture repair; no executable component changed

### E2E

- `NOT_APPLICABLE` for this delivery — the contract defines future Tier 1/Tier 2/Tier 3 obligations but does not implement them

### Exact-head CI

- current final head: recorded externally on PR #273 after this commit exists
- required Agent governance / Merge authority / Merge gate: pending current exact head

## Self-review

- required: YES
- exact head: external PR evidence after this commit
- method: full changed-file, full-diff, authority/dependency, regression and stable-gate-budget review
- verdict: pending exact-final-head pass

## Independent review

- required: YES
- exact head: must be the unchanged final repair head
- method: owner-authorized Codex/OpenAI review or another genuinely independent reviewer
- prior review authorization: user has now granted continuing Codex review use; invocation still must target the exact current head
- verdict: pending

## PR and closeout

- PR #273 remains open and unmerged during repair validation.
- Prior review threads remain historical; current P1/P2 threads may be resolved only after exact-head repair proof.
- No archive or ownership release before merge.
- **Stable-gate repair budget:** `repair_cycles_for_current_gate: 3`. This is the third ordinary material repair cycle. Any further material repair after this generation is `BLOCKED` absent an explicit owner override of the gate-level repair stop.

## Context checkpoint

```yaml
last_progress: third/final ordinary ALPHA-CLIENT-01 repair applied for Tier-1 production-codec coverage and visual scene/presentation ownership after reconciling canonical main
status: validating
branch: docs/arch-e-alpha-client
head_sha: c3eeb3e736cb9459c658534c1c2eca0123e662bf
pr: 273
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: push/pull_request
ci_check_generation: final-repair-head-pending
ci_checks_for_current_head: 0
ci_run_ids: []
ci_job_ids: []
runner_assignment_state: unknown
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 3
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: EXACT_HEAD_FULL_DIFF_SELF_REVIEW_AND_CI_THEN_OWNER_AUTHORIZED_INDEPENDENT_REVIEW
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
`IMPLEMENTATION_AUTHORITY: NONE`