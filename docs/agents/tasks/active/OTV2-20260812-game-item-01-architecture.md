# OTV2-20260812-game-item-01-architecture

```yaml
task_id: OTV2-20260812-game-item-01-architecture
title: GAME-ITEM-01 item model and equipment architecture
mode: CONTRACT
status: blocked
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260812-game-item-01-architecture
pr: 205
base_sha: 93a49731ad91620748b87cdaba9525c9df70bc12
head_sha: f0d62331d71deedcb2b9a3b1fe0a1a32578200ed
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-12T11:37:00+02:00
updated_at: 2026-08-12T12:36:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-game-item-01-architecture.md
  - docs/architecture/GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_ANALYSIS.md
  - docs/architecture/GAME-ITEM-01_ITEM_MODEL_AND_EQUIPMENT_CONTRACT.md
public_contracts:
  - GAME-ITEM-01
depends_on:
  - GAME-VISION-01
  - DUR-01
  - DUR-02
  - ANL-01
  - ADR-0005
blocks:
  - DUR-03
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one bounded, paper-only `GAME-ITEM-01` architecture candidate that closes the native item-model and equipment semantic boundary needed by `DUR-03` once accepted and lifecycle-closed, while preserving the accepted first Reference target, stable content identity, durable ItemInstanceId semantics, common persistence/audit boundaries and fail-closed parity discipline.

The delivery PR itself remains a candidate. Canonical programme overlays are not promoted before the delivery is accepted and merged; a separate lifecycle-closeout delivery must promote them together afterwards. `DUR-03` must remain blocked until that lifecycle closeout is complete.

## Architecture and source of truth

- `PROVEN`: `GAME-VISION-01_FIRST_REFERENCE_BASELINE_OWNER_BASELINE.md` fixes the first Reference target to Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary and requires `UNKNOWN`/`CONFLICT` behavior to remain fail-closed.
- `PROVEN`: ADR-0005 makes stable namespaced Content Registry keys canonical and compact numeric item/content IDs revision-scoped runtime mappings only.
- `PROVEN`: `DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md` defines `ItemInstanceId` as a strongly typed UUIDv7 and leaves create/destroy/split/merge/transform identity-transition rules to `DUR-03`.
- `PROVEN`: `DUR-02_PERSISTENCE_V1_OWNER_BASELINE.md` keeps common transaction/audit substrate in DUR-02 while moving inventory/equipment/ground-item transfer semantics to GAME-ITEM-01 + DUR-03.
- `PROVEN`: `ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md` owns event/audit identity and durable evidence semantics; analytics never becomes gameplay authority.
- `PROVEN`: `AGENTS.override.md` permits task status only from `investigating`, `implementing`, `validating`, `ready`, `waiting`, `blocked`, `completed`.
- `PROVEN`: `docs/agents/ANTI_STALL_AND_EXECUTION_BUDGET.md` sets `max_repair_cycles_per_gate: 3` and requires `BLOCKED` or `ROTATE` after three repair cycles.
- `UNKNOWN`: exact Reference item limits, formula ordering and edge-case behavior not established by accepted evidence remain parity-pending and may not be invented in this task.

## Acceptance criteria

- [x] Freeze the candidate semantic boundary between immutable/versioned item definitions and concrete durable item instances without redefining `ItemInstanceId`.
- [x] Define typed bounded state capabilities for stack quantity, charges, durability, decay/expiration, binding/restrictions, upgrades/modifiers and container capability; prohibit a generic authoritative JSON/EAV escape hatch.
- [x] Define equipment legality using server-authoritative slot/occupancy claims, requirements and mutually-exclusive constraints without hard-coding client authority.
- [x] Define deterministic modifier/derived-stat ordering responsibility and its boundary with ruleset/SIM formula ownership.
- [x] Define bounded container graph legality, nesting/capacity/weight limits and cycle prevention while leaving atomic transfer/single-location conservation to DUR-03.
- [x] Define content-definition revision compatibility, explicit migration requirements and no-silent-reinterpretation rules.
- [x] Define world/account/character binding/restriction semantics and separate item-instance semantics from non-item currency/value ledgers.
- [x] Define boundaries with loot, trade, market, bank, depot, mail, rewards, houses, content/scripting, persistence and audit without capturing their transaction policy.
- [x] Preserve Reference evidence classes and mark exact unevidenced behavior `PARITY_PENDING_EVIDENCE` rather than guessing.
- [x] Keep maintained canonical overlays at live-main pre-acceptance state during delivery review; defer all `GAME-ITEM-01 -> ACCEPTED` and `DUR-03 -> unblocked/next` promotion to one post-merge lifecycle closeout.
- [ ] Correct the remaining independent-review lifecycle clause so `DUR-03` is unblocked only after both accepted merge **and** lifecycle closeout.
- [x] Use a repository-supported task status; current stop state is `blocked`.
- [ ] Obtain explicit owner authorization to extend this gate's repair budget beyond the repository default before making another material repair.
- [ ] After such authorization, run terminal exact-head self-review, independent review, exact-head CI, merge and lifecycle closeout.

## Excluded scope

- Rust/runtime/client implementation, SQL DDL, migrations, production deployment or live data changes.
- `DUR-03` conservation, single-authoritative-location, idempotent transfer, split/merge survivor/new-ID rules, transaction isolation proof or anti-duplication implementation.
- Exact Reference numeric values/formulas/limits without accepted evidence.
- Broad item/content import, serializer/container format selection or scripting runtime selection (`DUR-04`).
- Combat/ability formula semantics, market pricing/order-book policy, house/social/reward lifecycle policy, or automatic economy tuning.
- Reintroducing `protocol-canary`, proprietary protocol/code/assets or OTS implementation as production authority.

## Implementation / findings

Task opened from live `main@93a49731ad91620748b87cdaba9525c9df70bc12` after verifying no active GAME-ITEM task/branch/PR ownership overlap. `main` was repeatedly rechecked and remained at that commit through the last mergeability check.

The candidate selects typed capability composition over stable namespaced ItemType definitions, distinguishes authored static placements from durable ItemInstances, defines server-authoritative equipment occupancy and bounded container legality, and requires explicit item-definition compatibility/migration. It intentionally preserves all create/destroy/split/merge/transform identity transitions, atomic item location, idempotency, retry/crash recovery and item/currency/value conservation for `DUR-03`.

All exact Reference item behavior not established by accepted evidence remains parity-pending/fail-closed. Platform-owned entitlement facts are not activated or consumed merely by GAME-ITEM; the candidate now requires a separately accepted Oteryn-v2 entitlement consumer/enforcement contract. Architecture-only scope; runtime/DDL/production authority remains none.

## Validation

### Focused

- PR #205 changed-file inspection confirms only three delivery paths before this blocker checkpoint: active task, GAME-ITEM analysis and candidate contract; maintained programme/status/register/horizon/index files are exact live-main and outside the delivery diff.
- `aae66a2b215acd3720b4e8de3a032809c2438ca0` exact-head self-review `4915469709`: PASS before subsequent independent findings.
- independent Codex review on `aae66a2b215acd3720b4e8de3a032809c2438ca0`: review `4915504377`; findings P1 `3765563501` and P2 `3765563506` opened.
- `f0d62331d71deedcb2b9a3b1fe0a1a32578200ed` exact-head self-review `4915520214`: PASS for entitlement/candidate wording and all prior repaired boundaries, but the two earlier `aae66a2b...` findings remain applicable until repaired.

### Component/integration

- command/run: `NOT_APPLICABLE` — paper-only architecture package; no runtime component changed.
- result: `NOT_APPLICABLE`.

### E2E

- scenario: `NOT_APPLICABLE` — no executable user/runtime outcome is introduced.
- result: `NOT_APPLICABLE`.

### Exact-head CI

Last material content head before budget-stop checkpoint: `f0d62331d71deedcb2b9a3b1fe0a1a32578200ed`.

- Agent Governance `31587838775`: PASS.
- Dependency Review `31587838756`: PASS.
- CodeQL `31587838750`: PASS.
- CI success does **not** override unresolved independent-review findings or repair-budget exhaustion.
- This blocker checkpoint is not a merge candidate and its newly resulting branch SHA is not claimed as terminal validated evidence.

## Self-review

- last material content head: `f0d62331d71deedcb2b9a3b1fe0a1a32578200ed`.
- implementing-agent review: `4915520214`, PASS for the content then known to the coordinator.
- subsequent applicable independent findings prevent terminal PASS/merge.
- current task state: `blocked`.

## Independent review

- required: YES.
- `d38ec4efc5c504d4615269fd2346aef55970a112` review `4915420795` found valid premature acceptance/unblocking and CI-only churn findings; both were addressed/recorded.
- `aae66a2b215acd3720b4e8de3a032809c2438ca0` review `4915504377` found two additional material/process findings that remain applicable to `f0d62331...`:
  - P1 `3765563501`: contract section 19 says accepted merge alone unblocks `DUR-03`, but lifecycle policy requires **accepted merge + separate lifecycle closeout** before exposing the next gate. **UNRESOLVED; material contract repair required.**
  - P2 `3765563506`: task status `reviewing` is outside the mandatory task-status vocabulary. **STOP-STATE FIXED by this blocker checkpoint using valid status `blocked`; no claim that terminal review is complete.**
- fresh Codex review request `5265542928` was issued for `f0d62331...`; it is non-terminal for completion because the gate is now stopped on the already-applicable unresolved P1 and repair-budget exhaustion.

## PR and closeout

- PR #205 remains open, non-draft and mergeable at the last live check, but **must not be merged** with unresolved P1 or without repair-budget authorization.
- maintained programme/status/register/horizon/index files remain unmodified in the delivery PR.
- old review threads for premature overlay acceptance and CI-only head churn were resolved after their repairs; the newer lifecycle-unblock thread remains unresolved until a permitted material repair is made.
- no protected merge/auto-merge is configured or claimed.
- merge commit/result: none.
- ownership release: not allowed while blocked task remains active.

## Repair history

### Repair cycle 1 — transient status-overlay evidence typo

A historical DUR-01 closeout SHA was mistyped while editing `FOUNDATION_PROGRAMME_CURRENT_STATUS.md`. Self-review found and corrected it before terminal review. The status file was later restored to the exact live-main blob, so the delivery diff contains no status-overlay mutation.

### Repair cycle 2 — PR metadata governance and incorrect CI recovery action

Agent Governance run `31586112278` failed PR metadata preflight because the initial title exceeded 72 characters and the body lacked mandatory `## Summary` / `## Validation` headings. Metadata was corrected. A subsequent task-only commit was incorrectly created solely to trigger a fresh `synchronize` event; Codex correctly identified this as contrary to anti-stall/check-regeneration policy. The process error is retained in evidence and will not be repeated.

