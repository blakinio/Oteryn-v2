# GAME-CHAR-01 — Stage B Reference Evidence Reconciliation

- Status: **PRE-DECISION EVIDENCE ANALYSIS / NOT ACCEPTED**
- Date: 2026-08-11
- Gate: `GAME-CHAR-01` Stage B
- Reference target: **Global Tibia production-observable behavior after the 2026-07-28 server-save/maintenance change boundary**
- Coordination ID: `OTV2-GLOBAL-ARCHITECTURE`
- Trusted repository base: `blakinio/Oteryn-v2@ef906b3c2d9cbb9cb7a455a94f84068fb6175795`
- Purpose: determine which Reference-sensitive character semantics are sufficiently evidenced for the selected target and which remain fail-closed
- Does not authorize: Stage-B acceptance, overall GAME-CHAR acceptance, runtime/client/protocol/persistence/content implementation, physical schema, production rollout or intentional Reference differences

## 1. Executive result

### Can full GAME-CHAR Stage B close now?

**NO.**

The selected July-28 target removes the version ambiguity, but it does not remove evidence gaps. The current evidence is already sufficient to establish several durable character-state categories and several historical rules with useful confidence. It is **not** yet sufficient to freeze the complete target-accurate naming/deletion/creation policy, exact progression formulas, all promotion/death edge cases, offline-training effectiveness, or the ownership/shape of every modern character-build subsystem.

The correct next step is evidence acquisition and reconciliation, not owner acceptance of guessed mechanics.

### What is already materially useful

The evidence is strong enough to constrain architecture in several ways without closing Stage B:

- the target has five vocations and promoted forms;
- the target exposes level, experience, hit points, mana, capacity, speed, eight named skills, vocation/promotion and blessings as durable/public character facts;
- the 25-active-character account quota predates the target and is still documented after it;
- seven regular blessings existed at the target;
- the long-lived death-loss model and offline-training timing have strong before/after continuity evidence;
- capacity has explicit historical migration semantics that prove it cannot always be treated as a pure level/vocation-derived value;
- the target early-game flow already includes Targuna, while at least one current official quick-start surface still contains stale Thais-Peninsula wording, proving that even official manuals require claim-level chronology checks.

## 2. Evidence discipline used here

The accepted first-Reference owner baseline defines these evidence states:

- `PROVEN`
- `OBSERVED`
- `DERIVED`
- `UNKNOWN`
- `CONFLICT`
- `DECLARED_DIFFERENCE`

This dossier applies them **to the July-28 target claim**, not merely to the fact that a web page currently says something.

### Important distinction

```text
PROVEN that current official manual says X
!= PROVEN that July-28 target behavior was X
```

A current official page may be excellent primary evidence about current Tibia while target continuity remains `UNKNOWN`.

Likewise:

```text
no discovered change note between dates
!= proof that the rule never changed
```

Where the same rule is documented by primary official evidence before and after the target with no material conflict, this dossier may classify target continuity as `DERIVED`, but it does not relabel that as direct target proof.

## 3. Primary evidence inventory

The following public official sources were used as primary evidence inputs.

### Target-era direct public surfaces

- Official Character Bazaar/search surfaces with auctions starting/ending on 2026-07-28 and 2026-07-29, including target-era characters across Druid/Elder Druid, Knight/Elite Knight, Monk/Exalted Monk, Paladin/Royal Paladin and Sorcerer/Master Sorcerer.
- Example target-boundary detail: `Mord Or`, Exalted Monk, auction ending 2026-07-28 10:00 CEST, exposing level, HP, mana, capacity, speed, blessings, all eight skills, experience, current world-transfer availability and other durable/public facts.
- Official July-28 production news: `Balancing, Fixes and Changes` after that day's server save.

### Dated pre-target primary sources

