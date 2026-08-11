# GAME-CHAR-01 — Stage B Reference Evidence Delta 02

- Status: **PRE-DECISION EVIDENCE DELTA / NOT ACCEPTED**
- Date: 2026-08-11
- Gate: `GAME-CHAR-01` Stage B
- Reference target: **Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary**
- Trusted repository base: `blakinio/Oteryn-v2@1411994c70abbf065273c0502c88413b61ca5ca0`
- Supersedes: nothing; this is an additive delta to `GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_RECONCILIATION.md`
- Runtime authority: **NONE**
- Does not authorize: Stage-B acceptance, overall GAME-CHAR acceptance, runtime/client/protocol/persistence/content implementation, physical schema, production rollout or intentional Reference differences

## 1. Purpose

Reduce the remaining Stage-B evidence blockers using additional primary official Tibia evidence while preserving the accepted evidence discipline:

```text
target cut selected
!= every rule proven

current official documentation says X
!= July-28 target behavior was X

no discovered change note
!= proof that X did not change
```

This delta does not rewrite the historical #183 analysis. It records only new evidence, stronger or unchanged classifications, and one architecture-timing recommendation about which unresolved numeric formulas genuinely need to block durable schema design.

## 2. Executive result

### Can full Stage B close after this delta?

**NO.**

Material gaps remain in exact naming normalization/recycling, deletion target continuity, exact starter template, several target-sensitive death/PvP edges, exact offline-training effectiveness and some modern build interactions.

### Did the blocker set improve?

**YES.** New primary evidence materially strengthens:

1. global character-name namespace as a long-lived Tibia property;
2. promotion's level-20 + Premium core eligibility;
3. offline-training counter/state-machine semantics;
4. Twist of Fate and Adventurer's Blessing feature existence/world-type boundaries;
5. Wheel/Promotion Point character-build ownership;
6. Weapon Proficiency progress ownership;
7. separation of durable progression facts from formula implementation.

### Most important architecture finding

Exact gameplay formulas should not all be treated as physical-schema blockers merely because they are part of Reference behavior.

The project can safely separate:

```text
semantic fact ownership + version/migration envelope
from
exact ruleset arithmetic / fixture values
```

provided the durable contract does not encode guessed formulas or make later target-accurate rules impossible.

This is a **RECOMMENDATION**, not an accepted gate redefinition.

## 3. New primary evidence inventory

### E1 — global character-name namespace, official 2008

Official CipSoft article **Tibia Character Names - Now and in the Future**, 2008-04-02:

- states that more than seven million characters across 74 worlds each had a unique name;
- explicitly contrasts Tibia with games where uniqueness exists only per server;
- says players can rely on character names being truly unique.

Primary source:

- `https://www.tibia.com/news/?id=708&subtopic=latestnews`

The 2008-04-08 production patch then changed name-rule categories and technical limits without announcing a change to global uniqueness.

Primary source:

- `https://www.tibia.com/news/?id=716&subtopic=newsarchive`

Current creation documentation still treats name availability as one global character-creation concern but does not itself provide a dated July-28 namespace attestation.

Primary current source:

- `https://www.tibia.com/gameguides/?section=starting&subtopic=manual`

### E2 — active-character limit 25, official 2025

Official 2025 Monk rollout material first announced and then explicitly implemented the account active-character limit increase from 20 to 25.

Primary sources:

- `https://www.tibia.com/news/?id=8260&subtopic=latestnews`
- `https://www.tibia.com/news/?id=8307&subtopic=newsarchive`

Current official creation/account documentation continues to state 25 active characters.

This strengthens the already recorded before/after continuity case.

### E3 — promotion level 20 + Premium, official 2001 to current

Official 2001 release material introducing promoted vocations states that Premium players at or above level 20 can receive promotion.

Primary source:

- `https://www.tibia.com/news/?id=122&subtopic=newsarchive`

Current official character manual still requires:

- level at least 20;
- Premium;
- one-time 20,000 gp fee;
- and documents suspension/restoration when Premium expires/returns.

Current source:

- `https://www.tibia.com/gameguides/?section=characters&subtopic=manual`

Only the level-20 + Premium core has strong dated pre/post continuity in the gathered primary evidence. The exact 20,000 gp target continuity and current suspension details are not promoted to direct July-28 proof by this delta.

