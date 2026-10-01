#!/usr/bin/env python3
"""B8 signature Pokémon staging checks."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main():
    lorelei = read_json("data/maps/PokemonLeague_LoreleisRoom/map.json")
    objects = lorelei["object_events"]

    trainer = [o for o in objects if o.get("graphics_id") == "OBJ_EVENT_GFX_LORELEI"]
    assert len(trainer) == 1
    assert (trainer[0]["x"], trainer[0]["y"]) == (6, 5)

    companions = [o for o in objects if o.get("local_id") == "LOCALID_FULL_LORELEI_LAPRAS"]
    assert len(companions) == 1
    lapras = companions[0]
    assert lapras["graphics_id"] == "OBJ_EVENT_GFX_LAPRAS"
    assert (lapras["x"], lapras["y"]) == (5, 5)
    assert lapras["script"] == "0x0"
    assert lapras["flag"] == "0"
    assert lapras["trainer_type"] == "TRAINER_TYPE_NONE"

    # Keep the central League approach/exit lane unobstructed.
    assert lapras["x"] != 6
    assert abs(lapras["x"] - trainer[0]["x"]) + abs(lapras["y"] - trainer[0]["y"]) == 1
    assert not any(
        (warp["x"], warp["y"]) == (lapras["x"], lapras["y"])
        for warp in lorelei["warp_events"]
    )

    brock = read_json("data/maps/PewterCity_Gym/map.json")
    brock_objs = brock["object_events"]
    brock_trainer = [o for o in brock_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_BROCK"]
    assert len(brock_trainer) == 1
    assert (brock_trainer[0]["x"], brock_trainer[0]["y"]) == (6, 5)
    signature = [o for o in brock_objs if o.get("local_id") == "LOCALID_FULL_BROCK_SIGNATURE"]
    assert len(signature) == 1
    signature = signature[0]
    assert signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_0"
    assert (signature["x"], signature["y"]) == (5, 5)
    assert signature["script"] == "0x0"
    assert signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert signature["x"] != 6
    assert abs(signature["x"] - brock_trainer[0]["x"]) + abs(signature["y"] - brock_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (signature["x"], signature["y"]) for w in brock["warp_events"])

    event_objects = (ROOT / "include/constants/event_objects.h").read_text(encoding="utf-8")
    movement = (ROOT / "src/event_object_movement.c").read_text(encoding="utf-8")
    graphics = (ROOT / "src/data/object_events/object_event_graphics.h").read_text(encoding="utf-8")
    info = (ROOT / "src/data/object_events/object_event_graphics_info.h").read_text(encoding="utf-8")
    pointers = (ROOT / "src/data/object_events/object_event_graphics_info_pointers.h").read_text(encoding="utf-8")
    pic_tables = (ROOT / "src/data/object_events/object_event_pic_tables.h").read_text(encoding="utf-8")

    # Global B8 graphics registry invariants.
    expected_b8_assets = [
        ("OBJ_EVENT_GFX_ONIX", 152, "Onix"),
        ("OBJ_EVENT_GFX_STEELIX", 153, "Steelix"),
        ("OBJ_EVENT_GFX_GOLBAT", 154, "Golbat"),
        ("OBJ_EVENT_GFX_CROBAT", 155, "Crobat"),
        ("OBJ_EVENT_GFX_GLOOM", 156, "Gloom"),
        ("OBJ_EVENT_GFX_KADABRA", 157, "Kadabra"),
        ("OBJ_EVENT_GFX_STARMIE", 158, "Starmie"),
        ("OBJ_EVENT_GFX_RAICHU", 159, "Raichu"),
        ("OBJ_EVENT_GFX_MAGMAR", 160, "Magmar"),
        ("OBJ_EVENT_GFX_PERSIAN", 161, "Persian"),
        ("OBJ_EVENT_GFX_MACHAMP", 162, "Machamp"),
        ("OBJ_EVENT_GFX_GENGAR", 163, "Gengar"),
        ("OBJ_EVENT_GFX_DRAGONITE", 164, "Dragonite"),
        ("OBJ_EVENT_GFX_BLASTOISE", 165, "Blastoise"),
        ("OBJ_EVENT_GFX_SEEL_ICON", 166, "SeelIcon"),
        ("OBJ_EVENT_GFX_STARYU_ICON", 167, "StaryuIcon"),
        ("OBJ_EVENT_GFX_VILEPLUME", 170, "Vileplume"),
    ]
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    for gfx_name, gfx_id, stem in expected_b8_assets:
        assert event_objects.count(f"#define {gfx_name} {gfx_id}") == 1
        assert graphics.count(f"gObjectEventPic_{stem}[]") == 1
        assert info.count(f"gObjectEventGraphicsInfo_{stem} = {{") == 1
        assert pointers.count(f"gObjectEventGraphicsInfo_{stem};") == 1
        assert pointers.count(f"[{gfx_name}]") == 1
        assert pic_tables.count(f"sPicTable_{stem}[]") == 1
        info_block = info.split(f"const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_{stem} = {{", 1)[1].split("};", 1)[0]
        assert ".size = 512" in info_block
        assert ".width = 32" in info_block
        assert ".height = 32" in info_block
        assert ".inanimate = TRUE" in info_block
        assert ".tracks = TRACKS_NONE" in info_block

    # Global B8 map invariants: no duplicate local IDs, no object stacking,
    # all LOCALID_FULL_* staging objects are non-interactive and never occupy warps.
    b8_map_paths = [
        "data/maps/PokemonLeague_LoreleisRoom/map.json",
        "data/maps/PokemonLeague_BrunosRoom/map.json",
        "data/maps/PokemonLeague_AgathasRoom/map.json",
        "data/maps/PokemonLeague_LancesRoom/map.json",
        "data/maps/PokemonLeague_ChampionsRoom/map.json",
        "data/maps/PewterCity_Gym/map.json",
        "data/maps/CeruleanCity_Gym/map.json",
        "data/maps/VermilionCity_Gym/map.json",
        "data/maps/CeladonCity_Gym/map.json",
        "data/maps/FuchsiaCity_Gym/map.json",
        "data/maps/SaffronCity_Gym/map.json",
        "data/maps/CinnabarIsland_Gym/map.json",
        "data/maps/ViridianCity_Gym/map.json",
    ]
    for map_path in b8_map_paths:
        audit_map = read_json(map_path)
        audit_objects = audit_map["object_events"]
        explicit_local_ids = [o["local_id"] for o in audit_objects if "local_id" in o]
        assert len(explicit_local_ids) == len(set(explicit_local_ids))
        occupied_tiles = [(o["x"], o["y"], o["elevation"]) for o in audit_objects]
        assert len(occupied_tiles) == len(set(occupied_tiles))
        warp_tiles = {(w["x"], w["y"]) for w in audit_map["warp_events"]}
        for staged in (o for o in audit_objects if o.get("local_id", "").startswith("LOCALID_FULL_")):
            assert staged["script"] == "0x0"
            assert staged["trainer_type"] == "TRAINER_TYPE_NONE"
            assert (staged["x"], staged["y"]) not in warp_tiles
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STEELIX 153" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in movement
    assert "gMonIconPalettes[2]" in movement
    assert 'graphics/pokemon/onix/icon.4bpp' in graphics
    assert 'graphics/pokemon/steelix/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Onix" in info
    assert "gObjectEventGraphicsInfo_Steelix" in info
    assert ".paletteSlot = PALSLOT_NPC_SPECIAL" in info
    assert "[OBJ_EVENT_GFX_ONIX]" in pointers
    assert "[OBJ_EVENT_GFX_STEELIX]" in pointers

    brock_scripts = (ROOT / "data/maps/PewterCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "setvar VAR_OBJ_GFX_ID_0, OBJ_EVENT_GFX_ONIX" in brock_scripts
    assert "goto_if_unset FLAG_SYS_GAME_CLEAR" in brock_scripts
    assert "goto_if_unset FLAG_GOT_TM39_FROM_BROCK" in brock_scripts
    assert "setvar VAR_OBJ_GFX_ID_0, OBJ_EVENT_GFX_STEELIX" in brock_scripts

    koga = read_json("data/maps/FuchsiaCity_Gym/map.json")
    koga_objs = koga["object_events"]
    koga_trainer = [o for o in koga_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_KOGA"]
    assert len(koga_trainer) == 1
    assert (koga_trainer[0]["x"], koga_trainer[0]["y"]) == (7, 13)
    koga_signature = [o for o in koga_objs if o.get("local_id") == "LOCALID_FULL_KOGA_SIGNATURE"]
    assert len(koga_signature) == 1
    koga_signature = koga_signature[0]
    assert koga_signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_1"
    assert (koga_signature["x"], koga_signature["y"]) == (6, 13)
    assert koga_signature["script"] == "0x0"
    assert koga_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert abs(koga_signature["x"] - koga_trainer[0]["x"]) + abs(koga_signature["y"] - koga_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (koga_signature["x"], koga_signature["y"]) for w in koga["warp_events"])

    assert "#define OBJ_EVENT_GFX_GOLBAT 154" in event_objects
    assert "#define OBJ_EVENT_GFX_CROBAT 155" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/golbat/icon.4bpp' in graphics
    assert 'graphics/pokemon/crobat/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Golbat" in info
    assert "gObjectEventGraphicsInfo_Crobat" in info
    assert "[OBJ_EVENT_GFX_GOLBAT]" in pointers
    assert "[OBJ_EVENT_GFX_CROBAT]" in pointers

    erika = read_json("data/maps/CeladonCity_Gym/map.json")
    erika_objs = erika["object_events"]
    erika_trainer = [o for o in erika_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_ERIKA"]
    assert len(erika_trainer) == 1
    assert (erika_trainer[0]["x"], erika_trainer[0]["y"]) == (6, 4)
    erika_signature = [o for o in erika_objs if o.get("local_id") == "LOCALID_FULL_ERIKA_SIGNATURE"]
    assert len(erika_signature) == 1
    erika_signature = erika_signature[0]
    assert erika_signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_2"
    assert (erika_signature["x"], erika_signature["y"]) == (7, 4)
    assert erika_signature["script"] == "0x0"
    assert erika_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert abs(erika_signature["x"] - erika_trainer[0]["x"]) + abs(erika_signature["y"] - erika_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (erika_signature["x"], erika_signature["y"]) for w in erika["warp_events"])
    erika_lisa = [o for o in erika_objs if o.get("script") == "CeladonCity_Gym_EventScript_Lisa"]
    assert len(erika_lisa) == 1
    assert (erika_lisa[0]["x"], erika_lisa[0]["y"]) == (8, 4)
    assert erika_lisa[0]["movement_type"] == "MOVEMENT_TYPE_FACE_DOWN"
    assert erika_lisa[0]["trainer_sight_or_berry_tree_id"] == "2"

    assert "#define OBJ_EVENT_GFX_GLOOM 156" in event_objects
    assert "#define OBJ_EVENT_GFX_VILEPLUME 170" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/gloom/icon.4bpp' in graphics
    assert 'graphics/pokemon/vileplume/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Gloom" in info
    assert "gObjectEventGraphicsInfo_Vileplume" in info
    assert "[OBJ_EVENT_GFX_GLOOM]" in pointers
    assert "[OBJ_EVENT_GFX_VILEPLUME]" in pointers

    erika_scripts = (ROOT / "data/maps/CeladonCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "setvar VAR_OBJ_GFX_ID_2, OBJ_EVENT_GFX_GLOOM" in erika_scripts
    assert "goto_if_unset FLAG_SYS_GAME_CLEAR" in erika_scripts
    assert "goto_if_unset FLAG_GOT_TM19_FROM_ERIKA" in erika_scripts
    assert "setvar VAR_OBJ_GFX_ID_2, OBJ_EVENT_GFX_VILEPLUME" in erika_scripts

    sabrina = read_json("data/maps/SaffronCity_Gym/map.json")
    sabrina_objs = sabrina["object_events"]
    sabrina_trainer = [o for o in sabrina_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_SABRINA"]
    assert len(sabrina_trainer) == 1
    assert (sabrina_trainer[0]["x"], sabrina_trainer[0]["y"]) == (14, 11)
    sabrina_signature = [o for o in sabrina_objs if o.get("local_id") == "LOCALID_FULL_SABRINA_SIGNATURE"]
    assert len(sabrina_signature) == 1
    sabrina_signature = sabrina_signature[0]
    assert sabrina_signature["graphics_id"] == "OBJ_EVENT_GFX_KADABRA"
    assert (sabrina_signature["x"], sabrina_signature["y"]) == (13, 11)
    assert sabrina_signature["script"] == "0x0"
    assert sabrina_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert abs(sabrina_signature["x"] - sabrina_trainer[0]["x"]) + abs(sabrina_signature["y"] - sabrina_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (sabrina_signature["x"], sabrina_signature["y"]) for w in sabrina["warp_events"])

    assert "#define OBJ_EVENT_GFX_KADABRA 157" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/kadabra/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Kadabra" in info
    assert "[OBJ_EVENT_GFX_KADABRA]" in pointers

    misty = read_json("data/maps/CeruleanCity_Gym/map.json")
    misty_objs = misty["object_events"]
    misty_trainer = [o for o in misty_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_MISTY"]
    assert len(misty_trainer) == 1
    assert (misty_trainer[0]["x"], misty_trainer[0]["y"]) == (8, 6)
    misty_signature = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_SIGNATURE"]
    assert len(misty_signature) == 1
    misty_signature = misty_signature[0]
    assert misty_signature["graphics_id"] == "OBJ_EVENT_GFX_STARMIE"
    assert (misty_signature["x"], misty_signature["y"]) == (7, 6)
    assert misty_signature["script"] == "0x0"
    assert misty_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert abs(misty_signature["x"] - misty_trainer[0]["x"]) + abs(misty_signature["y"] - misty_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (misty_signature["x"], misty_signature["y"]) for w in misty["warp_events"])

    assert "#define OBJ_EVENT_GFX_STARMIE 158" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/starmie/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Starmie" in info
    assert "[OBJ_EVENT_GFX_STARMIE]" in pointers

    misty_pool_seel = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_POOL_SEEL"]
    misty_pool_staryu = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_POOL_STARYU"]
    assert len(misty_pool_seel) == 1
    assert len(misty_pool_staryu) == 1
    misty_pool_seel = misty_pool_seel[0]
    misty_pool_staryu = misty_pool_staryu[0]
    assert misty_pool_seel["graphics_id"] == "OBJ_EVENT_GFX_SEEL_ICON"
    assert misty_pool_staryu["graphics_id"] == "OBJ_EVENT_GFX_STARYU_ICON"
    assert (misty_pool_seel["x"], misty_pool_seel["y"], misty_pool_seel["elevation"]) == (5, 12, 0)
    assert (misty_pool_staryu["x"], misty_pool_staryu["y"], misty_pool_staryu["elevation"]) == (12, 14, 0)
    for ambience in (misty_pool_seel, misty_pool_staryu):
        assert ambience["script"] == "0x0"
        assert ambience["trainer_type"] == "TRAINER_TYPE_NONE"
        assert ambience["flag"] == "0"
        assert not any((w["x"], w["y"]) == (ambience["x"], ambience["y"]) for w in misty["warp_events"])
    assert (misty_pool_seel["x"], misty_pool_seel["y"]) != (misty_pool_staryu["x"], misty_pool_staryu["y"])
    assert "#define OBJ_EVENT_GFX_SEEL_ICON 166" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/seel/icon.4bpp' in graphics
    assert 'graphics/pokemon/staryu/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_SeelIcon" in info
    assert "gObjectEventGraphicsInfo_StaryuIcon" in info
    assert "[OBJ_EVENT_GFX_SEEL_ICON]" in pointers
    assert "[OBJ_EVENT_GFX_STARYU_ICON]" in pointers
    starmie_info = info.split("const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Starmie = {", 1)[1].split("};", 1)[0]
    seel_icon_info = info.split("const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_SeelIcon = {", 1)[1].split("};", 1)[0]
    staryu_icon_info = info.split("const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_StaryuIcon = {", 1)[1].split("};", 1)[0]
    for pool_info in (starmie_info, seel_icon_info, staryu_icon_info):
        assert ".paletteTag = OBJ_EVENT_PAL_TAG_MON_ICON_2" in pool_info
        assert ".paletteSlot = PALSLOT_NPC_SPECIAL" in pool_info

    surge = read_json("data/maps/VermilionCity_Gym/map.json")
    surge_objs = surge["object_events"]
    surge_trainer = [o for o in surge_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_LT_SURGE"]
    assert len(surge_trainer) == 1
    assert (surge_trainer[0]["x"], surge_trainer[0]["y"]) == (5, 2)
    surge_signature = [o for o in surge_objs if o.get("local_id") == "LOCALID_FULL_SURGE_SIGNATURE"]
    assert len(surge_signature) == 1
    surge_signature = surge_signature[0]
    assert surge_signature["graphics_id"] == "OBJ_EVENT_GFX_RAICHU"
    assert (surge_signature["x"], surge_signature["y"]) == (4, 2)
    assert surge_signature["script"] == "0x0"
    assert surge_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert abs(surge_signature["x"] - surge_trainer[0]["x"]) + abs(surge_signature["y"] - surge_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (surge_signature["x"], surge_signature["y"]) for w in surge["warp_events"])

    assert "#define OBJ_EVENT_GFX_RAICHU 159" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/raichu/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Raichu" in info
    assert "[OBJ_EVENT_GFX_RAICHU]" in pointers

    blaine = read_json("data/maps/CinnabarIsland_Gym/map.json")
    blaine_objs = blaine["object_events"]
    blaine_trainer = [o for o in blaine_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_BLAINE"]
    assert len(blaine_trainer) == 1
    assert (blaine_trainer[0]["x"], blaine_trainer[0]["y"]) == (5, 4)
    blaine_signature = [o for o in blaine_objs if o.get("local_id") == "LOCALID_FULL_BLAINE_SIGNATURE"]
    assert len(blaine_signature) == 1
    blaine_signature = blaine_signature[0]
    assert blaine_signature["graphics_id"] == "OBJ_EVENT_GFX_MAGMAR"
    assert (blaine_signature["x"], blaine_signature["y"]) == (4, 4)
    assert blaine_signature["script"] == "0x0"
    assert blaine_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert abs(blaine_signature["x"] - blaine_trainer[0]["x"]) + abs(blaine_signature["y"] - blaine_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (blaine_signature["x"], blaine_signature["y"]) for w in blaine["warp_events"])

    assert "#define OBJ_EVENT_GFX_MAGMAR 160" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/magmar/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Magmar" in info
    assert "[OBJ_EVENT_GFX_MAGMAR]" in pointers

    bruno = read_json("data/maps/PokemonLeague_BrunosRoom/map.json")
    bruno_objs = bruno["object_events"]
    bruno_trainer = [o for o in bruno_objs if o.get("local_id") == "LOCALID_BRUNO"]
    assert len(bruno_trainer) == 1
    assert (bruno_trainer[0]["x"], bruno_trainer[0]["y"]) == (6, 5)
    bruno_signature = [o for o in bruno_objs if o.get("local_id") == "LOCALID_FULL_BRUNO_SIGNATURE"]
    assert len(bruno_signature) == 1
    bruno_signature = bruno_signature[0]
    assert bruno_signature["graphics_id"] == "OBJ_EVENT_GFX_MACHAMP"
    assert (bruno_signature["x"], bruno_signature["y"]) == (5, 5)
    assert bruno_signature["script"] == "0x0"
    assert bruno_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert bruno_signature["flag"] == "0"
    assert bruno_signature["x"] != 6
    assert abs(bruno_signature["x"] - bruno_trainer[0]["x"]) + abs(bruno_signature["y"] - bruno_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (bruno_signature["x"], bruno_signature["y"]) for w in bruno["warp_events"])

    assert "#define OBJ_EVENT_GFX_MACHAMP 162" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/machamp/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Machamp" in info
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_0" in info
    assert "[OBJ_EVENT_GFX_MACHAMP]" in pointers

    agatha = read_json("data/maps/PokemonLeague_AgathasRoom/map.json")
    agatha_objs = agatha["object_events"]
    agatha_trainer = [o for o in agatha_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_AGATHA"]
    assert len(agatha_trainer) == 1
    assert (agatha_trainer[0]["x"], agatha_trainer[0]["y"]) == (6, 5)
    agatha_signature = [o for o in agatha_objs if o.get("local_id") == "LOCALID_FULL_AGATHA_SIGNATURE"]
    assert len(agatha_signature) == 1
    agatha_signature = agatha_signature[0]
    assert agatha_signature["graphics_id"] == "OBJ_EVENT_GFX_GENGAR"
    assert (agatha_signature["x"], agatha_signature["y"]) == (7, 5)
    assert agatha_signature["script"] == "0x0"
    assert agatha_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert agatha_signature["flag"] == "0"
    assert agatha_signature["x"] != 6
    assert abs(agatha_signature["x"] - agatha_trainer[0]["x"]) + abs(agatha_signature["y"] - agatha_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (agatha_signature["x"], agatha_signature["y"]) for w in agatha["warp_events"])
    assert "#define OBJ_EVENT_GFX_GENGAR 163" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/gengar/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Gengar" in info
    assert "[OBJ_EVENT_GFX_GENGAR]" in pointers

    lance = read_json("data/maps/PokemonLeague_LancesRoom/map.json")
    lance_objs = lance["object_events"]
    lance_trainer = [o for o in lance_objs if o.get("local_id") == "LOCALID_LANCE"]
    assert len(lance_trainer) == 1
    assert (lance_trainer[0]["x"], lance_trainer[0]["y"]) == (6, 8)
    lance_signature = [o for o in lance_objs if o.get("local_id") == "LOCALID_FULL_LANCE_SIGNATURE"]
    assert len(lance_signature) == 1
    lance_signature = lance_signature[0]
    assert lance_signature["graphics_id"] == "OBJ_EVENT_GFX_DRAGONITE"
    assert (lance_signature["x"], lance_signature["y"]) == (7, 8)
    assert lance_signature["script"] == "0x0"
    assert lance_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert lance_signature["flag"] == "0"
    assert abs(lance_signature["x"] - lance_trainer[0]["x"]) + abs(lance_signature["y"] - lance_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (lance_signature["x"], lance_signature["y"]) for w in lance["warp_events"])

    lance_scripts = (ROOT / "data/maps/PokemonLeague_LancesRoom/scripts.inc").read_text(encoding="utf-8")
    assert "PokemonLeague_LancesRoom_Movement_LanceMoveOutOfWayRight::\n\twalk_up\n\twalk_right\n\twalk_right\n\twalk_down" in lance_scripts

    assert "#define OBJ_EVENT_GFX_DRAGONITE 164" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/dragonite/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Dragonite" in info
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in info
    assert "[OBJ_EVENT_GFX_DRAGONITE]" in pointers

    champion = read_json("data/maps/PokemonLeague_ChampionsRoom/map.json")
    champion_objs = champion["object_events"]
    champion_rival = [o for o in champion_objs if o.get("local_id") == "LOCALID_CHAMPIONS_ROOM_RIVAL"]
    assert len(champion_rival) == 1
    assert (champion_rival[0]["x"], champion_rival[0]["y"]) == (6, 8)
    assert champion_rival[0]["script"] == "PokemonLeague_ChampionsRoom_EventScript_Rival"
    champion_signature = [o for o in champion_objs if o.get("local_id") == "LOCALID_FULL_CHAMPION_SIGNATURE"]
    assert len(champion_signature) == 1
    champion_signature = champion_signature[0]
    assert champion_signature["graphics_id"] == "OBJ_EVENT_GFX_BLASTOISE"
    assert (champion_signature["x"], champion_signature["y"]) == (7, 8)
    assert champion_signature["script"] == "0x0"
    assert champion_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert champion_signature["flag"] == "0"
    assert abs(champion_signature["x"] - champion_rival[0]["x"]) + abs(champion_signature["y"] - champion_rival[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (champion_signature["x"], champion_signature["y"]) for w in champion["warp_events"])

    assert "#define OBJ_EVENT_GFX_BLASTOISE 165" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/blastoise/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Blastoise" in info
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in info
    assert "[OBJ_EVENT_GFX_BLASTOISE]" in pointers

    champion_scripts = (ROOT / "data/maps/PokemonLeague_ChampionsRoom/scripts.inc").read_text(encoding="utf-8")
    enter_room = champion_scripts.split("PokemonLeague_ChampionsRoom_EventScript_EnterRoom::", 1)[1].split("PokemonLeague_ChampionsRoom_EventScript_Rival::", 1)[0]
    assert "applymovement LOCALID_PLAYER, PokemonLeague_ChampionsRoom_Movement_PlayerEnter" in enter_room
    assert "setvar VAR_TEMP_1, 1" in enter_room
    assert "PokemonLeague_ChampionsRoom_EventScript_Battle" not in enter_room
    rival_talk = champion_scripts.split("PokemonLeague_ChampionsRoom_EventScript_Rival::", 1)[1].split("PokemonLeague_ChampionsRoom_EventScript_QuestLogTalkEnd::", 1)[0]
    assert "faceplayer" in rival_talk
    assert "PokemonLeague_ChampionsRoom_EventScript_Intro" in rival_talk
    assert "PokemonLeague_ChampionsRoom_EventScript_RematchIntro" in rival_talk
    assert "PokemonLeague_ChampionsRoom_EventScript_Battle" in rival_talk
    assert "PokemonLeague_ChampionsRoom_EventScript_Rematch" in rival_talk
    assert "setflag FLAG_DEFEATED_CHAMP" in rival_talk
    assert "addobject LOCALID_CHAMPIONS_ROOM_PROF_OAK" in rival_talk
    assert "warp MAP_POKEMON_LEAGUE_HALL_OF_FAME, 5, 12" in rival_talk

    giovanni = read_json("data/maps/ViridianCity_Gym/map.json")
    giovanni_objs = giovanni["object_events"]
    giovanni_trainer = [o for o in giovanni_objs if o.get("local_id") == "LOCALID_VIRIDIAN_GIOVANNI"]
    assert len(giovanni_trainer) == 1
    assert (giovanni_trainer[0]["x"], giovanni_trainer[0]["y"]) == (2, 2)
    giovanni_signature = [o for o in giovanni_objs if o.get("local_id") == "LOCALID_FULL_GIOVANNI_SIGNATURE"]
    assert len(giovanni_signature) == 1
    giovanni_signature = giovanni_signature[0]
    assert giovanni_signature["graphics_id"] == "OBJ_EVENT_GFX_PERSIAN"
    assert (giovanni_signature["x"], giovanni_signature["y"]) == (1, 2)
    assert giovanni_signature["script"] == "0x0"
    assert giovanni_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert giovanni_signature["flag"] == "FLAG_TEMP_2"
    assert abs(giovanni_signature["x"] - giovanni_trainer[0]["x"]) + abs(giovanni_signature["y"] - giovanni_trainer[0]["y"]) == 1
    assert not any((w["x"], w["y"]) == (giovanni_signature["x"], giovanni_signature["y"]) for w in giovanni["warp_events"])

    assert "#define OBJ_EVENT_GFX_PERSIAN 161" in event_objects
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STARYU_ICON 167" in event_objects
    assert 'graphics/pokemon/persian/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Persian" in info
    assert "[OBJ_EVENT_GFX_PERSIAN]" in pointers

    giovanni_scripts = (ROOT / "data/maps/ViridianCity_Gym/scripts.inc").read_text(encoding="utf-8")
    giovanni_transition = giovanni_scripts.split("ViridianCity_Gym_OnTransitionFull::", 1)[1].split("ViridianCity_Gym_EventScript_ShowGiovanniFull::", 1)[0]
    assert "setflag FLAG_TEMP_1" in giovanni_transition
    assert "clearflag FLAG_TEMP_2" in giovanni_transition
    assert "goto_if_unset FLAG_DEFEATED_LEADER_GIOVANNI, EventScript_Return" in giovanni_transition
    assert "goto_if_set FLAG_SYS_GAME_CLEAR, ViridianCity_Gym_EventScript_ShowGiovanniFull" in giovanni_transition
    assert "setflag FLAG_HIDE_VIRIDIAN_GIOVANNI" in giovanni_transition
    assert "setflag FLAG_TEMP_2" in giovanni_transition
    assert giovanni_transition.index("clearflag FLAG_TEMP_2") < giovanni_transition.index("goto_if_unset FLAG_DEFEATED_LEADER_GIOVANNI")
    giovanni_postgame = giovanni_scripts.split("ViridianCity_Gym_EventScript_ShowGiovanniFull::", 1)[1].split("ViridianCity_Gym_EventScript_Giovanni::", 1)[0]
    assert "clearflag FLAG_HIDE_VIRIDIAN_GIOVANNI" in giovanni_postgame
    assert "clearflag FLAG_TEMP_2" in giovanni_postgame
    giovanni_story = giovanni_scripts.split("ViridianCity_Gym_EventScript_GiovanniStory::", 1)[1].split("ViridianCity_Gym_EventScript_DefeatedGiovanni::", 1)[0]
    assert "removeobject LOCALID_VIRIDIAN_GIOVANNI" in giovanni_story
    assert "removeobject LOCALID_FULL_GIOVANNI_SIGNATURE" in giovanni_story
    assert "setflag FLAG_TEMP_2" in giovanni_story
    mewtwo_escape = giovanni_scripts.split("ViridianCity_Gym_Movement_MewtwoEscape:", 1)[1].split("ViridianCity_Gym_Movement_GiovanniPanic:", 1)[0]
    giovanni_panic = giovanni_scripts.split("ViridianCity_Gym_Movement_GiovanniPanic:", 1)[1].split("ViridianCity_Gym_EventScript_GiveTM26::", 1)[0]
    assert "fly_up" in mewtwo_escape
    assert "walk_left" not in mewtwo_escape and "walk_right" not in mewtwo_escape
    assert "walk_up" not in giovanni_panic and "walk_down" not in giovanni_panic
    assert "walk_left" not in giovanni_panic and "walk_right" not in giovanni_panic

    misty = read_json("data/maps/CeruleanCity_Gym/map.json")
    misty_objs = misty["object_events"]
    misty_trainer = [o for o in misty_objs if o.get("graphics_id") == "OBJ_EVENT_GFX_MISTY"]
    assert len(misty_trainer) == 1 and (misty_trainer[0]["x"], misty_trainer[0]["y"]) == (8, 6)
    starmie = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_SIGNATURE"]
    togepi = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_TOGEPI"]
    seel = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_POOL_SEEL"]
    horsea = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_POOL_HORSEA"]
    assert len(starmie) == len(togepi) == len(seel) == len(horsea) == 1
    assert (starmie[0]["x"], starmie[0]["y"]) == (7, 6)
    assert (togepi[0]["x"], togepi[0]["y"]) == (9, 6)
    assert (seel[0]["x"], seel[0]["y"]) == (5, 12)
    assert (horsea[0]["x"], horsea[0]["y"]) == (6, 12)
    assert togepi[0]["graphics_id"] == "OBJ_EVENT_GFX_TOGEPI_ICON"
    assert horsea[0]["graphics_id"] == "OBJ_EVENT_GFX_HORSEA_ICON"
    for staged in (starmie[0], togepi[0], seel[0], horsea[0]):
        assert staged["script"] == "0x0"
        assert staged["trainer_type"] == "TRAINER_TYPE_NONE"
    assert "#define OBJ_EVENT_GFX_TOGEPI_ICON 168" in event_objects
    assert "#define OBJ_EVENT_GFX_HORSEA_ICON 169" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     171" in event_objects
    assert 'graphics/pokemon/togepi/icon.4bpp' in graphics
    assert 'graphics/pokemon/horsea/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_TogepiIcon" in info
    assert "gObjectEventGraphicsInfo_HorseaIcon" in info
    assert "[OBJ_EVENT_GFX_TOGEPI_ICON]" in pointers
    assert "[OBJ_EVENT_GFX_HORSEA_ICON]" in pointers

    koga_scripts = (ROOT / "data/maps/FuchsiaCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "setvar VAR_OBJ_GFX_ID_1, OBJ_EVENT_GFX_GOLBAT" in koga_scripts
    assert "goto_if_unset FLAG_SYS_GAME_CLEAR" in koga_scripts
    assert "goto_if_unset FLAG_GOT_TM06_FROM_KOGA" in koga_scripts
    assert "setvar VAR_OBJ_GFX_ID_1, OBJ_EVENT_GFX_CROBAT" in koga_scripts

    print("B8 signature staging PASS: Lorelei/Lapras stable; Bruno/Machamp, Agatha/Gengar, Lance/Dragonite, Champion/Blastoise, Brock Onix->Steelix, Misty/Starmie, Surge/Raichu, Erika Gloom->Vileplume, Koga Golbat->Crobat, Sabrina/Kadabra, Blaine/Magmar, and Giovanni/Persian are nonblocking and valid.")


if __name__ == "__main__":
    main()