- 2009 death-penalty redesign: level-based experience/skill loss, promotion reduction and blessing/item-loss percentages.
- 2012 offline-training introduction and later bed support.
- 2017 introduction of two additional regular blessings, taking the total to seven, plus Death Redemption.
- 2025 Monk rollout and explicit account-character-limit increase from 20 to 25.
- 2025 Newhaven/base-capacity change: base capacity increased by 200, with existing-character effect applied only after a level-up.
- 2026 Targuna introduction and follow-up live fixes in March/April.
- 2026 vocation-adjustment release-state and July live changes.

### Current primary sources

- official `Creating a Character` manual;
- official account-management character/deletion manual;
- official character manual covering progression, skills, promotion, vocation data and death;
- official offline-training FAQ;
- official promotion FAQ.

Current sources are used as post-target evidence, not automatically as target snapshots.

## 4. Evidence summary matrix

| Stage-B subject | July-28 evidence result | Freeze readiness | Main reason |
|---|---|---|---|
| Five-vocation roster + promoted forms | `PROVEN` / target-era direct | **READY as vocabulary** | target-era official Character Bazaar exposes all five vocation families and promoted forms |
| Level / experience / HP / mana / capacity / speed as character facts | `PROVEN` / target-era direct | **READY as vocabulary** | official target-era Character Bazaar exposes them directly |
| Eight skill categories | `PROVEN` / target-era direct | **READY as vocabulary** | target-era official character details expose fist/club/sword/axe/distance/shielding/fishing/magic level |
| Active-character quota = 25 | `DERIVED` | **STRONG, not direct target snapshot** | official 2025 increase 20→25 + current official manual 25 |
| Total active+deletion quota = 30 | `UNKNOWN` target continuity | **NOT READY** | current official account manual only in gathered evidence |
| 60-day reversible deletion | `UNKNOWN` target continuity | **NOT READY** | current official account manual only in gathered evidence |
| Deleted-name reuse delay ≥6 months | `UNKNOWN` target continuity | **NOT READY** | current manual only; exact recycling rule may be longer/contextual |
| Name max 29 letters / no numbers/special chars/etc. | `UNKNOWN` target continuity | **NOT READY** | current creation manual only; exact normalization/reserved-word policy unspecified |
| Creation inputs name/sex/world | `UNKNOWN` target continuity | **NOT READY as exact target contract** | current manual says so; target-era public character surfaces prove the facts exist, not the exact creation transaction |
| Newhaven→Targuna target-era early flow | `PROVEN` live before target | **READY as content-flow fact** | March 2026 release/fix chronology establishes Targuna live months before target |
| Exact starter template/items/stats/home-city/citizenship | `UNKNOWN` | **NOT READY** | no complete target-era primary capture |
| Vocation selection at/around level 8 | `DERIVED` | **PARTIALLY READY** | longstanding official level-8 vocation model + 2026 Targuna/current guide evidence, but exact flow needs target snapshot |
| Per-level HP/mana/capacity gains table | `OBSERVED`/`DERIVED` | **NOT READY as universal formula** | current table plus target-era samples support it, but capacity migration proves derived-state caveats |
| Capacity as pure derived value | **rejected by `PROVEN` migration evidence** | **READY negative constraint** | 2025 +200 base-capacity migration applies to existing character only after level-up |
| Exact experience→level formula | `UNKNOWN` | **NOT READY** | current manual describes progression but not full formula |
| Exact skill advancement formulas | `UNKNOWN` | **NOT READY** | current manual names skills/training behavior, not advancement curves |
| Promotion existence + promoted vocation titles | `PROVEN` target-era | **READY as vocabulary** | target-era Bazaar exposes promoted forms |
| Promotion level 20 / 20,000 gp / Premium eligibility | `UNKNOWN` target continuity | **NOT READY** | current manual/FAQ primary evidence gathered, but no target-era continuity proof yet |
| Seven regular blessings | `PROVEN` target-era | **READY** | 2017 introduction + target-era Character Bazaar counts up to 7/7 |
| Base death XP/skill model | `DERIVED` strong continuity | **READY as candidate rule, not yet owner-accepted** | 2009 official rule and current official manual materially match |
| Promotion death-loss reduction = 30% | `DERIVED` strong continuity | **READY as candidate rule** | 2009 official rule and current manual match |
| Regular blessing XP/skill reduction = 8% each | `DERIVED` strong continuity | **READY as candidate rule** | 2009 rule + 2017 seven-blessing total + current manual |
| Equipment loss 10% each; blessing item protection 30/55/75/90/100% | `DERIVED` strong continuity | **READY as candidate rule** | 2009 official model + current manual match |
| PvP blessing / red-black-skull / Adventurer's Blessing exact target rules | `UNKNOWN` target continuity | **NOT READY** | current manual gives details; target-era proof not yet complete |
| Death Redemption exists | `DERIVED` / pre-target + current | **STRONG** | official 2017 introduction + current manual |
| Offline training starts after >10 min and max counter =12h | `DERIVED` strong continuity | **READY as candidate rule** | 2012 official introduction + current FAQ match |
| Exact offline-training skill effectiveness/formulas | `UNKNOWN` | **NOT READY** | official material does not establish full target formula |
| Wheel/bonus promotion points as target-visible build facts | `OBSERVED` target-era | **READY as vocabulary, ownership detail open** | target-era auctions expose bonus promotion points; official manual defines Wheel |
| Proficiencies / Animus / charm/task state ownership inside Character aggregate | `UNKNOWN / boundary unresolved` | **NOT READY** | target-era public character surfaces expose these systems, but aggregate ownership belongs to their named later gates/contracts |

