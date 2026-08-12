# OTV2-20260812-dur-02-character-persistence-owner-baseline

```yaml
task_id: OTV2-20260812-dur-02-character-persistence-owner-baseline
title: Persist owner-accepted DUR-02 Character persistence partial baseline
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260812-dur-02-character-persistence-owner-baseline
pr: null
base_sha: c98f463b26f22df99dd10ef3819086a59c25250b
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-12T08:25:00+02:00
updated_at: 2026-08-12T08:25:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-dur-02-character-persistence-owner-baseline.md
  - docs/architecture/DUR-02_PROFILE_NEUTRAL_CHARACTER_PERSISTENCE_OWNER_BASELINE.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md
public_contracts: []
depends_on:
  - docs/architecture/DUR-02_PROFILE_NEUTRAL_CHARACTER_SCHEMA_DECISION_PACKET.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_OWNER_BASELINE.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/FND-04A_AUTHORITY_FRESH_ADMISSION_CONTRACT.md
  - docs/architecture/FND-04B_RECONNECT_RECOVERY_CONTINUITY_CONTRACT.md
  - docs/architecture/ADR-0004-postgresql-and-data-ownership.md
  - docs/architecture/ADR-0012-character-authority-and-platform-lifecycle-boundary.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/ARCHITECTURE_STATUS_MODEL.md
blocks:
  - later full DUR-02 Persistence-v1 reconciliation
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Persist the owner's explicit acceptance of all seventeen recommendations in section 18 of `DUR-02_PROFILE_NEUTRAL_CHARACTER_SCHEMA_DECISION_PACKET.md` as a binding **partial owner baseline** for the profile-neutral Character persistence sub-scope of stable gate `DUR-02 — Persistence v1`.

The delivery must keep the overall stable `DUR-02` gate `PROPOSED / PLANNED / NOT_STARTED`, preserve runtime/DDL authority as `NONE`, and synchronize current coordination documents without rewriting the historical pre-decision packet.

## Architecture and source of truth

- `USER_SOURCE`: on 2026-08-12 at 08:25 +02:00, after the seventeen-point package was explained as the technical/safety architecture for Character persistence, the owner instructed `wykonaj`. This task treats that as explicit acceptance of the complete seventeen-rule recommendation previously presented for owner decision.
- `PROVEN`: trusted base is `main@c98f463b26f22df99dd10ef3819086a59c25250b`.
- `PROVEN`: `DUR-02_PROFILE_NEUTRAL_CHARACTER_SCHEMA_DECISION_PACKET.md` is lifecycle-closed, nonbinding pre-decision evidence delivered by PR #195 / merge `ca0a7373104cf9908e347dcc9890f46893098928` and archived by PR #196 / merge `c98f463b26f22df99dd10ef3819086a59c25250b`.
- `PROVEN`: that packet explicitly states the stable historical `DUR-02 — Persistence v1` scope is broader than the Character persistence package; future acceptance must therefore be partial and cannot set overall `DUR-02` to `ACCEPTED`.
- `PROVEN`: `GAME-CHAR-01` is `ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED` and supplies the semantic Character inputs to this persistence sub-scope.
- `PROVEN`: open PR #191 is a disjoint factual evidence-provenance correction; open PR #162 is disjoint CI/governance work; neither is owned or modified here.
- `PROVEN`: current active tasks on trusted base do not own the five paths declared by this task; the foundation programme checkpoint is non-owning.

## Acceptance criteria

- [ ] Add a dedicated `OWNER_ACCEPTED PARTIAL BASELINE` document binding all seventeen recommendations and the detailed sections they summarize.
- [ ] Preserve one Character root/revision anchor and a global CharacterRevision independent from FND-04 authority generations.
- [ ] Preserve account portfolio guards, global canonical-name registry, typed child/profile extensions and the ban on generic JSON/KV/EAV miscellaneous state.
- [ ] Preserve FND-04 separation and atomic fresh-admission / reconnect-recovery PREPARE-COMMIT / post-grace recovery semantics.
- [ ] Preserve OperationId receipts, conditional GameSession-scoped durable CommandId dedup, explicit lock/isolation proof and no advisory-lock sole authority.
- [ ] Preserve mandatory audit/publication atomicity, normalized current-state authority, no success before commit, staged migration and no authority resurrection after PITR/restore.
- [ ] Preserve profile-neutral scope only; unresolved Reference/profile/operational values remain owned by later gates.
- [ ] Overall stable `DUR-02` remains `PROPOSED / PLANNED / NOT_STARTED` after lifecycle closeout; only the named Character persistence sub-scope is owner-accepted.
- [ ] No PostgreSQL DDL/migrations, runtime persistence, Rust DB-library choice, profile-specific PvP schema, item/currency/DUR-03 implementation, Platform write or production action is authorized.
- [ ] Synchronize `FOUNDATION_PROGRAMME_CURRENT_STATUS.md`, `GLOBAL_ARCHITECTURE_DECISION_REGISTER.md` and `GAMEPLAY_AND_PRODUCT_ARCHITECTURE_HORIZON.md` narrowly.
- [ ] Do not rewrite the historical decision packet, `FOUNDATION_DECISION_BACKLOG.md`, PR #191, PR #162 or external repositories.
- [ ] Complete full exact-head self-review and repository-required documentation CI before squash merge.

## Excluded scope

This task does not:

- mark the whole `DUR-02 — Persistence v1` gate accepted;
- identify or accept all remaining historical DUR-02 subjects;
- emit SQL DDL, migration files, ORM/query-builder configuration or Rust persistence code;
- choose PostgreSQL table/index/constraint names or migration tooling;
- choose reconnect-secret/KMS implementation;
- define item/currency/market/house persistence or DUR-03 conservation;
- choose a first Reference PvP/world profile;
- fill any unresolved Reference behavior or exact gameplay formula;
- set production lease TTL, retry, retention, backup, RPO or RTO values;
- modify Platform, Canary, Otheryn, otclient or production state.

## Implementation / findings

Owner acceptance is explicit and bounded to the complete seventeen-rule Character persistence recommendation. The historical decision packet remains evidence/provenance; this task creates the binding owner record and current-state coordination overlay.

A later whole-DUR-02 reconciliation remains mandatory before overall `DUR-02` can become `ACCEPTED`.

## Validation

### Focused

- reconcile accepted owner baseline against the exact decision packet, accepted GAME-CHAR, DUR-01, ANL-01, FND-04, ADR-0004/0012, status model and historical DUR-02 backlog scope;
- result: pending.

### Component/integration

- `NOT_APPLICABLE` — paper-only owner architecture acceptance; no executable persistence behavior changes.

### E2E

- `NOT_APPLICABLE` — no runtime/database schema implementation or user-visible journey changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` unless final diff changes executable persistence/security/production authority or introduces material uncertainty; intended delivery records an already owner-authorized partial architecture baseline and coordination state only.

## PR and closeout

- changed-file review: pending;
- unresolved review threads: pending;
- related PRs: #191 and #162 disjoint/untouched;
- merge: squash only after exact-head gates pass;
- lifecycle closeout: separate active->archive delivery after merge, releasing ownership.

## Context checkpoint

```yaml
last_progress: Owner instructed `wykonaj`, explicitly accepting the complete seventeen-rule DUR-02 profile-neutral Character persistence recommendation as a partial baseline; dedicated branch/task claimed from current main.
status: implementing
branch: docs/OTV2-20260812-dur-02-character-persistence-owner-baseline
head_sha: null
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_trigger_source: null
ci_check_generation: null
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
next_action: Add the binding partial owner baseline and synchronize current status/register/horizon without broadening overall DUR-02 or creating runtime/DDL authority.
```
