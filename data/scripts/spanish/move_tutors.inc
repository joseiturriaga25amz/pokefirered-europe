VictoryRoad_2F_EventScript_DoubleEdgeTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_DOUBLE_EDGE, EventScript_DoubleEdgeRepeat
	msgbox Text_DoubleEdgeTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_DoubleEdgeDeclined
	msgbox Text_DoubleEdgeWhichMon
	setvar VAR_0x8005, MOVETUTOR_DOUBLE_EDGE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_DoubleEdgeDeclined
	setflag FLAG_TUTOR_DOUBLE_EDGE
	goto EventScript_DoubleEdgeTaught
	end

EventScript_DoubleEdgeRepeat::
	msgbox Text_FullTutorRepeat_DoubleEdge, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_DoubleEdgeDeclined
	checkmoney 5000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_DoubleEdgeWhichMon
	setvar VAR_0x8005, MOVETUTOR_DOUBLE_EDGE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_DoubleEdgeDeclined
	removemoney 5000
	goto EventScript_DoubleEdgeTaught
	end

EventScript_DoubleEdgeDeclined::
	msgbox Text_DoubleEdgeDeclined
	release
	end

EventScript_DoubleEdgeTaught::
	msgbox Text_DoubleEdgeTaught
	release
	end

EventScript_ThunderWaveTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_THUNDER_WAVE, EventScript_ThunderWaveRepeat
	msgbox Text_ThunderWaveTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_ThunderWaveDeclined
	msgbox Text_ThunderWaveWhichMon
	setvar VAR_0x8005, MOVETUTOR_THUNDER_WAVE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_ThunderWaveDeclined
	setflag FLAG_TUTOR_THUNDER_WAVE
	goto EventScript_ThunderWaveTaught
	end

EventScript_ThunderWaveRepeat::
	msgbox Text_FullTutorRepeat_ThunderWave, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_ThunderWaveDeclined
	checkmoney 6500
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_ThunderWaveWhichMon
	setvar VAR_0x8005, MOVETUTOR_THUNDER_WAVE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_ThunderWaveDeclined
	removemoney 6500
	goto EventScript_ThunderWaveTaught
	end

EventScript_ThunderWaveDeclined::
	msgbox Text_ThunderWaveDeclined
	release
	end

EventScript_ThunderWaveTaught::
	msgbox Text_ThunderWaveTaught
	release
	end

RockTunnel_B1F_EventScript_RockSlideTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_ROCK_SLIDE, EventScript_RockSlideRepeat
	msgbox Text_RockSlideTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_RockSlideDeclined
	msgbox Text_RockSlideWhichMon
	setvar VAR_0x8005, MOVETUTOR_ROCK_SLIDE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_RockSlideDeclined
	setflag FLAG_TUTOR_ROCK_SLIDE
	goto EventScript_RockSlideTaught
	end

EventScript_RockSlideRepeat::
	msgbox Text_FullTutorRepeat_RockSlide, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_RockSlideDeclined
	checkmoney 7500
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_RockSlideWhichMon
	setvar VAR_0x8005, MOVETUTOR_ROCK_SLIDE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_RockSlideDeclined
	removemoney 7500
	goto EventScript_RockSlideTaught
	end

EventScript_RockSlideDeclined::
	msgbox Text_RockSlideDeclined
	release
	end

EventScript_RockSlideTaught::
	msgbox Text_RockSlideTaught
	release
	end

MtEmber_Exterior_EventScript_ExplosionTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_EXPLOSION, EventScript_ExplosionRepeat
	msgbox Text_ExplosionTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_ExplosionDeclined
	msgbox Text_ExplosionWhichMon
	setvar VAR_0x8005, MOVETUTOR_EXPLOSION
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_ExplosionDeclined
	setflag FLAG_TUTOR_EXPLOSION
	goto EventScript_ExplosionTaught
	end