## 5. Creation and starter-state reconciliation

### 5.1 Current official creation inputs

The current official creation manual says a new character is created by selecting:

- name;
- sex/gender;
- game world.

It also currently states a 25-active-character account limit.

### Target classification

- existence of name/sex/world as durable public character facts: `OBSERVED` target-era through official character surfaces;
- exact July-28 creation transaction and initial template: `UNKNOWN`.

The architecture must therefore preserve room for these inputs without treating the current website flow as a complete July-28 creation contract.

### 5.2 Starter-flow chronology — important stale-document finding

A dated official March 17, 2026 announcement states that from level 8 onward characters no longer travel directly to Thais Peninsula after Newhaven and instead continue to **Targuna**. Official March 18, March 24, March 31 and April 8 production fixes explicitly describe Targuna as introduced/live.

At the same time, a currently indexed official quick-start page still contains older wording about leaving Newhaven for Thais Peninsula and a separate Blue Valley path for monks.

Classification:

- Targuna was live before July 28: `PROVEN`;
- current quick-start wording for the old route: `CONFLICT / stale documentation evidence`;
- exact complete starter transaction/template at July 28: `UNKNOWN`.

### Architecture consequence

Do **not** encode starter routing or initial home-city/citizenship as a hard-coded universal Character constructor based on whichever current manual paragraph is easiest to find. Starter state must come from an explicit versioned Reference content/ruleset template, as Stage A already requires.

## 6. Account quota, deletion and restore

### 6.1 25 active characters

Official February/March 2025 Monk rollout material explicitly increased the account character limit from 20 to 25. The current official creation/account manuals also state 25 active characters.

Target classification: **`DERIVED` strong continuity**.

It is reasonable to treat 25 as a high-confidence July-28 Reference candidate, but this dossier does not relabel the derivation as direct target observation.

### 6.2 Current deletion model

The current official account manual states:

- deletion is reversible for 60 days;
- deletion-scheduled characters do not count against the 25 active limit;
- active + deletion-scheduled total may not exceed 30;
- undelete during the 60-day period is blocked when it would exceed 25 active characters;
- after final deletion the character cannot be restored;
- deleted-character names cannot be chosen for new characters for at least six months.

### Target classification

The gathered evidence did not establish a dated July-28 snapshot or before/after continuity proof for these exact values.

Therefore:

- `60 days` = `UNKNOWN` target continuity;
- `30 total` = `UNKNOWN` target continuity;
- `≥6 months name hold` = `UNKNOWN` target continuity.

