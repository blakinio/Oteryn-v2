# OTV2-20260805-foundation-preimplementation-contracts

```yaml
task_id: OTV2-20260805-foundation-preimplementation-contracts
title: Freeze Oteryn v2 pre-implementation foundation contracts
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/foundation-decisions-20260805
pr: null
base_sha: 0eb3c329fd04211e1bb5c6e3f219f4daad5e500a
head_sha: null
owner: chatgpt-github-agent
created_at: 2026-08-05T08:49:00+02:00
updated_at: 2026-08-05T09:28:00+02:00
execution_budget_minutes: 120
large_budget_reason: The contract programme spans repository ownership, protocol, runtime, persistence, content, Platform integration and a cross-repository migration boundary.
owned_paths:
  - docs/architecture/ADR-0002-repository-ownership-and-client-migration.md
  - docs/architecture/ADR-0003-platform-identity-game-gateway-and-admission-boundary.md
  - docs/architecture/ADR-0004-postgresql-and-data-ownership.md
  - docs/agents/tasks/active/OTV2-20260805-foundation-preimplementation-contracts.md
public_contracts:
  - docs/architecture/ADR-0001-native-rust-multichannel-platform.md
  - docs/architecture/ADR-0002-repository-ownership-and-client-migration.md
  - docs/architecture/ADR-0003-platform-identity-game-gateway-and-admission-boundary.md
  - docs/architecture/ADR-0004-postgresql-and-data-ownership.md
  - docs/architecture/MULTICHANNEL_SYSTEM_SCOPE_MATRIX.md
  - docs/architecture/OTHERYN_REFERENCE_MIGRATION_PLAN.md
depends_on:
  - ADR-0001 accepted native Rust and multichannel foundation
blocks:
  - creation of the root Cargo workspace
  - implementation of protocol-oteryn
  - migration of the existing Rust client
  - implementation of the authoritative Rust game server
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform
  - blakinio/Otheryn
  - blakinio/otclient
```

## Outcome

Freeze the minimum architecture decisions needed before creating the real Oteryn v2 Rust workspace. The repository must contain a durable source of truth for repository ownership, client migration, the Platform/Game Gateway boundary and database ownership so that a later agent does not need this chat transcript.

This task records decisions only. It does not move code, create the Rust workspace, modify `Oteryn-Platform`, activate a native protocol or migrate a live database.

## Architecture and source of truth

### PROVEN — existing accepted foundation

- Oteryn v2 consists of a native Rust game client, authoritative Rust game server and one project-owned gameplay protocol named `protocol-oteryn`.
- One logical world may contain multiple gameplay channels.
- Otheryn C++ is a behavioural/content migration reference, not the target runtime.
- `protocol-canary` and legacy Tibia packet compatibility are not part of the target Oteryn v2 runtime.
- `blakinio/Oteryn-Platform` remains the external owner of web portal, Identity, OAuth/PKCE, Game Login Tickets, Game Gateway and World Registry unless a later accepted ADR explicitly changes that boundary.
- The existing Rust client is currently under `blakinio/otclient/oteryn-client`; it uses Tokio and has `protocol-core` plus `protocol-canary`, but no implemented `protocol-oteryn` crate.
- Oteryn Platform contains a standalone Go Game Gateway. The native gameplay producer side exists but is disabled by default and does not prove a working native client-to-server path.
- There is no complete `protocol-oteryn` runtime today: no Rust client adapter, no authoritative Rust server listener and no passing native E2E gameplay path.

### ACCEPTED OWNER DECISIONS — 2026-08-05

1. **Client and server repository ownership**
   - the native Rust client will move from `blakinio/otclient/oteryn-client` into `blakinio/Oteryn-v2`;
   - client, server, shared Rust types and `protocol-oteryn` will have one canonical Rust workspace and one repository owner;
   - the migration must preserve exact source revision and provenance and must not leave two actively developed client copies;
   - `blakinio/otclient` remains a reference/history repository after migration.

2. **Platform and admission boundary**
   - Oteryn v2 does not introduce a new classic login-server process;
   - Platform Identity remains the only target authority for reusable credentials, OAuth/PKCE, MFA and account-security policy;
   - Game Gateway remains in `blakinio/Oteryn-Platform` and remains the route/session orchestration boundary;
   - the existing Gateway remains implemented in Go for the initial Oteryn v2 delivery;
   - it is not moved into the game-server repository and is not rewritten in Rust without a later ADR supported by measurable operational or maintenance evidence;
   - the Rust client calls Platform/Identity and Game Gateway; the Rust game server accepts only a bounded Game Session and does not verify passwords or perform direct OAuth.

3. **Database and ownership direction**
   - PostgreSQL is the target relational database technology for Oteryn v2;
   - Platform and game persistence use separate logical databases, owners, credentials and migration histories;
   - the initial deployment may place `oteryn_platform` and `oteryn_game` on one PostgreSQL cluster, but they remain separate security and ownership boundaries;
   - no table has two unrestricted writers and no cross-database foreign key is required;
   - Platform may temporarily remain on its current database during migration, but the production target is PostgreSQL and new Oteryn v2 contracts must not add a MariaDB dependency;
   - Redis may support cache, rate limiting, presence or short-lived coordination, but it is not the source of truth for character, inventory, lease, house, market or financial data.

