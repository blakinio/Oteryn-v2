# OTV2-20260806-vsl-02-rust-client-cutover-contract

```yaml
task_id: OTV2-20260806-vsl-02-rust-client-cutover-contract
title: Define exact Rust client migration and cutover contract
mode: CONTRACT
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/vsl-02-rust-client-cutover-contract
pr: 48
base_sha: 9034bd4bfa491eac6a898b29bc8151c94a4c2b89
head_sha: null
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-06T09:50:00+02:00
updated_at: 2026-08-06T10:25:00+02:00
execution_budget_minutes: 120
large_budget_reason: VSL-02 pins the exact source subtree, reconciles source PRs/tasks, defines path/provenance/dependency mapping, one atomic destination PR, source freeze/marker sequencing, validation and rollback across two repositories.
owned_paths:
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
  - docs/migration/VSL-02_SOURCE_RECONCILIATION.md
  - docs/migration/rust-client-path-map.json
  - docs/migration/rust-client-provenance-plan.json
  - docs/agents/tasks/active/OTV2-20260806-vsl-02-rust-client-cutover-contract.md
public_contracts:
  - docs/migration/VSL-02_RUST_CLIENT_MIGRATION_AND_CUTOVER_CONTRACT.md
  - docs/migration/VSL-02_SOURCE_RECONCILIATION.md
  - docs/migration/rust-client-path-map.json
  - docs/migration/rust-client-provenance-plan.json
depends_on:
  - FND-01 accepted at 3e11cf36ffdc1191fabd60c09e8da9818594e189
  - ADR-0002
  - ADR-0008
  - ADR-0011
blocks:
  - the one atomic destination Rust-client migration/workspace PR
  - FND-ID-01 until destination migration and source marker are terminal
  - FND-02
  - FND-03
  - FND-04
cross_repository_coordination_id: OTV2-RUST-CLIENT-CUTOVER-20260806
external_repositories:
  - blakinio/otclient (read-only source evidence; later marker PR requires a separate authorized task)
```

## Outcome

Deliver an implementation-ready VSL-02 contract that pins the exact Rust-client source commit and subtree, and defines the complete destination import, transformation, provenance, dependency, validation, rollout, freeze, source-marker and rollback procedure without moving code in this task.

## Architecture and source of truth

### PROVEN

- Destination `main` at task start is `9034bd4bfa491eac6a898b29bc8151c94a4c2b89`.
- FND-01 is accepted and archived; the 19-member workspace and source dispositions are canonical.
- Selected source commit is `c923ad8a1dff17b4933a6110931b0823cec2c590`.
- Selected source subtree tree is `c0928dafca6df19ff11d7901e503ed85a5199439`.
- Source manifest blob is `037013e8e4a762a65f0f2a30f7761ee14725a3fc`; lockfile blob is `2143408c12c50132883890f0821278320a331fde`.
- At reconciliation, source `main` equals the selected commit and no open PR changes `oteryn-client/**`.
- Source PRs #23, #48 and #97 are legacy/operational lanes outside the Rust subtree.
- Root source active records are stale/historical or Canary-reference work.
- A nested active source task proposed dual-protocol/native runtime work that conflicts with accepted destination ADRs.

### ACCEPTED BY THIS CANDIDATE

- Import always uses the pinned commit, not mutable source `main`.
- Future source `main` may advance outside the Rust subtree; cutover checks the subtree tree, not whole-repository equality.
- The nested native/dual-protocol task is `SUPERSEDED_REFERENCE_ONLY` and is archived with the Canary task by the later source-marker PR.
- All 26 source members have exact machine dispositions.
- One atomic destination PR creates exactly the accepted 19-member workspace.
- Tokio `1.51.4` is retained; reqwest `0.13.4` with explicit rustls/form/json/stream features replaces blocking `ureq`.
- Production and synthetic harness closures remain separate.
- Provenance is machine-readable and does not claim cross-repository Git ancestry.
- Rollout and rollback preserve exactly one writable canonical Rust client.

### DEFERRED

