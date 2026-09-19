SaffronCity_Dojo_MapScripts::
	.byte 0

SaffronCity_Dojo_EventScript_TriggerMasterBattleLeft::
	lockall
	setvar VAR_MAP_SCENE_SAFFRON_CITY_DOJO, 1
	applymovement LOCALID_KARATE_MASTER, Common_Movement_WalkInPlaceFasterLeft
	waitmovement 0
	releaseall
	end

SaffronCity_Dojo_EventScript_TriggerMasterBattleRight::
	lockall
	setvar VAR_MAP_SCENE_SAFFRON_CITY_DOJO, 1
	applymovement LOCALID_KARATE_MASTER, Common_Movement_WalkInPlaceFasterRight
	waitmovement 0
	releaseall
	end

SaffronCity_Dojo_EventScript_HitmonleeBall::
	lock
	faceplayer
	goto_if_set FLAG_GOT_HITMON_FROM_DOJO, SaffronCity_Dojo_EventScript_AlreadyGotHitmon
	showmonpic SPECIES_HITMONLEE, 10, 3
	setvar VAR_TEMP_1, SPECIES_HITMONLEE
	applymovement LOCALID_KARATE_MASTER, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	textcolor NPC_TEXT_COLOR_MALE
	msgbox SaffronCity_Dojo_Text_YouWantHitmonlee, MSGBOX_YESNO
	call EventScript_RestorePrevTextColor
	goto_if_eq VAR_RESULT, YES, SaffronCity_Dojo_EventScript_GiveHitmon
	hidemonpic
	release
	end

SaffronCity_Dojo_EventScript_AlreadyGotHitmon::
	msgbox SaffronCity_Dojo_Text_BetterNotGetGreedy
	release
	end

SaffronCity_Dojo_EventScript_HitmonchanBall::
	lock
	faceplayer
	goto_if_set FLAG_GOT_HITMON_FROM_DOJO, SaffronCity_Dojo_EventScript_AlreadyGotHitmon
	showmonpic SPECIES_HITMONCHAN, 10, 3
	setvar VAR_TEMP_1, SPECIES_HITMONCHAN
	applymovement LOCALID_KARATE_MASTER, Common_Movement_WalkInPlaceFasterUp
	waitmovement 0
	textcolor NPC_TEXT_COLOR_MALE
	msgbox SaffronCity_Dojo_Text_YouWantHitmonchan, MSGBOX_YESNO
	call EventScript_RestorePrevTextColor
	goto_if_eq VAR_RESULT, YES, SaffronCity_Dojo_EventScript_GiveHitmon
	hidemonpic
	release
	end

SaffronCity_Dojo_EventScript_GiveHitmon::
	hidemonpic
	givemon VAR_TEMP_1, 25
	goto_if_eq VAR_RESULT, 0, SaffronCity_Dojo_EventScript_ReceivedHitmonParty
	goto_if_eq VAR_RESULT, 1, SaffronCity_Dojo_EventScript_ReceivedHitmonPC
	goto_if_eq VAR_RESULT, 2, EventScript_NoMoreRoomForPokemon
	release
	end

SaffronCity_Dojo_EventScript_ReceivedHitmonParty::
	call_if_eq VAR_TEMP_1, SPECIES_HITMONLEE, SaffronCity_Dojo_EventScript_RecordHitmonleeChoice
	removeobject VAR_LAST_TALKED
	bufferspeciesname STR_VAR_1, VAR_TEMP_1
	playfanfare MUS_LEVEL_UP
	message SaffronCity_Dojo_Text_ReceivedMonFromKarateMaster
	waitmessage
	waitfanfare
	setflag FLAG_GOT_HITMON_FROM_DOJO
	msgbox Text_GiveNicknameToThisMon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, SaffronCity_Dojo_EventScript_EndGiveMon
	call EventScript_GetGiftMonPartySlot
	call EventScript_ChangePokemonNickname
	goto SaffronCity_Dojo_EventScript_EndGiveMon
	end

SaffronCity_Dojo_EventScript_ReceivedHitmonPC::
	call_if_eq VAR_TEMP_1, SPECIES_HITMONLEE, SaffronCity_Dojo_EventScript_RecordHitmonleeChoice
	removeobject VAR_LAST_TALKED
	bufferspeciesname STR_VAR_1, VAR_TEMP_1
	playfanfare MUS_LEVEL_UP
	message SaffronCity_Dojo_Text_ReceivedMonFromKarateMaster
	waitmessage
	waitfanfare
	setflag FLAG_GOT_HITMON_FROM_DOJO
	msgbox Text_GiveNicknameToThisMon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, SaffronCity_Dojo_EventScript_TransferredHitmonToPC
	call EventScript_NameReceivedBoxMon
	goto SaffronCity_Dojo_EventScript_TransferredHitmonToPC
	end

