# OTV2-20260808-reentry-pve-protection — archived

```yaml
task_id: OTV2-20260808-reentry-pve-protection
title: Freeze four-second defensive PvE re-entry protection
mode: ARCHITECTURE_ONLY
status: complete
repository: blakinio/Oteryn-v2
coordination_id: OTV2-NATIVE-FOUNDATION
base_sha: 19756eab0a66db37cb6f27ec367aaf2e4986df69
delivery_pr: 96
delivery_exact_head: ddf62ec48443fb4ce119eed0900662e222a99726
delivery_squash_merge: 496f0b9ad5231d24325e937a3f09ba221cf5c86b
completed_at: 2026-08-08T18:55:00+02:00
ownership_released: true
next_gate: FND-03
```

## Outcome

The owner-accepted disconnect/re-entry clarification is complete at the architecture level and canonical on `main`.

Canonical deliverables:

- `docs/architecture/DISCONNECT_REENTRY_PVE_PROTECTION_OWNER_DECISION.md`;
- `docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_OWNER_DIRECTION.md`;
- `docs/architecture/DISCONNECT_CLIENT_OS_FORENSICS_PRIVACY_TIMING_REFINEMENT.md`;
- synchronized `docs/architecture/FOUNDATION_PROGRAMME_CURRENT_STATUS.md`.

The accepted package freezes exactly four seconds of defensive PvE protection after valid recovery from unexpected loss of playable control, excludes ordinary graceful logout/login from that benefit, permits movement/self-heal/health and mana/resource potions under normal legality and costs, prohibits outgoing PvE offense and healing another player during the window, and never buffers prohibited outgoing actions for execution after expiry.

The package preserves same-actor continuity, session-generation fencing, one-character-per-account, combat/PZ/logout obligations, committed effects, threat/aggro and anti-duplication invariants. It does not authorize runtime implementation.

For disconnect forensics, server-generated gameplay/liveness/runtime evidence remains authoritative. Client/OS/Launcher/Guardian evidence is optional corroborating diagnostics. Automatic client-originated incident-capsule upload remains governed by the existing global client-diagnostics opt-out, and opt-out or missing client evidence is not adverse evidence.

Launcher/Guardian is preserved only as an extension point. A separate process is not required by the foundation architecture, and a direct Guardian heartbeat remains separately gated by purpose, privacy, security, resource and measurement evidence.

## Exact-head validation evidence

Delivery exact head: `ddf62ec48443fb4ce119eed0900662e222a99726`.

- Agent governance run `31268053954`: `PASS`;
- Dependency review run `31268053946`: `PASS`;
- CodeQL run `31268053944`: `PASS`;
- exact-head continuation architecture audit review `4889231397`: `PASS`, zero open material findings;
- unresolved review threads: `0`;
- changed-file scope: exactly five declared task/architecture/status files;
- runtime/component/integration/E2E execution: `NOT_APPLICABLE` for this documentation-only architecture delivery;
- squash merge: `496f0b9ad5231d24325e937a3f09ba221cf5c86b`.

## Material findings resolved before acceptance

1. **Client diagnostics privacy boundary** — the earlier forensic direction could be read as allowing Launcher/Guardian/OS diagnostic transmission to bypass the existing global client-diagnostics opt-out. The final package explicitly prohibits such a bypass and preserves missing/opted-out evidence as non-adverse.
2. **Current-status transition safety** — the earlier current-status text would have become stale immediately after merge by retaining `PR #96 VALIDATING` and a self-referential merge-next step. The final wording is correct both while the PR is open and after it is merged.
3. **Premature Launcher/Guardian concretization** — the final package preserves an independent observer capability boundary without requiring a separate executable/process, specific privilege model, transport or heartbeat before evidence justifies those choices.

No material finding remained at merge.

## Supersession boundary

The package narrowly supersedes only the older generic reconnect wording that prohibited any protection/invulnerability window, for the exact four-second PvE defensive re-entry interval defined by the delivered decision.

It does not supersede the underlying anti-reset, session-fencing, account/character concurrency, combat/PZ/logout, durable-state or anti-duplication invariants.

The privacy/timing refinement preserves rather than supersedes `CLIENT_CRASH_DIAGNOSTICS_PRIVACY_OWNER_BASELINE.md`, `DISCONNECT_FORENSIC_EVIDENCE_OWNER_BASELINE.md`, ADR-0006 and the architecture decision-discipline policy.

## Cross-repository disposition

No external repository was modified by this task.

`blakinio/Oteryn-Platform`, `blakinio/Otheryn` and `blakinio/otclient` remained read-only. Any future Platform reconciliation, native client diagnostic implementation or production telemetry change requires its own separately authorized task/branch/PR and rollout contract.

## Next action

`FND-03` is the next ordered foundation gate.

It must define the authoritative Rust runtime execution contract while consuming the delivered disconnect/re-entry authority, timing and forensic boundaries and without redefining accepted FND-02 wire semantics or prematurely selecting a concrete Launcher/Guardian design.