EventScript_ExplosionRepeat::
	msgbox Text_FullTutorRepeat_Explosion, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_ExplosionDeclined
	checkmoney 6000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_ExplosionWhichMon
	setvar VAR_0x8005, MOVETUTOR_EXPLOSION
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_ExplosionDeclined
	removemoney 6000
	goto EventScript_ExplosionTaught
	end

EventScript_ExplosionDeclined::
	msgbox Text_ExplosionDeclined
	release
	end

EventScript_ExplosionTaught::
	msgbox Text_ExplosionTaught
	release
	end

Route4_EventScript_MegaPunchTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_MEGA_PUNCH, EventScript_MegaPunchRepeat
	msgbox Text_MegaPunchTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MegaPunchDeclined
	msgbox Text_MegaPunchWhichMon
	setvar VAR_0x8005, MOVETUTOR_MEGA_PUNCH
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_MegaPunchDeclined
	setflag FLAG_TUTOR_MEGA_PUNCH
	goto EventScript_MegaPunchTaught
	end

EventScript_MegaPunchRepeat::
	msgbox Text_FullTutorRepeat_MegaPunch, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MegaPunchDeclined
	checkmoney 1500
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_MegaPunchWhichMon
	setvar VAR_0x8005, MOVETUTOR_MEGA_PUNCH
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_MegaPunchDeclined
	removemoney 1500
	goto EventScript_MegaPunchTaught
	end

EventScript_MegaPunchDeclined::
	msgbox Text_MegaPunchDeclined
	release
	end

EventScript_MegaPunchTaught::
	msgbox Text_MegaPunchTaught
	release
	end

Route4_EventScript_MegaKickTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_MEGA_KICK, EventScript_MegaKickRepeat
	msgbox Text_MegaKickTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MegaKickDeclined
	msgbox Text_MegaKickWhichMon
	setvar VAR_0x8005, MOVETUTOR_MEGA_KICK
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_MegaKickDeclined
	setflag FLAG_TUTOR_MEGA_KICK
	goto EventScript_MegaKickTaught
	end

EventScript_MegaKickRepeat::
	msgbox Text_FullTutorRepeat_MegaKick, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MegaKickDeclined
	checkmoney 2500
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_MegaKickWhichMon
	setvar VAR_0x8005, MOVETUTOR_MEGA_KICK
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_MegaKickDeclined
	removemoney 2500
	goto EventScript_MegaKickTaught
	end

EventScript_MegaKickDeclined::
	msgbox Text_MegaKickDeclined
	release
	end

EventScript_MegaKickTaught::
	msgbox Text_MegaKickTaught
	release
	end

EventScript_DreamEaterTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_DREAM_EATER, EventScript_DreamEaterRepeat
	msgbox Text_DreamEaterTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_DreamEaterDeclined
	msgbox Text_DreamEaterWhichMon
	setvar VAR_0x8005, MOVETUTOR_DREAM_EATER
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_DreamEaterDeclined
	setflag FLAG_TUTOR_DREAM_EATER
	goto EventScript_DreamEaterTaught
	end

EventScript_DreamEaterRepeat::
	msgbox Text_FullTutorRepeat_DreamEater, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_DreamEaterDeclined
	checkmoney 3000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_DreamEaterWhichMon
	setvar VAR_0x8005, MOVETUTOR_DREAM_EATER
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_DreamEaterDeclined
	removemoney 3000
	goto EventScript_DreamEaterTaught
	end

EventScript_DreamEaterDeclined::
	msgbox Text_DreamEaterDeclined
	release
	end

EventScript_DreamEaterTaught::
	msgbox Text_DreamEaterTaught
	release
	end

EventScript_SoftboiledTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_SOFT_BOILED, EventScript_SoftboiledRepeat
	msgbox Text_SoftboiledTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SoftboiledDeclined
	msgbox Text_SoftboiledWhichMon
	setvar VAR_0x8005, MOVETUTOR_SOFT_BOILED
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SoftboiledDeclined
	setflag FLAG_TUTOR_SOFT_BOILED
	goto EventScript_SoftboiledTaught
	end

