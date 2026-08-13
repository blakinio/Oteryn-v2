# GAME-ABILITY-01 — Reference Mechanic Catalogue Entry and Parity-Fixture Binding Contract

- Status: **CANDIDATE PARTIAL BASELINE / GAME-ABILITY-01 REMAINS OPEN**
- Date: 2026-08-13
- Runtime/client/protocol/DDL/Platform/production authority: **NONE**

## Decision

A Reference Mechanic Catalogue entry is a catalogue-local evidence/provenance record. It binds one concrete mechanic to accepted GAME-ABILITY semantic surfaces, canonical Reference evidence-manifest cases, exact behavior-affecting revisions and bounded parity fixtures.

It is not executable content, a runtime entity, protocol discriminator, effect-family definition or independent parity authority. Catalogue presence never proves Reference behavior and never promotes parity.

```text
catalogue-local mechanic key
+ immutable Reference target context
+ evidence-manifest case references
+ exact semantic revision bindings
+ effect-family composition
+ owning-domain integration references
+ parity-fixture bindings
+ implementation linkage
+ projection of evidence / implementation / parity state
```

## Identity boundary

The mechanic key is stable only inside the catalogue/provenance layer. It must not become a new foundation ID, runtime occurrence ID, protocol opcode, database ownership token or cross-domain fence.

Exact physical representation is deferred. A later format must guarantee uniqueness within a catalogue revision and stability across non-semantic editorial changes.

## Evidence binding

Every in-scope Reference entry binds the accepted immutable Reference target and one or more canonical manifest case IDs when such cases exist.

The catalogue references or projects the manifest classification; it does not duplicate or override it.

- no mechanic case => explicit evidence gap;
- `UNKNOWN` => fail closed / parity pending evidence;
- `CONFLICT` => fail closed / parity conflict;
- uncleared provenance blocks promotion;
- OTS implementations remain hypothesis input only;
- later upstream behavior cannot silently rewrite the accepted Reference target.

If one mechanic depends on several claims, all relevant manifest cases remain visible; conflicting cases may not be collapsed into an optimistic summary.

## Behavior-affecting revision graph

As applicable, an entry must bind exact revisions for:

- Ability/Mechanic Definition;
- targeting and legality policy;
- cast/channel/interruption policy;
- cost/reservation/commit-anchor policy;
- cooldown and charge policy;
- condition policy;
- effect-family composition;
- damage/heal formula composition;
- SIM numeric/RNG semantics and named RNG purposes;
- DUR-04 script profile/artifact when used;
- ruleset/profile;
- owning-domain integrations.

A parity fixture that exercises behavior with a missing required revision binding is invalid. Retry/replay may not silently substitute a newer incompatible revision.

## Effect and domain ownership

Catalogue metadata creates no mutation authority. Core Effect Families remain governed by accepted GAME-ABILITY contracts. Cross-domain consequences remain with their owning domains.

In particular, item/currency/loot/conserved value stays under `GAME-ITEM` / `DUR-03`; movement stays under world/movement ownership; entity lifecycle stays with its authoritative owner; AI state stays under `GAME-AI-01` when accepted; world interaction stays under its owning interaction/world contracts.

Generic authoritative state patches, hidden event-bus mutation, direct script mutation and invented global transaction ownership are forbidden.

If a mechanic needs stronger cross-domain atomicity than accepted owner contracts provide, that integration requirement remains explicit and parity stays fail closed for outcomes that depend on it.

## Parity-fixture binding

One parity fixture binds one bounded observable scenario and must be able to identify:

```text
fixture key
+ catalogue mechanic key
+ manifest case refs
+ Reference target context
+ explicit preconditions
+ normalized invocation/origin context
+ exact behavior-affecting revisions
+ expected observable outcomes
+ allowed non-semantic presentation differences
+ exact Oteryn implementation revision
+ fixture/test locator
+ result
```

