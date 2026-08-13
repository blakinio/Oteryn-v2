# OTV2-20260813-game-ability-reference-catalogue-parity-fixture-contract

```yaml
task_id: OTV2-20260813-game-ability-reference-catalogue-parity-fixture-contract
title: Define representative Reference Mechanic Catalogue and parity-fixture entry contract
mode: CONTRACT
status: ready_for_continuation
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/game-ability-reference-catalogue-handoff
owner: unassigned architecture continuation agent
implementation_status: NOT_STARTED
runtime_client_authority: NONE
postgresql_ddl_migration_authority: NONE
platform_write_authority: NONE
production_authority: NONE
```

## Durable handover

Verified canonical `main` at handoff: `199bb6a7559d610be9e01508dd1e5d192b5db820` (PR #247 closeout).

Accepted and lifecycle-closed `GAME-ABILITY-01` baselines on `main`:
- `GAME-ABILITY-01_TYPED_EFFECT_PIPELINE_OWNER_BASELINE.md`
- `GAME-ABILITY-01_TARGETING_AND_LEGALITY_BOUNDARY_OWNER_BASELINE.md`
- `GAME-ABILITY-01_CAST_CHANNEL_COMMIT_OWNER_BASELINE.md`
- `GAME-ABILITY-01_COOLDOWN_CHARGE_CONDITION_OWNER_BASELINE.md`
- `GAME-ABILITY-01_EFFECT_COMPOSITION_DAMAGE_HEAL_OWNER_BASELINE.md`
- `GAME-ABILITY-01_EFFECT_FAMILIES_REFERENCE_CATALOGUE_OWNER_BASELINE.md`

Overall `GAME-ABILITY-01` remains `REQUIRED_FOR_ALPHA / OPEN`; runtime is unauthorized.

Preserve: typed effects only; authoritative mutation stays with owner domains; item/value conservation remains under `GAME-ITEM`/`DUR-03`; movement/world/entity/AI ownership is not transferred to abilities; no generic state patch/event bus, giant per-mechanic core enum, hidden global transaction model or alternate mutation engine; catalogue identity is local provenance only; catalogue presence never proves Reference parity; `UNKNOWN`/`CONFLICT` remains fail-closed.

Before continuing, read live `main` governance (`AGENTS.md`, `docs/agents/AGENTS.md`, `PROMPTING_STANDARD.md`, `PROMPTING_HANDOVER.md`, `ARCHITECTURE_DECISION_DISCIPLINE.md`, `CONTEXT_HANDOFF.md`), all six baselines above, `REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md`, `ANL-01_GAME_EVENT_AND_AUDIT_FOUNDATION_CONTRACT.md`, and applicable `GAME-ITEM`, `DUR-03`, `DUR-04`, `SIM-DETERMINISM-01` contracts. Verify live PR/task drift first. PR #191 was separate stale-base GAME-CHAR provenance work at the last check and must not be silently absorbed.

Next bounded decision: define one representative Reference Mechanic Catalogue entry + parity-fixture binding contract. Bind a catalogue-local mechanic key to evidence references and behavior-affecting revision bindings; represent parity/unknown state without promotion-by-presence; reference target/cast/cost/cooldown/formula/effect/condition/RNG revisions; keep missing/conflicting evidence explicit and fail-closed; include one representative example shape without inventing Tibia facts; preserve domain ownership; remain paper-only with no runtime/protocol/DDL/serializer lock-in/Platform/production changes.

Governance: exact-head `Merge gate / validate` is required; CI from an older head cannot be reused; all review threads must be resolved; do not invoke owner-funded Codex/OpenAI usage without explicit authorization.

## Context checkpoint

```yaml
status: ready_for_continuation
branch: docs/game-ability-reference-catalogue-handoff
head_sha: pending_delivery
pr: pending
owned_paths:
  - docs/agents/tasks/active/OTV2-20260813-game-ability-reference-catalogue-parity-fixture-contract.md
public_contracts:
  - six accepted GAME-ABILITY-01 owner baselines
  - docs/architecture/REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md
last_progress: Sixth partial baseline delivered by PR #245 and lifecycle-closed by PR #247; main = 199bb6a7559d610be9e01508dd1e5d192b5db820.
validation_state: Previous delivery and closeout exact-head aggregate gates PASS; this checkpoint requires normal PR governance before becoming canonical.
audit_state: Previous self-review complete; no unresolved review threads after #247.
e2e_state: NOT_APPLICABLE
ci_generation: none
run_ids: []
counters: {}
blocker: null
next_action: Verify live main/open-PR/task drift, claim a fresh bounded branch, then draft the representative Reference Mechanic Catalogue plus parity-fixture entry contract against the six accepted GAME-ABILITY baselines and evidence-manifest contract.
```