EventScript_SoftboiledRepeat::
	msgbox Text_FullTutorRepeat_Softboiled, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SoftboiledDeclined
	checkmoney 5000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_SoftboiledWhichMon
	setvar VAR_0x8005, MOVETUTOR_SOFT_BOILED
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SoftboiledDeclined
	removemoney 5000
	goto EventScript_SoftboiledTaught
	end

EventScript_SoftboiledDeclined::
	msgbox Text_SoftboiledDeclined
	release
	end

EventScript_SoftboiledTaught::
	msgbox Text_SoftboiledTaught
	release
	end

FuchsiaCity_EventScript_SubstituteTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_SUBSTITUTE, EventScript_SubstituteRepeat
	msgbox Text_SubstituteTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SubstituteDeclined
	msgbox Text_SubstituteWhichMon
	setvar VAR_0x8005, MOVETUTOR_SUBSTITUTE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SubstituteDeclined
	setflag FLAG_TUTOR_SUBSTITUTE
	goto EventScript_SubstituteTaught
	end

EventScript_SubstituteRepeat::
	msgbox Text_FullTutorRepeat_Substitute, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SubstituteDeclined
	checkmoney 8000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_SubstituteWhichMon
	setvar VAR_0x8005, MOVETUTOR_SUBSTITUTE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SubstituteDeclined
	removemoney 8000
	goto EventScript_SubstituteTaught
	end

EventScript_SubstituteDeclined::
	msgbox Text_SubstituteDeclined
	release
	end

EventScript_SubstituteTaught::
	msgbox Text_SubstituteTaught
	release
	end

SevenIsland_EventScript_SwordsDanceTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_SWORDS_DANCE, EventScript_SwordsDanceRepeat
	msgbox Text_SwordsDanceTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SwordsDanceDeclined
	msgbox Text_SwordsDanceWhichMon
	setvar VAR_0x8005, MOVETUTOR_SWORDS_DANCE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SwordsDanceDeclined
	setflag FLAG_TUTOR_SWORDS_DANCE
	goto EventScript_SwordsDanceTaught
	end

EventScript_SwordsDanceRepeat::
	msgbox Text_FullTutorRepeat_SwordsDance, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SwordsDanceDeclined
	checkmoney 10000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_SwordsDanceWhichMon
	setvar VAR_0x8005, MOVETUTOR_SWORDS_DANCE
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SwordsDanceDeclined
	removemoney 10000
	goto EventScript_SwordsDanceTaught
	end

EventScript_SwordsDanceDeclined::
	msgbox Text_SwordsDanceDeclined
	release
	end

EventScript_SwordsDanceTaught::
	msgbox Text_SwordsDanceTaught
	release
	end

PewterCity_Museum_1F_EventScript_SeismicTossTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_SEISMIC_TOSS, EventScript_SeismicTossRepeat
	msgbox Text_SeismicTossTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SeismicTossDeclined
	msgbox Text_SeismicTossWhichMon
	setvar VAR_0x8005, MOVETUTOR_SEISMIC_TOSS
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SeismicTossDeclined
	setflag FLAG_TUTOR_SEISMIC_TOSS
	goto EventScript_SeismicTossTaught
	end

EventScript_SeismicTossRepeat::
	msgbox Text_FullTutorRepeat_SeismicToss, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_SeismicTossDeclined
	checkmoney 3500
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_SeismicTossWhichMon
	setvar VAR_0x8005, MOVETUTOR_SEISMIC_TOSS
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_SeismicTossDeclined
	removemoney 3500
	goto EventScript_SeismicTossTaught
	end

EventScript_SeismicTossDeclined::
	msgbox Text_SeismicTossDeclined
	release
	end

EventScript_SeismicTossTaught::
	msgbox Text_SeismicTossTaught
	release
	end

EventScript_CounterTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_COUNTER, EventScript_CounterRepeat
	msgbox Text_CounterTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_CounterDeclined
	msgbox Text_CounterWhichMon
	setvar VAR_0x8005, MOVETUTOR_COUNTER
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_CounterDeclined
	setflag FLAG_TUTOR_COUNTER
	goto EventScript_CounterTaught
	end

