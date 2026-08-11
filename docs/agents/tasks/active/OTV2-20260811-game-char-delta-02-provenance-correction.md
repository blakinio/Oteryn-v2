# OTV2-20260811-game-char-delta-02-provenance-correction

```yaml
task_id: OTV2-20260811-game-char-delta-02-provenance-correction
title: Correct merged GAME-CHAR delta-02 promotion source date
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-game-char-delta-02-provenance-correction
pr: null
base_sha: 4dce1e4da5c7c9e442abe99975aac3e7913b46b4
head_sha: null
final_head_sha: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T23:59:00+02:00
updated_at: 2026-08-11T23:59:00+02:00
execution_budget_minutes: 30
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-game-char-delta-02-provenance-correction.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_DELTA_02.md
  - docs/agents/tasks/archive/OTV2-20260811-game-char-stage-b-evidence-delta-02.md
public_contracts: []
depends_on:
  - docs/architecture/GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_DELTA_02.md
  - docs/agents/tasks/archive/OTV2-20260811-game-char-stage-b-evidence-delta-02.md
blocks:
  - factual provenance integrity of the canonical merged B4-B8 evidence report
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Correct one factual provenance error that survived delivery/closeout of the nonbinding B4-B8 evidence delta and preserve a durable erratum trail without reopening or changing its substantive Stage-B evidence classifications.

## Source of truth

- `PROVEN`: current trusted base is `main@4dce1e4da5c7c9e442abe99975aac3e7913b46b4`, after #187 delivery and #188 lifecycle closeout.
- `PROVEN`: canonical report E1 says `Official 2001 release material` for `https://www.tibia.com/news/?id=122&subtopic=newsarchive`.
- `PROVEN`: the official Tibia source is `The Update is here!`, dated **February 18, 2002**.
- `PROVEN`: the source still supports the substantive core promotion claim: Premium players at/above level 20 can receive promotion.
- `PROVEN`: exact 20,000 gp July-28 continuity and exact Premium-lapse semantics remain `UNKNOWN`; this correction does not alter those classifications.
- `PROVEN`: initial repair PR #189 was closed without merge because parallel #188 had already archived the original task; merging #189 from the stale base risked reintroducing an active task record.
- `PROVEN`: PR #162 remains disjoint CI/repository-governance work and is out of scope.

## Acceptance criteria

- [ ] Correct only the E1 factual year `2001 -> 2002` in the canonical evidence report.
- [ ] Preserve every substantive B4-B8 classification/recommendation unchanged.
- [ ] Add an auditable post-closeout erratum note to the archived original task referencing the correction lifecycle.
- [ ] Do not re-create or mutate the archived original task as active.
- [ ] Do not change GAME-CHAR status, current status/register/horizon, runtime/schema/content/protocol/Platform/production semantics.
- [ ] Keep external repositories and PR #162 untouched.
- [ ] Perform full exact-head self-review and fresh documentation CI before merge.
- [ ] Archive this correction task after terminal completion.

## Excluded scope

This task does not re-review or accept the B4-B8 evidence package, change promotion semantics, alter Stage B, update owner decisions, implement code/schema/content, or resolve unrelated evidence gaps.

## Validation

### Focused

Verify the report diff is the exact source-year correction and the original archive receives only an erratum/audit note.

### Component/integration/runtime E2E

`NOT_APPLICABLE` — factual paper-only provenance correction.

### Exact-head CI

Pending.

## Self-review

Pending.

## Context checkpoint

```yaml
last_progress: Fresh correction task created from post-#188 main after stale-base repair PR #189 was safely closed without merge.
status: implementing
branch: docs/OTV2-20260811-game-char-delta-02-provenance-correction
pr: null
owner_action_required: null
blocker: null
next_action: Correct the canonical report source year, annotate the original archive with the erratum, open PR and validate exact head.
```
