# GAME-ABILITY-01 — Reference Mechanic Catalogue Entry and Parity-Fixture Binding Contract

- Status: **CANDIDATE PARTIAL BASELINE / GAME-ABILITY-01 REMAINS OPEN**
- Date: 2026-08-13
- Runtime/client/protocol/DDL/Platform/production authority: **NONE**

## Decision

A Reference Mechanic Catalogue entry is a catalogue-local provenance record that binds one concrete mechanic to accepted GAME-ABILITY semantics, the applicable versioned Reference evidence manifest, exact behavior-affecting revisions and bounded parity fixtures.

It is not executable content, a runtime identity, protocol discriminator, effect-family definition or independent parity authority. Catalogue presence never proves Reference behavior and never promotes parity.

The current `REFERENCE_EVIDENCE_PARITY_MANIFEST_CONTRACT.md` is still `CANDIDATE / NOT ACCEPTED`. This contract aligns with its current axes but does **not** promote that manifest contract or schema. A future physical catalogue must pin an accepted manifest/schema revision before parity confirmation is possible.

## Required binding

Each entry must be capable of carrying:

```text
catalogue-local mechanic key
+ immutable Reference target context
+ manifest case references
+ exact behavior-affecting revision references
+ effect-family composition
+ owning-domain integration references
+ parity-fixture references
+ exact implementation linkage
```

The mechanic key is local to catalogue/provenance. It must not become a foundation ID, runtime occurrence ID, protocol opcode, persistence ownership token or cross-domain fence.

## Evidence and parity

The catalogue references or projects classification from the applicable manifest revision; it does not duplicate or override it.

- no mechanic-level manifest case => explicit evidence gap;
- `UNKNOWN` => fail closed / parity pending evidence;
- `CONFLICT` => fail closed / parity conflict;
- uncleared provenance blocks promotion;
- OTS implementations remain hypothesis input only;
- later upstream behavior cannot silently rewrite the accepted immutable Reference target.

`PARITY_CONFIRMED` is allowed only after an accepted manifest/schema revision exists and the relevant manifest case permits it with sufficient target evidence, cleared provenance, exact Oteryn implementation revision and passing fixture/test evidence.

## Revision graph

As applicable, the entry binds exact revisions for Ability/Mechanic Definition, targeting, legality, cast/channel/interruption, cost/reservation/commit anchors, cooldown/charges, conditions, effect composition, damage/heal formula composition, SIM numeric/RNG semantics and named RNG purposes, DUR-04 script profile/artifact, ruleset/profile and owning-domain integrations.

A fixture that exercises behavior with a missing required revision binding is invalid. Retry/replay may not silently substitute a newer incompatible revision.

## Ownership

Catalogue metadata creates no mutation authority. Effect Families remain governed by GAME-ABILITY. Cross-domain consequences remain with their owning domains. Conserved item/currency/loot value remains under `GAME-ITEM` / `DUR-03`.

Generic state patches, direct script mutation, hidden event-bus mutation and invented global transaction ownership are forbidden. If stronger cross-domain atomicity is required but not yet accepted, the requirement stays explicit and dependent parity remains fail closed.

## Parity fixture

One fixture binds one bounded observable scenario. It must be able to name the fixture key, catalogue mechanic key, manifest cases, Reference target, preconditions, normalized invocation/origin context, exact semantic revisions, expected observable outcomes, exact Oteryn implementation revision, fixture/test locator and result.

Passing one scenario proves only that declared scenario on that exact implementation revision. It does not imply parity for unrelated targeting, interruption, cost timing, cooldown, condition, RNG, cross-domain or edge-case behavior.

## Non-factual example

This shape is illustrative only and is not a real Reference mechanic, evidence case or parity claim:

```yaml
catalogue_mechanic_key: example.non_reference.training_pulse
manifest_case_refs: []
classification_projection:
  target_evidence: UNKNOWN
  implementation_state: NOT_STARTED
  parity_status: PARITY_PENDING_EVIDENCE
revision_bindings: {}
effect_families: []
owning_domain_integrations: []
parity_fixtures: []
```

## Future schema validation

A later physical schema must reject duplicate local keys, unknown manifest references, parity projections inconsistent with the pinned accepted manifest revision, parity claims without exact implementation revision and passing fixture evidence, missing required semantic revision bindings, generic state patches, unowned cross-domain mutations, catalogue keys reused as runtime/protocol/global identity and silent defaults for `UNKNOWN` or `CONFLICT`.

Physical JSON/RON/YAML choice, serializer, generated indexes, digest tooling and fixture runner remain deferred.

## Required analysis

**Problem:** mechanic-level evidence and fixtures need one binding contract before catalogue population so executable content and passing tests cannot be mistaken for Reference truth.

**Constraints:** immutable Reference target; separate evidence/implementation/parity axes; accepted typed Effect Plan, targeting/legality, lifecycle, cooldown/condition, damage/heal and effect-family boundaries; domain ownership/conservation; fail-closed unknowns; candidate manifest status; no runtime authority.

**Options:** thin catalogue index + exact revision/fixture bindings is selected. Duplicating evidence in the catalogue, combining executable content with parity metadata, or using only an unstructured fixture registry are rejected because they create duplicate truth, implementation/evidence conflation or weak auditability.

**Must decide now: YES.** First reviewed `ABILITY_COMBAT` mechanic cases, representative parity fixtures, Studio linking and later AI/interaction integration need this boundary.

**Blocked without it:** mechanic-level evidence population, bounded parity fixtures and evidence-driven GAME-ABILITY closure.

**Supersession evidence:** representative mechanic packages show the graph is insufficient or excessive; Studio/tooling evidence shows unacceptable authoring cost; replay/provenance failures; repeated cross-domain cases prove a different integration boundary is needed.

## Deliberately not decided

No actual Reference mechanic entries, exact spell values/formulas/RNG probabilities, manifest case population, physical catalogue schema, IDs, fixture format/runner, runtime loader, protocol/client UI, persistence/DDL, cross-domain transaction protocol or production rollout are decided here.

Unresolved Reference-sensitive behavior remains fail closed.

## Current status

```text
GAME-ABILITY-01 -> REQUIRED_FOR_ALPHA / OPEN
candidate -> local catalogue key + versioned manifest refs + exact revision graph + bounded fixture bindings
candidate -> catalogue presence never upgrades evidence, manifest acceptance or parity
next -> accept/pin the evidence-manifest revision, then add reviewed representative ABILITY_COMBAT cases and fixtures without runtime authority
```