EventScript_CounterRepeat::
	msgbox Text_FullTutorRepeat_Counter, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_CounterDeclined
	checkmoney 4000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_CounterWhichMon
	setvar VAR_0x8005, MOVETUTOR_COUNTER
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_CounterDeclined
	removemoney 4000
	goto EventScript_CounterTaught
	end

EventScript_CounterDeclined::
	msgbox Text_CounterDeclined
	release
	end

EventScript_CounterTaught::
	msgbox Text_CounterTaught
	release
	end

EventScript_MetronomeTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_METRONOME, EventScript_MetronomeRepeat
	msgbox Text_MetronomeTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MetronomeDeclined
	msgbox Text_MetronomeWhichMon
	setvar VAR_0x8005, MOVETUTOR_METRONOME
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_MetronomeDeclined
	setflag FLAG_TUTOR_METRONOME
	goto EventScript_MetronomeTaught
	end

EventScript_MetronomeRepeat::
	msgbox Text_FullTutorRepeat_Metronome, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MetronomeDeclined
	checkmoney 1000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_MetronomeWhichMon
	setvar VAR_0x8005, MOVETUTOR_METRONOME
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_MetronomeDeclined
	removemoney 1000
	goto EventScript_MetronomeTaught
	end

EventScript_MetronomeDeclined::
	msgbox Text_MetronomeDeclined
	release
	end

EventScript_MetronomeTaught::
	msgbox Text_MetronomeTaught
	release
	end

EventScript_MimicTutor::
	goto_if_set FLAG_TUTOR_MIMIC, EventScript_MimicRepeat
	msgbox Text_MimicTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MimicDeclined
	msgbox Text_MimicWhichMon
	setvar VAR_0x8005, MOVETUTOR_MIMIC
	call EventScript_ChooseMoveTutorMon
	lock
	faceplayer
	goto_if_eq VAR_RESULT, 0, EventScript_MimicDeclined
	removeitem ITEM_POKE_DOLL
	setflag FLAG_TUTOR_MIMIC
	goto EventScript_MimicTaught
	end

EventScript_MimicRepeat::
	msgbox Text_FullTutorRepeat_Mimic, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_MimicDeclined
	checkmoney 2000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_MimicWhichMon
	setvar VAR_0x8005, MOVETUTOR_MIMIC
	call EventScript_ChooseMoveTutorMon
	lock
	faceplayer
	goto_if_eq VAR_RESULT, FALSE, EventScript_MimicDeclined
	removemoney 2000
	goto EventScript_MimicTaught
	end

EventScript_MimicDeclined::
	msgbox Text_MimicDeclined
	release
	end

EventScript_MimicTaught::
	checkplayergender
	call_if_eq VAR_RESULT, MALE, EventScript_MimicTaughtMale
	call_if_eq VAR_RESULT, FEMALE, EventScript_MimicTaughtFemale
	release
	end

EventScript_MimicTaughtMale::
	msgbox Text_MimicTaughtMale
	return

EventScript_MimicTaughtFemale::
	msgbox Text_MimicTaughtFemale
	return

FourIsland_House1_EventScript_BodySlamTutor::
	lock
	faceplayer
	goto_if_set FLAG_TUTOR_BODY_SLAM, EventScript_BodySlamRepeat
	msgbox Text_BodySlamTeach, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_BodySlamDeclined
	msgbox Text_BodySlamWhichMon
	setvar VAR_0x8005, MOVETUTOR_BODY_SLAM
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_BodySlamDeclined
	setflag FLAG_TUTOR_BODY_SLAM
	goto EventScript_BodySlamTaught
	end

EventScript_BodySlamRepeat::
	msgbox Text_FullTutorRepeat_BodySlam, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_BodySlamDeclined
	checkmoney 6000
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullTutorNotEnoughMoney
	msgbox Text_BodySlamWhichMon
	setvar VAR_0x8005, MOVETUTOR_BODY_SLAM
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, EventScript_BodySlamDeclined
	removemoney 6000
	goto EventScript_BodySlamTaught
	end

