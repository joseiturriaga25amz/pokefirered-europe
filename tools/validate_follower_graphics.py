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
    print("Synthetic follower graphics contract PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.manifest is None:
        parser.error("--manifest is required unless --self-test")
    try:
        errors = check_manifest(json.loads(args.manifest.read_text()), args.root.resolve())
    except (OSError, ValueError) as exc:
        print("manifest error:", exc, file=sys.stderr)
        return 1
    for error in errors[:50]:
        print("ERROR:", error, file=sys.stderr)
    if errors:
        print("%s coverage/graphics issues; only first 50 printed" % len(errors), file=sys.stderr)
        return 1
    print("386 normal/shiny x 4 directional indexed 4bpp sheets: contract PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
