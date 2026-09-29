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
    signature = [o for o in brock_objs if o.get("local_id") == "LOCALID_FULL_BROCK_SIGNATURE"]
    assert len(signature) == 1
    signature = signature[0]
    assert signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_0"
    assert (signature["x"], signature["y"]) == (4, 5)
    assert signature["script"] == "0x0"
    assert signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert signature["x"] != 6
    assert not any((w["x"], w["y"]) == (signature["x"], signature["y"]) for w in brock["warp_events"])

    event_objects = (ROOT / "include/constants/event_objects.h").read_text(encoding="utf-8")
    movement = (ROOT / "src/event_object_movement.c").read_text(encoding="utf-8")
    graphics = (ROOT / "src/data/object_events/object_event_graphics.h").read_text(encoding="utf-8")
    info = (ROOT / "src/data/object_events/object_event_graphics_info.h").read_text(encoding="utf-8")
    pointers = (ROOT / "src/data/object_events/object_event_graphics_info_pointers.h").read_text(encoding="utf-8")
    assert "#define OBJ_EVENT_GFX_ONIX 152" in event_objects
    assert "#define OBJ_EVENT_GFX_STEELIX 153" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
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
    koga_signature = [o for o in koga_objs if o.get("local_id") == "LOCALID_FULL_KOGA_SIGNATURE"]
    assert len(koga_signature) == 1
    koga_signature = koga_signature[0]
    assert koga_signature["graphics_id"] == "OBJ_EVENT_GFX_VAR_1"
    assert (koga_signature["x"], koga_signature["y"]) == (5, 13)
    assert koga_signature["script"] == "0x0"
    assert koga_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (koga_signature["x"], koga_signature["y"]) for w in koga["warp_events"])

    assert "#define OBJ_EVENT_GFX_GOLBAT 154" in event_objects
    assert "#define OBJ_EVENT_GFX_CROBAT 155" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/golbat/icon.4bpp' in graphics
    assert 'graphics/pokemon/crobat/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Golbat" in info
    assert "gObjectEventGraphicsInfo_Crobat" in info
    assert "[OBJ_EVENT_GFX_GOLBAT]" in pointers
    assert "[OBJ_EVENT_GFX_CROBAT]" in pointers

    erika = read_json("data/maps/CeladonCity_Gym/map.json")
    erika_objs = erika["object_events"]
    erika_signature = [o for o in erika_objs if o.get("local_id") == "LOCALID_FULL_ERIKA_SIGNATURE"]
    assert len(erika_signature) == 1
    erika_signature = erika_signature[0]
    assert erika_signature["graphics_id"] == "OBJ_EVENT_GFX_GLOOM"
    assert (erika_signature["x"], erika_signature["y"]) == (6, 3)
    assert erika_signature["script"] == "0x0"
    assert erika_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (erika_signature["x"], erika_signature["y"]) for w in erika["warp_events"])

    assert "#define OBJ_EVENT_GFX_GLOOM 156" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/gloom/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Gloom" in info
    assert "[OBJ_EVENT_GFX_GLOOM]" in pointers

    sabrina = read_json("data/maps/SaffronCity_Gym/map.json")
    sabrina_objs = sabrina["object_events"]
    sabrina_signature = [o for o in sabrina_objs if o.get("local_id") == "LOCALID_FULL_SABRINA_SIGNATURE"]
    assert len(sabrina_signature) == 1
    sabrina_signature = sabrina_signature[0]
    assert sabrina_signature["graphics_id"] == "OBJ_EVENT_GFX_KADABRA"
    assert (sabrina_signature["x"], sabrina_signature["y"]) == (14, 10)
    assert sabrina_signature["script"] == "0x0"
    assert sabrina_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (sabrina_signature["x"], sabrina_signature["y"]) for w in sabrina["warp_events"])

    assert "#define OBJ_EVENT_GFX_KADABRA 157" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/kadabra/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Kadabra" in info
    assert "[OBJ_EVENT_GFX_KADABRA]" in pointers

    misty = read_json("data/maps/CeruleanCity_Gym/map.json")
    misty_objs = misty["object_events"]
    misty_signature = [o for o in misty_objs if o.get("local_id") == "LOCALID_FULL_MISTY_SIGNATURE"]
    assert len(misty_signature) == 1
    misty_signature = misty_signature[0]
    assert misty_signature["graphics_id"] == "OBJ_EVENT_GFX_STARMIE"
    assert (misty_signature["x"], misty_signature["y"]) == (8, 5)
    assert misty_signature["script"] == "0x0"
    assert misty_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (misty_signature["x"], misty_signature["y"]) for w in misty["warp_events"])

    assert "#define OBJ_EVENT_GFX_STARMIE 158" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/starmie/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Starmie" in info
    assert "[OBJ_EVENT_GFX_STARMIE]" in pointers

    surge = read_json("data/maps/VermilionCity_Gym/map.json")
    surge_objs = surge["object_events"]
    surge_signature = [o for o in surge_objs if o.get("local_id") == "LOCALID_FULL_SURGE_SIGNATURE"]
    assert len(surge_signature) == 1
    surge_signature = surge_signature[0]
    assert surge_signature["graphics_id"] == "OBJ_EVENT_GFX_RAICHU"
    assert (surge_signature["x"], surge_signature["y"]) == (4, 2)
    assert surge_signature["script"] == "0x0"
    assert surge_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (surge_signature["x"], surge_signature["y"]) for w in surge["warp_events"])

    assert "#define OBJ_EVENT_GFX_RAICHU 159" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/raichu/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Raichu" in info
    assert "[OBJ_EVENT_GFX_RAICHU]" in pointers

    blaine = read_json("data/maps/CinnabarIsland_Gym/map.json")
    blaine_objs = blaine["object_events"]
    blaine_signature = [o for o in blaine_objs if o.get("local_id") == "LOCALID_FULL_BLAINE_SIGNATURE"]
    assert len(blaine_signature) == 1
    blaine_signature = blaine_signature[0]
    assert blaine_signature["graphics_id"] == "OBJ_EVENT_GFX_MAGMAR"
    assert (blaine_signature["x"], blaine_signature["y"]) == (4, 4)
    assert blaine_signature["script"] == "0x0"
    assert blaine_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert not any((w["x"], w["y"]) == (blaine_signature["x"], blaine_signature["y"]) for w in blaine["warp_events"])

    assert "#define OBJ_EVENT_GFX_MAGMAR 160" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
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
    assert (bruno_signature["x"], bruno_signature["y"]) == (4, 5)
    assert bruno_signature["script"] == "0x0"
    assert bruno_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert bruno_signature["flag"] == "0"
    assert bruno_signature["x"] != 6
    assert not any((w["x"], w["y"]) == (bruno_signature["x"], bruno_signature["y"]) for w in bruno["warp_events"])

    assert "#define OBJ_EVENT_GFX_MACHAMP 162" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/machamp/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Machamp" in info
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_0" in info
    assert "[OBJ_EVENT_GFX_MACHAMP]" in pointers

    agatha = read_json("data/maps/PokemonLeague_AgathasRoom/map.json")
    agatha_objs = agatha["object_events"]
    agatha_signature = [o for o in agatha_objs if o.get("local_id") == "LOCALID_FULL_AGATHA_SIGNATURE"]
    assert len(agatha_signature) == 1
    agatha_signature = agatha_signature[0]
    assert agatha_signature["graphics_id"] == "OBJ_EVENT_GFX_GENGAR"
    assert (agatha_signature["x"], agatha_signature["y"]) == (8, 5)
    assert agatha_signature["script"] == "0x0"
    assert agatha_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert agatha_signature["flag"] == "0"
    assert agatha_signature["x"] != 6
    assert not any((w["x"], w["y"]) == (agatha_signature["x"], agatha_signature["y"]) for w in agatha["warp_events"])
    assert "#define OBJ_EVENT_GFX_GENGAR 163" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
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
    assert (lance_signature["x"], lance_signature["y"]) == (9, 8)
    assert lance_signature["script"] == "0x0"
    assert lance_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert lance_signature["flag"] == "0"
    assert lance_signature["x"] != 6
    assert (lance_signature["x"], lance_signature["y"]) not in {(5, 8), (7, 8)}
    assert not any((w["x"], w["y"]) == (lance_signature["x"], lance_signature["y"]) for w in lance["warp_events"])

    assert "#define OBJ_EVENT_GFX_DRAGONITE 164" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/dragonite/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Dragonite" in info
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in info
    assert "[OBJ_EVENT_GFX_DRAGONITE]" in pointers

    champion = read_json("data/maps/PokemonLeague_ChampionsRoom/map.json")
    champion_objs = champion["object_events"]
    champion_rival = [o for o in champion_objs if o.get("local_id") == "LOCALID_CHAMPIONS_ROOM_RIVAL"]
    assert len(champion_rival) == 1
    assert (champion_rival[0]["x"], champion_rival[0]["y"]) == (6, 8)
    champion_signature = [o for o in champion_objs if o.get("local_id") == "LOCALID_FULL_CHAMPION_SIGNATURE"]
    assert len(champion_signature) == 1
    champion_signature = champion_signature[0]
    assert champion_signature["graphics_id"] == "OBJ_EVENT_GFX_BLASTOISE"
    assert (champion_signature["x"], champion_signature["y"]) == (8, 8)
    assert champion_signature["script"] == "0x0"
    assert champion_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert champion_signature["flag"] == "0"
    assert champion_signature["x"] != 6
    assert (champion_signature["x"], champion_signature["y"]) != (5, 8)
    assert not any((w["x"], w["y"]) == (champion_signature["x"], champion_signature["y"]) for w in champion["warp_events"])

    assert "#define OBJ_EVENT_GFX_BLASTOISE 165" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/blastoise/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Blastoise" in info
    assert "OBJ_EVENT_PAL_TAG_MON_ICON_2" in info
    assert "[OBJ_EVENT_GFX_BLASTOISE]" in pointers

    giovanni = read_json("data/maps/ViridianCity_Gym/map.json")
    giovanni_objs = giovanni["object_events"]
    giovanni_signature = [o for o in giovanni_objs if o.get("local_id") == "LOCALID_FULL_GIOVANNI_SIGNATURE"]
    assert len(giovanni_signature) == 1
    giovanni_signature = giovanni_signature[0]
    assert giovanni_signature["graphics_id"] == "OBJ_EVENT_GFX_PERSIAN"
    assert (giovanni_signature["x"], giovanni_signature["y"]) == (1, 2)
    assert giovanni_signature["script"] == "0x0"
    assert giovanni_signature["trainer_type"] == "TRAINER_TYPE_NONE"
    assert giovanni_signature["flag"] == "FLAG_TEMP_2"
    assert not any((w["x"], w["y"]) == (giovanni_signature["x"], giovanni_signature["y"]) for w in giovanni["warp_events"])

    assert "#define OBJ_EVENT_GFX_PERSIAN 161" in event_objects
    assert "#define NUM_OBJ_EVENT_GFX     166" in event_objects
    assert 'graphics/pokemon/persian/icon.4bpp' in graphics
    assert "gObjectEventGraphicsInfo_Persian" in info
    assert "[OBJ_EVENT_GFX_PERSIAN]" in pointers

    giovanni_scripts = (ROOT / "data/maps/ViridianCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "clearflag FLAG_TEMP_2" in giovanni_scripts
    assert "setflag FLAG_TEMP_2" in giovanni_scripts
    assert "removeobject LOCALID_FULL_GIOVANNI_SIGNATURE" in giovanni_scripts

    koga_scripts = (ROOT / "data/maps/FuchsiaCity_Gym/scripts.inc").read_text(encoding="utf-8")
    assert "setvar VAR_OBJ_GFX_ID_1, OBJ_EVENT_GFX_GOLBAT" in koga_scripts
    assert "goto_if_unset FLAG_SYS_GAME_CLEAR" in koga_scripts
    assert "goto_if_unset FLAG_GOT_TM06_FROM_KOGA" in koga_scripts
    assert "setvar VAR_OBJ_GFX_ID_1, OBJ_EVENT_GFX_CROBAT" in koga_scripts

    print("B8 signature staging PASS: Lorelei/Lapras stable; Bruno/Machamp, Agatha/Gengar, Lance/Dragonite, Champion/Blastoise, Brock Onix->Steelix, Misty/Starmie, Surge/Raichu, Erika/Gloom, Koga Golbat->Crobat, Sabrina/Kadabra, Blaine/Magmar, and Giovanni/Persian are nonblocking and valid.")


if __name__ == "__main__":
    main()
