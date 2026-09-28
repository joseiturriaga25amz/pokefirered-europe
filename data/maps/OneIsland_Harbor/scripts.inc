OneIsland_Harbor_MapScripts::
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, OneIsland_Harbor_OnWarp
	map_script MAP_SCRIPT_ON_FRAME_TABLE, OneIsland_Harbor_OnFrame
	.byte 0

OneIsland_Harbor_OnWarp::
	map_script_2 VAR_MAP_SCENE_ONE_ISLAND_HARBOR, 1, OneIsland_Harbor_EventScript_TurnPlayerNorth
	.2byte 0

OneIsland_Harbor_EventScript_TurnPlayerNorth::
	turnobject LOCALID_PLAYER, DIR_NORTH
	end

OneIsland_Harbor_OnFrame::
	map_script_2 VAR_MAP_SCENE_ONE_ISLAND_HARBOR, 1, OneIsland_Harbor_EventScript_PlayerEnterHarborFirstTime
	.2byte 0

OneIsland_Harbor_EventScript_PlayerEnterHarborFirstTime::
	lockall
	textcolor NPC_TEXT_COLOR_MALE
	applymovement LOCALID_PLAYER, OneIsland_Harbor_Movement_PlayerExitHarbor
	waitmovement 0
	setvar VAR_MAP_SCENE_ONE_ISLAND_HARBOR, 2
	warp MAP_ONE_ISLAND, 12, 18
	waitstate
	releaseall
	end

OneIsland_Harbor_Movement_PlayerExitHarbor::
	walk_up
	walk_up
	walk_up
	step_end

OneIsland_Harbor_EventScript_Sailor::
	lock
	faceplayer
	goto_if_eq VAR_FULL_MYSTIC_QUEST, 1, OneIsland_Harbor_EventScript_FullGiveMysticTicket
OneIsland_Harbor_EventScript_SailorMenu::
	message Text_WhereDoYouWantToSail
	waitmessage
	setvar VAR_0x8004, SEAGALLOP_ONE_ISLAND
	goto EventScript_ChooseDestFromOneIsland
	end

OneIsland_Harbor_EventScript_FullGiveMysticTicket::
	checkitemspace ITEM_MYSTIC_TICKET
	goto_if_eq VAR_RESULT, FALSE, OneIsland_Harbor_EventScript_FullMysticNoRoom
	giveitem_msg OneIsland_Harbor_Text_FullReceivedMysticTicket, ITEM_MYSTIC_TICKET, 1, MUS_OBTAIN_KEY_ITEM
	setflag FLAG_RECEIVED_MYSTIC_TICKET
	setflag FLAG_ENABLE_SHIP_NAVEL_ROCK
	setvar VAR_FULL_MYSTIC_QUEST, 2
	goto OneIsland_Harbor_EventScript_SailorMenu
	end

OneIsland_Harbor_EventScript_FullMysticNoRoom::
	msgbox OneIsland_Harbor_Text_FullMysticNoRoom
	release
	end

OneIsland_Harbor_Text_FullReceivedMysticTicket::
	.string "MARINERO: La corriente termina en una\n"
	.string "isla que no figura en las rutas normales.\p"
	.string "Este TICKET pertenecía a una antigua\n"
	.string "expedición marítima. Ahora es tuyo.\p"
	.string "¡{PLAYER} obtuvo el MISTI-TICKET!$"

OneIsland_Harbor_Text_FullMysticNoRoom::
	.string "MARINERO: Haz sitio en la BOLSA y\n"
	.string "vuelve. Este TICKET debe llegar a ti.$"
