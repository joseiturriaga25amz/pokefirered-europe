#ifndef GUARD_FULL_FOLLOWER_H
#define GUARD_FULL_FOLLOWER_H

#include "global.h"

#define OBJ_EVENT_ID_FULL_FOLLOWER 254

void FullFollower_OnLocalMapReady(void);
void FullFollower_DiscardForLink(void);
void FullFollower_DiscardForLocalReload(void);
void FullFollower_RecallForWarp(void);
void FullFollower_OnCameraCoordsShift(s16 dx, s16 dy);
void FullFollower_SetEnabled(bool8 enabled);
bool8 FullFollower_IsEnabled(void);
u8 FullFollower_GetSpriteGraphicsId(void);
// Runtime-only variant key for future registered normal/shiny overworld graphics.
bool8 FullFollower_IsShiny(void);
// Unsaved, 16-bit National species key; never changes 8-bit object graphics ID.
u16 FullFollower_GetSpecies(void);
// Pilot only; final 386-species asset registry will replace this gate.
bool8 FullFollower_UsesPilotGraphics(void);

#endif // GUARD_FULL_FOLLOWER_H