### Repair cycle 3 — premature architecture acceptance/unblocking overlays

Codex correctly identified that the delivery branch had promoted GAME-ITEM to `ACCEPTED` and DUR-03 to unblocked before PR #205 passed terminal review/CI and merged. All maintained overlays/index files were restored exactly to live-main, narrowing PR #205 to candidate task/analysis/contract only.

### Repair cycle 4 — entitlement consumer boundary self-audit

After cycle 3, a source audit found candidate wording that could imply an already accepted Oteryn-v2 entitlement consumer boundary although `PROD-ENTITLEMENTS-01` remains unaccepted for game consumption. Commit `f0d62331d71deedcb2b9a3b1fe0a1a32578200ed` corrected this and changed candidate wording from `accepts` to `defines` representation capability.

This fourth material repair exceeded the repository default `max_repair_cycles_per_gate: 3`. The coordinator therefore may not make the next material contract repair without explicit owner authorization. This overrun is recorded transparently rather than normalized away.

## Budget stop

`docs/agents/ANTI_STALL_AND_EXECUTION_BUDGET.md` is binding:

```text
max_repair_cycles_per_gate = 3
After three repair cycles for one gate
-> persist evidence
-> return BLOCKED or ROTATE
```

Observed count: `4` material repair cycles, one beyond the default before the stop condition was re-applied. No fifth repair is authorized.

