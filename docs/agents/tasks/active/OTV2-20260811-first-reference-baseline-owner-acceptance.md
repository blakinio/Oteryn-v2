# OTV2-20260811-first-reference-baseline-owner-acceptance

```yaml
task_id: OTV2-20260811-first-reference-baseline-owner-acceptance
title: Persist owner-accepted first Reference baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-first-reference-baseline-owner-acceptance
pr: null
base_sha: 3106590eee22227b81228d2930b5d90e2053c9e9
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T22:09:00+02:00
updated_at: 2026-08-11T22:09:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-first-reference-baseline-owner-acceptance.md
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
public_contracts:
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
depends_on:
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_DECISION_DOSSIER.md
  - docs/architecture/GAME-VISION-01_MINIMUM_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
  - docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
  - docs/architecture/GAME-VISION-01_REFERENCE_PARITY_PRECEDENCE_OWNER_BASELINE.md
blocks:
  - canonical recording of the owner-selected first Reference behavior cut
  - GAME-CHAR-01 Stage-B evidence reconciliation
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Persist the product owner's explicit acceptance of the complete recommended package in section 21 of `GAME-VISION-01_FIRST_REFERENCE_BASELINE_DECISION_DOSSIER.md`.

## Source of truth

- `PROVEN`: trusted base is `main@3106590eee22227b81228d2930b5d90e2053c9e9`.
- `USER_SOURCE`: on 2026-08-11 at 22:09 +02:00 the product owner explicitly answered `Tak` to the complete recommended first-Reference-baseline package.
- `PROVEN`: the accepted target is Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary, not a proprietary source/binary snapshot and not a continuously moving upstream target.
- `PROVEN`: target selection and evidence completeness remain separate; unknown mechanics remain `UNKNOWN` until evidenced.
- `PROVEN`: accepting the target unblocks evidence-backed GAME-CHAR Stage B but does not accept Stage B, a physical schema, runtime/content implementation or production rollout.
- `PROVEN`: open PR #162 owns disjoint CI/repository-governance paths and is out of scope.

## Acceptance criteria

- [ ] Add a canonical owner baseline accepting all ten package items from dossier section 21.
- [ ] Record the 2026-07-28 post-server-save behavior cut as immutable first Reference target semantics.
- [ ] Preserve evidence states `PROVEN`, `OBSERVED`, `DERIVED`, `UNKNOWN`, `CONFLICT`, `DECLARED_DIFFERENCE` and the accepted evidence-source hierarchy.
- [ ] Preserve the rule that patch-note/search absence is not evidence of no upstream change.
- [ ] Preserve lawful/provenance-safe native implementation and security/integrity/legal overrides.
- [ ] Update current status/register/horizon so the target is no longer shown as deferred/hard-blocking.
- [ ] Keep overall `GAME-CHAR-01` `PROPOSED / PLANNED / NOT_STARTED`; Stage B becomes unblocked but remains unaccepted.
- [ ] Keep final character-bearing DUR-02 schema blocked on accepted Stage B/full GAME-CHAR closure.
- [ ] Do not choose final Reference revision naming syntax, specific Stage-B mechanics/formulas or implementation.
- [ ] Do not modify PR #162 or external repositories.
- [ ] Perform full exact-head self-review and repository-required documentation CI before merge.

## Excluded scope

This task does not:

- accept GAME-CHAR Stage B or the complete GAME-CHAR gate;
- infer unknown July-28 mechanics from current Global behavior without continuity evidence;
- copy proprietary code/protocol/assets or promote Canary/OTS code to Global authority;
- create final Reference revision identifier syntax;
- create physical database schema, runtime/client/protocol/content implementation or production behavior;
- modify governance/CI or external repositories.

## Validation

### Focused

Reconcile the owner baseline against the delivered dossier, accepted GAME-VISION Reference-first/hybrid/parity-precedence baselines, GAME-CHAR Stage A and the architecture status model.

### Component/integration

`NOT_APPLICABLE` — paper-only product/architecture owner baseline.

### E2E

`NOT_APPLICABLE` — no executable/player-visible behavior changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` unless final diff unexpectedly changes executable high-risk security/protocol/persistence/production authority; intended scope is owner-approved paper-only product architecture.

## Context checkpoint

```yaml
last_progress: Owner accepted the full first-Reference-baseline recommendation; dedicated branch/task claimed from current main.
status: implementing
branch: docs/OTV2-20260811-first-reference-baseline-owner-acceptance
pr: null
final_head_sha: null
ci_check_generation: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Persist the canonical owner baseline and synchronize current status/register/horizon without accepting GAME-CHAR Stage B or implementation.
```
