#!/usr/bin/env python3
"""Strict pre-import coverage gate for licensed Gen III follower overworld sheets.

Contract: JSON list with one record for each national Dex ID 1..386:
{"species":1,"size":32,"normal":{"down":"...png","up":"...png","left":"...png","right":"...png"},
 "shiny":{"down":"...png","up":"...png","left":"...png","right":"...png"}}
Each directional indexed PNG contains exactly four horizontal square frames.
No third-party graphics are bundled by this tool. Filename validation is not
visual, animation-timing, provenance, runtime or MyBoy acceptance.
"""
import argparse
import json
from pathlib import Path
import struct
import sys
import tempfile
import zlib

DIRECTIONS = ("down", "up", "left", "right")
VARIANTS = ("normal", "shiny")
SIZES = (16, 32, 64)
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_header(path):
    with path.open("rb") as stream:
        if stream.read(8) != PNG_SIGNATURE:
            raise ValueError("not PNG")
        length_bytes = stream.read(4)
        if len(length_bytes) != 4:
            raise ValueError("truncated PNG")
        length = struct.unpack(">I", length_bytes)[0]
        if stream.read(4) != b"IHDR" or length != 13:
            raise ValueError("invalid IHDR")
        data = stream.read(13)
        crc = stream.read(4)
        if len(data) != 13 or len(crc) != 4:
            raise ValueError("truncated IHDR")
        if zlib.crc32(b"IHDR" + data) & 0xffffffff != struct.unpack(">I", crc)[0]:
            raise ValueError("bad IHDR CRC")
        width, height, depth, color, compression, filtering, interlace = struct.unpack(">IIBBBBB", data)
        if (depth, color, compression, filtering, interlace) != (4, 3, 0, 0, 0):
            raise ValueError("requires indexed 4bpp PNG without interlace")
        # Inspect the complete PNG chunk structure, not just its filename/header.
        colors = None
        has_data = False
        finished = False
        while not finished:
            length_bytes = stream.read(4)
            if len(length_bytes) != 4:
                raise ValueError("missing IEND")
            length = struct.unpack(">I", length_bytes)[0]
            if length > 16 * 1024 * 1024:
                raise ValueError("oversized PNG chunk")
            kind = stream.read(4)
            payload = stream.read(length)
            crc = stream.read(4)
            if len(kind) != 4 or len(payload) != length or len(crc) != 4:
                raise ValueError("truncated PNG chunk")
            if zlib.crc32(kind + payload) & 0xffffffff != struct.unpack(">I", crc)[0]:
                raise ValueError("bad PNG chunk CRC")
            if kind == b"PLTE":
                colors = len(payload) // 3
                if len(payload) % 3 or not (1 <= colors <= 16):
                    raise ValueError("invalid 16-color palette")
            elif kind == b"IDAT":
                has_data = True
            elif kind in (b"acTL", b"fcTL", b"fdAT"):
                raise ValueError("APNG must first be flattened into frames")
            elif kind == b"IEND":
                finished = True
        if colors is None or not has_data or stream.read(1):
            raise ValueError("incomplete PNG")
        return width, height, colors


def check_manifest(manifest, root):
    errors = []
    if not isinstance(manifest, list):
        return ["manifest must be a JSON list"]
    by_id = {}
    for entry in manifest:
        if not isinstance(entry, dict) or type(entry.get("species")) is not int:
            errors.append("entry has no integer species ID")
            continue
        species = entry["species"]
        if species in by_id:
            errors.append("duplicate species %s" % species)
        by_id[species] = entry
    expected = set(range(1, 387))
    if set(by_id) != expected:
        errors.append("species coverage: missing=%s extra=%s" % (
            sorted(expected - set(by_id)), sorted(set(by_id) - expected)))
    owned_paths = set()
    for species, entry in sorted(by_id.items()):
        size = entry.get("size")
        if size not in SIZES:
            errors.append("%s: size must be 16, 32 or 64" % species)
            continue
        for variant in VARIANTS:
            directions = entry.get(variant)
            if not isinstance(directions, dict) or set(directions) != set(DIRECTIONS):
                errors.append("%s/%s: require all four directions" % (species, variant))
                continue
            for direction in DIRECTIONS:
                name = directions[direction]
                if not isinstance(name, str) or not name.endswith(".png"):
                    errors.append("%s/%s/%s: invalid filename" % (species, variant, direction))
                    continue
                path = Path(name)
                if path.is_absolute() or ".." in path.parts or name in owned_paths:
                    errors.append("%s/%s/%s: unsafe/duplicate path" % (species, variant, direction))
                    continue
                owned_paths.add(name)
                try:
                    width, height, colors = png_header(root / path)
                    if (width, height) != (size * 4, size):
                        errors.append("%s/%s/%s: expected four %sx%s frames" % (
                            species, variant, direction, size, size))
                except (OSError, ValueError) as exc:
                    errors.append("%s/%s/%s: %s" % (species, variant, direction, exc))
    return errors


