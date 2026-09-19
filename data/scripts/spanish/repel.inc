EventScript_RepelWoreOff::
	checkitem ITEM_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullRepelOffer
	checkitem ITEM_SUPER_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullRepelOffer
	checkitem ITEM_MAX_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullRepelOffer
	msgbox Text_RepelWoreOff, MSGBOX_SIGN
	end

EventScript_FullRepelOffer::
	msgbox Text_FullUseAnotherRepel, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_FullRepelEnd

	compare VAR_FULL_LAST_REPEL, ITEM_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullReuseRepel
	compare VAR_FULL_LAST_REPEL, ITEM_SUPER_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullReuseSuperRepel
	compare VAR_FULL_LAST_REPEL, ITEM_MAX_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullReuseMaxRepel

	goto EventScript_FullUseFallbackRepel

EventScript_FullReuseRepel::
	checkitem ITEM_REPEL
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullUseFallbackRepel
	removeitem ITEM_REPEL
	setvar VAR_REPEL_STEP_COUNT, 100
	setvar VAR_FULL_LAST_REPEL, ITEM_REPEL
	goto EventScript_FullRepelUsed

EventScript_FullReuseSuperRepel::
	checkitem ITEM_SUPER_REPEL
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullUseFallbackRepel
	removeitem ITEM_SUPER_REPEL
	setvar VAR_REPEL_STEP_COUNT, 200
	setvar VAR_FULL_LAST_REPEL, ITEM_SUPER_REPEL
	goto EventScript_FullRepelUsed

EventScript_FullReuseMaxRepel::
	checkitem ITEM_MAX_REPEL
	goto_if_eq VAR_RESULT, FALSE, EventScript_FullUseFallbackRepel
	removeitem ITEM_MAX_REPEL
	setvar VAR_REPEL_STEP_COUNT, 250
	setvar VAR_FULL_LAST_REPEL, ITEM_MAX_REPEL
	goto EventScript_FullRepelUsed

EventScript_FullUseFallbackRepel::
	checkitem ITEM_MAX_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullReuseMaxRepel
	checkitem ITEM_SUPER_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullReuseSuperRepel
	checkitem ITEM_REPEL
	goto_if_eq VAR_RESULT, TRUE, EventScript_FullReuseRepel
	goto EventScript_FullRepelEnd

EventScript_FullRepelUsed::
	msgbox Text_FullRepelUsed, MSGBOX_SIGN
	end

EventScript_FullRepelEnd::
	msgbox Text_RepelWoreOff, MSGBOX_SIGN
	end

Text_RepelWoreOff::
	.string "El REPELENTE ha dejado de hacer\n"
	.string "efecto.$"

Text_FullUseAnotherRepel::
	.string "El REPELENTE ha dejado de hacer\n"
	.string "efecto. ¿Quieres usar otro?$"

Text_FullRepelUsed::
	.string "Has usado otro REPELENTE.$"