A fixture proves only its declared observable scenario on its exact implementation revision. A passing scenario does not imply parity for unrelated targeting, interruption, cost timing, cooldown, stacking, RNG, cross-domain or edge-case behavior.

`PARITY_CONFIRMED` may be exposed only when the canonical manifest permits it and all required target evidence, cleared provenance, exact implementation revision, exact semantic revision bindings, passing fixture evidence and absence of unresolved required conflicts are present.

## Unknown/conflict rule

Missing evidence or missing required revisions are never interpreted as zero, false, default order, latest revision or implementation-defined behavior. Unresolved range/LoS/order/timing/formula/RNG/domain-integration semantics remain fail closed.

## Reference and Evolved

Reference entries preserve the immutable accepted target. Evolved rulesets may reuse the mechanic key as provenance and declare a versioned difference, but must not rewrite Reference evidence in place.

Shared infrastructure does not imply shared exact targeting, timing, formula, condition, RNG or domain-integration semantics.

## Non-factual example shape

The following is deliberately illustrative only. It is not a real Reference mechanic, evidence case or parity claim.

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

## Future physical-schema validation

A later physical schema must reject at least duplicate local keys, unknown manifest references, parity-confirmed projections inconsistent with the canonical manifest, parity claims without exact implementation revision and passing fixture evidence, missing behavior-affecting revision bindings, generic state patches, unowned cross-domain mutation, catalogue keys used as runtime/protocol/global identity and silent defaults for `UNKNOWN`/`CONFLICT`.

Physical format, serializer, generated indexes and digest tooling remain deferred.

## Required analysis

**Problem:** mechanic-level evidence and parity fixtures need one binding contract before catalogue population, otherwise executable content and passing tests can be mistaken for Reference truth.

**Constraints:** immutable Reference target; independent evidence/implementation/parity axes; typed Effect Plan; accepted targeting/legality, lifecycle, cooldown/condition, damage/heal and effect-family boundaries; domain conservation/ownership; fail-closed unknowns; no runtime authority.

**Options:**

- **A — thin catalogue index + exact revision/fixture bindings — SELECTED.** One evidence authority, explicit provenance and no duplicate truth.
- **B — duplicate evidence inside catalogue — REJECTED.** Creates classification drift.
- **C — executable content doubles as catalogue/parity record — REJECTED.** Conflates implementation with truth.
- **D — fixture-only registry — REJECTED.** Weak mechanic identity, migration and auditability.

The selected model costs explicit revision bookkeeping but prevents false parity, stale-revision replay and hidden ownership violations.

## Decision timing

**Must decide now: YES.** First reviewed `ABILITY_COMBAT` mechanic cases, representative parity fixtures, Studio linking and later AI/interaction integration need this boundary.

**Blocked without it:** mechanic-level manifest population, bounded parity fixtures and evidence-driven GAME-ABILITY closure.

**Harder later:** evidence classes, implementation revisions and parity claims become duplicated across content and tests.

**Supersession evidence:** representative packages show the graph is insufficient or excessively complex; tooling/Studio evidence shows unacceptable authoring burden; replay/provenance failures; repeated cross-domain cases prove another integration boundary is needed.

## Deliberately not decided

No actual Reference mechanic entries, exact spells/values/formulas/RNG probabilities, manifest case population, catalogue JSON/RON/YAML schema, physical IDs, fixture file format/runner, runtime loader, protocol/client UI, persistence/DDL, cross-domain transaction protocol or production rollout are decided here.

Unresolved Reference-sensitive behavior remains fail closed.

## Current status

```text
GAME-ABILITY-01 -> REQUIRED_FOR_ALPHA / OPEN
candidate -> catalogue entry = local key + canonical evidence refs + exact revision graph + bounded fixture bindings
candidate -> catalogue presence never upgrades evidence or parity
candidate -> missing evidence/revisions/domain atomicity fail closed
next after acceptance -> add reviewed representative ABILITY_COMBAT evidence cases and parity fixtures without runtime authority
```