### Stage-A interaction

Stage A already safely freezes only the semantic distinction:

```text
ACTIVE -> DELETION_SCHEDULED -> RETIRED
```

with restore before terminal retirement and no CharacterId reuse. That architecture remains valid while target-specific grace/quota/name-reuse values stay unresolved.

## 7. Naming evidence

### Current primary documentation

The official creation manual currently states:

- maximum 29 letters;
- no numbers;
- no special characters;
- some words/letter combinations are disallowed;
- Tibia Rules apply;
- character rename exists as a paid later operation.

### Evidence limitations

The current public rules do **not** fully define the implementation-grade target semantics needed by Character Authority, including:

- Unicode normalization/canonicalization;
- case-folding semantics;
- whitespace normalization;
- exact permitted character repertoire;
- global versus scoped uniqueness in machine terms;
- reserved-word source/revision;
- exact deleted-name reuse timing and exceptions;
- rename-history/redirect behavior.

The gathered material also does not prove that the current 29-character/filter details were identical on July 28.

### Result

Exact naming policy is **not freeze-ready** for Stage B. Final name unique-index scope/normalization remains forbidden DUR-02 territory until this is resolved.

## 8. Durable progression vocabulary

### 8.1 Target-era official Character Bazaar evidence

Official Character Bazaar pages around July 28 expose character facts including:

- level;
- experience;
- hit points;
- mana;
- capacity;
- speed;
- vocation / promoted vocation;
- blessings;
- Fist Fighting;
- Club Fighting;
- Sword Fighting;
- Axe Fighting;
- Distance Fighting;
- Shielding;
- Fishing;
- Magic Level.

The detailed target-boundary auction for `Mord Or` (Exalted Monk, ending July 28 10:00 CEST) directly exposes all of these categories.

### Result

The **vocabulary** is target-ready as character-visible/persistent semantics.

This does **not** mean every value belongs in one Character table or every value is independently mutable. It only establishes the target-visible semantic catalogue.

### 8.2 Exact formulas remain separate

The current manual states that level increases affect HP, mana, capacity, movement and magical power, and provides vocation-specific per-level HP/mana/capacity gains. It does not provide all implementation-grade formulas for:

- total experience required per level;
- low-level experience bonus function;
- exact walking-speed formula;
- skill advancement curves per vocation/skill;
- all derived combat-stat formulas;
- rounding/overflow behavior.

Those exact formulas remain `UNKNOWN` unless separately evidenced, and several belong to `SIM-DETERMINISM-01` or gameplay/ability contracts rather than the Character aggregate itself.

## 9. Capacity migration — authoritative fact versus derived value

This is a particularly important Stage-B finding.

Official 2025 Newhaven release material states that base capacity for all characters was increased by 200, raising it to 600, but that for an existing character the change would take effect in game only **after the character levelled up**.

Consequently, at a later production cut such as July 28, two characters with otherwise similar level/vocation history could have different persisted capacity state if one had crossed the migration trigger and the other had not.

### Architecture consequence

The first native model must not assume:

```text
capacity = pure_function(level, vocation)
```

for all imported/reference state.

Instead, one of the following semantics must exist under the eventual migration contract:

- authoritative persisted capacity fact; or
- a deterministic source revision + migration-state fact sufficient to derive it exactly.

The physical choice belongs to DUR-02, but the semantic requirement is already clear.

### Status

- existence of migration-sensitive capacity semantics: `PROVEN`;
- final Oteryn persistence representation: deliberately undecided.

This directly supports the accepted Stage-A rule separating authoritative progression facts from derived values and forbidding silent reinterpretation under ruleset revision changes.

## 10. Vocation and promotion reconciliation

### 10.1 Five vocation families

Official target-era July-28 Character Bazaar surfaces expose:

- Druid / Elder Druid;
- Knight / Elite Knight;
- Monk / Exalted Monk;
- Paladin / Royal Paladin;
- Sorcerer / Master Sorcerer.