### E4 — offline-training counter mechanics, official 2012 to current

Official 2012 introduction material records:

- training begins only after at least 10 minutes offline;
- maximum 12 consecutive hours;
- each training second consumes one second from the character's pool;
- one second is restored for each second online;
- one second is restored for each second offline without training;
- a depleted pool can regenerate while still offline, but renewed training requires another activation;
- training is intentionally less effective than online training;
- vocation affects advancement;
- the exact advancement uses formulas not published in full there.

Primary source:

- `https://www.tibia.com/news/?id=2105&subtopic=newsarchive`

The 2012 release and bed extension corroborate persistence of the feature family:

- `https://www.tibia.com/news/?id=2125&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=2197&subtopic=newsarchive`

Current official FAQ/manual materially preserves the same timer/counter model.

### E5 — death/blessing base model, official 2009 onward

Official 2009 death-penalty redesign states:

- low-level unprotected base loss model;
- level-scaled reduction at higher levels;
- promotion reduces death penalty by 30%;
- each regular blessing reduces experience/skill loss by 8%;
- equipment-loss protection ladder 30/55/75/90/100% for 1/2/3/4/5 blessings.

Primary source:

- `https://www.tibia.com/news/?id=944&subtopic=newsarchive`

Current official manual materially retains the base experience/skill model and promotion/blessing reductions, while later features add world-type/PvP-specific edges.

### E6 — Twist of Fate and world-type specificity

Official PvP development/release history establishes Twist of Fate as a distinct PvP blessing and later explicitly documents world types where it is unavailable.

Primary sources include:

- `https://www.tibia.com/news/?id=2405&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=2946&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=4128&subtopic=newsarchive`

Official 2023 blessing-price changes explicitly say Twist of Fate itself was not adjusted, confirming continued feature existence before the selected target:

- `https://www.tibia.com/news/?id=7260&subtopic=newsarchive`

Official Character Bazaar entries with auction starts around 2026-07-28 10:42–10:44 CEST display `Twist of Fate active: yes/no` together with regular blessing counts. Because the public maintenance notice gives an expected rather than exact cryptographic resume time, these remain `OBSERVED / strong target alignment`, not unconditional minute-exact proof.

### E7 — Adventurer's Blessing, official 2014

Official 2014 production material states:

- it protects characters from PvP loss until level 21;
- it is lost if the character attacks another player;
- it is automatically granted to characters below level 21 without player kills in their history.

Primary source:

- `https://www.tibia.com/news/?id=2894&subtopic=newsarchive`

Current official manual/Quick Start materially retains the level-20/21 boundary and protection intent.

This is strong before/after continuity, but the delta still does not claim every July-28 PvP qualification edge is proven.

### E8 — Wheel of Destiny / Promotion Points are character build state

Official 2022 Wheel design says:

- from level 51, promoted Premium characters gain one Promotion Point per level;
- points are spent to specialise the character;
- each vocation has its own Wheel;
- allocations can be changed/reset under product rules.

Primary source:

- `https://www.tibia.com/news/?id=7013&subtopic=newsarchive`

Official 2023 preset material describes multiple Wheel setups belonging to the player's character workflow and allows setup import/export as configuration data:

- `https://www.tibia.com/news/?id=7336&subtopic=newsarchive`

Official 2026 fixes reference character promotion-point state, including a fix for excess Promotion Points granted through hunting tasks:

- `https://www.tibia.com/news/?id=8747&subtopic=newsarchive`

Current manual also describes permanent additional Promotion Points from character progression systems.

### E9 — Weapon Proficiency progress ownership is explicit

Official 2025 Weapon Proficiency design states directly:

- characters gain Proficiency Progress by killing monsters with the weapon equipped;
- **Proficiency Progress is bound to the character and cannot be transferred**;
- each weapon has its own proficiency tree/definition;
- Char Bazaar displays per-weapon proficiency progress.

Primary source:

- `https://www.tibia.com/news/?id=8421&subtopic=newsarchive`

Official 2026 Weapon Proficiency Update preserves the character-progress/weapon-definition split and makes dust character-bound while allowing weapon-specific tree modification:

- `https://www.tibia.com/news/?id=8850&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=8845&subtopic=newsarchive`

### E10 — current official Experience Table

