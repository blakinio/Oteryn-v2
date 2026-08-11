# GAME-CHAR-01 — Stage B Reference Evidence Delta 02

- Status: **PRE-DECISION EVIDENCE DELTA / NOT ACCEPTED**
- Date: 2026-08-11
- Gate: `GAME-CHAR-01` Stage B
- Reference target: **Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary**
- Trusted repository base: `blakinio/Oteryn-v2@1411994c70abbf065273c0502c88413b61ca5ca0`
- Supersedes: nothing; additive to `GAME-CHAR-01_STAGE_B_REFERENCE_EVIDENCE_RECONCILIATION.md`
- Runtime authority: **NONE**
- Does not authorize: Stage-B acceptance, overall GAME-CHAR acceptance, runtime/client/protocol/persistence/content implementation, physical schema, production rollout or intentional Reference differences

## 1. Purpose

Reduce Stage-B evidence blockers with additional primary official Tibia evidence while preserving the accepted evidence discipline:

```text
target cut selected
!= every rule proven

current official documentation says X
!= July-28 target behavior was X

no discovered change note
!= proof that X did not change
```

This delta does not rewrite the historical #183 reconciliation. It records only new evidence, revised classifications and architecture-timing recommendations.

## 2. Executive result

### Can full Stage B close after this delta?

**NO.**

Material gaps remain in exact naming normalization/recycling, target deletion values, exact starter template, several persistent death/PvP edges, exact offline-training effectiveness and a small residual set of modern-system ownership/migration details.

### What improved materially?

Primary official evidence strengthens:

1. global character-name namespace as a long-lived Tibia property;
2. active-character quota `25` continuity;
3. promotion level-20 + Premium core eligibility;
4. offline-training counter/state-machine semantics;
5. Twist of Fate and Adventurer's Blessing feature/world-type boundaries;
6. Wheel/Promotion Point character-build ownership;
7. Weapon Proficiency progress ownership;
8. charms/charm points, Hunting Task Points and permanent Hunting Task/Prey slots as character-specific state;
9. Animus Mastery as character-visible progression with strong character-specific alignment;
10. separation of durable fact ownership from exact arithmetic.

### Most important architecture finding

Exact gameplay formulas should not all be physical-schema blockers merely because they are part of Reference behavior.

```text
semantic fact ownership + version/migration envelope
!=
exact ruleset arithmetic / fixture values
```

If persistence remains formula-neutral, versioned and migration-safe, exact arithmetic may remain a Reference implementation/SIM fixture gate without forcing every numeric formula into `DUR-02` prerequisites.

This is a **RECOMMENDATION**, not an accepted gate redefinition.

## 3. New primary evidence inventory

### E1 — global character-name namespace

Official CipSoft article **Tibia Character Names - Now and in the Future** (2008-04-02) explicitly describes character names as unique across Tibia worlds, contrasting Tibia with games where uniqueness exists only per server.

Primary source:

- `https://www.tibia.com/news/?id=708&subtopic=latestnews`

The 2008-04-08 production patch changed technical naming rules without announcing a namespace-scope change:

- `https://www.tibia.com/news/?id=716&subtopic=newsarchive`

Current creation documentation still treats name availability globally, but is current-only evidence for detailed rules:

- `https://www.tibia.com/gameguides/?section=starting&subtopic=manual`

### E2 — active-character limit 25

Official 2025 Monk rollout material announced and implemented the account active-character limit increase from 20 to 25:

- `https://www.tibia.com/news/?id=8260&subtopic=latestnews`
- `https://www.tibia.com/news/?id=8307&subtopic=newsarchive`

Current official account/creation documentation still states 25 active characters.

### E3 — promotion level 20 + Premium

Official 2001 release material introducing promoted vocations states that Premium players at or above level 20 can be promoted:

- `https://www.tibia.com/news/?id=122&subtopic=newsarchive`

Current official character documentation still requires level >=20 and Premium and also currently states a one-time 20,000 gp fee plus Premium-lapse suspension/restoration behavior:

- `https://www.tibia.com/gameguides/?section=characters&subtopic=manual`

Only level-20 + Premium has the strong dated pre/post continuity established here. The exact 20,000 gp target continuity and suspension details remain target-unproven.

### E4 — offline-training counter mechanics

Official 2012 introduction material records:

- training begins only after at least 10 minutes offline;
- maximum 12 consecutive hours;
- each training second consumes one pool second;
- one pool second regenerates per second online;
- one pool second regenerates per second offline without training;
- depletion while offline may refill later, but using the refilled pool requires reactivation;
- training is deliberately less effective than online training;
- vocation affects advancement;
- full advancement formulas were not published there.