Official 2025 Monk launch material and 2026 vocation-adjustment releases independently establish Monk as the fifth vocation before the target.

Target classification: **`PROVEN`** for the roster/promoted vocabulary.

### 10.2 Vocation state belongs to ruleset profile

This evidence strengthens, rather than changes, Stage A:

- vocation/promotion state is durable Character-owned build/profession state;
- exact combat mechanics belong to the ruleset/ability/simulation layers;
- five target vocations do not become a universal engine enum that all future profiles must use.

### 10.3 Promotion eligibility/current rules

Current official manual/FAQ states:

- minimum level 20;
- one-time cost 20,000 gp;
- Premium required;
- promotion is suspended when Premium expires and restored when Premium returns.

Target classification: **`UNKNOWN` continuity for these exact eligibility/commercial values** with the evidence gathered in this task.

Promotion **existence/titles** are target-proven; exact July-28 eligibility/effect contract still needs target continuity evidence.

## 11. Modern character-build state boundary

Target-era Character Bazaar surfaces expose additional long-lived character facts such as:

- Bonus Promotion Points;
- Animus Masteries unlocked;
- Charm points / minor charm echoes;
- Hunting Task points;
- proficiency-related surfaces;
- additional permanent slots/expansions.

The current manual also describes Wheel of Destiny allocations and promotion points.

### Finding

Public exposure on a character page does **not** prove that all such state belongs to the Character aggregate.

Stage A remains binding: references to CharacterId do not transfer authority.

### Recommended ownership questions

- Wheel allocation / promotion-point spend: likely Character-owned build state, but exact ruleset representation must be reconciled with ability/simulation contracts.
- Weapon proficiency: likely crosses Character progression + item/weapon-definition semantics; do not assign solely to Character without `GAME-ITEM-01` / ability ownership analysis.
- Charms/bestiary/animus/task systems: likely separate progression/content aggregates or character-scoped subdomains; do not inflate the core Character aggregate merely because Bazaar renders them together.
- account-purchased/permanent extra slots: entitlement/product ownership may remain Platform/product-owned with game-side validated projection/claim depending the specific feature.

### Result

Full modern build-state ownership is **not Stage-B freeze-ready** from this evidence alone.

## 12. Death and respawn reconciliation

### 12.1 Long-lived base loss model

Official 2009 production-change documentation introduced the level-scaled death-loss model that the current official manual still describes materially the same way:

- unprotected characters up to the low-level threshold lose 10% experience/skills;
- from higher levels, loss scales down as an approximate level-loss function;
- promotion reduces death loss by 30%;
- each regular blessing reduces experience/skill loss by 8%.

Current manual gives the low-level threshold as up to level 23 and starts the level-based explanation at 24.

Target classification: **`DERIVED` strong continuity**, not direct July-28 proof.

### 12.2 Seven regular blessings

Official 2017 material introduced two additional blessings, taking the total to seven. Target-era Character Bazaar pages around July 28 directly expose counts such as 5/7, 6/7 and 7/7.

Target classification: **`PROVEN`** that seven regular blessings existed at the selected cut.

### 12.3 Equipment-loss protection

The 2009 official rule and current manual materially agree on the item-loss protection ladder:

- base 10% chance per equipped item;
- containers/backpack handling;
- 1 blessing = 30% item-loss protection;
- 2 = 55%;
- 3 = 75%;
- 4 = 90%;
- 5+ = 100%.

Target classification: **`DERIVED` strong continuity**.

### 12.4 Death Redemption

Official 2017 material introduced Death Redemption and current manual still documents it.

Target classification: **`DERIVED`** for existence; exact target restrictions need per-claim confirmation.

### 12.5 What is still not sufficiently target-proven

The current manual contains detailed rules for:

- Twist of Fate / PvP blessing;
- PvP damage qualification window;
- red/black skull exceptions;
- Adventurer's Blessing;
- Retro Hardcore PvP percentages;
- Death Redemption recency/death-count eligibility;
- special PvP loss adjustments.