CipSoft publishes a current exact total-experience-per-level table:

- `https://www.tibia.com/library/?subtopic=experiencetable`

This is strong evidence that experience total and level have a deterministic public relation **today**, but without target continuity evidence this delta does not relabel the full July-28 formula as `PROVEN`.

## 4. Revised evidence matrix

| Stage-B subject | Prior result | Delta result | Freeze-readiness consequence |
|---|---|---|---|
| Character-name namespace scope | `UNKNOWN` inside full naming contract | `DERIVED / strong historical continuity`: Tibia explicitly used globally unique character names across worlds; no target-day attestation gathered | **Strong architecture candidate**, but full naming contract still blocked |
| Exact normalization/case/space/repertoire | `UNKNOWN` | `UNKNOWN` | **NOT READY** |
| Name recycling / deleted-name hold | `UNKNOWN` | current official `>=6 months`, but target continuity still `UNKNOWN` | **NOT READY as Reference rule** |
| Active-character quota 25 | `DERIVED strong continuity` | stronger `DERIVED` via explicit 2025 production change + current manual | **Strong candidate** |
| Total active+deletion quota 30 | `UNKNOWN` | current-only primary evidence; target continuity still `UNKNOWN` | **NOT READY as Reference value** |
| Reversible deletion 60 days | `UNKNOWN` | current-only primary evidence; target continuity still `UNKNOWN` | **NOT READY as Reference value** |
| Promotion existence/titles | strong target evidence | unchanged/strengthened | **Strong candidate** |
| Promotion minimum level 20 | `UNKNOWN target continuity` | `DERIVED / very strong primary continuity` from 2001 + current | **Strong candidate rule** |
| Promotion Premium eligibility | `UNKNOWN target continuity` | `DERIVED / very strong primary continuity` from introduction + current | **Strong candidate rule** |
| Promotion cost 20,000 gp | current-only | remains `UNKNOWN` target continuity | **NOT READY as exact target value** |
| Promotion suspension on Premium lapse | current-only | remains `UNKNOWN` target continuity | **NOT READY as exact target edge** |
| Offline 10-minute activation | `DERIVED strong continuity` | strengthened | **Strong candidate rule** |
| Offline 12-hour max | `DERIVED strong continuity` | strengthened | **Strong candidate rule** |
| Offline pool drain/refill state machine | not fully elevated | `DERIVED / strong primary continuity` | **Strong semantic candidate** |
| Offline skill effectiveness/formulas | `UNKNOWN` | `UNKNOWN` | **Reference implementation blocker, not necessarily schema blocker** |
| Twist of Fate existence/state | partially unresolved | pre-target `PROVEN` existence + target-day `OBSERVED / strong alignment` | **Strong feature-existence candidate** |
| Twist exact PvP consumption/fair-fight edges | `UNKNOWN` | `UNKNOWN` | **NOT READY** |
| Adventurer's Blessing existence/core level rule | `UNKNOWN target continuity` | `DERIVED / strong primary continuity` from 2014 + current | **Strong candidate rule family** |
| World-type death exceptions | `UNKNOWN` | `PROVEN` that rules differ materially by world type; exact July-28 matrix incomplete | **Must be profile/world-type policy, not one universal Character formula** |
| Wheel Promotion Points / allocations ownership | boundary unresolved | `DERIVED / strong`: character-local build progression, entitlement-gated benefits | **Ownership candidate improved** |
| Weapon Proficiency progress ownership | boundary unresolved | **`PROVEN` by official design: character-bound and non-transferable** | **Ownership ready at semantic level** |
| Weapon Proficiency tree/perk definitions | boundary unresolved | weapon/ruleset/content definition, not Character-owned | **Boundary candidate improved** |
| Exact XP→level target formula | `UNKNOWN` | current exact table exists; July-28 continuity still `UNKNOWN` | **Reference fixture blocker; recommended not to block generic durable ownership** |
| Exact skill curves | `UNKNOWN` | `UNKNOWN` | **Reference fixture/ruleset blocker; recommended not to block generic durable ownership if representation remains formula-neutral** |

## 5. B1 naming — blocker reduced, not closed

### New conclusion

The **namespace scope** is no longer an evidence-free design choice. CipSoft explicitly documented cross-world global character-name uniqueness in 2008.