SaffronCity_Dojo_EventScript_TransferredHitmonToPC::
	call EventScript_TransferredToPC
	goto SaffronCity_Dojo_EventScript_EndGiveMon
	end

SaffronCity_Dojo_EventScript_RecordHitmonleeChoice::
	setflag FLAG_FULL_DOJO_CHOSE_HITMONLEE
	return

SaffronCity_Dojo_EventScript_EndGiveMon::
	release
	end

SaffronCity_Dojo_EventScript_Statue::
	msgbox SaffronCity_Dojo_Text_FightingDojo, MSGBOX_SIGN
	end

SaffronCity_Dojo_EventScript_LeftScroll::
	msgbox SaffronCity_Dojo_Text_EnemiesOnEverySide, MSGBOX_SIGN
	end

SaffronCity_Dojo_EventScript_RightScroll::
	msgbox SaffronCity_Dojo_Text_GoesAroundComesAround, MSGBOX_SIGN
	end

SaffronCity_Dojo_EventScript_Hitoshi::
	trainerbattle_single TRAINER_BLACK_BELT_HITOSHI, SaffronCity_Dojo_Text_HitoshiIntro, SaffronCity_Dojo_Text_HitoshiDefeat
	msgbox SaffronCity_Dojo_Text_HitoshiPostBattle, MSGBOX_AUTOCLOSE
	end

SaffronCity_Dojo_EventScript_Hideki::
	trainerbattle_single TRAINER_BLACK_BELT_HIDEKI, SaffronCity_Dojo_Text_HidekiIntro, SaffronCity_Dojo_Text_HidekiDefeat
	msgbox SaffronCity_Dojo_Text_HidekiPostBattle, MSGBOX_AUTOCLOSE
	end

SaffronCity_Dojo_EventScript_Aaron::
	trainerbattle_single TRAINER_BLACK_BELT_AARON, SaffronCity_Dojo_Text_AaronIntro, SaffronCity_Dojo_Text_AaronDefeat
	msgbox SaffronCity_Dojo_Text_AaronPostBattle, MSGBOX_AUTOCLOSE
	end

SaffronCity_Dojo_EventScript_Mike::
	trainerbattle_single TRAINER_BLACK_BELT_MIKE, SaffronCity_Dojo_Text_MikeIntro, SaffronCity_Dojo_Text_MikeDefeat
	msgbox SaffronCity_Dojo_Text_MikePostBattle, MSGBOX_AUTOCLOSE
	end

SaffronCity_Dojo_EventScript_MasterKoichi::
	goto_if_not_defeated TRAINER_BLACK_BELT_KOICHI, SaffronCity_Dojo_EventScript_FirstKoichiBattle
	goto_if_unset FLAG_GOT_HITMON_FROM_DOJO, SaffronCity_Dojo_EventScript_ChooseFirstHitmon
	goto_if_unset FLAG_DEFEATED_SABRINA, SaffronCity_Dojo_EventScript_MasterKoichiAlreadyGotHitmon
	goto_if_set FLAG_FULL_DOJO_SECOND_REWARD, SaffronCity_Dojo_EventScript_SecondTrialComplete
	goto_if_defeated TRAINER_RS_BLACK_BELT, SaffronCity_Dojo_EventScript_GiveSecondHitmon
	trainerbattle_single TRAINER_RS_BLACK_BELT, SaffronCity_Dojo_Text_FullSecondTrialIntro, SaffronCity_Dojo_Text_FullSecondTrialDefeat
	goto SaffronCity_Dojo_EventScript_GiveSecondHitmon
	end

SaffronCity_Dojo_EventScript_FirstKoichiBattle::
	trainerbattle_single TRAINER_BLACK_BELT_KOICHI, SaffronCity_Dojo_Text_MasterKoichiIntro, SaffronCity_Dojo_Text_MasterKoichiDefeat, SaffronCity_Dojo_EventScript_DefeatedMasterKoichi
	goto SaffronCity_Dojo_EventScript_ChooseFirstHitmon
	end

