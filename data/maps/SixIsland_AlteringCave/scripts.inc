SixIsland_AlteringCave_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, SixIsland_AlteringCave_OnTransition
	.byte 0

SixIsland_AlteringCave_OnTransition::
	setworldmapflag FLAG_WORLD_MAP_SIX_ISLAND_ALTERING_CAVE
	end

SixIsland_AlteringCave_EventScript_Researcher::
	lock
	faceplayer
	msgbox SixIsland_AlteringCave_Text_ResearcherIntro
	goto SixIsland_AlteringCave_EventScript_SelectPage1

SixIsland_AlteringCave_EventScript_SelectPage1::
	multichoice 0, 0, MULTICHOICE_FULL_ALTERING_CAVE_PAGE1, FALSE
	switch VAR_RESULT
	case 0, SixIsland_AlteringCave_EventScript_SetZubat
	case 1, SixIsland_AlteringCave_EventScript_SetMareep
	case 2, SixIsland_AlteringCave_EventScript_SetPineco
	case 3, SixIsland_AlteringCave_EventScript_SetHoundour
	case 4, SixIsland_AlteringCave_EventScript_SetTeddiursa
	case 5, SixIsland_AlteringCave_EventScript_SelectPage2
	case 6, SixIsland_AlteringCave_EventScript_ResearcherEnd
	case 127, SixIsland_AlteringCave_EventScript_ResearcherEnd
	end

SixIsland_AlteringCave_EventScript_SelectPage2::
	multichoice 0, 0, MULTICHOICE_FULL_ALTERING_CAVE_PAGE2, FALSE
	switch VAR_RESULT
	case 0, SixIsland_AlteringCave_EventScript_SetAipom
	case 1, SixIsland_AlteringCave_EventScript_SetShuckle
	case 2, SixIsland_AlteringCave_EventScript_SetStantler
	case 3, SixIsland_AlteringCave_EventScript_SetSmeargle
	case 4, SixIsland_AlteringCave_EventScript_SelectPage1
	case 5, SixIsland_AlteringCave_EventScript_ResearcherEnd
	case 127, SixIsland_AlteringCave_EventScript_ResearcherEnd
	end

SixIsland_AlteringCave_EventScript_SetZubat::
	setvar VAR_ALTERING_CAVE_WILD_SET, 0
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetMareep::
	setvar VAR_ALTERING_CAVE_WILD_SET, 1
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetPineco::
	setvar VAR_ALTERING_CAVE_WILD_SET, 2
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetHoundour::
	setvar VAR_ALTERING_CAVE_WILD_SET, 3
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetTeddiursa::
	setvar VAR_ALTERING_CAVE_WILD_SET, 4
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetAipom::
	setvar VAR_ALTERING_CAVE_WILD_SET, 5
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetShuckle::
	setvar VAR_ALTERING_CAVE_WILD_SET, 6
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetStantler::
	setvar VAR_ALTERING_CAVE_WILD_SET, 7
	goto SixIsland_AlteringCave_EventScript_ResearcherChanged

SixIsland_AlteringCave_EventScript_SetSmeargle::
	setvar VAR_ALTERING_CAVE_WILD_SET, 8

SixIsland_AlteringCave_EventScript_ResearcherChanged::
	msgbox SixIsland_AlteringCave_Text_ResearcherChanged
	release
	end

SixIsland_AlteringCave_EventScript_ResearcherEnd::
	release
	end

SixIsland_AlteringCave_Text_ResearcherIntro::
	.string "Estoy estudiando los avistamientos de\\n"
	.string "esta cueva tan extraña.\\p"
	.string "Puedo ayudarte a buscar una especie\\n"
	.string "concreta. ¿Cuál quieres rastrear?$"

SixIsland_AlteringCave_Text_ResearcherChanged::
	.string "Perfecto. He ajustado el seguimiento.\\p"
	.string "La cueva debería mostrar ahora ese\\n"
	.string "avistamiento.$"
