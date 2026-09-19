CeruleanCity_Gym_MapScripts::
	.byte 0

CeruleanCity_Gym_EventScript_Misty::
	goto_if_unset FLAG_SYS_NATIONAL_DEX, CeruleanCity_Gym_EventScript_MistyStory
	goto_if_unset FLAG_GOT_TM03_FROM_MISTY, CeruleanCity_Gym_EventScript_MistyStory
	goto CeruleanCity_Gym_EventScript_FullRematchOffer

CeruleanCity_Gym_EventScript_MistyStory::
	famechecker FAMECHECKER_MISTY, FCPICKSTATE_COLORED, UpdatePickStateFromSpecialVar8005
	trainerbattle_single TRAINER_LEADER_MISTY, CeruleanCity_Gym_Text_MistyIntro, CeruleanCity_Gym_Text_MistyDefeat, CeruleanCity_Gym_EventScript_MistyDefeated, NO_MUSIC
	goto_if_unset FLAG_GOT_TM03_FROM_MISTY, CeruleanCity_Gym_EventScript_GiveTM03
	msgbox CeruleanCity_Gym_Text_ExplainTM03
	release
	end

CeruleanCity_Gym_EventScript_MistyDefeated::
	famechecker FAMECHECKER_MISTY, 1
	setflag FLAG_DEFEATED_MISTY
	setflag FLAG_BADGE02_GET
	setrespawn HEAL_LOCATION_CERULEAN_CITY
	set_gym_trainers 2
	goto CeruleanCity_Gym_EventScript_GiveTM03
	end

CeruleanCity_Gym_EventScript_GiveTM03::
	msgbox CeruleanCity_Gym_Text_ExplainCascadeBadge
	checkitemspace ITEM_TM03
	goto_if_eq VAR_RESULT, FALSE, CeruleanCity_Gym_EventScript_NoRoomForTM03
	giveitem_msg CeruleanCity_Gym_Text_ReceivedTM03FromMisty, ITEM_TM03
	setflag FLAG_GOT_TM03_FROM_MISTY
	msgbox CeruleanCity_Gym_Text_ExplainTM03
	release
	end

CeruleanCity_Gym_EventScript_NoRoomForTM03::
	msgbox CeruleanCity_Gym_Text_BetterMakeRoomForThis
	release
	end

CeruleanCity_Gym_EventScript_Diana::
	trainerbattle_single TRAINER_PICNICKER_DIANA, CeruleanCity_Gym_Text_DianaIntro, CeruleanCity_Gym_Text_DianaDefeat
	msgbox CeruleanCity_Gym_Text_DianaPostBattle, MSGBOX_AUTOCLOSE
	end

CeruleanCity_Gym_EventScript_Luis::
	trainerbattle_single TRAINER_SWIMMER_MALE_LUIS, CeruleanCity_Gym_Text_LuisIntro, CeruleanCity_Gym_Text_LuisDefeat
	famechecker FAMECHECKER_MISTY, 2
	msgbox CeruleanCity_Gym_Text_LuisPostBattle, MSGBOX_AUTOCLOSE
	end

CeruleanCity_Gym_EventScript_GymGuy::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_MISTY, CeruleanCity_Gym_EventScript_GymGuyPostVictory
	msgbox CeruleanCity_Gym_Text_GymGuyAdvice
	release
	end

CeruleanCity_Gym_EventScript_GymGuyPostVictory::
	msgbox CeruleanCity_Gym_Text_WeMakePrettyGoodTeam
	release
	end

CeruleanCity_Gym_EventScript_GymStatue::
	lockall
	goto_if_set FLAG_BADGE02_GET, CeruleanCity_Gym_EventScript_GymStatuePostVictory
	msgbox CeruleanCity_Gym_Text_GymStatue
	releaseall
	end

CeruleanCity_Gym_EventScript_GymStatuePostVictory::
	msgbox CeruleanCity_Gym_Text_GymStatuePlayerWon
	releaseall
	end

CeruleanCity_Gym_EventScript_FullRematchOffer::
	lock
	faceplayer
	msgbox CeruleanCity_Gym_Text_FullRematchOffer, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, CeruleanCity_Gym_EventScript_FullRematchDecline
	cleartrainerflag TRAINER_RS_RUIN_MANIAC
	trainerbattle_single TRAINER_RS_RUIN_MANIAC, CeruleanCity_Gym_Text_FullRematchIntro, CeruleanCity_Gym_Text_FullRematchDefeat, CeruleanCity_Gym_EventScript_FullRematchWon
	end

CeruleanCity_Gym_EventScript_FullRematchWon::
	msgbox CeruleanCity_Gym_Text_FullRematchAfter
	release
	end

CeruleanCity_Gym_EventScript_FullRematchDecline::
	release
	end

CeruleanCity_Gym_Text_FullRematchOffer::
	.string "Has recorrido un largo camino desde\n"
	.string "nuestro primer combate.\p"
	.string "¿Quieres una revancha de verdad?$"

CeruleanCity_Gym_Text_FullRematchIntro::
	.string "¡Entonces veamos cuánto has crecido!$"

CeruleanCity_Gym_Text_FullRematchDefeat::
	.string "Excelente. Tu fuerza sigue creciendo.$"

CeruleanCity_Gym_Text_FullRematchAfter::
	.string "Puedes volver cuando quieras.\p"
	.string "Siempre aceptaré otra revancha.$"