Classification for a July-28 contract:

- global name namespace: `DERIVED / strong historical continuity candidate`;
- exact target normalization/canonicalization: `UNKNOWN`;
- exact whitespace/case equivalence: `UNKNOWN`;
- exact permitted character repertoire and technical normalization pipeline: `UNKNOWN`;
- exact recycling/redirect/history semantics after delete/rename: `UNKNOWN`.

### Architecture consequence

A future Character Authority contract should prefer a **global canonical name namespace** unless contrary target evidence is found. However DUR-02 still must not freeze the physical unique-index normalization or collation from this evidence alone.

Current max-29/no-numbers/no-special-characters text is current evidence, not automatic target truth.

B1 remains **PARTIALLY OPEN**.

## 6. B2 deletion/quota — active quota stronger; timers still open

### Active quota

25 active characters has explicit pre-target production evidence and current continuity.

Classification: `DERIVED / strong continuity`.

### Still target-unproven

Current official account manual states:

- 60-day reversible deletion;
- total active + deletion-scheduled <= 30;
- deleted names unavailable for at least six months.

This delta did not locate a target-era dated primary source that establishes those exact values at July 28.

Therefore:

- 60 days: `UNKNOWN target continuity`;
- total 30: `UNKNOWN target continuity`;
- >=6-month deleted-name hold: `UNKNOWN target continuity`.

### Architecture consequence

The Stage-A lifecycle already prevents these values from blocking semantic lifecycle architecture:

```text
ACTIVE -> DELETION_SCHEDULED -> RETIRED
```

The exact durations/quotas should be represented as versioned Reference policy values rather than baked into lifecycle-state identity or database topology.

This is a **RECOMMENDATION**, not accepted policy.

## 7. B4 progression formulas — split ownership from arithmetic

### Evidence improvement

Current official sources provide:

- an exact Experience Table;
- public level/experience state on Character Bazaar;
- vocation-specific current HP/mana/capacity gains;
- target-era observable progression vocabulary;
- historical capacity migration evidence showing that at least some state cannot be assumed to be a pure function of level/vocation.

### Mandatory decision test

**Must exact XP/skill formulas be decided now for durable schema ownership?**

**RECOMMENDATION: NO**, provided the durable contract preserves:

1. authoritative total experience/progression facts;
2. authoritative skill/progression facts at sufficient precision/range;
3. explicit ruleset/profile revision context;
4. deterministic migration/versioning hooks;
5. no schema constraint that assumes an unproven formula;
6. exact formula/rounding fixtures before Reference behavior is implemented/claimed.

### Blocked downstream work if formulas stay unknown

- target-accurate Reference level/skill advancement implementation;
- deterministic parity fixtures;
- balance/simulation verification.

### Work that need not be blocked solely by unknown arithmetic

- identifying Character as owner of persisted XP/skill facts;
- bounded DUR-02 discovery for revision/fencing/transaction boundaries;
- formula-neutral storage envelope design.

### Owning later gates

Exact arithmetic should ultimately reconcile under the relevant ruleset plus `SIM-DETERMINISM-01`/gameplay gates before Reference implementation, even if Stage B freezes the semantic progression catalogue first.

### What would justify reversing this recommendation

Evidence that a formula choice changes identity, ownership, required transaction atomicity, irreversible physical representation or migration semantics would make the formula a DUR-02 prerequisite again.

## 8. B5 promotion — stable core split from commercial/value edges

### Strongly supported core

Promotion as a character build/profession transition with:

- level >=20;
- Premium eligibility;
- vocation-specific promoted title;

has very strong primary historical/current continuity.

Classification: `DERIVED / very strong continuity candidate`.

### Still not target-closed

- exact 20,000 gp fee continuity at July 28;
- exact Premium-expiry suspension/reactivation behavior at July 28;
- ownership boundary between durable promotion fact and entitlement projection when Premium is absent.

### Architecture recommendation

Store/own the **promotion achievement/state** as Character build state; treat whether benefits are currently active under Premium as ruleset/entitlement-derived eligibility rather than deleting promotion history when entitlement lapses.

This aligns with the current documented restoration behavior but remains a recommendation until target continuity/owner acceptance.

## 9. B6 death/PvP — feature existence stronger, edge matrix still open

### Twist of Fate

