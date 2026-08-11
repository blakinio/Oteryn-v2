# OTV2-20260812-dur-02-profile-neutral-character-schema

```yaml
task_id: OTV2-20260812-dur-02-profile-neutral-character-schema
title: Prepare DUR-02 profile-neutral core Character schema architecture
mode: COORDINATE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260812-dur-02-profile-neutral-character-schema
pr: null
base_sha: 2913201186d0e38cfc0bf0c9e2c5b83f981a61c6
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-12T00:42:00+02:00
updated_at: 2026-08-12T00:42:00+02:00
execution_budget_minutes: 60
owned_paths:
  - docs/agents/tasks/active/OTV2-20260812-dur-02-profile-neutral-character-schema.md
  - docs/architecture/DUR-02_PROFILE_NEUTRAL_CHARACTER_SCHEMA_DECISION_PACKET.md
public_contracts: []
depends_on:
  - docs/architecture/ADR-0004-postgresql-and-data-ownership.md
  - docs/architecture/DUR-01_DURABLE_IDENTIFIER_REPRESENTATION_CONTRACT.md
  - docs/architecture/ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md
  - docs/architecture/GAME-CHAR-01_STAGE_A_OWNER_BASELINE.md
  - docs/architecture/GAME-CHAR-01_STAGE_B_OWNER_BASELINE.md
  - docs/architecture/FND-04_IDENTITY_GAME_SESSION_ADMISSION_CHARACTER_LEASE_CONTRACT.md
  - docs/architecture/FND-04A_AUTHORITY_FRESH_ADMISSION_CONTRACT.md
  - docs/architecture/FND-04B_RECONNECT_RECOVERY_CONTINUITY_CONTRACT.md
  - docs/architecture/ADR-0012-character-authority-and-platform-lifecycle-boundary.md
  - docs/contracts/CHARACTER_AUTHORITY_PLATFORM_BOUNDARY.md
  - docs/architecture/ARCHITECTURE_STATUS_MODEL.md
blocks:
  - owner decision on DUR-02 profile-neutral core Character persistence architecture
  - later authorized physical PostgreSQL Character persistence implementation
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Prepare one nonbinding paper-only DUR-02 decision packet for the profile-neutral core Character persistence architecture now unblocked by accepted GAME-CHAR. Define relation/ownership families, revisions/fencing, transaction and locking rules, idempotency/receipts, durable audit/outbox, checkpoint/recovery, migration and restore safety without emitting SQL DDL, migrations or runtime code and without encoding unresolved Reference behavior.

## Source of truth

- `PROVEN`: trusted base is `main@2913201186d0e38cfc0bf0c9e2c5b83f981a61c6`.
- `PROVEN`: GAME-CHAR-01 is `ACCEPTED / LIFECYCLE_CLOSED / NOT_STARTED`; only paper-only profile-neutral DUR-02 schema architecture is unblocked.
- `PROVEN`: PostgreSQL is the authoritative game relational target; Platform and game use separate logical databases and have no cross-database foreign keys or unrestricted shared writers.
- `PROVEN`: native UUIDv7 identities persist as PostgreSQL `uuid`; persisted CommandId uses full-range `numeric(20,0)` in `(GameSessionId, CommandId)` scope.
- `PROVEN`: CharacterRevision is semantically distinct from CharacterLease/session generations; every durable Character mutation must validate/fence stale expected Character state.
- `PROVEN`: FND-04 keeps AccountPresenceClaim, CharacterLease, GameSession, TransportBinding and RuntimeScopeAuthority distinct; reconnect/control-loss continuity must survive permitted restarts without authority resurrection or timer reset.
- `PROVEN`: mandatory durable audit evidence commits atomically with its owning mutation; publication is at-least-once and replay never replays gameplay mutation.
- `PROVEN`: Character Authority alone owns native Character mutation; Platform AccountId/commercial state remains separate and Platform direct native Character-table writes are forbidden.
- `PROVEN`: profile-specific Character facts, unresolved Reference values/formulas and item/economy conservation remain outside the neutral-core authority of this task.
- `PROVEN`: open PR #191 is a disjoint factual evidence-provenance correction; PR #162 is disjoint CI/governance; both remain untouched.
- `PROVEN`: the foundation programme checkpoint has `owned_paths: []` and is non-owning; it does not reserve DUR-02 paths.

## Acceptance criteria

- [ ] Compare realistic persistence shapes and recommend one profile-neutral model.
- [ ] Define root Character relation and global CharacterRevision semantics without making UUID ordering or wall time authority.
- [ ] Define global name-registry physical boundary without allowing database collation to choose canonicalization.
- [ ] Define account-global quota/concurrency lock anchoring without creating a second Account authority or drift-prone counter truth.
- [ ] Define FND-04 persistence relations/fencing separately from CharacterRevision.
- [ ] Define typed profile-extension boundaries; reject one giant Character row and untyped JSON/KV miscellaneous-state storage.
- [ ] Define retryable Character Authority operation receipts/idempotency and the separate optional persisted `(GameSessionId, CommandId)` dedup boundary where required.
- [ ] Define transaction/lock ordering and isolation/retry policy sufficient to avoid name/quota/ownership/lease races.
- [ ] Define immutable durable-audit journal + publication/outbox boundary satisfying ANL-01 without making event sourcing authoritative state.
- [ ] Define checkpoint/recovery semantics without a redundant generic Character snapshot blob.
- [ ] Define migration/rollback/restore/backup safety, including no pre-restore session/lease authority resurrection.
- [ ] Preserve semantic retirement versus privacy erasure and no CharacterId reuse.
- [ ] Keep exact operational RPO/RTO, lease TTL, reconnect timing and unresolved Reference values out of this gate unless already accepted elsewhere.
- [ ] Do not emit SQL DDL, ORM/migration files, runtime code or production configuration.
- [ ] Do not update current status/register/horizon because no DUR-02 owner acceptance exists yet.
- [ ] Perform full exact-head self-review and repository-required documentation CI before merge.

## Excluded scope

No PostgreSQL DDL/migration implementation, no database provisioning, no connection-pool/library selection, no runtime persistence adapter, no item/currency tables or DUR-03 transaction semantics, no Platform writes, no ruleset/content implementation, no first PvP/world-profile schema extension, no exact unresolved Reference values/formulas, no production backup target or numeric RPO/RTO.

## Validation

### Focused

Reconcile the packet against ADR-0004, DUR-01, ANL-01, accepted GAME-CHAR, FND-04, ADR-0012/Character Authority boundary and architecture decision discipline.

### Component/integration/runtime E2E

`NOT_APPLICABLE` — nonbinding paper-only persistence architecture analysis; no executable database behavior changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` unless final analysis unexpectedly freezes high-risk executable data/security behavior rather than remaining a nonbinding decision packet; an accepted DUR-02 contract or implementation would require risk reassessment.

## Context checkpoint

```yaml
last_progress: GAME-CHAR owner baseline lifecycle is closed; DUR-02 profile-neutral Character persistence inputs were reconciled and a dedicated nonbinding schema-architecture task/branch is claimed from current main.
status: implementing
branch: docs/OTV2-20260812-dur-02-profile-neutral-character-schema
pr: null
final_head_sha: null
final_head_frozen_at: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 0
owner_action_required: null
blocker: null
next_action: Write the nonbinding DUR-02 profile-neutral core Character schema decision packet, explicitly separating core relation/transaction/fencing decisions from typed profile extensions and unresolved Reference behavior.
```
