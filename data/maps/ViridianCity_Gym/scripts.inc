ViridianCity_Gym_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, ViridianCity_Gym_OnTransitionFull
	.byte 0

ViridianCity_Gym_OnTransitionFull::
	setflag FLAG_TEMP_1
	goto_if_unset FLAG_DEFEATED_LEADER_GIOVANNI, EventScript_Return
	goto_if_set FLAG_SYS_NATIONAL_DEX, ViridianCity_Gym_EventScript_ShowGiovanniFull
	setflag FLAG_HIDE_VIRIDIAN_GIOVANNI
	return

ViridianCity_Gym_EventScript_ShowGiovanniFull::
	clearflag FLAG_HIDE_VIRIDIAN_GIOVANNI
	return

ViridianCity_Gym_EventScript_Giovanni::
	goto_if_unset FLAG_SYS_NATIONAL_DEX, ViridianCity_Gym_EventScript_GiovanniStory
	goto_if_unset FLAG_GOT_TM26_FROM_GIOVANNI, ViridianCity_Gym_EventScript_GiovanniStory
	goto ViridianCity_Gym_EventScript_FullRematchOffer

ViridianCity_Gym_EventScript_GiovanniStory::
	famechecker FAMECHECKER_GIOVANNI, FCPICKSTATE_COLORED, UpdatePickStateFromSpecialVar8005
	trainerbattle_single TRAINER_LEADER_GIOVANNI, ViridianCity_Gym_Text_GiovanniIntro, ViridianCity_Gym_Text_GiovanniDefeat, ViridianCity_Gym_EventScript_DefeatedGiovanni, NO_MUSIC
	goto_if_unset FLAG_GOT_TM26_FROM_GIOVANNI, ViridianCity_Gym_EventScript_GiveTM26
	msgbox ViridianCity_Gym_Text_GiovanniPostBattle
	closemessage
	fadescreen FADE_TO_BLACK
	removeobject LOCALID_VIRIDIAN_GIOVANNI
	fadescreen FADE_FROM_BLACK
	release
	end

ViridianCity_Gym_EventScript_DefeatedGiovanni::
	famechecker FAMECHECKER_GIOVANNI, 3
	call ViridianCity_Gym_EventScript_MewtwoBreaksFree
	setflag FLAG_HIDE_MISC_KANTO_ROCKETS
	setflag FLAG_DEFEATED_LEADER_GIOVANNI
	setflag FLAG_BADGE08_GET
	setvar VAR_MAP_SCENE_ROUTE22, 3
	set_gym_trainers 8
	msgbox ViridianCity_Gym_Text_EarthBadgeAfterMewtwo
	goto ViridianCity_Gym_EventScript_GiveTM26
	end

ViridianCity_Gym_EventScript_MewtwoBreaksFree::
	lockall
	clearflag FLAG_TEMP_1
	addobject LOCALID_VIRIDIAN_MEWTWO
	delay 16
	waitse
	playmoncry SPECIES_MEWTWO, CRY_MODE_ENCOUNTER
	waitmoncry
	msgbox ViridianCity_Gym_Text_MewtwoPower
	msgbox ViridianCity_Gym_Text_GiovanniMaster
	msgbox ViridianCity_Gym_Text_MewtwoPartners
	msgbox ViridianCity_Gym_Text_GiovanniHumans
	msgbox ViridianCity_Gym_Text_MewtwoFreedom
	waitse
	playse SE_M_PSYBEAM2
	delay 24
	applymovement LOCALID_VIRIDIAN_MEWTWO, ViridianCity_Gym_Movement_MewtwoEscape
	applymovement LOCALID_VIRIDIAN_GIOVANNI, ViridianCity_Gym_Movement_GiovanniPanic
	msgbox ViridianCity_Gym_Text_GiovanniStopMewtwo
	waitmovement 0
	playse SE_M_TELEPORT
	delay 12
	removeobject LOCALID_VIRIDIAN_MEWTWO
	setflag FLAG_TEMP_1
	msgbox ViridianCity_Gym_Text_MewtwoEscaped
	delay 20
	msgbox ViridianCity_Gym_Text_GiovanniAfterMewtwo
	return

