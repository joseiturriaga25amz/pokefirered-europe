CeladonCity_DepartmentStore_4F_MapScripts::
	.byte 0

CeladonCity_DepartmentStore_4F_EventScript_Man::
	msgbox CeladonCity_DepartmentStore_4F_Text_GettingPokeDollAsPresent, MSGBOX_NPC
	end

CeladonCity_DepartmentStore_4F_EventScript_Youngster::
	msgbox CeladonCity_DepartmentStore_4F_Text_CanRunAwayWithPokeDoll, MSGBOX_NPC
	end

CeladonCity_DepartmentStore_4F_EventScript_FloorSign::
	msgbox CeladonCity_DepartmentStore_4F_Text_FloorSign, MSGBOX_SIGN
	end

CeladonCity_DepartmentStore_4F_EventScript_Clerk::
	goto_if_questlog EventScript_ReleaseEnd
	lock
	faceplayer
	message Text_MayIHelpYou
	waitmessage
	goto_if_set FLAG_SYS_NATIONAL_DEX, CeladonCity_DepartmentStore_4F_EventScript_PostNationalShop
	pokemart CeladonCity_DepartmentStore_4F_Items
	goto CeladonCity_DepartmentStore_4F_EventScript_AfterShop

CeladonCity_DepartmentStore_4F_EventScript_PostNationalShop::
	pokemart CeladonCity_DepartmentStore_4F_PostNationalItems

CeladonCity_DepartmentStore_4F_EventScript_AfterShop::
	msgbox Text_PleaseComeAgain
	release
	end

	.align 2
CeladonCity_DepartmentStore_4F_Items::
	.2byte ITEM_POKE_DOLL
	.2byte ITEM_RETRO_MAIL
	.2byte ITEM_FIRE_STONE
	.2byte ITEM_THUNDER_STONE
	.2byte ITEM_WATER_STONE
	.2byte ITEM_LEAF_STONE
	.2byte ITEM_SOFT_SAND
	.2byte ITEM_HARD_STONE
	.2byte ITEM_MIRACLE_SEED
	.2byte ITEM_BLACK_GLASSES
	.2byte ITEM_BLACK_BELT
	.2byte ITEM_MAGNET
	.2byte ITEM_MYSTIC_WATER
	.2byte ITEM_SHARP_BEAK
	.2byte ITEM_POISON_BARB
	.2byte ITEM_NEVER_MELT_ICE
	.2byte ITEM_SPELL_TAG
	.2byte ITEM_TWISTED_SPOON
	.2byte ITEM_CHARCOAL
	.2byte ITEM_DRAGON_FANG
	.2byte ITEM_SILK_SCARF
	.2byte ITEM_SILVER_POWDER
	.2byte ITEM_NONE
	release
	end

	.align 2
CeladonCity_DepartmentStore_4F_PostNationalItems::
	.2byte ITEM_POKE_DOLL
	.2byte ITEM_RETRO_MAIL
	.2byte ITEM_FIRE_STONE
	.2byte ITEM_THUNDER_STONE
	.2byte ITEM_WATER_STONE
	.2byte ITEM_LEAF_STONE
	.2byte ITEM_SUN_STONE
	.2byte ITEM_MOON_STONE
	.2byte ITEM_KINGS_ROCK
	.2byte ITEM_METAL_COAT
	.2byte ITEM_DRAGON_SCALE
	.2byte ITEM_UP_GRADE
	.2byte ITEM_QUICK_CLAW
	.2byte ITEM_LUCKY_PUNCH
	.2byte ITEM_STICK
	.2byte ITEM_SCOPE_LENS
	.2byte ITEM_FOCUS_BAND
	.2byte ITEM_METAL_POWDER
	.2byte ITEM_SHELL_BELL
	.2byte ITEM_BRIGHT_POWDER
	.2byte ITEM_LIGHT_BALL
	.2byte ITEM_LEFTOVERS
	.2byte ITEM_THICK_CLUB
	.2byte ITEM_CHOICE_BAND
	.2byte ITEM_LUCKY_EGG
	.2byte ITEM_ETHER
	.2byte ITEM_MAX_ETHER
	.2byte ITEM_ELIXIR
	.2byte ITEM_MAX_ELIXIR
	.2byte ITEM_SOFT_SAND
	.2byte ITEM_HARD_STONE
	.2byte ITEM_MIRACLE_SEED
	.2byte ITEM_BLACK_GLASSES
	.2byte ITEM_BLACK_BELT
	.2byte ITEM_MAGNET
	.2byte ITEM_MYSTIC_WATER
	.2byte ITEM_SHARP_BEAK
	.2byte ITEM_POISON_BARB
	.2byte ITEM_NEVER_MELT_ICE
	.2byte ITEM_SPELL_TAG
	.2byte ITEM_TWISTED_SPOON
	.2byte ITEM_CHARCOAL
	.2byte ITEM_DRAGON_FANG
	.2byte ITEM_SILK_SCARF
	.2byte ITEM_SILVER_POWDER
	.2byte ITEM_NONE
	release
	end
