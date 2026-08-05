# OTV2-20260805-pre-native-protocol-migration-state

```yaml
task_id: OTV2-20260805-pre-native-protocol-migration-state
title: Define the post-migration pre-native-protocol client state
mode: CONTRACT
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/fnd-01-pre-native-protocol-state
pr: pending
base_sha: 100f2d538fa1fc5d0f32d2aed491778bc60033a1
head_sha: pending
owner: GPT-5.6-Thinking-architecture-coordinator
created_at: 2026-08-05T23:26:00+02:00
updated_at: 2026-08-05T23:26:00+02:00
execution_budget_minutes: 30
large_budget_reason: null
owned_paths:
  - docs/architecture/ADR-0011-native-client-pre-protocol-migration-state.md
  - docs/agents/tasks/active/OTV2-20260805-pre-native-protocol-migration-state.md
public_contracts:
  - docs/architecture/ADR-0011-native-client-pre-protocol-migration-state.md
depends_on:
  - ADR-0001
  - ADR-0002
  - ADR-0008
  - FND-01
  - VSL-02
blocks:
  - the atomic destination migration until the no-adapter transition state is explicit
cross_repository_coordination_id: OTV2-NATIVE-FOUNDATION
external_repositories:
  - blakinio/otclient (read-only evidence)
```

## Outcome

Record the owner-accepted migration invariant that the atomic Rust-client destination migration may produce a compilable and launchable `pre-native-protocol` client state, while production gameplay entry remains explicitly unavailable until the native Oteryn protocol and the later runtime/admission gates are implemented and validated.

## Architecture and source of truth

### PROVEN

- ADR-0002 requires `FND-01`, then `VSL-02`, then one atomic destination migration/workspace PR before `FND-02`.
- ADR-0008 fixes `protocol-canary` as `REFERENCE_ONLY` and excludes it from the destination production dependency graph, negotiation, fallback and translation paths.
- The existing Rust client source workspace contains production dependencies on `protocol-canary` and does not contain an implemented `protocol-oteryn` crate.
- `FND-02` owns the native protocol contract; speculative protocol constants, placeholder codecs and false compatibility claims are forbidden before that gate.

### ACCEPTED

- The owner accepted on 2026-08-05 that the migrated client may compile and launch in a `pre-native-protocol` state.
- The transition state contains no production gameplay protocol adapter.
- Gameplay entry is fail-closed and visibly unavailable; no credentials are consumed and no false success is presented.
- `FND-02` is necessary to leave the no-native-protocol state, but production gameplay still requires the applicable runtime and admission gates, including `FND-03` and `FND-04`.

## Acceptance criteria

- [ ] ADR-0011 defines the transition state and its exact security/product invariants.
- [ ] The migration is not allowed to retain `protocol-canary` as a temporary production adapter.
- [ ] The migration is not allowed to create an empty or speculative `protocol-oteryn` production crate.
- [ ] The client may compile and launch, but every production gameplay-entry path fails closed before gameplay credential handoff or endpoint connection.
- [ ] User-facing state cannot imply that gameplay is available.
- [ ] `FND-02` is recorded as necessary but not sufficient for production gameplay; `FND-03` and `FND-04` remain mandatory.
- [ ] No runtime code, workspace, protocol schema or external repository is modified.
- [ ] Exact-head documentation/governance validation passes.

## Excluded scope

- No client migration or Cargo workspace mutation.
- No `protocol-oteryn` schema, codec, transport or capability implementation.
- No Platform, Game Gateway, Game Session or game-server implementation.
- No changes to `blakinio/otclient`.
- No decision about the final launcher, login-screen or offline-tool UX beyond explicit non-deception and fail-closed behavior.

## Implementation / findings

Pending ADR creation.

## Validation

### Focused

- command/run: complete changed-file review against the exact base SHA
- result: pending

### Component/integration

- command/run: `NOT_APPLICABLE` — architecture-only task
- result: `NOT_APPLICABLE`

### E2E

- scenario: `NOT_APPLICABLE` — no executable product change
- result: `NOT_APPLICABLE`

### Exact-head CI

- head: pending
- workflow/run: pending
- result: pending

## Independent audit

- exact head: pending
- method/auditor: adversarial architecture review against ADR-0001, ADR-0002, ADR-0008, FND-01, VSL-02, FND-02, FND-03 and FND-04
- material findings: pending
- verdict: pending

## Context checkpoint

```yaml
last_progress: Created the bounded architecture task and reserved the new ADR path.
status: implementing
branch: docs/fnd-01-pre-native-protocol-state
head_sha: pending
pr: pending
blocker: none
next_action: Create ADR-0011, open the draft PR, audit the exact diff and update this task record.
```