def check_packed_manifest(manifest, root, expected_species=None):
    """Verify exactly the 16-frame files emitted by convert_follower_apng.py.

    A one-species expected_species is permitted ONLY by the synthetic unit test.
    The normal CLI always requires national Dex IDs 1..386.
    """
    errors = []
    if not isinstance(manifest, list):
        return ["packed manifest must be a JSON list"], 0
    expected = set(range(1, 387)) if expected_species is None else set(expected_species)
    by_id = {}
    for entry in manifest:
        if not isinstance(entry, dict) or type(entry.get("species")) is not int:
            errors.append("packed entry lacks integer species")
            continue
        species = entry["species"]
        if species in by_id:
            errors.append("duplicate packed species %s" % species)
        by_id[species] = entry
    if set(by_id) != expected:
        errors.append("packed coverage missing=%s extra=%s" % (
            sorted(expected - set(by_id)), sorted(set(by_id) - expected)))
    seen_paths = set()
    raw_bytes = 0
    root = root.resolve()
    for species, entry in sorted(by_id.items()):
        size = entry.get("size")
        if size not in SIZES:
            errors.append("%s: invalid packed dimensions" % species)
            continue
        if (entry.get("frames_per_direction") != 4
                or entry.get("direction_order") != list(DIRECTIONS)):
            errors.append("%s: wrong animation frame/direction order" % species)
            continue
        variants = entry.get("variants")
        if not isinstance(variants, dict) or set(variants) != set(VARIANTS):
            errors.append("%s: normal and shiny packed variants required" % species)
            continue
        frame_bytes = size * size // 2
        sheet_bytes = frame_bytes * 16
        render_keys = {}
        for variant in VARIANTS:
            info = variants[variant]
            if not isinstance(info, dict):
                errors.append("%s/%s: invalid packed record" % (species, variant))
                continue
            colors = info.get("palette_visible_colors")
            if (type(colors) is not int or not 1 <= colors <= 15
                    or info.get("frame_bytes") != frame_bytes
                    or info.get("sheet_bytes") != sheet_bytes):
                errors.append("%s/%s: invalid palette or GBA frame budget" % (species, variant))
                continue
            resources = {}
            for attr, ext, target_size in (
                    ("tiles", ".4bpp", sheet_bytes), ("palette", ".gbapal", 32)):
                name = info.get(attr)
                if not isinstance(name, str) or not name.endswith(ext):
                    errors.append("%s/%s: invalid %s filename" % (species, variant, attr))
                    continue
                path = Path(name)
                target = (root / path).resolve()
                if (path.is_absolute() or ".." in path.parts
                        or not target.is_relative_to(root) or name in seen_paths):
                    errors.append("%s/%s: unsafe/reused resource path" % (species, variant))
                    continue
                seen_paths.add(name)
                try:
                    blob = target.read_bytes()
                except OSError as exc:
                    errors.append("%s/%s: missing %s: %s" % (species, variant, attr, exc))
                    continue
                if len(blob) != target_size:
                    errors.append("%s/%s: %s expected %s bytes, found %s" % (
                        species, variant, attr, target_size, len(blob)))
                    continue
                resources[attr] = blob
            if set(resources) != {"tiles", "palette"}:
                continue
            colors_raw = struct.unpack("<16H", resources["palette"])
            if colors_raw[0] != 0 or any(color & 0x8000 for color in colors_raw):
                errors.append("%s/%s: invalid transparent/BGR555 palette" % (species, variant))
            if any(colors_raw[i] != 0 for i in range(colors + 1, 16)):
                errors.append("%s/%s: palette contains undeclared colors" % (species, variant))
            indices = set()
            frames = [
                resources["tiles"][offset:offset + frame_bytes]
                for offset in range(0, sheet_bytes, frame_bytes)
            ]
            for frame in frames:
                for byte in frame:
                    indices.add(byte & 15)
                    indices.add(byte >> 4)
            if not indices.intersection(range(1, 16)):
                errors.append("%s/%s: all frames transparent" % (species, variant))
            if max(indices) > colors:
                errors.append("%s/%s: sprite pixels index beyond palette" % (species, variant))
            for direction_idx, direction in enumerate(DIRECTIONS):
                direction_frames = frames[direction_idx * 4:(direction_idx + 1) * 4]
                if len(set(direction_frames)) < 2:
                    errors.append("%s/%s/%s: not animated after 4bpp conversion" % (
                        species, variant, direction))
            render_keys[variant] = (resources["tiles"], resources["palette"])
            raw_bytes += sheet_bytes + 32
        if len(render_keys) == 2 and render_keys["normal"] == render_keys["shiny"]:
            errors.append("%s: normal and shiny would render identically" % species)
    return errors, raw_bytes


