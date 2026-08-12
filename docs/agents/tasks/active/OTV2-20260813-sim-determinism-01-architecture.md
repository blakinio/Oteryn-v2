# OTV2-20260813-sim-determinism-01-architecture

```yaml
task_id: OTV2-20260813-sim-determinism-01-architecture
title: SIM-DETERMINISM-01 authoritative simulation determinism architecture
mode: CONTRACT
status: investigating
repository: blakinio/Oteryn-v2
base_branch: main
branch: agent/otv2-20260813-sim-determinism-01-architecture
pr: null
base_sha: 27c313a0c6032f0433ad9598c3cf53e4f0179813
head_sha: null
final_head_sha: null
final_head_frozen_at: null
owner: architecture-coordinator/current-session
created_at: 2026-08-13T00:55:00+02:00
updated_at: 2026-08-13T00:55:00+02:00
execution_budget_minutes: 90
large_budget_reason: Cross-cutting paper-only determinism gate spans authoritative arithmetic, RNG ownership, logical time/order, replay inputs and cross-target evidence without authorizing runtime implementation.
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-sim-determinism-01-architecture.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_ANALYSIS.md
  - docs/architecture/SIM-DETERMINISM-01_AUTHORITATIVE_SIMULATION_CONTRACT.md
public_contracts:
  - SIM-DETERMINISM-01
depends_on:
  - FND-03
  - GAME-VISION-01
  - GAME-CHAR-01
  - GAME-ITEM-01
  - DUR-03
  - DUR-04
  - ANL-01
blocks:
  - broad combat and AI formula freeze
  - deterministic replay implementation contract
  - PARITY_CONFIRMED claims for unresolved authoritative Character arithmetic
cross_repository_coordination_id: OTV2-GLOBAL-ARCHITECTURE
external_repositories: []
```

## Outcome

Produce one bounded paper-only `SIM-DETERMINISM-01 — Authoritative Simulation Determinism Contract` that refines, but does not replace, accepted FND-03 runtime order/RNG/replay foundations and DUR-04 script execution determinism.

The gate must freeze only the cross-domain semantics needed before broad combat/AI/progression formula implementation: authoritative numeric representation classes, rounding/overflow/invalid numeric state, RNG stream identity/ownership/consumption, logical time and deterministic ordering/tie-break rules, replay input capture, state hashing/divergence evidence, supported-target determinism and formula/ruleset revision compatibility.

No Rust/runtime/client/combat/AI/script implementation, PostgreSQL DDL/migrations, Platform write, production configuration/deployment or formula/balance-value acceptance is authorized.

Maintained programme/register/horizon/index/handoff files stay outside the delivery PR and may be promoted only through a separate lifecycle closeout after a reviewed delivery merge.

## Verified start facts

- `PROVEN`: post-DUR-04-closeout `main@27c313a0c6032f0433ad9598c3cf53e4f0179813` selects `SIM-DETERMINISM-01 = PROPOSED / PLANNED / NOT_STARTED` as the one next bounded paper-only architecture action.
- `PROVEN`: no active SIM-DETERMINISM task and no open SIM delivery PR existed at task start.
- `PROVEN`: FND-03 already owns one logical authoritative writer per Channel/Instance, owner-scoped `RuntimeExecutionOrdinal`, separation of execution order from monotonic deadlines and wall-clock timestamps, deterministic authoritative RNG/replay requirements and stale-result rejection. SIM must refine these semantics rather than create a competing runtime order.
- `PROVEN`: GAME-CHAR deliberately keeps authoritative progression facts formula-neutral and delegates exact arithmetic/rounding to ruleset/SIM parity gates where those details do not constrain identity/ownership/migration.
- `PROVEN`: GAME-ITEM requires deterministic modifier contribution ordering while exact arithmetic/rounding remains SIM/ruleset-owned.
- `PROVEN`: DUR-03 conservation uses exact item/asset quantities and bounded non-floating value arithmetic; SIM may define formula arithmetic but must not weaken conservation or transaction authority.
- `PROVEN`: DUR-04 owns authoritative script execution determinism through `script_execution_profile_revision`, snapshot-bound inputs, invocation-local deterministic RNG, stable query order and deterministic numeric/fuel/resource semantics. SIM must define how script results enter core simulation order without making the script profile a competing global simulation authority.
- `PROVEN`: GAME-VISION Reference claims remain evidence-gated; deterministic implementation convenience cannot fill `UNKNOWN/CONFLICT` Global behavior.
- `PROVEN`: current governance forbids Codex/OpenAI API/owner-funded AI use without specific owner permission for that exact use. The prior owner review override was recorded for PR #212 only and is not assumed to be standing permission for this task.