Primary sources:

- `https://www.tibia.com/news/?id=2105&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=2125&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=2197&subtopic=newsarchive`

Current official FAQ/manual materially preserves the counter/timing model.

### E5 — death/blessing base model

Official 2009 death-penalty redesign records the level-scaled experience/skill-loss family, 30% promotion reduction, 8% experience/skill-loss reduction per regular blessing, and the equipment-loss protection ladder 30/55/75/90/100% for 1/2/3/4/5 blessings:

- `https://www.tibia.com/news/?id=944&subtopic=newsarchive`

Current official documentation materially retains the base family while later systems/world types add edge rules.

### E6 — Twist of Fate and world-type specificity

Official PvP history establishes Twist of Fate and explicitly documents profiles/world types where Twist/fair-fight behavior is absent or different:

- `https://www.tibia.com/news/?id=2405&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=2946&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=4128&subtopic=newsarchive`

Official 2023 blessing-price material states Twist of Fate itself was not adjusted, supporting feature continuity before target:

- `https://www.tibia.com/news/?id=7260&subtopic=newsarchive`

Official Character Bazaar entries starting around the July-28 maintenance boundary expose `Twist of Fate active: yes/no` with regular blessing counts. Because the public maintenance notice provides an expected rather than cryptographically exact resume time, classify this `OBSERVED / strong target alignment`, not minute-exact target proof.

### E7 — Adventurer's Blessing

Official 2014 production material states it protects from PvP loss until level 21, is lost when attacking another player and is granted automatically under the documented low-level/no-player-kill conditions:

- `https://www.tibia.com/news/?id=2894&subtopic=newsarchive`

Current official docs materially retain the core protection family.

### E8 — Wheel / Promotion Points

Official 2022 Wheel design describes Promotion Points as progression used to specialise the character, with one point per level from level 51 for promoted Premium characters and vocation-specific Wheel definitions:

- `https://www.tibia.com/news/?id=7013&subtopic=newsarchive`

Official 2023 presets describe saved Wheel configurations:

- `https://www.tibia.com/news/?id=7336&subtopic=newsarchive`

Official 2026 fixes reference persistent character Promotion Point state, including excess points granted through hunting tasks:

- `https://www.tibia.com/news/?id=8747&subtopic=newsarchive`

### E9 — Weapon Proficiency progress ownership

Official 2025 Weapon Proficiency design states directly that **Proficiency Progress is bound to the character and cannot be transferred**. Each weapon has its own proficiency tree/definition and Character Bazaar exposes progress:

- `https://www.tibia.com/news/?id=8421&subtopic=newsarchive`

Official 2026 update preserves the character-progress/weapon-definition split and describes dust as character-bound:

- `https://www.tibia.com/news/?id=8850&subtopic=newsarchive`
- `https://www.tibia.com/news/?id=8845&subtopic=newsarchive`

### E10 — current official Experience Table

CipSoft currently publishes an exact total-experience-per-level table:

- `https://www.tibia.com/library/?subtopic=experiencetable`

This proves a deterministic public relation today. It does not by itself prove unchanged July-28 arithmetic.

### E11 — Character Bazaar transfer boundary for character-specific progression

Official Character Bazaar FAQ/launch material defines a transfer boundary between account-bound and **character-specific** state. Character-specific state includes, among other things:

- experience and skills;
- blessings;
- charms, charm points and charm expansion;
- Hunting Task Points;
- permanent Hunting Task slots;
- permanent Prey slots;
- daily reward streak;
- completed map areas;
- quest lines, titles, achievements and bestiary progress.

This is strong primary evidence that these are character-specific product state for transfer/ownership purposes. It does **not** prove they must all be fields of one physical Character row or one transaction aggregate.

Official source family:

- Character Bazaar announcement/FAQ and `charactertrade` documentation on `tibia.com` (2020).

### E12 — Animus Mastery progression

Official 2024 Soulpit/Animus material describes obtaining Animus Mastery for creatures and accumulating mastery across creatures to unlock character-relevant bonuses. Official Character Bazaar listings in 2025/2026 expose `Animus Masteries unlocked` as part of the traded character state.

Primary source:

- `https://www.tibia.com/news/?id=7944&subtopic=newsarchive`

Classification: strong **character-specific progression candidate / transfer-observed state**, while creature definitions, bonus formulas and compatibility remain ruleset/content-owned.

## 4. Revised evidence matrix

