# OTV2-20260807-fnd-id01-register-reconcile

```yaml
task_id: OTV2-20260807-fnd-id01-register-reconcile
title: Reconcile stale FND-ID-01 coordination-register scope
mode: ARCHITECTURE_DOCS
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/OTV2-20260807-fnd-id01-register-reconcile
pr: null
base_sha: 648aa10bb5b36d8826d82ed0f1ed94a47ca53a24
owner: ChatGPT architecture coordinator
created_at: 2026-08-07T21:28:00+02:00
owned_paths:
  - docs/agents/tasks/active/OTV2-20260807-fnd-id01-register-reconcile.md
  - docs/architecture/FOUNDATION_DECISION_BACKLOG.md
  - docs/architecture/GLOBAL_ARCHITECTURE_DECISION_REGISTER.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
public_contracts: []
depends_on:
  - docs/architecture/FND-ID-01_FOUNDATION_IDENTIFIER_CONTRACT.md
  - docs/architecture/FND-ID-01_MINIMUM_CROSS_BOUNDARY_SCOPE_OWNER_BASELINE.md
  - docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md
  - issue #86
blocks:
  - clean programme handoff to FND-02
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories: []
```

## Outcome

Resolve issue #86 by making the two long-lived coordination registers agree with the merged minimum `FND-ID-01` contract, while preserving the existing gate ordering and all unrelated architecture.

## Required reconciliation

- `FND-ID-01` becomes `ACCEPTED` and references the merged canonical contract.
- Foundation catalogue is limited to `AccountId`, `CharacterId`, `WorldId`, `ChannelId`, `NodeId`, `InstanceId`, `PartyId`, `GameSessionId` and the accepted conditional `HandoffId`.
- `CommandId` and command sequencing remain `FND-02` protocol mechanics.
- Runtime-local entity/handle mechanics remain `FND-03`.
- Admission/session/lease state machines remain `FND-04`.
- Event/operation/transaction/correlation/causation/analytics identity catalogues remain with `ANL-*`/`DUR-*` as appropriate.
- No runtime, protocol, persistence or Platform implementation is authorized.

## Acceptance criteria

- [ ] Reconcile `FOUNDATION_DECISION_BACKLOG.md` without erasing unrelated history or gate definitions.
- [ ] Reconcile `GLOBAL_ARCHITECTURE_DECISION_REGISTER.md` without erasing unrelated horizon entries.
- [ ] Update `FOUNDATION_PROGRAMME_CURRENT_STATUS.md` so #86 becomes complete and `FND-02` is the clean next ordered architecture gate.
- [ ] Preserve `FND-ID-01 -> FND-02 -> FND-03 -> FND-04` ordering.
- [ ] Full changed-file review shows only declared documentation paths.
- [ ] Exact-head governance/security checks pass.
- [ ] Independent architecture audit has zero open material findings.
- [ ] Merge through squash PR, archive task and close #86 only after evidence is terminal.

## Validation

Documentation-only. Runtime/component/E2E: `NOT_APPLICABLE`.

## Context checkpoint

```yaml
last_progress: Current main and issue #86 verified; bounded reconciliation branch created and paths claimed.
status: implementing
branch: docs/OTV2-20260807-fnd-id01-register-reconcile
pr: null
base_sha: 648aa10bb5b36d8826d82ed0f1ed94a47ca53a24
blocker: null
next_action: Reconcile FOUNDATION_DECISION_BACKLOG.md and GLOBAL_ARCHITECTURE_DECISION_REGISTER.md to the merged FND-ID-01 contract.
```