## Candidate decision goals

- [ ] Define authoritative numeric semantic classes rather than one universal number type.
- [ ] Keep identifiers/counts/currency/conservation exact and separate from formula-domain numeric policy.
- [ ] Decide deterministic fixed-point/integer/rational/floating boundaries and when float is forbidden or requires an explicit deterministic profile.
- [ ] Define rounding mode, rounding stage, overflow/underflow, divide-by-zero, NaN/infinity and invalid-state handling.
- [ ] Define formula/ruleset revision identity so an unchanged revision cannot silently reinterpret arithmetic.
- [ ] Define RNG root identity, deterministic stream/substream derivation, ownership and consumption rules without one mutable process-global RNG stream.
- [ ] Prevent unrelated random consumers from perturbing another mechanic's future sequence.
- [ ] Define replay-safe treatment of rejection/cancellation/retry so random draws are not invisibly consumed by failed authority paths.
- [ ] Consume FND-03 `RuntimeExecutionOrdinal` as owner-scoped authoritative order; do not invent a global total order.
- [ ] Define deterministic tie-breakers for commands, timers, system inputs, worker results and simultaneous-domain actions at the normalization boundary.
- [ ] Keep wall clock observational/policy input distinct from authoritative logical simulation time/order.
- [ ] Define which external nondeterminism must be captured as normalized authoritative input before it can affect simulation.
- [ ] Define replay envelope: exact input identities, revisions, RNG streams, content/ruleset/script execution profiles and initial/checkpoint state required for reproducibility.
- [ ] Define canonical state-hash scopes and first-divergence localization without treating hash as gameplay authority.
- [ ] Define supported-target determinism: which outputs must be bit-identical or semantically identical across Linux/Windows/CPU architectures and how exceptions are explicit.
- [ ] Define boundary between core SIM determinism and DUR-04 `script_execution_profile_revision`.
- [ ] Define deterministic acceptance scenarios for arithmetic edge cases, RNG isolation, replay, cross-target comparison and divergence diagnosis.
- [ ] Apply full architecture decision tests for any technology/representation choice that would be costly to change later.
- [ ] Preserve all implementation/non-authority boundaries.
- [ ] Perform full exact-head self-review and required exact-head Agent Governance / Dependency Review / CodeQL.
- [ ] Evaluate independent-review requirement truthfully under current root risk policy; do not invoke owner-funded AI without a new explicit permission for this task.

## Excluded scope

- concrete Rust numeric/RNG crate selection or dependency changes;
- implementation of RNG, replay, state hashing, simulation loop, combat, AI, progression or scripts;
- exact combat/skill/XP/item/balance formulas or numeric Global values;
- fixed global tick rate, thread/worker counts, CPU affinity or scheduler library;
- PostgreSQL schema/migrations;
- protocol packet/schema changes unless a later owner explicitly expands scope;
- production deployment/configuration;
- Reference behavior guessing from OTS implementations.

## Validation

### Focused

- live main/ownership preflight: PASS
- accepted-source audit: in progress
- analysis/contract drafting: pending
- full-diff self-review: pending

### Component/integration/runtime E2E

- `NOT_APPLICABLE` — paper-only architecture task

### Owner-funded AI policy

- Codex/OpenAI API/paid AI reviewer: **NOT AUTHORIZED / NOT INVOKED**
- prior owner override for PR #212: **NOT INHERITED**

## Context checkpoint

```yaml
last_progress: DUR-04 lifecycle closeout merged as main@27c313a0c6032f0433ad9598c3cf53e4f0179813; live active-task/open-PR preflight found no SIM-DETERMINISM owner, so this bounded paper-only task claimed exactly task + analysis + contract paths.
status: investigating
branch: agent/otv2-20260813-sim-determinism-01-architecture
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
owner_action_required: false
blocker: null
next_action: Audit accepted FND-03/GAME-CHAR/GAME-ITEM/DUR-03/DUR-04 determinism ownership, then draft the bounded SIM analysis and contract without implementing runtime behavior.
```