| Stage-B subject | Delta result | Freeze-readiness consequence |
|---|---|---|
| Character-name namespace scope | `DERIVED / strong historical continuity`: global cross-world uniqueness | **Strong architecture candidate**; detailed naming still open |
| Exact naming normalization/case/space/repertoire | `UNKNOWN` | **NOT READY** |
| Deleted-name recycling/hold | current `>=6 months`; target continuity `UNKNOWN` | **NOT READY as Reference value** |
| Active-character quota 25 | `DERIVED / strong continuity` | **Strong candidate** |
| Total active+deletion quota 30 | current-only; target continuity `UNKNOWN` | **NOT READY as Reference value** |
| Reversible deletion 60 days | current-only; target continuity `UNKNOWN` | **NOT READY as Reference value** |
| Promotion minimum level 20 | `DERIVED / very strong primary continuity` | **Strong candidate rule** |
| Promotion Premium eligibility | `DERIVED / very strong primary continuity` | **Strong candidate rule** |
| Promotion cost 20,000 gp | target continuity `UNKNOWN` | **NOT READY as exact value** |
| Promotion Premium-lapse behavior | target continuity `UNKNOWN` | **NOT READY as exact edge** |
| Offline 10-minute activation | `DERIVED / strong continuity` | **Strong candidate rule** |
| Offline 12-hour max | `DERIVED / strong continuity` | **Strong candidate rule** |
| Offline pool drain/refill state machine | `DERIVED / strong primary continuity` | **Strong semantic candidate** |
| Offline effectiveness/formulas | `UNKNOWN` | **Reference implementation blocker, not necessarily schema blocker** |
| Twist of Fate existence/state | pre-target existence + target-boundary `OBSERVED / strong alignment` | **Strong feature candidate** |
| Twist exact PvP/fair-fight edges | `UNKNOWN` | **NOT READY** |
| Adventurer's Blessing core family | `DERIVED / strong continuity` | **Strong candidate rule family** |
| World-type death exceptions | `PROVEN` that material profile differences exist; exact target matrix incomplete | **Must be profile/ruleset-scoped** |
| Wheel Promotion Point progress/allocations | `DERIVED / strong character-build evidence` | **Ownership candidate improved** |
| Weapon Proficiency progress | **`PROVEN` character-bound/non-transferable** | **Semantic ownership ready** |
| Weapon Proficiency tree/perk definitions | definition-scoped, not Character-owned item instances | **Boundary candidate improved** |
| Charms/charm points/charm expansion | **`PROVEN` character-specific by Bazaar transfer contract** | **Semantic ownership ready** |
| Hunting Task Points | **`PROVEN` character-specific by Bazaar transfer contract** | **Semantic ownership ready** |
| Permanent Hunting Task/Prey slots | **`PROVEN` character-specific by Bazaar transfer contract** | **Semantic ownership ready; purchase/entitlement source remains separate** |
| Animus Mastery count/progress | primary design + Bazaar transfer-observed character state | **Strong character-specific candidate** |
| Exact XP→level target formula | current exact table; July-28 continuity `UNKNOWN` | **Reference fixture blocker; recommend not generic-schema blocker** |
| Exact skill curves | `UNKNOWN` | **Reference fixture/ruleset blocker; recommend formula-neutral persistence** |

## 5. B1 naming — blocker reduced, not closed

The namespace scope is no longer an evidence-free product choice: official historical material explicitly describes globally unique character names across worlds.

For July-28 contract purposes:

- global name namespace: `DERIVED / strong historical continuity candidate`;
- exact normalization/canonicalization: `UNKNOWN`;
- case/space equivalence: `UNKNOWN`;
- permitted repertoire/technical normalization pipeline: `UNKNOWN`;
- recycling/redirect/history after delete/rename: `UNKNOWN`.

**Recommendation:** future Character Authority should prefer a global canonical namespace unless contrary target evidence appears, while DUR-02 must not freeze physical collation/index normalization yet.

B1 remains **PARTIALLY OPEN**.

## 6. B2 deletion/quota — lifecycle is safe; exact policy values still open

25 active characters has explicit pre-target production evidence plus current continuity: `DERIVED / strong continuity`.

This delta still lacks target-era dated proof for:

- 60-day reversible deletion;
- active + deletion-scheduled total `30`;
- deleted-name hold `>=6 months`.

These remain `UNKNOWN target continuity`.

Stage A already safely freezes the semantic lifecycle:

```text
ACTIVE -> DELETION_SCHEDULED -> RETIRED
```

**Recommendation:** exact durations/quotas should be versioned Reference policy values, not baked into lifecycle identity or database topology. This recommendation is not owner-accepted here.

## 7. B4 progression formulas — separate ownership from arithmetic

### Mandatory decision test

**Must exact XP/skill formulas be decided now for durable schema ownership?**