ViridianCity_Gym_Movement_MewtwoEscape:
	walk_in_place_faster_up
	delay_16
	fly_up
	step_end

ViridianCity_Gym_Movement_GiovanniPanic:
	walk_in_place_faster_right
	walk_in_place_faster_left
	shake_head_or_walk_in_place
	jump_in_place_up_down
	walk_in_place_faster_up
	step_end

ViridianCity_Gym_EventScript_GiveTM26::
	msgbox ViridianCity_Gym_Text_ExplainEarthBadgeTakeThis
	checkitemspace ITEM_TM26
	goto_if_eq VAR_RESULT, FALSE, ViridianCity_Gym_EventScript_NoRoomForTM26
	giveitem_msg ViridianCity_Gym_Text_ReceivedTM26FromGiovanni, ITEM_TM26
	setflag FLAG_GOT_TM26_FROM_GIOVANNI
	msgbox ViridianCity_Gym_Text_ExplainTM26
	release
	end

ViridianCity_Gym_EventScript_NoRoomForTM26::
	msgbox ViridianCity_Gym_Text_YouDoNotHaveSpace
	release
	end

ViridianCity_Gym_EventScript_Jason::
	trainerbattle_single TRAINER_TAMER_JASON, ViridianCity_Gym_Text_JasonIntro, ViridianCity_Gym_Text_JasonDefeat
	msgbox ViridianCity_Gym_Text_JasonPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Cole::
	trainerbattle_single TRAINER_TAMER_COLE, ViridianCity_Gym_Text_ColeIntro, ViridianCity_Gym_Text_ColeDefeat
	msgbox ViridianCity_Gym_Text_ColePostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Atsushi::
	trainerbattle_single TRAINER_BLACK_BELT_ATSUSHI, ViridianCity_Gym_Text_AtsushiIntro, ViridianCity_Gym_Text_AtsushiDefeat
	msgbox ViridianCity_Gym_Text_AtsushiPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Kiyo::
	trainerbattle_single TRAINER_BLACK_BELT_KIYO, ViridianCity_Gym_Text_KiyoIntro, ViridianCity_Gym_Text_KiyoDefeat
	msgbox ViridianCity_Gym_Text_KiyoPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Takashi::
	trainerbattle_single TRAINER_BLACK_BELT_TAKASHI, ViridianCity_Gym_Text_TakashiIntro, ViridianCity_Gym_Text_TakashiDefeat
	msgbox ViridianCity_Gym_Text_TakashiPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Samuel::
	trainerbattle_single TRAINER_COOLTRAINER_SAMUEL, ViridianCity_Gym_Text_SamuelIntro, ViridianCity_Gym_Text_SamuelDefeat
	msgbox ViridianCity_Gym_Text_SamuelPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Yuji::
	trainerbattle_single TRAINER_COOLTRAINER_YUJI, ViridianCity_Gym_Text_YujiIntro, ViridianCity_Gym_Text_YujiDefeat
	msgbox ViridianCity_Gym_Text_YujiPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_Warren::
	trainerbattle_single TRAINER_COOLTRAINER_WARREN, ViridianCity_Gym_Text_WarrenIntro, ViridianCity_Gym_Text_WarrenDefeat
	msgbox ViridianCity_Gym_Text_WarrenPostBattle, MSGBOX_AUTOCLOSE
	end

ViridianCity_Gym_EventScript_GymGuy::
	lock
	faceplayer
	goto_if_set FLAG_DEFEATED_LEADER_GIOVANNI, ViridianCity_Gym_EventScript_GymGuyPostVictory
	msgbox ViridianCity_Gym_Text_GymGuyAdvice
	release
	end

ViridianCity_Gym_EventScript_GymGuyPostVictory::
	famechecker FAMECHECKER_GIOVANNI, 4
	msgbox ViridianCity_Gym_Text_GymGuyPostVictory
	release
	end