def self_test():
    # Synthetic GBA-indexed PNGs only; no Pokémon copyrighted artwork.
    def chunk(tag, payload):
        return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", zlib.crc32(tag + payload) & 0xffffffff)

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        # 16x16 * 4 frames, 4bpp indexed, with one transparent-color index.
        header = struct.pack(">IIBBBBB", 64, 16, 4, 3, 0, 0, 0)
        scanlines = b"".join(b"\x00" + b"\x00" * 32 for _ in range(16))
        png = (PNG_SIGNATURE + chunk(b"IHDR", header) + chunk(b"PLTE", b"\x00\x00\x00" * 16)
               + chunk(b"IDAT", zlib.compress(scanlines)) + chunk(b"IEND", b""))
        (root / "frame.png").write_bytes(png)
        assert png_header(root / "frame.png") == (64, 16, 16)
        assert any("coverage" in err for err in check_manifest([], root))
        assert any("direction" in err for err in check_manifest(
            [{"species": 1, "size": 16, "normal": {}, "shiny": {}}], root))
        damaged = bytearray(png)
        damaged[25] = 6
        (root / "damaged.png").write_bytes(damaged)
        try:
            png_header(root / "damaged.png")
        except ValueError:
            pass
        else:
            raise AssertionError("invalid graphic accepted")

        # Validate packed output contract separately from the pre-import PNGs.
        packed_root = root / "packed"
        (packed_root / "001").mkdir(parents=True)
        frame = 16 * 16 // 2
        base_frames = bytes().join(
            bytes(((i % 3) + 1) * 0x11 for _ in range(frame))
            for i in range(16))
        assert len(base_frames) == frame * 16
        for variant in VARIANTS:
            (packed_root / "001" / (variant + ".4bpp")).write_bytes(base_frames)
            colors = [0, 0x001f, 0x03e0, 0x7c00] if variant == "normal" else [0, 0x7c00, 0x03e0, 0x001f]
            (packed_root / "001" / (variant + ".gbapal")).write_bytes(
                struct.pack("<16H", *(colors + [0] * 12)))
        entry = {"species": 1, "size": 16, "frames_per_direction": 4,
                 "direction_order": list(DIRECTIONS), "variants": {}}
        for variant in VARIANTS:
            entry["variants"][variant] = {
                "tiles": "001/%s.4bpp" % variant,
                "palette": "001/%s.gbapal" % variant,
                "palette_visible_colors": 3,
                "frame_bytes": frame,
                "sheet_bytes": frame * 16}
        packed = [entry]
        errors, total = check_packed_manifest(packed, packed_root, {1})
        assert not errors, errors
        assert total == frame * 16 * 2 + 64
        assert any("coverage" in err for err in check_packed_manifest(packed, packed_root)[0])
        corrupted = packed_root / "001" / "shiny.4bpp"
        corrupted.write_bytes(b"\x00" * (frame * 16))
        assert any("transparent" in err or "not animated" in err for err in
                   check_packed_manifest(packed, packed_root, {1})[0])
        corrupted.write_bytes(base_frames[:-1])
        assert any("expected" in err for err in
                   check_packed_manifest(packed, packed_root, {1})[0])
        corrupted.write_bytes(base_frames)
        duplicate = [entry, dict(entry)]
        assert any("duplicate packed species" in err for err in
                   check_packed_manifest(duplicate, packed_root, {1})[0])

    print("Synthetic follower graphics source and packed 4bpp contract PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--packed-manifest", type=Path, help="validate convert_follower_apng.py output; requires 386 species")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if (args.manifest is None) == (args.packed_manifest is None):
        parser.error("provide exactly one of --manifest or --packed-manifest, unless --self-test")
    try:
        if args.packed_manifest is not None:
            errors, raw_bytes = check_packed_manifest(
                json.loads(args.packed_manifest.read_text()), args.root)
        else:
            errors = check_manifest(json.loads(args.manifest.read_text()), args.root)
            raw_bytes = None
    except (OSError, ValueError) as exc:
        print("manifest error:", exc, file=sys.stderr)
        return 1
    for error in errors[:50]:
        print("ERROR:", error, file=sys.stderr)
    if errors:
        print("%s coverage/graphics issues; only first 50 printed" % len(errors), file=sys.stderr)
        return 1
    if raw_bytes is None:
        print("386 normal/shiny x 4 directional indexed 4bpp PNG sheets: contract PASS")
    else:
        print("386 normal/shiny x 4 directions x 4 frames: packed 4bpp contract PASS")
        print("Raw packed bytes (not resident GBA VRAM):", raw_bytes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