4. **Data access boundary**
   - Platform-owned identity, web, CMS, payments, wallet, support and audit data remain Platform-owned;
   - gameplay state, characters, inventory, progression, guild/world gameplay state, houses, leases and durable game mutations are game-owned;
   - cross-system mutations use explicit versioned APIs/contracts rather than unrestricted shared SQL;
   - public portal reads should use a query API or tightly allowlisted read-only views/principals.

### UNKNOWN — still requires a later contract

- exact root Cargo workspace members and final crate names;
- exact source commit and history-preserving mechanism used for client migration;
- exact `protocol-oteryn` framing, IDL ownership, message namespace and hard limits;
- whether the existing Platform native gameplay contract is adopted, revised or explicitly superseded for the Rust server;
- exact Game Session token format, issuer keys, rotation, atomic consume, reconnect and revocation behaviour;
- exact lease ownership and storage split between Platform and the game persistence boundary;
- simulation tick frequency, queue capacities and deterministic timer model;
- exact identifier representations and entity/position encoding;
- full PostgreSQL schema, migration tooling, isolation levels, partitioning, backup, RPO and RTO;
- content output formats, scripting runtime and initial production ruleset;
- final house presence/entry topology.

## Required pre-implementation contracts

The start gate remains:

1. repository ownership and client migration ADR;
2. workspace and dependency contract;
3. `protocol-oteryn` v1 contract;
4. runtime execution contract;
5. Identity, admission, Game Session and lease contract;
6. persistence v1 contract;
7. content migration and scripting contract;
8. foundation vertical-slice programme.

Contracts 1 and the ownership/database portions of 5 and 6 are advanced by this decision-recording change. The remaining protocol, runtime, session/lease and detailed persistence decisions still block workspace implementation.

## Target boundaries

```text
blakinio/Oteryn-Platform
├── portal and account UI
├── Identity / OAuth Authorization Code + PKCE
├── MFA, recovery and account-security policy
├── one-time Game Login Ticket
├── Game Gateway (Go)
├── World Registry and channel directory
└── Game Session issuance/orchestration contract

blakinio/Oteryn-v2
├── apps/client (migrated Rust client)
├── services/game-server (authoritative Rust server)
├── crates/protocol-oteryn
├── shared domain/session/protocol types
├── channel and world runtimes
└── PostgreSQL game persistence adapters
```

Target admission flow:

```text
Rust client
→ Platform Identity OAuth Authorization Code + PKCE
→ one-time Game Login Ticket
→ Game Gateway
→ World Registry selection
→ Game Session bound to account, character, world, channel and revisions
→ Rust game server admission
→ character lease
→ protocol-oteryn gameplay connection
```

## Acceptance criteria

- [ ] Repository ownership/client migration ADR is present and records the accepted move into `Oteryn-v2`.
- [ ] Platform Identity/Game Gateway ADR is present and forbids a second password/OAuth authority.
- [ ] Gateway ownership and initial Go implementation are explicitly recorded.
- [ ] PostgreSQL and separate logical database ownership are explicitly recorded.
- [ ] Current versus target protocol status is stated without claiming native E2E support.
- [ ] Remaining unknowns are preserved and not accidentally frozen.
- [ ] Focused governance/link validation passes on the exact final head.
- [ ] Independent diff audit has no material finding.
- [ ] PR is squash-merged and this task is archived or updated for the next foundation contract lane.

## Excluded scope

- no code migration from `blakinio/otclient`;
- no write to `blakinio/Oteryn-Platform`, `blakinio/Otheryn` or `blakinio/otclient`;
- no root Cargo workspace or crate creation;
- no Gateway rewrite;
- no protocol activation or runtime claim;
- no PostgreSQL deployment or data migration;
- no final schema, token, lease, house or content-runtime decision.

## Validation

### Focused

- command/run: pending `python tools/agents/validate_governance.py`
- result: pending

### Component/integration

- result: `NOT_APPLICABLE` — documentation-only contract recording

### E2E

- result: `NOT_APPLICABLE` — no runtime implementation or deployment changes

### Exact-head CI

- head: pending
- workflow/run: pending `Agent governance`
- result: pending

## Independent audit

- exact head: pending
- method/auditor: review complete changed-file set against ADR-0001, current Platform/otclient evidence and owner decisions
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: none found at task start
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Existing foundation task was claimed and the owner decisions from the 2026-08-05 architecture conversation were converted into explicit contract scope.
status: implementing
branch: docs/foundation-decisions-20260805
head_sha: null
pr: null
ci_check_generation: null
ci_checks_for_current_head: 0
terminal_ci_wait_started_at: null
terminal_ci_checks_for_current_generation: 0
unchanged_state_checks: 0
identical_failure_retries: 0
repair_cycles_for_current_gate: 0
stall_warnings: 0
blocker: null
next_action: Add ADR-0002, ADR-0003 and ADR-0004 with the accepted repository, admission and PostgreSQL decisions.
```