ViridianCity_Gym_EventScript_GymStatue::
	lockall
	goto_if_set FLAG_BADGE08_GET, ViridianCity_Gym_EventScript_GymStatuePostVictory
	msgbox ViridianCity_Gym_Text_GymStatue
	releaseall
	end

ViridianCity_Gym_EventScript_GymStatuePostVictory::
	msgbox ViridianCity_Gym_Text_GymStatuePlayerWon
	releaseall
	end

ViridianCity_Gym_EventScript_FullRematchOffer::
	lock
	faceplayer
	msgbox ViridianCity_Gym_Text_FullRematchOffer, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, ViridianCity_Gym_EventScript_FullRematchDecline
	cleartrainerflag TRAINER_RS_BEAUTY
	trainerbattle_single TRAINER_RS_BEAUTY, ViridianCity_Gym_Text_FullRematchIntro, ViridianCity_Gym_Text_FullRematchDefeat, ViridianCity_Gym_EventScript_FullRematchWon
	end

ViridianCity_Gym_EventScript_FullRematchWon::
	msgbox ViridianCity_Gym_Text_FullRematchAfter
	release
	end

ViridianCity_Gym_EventScript_FullRematchDecline::
	release
	end

ViridianCity_Gym_Text_FullRematchOffer::
	.string "Has recorrido un largo camino desde\n"
	.string "nuestro primer combate.\p"
	.string "¿Quieres una revancha de verdad?$"

ViridianCity_Gym_Text_FullRematchIntro::
	.string "¡Entonces veamos cuánto has crecido!$"

ViridianCity_Gym_Text_FullRematchDefeat::
	.string "Excelente. Tu fuerza sigue creciendo.$"

ViridianCity_Gym_Text_FullRematchAfter::
	.string "Puedes volver cuando quieras.\p"
	.string "Siempre aceptaré otra revancha.$"


ViridianCity_Gym_Text_MewtwoPower::
	.string "MEWTWO: Ahora comprendo todo mi\\n"
	.string "poder... ¿Pero cuál es mi destino?$"

ViridianCity_Gym_Text_GiovanniMaster::
	.string "GIOVANNI: Tu destino es servirme.\\n"
	.string "Fuiste creado para luchar por mí.$"

ViridianCity_Gym_Text_MewtwoPartners::
	.string "MEWTWO: Dijiste que éramos socios...\\n"
	.string "Que éramos iguales.$"

ViridianCity_Gym_Text_GiovanniHumans::
	.string "GIOVANNI: Fuiste creado por humanos.\\n"
	.string "¡Jamás podrás ser nuestro igual!$"

ViridianCity_Gym_Text_MewtwoFreedom::
	.string "MEWTWO: Los humanos pudieron\\n"
	.string "crearme...\\p"
	.string "¡Pero jamás me esclavizarán!$"

ViridianCity_Gym_Text_GiovanniStopMewtwo::
	.string "GIOVANNI: ¡Detén esto ahora mismo!\\n"
	.string "¡MEWTWO! ¡Te ordeno que vuelvas!$"

ViridianCity_Gym_Text_MewtwoEscaped::
	.string "¡MEWTWO ha roto el control de\\n"
	.string "GIOVANNI y ha escapado del GIMNASIO!$"

ViridianCity_Gym_Text_GiovanniAfterMewtwo::
	.string "GIOVANNI: ...\\p"
	.string "Así que finalmente elegiste\\n"
	.string "desobedecerme...\\p"
	.string "No importa. Has derrotado incluso\\n"
	.string "al poder que yo creía controlar.$"

ViridianCity_Gym_Text_EarthBadgeAfterMewtwo::
	.string "¡Ha sido un duro combate!\\n"
	.string "Tu victoria es indiscutible.\\p"
	.string "¡Toma la MEDALLA TIERRA!{PAUSE_MUSIC}{PLAY_BGM}{MUS_OBTAIN_BADGE}{PAUSE 0xFE}{PAUSE 0x56}{RESUME_MUSIC}$"
