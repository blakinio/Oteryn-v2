# OTV2-20260811-game-char-stage-b-b1-b3-evidence

```yaml
task_id: OTV2-20260811-game-char-stage-b-b1-b3-evidence
title: Acquire GAME-CHAR Stage B naming deletion creation evidence
mode: COORDINATE
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-game-char-stage-b-b1-b3-evidence
pr: null
base_sha: 1411994c70abbf065273c0502c88413b61ca5ca0
head_sha: null
final_head_sha: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T23:05:00+02:00
updated_at: 2026-08-11T23:05:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-game-char-stage-b-b1-b3-evidence.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_B1_B3_EVIDENCE_ACQUISITION.md
public_contracts: []
depends_on:
  - docs/architecture/GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_RECONCILIATION.md
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
blocks:
  - target-quality naming normalization/recycling evidence
  - target-quality deletion/quota continuity evidence
  - target-quality creation/starter-state evidence
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Acquire and reconcile historical primary evidence for Stage-B blockers B1-B3 against the accepted 2026-07-28 Reference target. Prefer dated official Tibia/CipSoft pages, preserved official snapshots and official change chronology. Keep current-only rules `UNKNOWN` when July-28 continuity cannot be established.

## Acceptance criteria

- [ ] Search dated official primary sources for naming length/repertoire/restrictions, uniqueness, rename and deleted-name reuse.
- [ ] Search dated official primary sources for deletion grace period, active/deletion quota interactions, permanent deletion and undelete behavior.
- [ ] Search dated official primary sources for creation inputs and exact target-era starter-state/route semantics.
- [ ] Use historical archives/snapshots only when provenance is clear and record archive timestamp separately from page semantics.
- [ ] Reconcile current official manuals only as post-target evidence; do not silently project them backward.
- [ ] Identify which B1-B3 claims can be promoted from `UNKNOWN` and which remain blocked.
- [ ] Do not accept Stage B or update current status/register/horizon.
- [ ] Do not implement runtime/schema/content/protocol or write external repositories.
- [ ] Deliver nonbinding evidence report through PR/self-review/exact-head documentation CI and archive the task.

## Excluded scope

- B4-B8 formulas/promotion/death/offline/build ownership except when source chronology directly intersects B1-B3;
- physical Character schema/indexes;
- intentional Reference differences;
- Canary/crystalserver implementation as evidence authority;
- runtime or production changes.

## Context checkpoint

```yaml
last_progress: Prior Stage-B reconciliation is lifecycle-closed; B1-B3 evidence-acquisition branch claimed from main with no ownership conflict.
status: investigating
branch: docs/OTV2-20260811-game-char-stage-b-b1-b3-evidence
pr: null
owner_action_required: null
blocker: null
next_action: Search historical primary/archived evidence for naming, deletion/quota and creation/starter semantics around the 2026-07-28 target.
```
