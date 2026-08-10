# OTV2-20260811-dual-transport-closeout-repair

```yaml
task_id: OTV2-20260811-dual-transport-closeout-repair
title: Close final dual-transport architecture review findings
mode: REPAIR
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-dual-transport-closeout-repair
pr: null
base_sha: 9794e9a6307b6f9db193ca2ce08607eb065b7d7e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture closeout coordinator
created_at: 2026-08-11T00:35:00+02:00
updated_at: 2026-08-11T00:35:00+02:00
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
  - exhausted successor PR 148 at c36e0eb1127c5689a23ea810c802766fe79d8050
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
- `OWNER_ACCEPTED`: transport/admission/security architecture already reviewed remains unchanged: one `protocol-oteryn`, TCP profile 1 architecture registration only, QUIC future opt-in target blocked on profile/FND-04/order/resource/fault/measured-benefit evidence, Gateway-only Game Login Ticket redemption, no cross-profile grant reuse, fail-closed fallback, no 0-RTT/DATAGRAM baseline.
- `OWNER_ACCEPTED`: Codex is not routine; this high-risk inherited package still requires exactly one final independent review after the repaired head is frozen.

## Acceptance criteria

- [x] Add a dedicated clarification making GameNode process/service topology not-yet-frozen and the modular-monolith shape a nonbinding preferred starting hypothesis with explicit future decision tests.
- [x] Add a dedicated clarification making `TCP_ONLY` and all gameplay transport client modes runtime-unavailable until their transport/client path is implemented and proven.
- [x] Add the two clarifications to the canonical architecture index with explicit supersession precedence.
- [ ] Archive/rotate exhausted PR #148 task without a fourth repair on that task.
- [ ] Close PR #148 unmerged and point it to this successor PR.
- [ ] Full trusted-base diff contains only declared documentation/task/contract paths and preserves reviewed invariants.
- [ ] Mandatory exact-head self-review passes with zero material findings.
- [ ] Exact-head Agent Governance, Dependency Review and CodeQL pass.
- [ ] One required independent final review passes on the unchanged head with zero material findings.
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
- The canonical architecture index now includes ADR-0015/0016 and states their narrow precedence.

## Validation

### Focused

- trusted full-diff base: `9794e9a6307b6f9db193ca2ce08607eb065b7d7e`
- inherited exact reviewed head: `c36e0eb1127c5689a23ea810c802766fe79d8050`
- successor focused review: pending after lifecycle rotation

### Component/integration

- result: `NOT_APPLICABLE` — documentation/contract repair only

### E2E

- result: `NOT_APPLICABLE` — no executable runtime behavior

### Exact-head CI

- final head: pending
- trigger source: pull_request
- result: pending

## Self-review

- exact head: pending
- material findings: pending
- verdict: pending

## Independent review

- required: `YES` — inherited package contains high-risk transport/admission/security architecture
- auditor: one genuinely independent final reviewer; Codex only for this required gate if no other independent reviewer is available
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #145 closed unmerged; PR #148 to be closed/rotated
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: ADR-0015 and ADR-0016 added on the final successor branch to repair the two remaining independent-review findings without changing runtime authority.
status: implementing
branch: docs/OTV2-20260811-dual-transport-closeout-repair
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: pre-pr
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
next_action: Archive the exhausted PR #148 task, open the successor PR, close #148 unmerged, then freeze and validate the full successor head.
```
