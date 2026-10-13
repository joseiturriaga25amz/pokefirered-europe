#!/usr/bin/env python3
"""Read-only sample audit of HGSS APNGs; outputs metadata, not artwork.

A pinned upstream revision is fetched into a temporary directory on the CI
runner. No third-party sprites are committed, built into Full or uploaded.
Results classify source compatibility; blocked input is not a build regression.
Network/source-fetch failures are errors and must not be reported as readiness.
"""
import argparse
import hashlib
import io
import re
import zipfile
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


def summarize_variant(folder, species=None):
    colors = set()
    direction_stats = {}
    semi_alpha = 0
    dimension = None
    for direction in DIRECTIONS:
        metapod_hold = species == 11 and direction == "down"
        size, frames = read_apng(folder / (direction + ".png"),
                                 allow_metapod_three_down=metapod_hold)
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
            "native_frames": 3 if metapod_hold else len(frames),
            "packed_frames": len(frames),
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
            out_size, tiles, palette, palette_colors = pack_variant(folder, species=species)
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


def download_archive():
    """Download the pinned upstream archive once, never materialize as a ROM asset."""
    url = ("https://codeload.github.com/" + SOURCE_REPO + "/zip/" + SOURCE_REVISION)
    request = urllib.request.Request(
        url, headers={"User-Agent": "FireRedFull-B10-read-only-coverage/1"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                archive = response.read(100 * 1024 * 1024 + 1)
            if len(archive) > 100 * 1024 * 1024 or not zipfile.is_zipfile(io.BytesIO(archive)):
                raise ValueError("invalid/oversized pinned source archive")
            return archive
        except (urllib.error.URLError, TimeoutError, urllib.error.HTTPError) as exc:
            if isinstance(exc, urllib.error.HTTPError) and exc.code not in (429, 500, 502, 503, 504):
                raise RuntimeError("non-retryable upstream archive response") from exc
            if attempt == 2:
                raise RuntimeError("upstream archive could not be retrieved") from exc
            time.sleep(attempt + 1)


def audit_complete_gen3(archive, first=1, last=386):
    """Audit every Gen I–III Dex ID, reporting blockers rather than dropping IDs.

    A successful *audit run* can report source blockers. Only a 386/386 result
    with all normal/shiny variants distinct would pass future asset-coverage
    acceptance; this audit never means the sprites are integrated in FireRed.
    """
    inventory = {}
    expected_files = {v + "/" + d + ".png" for _, v in VARIANTS for d in DIRECTIONS}
    archive_prefix = re.compile(
        r"^[^/]+/APNG/by-pokemon/(\d{3}_[a-z0-9_-]+)/((?:regular|shiny)/(?:down|up|left|right)\.png)$")
    with zipfile.ZipFile(io.BytesIO(archive)) as zf:
        for item in zf.infolist():
            found = archive_prefix.fullmatch(item.filename)
            if not found:
                continue
            name, relative = found.groups()
            species = int(name[:3])
            if first <= species <= last:
                inventory.setdefault(species, {}).setdefault(name, {})[relative] = item
        results = []
        with tempfile.TemporaryDirectory(prefix="hgss-full-gen3-audit-") as temp:
            root = Path(temp)
            for species in range(first, last + 1):
                folders = inventory.get(species, {})
                entry = {"species": species, "status": "SOURCE_BLOCKED",
                         "reasons": [], "normal": {}, "shiny": {}}
                if len(folders) != 1:
                    entry["reasons"].append("species_folder_count_" + str(len(folders)))
                    results.append(entry)
                    continue
                folder, file_map = next(iter(folders.items()))
                entry["folder"] = folder
                missing = sorted(expected_files - set(file_map))
                if missing:
                    entry["reasons"].append("missing_directional_files:" + ",".join(missing))
                    results.append(entry)
                    continue
                for variant, upstream_variant in VARIANTS:
                    dest_dir = root / ("%03d" % species) / upstream_variant
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    for direction in DIRECTIONS:
                        asset = file_map[upstream_variant + "/" + direction + ".png"]
                        if asset.file_size > 500_000:
                            entry["reasons"].append(variant + ":over_500KB_per_APNG")
                            break
                        (dest_dir / (direction + ".png")).write_bytes(zf.read(asset))
                    if entry["reasons"]:
                        break
                    try:
                        data = summarize_variant(dest_dir, species=species)
                    except (ValueError, OSError, AssertionError, IndexError, KeyError) as exc:
                        data = {"status": "SOURCE_BLOCKED",
                                "reasons": ["decoder_or_format:" + str(exc)[:140]]}
                    entry[variant] = {
                        "status": data["status"],
                        "colors": data.get("unique_opaque_BGR555_colors"),
                        "frame_px": data.get("frame_px"),
                        "semi_alpha": data.get("semi_transparent_pixel_instances"),
                        "packed_render_sha256": data.get("packed_render_sha256"),
                        "reasons": data.get("reasons", []),
                        "metapod_down_held_frame": species == 11
                            and data.get("directions", {}).get("down", {}).get("native_frames") == 3,
                        "minimum_unique_frames_per_direction": min(
                            (v["unique_BGR555_frames"] for v in data.get("directions", {}).values()),
                            default=None),
                    }
                if (entry["normal"].get("status") == "SOURCE_FEASIBLE"
                        and entry["shiny"].get("status") == "SOURCE_FEASIBLE"):
                    if entry["normal"]["frame_px"] != entry["shiny"]["frame_px"]:
                        entry["reasons"].append("normal_shiny_size_mismatch")
                    elif (entry["normal"]["packed_render_sha256"]
                          == entry["shiny"]["packed_render_sha256"]):
                        entry["reasons"].append("normal_shiny_render_identical")
                    else:
                        entry["status"] = "SOURCE_FEASIBLE"
                else:
                    for variant in ("normal", "shiny"):
                        if entry[variant].get("status") not in (None, "SOURCE_FEASIBLE"):
                            entry["reasons"].append(variant + ":" +
                                ",".join(entry[variant].get("reasons", [])))
                results.append(entry)
    pass_ids = [r["species"] for r in results if r["status"] == "SOURCE_FEASIBLE"]
    blocked = [{"id": r["species"], "reasons": r["reasons"],
                "normal_colors": r["normal"].get("colors"),
                "shiny_colors": r["shiny"].get("colors")}
               for r in results if r["status"] != "SOURCE_FEASIBLE"]
    held = [r["species"] for r in results if r["status"] == "SOURCE_FEASIBLE"
            and r["normal"].get("metapod_down_held_frame")
            and r["shiny"].get("metapod_down_held_frame")]
    size_counts = {}
    for entry in results:
        if entry["status"] == "SOURCE_FEASIBLE":
            size = str(entry["normal"]["frame_px"])
            size_counts[size] = size_counts.get(size, 0) + 1
    return {
        "scope": "PINNED_READ_ONLY_HGSS_GEN3_SOURCE_AUDIT_NOT_RUNTIME_OR_ART_REDISTRIBUTION",
        "source_revision": SOURCE_REVISION,
        "expected_species": last - first + 1,
        "source_feasible_species": len(pass_ids),
        "blocked_species_count": len(blocked),
        "feasible_ids": pass_ids,
        "frame_sizes": size_counts,
        "timing_preserved_three_frame_exceptions": held,
        "blocked": blocked
    }


def synthetic_full_test():
    from convert_follower_apng import synthetic_apng
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for variant in ("regular", "shiny"):
            for direction in DIRECTIONS:
                zf.writestr("source-pinned/APNG/by-pokemon/001_synthetic/" +
                            variant + "/" + direction + ".png", synthetic_apng())
    report = audit_complete_gen3(data.getvalue(), first=1, last=2)
    assert report["expected_species"] == 2
    assert report["blocked_species_count"] == 2
    assert report["blocked"][0]["id"] == 1
    assert "normal_shiny_render_identical" in report["blocked"][0]["reasons"]
    assert report["blocked"][1]["id"] == 2
    assert "species_folder_count_0" in report["blocked"][1]["reasons"]

    extra = io.BytesIO()
    with zipfile.ZipFile(extra, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for variant in ("regular", "shiny"):
            for direction in DIRECTIONS:
                zf.writestr("source-pinned/APNG/by-pokemon/011_metapod/" +
                            variant + "/" + direction + ".png",
                            synthetic_apng(frame_count=3 if direction == "down" else 4,
                                           color_bias=8 if variant == "shiny" else 0))
    metapod = audit_complete_gen3(extra.getvalue(), first=11, last=11)
    assert metapod["source_feasible_species"] == 1, metapod["blocked"]
    assert metapod["timing_preserved_three_frame_exceptions"] == [11]
    print("Pinned-archive inventory, 386 source contract and Metapod timed hold PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-gen3", action="store_true",
                        help="audit all 386 pinned upstream normal/shiny APNGs")
    parser.add_argument("--self-test-all", action="store_true")
    args = parser.parse_args()
    if args.self_test_all:
        synthetic_full_test()
        return
    if args.full_gen3:
        report = audit_complete_gen3(download_archive())
        print("HGSS_FULL_GEN3_REPORT=" + json.dumps(report, sort_keys=True, separators=(",", ":")))
        print("HGSS full pinned audit: %d/%d normal/shiny pairs source-convertible; "
              "%d source blockers" % (report["source_feasible_species"],
              report["expected_species"], report["blocked_species_count"]))
        print("This is a source feasibility audit, not ROM integration or legal clearance.")
        return
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
                entry["variants"][variant] = summarize_variant(variant_root, species=species)
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
