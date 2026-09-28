SixIsland_AlteringCave_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, SixIsland_AlteringCave_OnTransition
	.byte 0

SixIsland_AlteringCave_OnTransition::
	setworldmapflag FLAG_WORLD_MAP_SIX_ISLAND_ALTERING_CAVE
	switch VAR_ALTERING_CAVE_WILD_SET
	case 0, SixIsland_AlteringCave_EventScript_RotateTo1
	case 1, SixIsland_AlteringCave_EventScript_RotateTo2
	case 2, SixIsland_AlteringCave_EventScript_RotateTo3
	case 3, SixIsland_AlteringCave_EventScript_RotateTo4
	case 4, SixIsland_AlteringCave_EventScript_RotateTo5
	case 5, SixIsland_AlteringCave_EventScript_RotateTo6
	case 6, SixIsland_AlteringCave_EventScript_RotateTo7
	case 7, SixIsland_AlteringCave_EventScript_RotateTo8
	case 8, SixIsland_AlteringCave_EventScript_RotateTo0
	goto SixIsland_AlteringCave_EventScript_RotateTo0

SixIsland_AlteringCave_EventScript_RotateTo0::
	setvar VAR_ALTERING_CAVE_WILD_SET, 0
	end

SixIsland_AlteringCave_EventScript_RotateTo1::
	setvar VAR_ALTERING_CAVE_WILD_SET, 1
	end

SixIsland_AlteringCave_EventScript_RotateTo2::
	setvar VAR_ALTERING_CAVE_WILD_SET, 2
	end

SixIsland_AlteringCave_EventScript_RotateTo3::
	setvar VAR_ALTERING_CAVE_WILD_SET, 3
	end

SixIsland_AlteringCave_EventScript_RotateTo4::
	setvar VAR_ALTERING_CAVE_WILD_SET, 4
	end

SixIsland_AlteringCave_EventScript_RotateTo5::
	setvar VAR_ALTERING_CAVE_WILD_SET, 5
	end

SixIsland_AlteringCave_EventScript_RotateTo6::
	setvar VAR_ALTERING_CAVE_WILD_SET, 6
	end

SixIsland_AlteringCave_EventScript_RotateTo7::
	setvar VAR_ALTERING_CAVE_WILD_SET, 7
	end

SixIsland_AlteringCave_EventScript_RotateTo8::
	setvar VAR_ALTERING_CAVE_WILD_SET, 8
	end

SixIsland_AlteringCave_EventScript_Researcher::
	lock
	faceplayer
	switch VAR_ALTERING_CAVE_WILD_SET
	case 0, SixIsland_AlteringCave_EventScript_ReportZubat
	case 1, SixIsland_AlteringCave_EventScript_ReportMareep
	case 2, SixIsland_AlteringCave_EventScript_ReportPineco
	case 3, SixIsland_AlteringCave_EventScript_ReportHoundour
	case 4, SixIsland_AlteringCave_EventScript_ReportTeddiursa
	case 5, SixIsland_AlteringCave_EventScript_ReportAipom
	case 6, SixIsland_AlteringCave_EventScript_ReportShuckle
	case 7, SixIsland_AlteringCave_EventScript_ReportStantler
	case 8, SixIsland_AlteringCave_EventScript_ReportSmeargle
	goto SixIsland_AlteringCave_EventScript_ReportZubat

SixIsland_AlteringCave_EventScript_ReportZubat::
	msgbox SixIsland_AlteringCave_Text_ReportZubat, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportMareep::
	msgbox SixIsland_AlteringCave_Text_ReportMareep, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportPineco::
	msgbox SixIsland_AlteringCave_Text_ReportPineco, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportHoundour::
	msgbox SixIsland_AlteringCave_Text_ReportHoundour, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportTeddiursa::
	msgbox SixIsland_AlteringCave_Text_ReportTeddiursa, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportAipom::
	msgbox SixIsland_AlteringCave_Text_ReportAipom, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportShuckle::
	msgbox SixIsland_AlteringCave_Text_ReportShuckle, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportStantler::
	msgbox SixIsland_AlteringCave_Text_ReportStantler, MSGBOX_DEFAULT
	goto SixIsland_AlteringCave_EventScript_ResearcherEnd

SixIsland_AlteringCave_EventScript_ReportSmeargle::
	msgbox SixIsland_AlteringCave_Text_ReportSmeargle, MSGBOX_DEFAULT

SixIsland_AlteringCave_EventScript_ResearcherEnd::
	release
	end

SixIsland_AlteringCave_Text_ReportZubat::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora mismo predominan los ZUBAT.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportMareep::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora mismo predominan los MAREEP.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportPineco::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora mismo predominan los PINECO.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportHoundour::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora predominan los HOUNDOUR.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportTeddiursa::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora predominan los TEDDIURSA.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportAipom::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora mismo predominan los AIPOM.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportShuckle::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora predominan los SHUCKLE.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportStantler::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora predominan los STANTLER.\n"
	.string "Durante esta visita no cambiarán.$"

SixIsland_AlteringCave_Text_ReportSmeargle::
	.string "Los avistamientos cambian cada vez\n"
	.string "que alguien vuelve a entrar.\p"
	.string "Ahora predominan los SMEARGLE.\n"
	.string "Durante esta visita no cambiarán.$"
