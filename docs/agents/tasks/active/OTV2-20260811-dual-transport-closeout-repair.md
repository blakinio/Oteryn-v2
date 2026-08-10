# OTV2-20260811-dual-transport-closeout-repair

```yaml
task_id: OTV2-20260811-dual-transport-closeout-repair
title: Close final dual-transport architecture review findings
mode: REPAIR
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-dual-transport-closeout-repair
pr: 149
base_sha: 9794e9a6307b6f9db193ca2ce08607eb065b7d7e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture closeout coordinator
created_at: 2026-08-11T00:35:00+02:00
updated_at: 2026-08-11T00:48:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - README.md
  - docs/agents/tasks/active/OTV2-20260807-protocol-contract-reconciliation.md
  - docs/agents/tasks/archive/OTV2-20260807-protocol-contract-reconciliation.md
  - docs/agents/tasks/active/OTV2-20260811-dual-transport-closeout-repair.md
  - docs/agents/tasks/archive/OTV2-20260810-architecture-review-dual-transport.md
  - docs/agents/tasks/archive/OTV2-20260810-dual-transport-final-repair.md
  - docs/architecture/ADR-0014-dual-gameplay-transport-tcp-default-quic-opt-in.md
  - docs/architecture/ADR-0015-gamenode-implementation-shape-not-yet-frozen.md
  - docs/architecture/ADR-0016-gameplay-transport-client-mode-runtime-readiness.md
  - docs/architecture/ARCHITECTURE_REVIEW_REFINEMENTS_2026-08-10.md
  - docs/architecture/ARCHITECTURE_STATUS_MODEL.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/README.md
  - docs/contracts/PROTOCOL_OTERYN_TRANSPORT_POLICY.json
public_contracts:
  - docs/architecture/ADR-0014-dual-gameplay-transport-tcp-default-quic-opt-in.md
  - docs/architecture/ADR-0015-gamenode-implementation-shape-not-yet-frozen.md
  - docs/architecture/ADR-0016-gameplay-transport-client-mode-runtime-readiness.md
  - docs/contracts/PROTOCOL_OTERYN_TRANSPORT_POLICY.json
depends_on:
  - closed unmerged PR 145 at 9bf162e9d78f41706e92253c41f36d745e33382e
  - closed unmerged PR 148 at c36e0eb1127c5689a23ea810c802766fe79d8050
  - merged governance PR 146
  - merged FND-ID lifecycle cleanup PR 147
blocks:
  - final merge of the owner-accepted architecture and dual-transport documentation programme
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
```

## Outcome

Deliver the complete architecture package inherited from exhausted PRs #145/#148 and repair only the two material findings from PR #148's final required independent review: prevent the 2026-08-10 GameNode modular-monolith recommendation from being misread as frozen topology, and make `TCP_ONLY` explicitly future/unavailable until gameplay transport implementation is proven.

## Architecture and source of truth

- `PROVEN`: trusted full-diff base for the inherited package is `main@9794e9a6307b6f9db193ca2ce08607eb065b7d7e`.
- `PROVEN`: PR #148 exact head `c36e0eb1127c5689a23ea810c802766fe79d8050` passed Agent Governance `31438343486`, Dependency Review `31438343473`, CodeQL `31438343467`, and self-review `4901430400`.
- `PROVEN`: independent review `4901458913` on that head found exactly two material remaining findings: GameNode topology wording lacked a decision gate, and ADR-0014 `TCP_ONLY remains available` contradicted current runtime-unavailable policy.
- `PROVEN`: PR #148 is closed unmerged and its task is archived after repair budget `3/3`; no fourth repair was applied to that task.
- `PROVEN`: initial PR #149 head `b080390b71cb6aa51404c02f28d52afb97a2f308` passed mandatory self-review `4901498075` and exact-head Agent Governance `31439274842`, Dependency Review `31439274845`, CodeQL `31439274868`.
- `PROVEN`: required independent review on that head found one bounded P2: `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` independently retained prescriptive modular-monolith wording outside ADR-0015's original supersession scope.
- `OWNER_ACCEPTED`: transport/admission/security architecture already reviewed remains unchanged: one `protocol-oteryn`, TCP profile 1 architecture registration only, QUIC future opt-in target blocked on profile/FND-04/order/resource/fault/measured-benefit evidence, Gateway-only Game Login Ticket redemption, no cross-profile grant reuse, fail-closed fallback, no 0-RTT/DATAGRAM baseline.
- `OWNER_ACCEPTED`: Codex is not routine; this high-risk inherited package requires one clean final independent review after the repaired head is frozen.

