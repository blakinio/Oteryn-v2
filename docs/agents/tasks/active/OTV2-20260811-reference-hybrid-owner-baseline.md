# OTV2-20260811-reference-hybrid-owner-baseline

```yaml
task_id: OTV2-20260811-reference-hybrid-owner-baseline
title: Persist GAME-VISION-01 hybrid Reference tracking owner baseline
mode: COORDINATE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260811-reference-hybrid-owner-baseline
pr: 158
base_sha: cd041f0da4e38ec87990a4924cb7a8a2b1f66f5e
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-11T09:57:00+02:00
updated_at: 2026-08-11T10:00:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260811-reference-hybrid-owner-baseline.md
  - docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
public_contracts:
  - docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md
depends_on:
  - GAME-VISION-01_REFERENCE_FIRST_OWNER_BASELINE.md
  - GAME-VISION-01_PREDECISION_ANALYSIS.md
  - ADR-0010-reference-and-evolved-world-product-profiles.md
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
```

## Outcome

Persist the owner's explicit acceptance that Reference uses a **hybrid upstream-tracking model**: Global Tibia is observed continuously, while every released Oteryn Reference revision remains immutable and changes reach a later Reference revision only through an explicit controlled promotion/release decision.

## Source of truth

- `USER_SOURCE`: on 2026-08-11, after the three tracking models were explained, the owner selected: `no to hybryda`.
- `PROVEN`: the existing Reference-first owner baseline already requires the evaluated Reference build to identify an immutable named Reference baseline/revision.
- `DERIVED`: accepting hybrid tracking resolves the long-term Reference tracking-policy question, but does not select a concrete Global Tibia patch/date, update cadence, migration mechanics, release naming, inclusion policy for every upstream change, or any other remaining GAME-VISION decision.

## Acceptance criteria

- [x] Record continuous upstream observation/evidence intake.
- [x] Record immutable released Reference revisions; no live mutation of released rules merely because Global changes.
- [x] Require explicit promotion into a later Reference revision before upstream changes become Reference product semantics.
- [x] Preserve reproducibility of tests, bug reports and parity evidence against the named revision.
- [x] Leave exact cadence, concrete Global baseline, migration/rollback mechanics and revision naming unresolved.
- [x] Keep full `GAME-VISION-01` explicitly `NOT ACCEPTED`.
- [x] Include decision-timing, downstream-consumer, cost-of-delay and supersession-evidence records.
- [x] No runtime/client/server/content/production implementation is authorized.
- [ ] Exact-head self-review and repository-required CI pass before merge.

## Implementation / findings

- Added `docs/architecture/GAME-VISION-01_REFERENCE_HYBRID_TRACKING_OWNER_BASELINE.md` as a separate owner-accepted partial baseline so the earlier Reference-first decision retains a narrow historical scope.
- The accepted model is continuous upstream evidence intake plus immutable released Reference revisions.
- A Global Tibia change never gains Reference product authority merely because it is newer; promotion into a later Reference revision is explicit.
- Historical tests, parity matrices and bug reports remain tied to the named Reference revision they evaluated.
- Concrete baseline version/date, release cadence, revision naming, migration/rollback mechanics, support lifetime and per-change promotion policy remain unresolved.
- Full `GAME-VISION-01` remains `NOT ACCEPTED` and no executable implementation is authorized.

## Validation

### Focused

- base: `main@cd041f0da4e38ec87990a4924cb7a8a2b1f66f5e`
- open PRs at task start: 0
- PR: #158
- pre-PR compare: `behind_by=0`; exactly two declared documentation paths
- source classification: current-session `USER_SOURCE`
- authority boundary: hybrid Reference tracking only; remaining GAME-VISION decisions explicitly unresolved

### Component/integration

- result: `NOT_APPLICABLE` — architecture documentation only

### E2E

- result: `NOT_APPLICABLE` — no executable behavior

### Exact-head CI

- final head: pending this metadata checkpoint commit
- result: pending

## Self-review

- exact head: pending this metadata checkpoint commit
- method/reviewer: implementing/coordinating agent full-diff product/architecture review
- material findings: pending
- verdict: pending

## Independent review

- required: `NO` under current risk policy — this changes product release/tracking semantics only and changes no authentication/session, protocol/wire, persistence/economy conservation, security, production or multichannel authority semantics.
- exact head: `NOT_APPLICABLE`
- verdict: `NOT_APPLICABLE`

## PR and closeout

- PR: #158
- changed-file review: pending exact final head
- unresolved review threads: pending
- merge: pending
- lifecycle archive: pending after merge

## Context checkpoint

```yaml
last_progress: Persisted the owner-accepted hybrid Reference tracking baseline and opened PR #158 without accepting any other GAME-VISION decisions.
status: validating
branch: docs/OTV2-20260811-reference-hybrid-owner-baseline
pr: 158
final_head_sha: null
ci_trigger_source: pull_request/synchronize
owner_action_required: null
blocker: null
next_action: Freeze the exact final head, perform mandatory full-diff self-review, verify repository-required CI, resolve any material review findings, and squash-merge only if unchanged and clean.
```