- Physical import and Cargo workspace creation belong to the atomic destination migration task.
- Source README/AGENTS/task lifecycle writes belong to the later separately authorized source-marker task.
- Public identifiers belong to FND-ID-01.
- Native protocol/transport belongs to FND-02.
- Game Session/admission belongs to FND-04.

## Acceptance criteria

- [x] Exact destination base, source commit and source subtree tree are verified.
- [x] Source drift, open PRs, root tasks and nested Rust task are reconciled.
- [x] Every source workspace member and relevant non-member path has one exact machine disposition.
- [x] Technical-login reference-only classification does not imply copied destination tests.
- [x] Provenance and history policy is machine-readable and truthful.
- [x] Exact dependency delta policy, including async HTTP/TLS selection, is fixed.
- [x] Atomic destination branch/PR contents, validation and equivalence evidence are fixed.
- [x] Source freeze and exact later marker paths/order are fixed.
- [x] Forward rollout and rollback prevent zero or dual canonical ownership.
- [ ] Final five-file diff and machine documents pass independent audit with zero material findings.
- [ ] Exact-head Agent governance, Dependency Review and CodeQL pass.
- [ ] PR #48 is marked ready and squash-merged.
- [ ] Task is archived and ownership released.

## Excluded scope

- No Rust source code or Cargo workspace is created.
- No write is made to `blakinio/otclient`.
- No source marker or freeze enforcement is implemented in source yet.
- No `protocol-oteryn`, server runtime, admission, persistence, content or Studio implementation.
- No production deployment or live Identity/Game Gateway operation.

## Implementation / findings

Delivered:

- exact source commit/tree reconciliation;
- classification of source PRs and both root/nested active task systems;
- complete 26-member path map and non-member exclusions;
- machine provenance, dependency, freeze, rollout and rollback plan;
- exact atomic 19-member implementation package;
- disposition-specific equivalence requirements;
- Windows, Linux, harness, security and provenance validation matrices;
- destination-first canonical ownership and exact source-marker scope.

Resolved audit findings:

1. **Whole-repository freeze was too broad.** Legacy PRs outside the Rust subtree may merge. The contract now pins import to the selected commit and compares the current `oteryn-client/` tree to `c0928daf...`.
2. **Nested active task was omitted.** `OTC2-20260805-native-protocol-single-version-completion` is now explicitly superseded and included in source-marker archival.
3. **Reference-only technical-login mapping implied a copy.** Its destination list is now empty; independently authored pre-native tests are recorded separately.
4. **Direct native-tls removal wording was overbroad.** Direct source Platform usage is removed, while every remaining transitive occurrence requires dependency-delta justification.

## Validation

### Focused

- command/run: exact source/destination revision checks; source tree inspection; open PR/task reconciliation; 26-member disposition audit; JSON structural review; complete five-file changed-path and contract consistency review
- result: pending final exact-head audit after this checkpoint

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture/migration-contract task only
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable migration occurs in this task
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending final checkpoint head
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending final checkpoint head
- method/auditor: adversarial source-to-target audit against FND-01, ADR-0002, ADR-0008, ADR-0011, exact source tree, nested task conflicts, provenance truthfulness, dependency/release closure and canonical rollback safety
- resolved material findings: whole-main freeze, omitted nested task, false reference-only destination mapping, overbroad native-tls wording
- open material findings: pending final full-diff review
- verdict: pending

## PR and closeout

- PR: #48, currently draft
- changed-file review: five declared task/migration files only at pre-final checkpoint
- unresolved review threads: pending final check
- related PRs: source #23/#48/#97 classified but not modified; destination #38 unrelated stale lifecycle cleanup
- merge commit/result: pending
- ownership release: pending archive PR

## Context checkpoint

```yaml
last_progress: Corrected the subtree freeze boundary, captured the nested conflicting native task and hardened reference-only/provenance/dependency semantics across all VSL-02 documents.
status: validating
branch: docs/vsl-02-rust-client-cutover-contract
head_sha_before_checkpoint: 1ef2cfbd6855d6e072ea1173abf1a47abba65a5a
pr: 48
ci_check_generation: pending final checkpoint commit
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Audit the final five-file diff and machine documents, then freeze the head for exact-head CI and merge if all gates pass.
```