## Context checkpoint

```yaml
last_progress: Verified repair-budget exhaustion after discovering two still-applicable Codex findings from exact head aae66a2b; preserved last material content head f0d62331 with green governance/dependency/CodeQL, left PR #205 unmerged and switched the task to a valid blocked stop state.
status: blocked
branch: agent/otv2-20260812-game-item-01-architecture
head_sha: f0d62331d71deedcb2b9a3b1fe0a1a32578200ed
pr: 205
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: PR #205
ci_check_generation: 31587838775 / 31587838756 / 31587838750 for last material head f0d62331
ci_checks_for_current_head: 3
ci_run_ids:
  - 31587838775
  - 31587838756
  - 31587838750
ci_job_ids: []
runner_assignment_state: terminal PASS on last material content head; blocker is review/budget, not CI
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 3
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 4
ci_recovery_actions_for_current_head: 0
stall_warnings: 1
owner_action_required: Explicitly authorize extending the GAME-ITEM-01 repair budget beyond max_repair_cycles_per_gate=3, sufficient for one additional material repair cycle that fixes the remaining lifecycle-unblock contract finding and then repeats exact-head self-review, independent review and CI.
blocker: Repository anti-stall policy repair budget exhausted; unresolved Codex P1 3765563501 requires a material contract change, and no fifth repair cycle is authorized.
next_action: After explicit owner repair-budget extension, change the contract so DUR-03 becomes unblocked only after accepted GAME-ITEM merge plus lifecycle closeout; re-freeze, exact-head self-review, independent Codex review, exact-head CI, merge #205 only if clean, then perform lifecycle closeout and continue to DUR-03.
```
