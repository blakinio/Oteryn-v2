# OTV2-20260814 — Official Tibia spell-library observations

- Evidence task: `OTV2-20260814-ability-combat-first-evidence-fixtures`
- Reference target: `global-tibia-observable-2026-07-28-post-server-save`
- Retrieval date: 2026-08-14
- Source class: `OFFICIAL_PUBLIC`
- Provenance state: `CLEARED` for source identity/locator and bounded factual transcription
- Legal review state: `PENDING`
- Usage: paper-only Reference evidence; no proprietary assets/code copied

## Evidence discipline

These are bounded observations from the current official Tibia Library pages retrieved after the accepted 2026-07-28 Reference boundary. They are **not** a time-locked capture made exactly on 2026-07-28 and therefore do not by themselves prove that every observed field was unchanged from the boundary through retrieval.

Patch-note absence is not used as continuity evidence. The manifest cases based on this capture must remain `OBSERVED`, preserve the continuity uncertainty, and must not become `PARITY_CONFIRMED` without exact Oteryn implementation/test evidence and cleared legal/provenance gates.

## Light Healing

Official locator:

`https://www.tibia.com/library/?spell=lighthealing&subtopic=spells`

Observed spell information:

- name: Light Healing;
- formula: `exura`;
- vocations listed: Druid, Monk, Paladin, Sorcerer;
- group: Healing;
- type: Instant;
- magic type: Healing;
- cooldown: 1 second; group cooldown: 1 second;
- experience level: 8;
- mana: 20;
- premium requirement: no.

The official description presents the spell as healing the caster's own wounds/injuries and describes the effect as limited. This supports only a qualitative self-healing interpretation. It does **not** provide an exact healing formula, magnitude range, rounding rule, scaling coefficients, failure/legality precedence or complete target-policy semantics.

## Ice Strike

Official locator:

`https://www.tibia.com/library/?spell=icestrike&subtopic=spells`

Observed spell information:

- name: Ice Strike;
- formula: `exori frigo`;
- vocations listed: Druid, Sorcerer;
- group: Attack;
- type: Instant;
- magic type: Ice;
- cooldown: 2 seconds; group cooldown: 2 seconds;
- experience level: 8;
- mana: 20;
- premium requirement: no.

The official description states qualitatively that the spell hits an aimed opponent in close range with ice and that its damage is determined by the caster's magical abilities. This supports targeted attack + ice-damage semantics only at a qualitative level. It does **not** provide an exact tile/range metric, exact target cardinality in every edge case, LoS/floor/PvP/PZ legality, damage formula, scaling coefficients, rounding, resistance interaction, critical/block/dodge behavior or RNG ordering.

## Explicitly unresolved

The following remain `UNKNOWN` for this package and must not be inferred from OTS implementations, current Oteryn convenience or absence of official patch notes:

- exact 2026-07-28 continuity of every listed field;
- exact Light Healing magnitude/formula/rounding/scaling;
- exact Ice Strike range metric and complete targeting/legality matrix;
- exact Ice Strike damage formula/rounding/scaling/mitigation/resistance;
- exact mana/cooldown commit anchors on failed/interrupted/illegal casts;
- error precedence and client-visible failure behavior;
- any implementation or parity state in Oteryn.
