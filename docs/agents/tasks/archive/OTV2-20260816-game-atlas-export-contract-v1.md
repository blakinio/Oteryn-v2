# OTV2-20260816-game-atlas-export-contract-v1

```yaml
task_id: OTV2-20260816-game-atlas-export-contract-v1
title: Define Game -> Atlas immutable export v1 semantic contract
mode: CONTRACT
status: completed
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-atlas-export-contract-v1
closeout_branch: docs/game-atlas-export-contract-v1-closeout
issue: 286
pr: 287
closeout_pr: null
base_sha: afcbf8585ba23c506242978c38b2b51f9ea6f1b6
reconciled_main_sha: 005e31d7ddb137e77bc6825c248ec4b78e55b9cc
final_head_sha: 36075da1698df0be6e1c89edc2cce9e08f3e21e6
final_head_frozen_at: 2026-08-16T09:35:21+02:00
delivery_merge_sha: f19f543144693960c66e4ebff384d323ccdcbb56
owner: SENIOR OTERYN ECOSYSTEM ARCHITECT / MIGRATION COORDINATOR
owner_state: released_after_closeout
created_at: 2026-08-16T09:30:43+02:00
updated_at: 2026-08-16T09:40:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths: []
historical_owned_paths:
  - docs/agents/tasks/active/OTV2-20260816-game-atlas-export-contract-v1.md
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
public_contracts:
  - docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md
depends_on:
  - blakinio/Oteryn-Platform@b549e42041eda426bbf88db469862a92df930860:docs/architecture/adr/0041-ecosystem-repository-authority-contracts-and-atlas-integration.md
  - blakinio/Oteryn-v2@afcbf8585ba23c506242978c38b2b51f9ea6f1b6:docs/architecture/ADR-0005-native-world-format-and-oteryn-studio.md
  - blakinio/Otheryn@39cb2ce4ff427e7c3760eb6112b45efc0c1f73b8:docs/architecture/OTERYN_ATLAS_EXTRACTION_REVIEW_2026-08-15.md
blocks: []
cross_repository_coordination_id: OTERYN-GAME-ATLAS-V1
external_repositories:
  - blakinio/Oteryn-Platform (read-only authority/evidence)
  - blakinio/Otheryn (read-only migration evidence)
source_branch_disposition: auto_deleted_after_merge
source_branch_evidence: exact branch search after PR #287 merge returned no docs/game-atlas-export-contract-v1 ref
```

## Outcome

The first formal Game-owned semantic contract for the immutable public-safe dataset consumed by future `Oteryn-Atlas` is merged on protected `main` as `f19f543144693960c66e4ebff384d323ccdcbb56`.

The contract freezes only the semantic invariants required to unblock safe producer/consumer design and Atlas responsibility separation. It deliberately does not freeze serialization bytes, compression, physical chunk dimensions, object storage/CDN, Atlas implementation framework, delta encoding, repository transfers or production deployment.

## Architecture and source of truth

- **PROVEN** — Oteryn-Platform ADR 0041 is the temporary ecosystem authority used by this task and assigns Atlas export schema/public allowlist/deterministic exporter/producer validation/provenance ownership to Game while Atlas owns consumer validation, indexing, cache, rendering and publication.
- **PROVEN** — Oteryn-v2 ADR-0005 makes the canonical Oteryn World/Content model authoritative and keeps OTBM/legacy formats behind bounded importer boundaries.
- **PROVEN** — the merged Otheryn Atlas extraction audit is `EXTRACTABLE_WITH_REFACTOR` and identifies the formal versioned Game -> Atlas contract as a P0 prerequisite.
- **PROVEN** — delivery PR #287 merged the contract to protected `main` at `f19f543144693960c66e4ebff384d323ccdcbb56` after exact-head validation.
- **DERIVED** — downstream work may now design an exporter/consumer against this semantic boundary, but implementation compatibility remains unproven until the later physical/profile and executable evidence gates exist.
- **UNKNOWN / deliberately deferred** — exact byte encoding, compression, digest profile, chunk dimensions, storage/CDN, Atlas framework, retention period, delta format and asset redistribution permissions.
- **CONFLICT / MODEL LIMITATION** — `docs/contracts/CROSS_REPOSITORY_CONTRACT_LOCK.json` currently permits `LOCKED` records only when `schema_revision` and a 64-hex `schema_sha256` exist. This semantic v1 contract deliberately does not define a physical schema yet. No lock record was created because inventing a physical schema revision/hash would falsely claim an implementation-format decision. A later bounded task must either (a) add the first accepted physical Game -> Atlas schema/profile and then register its immutable digest, or (b) explicitly evolve the lock model to represent semantic-contract revisions separately from physical schema revisions.

## Acceptance criteria