SaffronCity_Dojo_EventScript_ChooseFirstHitmon::
	msgbox SaffronCity_Dojo_Text_ChoosePrizedFightingMon, MSGBOX_AUTOCLOSE
	end

SaffronCity_Dojo_EventScript_MasterKoichiAlreadyGotHitmon::
	msgbox SaffronCity_Dojo_Text_StayAndTrainWithUs
	release
	end

SaffronCity_Dojo_EventScript_GiveSecondHitmon::
	goto_if_set FLAG_FULL_DOJO_CHOSE_HITMONLEE, SaffronCity_Dojo_EventScript_GiveSecondHitmonchan
	setvar VAR_TEMP_1, SPECIES_HITMONLEE
	goto SaffronCity_Dojo_EventScript_TrySecondReward

SaffronCity_Dojo_EventScript_GiveSecondHitmonchan::
	setvar VAR_TEMP_1, SPECIES_HITMONCHAN

SaffronCity_Dojo_EventScript_TrySecondReward::
	bufferspeciesname STR_VAR_1, VAR_TEMP_1
	msgbox SaffronCity_Dojo_Text_FullSecondReward
	givemon VAR_TEMP_1, 35
	goto_if_eq VAR_RESULT, 2, SaffronCity_Dojo_EventScript_SecondRewardNoRoom
	setflag FLAG_FULL_DOJO_SECOND_REWARD
	goto_if_eq VAR_RESULT, 0, SaffronCity_Dojo_EventScript_SecondRewardParty
	goto_if_eq VAR_RESULT, 1, SaffronCity_Dojo_EventScript_SecondRewardPC
	end

SaffronCity_Dojo_EventScript_SecondRewardParty::
	playfanfare MUS_LEVEL_UP
	message SaffronCity_Dojo_Text_ReceivedMonFromKarateMaster
	waitmessage
	waitfanfare
	msgbox Text_GiveNicknameToThisMon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, SaffronCity_Dojo_EventScript_SecondTrialComplete
	call EventScript_GetGiftMonPartySlot
	call EventScript_ChangePokemonNickname
	goto SaffronCity_Dojo_EventScript_SecondTrialComplete

SaffronCity_Dojo_EventScript_SecondRewardPC::
	playfanfare MUS_LEVEL_UP
	message SaffronCity_Dojo_Text_ReceivedMonFromKarateMaster
	waitmessage
	waitfanfare
	msgbox Text_GiveNicknameToThisMon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, SaffronCity_Dojo_EventScript_SecondRewardTransferred
	call EventScript_NameReceivedBoxMon

SaffronCity_Dojo_EventScript_SecondRewardTransferred::
	call EventScript_TransferredToPC
	goto SaffronCity_Dojo_EventScript_SecondTrialComplete

SaffronCity_Dojo_EventScript_SecondRewardNoRoom::
	msgbox SaffronCity_Dojo_Text_FullSecondRewardNoRoom
	release
	end

SaffronCity_Dojo_EventScript_SecondTrialComplete::
	msgbox SaffronCity_Dojo_Text_FullSecondTrialComplete
	release
	end

SaffronCity_Dojo_EventScript_DefeatedMasterKoichi::
	setvar VAR_MAP_SCENE_SAFFRON_CITY_DOJO, 1
	release
	end

SaffronCity_Dojo_Text_FullSecondTrialIntro::
	.string "Has derrotado a SABRINA y has seguido\n"
	.string "entrenando. Quiero comprobar cuánto\l"
	.string "has progresado. ¡Segunda prueba!$"

SaffronCity_Dojo_Text_FullSecondTrialDefeat::
	.string "Excelente... Has superado la segunda\n"
	.string "prueba del DOJO.$"

SaffronCity_Dojo_Text_FullSecondReward::
	.string "Cumpliste tu palabra.\p"
	.string "El otro POKéMON de lucha también\n"
	.string "merece viajar contigo.\p"
	.string "Recibe a {STR_VAR_1}, Nv.35.$"

SaffronCity_Dojo_Text_FullSecondRewardNoRoom::
	.string "No hay espacio para recibirlo ahora.\p"
	.string "Vuelve cuando tengas sitio; tu premio\n"
	.string "quedará esperándote.$"

SaffronCity_Dojo_Text_FullSecondTrialComplete::
	.string "Has demostrado la fuerza y disciplina\n"
	.string "de un verdadero luchador.\p"
	.string "Las puertas del DOJO siguen abiertas.$"