The feature existed well before target and official July-28-start Character Bazaar entries expose `Twist of Fate active: yes/no` alongside regular blessings.

Classification:

- existence/state field on normal target-era characters: `OBSERVED / strong target alignment` plus pre-target feature evidence;
- exact PvP qualification/consumption/fair-fight semantics: `UNKNOWN` for complete July-28 target contract.

### World-type boundary

Official history proves that some Retro PvP profiles deliberately remove Twist of Fate/fair-fight behavior. Therefore death/PvP rules cannot be one universal Character formula independent of world/ruleset profile.

This is a strong architecture constraint even before every target edge value is known.

### Adventurer's Blessing

2014 official release plus current manual provide strong continuity for the core protection family around the level-20/21 boundary.

Classification: `DERIVED / strong rule-family continuity`; full target edge contract remains open.

### Death Redemption

The feature existed before target, but public feature semantics changed over its lifetime. Do not infer current recovery-window/count semantics backward to July 28 without dated continuity evidence.

B6 remains **PARTIALLY OPEN**.

## 10. B7 offline training — counter semantics much closer to closure

### Strong semantic candidate

Official 2012 source specifies a real character-owned counter/state machine:

```text
activation chosen
-> at least 10 min offline before gain
-> consume one pool second per training second
-> maximum effective continuous training 12 h
-> regenerate one pool second per second online
-> regenerate one pool second per second offline without training
-> if depleted while offline, later offline time refills pool
-> using refilled pool requires reactivation
```

Combined with current continuity, classification is `DERIVED / strong primary continuity`.

### Still unknown

- exact July-28 effectiveness coefficients;
- exact selectable-skill matrix if it changed by vocation/features;
- exact rounding/tick implementation;
- loyalty/event/modifier interactions;
- migration edge cases.

### Architecture consequence

The existence of an explicit per-character offline-training pool/capability is a much stronger durable-state candidate than the unpublished advancement formula.

B7 should be split into:

- **semantic counter/capability ownership** — near freeze-ready;
- **target arithmetic/effectiveness** — still Reference/ruleset evidence-blocked.

## 11. B8 modern build-state ownership — materially reduced

### Wheel / Promotion Points

Primary official design consistently describes Promotion Points as character progression used to specialise that character. Presets are allocation configurations, not a separate economy authority.

Recommended semantic ownership:

```text
Character
owns earned Promotion Point facts
owns active/saved Wheel allocations/presets needed for gameplay
owns character-specific permanent bonus Promotion Point progression

ruleset/ability/content definitions
own perk catalogue, formulas, effects, compatibility

Platform/entitlement
owns Premium entitlement source
ruleset derives whether Premium-gated benefits are active
```

This is a **RECOMMENDATION**, not owner-accepted Stage-B policy.

### Weapon Proficiency

This ownership question is substantially stronger than before because CipSoft explicitly states Proficiency Progress is bound to the character and cannot be transferred.

Semantic boundary candidate:

```text
Character
owns per-weapon Proficiency Progress / reached progression state
owns character-selected proficiency choices where they are player state

a weapon ItemType / content definition
owns proficiency-tree definition, thresholds/perk definitions where definition-scoped

GAME-ITEM / DUR-03
owns concrete item instance conservation/location/value-transfer invariants
```

The character references a stable weapon-definition identity; it must not duplicate item-instance ownership into Character.

### Dust

Official 2026 material describes dust as character-bound. Its exact owner/value-conservation treatment crosses character progression and economy/item-resource semantics and should be reconciled with GAME-ITEM/DUR-03 rather than silently folded into this Stage-B delta.

### Remaining B8 gaps

- exact ownership of charms/Animus/task systems;
- permanent/additional slots with possible entitlement/product effects;
- exact migration/versioning of Wheel/proficiency definitions;
- whether every visible Bazaar field is authoritative Character state or a projection of another aggregate.

B8 remains **PARTIALLY OPEN**, but Weapon Proficiency progress ownership is no longer ambiguous.

## 12. Revised blocker classification

### Still hard blockers before a complete GAME-CHAR Stage-B owner package

