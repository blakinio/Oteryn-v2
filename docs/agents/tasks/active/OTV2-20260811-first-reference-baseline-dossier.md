# OTV2-20260811-first-reference-baseline-dossier

```yaml
task_id: OTV2-20260811-first-reference-baseline-dossier
title: Prepare exact first Reference baseline owner decision dossier
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-first-reference-baseline-dossier
pr: null
base_sha: 3853127dfccf7df2421dfe0a6c63714f19e828ff
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T19:05:00+02:00
updated_at: 2026-08-11T19:05:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-first-reference-baseline-dossier.md
  - docs/architecture/GAME-VISION-01_FIRST_REFERENCE_BASELINE_DECISION_DOSSIER.md
public_contracts: []
depends_on:
  - docs/architecture/GAME-VISION-01_MINIMUM_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_PREDECISION_ANALYSIS.md
  - docs/architecture/GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
  - docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
  - docs/architecture/GAME-VISION-01_REFERENCE_PARITY_PRECEDENCE_OWNER_BASELINE.md
  - docs/architecture/ARCHITECTURE_STATUS_MODEL.md
blocks:
  - owner selection of exact first named Reference behavior baseline
  - GAME-CHAR-01 Reference-sensitive Stage B
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Prepare one nonbinding paper-only dossier that defines what an exact immutable Reference behavior baseline means, compares defensible dated Global Tibia production cuts, recommends one target, defines lawful/provenance-safe evidence classification, and stops before owner acceptance.

## Source of truth

- `PROVEN`: trusted base is `main@3853127dfccf7df2421dfe0a6c63714f19e828ff`.
- `PROVEN`: GAME-VISION requires the first external evaluation to be Reference-first, each released Reference revision to be immutable, and newer upstream behavior to be promoted only through a later explicit named revision.
- `PROVEN`: GAME-CHAR Stage A is owner-accepted, while Reference-sensitive Stage B is hard-blocked on the exact first named Reference baseline.
- `PROVEN`: Reference parity never authorizes copying proprietary code/protocol/assets, security defects or unsafe mutation behavior.
- `OBSERVED EXTERNAL`: official Tibia public news records the Summer Update 2026 on 2026-07-13, fixes on 2026-07-14 and 2026-07-21, a delayed notice that Echo Raids stopped spawning on Rookgaard with the 2026-07-16 server save, and further balancing/fixes with the 2026-07-28 server save.
- `UNKNOWN`: web search on 2026-08-11 did not establish a complete authoritative proof that no behavior-changing production change occurred after 2026-07-28; absence of search results is not evidence of absence.
- `PROVEN`: open PR #162 owns disjoint CI/repository-governance paths and is out of scope.

## Acceptance criteria

- [ ] Define the exact semantic meaning of a dated Reference behavior cut without depending on a proprietary server/client binary hash.
- [ ] Distinguish target-date selection from evidence completeness; UNKNOWN mechanics remain UNKNOWN rather than guessed.
- [ ] Compare at least 2026-07-13 post-Summer-Update, 2026-07-28 post-server-save and 2026-08-11/current-production-cut approaches plus continuously-latest tracking.
- [ ] Recommend one exact first Reference baseline and explain why it is safer/more reproducible than alternatives.
- [ ] Define primary/corroborative/reference-only evidence tiers and provenance/legal boundaries.
- [ ] Define immutable evidence-manifest, parity-classification and later-revision promotion rules.
- [ ] Map consequence to GAME-CHAR Stage B, DUR-02 discovery, GAME-ITEM/content/parity fixtures without implementing them.
- [ ] Do not select/accept the baseline on behalf of the owner.
- [ ] Do not modify current status/register/horizon until an owner decision exists.
- [ ] Do not modify runtime, schema, content, protocol, Platform, Canary or external repositories.
- [ ] Perform full exact-head self-review and repository-required documentation CI before merge.

## Excluded scope

This task does not:

- accept any Reference target;
- create a final Reference revision naming scheme;
- claim exhaustive knowledge of Global Tibia behavior;
- reverse engineer or copy proprietary code/protocol/assets;
- implement parity mechanics, fixtures, runtime, persistence schema or content;
- update GAME-CHAR Stage B as accepted;
- modify PR #162 or external repositories.

## Validation

### Focused

Reconcile the dossier against accepted GAME-VISION Reference-first/hybrid/parity-precedence semantics, GAME-CHAR Stage-A hard gate, architecture decision discipline and official public Tibia evidence chronology.

### Component/integration

`NOT_APPLICABLE` — nonbinding paper-only decision analysis.

### E2E

`NOT_APPLICABLE` — no executable/player-visible behavior changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` unless final diff changes accepted high-risk authority/security/protocol/durable-data/production semantics; intended scope is nonbinding analysis only.

## Context checkpoint

```yaml
last_progress: GAME-CHAR Stage-A owner baseline lifecycle closed; dedicated first-Reference-baseline dossier branch claimed from current main and external official evidence chronology researched.
status: implementing
branch: docs/OTV2-20260811-first-reference-baseline-dossier
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: null
ci_checks_for_current_head: 0
ci_run_ids: []
runner_assignment_state: unknown
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Write the nonbinding Reference baseline decision dossier and produce one explicit owner recommendation without accepting it.
```
