# OTV2-20260805-agent-governance-bootstrap

```yaml
task_id: OTV2-20260805-agent-governance-bootstrap
title: Establish Oteryn v2 agent governance
mode: GOVERNANCE
status: validating
repository: blakinio/Oteryn-v2
base_branch: main
branch: docs/agent-governance-foundation
pr: null
base_sha: 93f6bd8ca20b46f9ddf7ea3d7d339b41ced16d2d
head_sha: null
owner: ChatGPT
created_at: 2026-08-05T08:06:00+02:00
updated_at: 2026-08-05T08:06:00+02:00
execution_budget_minutes: 60
owned_paths:
  - AGENTS.md
  - AGENTS.override.md
  - README.md
  - docs/agents/**
  - tools/agents/**
  - .github/workflows/agent-governance.yml
public_contracts:
  - docs/agents/GOVERNANCE_CONTRACT.json
depends_on: []
blocks: []
external_repositories:
  - blakinio/Oteryn-Platform (read-only policy source)
  - blakinio/Otheryn (read-only policy source)
  - blakinio/otclient (read-only policy source)
```

## Outcome

Adopt a reviewed Oteryn v2-specific governance system derived from the mature common policy baseline without copying Laravel, C++, Canary, legacy OTClient or trading-specific assumptions.

## Acceptance criteria

- [x] Root write allowlist and product architecture are Oteryn v2-specific.
- [x] Common autonomy, trust, recovery, closeout and prompt policies are represented.
- [x] Rust, multichannel, protocol-oteryn and cross-repository boundaries are explicit.
- [x] Machine-readable governance and project lanes exist.
- [x] Task template and lifecycle directories exist.
- [ ] Governance validator passes on exact final head.
- [ ] GitHub Actions exact-head governance check passes.
- [ ] Independent audit reports zero open material findings.
- [ ] PR is merged and this record is archived.

## Excluded scope

No Rust workspace/bootstrap, gameplay implementation, production deployment, external repository write or modification of accepted architecture.

## Context checkpoint

```yaml
last_progress: governance policy tree prepared from reviewed source repositories
status: validating
branch: docs/agent-governance-foundation
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
next_action: commit the complete governance tree and open its pull request
```