EventScript_BodySlamDeclined::
	msgbox Text_BodySlamDeclined
	release
	end

EventScript_BodySlamTaught::
	msgbox Text_BodySlamTaught
	release
	end

TwoIsland_CapeBrink_House_EventScript_StarterTutor::
	goto_if_questlog EventScript_ReleaseEnd
	special QuestLog_CutRecording
	lock
	faceplayer
	bufferleadmonspeciesname STR_VAR_1
	msgbox Text_UltimateMoveThatMon
	specialvar VAR_RESULT, CapeBrinkGetMoveToTeachLeadPokemon
	goto_if_eq VAR_RESULT, FALSE, CapeBrinkTutor_EventScript_NoLeadStarter
	copyvar VAR_0x8009, VAR_0x8005
	call_if_eq VAR_FACING, DIR_NORTH, CapeBrinkTutor_EventScript_JumpInPlaceDown
	call_if_eq VAR_FACING, DIR_SOUTH, CapeBrinkTutor_EventScript_JumpInPlaceUp
	call_if_eq VAR_FACING, DIR_EAST, CapeBrinkTutor_EventScript_JumpInPlaceLeft
	call_if_eq VAR_FACING, DIR_WEST, CapeBrinkTutor_EventScript_JumpInPlaceRight
	goto_if_eq VAR_0x8008, TRUE, CapeBrinkTutor_EventScript_RepeatOffer
	msgbox Text_AllowMeToTeachMonUltimateMove, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, CapeBrinkTutor_EventScript_DeclineMove
	goto CapeBrinkTutor_EventScript_StartTeaching

CapeBrinkTutor_EventScript_RepeatOffer::
	checkmoney 10000
	goto_if_eq VAR_RESULT, FALSE, CapeBrinkTutor_EventScript_NotEnoughMoney
	msgbox Text_FullCapeBrinkRepeat, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, CapeBrinkTutor_EventScript_DeclineMove

CapeBrinkTutor_EventScript_StartTeaching::
	msgbox Text_LetMeConferUltimateMove
	closemessage
	fadescreen FADE_TO_BLACK
	goto CapeBrinkTutor_EventScript_ChooseMon

@ Unused
CapeBrinkTutor_EventScript_FadeTaughtMove::
	fadescreen FADE_FROM_BLACK
	goto CapeBrinkTutor_EventScript_TaughtMove
	end

CapeBrinkTutor_EventScript_MoveJustTaught::
	msgbox Text_MakeBestUseOfMove
	release
	end

CapeBrinkTutor_EventScript_TaughtAllMoves::
	msgbox Text_FeelRejuvenated
	release
	end

CapeBrinkTutor_EventScript_TaughtMove::
	copyvar VAR_0x8005, VAR_0x8009
	call_if_eq VAR_0x8008, TRUE, CapeBrinkTutor_EventScript_ChargeRepeat
	specialvar VAR_RESULT, HasLearnedAllMovesFromCapeBrinkTutor
	goto_if_eq VAR_RESULT, TRUE, CapeBrinkTutor_EventScript_LearnedAllMoves
	msgbox Text_TaughtMove
	setflag FLAG_TEMP_2
	release
	end

CapeBrinkTutor_EventScript_LearnedAllMoves::
	msgbox Text_PassedOnEverythingIKnow
	setflag FLAG_LEARNED_ALL_MOVES_AT_CAPE_BRINK
	release
	end

CapeBrinkTutor_EventScript_ChooseMon::
	call EventScript_ChooseMoveTutorMon
	goto_if_eq VAR_RESULT, FALSE, CapeBrinkTutor_EventScript_DeclineMove
	goto CapeBrinkTutor_EventScript_TaughtMove
	end

