#ifndef GUARD_FULL_FOLLOWER_H
#define GUARD_FULL_FOLLOWER_H

#include "global.h"

#define OBJ_EVENT_ID_FULL_FOLLOWER 254

void FullFollower_OnLocalMapReady(void);
void FullFollower_SetEnabled(bool8 enabled);
bool8 FullFollower_IsEnabled(void);

#endif // GUARD_FULL_FOLLOWER_H
