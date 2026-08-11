# OTV2-20260811-game-char-stage-b-evidence-delta-02

```yaml
task_id: OTV2-20260811-game-char-stage-b-evidence-delta-02
title: Reduce GAME-CHAR Stage B evidence blockers with primary-source delta
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-game-char-stage-b-evidence-delta-02
pr: null
base_sha: 1411994c70abbf065273c0502c88413b61ca5ca0
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T23:12:00+02:00
updated_at: 2026-08-11T23:12:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-game-char-stage-b-evidence-delta-02.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_DELTA_02.md
public_contracts: []
depends_on:
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_RECONCILIATION.md
  - docs/agents/ARCHITECTURE_DECISION_DISCIPLINE.md
blocks:
  - honest reduction of GAME-CHAR Stage-B UNKNOWN/CONFLICT evidence
  - eventual Stage-B owner decision package
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one nonbinding evidence delta against the accepted 2026-07-28 Reference target, using primary official evidence to strengthen or retain Stage-B classifications without rewriting the historical #183 dossier or accepting Stage B.

## Source of truth

- `PROVEN`: trusted base is `main@1411994c70abbf065273c0502c88413b61ca5ca0`.
- `PROVEN`: first Reference target is owner-accepted as Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance boundary.
- `PROVEN`: prior Stage-B reconciliation is `PRE-DECISION / NOT ACCEPTED` and identifies blockers B1-B8.
- `PROVEN`: overall `GAME-CHAR-01` remains `PROPOSED / PLANNED / NOT_STARTED`; final character-bearing DUR-02 schema waits for full GAME-CHAR acceptance.
- `PROVEN`: open PR #162 owns disjoint CI/repository-governance paths and is out of scope.

## Acceptance criteria

- [ ] Add a separate evidence delta; do not rewrite the historical #183 reconciliation.
- [ ] Re-evaluate B1 naming, B2 deletion/quota, B4 progression/formula timing, B5 promotion, B6 death edge cases, B7 offline training and B8 modern build-state ownership using primary evidence.
- [ ] Keep current-only documentation distinct from July-28 target proof unless continuity evidence exists.
- [ ] Record stronger classifications only when evidence supports them; preserve `UNKNOWN`/`CONFLICT` otherwise.
- [ ] Separate semantic ownership/schema blockers from formula/value implementation blockers using architecture decision timing discipline.
- [ ] Do not accept Stage B or overall GAME-CHAR.
- [ ] Do not update current status/register/horizon because no owner acceptance is created.
- [ ] Do not modify runtime, physical schema, protocol, content, Platform, Canary or external repositories.
- [ ] Perform full exact-head self-review and repository-required documentation CI before merge.

## Excluded scope

No owner acceptance, runtime/client/protocol/schema/content implementation, production changes, external-repository writes, or PR #162 mutation.

## Validation

### Focused

Reconcile each changed evidence classification against the accepted evidence hierarchy, target cut, Stage-A ownership boundary and prior Stage-B dossier.

### Component/integration/E2E

`NOT_APPLICABLE` — nonbinding paper-only evidence analysis only.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Context checkpoint

```yaml
last_progress: Current main and prior Stage-B dossier verified; new official primary evidence found for promotion, offline-training counter mechanics, name namespace history, death/PvP features, Wheel and Weapon Proficiency ownership.
status: implementing
branch: docs/OTV2-20260811-game-char-stage-b-evidence-delta-02
pr: null
final_head_sha: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Write the evidence delta with strengthened and retained Stage-B classifications, then validate it without accepting Stage B.
```
