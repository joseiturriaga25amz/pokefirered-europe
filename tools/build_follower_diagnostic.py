#!/usr/bin/env python3
"""Build a private B10 MyBoy diagnostic ROM without retaining imported sprites in git.

Run from the isolated Full+B10 diagnostic integration candidate with an ARM GBA toolchain.
No ROM, converted art or private source archive is sent to GitHub Actions.
This is a diagnostic build only; it does not establish asset distribution rights.
"""
import argparse
import hashlib
import io
import json
import re
import shutil
import sys
import subprocess
import tempfile
import zipfile
from pathlib import Path

from audit_follower_source_samples import SOURCE_REPO, SOURCE_REVISION, download_archive
from convert_follower_apng import DIRECTIONS, synthetic_apng
from generate_follower_graphics import HEADER, SENTINEL, install

BRANCH = "diagnostic/b10-full-integrated-candidate"
REQUIRED_COMMANDS = ("git", "make", "gcc", "arm-none-eabi-gcc",
                     "arm-none-eabi-as", "arm-none-eabi-ld", "pkg-config")
ROM_NAME = "pokefirered_modern_es.gba"
ROM_LIMIT = 32 * 1024 * 1024
MAX_APNG_BYTES = 250000
ARCHIVE_NAME = re.compile(
    r"^[^/]+/APNG/by-pokemon/(\d{3}_[a-z0-9_-]+)/(regular|shiny)/(down|up|left|right)\.png$"
)


def run(*args, cwd):
    subprocess.run(args, cwd=cwd, check=True)


def output_of(*args, cwd):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()



def missing_commands(which):
    """Pure preflight predicate, separately tested without a system toolchain."""
    return [command for command in REQUIRED_COMMANDS if which(command) is None]


def check_environment():
    """Report actionable Ubuntu/WSL prerequisites before downloading any artwork."""
    problems = []
    if not sys.platform.startswith("linux"):
        problems.append("Use Ubuntu Linux or Ubuntu under WSL on a computer.")
    unavailable = missing_commands(shutil.which)
    if unavailable:
        problems.append("Missing commands: " + ", ".join(unavailable))
    if shutil.which("pkg-config") is not None:
        result = subprocess.run(("pkg-config", "--exists", "libpng"), check=False)
        if result.returncode:
            problems.append("libpng development headers are missing.")
    root = Path(__file__).resolve().parent.parent
    if shutil.which("git") is not None:
        try:
            branch = output_of("git", "branch", "--show-current", cwd=root)
            if branch != BRANCH:
                problems.append("Use branch: " + BRANCH + " (current: " + branch + ")")
            top = Path(output_of("git", "rev-parse", "--show-toplevel", cwd=root)).resolve()
            if top != root:
                problems.append("Run this script from its original Git checkout.")
            if output_of("git", "status", "--porcelain", cwd=root):
                print("Note: uncommitted checkout changes are ignored; private build uses the committed HEAD in a detached worktree.")
        except (subprocess.CalledProcessError, OSError):
            problems.append("No usable Git checkout found.")
    if problems:
        print("B10 private build: NOT READY")
        for problem in problems:
            print(" - " + problem)
        print("On Ubuntu/WSL: sudo apt update && sudo apt install -y "
              "git build-essential python3 gcc-arm-none-eabi "
              "binutils-arm-none-eabi libpng-dev pkg-config")
        raise SystemExit(1)
    print("B10 private build: environment READY (tools, branch, libpng).")
    print("This does not prove ROM runtime behavior or art distribution rights.")


def extract_source(archive, directory, ids):
    """Extract only complete selected normal/shiny directions, with strict paths."""
    ids = set(ids)
    expected = {(dex, variant, direction)
                for dex in ids for variant in ("regular", "shiny")
                for direction in DIRECTIONS}
    found = set()
    folder_by_id = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as zf:
        for item in zf.infolist():
            match = ARCHIVE_NAME.fullmatch(item.filename)
            if match is None:
                continue
            folder, variant, direction = match.groups()
            dex = int(folder[:3])
            if dex not in ids:
                continue
            key = (dex, variant, direction)
            if key in found or (dex in folder_by_id and folder_by_id[dex] != folder):
                raise ValueError("duplicate source species/variant/direction")
            if item.file_size > MAX_APNG_BYTES:
                raise ValueError("oversized APNG for National Dex %03d" % dex)
            found.add(key)
            folder_by_id[dex] = folder
            destination = directory / folder / variant / (direction + ".png")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(zf.read(item))
    if found != expected:
        missing = sorted(expected - found)
        raise ValueError("missing pinned HGSS APNGs: %d (first %s)" %
                         (len(missing), missing[:3]))
    return len(found)


def check_output_location(repo, output):
    output = output.expanduser().resolve()
    if output.suffix.lower() != ".gba":
        raise ValueError("diagnostic output must end with .gba")
    if output == repo or repo in output.parents:
        raise ValueError("save the private ROM outside the Git repository")
    manifest = output.with_suffix(".diagnostic.json")
    if output.exists() or manifest.exists():
        raise FileExistsError("output ROM or manifest exists; choose a fresh path")
    return output, manifest