**RECOMMENDATION: NO**, if the durable contract preserves:

1. authoritative total experience/progression facts;
2. authoritative skill facts at sufficient precision/range;
3. explicit ruleset/profile revision context;
4. deterministic migration/versioning hooks;
5. no schema constraint that assumes an unproven formula;
6. exact formula/rounding fixtures before Reference implementation/parity claim.

Unknown formulas continue to block:

- target-accurate Reference advancement implementation;
- deterministic parity fixtures;
- balance/simulation verification.

They need not alone block:

- Character ownership of XP/skills;
- revision/fencing/transaction discovery;
- formula-neutral durable representation.

Exact arithmetic belongs with the relevant ruleset and `SIM-DETERMINISM-01` before executable Reference parity is claimed.

## 8. B5 promotion — stable core versus value/entitlement edges

Level >=20 + Premium eligibility + vocation-specific promoted identity has very strong primary continuity and is a strong Stage-B candidate.

Still target-unproven:

- 20,000 gp fee continuity;
- exact Premium-lapse suspension/reactivation behavior;
- final split between durable promotion achievement and entitlement-derived active benefits.

**Recommendation:** Character owns promotion achievement/state; active benefits are derived from ruleset + current entitlement rather than erasing promotion history when Premium lapses. This remains nonbinding until accepted.

## 9. B6 death/PvP — profile boundary proven, full edge matrix open

Twist of Fate existed before target and is visible in target-boundary Character Bazaar state. Exact qualification/consumption/fair-fight semantics remain incomplete.

Official world-type history proves death/PvP rules materially differ by profile. Therefore the architecture must not model all death/blessing behavior as one universal world-independent Character formula.

Adventurer's Blessing has strong pre/post continuity for its core low-level PvP-protection family. Exact July-28 edge cases remain incomplete.

Death Redemption existed before target but changed over time; current semantics must not be projected backward without dated continuity evidence.

B6 remains **PARTIALLY OPEN**.

## 10. B7 offline training — semantic state near freeze-ready

The 2012 primary source defines a real character-owned timer/pool state machine:

```text
activation selected
-> >=10 min offline before gain
-> consume 1 pool second / training second
-> max 12 h effective continuous training
-> regenerate 1 pool second / second online
-> regenerate 1 pool second / second offline without training
-> depletion can refill while offline
-> refilled pool requires new activation before use
```

With current continuity this is `DERIVED / strong primary continuity`.

Still unknown:

- exact July-28 effectiveness coefficients;
- exact selectable-skill matrix where version-sensitive;
- tick/rounding behavior;
- loyalty/event/modifier interactions;
- migration edge cases.

Split B7 into:

- semantic counter/capability ownership — **near freeze-ready**;
- target arithmetic/effectiveness — still ruleset/evidence-blocked.

## 11. B8 modern build/progression ownership — materially reduced

### Wheel / Promotion Points

Strong primary design evidence makes earned Promotion Points and player allocations character-build state candidates. Perk definitions/formulas remain ruleset/ability/content definitions; Premium entitlement remains Platform-owned input.

### Weapon Proficiency

Primary official evidence explicitly states Proficiency Progress is character-bound and non-transferable.

Recommended boundary:

```text
Character
owns per-weapon Proficiency Progress / reached progress
owns character-selected proficiency choices where they are player state

weapon/content/ruleset definition
owns tree structure, thresholds, perk definitions and compatibility

GAME-ITEM / DUR-03
owns item-instance conservation/location/value-transfer invariants
```

### Bazaar-proven character-specific progression

The official Bazaar transfer contract is strong evidence that these are character-specific product state:

- charms / charm points / charm expansion;
- Hunting Task Points;
- permanent Hunting Task slots;
- permanent Prey slots;
- bestiary and other listed character progression/history.

This **does not require one giant Character aggregate/table**. Stage B only needs to preserve game-domain character ownership/scoping; dedicated sub-aggregates may remain appropriate when transaction, size or lifecycle evidence requires them.

### Animus Mastery

Official design describes accumulated creature masteries as player progression and Bazaar exposes mastery count in traded character state. Classify as **strong character-specific candidate**. Exact mastery definitions/bonus formulas remain content/ruleset-owned.

### Dust and purchase provenance

Character-bound dust and purchased permanent capabilities may be character-scoped state while their economy/commerce transaction evidence belongs to GAME-ITEM/DUR-03 and/or Platform entitlement contracts. Do not erase the ownership distinction by putting purchase authority into Character.

### Remaining B8 uncertainty

- exact migration/versioning of Wheel/proficiency/Animus/charm/task definitions;
- newer fields not covered by the historical Bazaar transfer contract;
- exact sub-aggregate versus core-Character placement where independent lifecycle/transaction evidence exists.