This task did not establish complete July-28 continuity for every one of those details.

They remain `UNKNOWN` at exact-target-contract level until evidenced.

### Architecture boundary

Character-owned consequences such as experience/skill/blessing state changes must remain idempotent and revision-aware under Stage A.

Item/equipment/corpse loss remains transaction/conservation-owned by combat + `GAME-ITEM-01` / `DUR-03`, not duplicated into the Character aggregate.

## 13. Offline training reconciliation

Official 2012 material introduced offline training, and the current official FAQ still documents the same key timing semantics:

- training begins only after the character has been offline for more than 10 minutes;
- offline-training counter maximum is 12 hours;
- training consumes available counter time;
- additional offline time refills the counter under the documented rules;
- statue/bed selection chooses the training path/skill where supported.

Target classification for the **10-minute threshold and 12-hour maximum**: **`DERIVED` strong continuity**.

### Not yet target-ready

The gathered official material does not completely establish:

- exact target-era advancement efficiency per vocation/skill;
- the full set of selectable skills for each vocation at July 28;
- exact rounding/tick behavior;
- how loyalty/temporary modifiers interact;
- all interruption/migration corner cases.

These remain `UNKNOWN` and must not be invented by a background timer implementation.

## 14. What is safe to consume before full Stage-B acceptance

This dossier is nonbinding, but it identifies **evidence-safe architecture questions** that downstream discovery may rely on without treating them as final owner-approved Reference rules:

1. the target character model must be able to represent level, experience, HP, mana, capacity, speed, the eight skills, vocation/promotion and blessing state;
2. vocation state must be profile/ruleset-owned, not an engine fork;
3. capacity must support migration-sensitive authoritative state and cannot be universally recomputed from level/vocation;
4. character deletion policy needs a reversible/nonterminal phase distinct from terminal retirement, already accepted in Stage A;
5. death consequences must be idempotent and split Character-owned progression/blessing effects from item-conservation transactions;
6. offline training needs explicit capability/counter/revision semantics rather than implicit background progress;
7. modern build/progression systems require explicit ownership rather than one giant Character row;
8. final naming unique-index/normalization cannot be frozen yet.

DUR-02 may use these as questions/constraints only within its already accepted bounded-discovery permission. Final schema still waits for accepted Stage B.

## 15. Full Stage-B blockers

The following evidence gaps are material enough that full `GAME-CHAR-01` must remain unaccepted:

### B1 — naming contract

Need target-quality evidence for:

- canonicalization/normalization;
- case/space semantics;
- valid character set;
- uniqueness scope;
- reserved-word/restricted-pattern authority;
- rename conflict/history semantics;
- deleted-name recycling timing/exceptions.

### B2 — deletion/quota target continuity

Need target-quality evidence for:

- 60-day reversible deletion;
- 30 active+scheduled total limit;
- exact undelete/quota interaction;
- name hold after final deletion.

The 25-active quota itself has strong derived continuity evidence.

### B3 — exact creation/starter template

Need the target-period creation/new-character state including:

- exact initial level/stats/skills/capacity;
- starter inventory/equipment;
- home-city/citizenship state;
- Newhaven/Targuna/vocation-choice transition facts that are Character-owned versus content-owned;
- retry-visible product semantics.

### B4 — exact progression formulas

Need evidence/owner assignment for:

- experience→level formula;
- skill advancement curves;
- speed formula;
- exact low-level modifiers;
- authoritative versus derived representation for every stored progression field;
- rounding and overflow under `SIM-DETERMINISM-01` where applicable.

### B5 — promotion target contract

Need target continuity for level/cost/Premium eligibility and promotion suspension semantics, plus exact durable state versus entitlement projection boundary.

### B6 — death edge cases

Need target evidence for the exact PvP/skull/blessing/Death-Redemption edge rules that materially affect persistent character/value state.

### B7 — offline-training effectiveness

Need target evidence for selectable skills, advancement efficiency and exact state transitions/rounding.

### B8 — modern build-state ownership

