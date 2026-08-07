# OTV2-20260807-fnd-id01-contract

```yaml
task_id: OTV2-20260807-fnd-id01-contract
title: Complete the minimum FND-ID-01 foundation identifier contract
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260807-fnd-id01-contract
pr: null
base_sha: 67c45efd35a4882ee414a9cd78c879a7d61a97ac
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: ChatGPT architecture coordinator
created_at: 2026-08-07T21:00:00+02:00
updated_at: 2026-08-07T21:00:00+02:00
execution_budget_minutes: 60
large_budget_reason: null
owned_paths:
  - docs/agents/tasks/active/OTV2-20260807-fnd-id01-contract.md
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
public_contracts:
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
depends_on:
  - ADR-0001 through ADR-0011
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - docs/architecture/FND-ID-01_MINIMUM_CROSS_BOUNDARY_SCOPE_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_OWNER_ACCEPTED_BASELINE.md
  - docs/architecture/UUIDV7_DURABLE_IDENTITY_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_WORLD_CHANNEL_ID_ISSUANCE_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_WORLD_CHANNEL_UUIDV7_REPRESENTATION_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_NODE_ID_PROCESS_INCARNATION_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_INSTANCE_ID_ISSUER_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_PARTY_ID_ISSUER_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_CHARACTER_ID_ACCOUNT_LINK_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_GAME_SESSION_ID_OWNER_ISSUER_BASELINE.md
  - docs/architecture/FND-ID-01_GAME_SESSION_RECONNECT_GENERATION_OWNER_BASELINE.md
  - docs/architecture/FND-ID-01_ACCOUNT_SINGLE_ONLINE_CHARACTER_OWNER_BASELINE.md
  - docs/architecture/INSTANCE_SCOPE_AND_RUNTIME_OWNER_BASELINE.md
blocks:
  - FND-02 must not freeze dependent protocol identity fields before this contract is accepted
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/Oteryn-Platform (read-only reconciliation input; no writes authorized)
```

## Outcome

Create the complete minimum `FND-ID-01` foundation identifier contract required before `FND-02`, without expanding the gate into a whole-game identifier catalogue or implementing runtime/protocol/persistence behavior.

The contract must consolidate the already owner-accepted identity decisions into one normative foundation surface, resolve only the remaining identity-level ambiguities that block downstream foundation contracts, and explicitly assign all remaining wire/runtime/session/persistence mechanics to their owning gates.

## Architecture and source of truth

- `PROVEN` — `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` identifies `FND-ID-01` as the next ordered gate and requires the complete contract before `FND-02` freezes dependent protocol identity fields.
- `PROVEN` — `FND-ID-01_MINIMUM_CROSS_BOUNDARY_SCOPE_OWNER_BASELINE.md` fixes the minimum catalogue: `AccountId`, `CharacterId`, `WorldId`, `ChannelId`, `NodeId`, `InstanceId`, `PartyId`, `GameSessionId`, plus only conditionally necessary foundation identities.
- `PROVEN` — detailed owner baselines already freeze semantic scope, UUIDv7 direction/representation for adopted Oteryn-owned identities, owner/issuer boundaries and identity-versus-authority separation.
- `PROVEN` — accepted instance handoff architecture requires every authoritative ownership transition to have a unique transfer identity and to be idempotent/generation-fenced.
- `DERIVED` — the complete contract must classify that already-required transfer identity at the identity layer while leaving transaction/state-machine behavior in `FND-03`/`FND-04`; otherwise the minimum catalogue would leave a circular downstream identity dependency.
- `PROVEN` — no runtime, protocol, database or Platform implementation is authorized by the current architecture mode.

## Acceptance criteria

- [ ] Provide one normative minimum identifier catalogue and owner/issuer/scope/lifecycle/representation/visibility matrix.
- [ ] Preserve all accepted semantics for `AccountId`, `CharacterId`, `WorldId`, `ChannelId`, `NodeId`, `InstanceId`, `PartyId` and `GameSessionId`.
- [ ] Resolve the identity-level `NodeId` generator/issuer ambiguity without making registration or channel authority implicit in identifier possession.
- [ ] Classify the already-required unique ownership-transfer identity without designing the downstream handoff state machine.
- [ ] Explicitly reject premature `AdmissionId` and `CharacterLeaseId` creation unless a later accepted foundation amendment proves an independent semantic entity is required.
- [ ] Define the minimum foundation fencing/revision vocabulary as non-identity values, including connection and channel/instance ownership generations, without stealing exact runtime/protocol mechanics.
- [ ] Preserve strong semantic typing, full 128-bit UUIDv7 where accepted, explicit scope, no nil sentinels, no reuse, and lossless validation.
- [ ] Preserve external `AccountId` authority without silent re-keying.
- [ ] Define public/internal visibility defaults and compact-handle boundaries.
- [ ] Keep `CommandId`, wire byte order/IDL/framing, runtime handle bit layout, session/lease state machines and PostgreSQL layout in their owning later gates.
- [ ] Preserve architecture/analysis-only mode; no Rust/runtime/protocol/persistence/Platform implementation.
- [ ] Review the complete changed-file diff.
- [ ] Obtain an independent architecture audit on the frozen exact head with zero open material findings.
- [ ] Pass required exact-head repository checks.

## Excluded scope

This task does not:

- implement Rust identifiers or crates;
- create `protocol-oteryn` schemas/codecs/listeners;
- implement GameNode registration, runtime ownership, Game Session admission, reconnect or leases;
- implement persistence schemas, migrations or database indexes;
- modify `blakinio/Oteryn-Platform`;
- define item/economy/analytics/quest/content/social/operations identifier catalogues beyond the minimum foundation requirement;
- freeze `CommandId` or protocol sequencing representation;
- finalize product/gameplay policy such as disconnect protection, combat, transfer pricing or Party Finder matching.

## Implementation / findings

The contract is being drafted from accepted owner baselines. New text must distinguish consolidation of accepted decisions from identity-level closure required by already accepted foundation invariants.

No runtime implementation is permitted in this task.

## Validation

### Focused

- command/run: pending documentation/governance validation
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture contract only; no executable behavior changes
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable user/runtime journey changes
- result: `NOT_APPLICABLE`

### Exact-head CI

- final head: pending
- trigger source: pull_request
- workflow/run/job: pending
- runner assignment: pending
- classification: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: separate architecture consistency review against accepted ADRs and owner baselines
- material findings: pending
- verdict: pending

## PR and closeout

- changed-file review: pending
- unresolved review threads: pending
- related/superseded PRs: PR #84 is separate minimum-scope lifecycle closeout only; no path overlap with this contract
- protected auto-merge: pending all gates
- merge commit/result: pending
- ownership release: pending

## Context checkpoint

```yaml
last_progress: Dedicated current-main branch created and complete FND-ID-01 contract task claimed with non-overlapping paths.
status: implementing
branch: docs/OTV2-20260807-fnd-id01-contract
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
next_action: Draft the complete minimum FND-ID-01 foundation identifier contract from all accepted owner baselines.
```
