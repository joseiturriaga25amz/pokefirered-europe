#ifndef GUARD_START_MENU_H
#define GUARD_START_MENU_H

#include "global.h"

void AppendToList(u8 *list, u8 *pos, u8 newEntry);
void Task_StartMenuHandleInput(u8 taskId);
void SetUpReturnToStartMenu(void);
void ShowStartMenu(void);
// Transient non-link field Start/Save UI, not arbitrary script locks.
bool8 StartMenu_IsSafeForFollower(void);
void Field_AskSaveTheGame(void);
void CB2_SetUpSaveAfterLinkBattle(void);

#endif // GUARD_START_MENU_H
