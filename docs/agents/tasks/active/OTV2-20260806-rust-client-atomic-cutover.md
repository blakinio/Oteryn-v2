# OTV2-20260806-rust-client-atomic-cutover

```yaml
task_id: OTV2-20260806-rust-client-atomic-cutover
title: Perform atomic Rust client cutover
mode: MIGRATION
status: implementing
repository: blakinio/Oteryn-v2
base_branch: main
branch: migrate/rust-client-cutover-c923ad8
pr: pending
base_sha: 33dc15dab82cfe5347e569036296204763270508
source_repository: blakinio/otclient
source_commit: c923ad8a1dff17b4933a6110931b0823cec2c590
source_subtree: oteryn-client/
source_subtree_tree: c0928dafca6df19ff11d7901e503ed85a5199439
coordination_id: OTV2-RUST-CLIENT-CUTOVER-20260806
owner: GPT-5.6-Thinking-migration-coordinator
created_at: 2026-08-06T10:32:00+02:00
execution_budget_minutes: 120
owned_paths:
  - Cargo.toml
  - Cargo.lock
  - rust-toolchain.toml
  - rustfmt.toml
  - deny.toml
  - workspace-boundaries.toml
  - apps/client/**
  - crates/foundation/**
  - crates/diagnostics/**
  - crates/client-runtime/**
  - crates/platform-contracts/**
  - crates/platform-client/**
  - crates/identity/**
  - crates/client-domain/**
  - crates/client-simulation/**
  - crates/input-actions/**
  - crates/input-platform/**
  - crates/renderer/**
  - crates/synthetic-assets/**
  - crates/test-support/**
  - tests/security/auth/**
  - tests/pre-native-client/**
  - tools/architecture-check/**
  - tools/synthetic-asset-compiler/**
  - tools/synthetic-client-harness/**
  - tests/fixtures/synthetic-assets/**
  - docs/migration/rust-client-provenance.json
  - docs/migration/rust-dependency-delta.json
  - docs/migration/rust-client-transformation-evidence.md
  - .github/workflows/rust.yml
  - docs/agents/tasks/active/OTV2-20260806-rust-client-atomic-cutover.md
public_contracts:
  - workspace-boundaries.toml
  - docs/migration/rust-client-provenance.json
  - docs/migration/rust-dependency-delta.json
depends_on:
  - FND-01 accepted and archived
  - VSL-02 merged as 824599bb2d696e15e22319007b4a919b4438f394
blocks:
  - source-marker task in blakinio/otclient
  - FND-ID-01
```

## Goal

Create and validate the complete 19-member Rust workspace in one destination PR, migrate or rewrite the selected client capabilities, preserve truthful provenance, keep production and synthetic closures separate, and expose a launchable pre-native client that fails closed before gameplay credentials, routing or transport.

## Acceptance criteria

- [ ] Exactly 19 workspace members exist and match FND-01.
- [ ] No Canary, protocol, gameplay transport, Game Session or speculative native crate is present.
- [ ] Production app and synthetic harness dependency closures are disjoint as required.
- [ ] Root toolchain, lockfile, formatting, deny and machine boundary policy exist.
- [ ] Platform and Identity use bounded cancellable async I/O on the application-owned Tokio runtime.
- [ ] Windows client launches a visible pre-native shell and cannot request gameplay entry.
- [ ] Linux shared crates compile, lint and test.
- [ ] Synthetic harness runs deterministic offline scenarios.
- [ ] Provenance, dependency delta and transformation evidence are complete.
- [ ] Required exact-head CI and independent audit pass with zero material findings.
- [ ] PR is squash-merged, destination main verified, task archived and ownership released.

## Excluded scope

- No write to blakinio/otclient in this task.
- No protocol-oteryn, protocol-canary, gameplay transport or Game Session implementation.
- No production deployment, live Identity/Gateway call or proprietary asset import.

## Context checkpoint

```yaml
status: implementing
head_sha: pending
pr: pending
last_progress: branch created from exact destination main and migration ownership claimed
blocker: none
next_action: create the complete 19-member workspace and retained validation workflow in one coherent implementation commit
```