## Acceptance criteria

- [x] Add a dedicated clarification making GameNode process/service topology not-yet-frozen and the modular-monolith shape a nonbinding preferred starting hypothesis with explicit future decision tests.
- [x] Add a dedicated clarification making `TCP_ONLY` and all gameplay transport client modes runtime-unavailable until their transport/client path is implemented and proven.
- [x] Add the two clarifications to the canonical architecture index with explicit supersession precedence.
- [x] Archive/rotate exhausted PR #148 task without a fourth repair on that task.
- [x] Close PR #148 unmerged and point it to successor PR #149.
- [x] Extend ADR-0015's narrow supersession scope to include the exact prescriptive modular-monolith sentence in `FOUNDATION_PROGRAMME_CURRENT_STATUS.md`; the status overlay remains authoritative for status, but not for frozen GameNode topology.
- [ ] Full trusted-base diff contains only declared documentation/task/contract paths and preserves reviewed invariants.
- [ ] Mandatory repaired exact-head self-review passes with zero material findings.
- [ ] Repaired exact-head Agent Governance, Dependency Review and CodeQL pass.
- [ ] One clean required independent final review passes on the unchanged repaired head with zero material findings.
- [ ] Squash merge succeeds on the exact reviewed head.

## Excluded scope

- no runtime implementation or transport listener;
- no QUIC transport profile registration;
- no FND-04 grant implementation;
- no Platform repository write;
- no production/live activation;
- no unrelated architecture cleanup;
- no routine/redundant Codex review.

## Implementation / findings

- `ADR-0015` converts the GameNode modular-monolith wording from potentially binding topology authority into a preferred nonbinding implementation-discovery hypothesis and records the mandatory tests for any future topology freeze.
- `ADR-0016` aligns ADR prose with the machine-readable transport policy: profile registration is not runtime availability; `TCP_ONLY` is future mode vocabulary only until exact-revision implementation/proof exists.
- The canonical architecture index includes ADR-0015/0016 and states their narrow precedence.
- PR #148 lifecycle record is archived; PR #148 is closed unmerged and references PR #149.
- Repair cycle 1 on PR #149 extends ADR-0015 only far enough to cover the canonical status-overlay sentence that repeated the same modular-monolith recommendation; no runtime or topology is selected.

## Validation

### Focused

- trusted full-diff base: `9794e9a6307b6f9db193ca2ce08607eb065b7d7e`
- inherited exact reviewed head: `c36e0eb1127c5689a23ea810c802766fe79d8050`
- first PR #149 head `b080390b71cb6aa51404c02f28d52afb97a2f308`: self-review + three exact-head checks PASS; one independent-review P2 repaired
- repaired full changed-file review: pending frozen head

### Component/integration

- result: `NOT_APPLICABLE` — documentation/contract repair only

### E2E

- result: `NOT_APPLICABLE` — no executable runtime behavior

### Exact-head CI

- final head: pending after this checkpoint commit
- trigger source: pull_request/synchronize
- result: pending

## Self-review

- exact head: pending repaired head
- material findings: previous independent-review P2 repaired in cycle 1
- verdict: pending

## Independent review

- required: `YES` — inherited package contains high-risk transport/admission/security architecture
- auditor: one genuinely independent final reviewer; Codex only for this required gate if no other independent reviewer is available
- first PR #149 review: one P2 repaired
- final verdict: pending

## PR and closeout

- changed-file review: pending repaired head
- unresolved review threads: one repaired thread to resolve after new content is visible
- related/superseded PRs: PR #145 and PR #148 closed unmerged/rotated
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: PR #149 repair cycle 1 extends ADR-0015 supersession to the canonical status-overlay modular-monolith sentence; no runtime/topology semantics added.
status: validating
branch: docs/OTV2-20260811-dual-transport-closeout-repair
head_sha: null
pr: 149
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: pull_request
ci_check_generation: repair-1-head-pending
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
next_action: Freeze repaired PR #149 head, run exact-head self-review and CI, resolve the repaired thread, then request one clean final independent review; squash-merge unchanged head if clean.
```
