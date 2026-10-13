#!/usr/bin/env python3
"""Convert four-frame RGBA HGSS-style APNG overworlds to Gen III tiled 4bpp.

Input layout (read-only): 001_bulbasaur/{regular,shiny}/{down,up,left,right}.png.
Output (local only): 001/{normal,shiny}.{4bpp,gbapal} and conversion_manifest.json.
Exact 15 visible BGR555 colors maximum per variant; excessive colors FAIL rather
than silently degrading artwork. No Pokemon graphics are distributed here.
"""
import argparse
import json
import re
import struct
import tempfile
import zlib
from pathlib import Path

PNG_SIG = b"\x89PNG\r\n\x1a\n"
DIRECTIONS = ("down", "up", "left", "right")
VARIANTS = (("normal", "regular"), ("shiny", "shiny"))
SIZES = (16, 32, 64)


def u32(data, offset=0):
    return struct.unpack_from(">I", data, offset)[0]


def chunks(blob):
    if not blob.startswith(PNG_SIG):
        raise ValueError("bad PNG signature")
    at = len(PNG_SIG)
    ended = False
    while at < len(blob):
        if at + 12 > len(blob):
            raise ValueError("truncated PNG chunk")
        length = u32(blob, at)
        if length > 1024 * 1024 or at + 12 + length > len(blob):
            raise ValueError("invalid PNG chunk length")
        kind = blob[at + 4:at + 8]
        data = blob[at + 8:at + 8 + length]
        crc = u32(blob, at + 8 + length)
        if zlib.crc32(kind + data) & 0xffffffff != crc:
            raise ValueError("PNG CRC error")
        at += 12 + length
        yield kind, data
        if kind == b"IEND":
            ended = True
            break
    if not ended or at != len(blob):
        raise ValueError("missing IEND or trailing data")


def paeth(a, b, c):
    p = a + b - c
    d = (abs(p - a), abs(p - b), abs(p - c))
    return (a, b, c)[d.index(min(d))]