B8 is now **SUBSTANTIALLY REDUCED**. Charms, Hunting Task Points, permanent Hunting Task/Prey slots and Weapon Proficiency progress should no longer be listed as ownership-unknown.

## 12. Revised blocker classification

### Hard blockers before a complete GAME-CHAR Stage-B owner package

1. **B1 exact naming normalization/recycling** — global namespace is strong; canonicalization is not.
2. **B3 creation/starter template** — insufficient target-period primary evidence.
3. **B6 persistent death/PvP edge matrix** — profile boundary is known, target edge set incomplete.
4. **B8 residual modern-state migration/sub-aggregate boundaries** — much smaller after Bazaar/Weapon Proficiency evidence, but not zero.

### Values/formulas recommended to remain versioned without blocking generic semantic ownership

If the owner later accepts this split:

1. B2 deletion duration/total quota/name-hold exact values;
2. B4 exact XP/skill arithmetic;
3. B5 promotion fee/Premium-lapse edge behavior;
4. B7 offline-training effectiveness coefficients.

These still block a **Reference parity implementation/release claim** where applicable. The recommendation is only that they need not automatically block every generic durable Character schema decision when persistence is versioned, formula-neutral and migration-safe.

## 13. DUR-02 implications

DUR-02 remains bounded by Stage A and is not authorized to freeze physical schema from this delta.

Nonbinding extension points to preserve:

- global canonical name reservation without premature collation/normalization selection;
- versioned deletion policy values;
- authoritative XP/skill facts independent from exact arithmetic implementation;
- persisted/derived distinction for migration-sensitive stats such as capacity;
- Character-scoped offline-training pool/capability state;
- Character-scoped Wheel/promotion-point state;
- Character-scoped per-weapon proficiency progress keyed by stable weapon definition identity;
- Character-scoped charms/task/permanent-slot progression or explicit child aggregates under the same ownership domain;
- profile/ruleset-scoped death/blessing semantics.

None of this creates DDL authority.

## 14. Later ruleset/SIM implications

Before any target-accurate Reference implementation or `PARITY_CONFIRMED` fixture, exact formulas/effects still require evidence and deterministic tests.

```text
DURABLE OWNERSHIP QUESTION
Who owns the authoritative fact and how is it versioned/fenced/migrated?

RULESET/SIM QUESTION
How does the target revision calculate, advance or transform that fact?
```

Separating these concerns avoids baking uncertain arithmetic into persistence. It must never be used to ship unproven Reference behavior.

## 15. Decision timing

### Must full Stage B be accepted now?

**NO.**

### Must the formula-vs-schema split be accepted in this task?

**NO.** Include it in a later owner Stage-B closure package after remaining semantic blockers are reduced.

### Still blocked

- final character-bearing DUR-02 schema acceptance;
- broad Reference character implementation;
- target-accurate naming/creation/death fixtures;
- final Stage-B owner contract.

### Still safe to continue

- historical primary evidence acquisition;
- bounded DUR-02 discovery under Stage A;
- GAME-CHANNEL/GAME-ITEM evidence work under separate ownership;
- SIM/ruleset formula evidence gathering;
- evidence-manifest/tooling design.

### Supersession evidence

Reopen these classifications only with stronger target-period primary snapshots, owner-provided target-era captures with provenance, an accepted Stage-B baseline or evidence that an unresolved formula materially changes durable identity/ownership/atomicity/representation.

## 16. Next evidence priorities

1. target-era official account/creation snapshots for B1/B2/B3;
2. target-era/current-continuity evidence for death/PvP blessing edges by world type;
3. modern progression migration/versioning evidence, especially Animus and post-2020 Bazaar-added systems;
4. exact progression/skill/offline formulas only where needed for Reference fixtures or proven to constrain durable representation;
5. assemble an owner Stage-B closure packet only after residual semantic blockers are materially reduced.

## 17. Deliberately not decided

- no Stage-B rule is owner accepted;
- no physical name index/collation;
- no 60-day/30/6-month Reference acceptance;
- no exact starter template;
- no exact XP/skill formula;
- no exact promotion price/entitlement transition target rule;
- no complete death/PvP matrix;
- no offline-training effectiveness formula;
- no final sub-aggregate layout for every modern progression system;
- no DDL/runtime/protocol/content implementation.

Until explicit owner acceptance, this document remains **PRE-DECISION EVIDENCE DELTA / NOT ACCEPTED** and does not change `GAME-CHAR-01 = PROPOSED / PLANNED / NOT_STARTED`.
