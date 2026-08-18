# Oteryn Tibia 15.25 Appearance Spatial Profile v1

- Contract ID: `oteryn-tibia-15-25-appearance-spatial-v1`
- Semantic revision: `1`
- Coordination ID: `OTERYN-GAME-ATLAS-V1-APPEARANCE`
- Canonical owner: `Oteryn-Game` (current source lineage: `blakinio/Oteryn-v2`)
- Status: **PROPOSED until this exact content is merged to protected `main`; ACCEPTED thereafter unless explicitly superseded**
- Runtime implementation status: `NOT_IMPLEMENTED`
- Production status: `NOT_ENABLED`

## 1. Purpose

This profile supplies the bounded appearance/anchor/displacement semantics required to project the owner-authorized Tibia client asset package used by `DYN-ATLAS-001` into `oteryn-world-spatial-v1` without making the Tibia asset format or the legacy renderer canonical World authority.

It is intentionally limited to the exact package and evidence below. It does not define Game item identity, gameplay interaction priority, collision, a permanent Atlas texture format, a permanent Game -> Atlas serializer, or a general license for unrelated assets.

## 2. Exact asset fixture

The owner supplied archive is pinned by digest:

```text
archive: assets(1).zip
sha256: 01c45146e2fcec3f4087844e0cbc1817fb1d60b310a35ac5d88c07aab6f73d1a
```

Direct archive inspection records:

```text
package.json version: 15.25.bd5a04
package.json sha256: 01c405e8f72bc4bbf2009052cdccc10510a5664ab8b81713b78c804422c3db3b
assets/catalog-content.json sha256: 93ea5888174ef44b352d7c2b1f8061573a4a260bfaba4b7ec32ea836b9e411ab
appearance file: appearances-aa44a154f30c7ed59acc25f246286396e4043851ef0b54ef3cf3951e46d1ce50.dat
appearance file sha256: aa44a154f30c7ed59acc25f246286396e4043851ef0b54ef3cf3951e46d1ce50
object appearances: 42107
sprite sheets: 4927
catalog sprite id domain: 0..289767
unique sprite ids referenced by object appearances: 75623
```

The version is therefore **15.25.bd5a04**, not 15.32.

The counts above reconcile with the pinned legacy Otheryn Atlas evidence for its `vendor/map-analysis/tibia-client/15.25.bd5a04/assets/` source family. That reconciliation is evidence of fixture compatibility for this bounded proof; it is not a general statement that any package labelled 15.25 is interchangeable.

## 3. Rights/provenance boundary

For `DYN-ATLAS-001`, the project owner explicitly attested that the exact archive digest above may be decoded, derived, rendered, deduplicated and published for the public Oteryn Atlas proof/product.

This profile records that project authorization as owner-supplied evidence. It does not claim independently verified third-party copyright ownership and does not extend authorization to another archive/digest or unrelated proprietary asset set.

## 4. Spatial unit

For this asset profile:

```text
AppearanceSpatialUnitProfile {
  units_per_tile: 32
}
```

One native presentation displacement unit equals one decoded source pixel at the proof's canonical 32-pixel tile scale.

The unit is semantic conversion data for this source profile; it does not require the browser to render at one screen pixel per unit or freeze a permanent GPU resolution.

## 5. Sprite dimensions and footprint

The pinned catalog exposes decoded sprite cell layouts of:

```text
32 x 32
32 x 64
64 x 32
64 x 64
```

Every selected sprite dimension MUST be an integral multiple of `units_per_tile` in this profile.

For a decoded sprite of `width_px x height_px`:

```text
width_tiles  = width_px  / 32
height_tiles = height_px / 32
```

The canonical appearance anchor for this legacy projection is the tile position owning the presentation record. The decoded sprite extends west/north from that anchor exactly as the pinned legacy renderer does.

The footprint offsets for one decoded sprite are therefore the Cartesian set:

```text
dx_tiles in [-(width_tiles  - 1), 0]
dy_tiles in [-(height_tiles - 1), 0]
```

with `(0, 0)` as the south-east / bottom-right anchor cell of that decoded sprite footprint.

This is a source-profile mapping, not a universal Oteryn sprite-origin convention.

## 6. Shift and height to native presentation displacement

The pinned appearance metadata may carry a legacy `shift = (shift_x, shift_y)` and `height` value. Missing values are treated as zero for this source profile.

The pinned reference renderer positions a sprite by subtracting both shift components and, when present, subtracting `height` from both image axes.

The Game-owned conversion therefore emits the effective native presentation displacement:

```text
PresentationDisplacement {
  dx_units = -(shift_x + height)
  dy_units = -(shift_y + height)
}
```

