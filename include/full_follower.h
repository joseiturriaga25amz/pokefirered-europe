#ifndef GUARD_FULL_FOLLOWER_H
#define GUARD_FULL_FOLLOWER_H

#include "global.h"

#define OBJ_EVENT_ID_FULL_FOLLOWER 254

void FullFollower_OnLocalMapReady(void);
void FullFollower_DiscardForLink(void);
void FullFollower_DiscardForLocalReload(void);
void FullFollower_RecallForWarp(void);
// Bounded trainer-intro presentation and battle-scene sprite teardown.
void FullFollower_BeginTrainerIntro(void);
void FullFollower_RecallForBattle(void);
void FullFollower_OnCameraCoordsShift(s16 dx, s16 dy);
void FullFollower_SetEnabled(bool8 enabled);
bool8 FullFollower_IsEnabled(void);
// Runtime-only exemption for statically verified, one-message field scripts.
void FullFollower_ClearSafeDialogue(void);
void FullFollower_BeginSafeDialogue(const u8 *script);
// Returns a script only for the actual current, healthy party follower.
const u8 *FullFollower_GetFriendshipInteractionScript(void);
u8 FullFollower_GetSpriteGraphicsId(void);
// Runtime-only variant key for future registered normal/shiny overworld graphics.
bool8 FullFollower_IsShiny(void);
// Unsaved, 16-bit National species key; never changes 8-bit object graphics ID.
u16 FullFollower_GetSpecies(void);
// Expects National Dex species ID, NOT Gen III internal species ID.
bool8 FullFollower_HasRegisteredGraphics(u16 nationalDexNum);
// Pilot only; final 386-species asset registry will replace this gate.
bool8 FullFollower_UsesPilotGraphics(void);

#endif // GUARD_FULL_FOLLOWER_H
