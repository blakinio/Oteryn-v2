# VSL-02 Source Reconciliation

- Status: normative evidence for `VSL-02`
- Reconciliation date: 2026-08-06
- Coordination ID: `OTV2-RUST-CLIENT-CUTOVER-20260806`
- Source repository: `blakinio/otclient`
- Source subtree: `oteryn-client/`
- Selected source commit: `c923ad8a1dff17b4933a6110931b0823cec2c590`
- Selected subtree tree: `c0928dafca6df19ff11d7901e503ed85a5199439`
- Result at reconciliation: no Rust-subtree drift

## 1. Reconciliation conclusion

The FND-01 inventory commit was still the live source default-branch head when VSL-02 started. The cutover therefore pins immutable content to:

```text
blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590
oteryn-client tree c0928dafca6df19ff11d7901e503ed85a5199439
```

The implementation always imports from that selected commit, not from a later mutable `main`.

A later source commit wholly outside `oteryn-client/**` is allowed and does not invalidate VSL-02. Cutover is blocked only when the current default branch resolves `oteryn-client/` to a tree other than `c0928dafca6df19ff11d7901e503ed85a5199439`, or a new PR/task claims the frozen Rust subtree.

Any authorized change to the subtree requires an owner-approved VSL-02 amendment with a new commit/tree, affected-path reconciliation, regenerated manifests and fresh audit before destination merge.

## 2. Immutable source identifiers

```yaml
cutover_commit: c923ad8a1dff17b4933a6110931b0823cec2c590
subtree_tree: c0928dafca6df19ff11d7901e503ed85a5199439
root_manifest_blob: 037013e8e4a762a65f0f2a30f7761ee14725a3fc
root_lockfile_blob: 2143408c12c50132883890f0821278320a331fde
crates_tree: c2a5426f764bab0f3a89de3e5a03e88a7f111c20
source_readme_blob: 62f49edd5aa584982ebf31339cc72e2ed8a74b0b
source_agents_blob: 3422f3af440456d16c70df92064ad06fdbf02659
```

These identify source evidence. They do not imply that manifests, lockfiles, README, governance or rewritten code are copied unchanged.

## 3. Open source pull requests

| PR | Lane | Rust subtree impact | Cutover decision |
|---:|---|---|---|
| #23 — Oteryn login shell prototype | legacy C++/Lua/OTUI | none | excluded; may continue as legacy-client work |
| #48 — official Tibia Linux package analysis | operational/proprietary package analysis | none | reference-only; never imported or treated as distributable provenance |
| #97 — release archive verification | legacy asset installer/security | none | excluded; may continue independently for the legacy client |

No open PR changes `oteryn-client/**`. No PR must be merged, cherry-picked or restacked into the selected Rust source before cutover.

A later merge of one of these PRs is harmless when it leaves the pinned Rust subtree tree unchanged. The source-marker PR must not close or rewrite unrelated legacy PRs.

## 4. Root source task records

| Task | Actual lane/state | Cutover decision |
|---|---|---|
| `OTC-20260712-client-test-foundation` | legacy C++/Lua tests; stale PR #3 handoff | excluded; legacy lifecycle cleanup |
| `OTC-20260714-protocol-session-reentrancy` | legacy C++/Lua protocol lifecycle; stale PR #9 | excluded; legacy lifecycle cleanup |
| `OTC-20260721-oteryn-identity-login` | merged legacy auth implementation | historical evidence only |
| `OTC-20260724-validation-cost-policy` | repository governance; stale PR #19 | excluded; governance lifecycle cleanup |
| `OTC-20260802-agent-governance-sync` | completed but left under `active/` | excluded; generic governance cleanup |
| `OTC2-20260803-playability-p2-canary-world-protocol` | Rust Canary implementation record | reference-only; archive in source-marker PR |

These records grant no destination ownership. The Canary task cannot block omission of `protocol-canary`, because ADR-0008 and FND-01 classify that package as `REFERENCE_ONLY`.

## 5. Nested Rust task conflict

The source subtree also contains:

```text
oteryn-client/docs/agents/tasks/active/
  OTC2-20260805-native-protocol-single-version-completion.md
```

