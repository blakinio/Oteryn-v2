# OTV2-20260812-dur-02-profile-neutral-character-schema

```yaml
task_id: OTV2-20260812-dur-02-profile-neutral-character-schema
title: Prepare DUR-02 profile-neutral core Character schema architecture
mode: COORDINATE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260812-dur-02-profile-neutral-character-schema
pr: 195
base_sha: 2913201186d0e38cfc0bf0c9e2c5b83f981a61c6
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-12T00:42:00+02:00
updated_at: 2026-08-12T00:57:00+02:00
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
- `PROVEN`: CharacterRevision is semantically distinct from CharacterLease/session generations; every durable Character mutation validates/fences stale expected Character state.
- `PROVEN`: FND-04 keeps AccountPresenceClaim, CharacterLease, GameSession, TransportBinding, ControlLoss continuity and RuntimeScopeAuthority distinct; reconnect/control-loss continuity must survive permitted restarts without authority resurrection or timer reset.
- `PROVEN`: mandatory durable audit evidence commits atomically with its owning mutation; publication is at-least-once and replay never replays gameplay mutation.
- `PROVEN`: Character Authority alone owns native Character mutation; Platform AccountId/commercial state remains separate and Platform direct native Character-table writes are forbidden.
- `PROVEN`: profile-specific Character facts, unresolved Reference values/formulas and item/economy conservation remain outside this neutral-core task authority.
- `PROVEN`: open PR #191 is a disjoint factual evidence-provenance correction; PR #162 is disjoint CI/governance; both remain untouched.
- `PROVEN`: the foundation programme checkpoint has `owned_paths: []` and is non-owning.

## Acceptance criteria

- [x] Compared realistic persistence shapes and recommended normalized current-state + typed child relations rather than a mega-row, EAV/JSON or event-sourcing source of truth.
- [x] Defined Character root and global CharacterRevision semantics without making UUID order or wall time authority.
- [x] Defined global name-registry physical boundary without allowing DB collation to choose canonicalization; destination-policy collision validation is mandatory before naming-policy cutover.
- [x] Defined account-global portfolio/quota lock anchoring without creating second Account authority or drift-prone counter truth; every quota-affecting lifecycle transition uses the guard.
- [x] Defined FND-04 presence/lease/session/control-loss persistence separately from CharacterRevision and prohibited duplicated actor-wide ControlLoss truth.
- [x] Defined typed profile-extension boundaries; rejected one giant Character row and generic JSON/KV/EAV miscellaneous-state storage.
- [x] Defined retryable Character Authority OperationId receipts and separate optional persisted `(GameSessionId, CommandId)` dedup where a durable command boundary requires it.
- [x] Defined transaction/lock ordering and conditional READ COMMITTED vs bounded SERIALIZABLE retry policy.
- [x] Defined retained immutable durable-audit journal + separate mutable publication state satisfying ANL-01 without making event sourcing authoritative state; privacy/retention lifecycle remains separately governed.
- [x] Defined current-state/checkpoint and no-ack-before-commit behavior without a redundant generic snapshot blob.
- [x] Defined migration/rollback/restore/backup safety, including a no-authority-resurrection requirement after PITR/disaster restore.
- [x] Preserved semantic retirement vs privacy erasure and CharacterId non-reuse.
- [x] Kept exact operational RPO/RTO, lease TTL, retry limits, retention and unresolved Reference values out of this gate.
- [x] Did not emit SQL DDL/ORM/migration files/runtime code/production configuration.
- [x] Did not update current status/register/horizon because no DUR-02 owner acceptance exists.
- [ ] Perform full exact-head self-review and repository-required documentation CI before merge.

## Recommended architecture

- `character_root` is the per-Character identity/lifecycle/owner/world/global-revision lock anchor.
- `account_character_guard` is a game-owned serialization anchor, not Account authority or a count truth.
- `character_name_registry` stores lossless domain-generated canonical keys and authoritative uniqueness; naming-policy revisions require collision-safe cutover.
- build/progression/profile state uses typed child relations and typed extensions; no generic misc-state payload.
- FND-04 AccountPresenceClaim, CharacterLease, GameSession and ControlLoss continuity are separate relation families and separate fencing dimensions.
- OperationId is the durable retry identity for retryable Character Authority workflows; `(GameSessionId, CommandId)` is persisted only when required by an actual durable gameplay command boundary.
- Character mutations serialize via root + explicit authority anchors/constraints; account portfolio mutations use guard rows; quiescent high-impact operations revalidate presence/lease at commit.
- READ COMMITTED is acceptable only with an explicit anomaly-closing lock/constraint proof; otherwise bounded SERIALIZABLE retry uses the same semantic operation identity.
- mandatory durable event journal + publication enqueue commits atomically with mutation; retained event content is immutable while mutable delivery state is separate.
- normalized current state is canonical; extra checkpoints only reference typed owner-specific components.
- PITR/disaster restore cannot resurrect rolled-back session/lease authority and requires a newer non-rollback fence/equivalent proof before admission resumes.
- migrations use expand -> migrate/backfill -> validate -> cut over -> contract; no silent semantic reinterpretation.

## Review repair

### Repair cycle 1 — concurrency, authority, retention and status corrections

Pre-freeze persistence review found six material/clarifying issues:

1. account guard wording covered create/restore/transfer but not every lifecycle transition that may change quota eligibility;
2. `game_session` wording risked duplicating actor-wide ControlLoss state owned by a separate continuity relation;
3. FND-04 recovery binding revisions were incompletely enumerated in the GameSession persistence boundary;
4. name-policy revision storage lacked an explicit rule preventing two simultaneously authoritative canonicalization universes from bypassing global uniqueness;
5. `immutable durable journal` wording could be misread as overriding an accepted retention/privacy deletion lifecycle;
6. future DUR-02 status example decorated `DecisionStatus` with scope text rather than keeping the normative value `ACCEPTED` separate from `Accepted scope`.

Repair:

- broadened account guard use to every quota-affecting portfolio/lifecycle transition;
- made actor-wide ControlLoss continuity single-owned and removed it from GameSession state;
- added protocol/transport/ruleset/content/map/world-policy/runtime-owner binding revision evidence to the GameSession recovery boundary;
- added full destination-key collision validation and one-authoritative-policy cutover for naming revisions;
- clarified event content is immutable while retained, with separately accepted/audited retention/privacy lifecycle;
- restored normative status-axis vocabulary;
- also narrowed pseudonymous analytics evidence to forbid raw-ID fallback only in pseudonymous families, not legitimate restricted audit classes.

Repair budget used: `1/3`.

## Excluded scope

No PostgreSQL DDL/migration implementation, DB provisioning, Rust persistence adapter, item/currency tables/DUR-03 semantics, Platform writes, ruleset/content implementation, first PvP/world-profile extension, unresolved Reference values/formulas or production backup targets/numeric RPO/RTO.

## Validation

### Focused

Result after repair cycle 1 before final freeze: **PASS** against ADR-0004, DUR-01, ANL-01, accepted GAME-CHAR, FND-04A/B, ADR-0012/Character Authority boundary and architecture decision discipline.

### Component/integration/runtime E2E

`NOT_APPLICABLE` — nonbinding paper-only persistence architecture analysis; no executable database behavior changes.

### Exact-head CI

Pending final immutable PR head.

## Self-review

Pending final immutable PR head.

## Independent review

- required: `NO` for this nonbinding packet unless final review identifies an executable high-risk authority change or unresolved material uncertainty; any later owner-accepted DUR-02 contract or implementation must reassess risk.

## PR and closeout

- delivery PR: #195
- intended changed files: exactly the task record + decision packet
- current status/register/horizon changes: none
- runtime/DDL authority: none
- closeout after merge must archive the complete task record and release ownership without accepting DUR-02.

## Context checkpoint

```yaml
last_progress: Nonbinding DUR-02 profile-neutral Character schema packet is in draft PR #195; repair cycle 1 corrected quota, FND-04 continuity/binding, naming-policy migration, journal-retention and status-vocabulary issues before final freeze.
status: validating
branch: docs/OTV2-20260812-dur-02-profile-neutral-character-schema
pr: 195
final_head_sha: null
final_head_frozen_at: null
ci_checks_for_current_head: 0
repair_cycles_for_current_gate: 1
owner_action_required: null
blocker: null
next_action: Verify live main/disjoint PR state, freeze final PR head, perform full-diff self-review, run exact-head documentation CI, merge/archive only if all gates pass, then present the DUR-02 owner decision package.
```