def rgba_scanlines(compressed, width, height):
    pitch = width * 4
    try:
        decoded = zlib.decompress(compressed)
    except zlib.error as exc:
        raise ValueError("invalid APNG deflate stream") from exc
    if len(decoded) != (pitch + 1) * height:
        raise ValueError("invalid frame pixel payload size")
    previous = bytearray(pitch)
    pixels = bytearray()
    at = 0
    for _ in range(height):
        filt = decoded[at]
        at += 1
        row = bytearray(decoded[at:at + pitch])
        at += pitch
        if filt > 4:
            raise ValueError("unsupported PNG row filter")
        for i in range(pitch):
            a = row[i - 4] if i >= 4 else 0
            b = previous[i]
            c = previous[i - 4] if i >= 4 else 0
            if filt == 1:
                row[i] = (row[i] + a) & 255
            elif filt == 2:
                row[i] = (row[i] + b) & 255
            elif filt == 3:
                row[i] = (row[i] + ((a + b) // 2)) & 255
            elif filt == 4:
                row[i] = (row[i] + paeth(a, b, c)) & 255
        pixels.extend(row)
        previous = row
    return pixels


def alpha_over(src, dst):
    sa = src[3]
    da = dst[3]
    oa = sa + (da * (255 - sa) + 127) // 255
    if oa == 0:
        return (0, 0, 0, 0)
    out = []
    for k in range(3):
        numerator = src[k] * sa * 255 + dst[k] * da * (255 - sa)
        out.append((numerator + (oa * 255) // 2) // (oa * 255))
    return (*out, oa)


def read_apng(path, allow_metapod_three_down=False):
    header = None
    declared = None
    controls = []
    expected_seq = 0
    seen_data = False
    for kind, payload in chunks(path.read_bytes()):
        if kind == b"IHDR":
            if header is not None or len(payload) != 13:
                raise ValueError("bad IHDR")
            w, h, depth, color, compression, filtering, interlace = struct.unpack(">IIBBBBB", payload)
            if w not in SIZES or h != w or (depth, color, compression, filtering, interlace) != (8, 6, 0, 0, 0):
                raise ValueError("expected 16/32/64 square 8-bit RGBA APNG")
            header = (w, h)
        elif kind == b"acTL":
            if len(payload) != 8 or declared is not None or seen_data:
                raise ValueError("bad acTL")
            declared = u32(payload)
        elif kind == b"fcTL":
            if declared is None or len(payload) != 26:
                raise ValueError("bad fcTL")
            seq, fw, fh, x, y, delay_num, delay_den, dispose, blend = struct.unpack(">IIIIIHHBB", payload)
            if seq != expected_seq or fw == 0 or fh == 0 or x + fw > header[0] or y + fh > header[1]:
                raise ValueError("bad APNG frame control")
            if dispose > 2 or blend > 1:
                raise ValueError("unknown APNG blend/dispose")
            expected_seq += 1
            controls.append({"w": fw, "h": fh, "x": x, "y": y, "dispose": dispose,
                             "blend": blend, "delay_num": delay_num, "delay_den": delay_den,
                             "compressed": bytearray()})
        elif kind in (b"IDAT", b"fdAT"):
            if not controls or declared is None:
                raise ValueError("missing APNG frame control")
            if kind == b"IDAT":
                if len(controls) != 1:
                    raise ValueError("IDAT after first frame")
                controls[-1]["compressed"].extend(payload)
            else:
                if len(payload) < 4 or u32(payload) != expected_seq or len(controls) < 2:
                    raise ValueError("invalid fdAT sequence")
                expected_seq += 1
                controls[-1]["compressed"].extend(payload[4:])
            seen_data = True
    # The pinned Metapod *down* source has three genuine frames with
    # 150/300/150 ms timings, in both palettes. Duplicate only the middle
    # frame to retain 150/150/150/150 ms cadence in a four-slot GBA sheet.
    # This is a duration hold, not an invented sprite or a general fallback.
    expected = 3 if allow_metapod_three_down else 4
    if declared != expected or len(controls) != expected or not seen_data:
        raise ValueError("requires exactly %d animated source frames" % expected)
    if allow_metapod_three_down:
        durations = [(frame["delay_num"], frame["delay_den"] or 100) for frame in controls]
        first, middle, last = durations
        if (first[0] * last[1] != last[0] * first[1]
                or middle[0] * first[1] != 2 * first[0] * middle[1]):
            raise ValueError("unexpected Metapod three-frame timing; manual review required")
    w, h = header
    canvas = [(0, 0, 0, 0)] * (w * h)
    frames = []
    for control in controls:
        if not control["compressed"]:
            raise ValueError("empty APNG frame")
        frame = rgba_scanlines(bytes(control["compressed"]), control["w"], control["h"])
        previous = canvas.copy() if control["dispose"] == 2 else None
        for sy in range(control["h"]):
            for sx in range(control["w"]):
                k = (sy * control["w"] + sx) * 4
                source = tuple(frame[k:k + 4])
                dest = (sy + control["y"]) * w + sx + control["x"]
                canvas[dest] = source if control["blend"] == 0 else alpha_over(source, canvas[dest])
        frames.append(canvas.copy())
        if control["dispose"] == 1:
            for sy in range(control["h"]):
                for sx in range(control["w"]):
                    canvas[(sy + control["y"]) * w + sx + control["x"]] = (0, 0, 0, 0)
        elif previous is not None:
            canvas = previous
    if len(set(tuple(frame) for frame in frames)) < 2:
        raise ValueError("animated source has no distinct frames")
    if allow_metapod_three_down:
        frames.insert(2, frames[1].copy())
    return w, frames


def rgb555(pixel):
    r, g, b, a = pixel
    if a == 0:
        return None
    if a != 255:
        raise ValueError("semi-transparent pixel needs explicit visual review")
    return ((b * 31 + 127) // 255 << 10
            | (g * 31 + 127) // 255 << 5
            | (r * 31 + 127) // 255)


def tiled_frame(frame, width, lookup):
    indices = [0 if (c := rgb555(pixel)) is None else lookup[c] for pixel in frame]
    output = bytearray()
    for tile_y in range(0, width, 8):
        for tile_x in range(0, width, 8):
            for y in range(8):
                for x in range(0, 8, 2):
                    pos = (tile_y + y) * width + tile_x + x
                    output.append(indices[pos] | (indices[pos + 1] << 4))
    assert len(output) == width * width // 2
    return output


def pack_variant(source_dir, species=None):
    all_frames = []
    width = None
    per_direction = {}
    for direction in DIRECTIONS:
        candidate, frames = read_apng(
            source_dir / (direction + ".png"),
            allow_metapod_three_down=(species == 11 and direction == "down"))
        if width is not None and width != candidate:
            raise ValueError("inconsistent sprite frame dimensions")
        width = candidate
        per_direction[direction] = frames
        all_frames.extend(frames)
    palette_colors = sorted({color for frame in all_frames for pixel in frame
                             if (color := rgb555(pixel)) is not None})
    if len(palette_colors) > 15:
        raise ValueError("needs %d opaque colors after BGR555 conversion; maximum is 15" % len(palette_colors))
    lookup = {color: i + 1 for i, color in enumerate(palette_colors)}
    tiles = bytearray()
    for direction in DIRECTIONS:
        for frame in per_direction[direction]:
            tiles.extend(tiled_frame(frame, width, lookup))
    # Palette entry zero is transparent and index 1..15 are opaque.
    palette = [0] + palette_colors + [0] * (15 - len(palette_colors))
    return width, bytes(tiles), struct.pack("<16H", *palette), len(palette_colors)


def locate_species(root, species):
    matches = [p for p in root.glob("%03d_*" % species)
               if p.is_dir() and re.fullmatch(r"%03d_[a-z0-9_]+" % species, p.name)]
    if len(matches) != 1:
        raise ValueError("%03d: expected exactly one species folder, got %d" % (species, len(matches)))
    return matches[0]


def pack_species(root, species):
    folder = locate_species(root, species)
    result = {}
    dimension = None
    for variant, source_variant in VARIANTS:
        size, tiles, pal, colors = pack_variant(folder / source_variant, species=species)
        if dimension is not None and size != dimension:
            raise ValueError("%03d: normal/shiny frame dimensions disagree" % species)
        dimension = size
        result[variant] = {"tiles": tiles, "palette": pal, "colors": colors}
    return dimension, result


def convert(root, out, ids):
    if root.resolve() == out.resolve() or root.resolve() in out.resolve().parents:
        raise ValueError("output cannot be inside input asset directory")
    staged = []
    manifest = []
    for species in ids:
        size, variants = pack_species(root, species)
        entry = {"species": species, "size": size, "frames_per_direction": 4,
                 "direction_order": list(DIRECTIONS), "variants": {}}
        for variant, _ in VARIANTS:
            tile_path = "%03d/%s.4bpp" % (species, variant)
            pal_path = "%03d/%s.gbapal" % (species, variant)
            info = variants[variant]
            staged.extend([(tile_path, info["tiles"]), (pal_path, info["palette"])])
            entry["variants"][variant] = {
                "tiles": tile_path, "palette": pal_path,
                "palette_visible_colors": info["colors"],
                "frame_bytes": size * size // 2,
                "sheet_bytes": len(info["tiles"])
            }
        manifest.append(entry)
    for file, data in staged:
        target = out / file
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    out.mkdir(parents=True, exist_ok=True)
    (out / "conversion_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def chunk(kind, payload):
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xffffffff)


def synthetic_apng(size=16, frame_count=4, color_bias=0):
    # First frame full-canvas; later frames are PARTIAL rectangles as in HGSS.
    output = PNG_SIG + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
    output += chunk(b"acTL", struct.pack(">II", frame_count, 0))
    seq = 0
    for index in range(frame_count):
        w, h, x, y = (size, size, 0, 0) if index == 0 else (8, 8, 3, 3)
        # Native Metapod downward timing: 150, 300, 150 ms.
        numerator = 3 if frame_count == 3 else 1
        denominator = 10 if frame_count != 3 or index == 1 else 20
        output += chunk(b"fcTL", struct.pack(">IIIIIHHBB", seq, w, h, x, y,
                                              numerator, denominator, 0, 0))
        seq += 1
        pixel = bytes((index * 55 + color_bias, 64, 80, 255))
        raw = (b"\x00" + pixel * w) * h
        comp = zlib.compress(raw)
        if index == 0:
            output += chunk(b"IDAT", comp)
        else:
            output += chunk(b"fdAT", struct.pack(">I", seq) + comp)
            seq += 1
    return output + chunk(b"IEND", b"")


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "input"
        dest = Path(tmp) / "built"
        for variant in ("regular", "shiny"):
            for direction in DIRECTIONS:
                path = root / "001_synthetic" / variant / (direction + ".png")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(synthetic_apng())
        width, frames = read_apng(root / "001_synthetic" / "regular" / "down.png")
        assert width == 16 and len(frames) == 4 and frames[0] != frames[1]
        report = convert(root, dest, [1])
        assert report[0]["size"] == 16 and report[0]["frames_per_direction"] == 4
        assert (dest / "001/normal.4bpp").stat().st_size == 16 * 16 // 2 * 16
        assert (dest / "001/shiny.gbapal").stat().st_size == 32
        assert len(set((dest / "001/normal.4bpp").read_bytes())) > 1
        data = bytearray(synthetic_apng())
        data[-10] ^= 1
        bad = root / "001_synthetic" / "regular" / "up.png"
        bad.write_bytes(data)
        try:
            pack_variant(bad.parent)
        except ValueError:
            pass
        else:
            raise AssertionError("corrupt APNG was accepted")

        # Actual Metapod down is three source frames with a held middle pose.
        # Use three-frame synthetic APNG only on species 011 and direction down.
        special = root / "011_metapod"
        for variant in ("regular", "shiny"):
            for direction in DIRECTIONS:
                path = special / variant / (direction + ".png")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(synthetic_apng(
                    frame_count=3 if direction == "down" else 4,
                    color_bias=8 if variant == "shiny" else 0))
        down = special / "regular" / "down.png"
        try:
            read_apng(down)
        except ValueError:
            pass
        else:
            raise AssertionError("generic 3-frame source was accepted")
        size, frames = read_apng(down, allow_metapod_three_down=True)
        assert size == 16 and len(frames) == 4
        assert frames[0] != frames[1] and frames[1] == frames[2] and frames[2] != frames[3]
        special_report = convert(root, dest, [11])
        assert special_report[0]["species"] == 11
        assert (dest / "011/normal.4bpp").stat().st_size == 16 * 16 // 2 * 16
        assert (dest / "011/shiny.gbapal").stat().st_size == 32
        # A different species may never use Metapod's exception.
        other = root / "010_caterpie"
        for variant in ("regular", "shiny"):
            for direction in DIRECTIONS:
                p = other / variant / (direction + ".png")
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(synthetic_apng(frame_count=3 if direction == "down" else 4))
        try:
            convert(root, dest, [10])
        except ValueError:
            pass
        else:
            raise AssertionError("3-frame non-Metapod input was accepted")
    print("Synthetic APNG and Metapod timed three-frame hold -> four GBA slots PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--source", type=Path, help="APNG/by-pokemon directory")
    parser.add_argument("--out", type=Path, help="local output directory (no source artwork in git)")
    parser.add_argument("--species", type=int, nargs="*", help="National Dex IDs; defaults to 1..386")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.source or not args.source.is_dir() or not args.out:
        parser.error("provide --source APNG root and --out")
    ids = list(range(1, 387)) if args.species is None else args.species
    if not ids or len(set(ids)) != len(ids) or any(not 1 <= i <= 386 for i in ids):
        parser.error("species list must contain unique National Dex IDs 1..386")
    report = convert(args.source, args.out, ids)
    print("Packed %d species; normal+shiny, four directions, four frames." % len(report))
    print("Output is local technical data only. Redistribution rights and MyBoy QA are NOT validated.")


if __name__ == "__main__":
    main()