Need explicit ownership mapping for Wheel allocations, bonus promotion points, proficiency and other character-visible progression systems without silently absorbing GAME-ITEM/content/entitlement authorities.

## 16. Evidence-acquisition plan

### Priority 1 — historical primary snapshots

Seek preserved July-28-era copies/captures of official:

- account/character management manual;
- character creation manual;
- character gameplay manual;
- support FAQ pages for promotion/offline training/naming/deletion.

A preserved official page is stronger historical continuity evidence than a current page alone.

### Priority 2 — target-era Character Bazaar samples

Capture a bounded evidence set across:

- all five vocation families;
- promoted and unpromoted characters;
- low/high levels;
- characters created before and after major migrations such as the capacity change.

Use these to test durable vocabulary and identify migration-sensitive facts. Do not infer hidden formulas from one sample.

### Priority 3 — official change chronology

Build rule-specific dated chronology for:

- character quotas/deletion/name policy;
- capacity/HP/mana progression changes;
- promotion changes;
- death/blessing/PvP-death changes;
- offline-training changes;
- early-game creation/Targuna changes;
- Wheel/progression-system changes.

### Priority 4 — controlled black-box observation

Current Global observation can answer a July-28 historical question only if continuity from target to observation is evidenced. Otherwise record it as current-state `OBSERVED`, not target proof.

### Priority 5 — community/OTS research

Use community sources and OTS implementations solely to:

- discover candidate formulas;
- find likely change dates;
- design tests;
- locate missing primary evidence.

They do not promote a claim to `PROVEN` by themselves.

## 17. Owner-decision result

### Recommendation

**Do not ask the owner to accept full Stage B yet.**

There is no useful product preference to choose among the unresolved facts at this point; they are primarily evidence questions.

The owner should only be asked for a new decision if:

- historical target evidence proves unavailable and an explicit Reference difference/fallback policy is required;
- two credible target sources remain in `CONFLICT` after investigation;
- a gameplay/product choice is genuinely not determined by Reference evidence;
- an intentional simplification would materially diverge from the selected target.

Until then, autonomous evidence acquisition should continue.

## 18. Decision-timing discipline

### Must Stage B be accepted now?

**NO — evidence acquisition can and should proceed first.**

### What downstream work is blocked?

- final character-bearing DUR-02 schema;
- broad Reference character progression implementation;
- final target-accurate naming/deletion/creation fixtures;
- final death/offline-training persistent behavior.

### What may still proceed?

- GAME-CHANNEL architecture under separate ownership;
- bounded DUR-02 discovery using Stage-A invariants and target context only;
- Reference evidence-manifest/tooling design;
- GAME-ITEM evidence work against the same target if paths/contracts do not overlap;
- this Stage-B evidence acquisition.

### Future cost of guessing now

Prematurely freezing current-only or OTS-inferred semantics would bake historical uncertainty into unique constraints, migration logic, progression state and deterministic fixtures. Correcting that later would be more expensive than preserving `UNKNOWN` now.

### Supersession evidence

Any later accepted Stage-B rule should name the evidence that promoted it from `UNKNOWN`/`DERIVED`/`OBSERVED` into an owner-accepted Reference semantic. A later Reference revision supersedes target behavior only through the already accepted explicit revision process.

## 19. Deliberately not decided here

- final Stage-B owner contract;
- final naming normalization/index model;
- final deletion timers/quotas where target continuity is not established;
- exact starter template;
- exact XP/skill/speed formulas;
- exact promotion eligibility/economy entitlement interaction;
- full PvP death edge matrix;
- exact offline-training effectiveness;
- Wheel/proficiency/charms/Animus/task aggregate ownership;
- PostgreSQL physical schema;
- runtime/client/protocol/content implementation;
- production activation.

Until the evidence blockers are reduced enough for an honest owner package, `GAME-CHAR-01` remains **PROPOSED / PLANNED / NOT_STARTED** with Stage A accepted, Stage B unaccepted, and runtime authority **NONE**.
