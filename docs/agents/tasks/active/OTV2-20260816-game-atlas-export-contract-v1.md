# OTV2-20260816-game-atlas-export-contract-v1

```yaml
task_id: OTV2-20260816-game-atlas-export-contract-v1
title: Define Game -> Atlas immutable export v1 semantic contract
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-atlas-export-contract-v1
pr: null
issue: 286
base_sha: afcbf8585ba23c506242978c38b2b51f9ea6f1b6
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: SENIOR OTERYN ECOSYSTEM ARCHITECT / MIGRATION COORDINATOR
created_at: 2026-08-16T09:30:43+02:00
updated_at: 2026-08-16T09:30:43+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-game-atlas-export-contract-v1.md
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
public_contracts:
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
depends_on:
  - blakinio/Oteryn-Platform@b549e42041eda426bbf88db469862a92df930860:docs/architecture/adr/0041-ecosystem-repository-authority-contracts-and-atlas-integration.md
  - blakinio/Oteryn-v2@afcbf8585ba23c506242978c38b2b51f9ea6f1b6:docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
  - blakinio/Otheryn@39cb2ce4ff427e7c3760eb6112b45efc0c1f73b8:docs/architecture/OTERYN_ATLAS_EXTRACTION_REVIEW_2026-08-15.md
blocks:
  - Game-owned Atlas exporter implementation
  - Atlas consumer implementation against canonical Game data
  - clean responsibility split of mixed legacy Atlas modules
  - selective history-preserving Oteryn-Atlas extraction
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1
external_repositories:
  - blakinio/Oteryn-Platform (read-only authority/evidence in this task)
  - blakinio/Otheryn (read-only migration evidence in this task)
```

## Outcome

Create the first formal Game-owned semantic contract for the immutable public-safe dataset consumed by future `Oteryn-Atlas`. The contract freezes only decisions required to unblock safe producer/consumer design and Atlas responsibility separation; it deliberately does not freeze serialization bytes, compression, physical chunk dimensions, object storage, repository moves or runtime implementation.

## Architecture and source of truth

- **PROVEN** — Oteryn-Platform ADR 0041 is the current temporary ecosystem authority. It assigns Atlas export schema, public-field allowlist, deterministic exporter, producer validation/golden fixtures and provenance to Game; Atlas owns consumer validation, limits, indexing, cache, render and publication.
- **PROVEN** — ADR 0041 requires deterministic immutable full snapshots first; Atlas may not consume OTBM, the canonical World Project wholesale, undocumented Game database tables or live GameNode state.
- **PROVEN** — Oteryn-v2 ADR-0005 makes legacy formats bounded migration inputs and the canonical Oteryn World/Content model the source authority; stable namespaced content identity is distinct from legacy/runtime numeric IDs.
- **PROVEN** — the merged Otheryn Atlas extraction audit is `EXTRACTABLE_WITH_REFACTOR`, identifies current mixed Game/Atlas responsibilities, and calls a formal versioned Game -> Atlas contract a P0 prerequisite.
- **DERIVED** — enough architecture evidence exists to freeze semantic v1 requirements now because they are direct consequences of accepted ownership and are required before exporter/consumer/refactor work can proceed.
- **UNKNOWN / deliberately deferred** — exact encoding, compression, concrete chunk dimensions, physical manifest/chunk file layout, CDN/object storage, Atlas framework, delta encoding, retention period and exact Tibia-derived asset redistribution model.
- **CONFLICT** — none identified between current accepted Game architecture, Platform ADR 0041 and the merged Otheryn extraction audit for this semantic scope.

## Decision timing

1. **Must decide now? YES.**
2. **Concrete downstream work blocked:** Game Atlas exporter design, Atlas parser/consumer design, mixed legacy Atlas module separation, migration manifest finalization and selective Atlas history extraction.
3. **What becomes harder later:** implementing Atlas against OTBM/legacy structures or an undocumented ad-hoc export would create dual truth, consumer lock-in and history extraction into the wrong owner.
4. **Evidence that may justify supersession:** measured export/publication scale, proven consumer requirements, security/privacy findings, canonical World/Content changes, or measured need for deltas/alternate capabilities.
5. **Deliberately not decided:** all physical serialization/storage/deployment choices listed above and all repository create/rename/transfer operations.

## Acceptance criteria

- [ ] One Game-owned semantic v1 contract exists under `docs/contracts/` and cites the exact external authority/evidence revisions used.
- [ ] Producer/consumer ownership is explicit and does not make Platform a transit owner or Atlas a world authority.
- [ ] Full-snapshot determinism, immutable identity, provenance, stable identities, coordinate/floor/order semantics, public allowlist, ambiguity handling, compatibility, limits and rollback are specified.
- [ ] OTBM, Legacy IR, canonical World Project, live GameNode memory/state and undocumented Game DB tables are explicitly forbidden as Atlas contract inputs.
- [ ] Physical encoding/compression/chunk dimensions/storage/delta/repository migration remain explicitly deferred.
- [ ] Runtime/component/E2E is classified `NOT_APPLICABLE` because this task changes documentation/contract semantics only and performs no executable producer/consumer change.
- [ ] Full exact-head diff self-review is clean and `Merge gate / validate` passes on the unchanged final head before merge.
- [ ] Issue #286, task lifecycle and source branch are reconciled after merge.

## Excluded scope

- no runtime Rust implementation or workspace dependency change;
- no legacy OTBM/Crystal code movement or rewrite;
- no `git filter-repo`, subtree extraction or history rewrite;
- no creation, rename or transfer of `Oteryn`, `Oteryn-Game`, `Oteryn-Platform` or `Oteryn-Atlas` repositories;
- no CI/GHCR/deployment namespace mutation;
- no Platform/Otheryn source mutation;
- no Synology, DNS, production, authentication/session, protected environment or secret operation;
- no asset redistribution decision.

## Implementation / findings

Issue #286 claims this bounded contract package. Preflight found no existing open Atlas-export issue, no existing `game-atlas` branch and no active task record owning the two declared paths. Existing open architecture/runtime PRs use disjoint paths; legacy Otheryn PR #417 touches Atlas CI and remains outside this task.

The cross-repository contract lock is intentionally not edited in the delivery commit: its policy permits canonical revisions only after merge. If this contract merges, a bounded lifecycle closeout may add the immutable merged Game revision to `docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json` without changing contract semantics.

## Validation

### Focused

- command/run: pending — repository governance/contract validation selected by current workflows
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — documentation-only semantic contract; no executable producer or consumer exists in this task
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no runtime, browser, protocol, deployment or user-visible behavior changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pending
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Self-review

- exact head: pending
- method/reviewer: SENIOR OTERYN ECOSYSTEM ARCHITECT / MIGRATION COORDINATOR (implementing/coordinating agent)
- material findings: pending
- verdict: pending

## Independent review

- required: pending
- exact head: pending or `NOT_APPLICABLE`
- method/auditor: pending or `NOT_APPLICABLE`
- material findings: pending or `NOT_APPLICABLE`
- verdict: pending or `NOT_APPLICABLE`

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: issue #286; no duplicate Atlas-export PR found at task start
- protected auto-merge: pending
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: issue #286 created and bounded task claimed from main afcbf8585ba23c506242978c38b2b51f9ea6f1b6
status: implementing
branch: docs/game-atlas-export-contract-v1
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
owner_action_required: null
blocker: null
next_action: create the Game -> Atlas v1 semantic contract within the declared owned path
```