def build_private(args):
    check_environment()
    root = Path(__file__).resolve().parent.parent
    if Path(output_of("git", "rev-parse", "--show-toplevel", cwd=root)).resolve() != root:
        raise ValueError("run the builder from its canonical Git checkout")
    if output_of("git", "branch", "--show-current", cwd=root) != BRANCH:
        raise ValueError("switch to prototype/follower-runtime before building")
    exact_sha = output_of("git", "rev-parse", "HEAD", cwd=root)
    selected = args.species if args.species is not None else list(range(1, 387))
    if (not selected or len(set(selected)) != len(selected)
            or any(not 1 <= dex <= 386 for dex in selected)):
        raise ValueError("species must be unique National Dex IDs 1..386")
    output, manifest_path = check_output_location(root, args.output)
    if args.archive is not None:
        archive = args.archive.expanduser().read_bytes()
        if len(archive) > 100 * 1024 * 1024:
            raise ValueError("source archive exceeds 100 MiB")
        source_label = "local-user-supplied-archive"
    else:
        archive = download_archive()  # pinned SOURCE_REPO/SOURCE_REVISION
        source_label = "%s@%s" % (SOURCE_REPO, SOURCE_REVISION)
    source_digest = hashlib.sha256(archive).hexdigest()

    with tempfile.TemporaryDirectory(prefix="firered-b10-private-") as temp:
        working = Path(temp)
        checkout = working / "checkout"
        art = working / "art"
        added = False
        try:
            run("git", "worktree", "add", "--detach", str(checkout), exact_sha, cwd=root)
            added = True
            if output_of("git", "rev-parse", "HEAD", cwd=checkout) != exact_sha:
                raise RuntimeError("detached checkout SHA mismatch")
            extracted = extract_source(archive, art, selected)
            if extracted != len(selected) * 2 * len(DIRECTIONS):
                raise AssertionError("incomplete extracted source")
            install(art, checkout, selected)
            run("make", "-j2", "firered_es_modern", cwd=checkout)
            rom = checkout / ROM_NAME
            if not rom.is_file() or not 0 < rom.stat().st_size <= ROM_LIMIT:
                raise RuntimeError("private ROM missing or exceeds 32 MiB")
            rom_sha1 = hashlib.sha1(rom.read_bytes()).hexdigest()
            rom_sha256 = hashlib.sha256(rom.read_bytes()).hexdigest()
            report = {
                "scope": "LOCAL_PRIVATE_B10_DIAGNOSTIC_NOT_MYBOY_ACCEPTANCE",
                "project_git_sha": exact_sha,
                "target": "firered_es_modern",
                "national_species_count": len(selected),
                "normal_shiny_variants": 2,
                "source_archive_sha256": source_digest,
                "source": source_label,
                "rom_bytes": rom.stat().st_size,
                "rom_sha1": rom_sha1,
                "rom_sha256": rom_sha256,
                "runtime_qa": "NOT_EXECUTED",
                "asset_redistribution": "NOT_AUTHORIZED_BY_THIS_TOOL",
            }
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(rom, output)
            output.chmod(0o600)
            manifest_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
            manifest_path.chmod(0o600)
        finally:
            if added:
                run("git", "worktree", "remove", "--force", str(checkout), cwd=root)
    print("Private B10 diagnostic built; no art was added to the project checkout.")
    print("ROM SHA-1:", rom_sha1)
    print("ROM:", output)
    print("Evidence:", manifest_path)
    print("MyBoy visual/runtime QA and redistribution clearance remain pending.")


def self_test():
    assert not missing_commands(lambda tool: "/fake/bin/" + tool)
    assert missing_commands(lambda tool: None) == list(REQUIRED_COMMANDS)
    from generate_follower_graphics import verify_installation
    ids = [1, 252]
    with tempfile.TemporaryDirectory(prefix="b10-builder-test-") as folder:
        base = Path(folder)
        archive_bytes = io.BytesIO()
        with zipfile.ZipFile(archive_bytes, "w") as zf:
            for dex, name in ((1, "bulbasaur"), (252, "treecko")):
                for variant in ("regular", "shiny"):
                    for direction in DIRECTIONS:
                        zf.writestr(
                            "pinned/APNG/by-pokemon/%03d_%s/%s/%s.png"
                            % (dex, name, variant, direction),
                            synthetic_apng(size=32, color_bias=8 if variant == "shiny" else 0))
        art = base / "art"
        assert extract_source(archive_bytes.getvalue(), art, ids) == 16
        checkout = base / "checkout"
        header = checkout / HEADER
        header.parent.mkdir(parents=True)
        header.write_text(
            "/* B10 species-keyed animated graphics contract. */\n"
            "sFollowerRegisteredGraphics[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2] = {\n"
            + SENTINEL + "\n};\n"
            "sFollowerRegisteredPalettes[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2] = {\n"
            + SENTINEL + "\n};\n")
        install(art, checkout, ids)
        verify_installation(checkout, ids)
        try:
            extract_source(archive_bytes.getvalue(), base / "incomplete", [1, 2])
        except ValueError:
            pass
        else:
            raise AssertionError("missing species files were accepted")
        try:
            check_output_location(base, base / "rom.gba")
        except ValueError:
            pass
        else:
            raise AssertionError("ROM inside repo allowed")
    print("Private B10 builder source completeness, generated registry and output isolation PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    src = parser.add_mutually_exclusive_group()
    src.add_argument("--download-pinned", action="store_true", help="retrieve pinned public HGSS source privately")
    src.add_argument("--archive", type=Path, help="use a local ZIP instead of downloading (unverified provenance)")
    parser.add_argument("--output", type=Path, help="private .gba path outside repository")
    parser.add_argument("--species", type=int, nargs="+", help="National IDs (default 1..386)")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check-environment", action="store_true", help="check prerequisites without downloading/building")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.check_environment:
        check_environment()
    elif args.output and (args.download_pinned or args.archive):
        build_private(args)
    else:
        parser.error("use --self-test or --output FILE.gba with --download-pinned/--archive")


if __name__ == "__main__":
    main()