where positive native `dx_units` means east/right and positive `dy_units` means south/down under `oteryn-world-spatial-v1`.

The exporter SHOULD preserve the raw source components as bounded provenance/debug metadata when public-safe, but Atlas must consume the explicit converted displacement rather than re-implement legacy shift/height rules.

## 7. Appearance frames, layers and concrete render primitives

The legacy appearance metadata contains pattern dimensions, layers, animation data and sprite IDs. Atlas must not infer a canonical sprite from a legacy appearance ID alone.

For the bounded static proof, Game owns resolution of the concrete presentation variant and exports a semantic render primitive equivalent to:

```text
ResolvedAppearancePrimitive {
  appearance_source_id
  frame_group
  phase
  layer_index
  sprite_source_id
  width_units
  height_units
  footprint_offsets
  displacement
  provenance
}
```

Rules:

- the legacy/source appearance and sprite IDs remain source/provenance identifiers, not canonical Game entity identity;
- layer order inside one resolved appearance primitive is explicit and deterministic;
- appearance-internal layers are not separate tile `PresentationOrderKey` records unless the Game exporter explicitly models them that way;
- the tile presentation record retains the Game-owned `PresentationOrderKey` from the spatial/import profile;
- Atlas may deduplicate identical decoded pixel payloads, but semantic appearance/placement identity must remain distinct.

## 8. Bounded static phase policy for DYN-ATLAS-001

DYN-ATLAS-001 is a static semantic proof, not the final animation contract.

For parity with the pinned legacy reference pipeline, the proof producer resolves:

- the first applicable object frame group used by the pinned reference parser/renderer;
- the declared `default_start_phase` for that frame;
- no elapsed-time animation advancement in the canonical static fixture.

The selected phase is exported explicitly. The browser does not recompute a legacy animation policy.

A later animation/live presentation contract may supersede this bounded static policy without changing stable semantic placement identity.

## 9. Pattern and subtype selection

Pattern/subtype/hangable/fluid/stack-count rules are source conversion concerns. For DYN-ATLAS-001 the Game-side fixture/export step MUST resolve the concrete primitive(s) before Atlas consumption.

Atlas MUST NOT reproduce legacy rules such as position modulo pattern dimensions, stack-count buckets, hook direction or fluid-color lookup to discover authoritative presentation state.

The producer may use pinned reference implementation evidence to perform that conversion, but the exported result is explicit semantic data with provenance.

## 10. Pixel content identity and Atlas deduplication boundary

Game owns the exact asset fixture/revision and the semantic mapping from source appearance to resolved primitives. Atlas owns publication-side pixel deduplication and GPU/runtime packing.

For proof measurements, Atlas may assign a deterministic content identity to decoded pixel blobs using a declared domain-separated digest over dimensions plus exact RGBA bytes. That proof content identity MUST NOT replace semantic appearance identity or become canonical Game item identity.

GPU atlas/page coordinates are runtime cache state only.

## 11. Validation requirements

Before a resolved primitive under this profile is accepted for Game -> Atlas proof use, producer/fixture validation must fail closed on:

- asset archive digest mismatch;
- package version mismatch;
- catalog or appearance digest mismatch;
- unknown sprite source id;
- unsupported sprite dimensions or dimensions not divisible by 32;
- malformed appearance/frame metadata;
- displacement arithmetic overflow;
- unresolved concrete sprite/phase/layer when that capability is declared required;
- missing public-safe provenance needed to reproduce the conversion.

Atlas consumer validation must reject inconsistent width/height/footprint/displacement metadata instead of rebuilding legacy rules from the source asset files.

## 12. DYN-ATLAS-001 effect

After merge, the proof has explicit Game-owned appearance semantics for the exact authorized 15.25.bd5a04 fixture:

```text
units_per_tile = 32
anchor = owning tile / south-east footprint cell
footprint = explicit west/north offsets derived from decoded sprite dimensions
effective displacement = (-(shift_x + height), -(shift_y + height))
concrete frame/phase/layer/sprite = producer-resolved and exported explicitly
```

This closes the appearance anchor/footprint/displacement authority gate.

DYN-ATLAS-001 still requires a bounded Game-owned Thais semantic export artifact/digest before the Atlas runtime may claim the full proof acceptance criteria.

## 13. Supersession

Revision 1 must be superseded rather than silently edited if evidence changes any of the following:

- exact asset archive/package identity;
- units-per-tile conversion;
- decoded sprite dimension semantics;
- anchor/footprint mapping;
- shift/height displacement conversion;
- static phase/layer resolution semantics.

Browser framework, texture packing, compression and immutable chunk packaging do not by themselves supersede this Game-owned appearance profile.