- [x] Game-owned semantic v1 contract exists at `docs/contracts/OTERYN_GAME_ATLAS_EXPORT_CONTRACT_V1.md`.
- [x] Exact external authority/evidence revisions are pinned in the contract.
- [x] Producer/consumer ownership is explicit and Platform is not a transit owner of world data.
- [x] Full deterministic immutable snapshots, provenance, stable identity, coordinate/floor/order profile requirements, default-deny public projection, ambiguity handling, capability compatibility, validation/limits and rollback are specified.
- [x] OTBM, Legacy IR, canonical World Project wholesale, live GameNode state and undocumented Game DB tables are forbidden Atlas truth/fallback paths.
- [x] Physical serialization/compression/chunking/storage/delta/repository migration remain explicitly deferred.
- [x] Full exact-head diff self-review on `36075da1698df0be6e1c89edc2cce9e08f3e21e6` passed with zero material findings and zero unresolved review threads.
- [x] Required `Merge gate / validate` passed on the unchanged exact head.
- [x] Delivery PR #287 squash-merged as `f19f543144693960c66e4ebff384d323ccdcbb56`.
- [x] Issue #286 closed as completed after merge.
- [x] Delivery source branch was automatically deleted and verified absent.
- [x] Runtime/component/browser E2E is `NOT_APPLICABLE` because the delivery changes documentation/semantic contract only and implements no executable producer/consumer path.
- [ ] Lifecycle closeout PR merges and this active task path is absent from protected `main`.

## Excluded scope

- No Rust runtime/exporter or Atlas consumer implementation.
- No physical schema/serialization profile.
- No OTBM/Crystal/Canary code movement or rewrite.
- No `git filter-repo`, subtree extraction or history rewrite.
- No creation, rename or transfer of `Oteryn`, `Oteryn-Game`, `Oteryn-Platform` or `Oteryn-Atlas` repositories.
- No CI/GHCR/deployment namespace mutation.
- No mutation of Platform or Otheryn.
- No Synology, DNS, secret, protected-environment or production change.
- No third-party asset redistribution decision.
- No synthetic `schema_sha256` or fabricated lock entry.

## Delivery validation

### Exact-head CI

Final delivery head: `36075da1698df0be6e1c89edc2cce9e08f3e21e6`.

- Agent governance run `31934241122`: PASS.
- Merge authority audit run `31934241126`: PASS.
- Merge gate run `31934241117`: PASS.
- Required aggregate job `Merge gate / validate`, job `95133750537`: PASS.
- Rust Linux workspace / Windows client / Rust supply-chain / Rust policy jobs: correctly `SKIPPED` for the documentation-only diff selected by repository scope logic.

Result: PASS.

### Self-review

- exact head: `36075da1698df0be6e1c89edc2cce9e08f3e21e6`
- method/reviewer: whole-diff implementing/coordinating self-review recorded as PR review `4945689816`
- changed paths: exactly two declared delivery paths
- material findings: 0
- unresolved review threads: 0
- verdict: PASS

### Independent review

- required: NO
- reason: documentation-only formalization of already accepted ADR 0041/ADR-0005 ownership and migration invariants; no runtime protocol/wire behavior, authentication/session semantics, durable data, production behavior, repository authority or governance safety gate changed; unresolved physical choices remained explicitly deferred
- verdict: NOT_APPLICABLE

### Runtime/component/E2E

- result: `NOT_APPLICABLE`
- reason: no executable producer, consumer, browser/runtime, deployment or user-visible behavior was changed by PR #287

## PR and closeout

- issue: #286 — CLOSED / completed
- delivery PR: #287 — MERGED
- delivery exact head: `36075da1698df0be6e1c89edc2cce9e08f3e21e6`
- delivery merge: `f19f543144693960c66e4ebff384d323ccdcbb56`
- delivery changed-file review: PASS; exactly two declared paths
- unresolved review threads: 0
- delivery source branch: automatically deleted; verified absent by exact branch search
- closeout PR: pending creation
- closeout scope: remove active task path and preserve this terminal archive only
- cross-repository lock: intentionally unchanged; physical schema/profile evidence does not exist yet and the current lock model cannot truthfully lock this semantic-only contract without `schema_revision` + `schema_sha256`
- ownership release: effective when closeout PR merges

## Context checkpoint

```yaml
last_progress: delivery PR #287 merged as f19f543144693960c66e4ebff384d323ccdcbb56; issue closed; delivery source branch verified absent
status: completed
branch: docs/game-atlas-export-contract-v1
closeout_branch: docs/game-atlas-export-contract-v1-closeout
pr: 287
closeout_pr: null
final_head_sha: 36075da1698df0be6e1c89edc2cce9e08f3e21e6
delivery_merge_sha: f19f543144693960c66e4ebff384d323ccdcbb56
ci_trigger_source: pull_request
ci_check_generation: terminal-delivery
ci_checks_for_current_head: 3
ci_run_ids:
  - 31934241122
  - 31934241126
  - 31934241117
ci_job_ids:
  - 95133750537
runner_assignment_state: completed
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
ci_recovery_actions_for_current_head: 0
stall_warnings: 0
owner_action_required: null
blocker: null
next_action: merge lifecycle-only closeout after exact-head governance/merge-gate checks; then proceed to the next separately claimed migration-readiness task rather than changing the accepted contract or performing repository transfers
```

## Post-merge closeout

PR #287 is terminal merged; Issue #286 is closed; the delivery source branch is absent. This archive becomes authoritative lifecycle evidence only when the closeout PR merges and removes the active task path. The accepted semantic contract remains unchanged by closeout.