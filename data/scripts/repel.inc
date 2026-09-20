EventScript_RepelWoreOff::
	setvar VAR_0x8004, ITEM_NONE
	checkitem VAR_FULL_LAST_REPEL, 1
	goto_if_eq VAR_RESULT, TRUE, EventScript_RepelReuseLastType
	checkitem ITEM_MAX_REPEL, 1
	goto_if_eq VAR_RESULT, TRUE, EventScript_RepelSelectMax
	checkitem ITEM_SUPER_REPEL, 1
	goto_if_eq VAR_RESULT, TRUE, EventScript_RepelSelectSuper
	checkitem ITEM_REPEL, 1
	goto_if_eq VAR_RESULT, TRUE, EventScript_RepelSelectNormal
	msgbox Text_RepelWoreOff, MSGBOX_SIGN
	end

EventScript_RepelReuseLastType::
	copyvar VAR_0x8004, VAR_FULL_LAST_REPEL
	goto EventScript_RepelAskReuse

EventScript_RepelSelectMax::
	setvar VAR_0x8004, ITEM_MAX_REPEL
	goto EventScript_RepelAskReuse

EventScript_RepelSelectSuper::
	setvar VAR_0x8004, ITEM_SUPER_REPEL
	goto EventScript_RepelAskReuse

EventScript_RepelSelectNormal::
	setvar VAR_0x8004, ITEM_REPEL

EventScript_RepelAskReuse::
	bufferitemname STR_VAR_1, VAR_0x8004
	msgbox Text_RepelWoreOffUseAnother, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, EventScript_RepelReuseEnd
	removeitem VAR_0x8004, 1
	goto_if_eq VAR_RESULT, FALSE, EventScript_RepelReuseEnd
	copyvar VAR_FULL_LAST_REPEL, VAR_0x8004
	goto_if_eq VAR_0x8004, ITEM_MAX_REPEL, EventScript_RepelApplyMax
	goto_if_eq VAR_0x8004, ITEM_SUPER_REPEL, EventScript_RepelApplySuper
	setvar VAR_REPEL_STEP_COUNT, 100
	goto EventScript_RepelReuseApplied

EventScript_RepelApplySuper::
	setvar VAR_REPEL_STEP_COUNT, 200
	goto EventScript_RepelReuseApplied

EventScript_RepelApplyMax::
	setvar VAR_REPEL_STEP_COUNT, 250

EventScript_RepelReuseApplied::
	playse SE_REPEL
	end

EventScript_RepelReuseEnd::
	end

Text_RepelWoreOff::
	.string "REPEL's effect wore off…$"

Text_RepelWoreOffUseAnother::
	.string "REPEL's effect wore off…\\nUse another {STR_VAR_1}?$"