That task proposed an independent `protocol-oteryn`, automatic dual-protocol selection and reuse of the source transport. Those instructions are superseded for the destination by ADR-0008, ADR-0011 and FND-01:

- Canary is not migrated as a production adapter;
- the initial destination has no gameplay transport or protocol crate;
- no empty/native placeholder or automatic protocol selection is created;
- FND-02 later owns the only native protocol contract.

The file remains immutable source evidence and is not imported. The post-destination source-marker PR archives it as `SUPERSEDED_REFERENCE_ONLY`, preserving links to its historical producer contracts without authorizing its runtime plan.

## 6. Source freeze

The administrative freeze becomes effective when VSL-02 merges:

```text
blakinio/otclient/oteryn-client/**
```

After that point:

- no feature, refactor, protocol, dependency, formatting or documentation work is accepted in the Rust subtree;
- legacy C++/Lua work outside the subtree is unaffected;
- the selected commit remains the only import source;
- the current source default branch may advance only without changing the pinned subtree tree;
- no bidirectional sync or dual-canonical Rust development is allowed.

An owner-approved critical security or cutover-build correction may amend the subtree only through a VSL-02 amendment as described above.

## 7. Destination implementation preflight

Before opening the atomic implementation PR and again before its merge, prove:

1. selected commit `c923ad8...` remains reachable;
2. its `oteryn-client/` tree equals `c0928daf...`;
3. current source default branch resolves `oteryn-client/` to `c0928daf...`;
4. no open PR changes `oteryn-client/**`;
5. no new active task claims a migratable Rust path;
6. destination `main` has no competing workspace/client import;
7. FND-01 and VSL-02 exist on destination `main`.

A failure stops the import. The implementation may not silently select a later source commit.

## 8. Later source-marker PR

A separate owner-authorized task in `blakinio/otclient` runs only after the verified destination implementation merge. It changes source ownership documentation and task lifecycle, not Rust runtime code.

Required scope:

```text
oteryn-client/README.md
oteryn-client/AGENTS.md
oteryn-client/MOVED_TO_OTERYN_V2.md

docs/agents/tasks/active/OTC2-20260803-playability-p2-canary-world-protocol.md
docs/agents/tasks/archive/OTC2-20260803-playability-p2-canary-world-protocol.md

oteryn-client/docs/agents/tasks/active/OTC2-20260805-native-protocol-single-version-completion.md
oteryn-client/docs/agents/tasks/archive/OTC2-20260805-native-protocol-single-version-completion.md

one source-marker task record
```

Required behavior:

- README begins with a prominent moved/non-canonical notice and exact destination merge;
- nested AGENTS begins with a highest-priority implementation freeze and destination pointer;
- `MOVED_TO_OTERYN_V2.md` records source commit/tree, destination merge, finalized manifests and rollback order;
- the Canary task is archived as reference-only;
- the nested native/dual-protocol task is archived as superseded reference-only;
- source code, commits and legal evidence remain present;
- root legacy C++/Lua ownership remains unchanged.

The marker PR must not delete the subtree, rewrite history, close unrelated legacy PRs or claim preserved cross-repository Git ancestry.

## 9. Canonical ownership transitions

```text
Before destination merge:
  otclient/oteryn-client = canonical frozen Rust source
  Oteryn-v2 = architecture-only destination

After destination merge, before source marker:
  Oteryn-v2 = canonical Rust implementation
  otclient/oteryn-client = intact frozen historical source

After source marker:
  Oteryn-v2 = canonical Rust implementation
  otclient/oteryn-client = explicitly moved/non-canonical evidence
```

At no point may both repositories accept normal Rust-client development. At no point may neither repository be identified as canonical.

## 10. Reconciliation verdict

```yaml
selected_source_commit: c923ad8a1dff17b4933a6110931b0823cec2c590
selected_subtree_tree: c0928dafca6df19ff11d7901e503ed85a5199439
rust_subtree_drift_at_reconciliation: none
open_rust_subtree_prs: 0
conflicting_source_tasks:
  - protocol-canary task: reference-only
  - nested dual/native task: superseded reference-only
material_source_ownership_conflicts: 0
result: PASS
```
