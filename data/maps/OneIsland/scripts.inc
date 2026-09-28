OneIsland_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, OneIsland_OnTransition
	map_script MAP_SCRIPT_ON_FRAME_TABLE, OneIsland_OnFrame
	.byte 0

OneIsland_OnTransition::
	setworldmapflag FLAG_WORLD_MAP_ONE_ISLAND
	call OneIsland_EventScript_UpdateFullBeastFirstContact
	end

OneIsland_EventScript_UpdateFullBeastFirstContact::
	goto_if_unset FLAG_SYS_CAN_LINK_WITH_RS, OneIsland_EventScript_HideFullBeastFirstContact
	goto_if_eq VAR_FULL_BEAST_INTRO, 2, OneIsland_EventScript_HideFullBeastFirstContact
	goto_if_ne VAR_FULL_BEAST_INTRO, 0, OneIsland_EventScript_ShowFullBeastFirstContact
	setvar VAR_FULL_BEAST_INTRO, 1
OneIsland_EventScript_ShowFullBeastFirstContact::
	clearflag FLAG_FULL_HIDE_BEAST_FIRST_CONTACT
	return
OneIsland_EventScript_HideFullBeastFirstContact::
	setflag FLAG_FULL_HIDE_BEAST_FIRST_CONTACT
	return

OneIsland_OnFrame::
	map_script_2 VAR_MAP_SCENE_ONE_ISLAND_HARBOR, 2, OneIsland_EventScript_EnterOneIslandFirstTime
	map_script_2 VAR_FULL_BEAST_INTRO, 1, OneIsland_EventScript_FullBeastFirstContact
	.2byte 0

OneIsland_EventScript_FullBeastFirstContact::
	lockall
	msgbox OneIsland_Text_FullBeastFirstContact
	waitse
	playmoncry SPECIES_SUICUNE, CRY_MODE_ENCOUNTER
	waitmoncry
	playmoncry SPECIES_RAIKOU, CRY_MODE_NORMAL
	waitmoncry
	playmoncry SPECIES_ENTEI, CRY_MODE_NORMAL
	waitmoncry
	special Full_MarkRoamingBeastsSeen
	msgbox OneIsland_Text_FullBeastTrioFlees
	setvar VAR_FULL_BEAST_INTRO, 2
	setflag FLAG_FULL_HIDE_BEAST_FIRST_CONTACT
	removeobject LOCALID_FULL_RAIKOU
	removeobject LOCALID_FULL_SUICUNE
	removeobject LOCALID_FULL_ENTEI
	special InitRoamer
	releaseall
	end

OneIsland_EventScript_EnterOneIslandFirstTime::
	lockall
	textcolor NPC_TEXT_COLOR_MALE
	applymovement LOCALID_PLAYER, OneIsland_Movement_PlayerExitHarbor
	waitmovement 0
	msgbox OneIsland_Text_BillLetsGoSeeCelio
	closemessage
	applymovement LOCALID_ONE_ISLAND_BILL, OneIsland_Movement_BillWalkToPokeCenter
	applymovement LOCALID_PLAYER, OneIsland_Movement_PlayerWalkToPokeCenter
	waitmovement 0
	opendoor 14, 5
	waitdooranim
	applymovement LOCALID_ONE_ISLAND_BILL, OneIsland_Movement_BillEnterPokeCenter
	applymovement LOCALID_PLAYER, OneIsland_Movement_PlayerEnterPokeCenter
	waitmovement 0
	closedoor 14, 5
	waitdooranim
	removeobject LOCALID_ONE_ISLAND_BILL
	setvar VAR_MAP_SCENE_ONE_ISLAND_HARBOR, 3
	warp MAP_ONE_ISLAND_POKEMON_CENTER_1F, 9, 9
	waitstate
	releaseall
	end

	.macro walk_to_pokecenter
	walk_up
	walk_up
	walk_up
	walk_up
	walk_right
	walk_right
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	.endm

OneIsland_Movement_PlayerWalkToPokeCenter::
	walk_up
	walk_to_pokecenter
	step_end

OneIsland_Movement_PlayerEnterPokeCenter::
	walk_up
	walk_up
	set_invisible
	step_end

OneIsland_Movement_PlayerExitHarbor::
	walk_up
	step_end

OneIsland_Movement_BillWalkToPokeCenter::
	walk_to_pokecenter
	walk_up
	step_end

OneIsland_Movement_BillEnterPokeCenter::
	walk_up
	set_invisible
	step_end

OneIsland_EventScript_OldMan::
	lock
	faceplayer
	goto_if_eq VAR_FULL_BEAST_INTRO, 2, OneIsland_EventScript_OldManBeastArc
	goto_if_set FLAG_SYS_CAN_LINK_WITH_RS, OneIsland_EventScript_OldManLinkHoenn
	goto_if_set FLAG_SEVII_DETOUR_FINISHED, OneIsland_EventScript_OldManLinkKanto
	msgbox OneIsland_Text_LuckyToHaveCelioHere
	release
	end

OneIsland_EventScript_OldManBeastArc::
	goto_if_eq VAR_FULL_ROAMER_SEQUENCE, 0, OneIsland_EventScript_OldManTrackSuicune
	goto_if_eq VAR_FULL_ROAMER_SEQUENCE, 1, OneIsland_EventScript_OldManTrackRaikou
	goto_if_eq VAR_FULL_ROAMER_SEQUENCE, 2, OneIsland_EventScript_OldManTrackEntei
	goto OneIsland_EventScript_OldManBeastsComplete
	end

OneIsland_EventScript_OldManTrackSuicune::
	msgbox OneIsland_Text_FullBeastTrackSuicune
	release
	end

OneIsland_EventScript_OldManTrackRaikou::
	msgbox OneIsland_Text_FullBeastTrackRaikou
	release
	end

OneIsland_EventScript_OldManTrackEntei::
	msgbox OneIsland_Text_FullBeastTrackEntei
	release
	end

OneIsland_EventScript_OldManBeastsComplete::
	msgbox OneIsland_Text_FullBeastArcComplete
	release
	end

OneIsland_EventScript_OldManLinkKanto::
	msgbox OneIsland_Text_HavePCLinkageWithKanto
	release
	end

OneIsland_EventScript_OldManLinkHoenn::
	msgbox OneIsland_Text_HavePCLinkageWithHoenn
	release
	end

OneIsland_EventScript_BaldingMan::
	msgbox OneIsland_Text_IsntWarmClimateHereGreat, MSGBOX_NPC
	end

OneIsland_EventScript_IslandSign::
	msgbox OneIsland_Text_IslandSign, MSGBOX_SIGN
	end

OneIsland_EventScript_PokemonNetCenterSign::
	msgbox OneIsland_Text_PokemonNetCenterSign, MSGBOX_SIGN
	end