1. **B1 normalization/recycling details** — global namespace is strong candidate, exact canonical name contract is not.
2. **B3 creation/starter template** — insufficient target-period primary evidence.
3. **B6 persistent death/PvP edge matrix** — world-type and blessing edge rules still incomplete.
4. **B8 residual modern-state ownership** — charms/Animus/tasks/slots and some migration boundaries remain open.

### Policy/evidence values that may remain versioned without blocking semantic ownership, if owner later accepts this split

1. B2 deletion duration/total quota/name-hold exact numeric values;
2. B4 exact XP/skill arithmetic;
3. B5 promotion fee and Premium suspension behavior;
4. B7 offline-training effectiveness coefficients.

These still block a **Reference parity implementation/release claim** when applicable. The recommendation is only that they need not automatically block every generic durable Character schema decision if the schema remains versioned, formula-neutral and migration-safe.

## 13. Impact on DUR-02

### Already accepted safe consumption

DUR-02 may continue bounded discovery using Stage-A invariants.

### New nonbinding recommendations from this delta

DUR-02 should preserve extension points for:

- global canonical name reservation without prematurely selecting normalization/collation;
- versioned deletion policy values rather than topology/state enums per duration;
- authoritative XP/skill facts independent from exact arithmetic implementation;
- persisted/derived distinction for migration-sensitive stats such as capacity;
- Character-owned offline-training pool/capability state;
- Character-owned Wheel/promotion-point state;
- Character-owned per-weapon proficiency progress keyed by stable weapon definition identity;
- profile/ruleset-scoped death/blessing semantics rather than one universal world-independent rule set.

None of this authorizes physical DDL or final schema.

## 14. Impact on later ruleset/SIM work

Before any target-accurate Reference implementation or `PARITY_CONFIRMED` fixture, later contracts still need exact evidence/formulas for the mechanics they execute.

The distinction is:

```text
DURABLE OWNERSHIP QUESTION
Who owns the authoritative fact and how is it versioned/fenced/migrated?

RULESET/SIM QUESTION
How does the target revision calculate, advance or transform that fact?
```

Conflating the two forces uncertain arithmetic into irreversible persistence design. Separating them must not be used as an excuse to ship unproven Reference behavior.

## 15. Decision timing

### Must full Stage B be accepted now?

**NO.**

### Must the formula-vs-schema split be accepted now?

**NO for this evidence-delta task.** It should be included in the eventual owner Stage-B closure package once the remaining ownership blockers are sufficiently reduced.

### What downstream work remains blocked?

- final character-bearing DUR-02 schema acceptance;
- broad Reference character implementation;
- target-accurate naming/creation/death fixtures;
- final GAME-CHAR Stage-B contract.

### What can continue safely?

- further historical primary evidence acquisition;
- bounded DUR-02 discovery under Stage A;
- GAME-CHANNEL / GAME-ITEM evidence architecture under separate ownership;
- SIM/ruleset formula evidence gathering;
- evidence-manifest/tooling design.

### What evidence would justify superseding this delta?

- target-period primary snapshots that directly prove or contradict current classifications;
- owner-provided target-era captures with provenance;
- accepted GAME-CHAR Stage-B owner baseline;
- evidence that an unresolved formula materially changes durable identity/ownership/atomicity/schema requirements.

## 16. Next evidence priorities

Priority order after this delta:

1. target-era official account/creation snapshots for B1/B2/B3;
2. target-era/current-continuity evidence for death/PvP blessing edges by world type;
3. primary ownership chronology for charms/Animus/Hunting Tasks/additional slots;
4. exact target progression/skill/offline formulas only where needed for Reference fixtures or where they prove to constrain durable representation;
5. assemble an owner Stage-B closure packet only after these residual ownership/semantic blockers are materially reduced.

## 17. Deliberately not decided here

- no Stage-B rule is owner accepted;
- no exact physical name index/collation;
- no 60-day/30/6-month Reference acceptance;
- no exact starter template;
- no exact XP or skill formula;
- no exact promotion price/entitlement transition target rule;
- no complete death/PvP matrix;
- no offline-training effectiveness formula;
- no final Wheel/Animus/charm/task/slot ownership contract;
- no DDL/runtime/protocol/content implementation.

Until an explicit owner decision is delivered, this document remains **PRE-DECISION EVIDENCE DELTA / NOT ACCEPTED** and does not change `GAME-CHAR-01 = PROPOSED / PLANNED / NOT_STARTED`.
