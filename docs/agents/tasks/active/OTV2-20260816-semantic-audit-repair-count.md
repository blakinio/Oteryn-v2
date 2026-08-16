# OTV2-20260816-semantic-audit-repair-count

```yaml
task_id: OTV2-20260816-semantic-audit-repair-count
title: Semantic audit repair-count generalization
mode: TOOLING_GOVERNANCE
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: fix/architecture-semantic-audit-repair-count
owner: ARCHITECTURE_COORDINATOR
created_at: 2026-08-16
updated_at: 2026-08-16
owned_paths:
  - tools/architecture/semantic_contract_audit.py
  - docs/agents/tasks/active/OTV2-20260816-semantic-audit-repair-count.md
implementation_authority: TOOLING_ONLY
merge_authority: ARCHITECTURE_COORDINATOR_ONLY
owner_funded_ai_authorized: false
```

## Goal

Repair the deterministic semantic auditor's incorrect assumption that every owner-overridden architecture gate must remain exactly at repair cycle 4. The project owner authorized continued C/D/E/F repair beyond the normal three-cycle ceiling; a real F finding now requires cycle 5.

The auditor must remain fail closed: parse the declared stable-gate repair count, require it to be at least 4 for the current E/F profiles, require the durable owner-override evidence, preserve the no-Codex constraint, and reject malformed/missing repair history.

## Acceptance criteria

- [ ] no hard-coded equality to repair cycle 4;
- [ ] declared cycle is parsed as a positive integer and must be `>= 4`;
- [ ] owner override evidence remains mandatory;
- [ ] no-Codex and merge-authority checks remain mandatory;
- [ ] E profile and F profile semantic predicates are otherwise unchanged;
- [ ] exact-head self-review and repository CI pass;
- [ ] no Codex/owner-funded AI is used.

## Context checkpoint

```yaml
status: implementing
next_action: GENERALIZE_REPAIR_COUNT_CHECK_THEN_VALIDATE_AND_MERGE
```

`MERGE_AUTHORITY: ARCHITECTURE_COORDINATOR_ONLY`
`IMPLEMENTATION_AUTHORITY: TOOLING_ONLY`
