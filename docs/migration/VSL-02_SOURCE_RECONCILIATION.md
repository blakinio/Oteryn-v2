# VSL-02 Source Reconciliation

- Status: normative evidence for `VSL-02`
- Reconciliation date: 2026-08-06
- Coordination ID: `OTV2-RUST-CLIENT-CUTOVER-20260806`
- Source repository: `blakinio/otclient`
- Source subtree: `oteryn-client/`
- FND-01 inventory revision: `c923ad8a1dff17b4933a6110931b0823cec2c590`
- Verified source `main`: `c923ad8a1dff17b4933a6110931b0823cec2c590`
- Result: no source drift

## 1. Reconciliation conclusion

The exact source commit inventoried by FND-01 is still the live default-branch head. Therefore `VSL-02` pins the cutover source to:

```text
blakinio/otclient@c923ad8a1dff17b4933a6110931b0823cec2c590
subtree: oteryn-client/
```

There is no commit delta to reconcile between FND-01 inventory and VSL-02 cutover selection. A later change to `oteryn-client/**` does not amend the selected source; it blocks the destination migration until an owner-approved VSL-02 amendment updates the source SHA and every affected path/provenance/dependency record.

## 2. Immutable source identifiers

```yaml
root_manifest_blob: 037013e8e4a762a65f0f2a30f7761ee14725a3fc
root_lockfile_blob: 2143408c12c50132883890f0821278320a331fde
crates_tree: c2a5426f764bab0f3a89de3e5a03e88a7f111c20
source_readme_blob: 62f49edd5aa584982ebf31339cc72e2ed8a74b0b
source_agents_blob: 3422f3af440456d16c70df92064ad06fdbf02659
```

These identify evidence; they do not imply that manifests, lockfiles, README or source governance are copied unchanged.

## 3. Open source pull requests

| PR | Lane | Rust subtree impact | Cutover decision |
|---:|---|---|---|
| #23 — Oteryn login shell prototype | legacy C++/Lua/OTUI | none | excluded from Rust migration; may continue only as legacy-client work |
| #48 — official Tibia Linux package analysis | operational/proprietary package analysis | none | reference-only operational branch; never imported or used as distributable asset provenance |
| #97 — configured release archive verification | legacy asset installer/security | none | excluded from Rust migration; may continue independently for the legacy client |

None owns or changes `oteryn-client/**`. No open Rust-client PR must be merged, cherry-picked or restacked before cutover.

The destination migration must not wait for those PRs unless one later changes a path explicitly listed in this contract. The later source-marker PR must not close or rewrite them merely because the Rust subtree moved.

## 4. Active source task records

| Task | Actual lane/state | Cutover decision |
|---|---|---|
| `OTC-20260712-client-test-foundation` | legacy C++/Lua tests; old PR #3 handoff | excluded; stale lifecycle cleanup belongs to the legacy repository |
| `OTC-20260714-protocol-session-reentrancy` | legacy C++/Lua protocol lifecycle; old PR #9 | excluded; stale lifecycle cleanup belongs to the legacy repository |
| `OTC-20260721-oteryn-identity-login` | merged legacy C++/Lua auth implementation | historical evidence only; not a Rust migration input |
| `OTC-20260724-validation-cost-policy` | repository governance; old PR #19 | excluded; stale lifecycle cleanup belongs to repository governance |
| `OTC-20260802-agent-governance-sync` | completed and merged but left under `active/` | excluded; generic source governance cleanup |
| `OTC2-20260803-playability-p2-canary-world-protocol` | Rust `protocol-canary` implementation record | reference-only; archive in the post-destination source-marker PR |

The stale records do not grant active ownership over the destination. The Canary task cannot block omission of `protocol-canary`, because ADR-0008 and accepted FND-01 classify that package as `REFERENCE_ONLY`.

## 5. Source freeze

The following administrative freeze becomes effective when the `VSL-02` contract merges:

```text
blakinio/otclient/oteryn-client/**
```

After that point:

- no new feature, refactor, protocol, dependency, formatting or documentation work is accepted in the Rust subtree;
- open legacy C++/Lua work outside the subtree is unaffected;
- the source remains intact and buildable as immutable migration evidence until the later marker PR;
- no bidirectional sync or dual-canonical development period is allowed.

Only an owner-approved critical security correction or a build correction required to complete the cutover may amend the frozen subtree. Such an exception requires a new exact source SHA, affected-path reconciliation, regenerated manifests, fresh audit and explicit owner-approved VSL-02 amendment before destination merge.

## 6. Destination implementation preflight

Before opening or updating the atomic implementation PR, the migration task must prove:

1. source `main` still equals `c923ad8a1dff17b4933a6110931b0823cec2c590`;
2. the selected subtree tree/blob identifiers remain reachable;
3. no open source PR changes `oteryn-client/**`;
4. no new active source task claims a migratable Rust path;
5. destination `main` has no competing Cargo workspace/client import;
6. FND-01 and VSL-02 contracts are present on destination `main`.

Failure of any check stops the import. The task may not silently select a newer source head.

## 7. Later source-marker PR

A separate, owner-authorized task in `blakinio/otclient` runs only after the verified destination implementation merge. It uses the same coordination ID and changes exactly the source ownership state, not Rust runtime code.

Required source-marker scope:

```text
oteryn-client/README.md
oteryn-client/AGENTS.md
oteryn-client/MOVED_TO_OTERYN_V2.md
docs/agents/tasks/active/OTC2-20260803-playability-p2-canary-world-protocol.md
docs/agents/tasks/archive/OTC2-20260803-playability-p2-canary-world-protocol.md
one source-marker task record
```

Required behavior:

- `README.md` begins with a prominent non-canonical/moved notice and exact destination merge commit;
- `AGENTS.md` begins with a highest-priority freeze rule forbidding new implementation in this subtree and points to destination governance;
- `MOVED_TO_OTERYN_V2.md` records source SHA, destination merge, path/provenance manifests and rollback coordination;
- the stale Rust/Canary task is archived as reference-only, with no claim that Canary moved into the destination;
- source code, commits and legal evidence remain present;
- legacy root C++/Lua client ownership is not changed.

The marker PR must not delete the subtree, rewrite history, close unrelated legacy PRs, or claim that the destination preserves cross-repository Git ancestry.

## 8. Canonical ownership transitions

```text
Before destination merge:
  otclient/oteryn-client = canonical Rust source
  Oteryn-v2 = architecture-only destination

After destination merge, before source marker:
  Oteryn-v2 = canonical Rust implementation
  otclient/oteryn-client = intact frozen historical source

After source marker:
  Oteryn-v2 = canonical Rust implementation
  otclient/oteryn-client = explicitly moved/non-canonical historical source
```

At no point may both repositories accept normal Rust-client development. At no point may neither repository be identified as canonical.

## 9. Reconciliation verdict

```yaml
source_drift: none
open_rust_prs: 0
material_source_ownership_conflicts: 0
cutover_source_sha: c923ad8a1dff17b4933a6110931b0823cec2c590
result: PASS
```