CapeBrinkTutor_EventScript_JumpInPlaceDown::
	applymovement LOCALID_CAPE_BRINK_TUTOR, Movement_JumpInPlaceDown
	waitmovement 0
	return

CapeBrinkTutor_EventScript_JumpInPlaceUp::
	applymovement LOCALID_CAPE_BRINK_TUTOR, Movement_JumpInPlaceUp
	waitmovement 0
	return

CapeBrinkTutor_EventScript_JumpInPlaceLeft::
	applymovement LOCALID_CAPE_BRINK_TUTOR, Movement_JumpInPlaceLeft
	waitmovement 0
	return

CapeBrinkTutor_EventScript_JumpInPlaceRight::
	applymovement LOCALID_CAPE_BRINK_TUTOR, Movement_JumpInPlaceRight
	waitmovement 0
	return

CapeBrinkTutor_EventScript_ChargeRepeat::
	removemoney 10000
	return

CapeBrinkTutor_EventScript_NotEnoughMoney::
	msgbox Text_FullCapeBrinkNotEnoughMoney
	release
	end

CapeBrinkTutor_EventScript_DeclineMove::
	msgbox Text_YouRejectIt
	release
	end

CapeBrinkTutor_EventScript_NoLeadStarter::
	msgbox Text_JustMistaken
	release
	end

EventScript_ChooseMoveTutorMon::
	special ChooseMonForMoveTutor
	waitstate
	lock
	faceplayer
	return

EventScript_CanOnlyBeLearnedOnce::
	textcolor NPC_TEXT_COLOR_NEUTRAL
	special DisableMsgBoxWalkaway
	signmsg
	msgbox Text_MoveCanOnlyBeLearnedOnce, MSGBOX_YESNO
	normalmsg
	call EventScript_RestorePrevTextColor
	return

Movement_JumpInPlaceDown:
	jump_in_place_down
	step_end

Movement_JumpInPlaceUp:
	jump_in_place_up
	step_end

Movement_JumpInPlaceLeft:
	jump_in_place_left
	step_end

Movement_JumpInPlaceRight:
	jump_in_place_right
	step_end


EventScript_FullTutorNotEnoughMoney::
	msgbox Text_FullTutorNotEnoughMoney
	release
	end

Text_FullTutorNotEnoughMoney::
	.string "No tienes suficiente dinero para\n"
	.string "otra lección.$"

Text_FullTutorRepeat_DoubleEdge::
	.string "Puedo enseñarlo otra vez por 5000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_ThunderWave::
	.string "Puedo enseñarlo otra vez por 6500.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_RockSlide::
	.string "Puedo enseñarlo otra vez por 7500.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_Explosion::
	.string "Puedo enseñarlo otra vez por 6000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_MegaPunch::
	.string "Puedo enseñarlo otra vez por 1500.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_MegaKick::
	.string "Puedo enseñarlo otra vez por 2500.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_DreamEater::
	.string "Puedo enseñarlo otra vez por 3000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_Softboiled::
	.string "Puedo enseñarlo otra vez por 5000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_Substitute::
	.string "Puedo enseñarlo otra vez por 8000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_SwordsDance::
	.string "Puedo enseñarlo otra vez por 10000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_SeismicToss::
	.string "Puedo enseñarlo otra vez por 3500.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_Counter::
	.string "Puedo enseñarlo otra vez por 4000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_Metronome::
	.string "Puedo enseñarlo otra vez por 1000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_Mimic::
	.string "Puedo enseñarlo otra vez por 2000.\n"
	.string "¿Quieres otra lección?$"

Text_FullTutorRepeat_BodySlam::
	.string "Puedo enseñarlo otra vez por 6000.\n"
	.string "¿Quieres otra lección?$"


Text_FullCapeBrinkRepeat::
	.string "Ya transmití este movimiento una vez.\p"
	.string "Puedo enseñarlo de nuevo por 10000.\n"
	.string "¿Quieres otra lección?$"

Text_FullCapeBrinkNotEnoughMoney::
	.string "Necesitas 10000 para repetir esta\n"
	.string "lección.$"
