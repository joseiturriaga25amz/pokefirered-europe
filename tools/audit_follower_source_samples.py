#!/usr/bin/env python3
"""Read-only sample audit of HGSS APNGs; outputs metadata, not artwork.

A pinned upstream revision is fetched into a temporary directory on the CI
runner. No third-party sprites are committed, built into Full or uploaded.
Results classify source compatibility; blocked input is not a build regression.
Network/source-fetch failures are errors and must not be reported as readiness.
"""
import hashlib
import json
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

from convert_follower_apng import DIRECTIONS, VARIANTS, pack_variant, read_apng, rgb555

SOURCE_REPO = "teobz/pkmn-hgss-animated-overworld-sprites"
SOURCE_REVISION = "f9ee9f83d0f53b196b64d65f7bb70369b196f33b"
# Representative Gen I-III color, rare/form, shiny and 64px pressure cases.
# The 20-sample gate is evidence of feasibility, NOT 386/386 acceptance.
SAMPLES = (
    (1, "001_bulbasaur"), (3, "003_venusaur"), (6, "006_charizard"),
    (25, "025_pikachu"), (65, "065_alakazam"), (94, "094_gengar"),
    (130, "130_gyarados"), (143, "143_snorlax"), (150, "150_mewtwo"),
    (151, "151_mew"), (201, "201_unown"), (248, "248_tyranitar"),
    (249, "249_lugia"), (321, "321_wailord"), (351, "351_castform"),
    (376, "376_metagross"), (382, "382_kyogre"), (383, "383_groudon"),
    (384, "384_rayquaza"), (386, "386_deoxys"),
)
OBJ_VRAM_BYTES = 32 * 1024  # GBA character data for objects, not free-space count.


def download(url):
    request = urllib.request.Request(url, headers={"User-Agent": "FireRedFull-B10-asset-feasibility/1"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                blob = response.read(250000)
            if not blob.startswith(b"\x89PNG\r\n\x1a\n"):
                raise ValueError("unexpected upstream asset format")
            return blob
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as error:
            if isinstance(error, urllib.error.HTTPError) and error.code not in (429, 500, 502, 503, 504):
                raise RuntimeError("upstream sample asset unavailable: " + url) from error
            if attempt == 2:
                raise RuntimeError("upstream sample network unavailable: " + url) from error
            time.sleep(attempt + 1)


def summarize_variant(folder):
    colors = set()
    direction_stats = {}
    semi_alpha = 0
    dimension = None
    for direction in DIRECTIONS:
        size, frames = read_apng(folder / (direction + ".png"))
        if dimension is not None and dimension != size:
            raise ValueError("inconsistent frame dimension")
        dimension = size
        converted = []
        for frame in frames:
            visible = []
            for pixel in frame:
                if pixel[3] not in (0, 255):
                    semi_alpha += 1
                    visible.append(None)
                else:
                    c = rgb555(pixel)
                    if c is not None:
                        colors.add(c)
                    visible.append(c)
            converted.append(tuple(visible))
        direction_stats[direction] = {
            "native_frames": len(frames),
            "unique_BGR555_frames": len(set(converted))
        }
    reasons = []
    if len(colors) > 15:
        reasons.append("palette_over_15_colors")
    if semi_alpha:
        reasons.append("semi_transparent_pixels")
    if any(d["unique_BGR555_frames"] < 2 for d in direction_stats.values()):
        reasons.append("animation_collapses_after_color_quantization")
    # One frame is resident in object tiles; sixteen walking frames belong
    # in ROM and must be streamed via Gen III SpriteFrameImage, not copied
    # as a single 64x64 sheet into the 32-KiB OBJ tile area.
    frame_bytes = dimension * dimension // 2
    result = {
        "frame_px": dimension,
        "frame_vram_bytes": frame_bytes,
        "follower_plus_reflection_frame_bytes": frame_bytes * 2,
        "four_directions_sixteen_frames_rom_bytes": frame_bytes * 16,
        "obj_vram_tile_bytes": OBJ_VRAM_BYTES,
        "unique_opaque_BGR555_colors": len(colors),
        "semi_transparent_pixel_instances": semi_alpha,
        "directions": direction_stats,
        "status": "SOURCE_BLOCKED" if reasons else "SOURCE_FEASIBLE",
        "reasons": reasons,
    }
    if not reasons:
        try:
            out_size, tiles, palette, palette_colors = pack_variant(folder)
            result["packed_bytes_4bpp"] = len(tiles)
            result["packed_palette_bytes"] = len(palette)
            result["packed_color_count"] = palette_colors
            # Hash of the actual GBA renderable pixels *and* palette, rather
            # than an APNG filename or source-byte difference.
            result["packed_render_sha256"] = hashlib.sha256(tiles + palette).hexdigest()
            if out_size != dimension:
                raise AssertionError("size mismatch after packing")
        except (ValueError, AssertionError) as error:
            result["status"] = "CONVERSION_ERROR"
            result["reasons"] = [str(error)]
    return result


def main():
    results = []
    with tempfile.TemporaryDirectory(prefix="follower-source-audit-") as temp:
        root = Path(temp)
        for species, folder in SAMPLES:
            entry = {"species": species, "folder": folder, "variants": {}}
            for variant, variant_folder in VARIANTS:
                variant_root = root / folder / variant_folder
                variant_root.mkdir(parents=True)
                sha = hashlib.sha256()
                for direction in DIRECTIONS:
                    url = ("https://raw.githubusercontent.com/" + SOURCE_REPO + "/"
                           + SOURCE_REVISION + "/APNG/by-pokemon/" + folder + "/"
                           + variant_folder + "/" + direction + ".png")
                    data = download(url)
                    sha.update(data)
                    (variant_root / (direction + ".png")).write_bytes(data)
                entry["variants"][variant] = summarize_variant(variant_root)
                entry["variants"][variant]["input_bundle_sha256"] = sha.hexdigest()
            regular = entry["variants"]["normal"]
            shiny = entry["variants"]["shiny"]
            if regular["frame_px"] != shiny["frame_px"]:
                entry["normal_shiny_size_mismatch"] = True
            if regular["status"] == "SOURCE_FEASIBLE" and shiny["status"] == "SOURCE_FEASIBLE":
                entry["normal_shiny_distinct_after_conversion"] = (
                    regular["packed_render_sha256"] != shiny["packed_render_sha256"]
                )
            results.append(entry)
    report = {
        "scope": "READ_ONLY_SOURCE_FEASIBILITY_NOT_REDISTRIBUTION_OR_MYBOY",
        "source_revision": SOURCE_REVISION,
        "species_count": len(results),
        "species": results,
    }
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    compatible = sum(all(x["status"] == "SOURCE_FEASIBLE"
                         for x in entry["variants"].values()) for entry in results)
    distinct = sum(entry.get("normal_shiny_distinct_after_conversion") is True
                   for entry in results)
    large = sum(any(x["frame_px"] == 64 for x in entry["variants"].values())
                for entry in results)
    print("HGSS pinned real APNG sample: %s species, %s normal+shiny pairs "
          "convertible losslessly, %s genuinely distinct pairs, %s 64px species"
          % (len(results), compatible, distinct, large))
    print("Source-blocked species remain research tasks; no actual art is committed or integrated.")


if __name__ == "__main__":
    main()
