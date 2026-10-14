#!/usr/bin/env python3
"""Temporary ROM graphics installer; requires source-art clearance for redistribution."""
import argparse
import tempfile
from pathlib import Path
from convert_follower_apng import DIRECTIONS, pack_species, synthetic_apng

HEADER = Path("src/data/object_events/follower_pilot_graphics.h")
TARGET = Path("graphics/object_events/pics/follower_import")
SENTINEL = "    { NULL, NULL }, /* species 0 is invalid */"

def install(source, checkout, ids):
    if not ids or len(set(ids)) != len(ids) or any(not 1 <= n <= 386 for n in ids):
        raise ValueError("bad National Dex ID(s)")
    hp = checkout / HEADER
    original = hp.read_text()
    # The invalid-species sentinel remains after import. Check that both
    # registry bodies contain only that sentinel before writing anything.
    for anchor in (
        "sFollowerRegisteredGraphics[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2]",
        "sFollowerRegisteredPalettes[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2]",
    ):
        if original.count(anchor) != 1:
            raise ValueError("missing or ambiguous registry")
        start = original.index("= {", original.index(anchor)) + len("= {")
        end = original.index("};", start)
        if original[start:end].strip() != SENTINEL:
            raise ValueError("registries not empty")
    declarations, gfx, pals, outputs = [], [], [], []
    for species in sorted(ids):
        size, variants = pack_species(source, species)
        names = []
        for variant in ("normal", "shiny"):
            name = "sFullFollower%03d%s" % (species, variant.capitalize())
            path = TARGET / ("%03d_%s.4bpp" % (species, variant))
            palette_path = TARGET / ("%03d_%s.gbapal" % (species, variant))
            frame_size = size * size // 2
            pixels = variants[variant]["tiles"]
            palette = variants[variant]["palette"]
            if len(pixels) != 16 * frame_size or len(palette) != 32:
                raise ValueError("frame/palette size incorrect")
            outputs.extend(((path, pixels), (palette_path, palette)))
            lines = [
                'static const u32 %sPixels[] = INCBIN_U32("%s");' % (name, path.as_posix()),
                'static const u16 %sPalette[] = INCBIN_U16("%s");' % (name, palette_path.as_posix()),
                'static const struct SpriteFrameImage %sImages[] = {' % name,
            ]
            lines.extend("    { (const u8 *)%sPixels + %d, %d }," %
                         (name, i * frame_size, frame_size) for i in range(16))
            lines.extend((
                "};",
                "static const struct ObjectEventGraphicsInfo %sGraphics = {" % name,
                "    .tileTag = TAG_NONE,",
                "    .paletteTag = TAG_NONE,",
                "    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,",
                "    .size = %d," % frame_size,
                "    .width = %d," % size,
                "    .height = %d," % size,
                "    .paletteSlot = PALSLOT_NPC_1,",
                "    .shadowSize = SHADOW_SIZE_M,",
                "    .inanimate = FALSE,",
                "    .disableReflectionPaletteLoad = FALSE,",
                "    .tracks = TRACKS_FOOT,",
                "    .oam = &gObjectEventBaseOam_%dx%d," % (size, size),
                "    .subspriteTables = gObjectEventSpriteOamTables_%dx%d," % (size, size),
                "    .anims = sFollowerPilotAnims,",
                "    .images = %sImages," % name,
                "    .affineAnims = gDummySpriteAffineAnimTable,",
                "};",
            ))
            declarations.append("\n".join(lines))
            names.append(name)
        gfx.append("    [%d] = { &%sGraphics, &%sGraphics }," %
                   (species, names[0], names[1]))
        pals.append("    [%d] = { %sPalette, %sPalette }," %
                    (species, names[0], names[1]))
    marker = "/* B10 species-keyed animated graphics contract."
    if original.count(marker) != 1:
        raise ValueError("missing registry marker")
    updated = original.replace(marker, "\n".join(declarations) + "\n" + marker)
    for anchor, entries in (
        ("sFollowerRegisteredGraphics[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2]", gfx),
        ("sFollowerRegisteredPalettes[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2]", pals),
    ):
        start = updated.index(anchor)
        offset = updated.index(SENTINEL, start)
        updated = (updated[:offset] + SENTINEL + "\n" + "\n".join(entries) +
                   updated[offset + len(SENTINEL):])
    # No external source ever enters git; only temporary runner checkout files.
    for relative, data in outputs:
        file = checkout / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(data)
    hp.write_text(updated)
    print("Installed %d National Dex normal/shiny sprite pairs into temporary checkout" % len(ids))

def self_test():
    with tempfile.TemporaryDirectory() as folder:
        base = Path(folder)
        source = base / "upstream"
        checkout = base / "checkout"
        (checkout / HEADER).parent.mkdir(parents=True)
        (checkout / HEADER).write_text(
            marker_test := (
                "/* B10 species-keyed animated graphics contract. */\n"
                "sFollowerRegisteredGraphics[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2] = {\n"
                + SENTINEL + "\n};\n"
                "sFollowerRegisteredPalettes[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2] = {\n"
                + SENTINEL + "\n};\n"
            ))
        for species, name in ((1, "bulbasaur"), (252, "treecko")):
            for variant in ("regular", "shiny"):
                for direction in DIRECTIONS:
                    p = source / ("%03d_%s" % (species, name)) / variant / (direction + ".png")
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_bytes(synthetic_apng(size=32))
        install(source, checkout, [252, 1])
        contents = (checkout / HEADER).read_text()
        assert "[252] = { &sFullFollower252NormalGraphics" in contents
        assert "[1] = { &sFullFollower001NormalGraphics" in contents
        assert "sFullFollower252ShinyPalette" in contents
        assert (checkout / TARGET / "252_shiny.4bpp").stat().st_size == 8192
        try:
            install(source, checkout, [1])
        except ValueError:
            pass
        else:
            raise AssertionError("unexpected overwrite")
    print("National registry compiler bindings, 16 frames and duplicate protection PASS")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--checkout", type=Path, default=Path("."))
    parser.add_argument("--species", type=int, nargs="+")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.source and args.species:
        install(args.source, args.checkout, args.species)
    else:
        parser.error("requires --source and --species or --self-test")
