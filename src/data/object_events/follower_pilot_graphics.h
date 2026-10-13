/* Diagnostic-only graphics for proving FireRed-native 4-direction / 4-frame
   follower presentation. NOT Pokemon artwork and NOT the accepted final sprites. */
static const u32 sFollowerPilotPixels[16][32] = {
    /* South frame 0 */
    {0x00000000, 0x00000000, 0x00000000, 0x44440000, 0x44440000, 0x44440000, 0x11120000, 0x11110000, 0x00000000, 0x00000000, 0x00000000, 0x00004444, 0x00004444, 0x00004444, 0x00001121, 0x00001112, 0x21110000, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x33300000, 0x00000000, 0x00000000, 0x00001111, 0x00002111, 0x00001211, 0x00001121, 0x00001112, 0x00003333, 0x00000000, 0x00000000},
    /* South frame 1 */
    {0x00000000, 0x00000000, 0x00000000, 0x44440000, 0x44440000, 0x44440000, 0x12110000, 0x11210000, 0x00000000, 0x00000000, 0x00000000, 0x00004444, 0x00004444, 0x00004444, 0x00002111, 0x00001211, 0x11120000, 0x11110000, 0x21110000, 0x12110000, 0x11210000, 0x33000000, 0x00000000, 0x00000000, 0x00001121, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x00003333, 0x00000000, 0x00000000},
    /* South frame 2 */
    {0x00000000, 0x00000000, 0x00000000, 0x44440000, 0x44440000, 0x44440000, 0x11110000, 0x21110000, 0x00000000, 0x00000000, 0x00000000, 0x00004444, 0x00004444, 0x00004444, 0x00001112, 0x00001111, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x30000000, 0x00000000, 0x00000000, 0x00002111, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x00003333, 0x00000000, 0x00000000},
    /* South frame 3 */
    {0x00000000, 0x00000000, 0x00000000, 0x44440000, 0x44440000, 0x44440000, 0x11210000, 0x11120000, 0x00000000, 0x00000000, 0x00000000, 0x00004444, 0x00004444, 0x00004444, 0x00001211, 0x00001121, 0x11110000, 0x21110000, 0x12110000, 0x11210000, 0x11120000, 0x00000000, 0x00000000, 0x00000000, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x00001121, 0x00003333, 0x00000000, 0x00000000},
    /* North frame 0 */
    {0x00000000, 0x00000000, 0x00000000, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x00000000, 0x00000000, 0x00000000, 0x00002111, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x12110000, 0x11210000, 0x44440000, 0x44440000, 0x44440000, 0x33300000, 0x00000000, 0x00000000, 0x00002111, 0x00001211, 0x00004444, 0x00004444, 0x00004444, 0x00003333, 0x00000000, 0x00000000},
    /* North frame 1 */
    {0x00000000, 0x00000000, 0x00000000, 0x11110000, 0x21110000, 0x12110000, 0x11210000, 0x11120000, 0x00000000, 0x00000000, 0x00000000, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x00001121, 0x11110000, 0x21110000, 0x44440000, 0x44440000, 0x44440000, 0x33000000, 0x00000000, 0x00000000, 0x00001112, 0x00001111, 0x00004444, 0x00004444, 0x00004444, 0x00003333, 0x00000000, 0x00000000},
    /* North frame 2 */
    {0x00000000, 0x00000000, 0x00000000, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x12110000, 0x00000000, 0x00000000, 0x00000000, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x00002111, 0x11210000, 0x11120000, 0x44440000, 0x44440000, 0x44440000, 0x30000000, 0x00000000, 0x00000000, 0x00001211, 0x00001121, 0x00004444, 0x00004444, 0x00004444, 0x00003333, 0x00000000, 0x00000000},
    /* North frame 3 */
    {0x00000000, 0x00000000, 0x00000000, 0x21110000, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x00000000, 0x00000000, 0x00000000, 0x00001111, 0x00002111, 0x00001211, 0x00001121, 0x00001112, 0x21110000, 0x12110000, 0x44440000, 0x44440000, 0x44440000, 0x00000000, 0x00000000, 0x00000000, 0x00001111, 0x00002111, 0x00004444, 0x00004444, 0x00004444, 0x00003333, 0x00000000, 0x00000000},
    /* West frame 0 */
    {0x00000000, 0x00000000, 0x00000000, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x12110000, 0x00000000, 0x00000000, 0x00000000, 0x00004441, 0x00004441, 0x00004442, 0x00004441, 0x00004441, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x12110000, 0x33300000, 0x00000000, 0x00000000, 0x00004441, 0x00004441, 0x00004442, 0x00004441, 0x00004441, 0x00003333, 0x00000000, 0x00000000},
    /* West frame 1 */
    {0x00000000, 0x00000000, 0x00000000, 0x21110000, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x00000000, 0x00000000, 0x00000000, 0x00004441, 0x00004441, 0x00004441, 0x00004441, 0x00004442, 0x21110000, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x33000000, 0x00000000, 0x00000000, 0x00004441, 0x00004441, 0x00004441, 0x00004441, 0x00004442, 0x00003333, 0x00000000, 0x00000000},
    /* West frame 2 */
    {0x00000000, 0x00000000, 0x00000000, 0x11120000, 0x11110000, 0x21110000, 0x12110000, 0x11210000, 0x00000000, 0x00000000, 0x00000000, 0x00004441, 0x00004442, 0x00004441, 0x00004441, 0x00004441, 0x11120000, 0x11110000, 0x21110000, 0x12110000, 0x11210000, 0x30000000, 0x00000000, 0x00000000, 0x00004441, 0x00004442, 0x00004441, 0x00004441, 0x00004441, 0x00003333, 0x00000000, 0x00000000},
    /* West frame 3 */
    {0x00000000, 0x00000000, 0x00000000, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x00000000, 0x00000000, 0x00000000, 0x00004441, 0x00004441, 0x00004441, 0x00004442, 0x00004441, 0x12110000, 0x11210000, 0x11120000, 0x11110000, 0x21110000, 0x00000000, 0x00000000, 0x00000000, 0x00004441, 0x00004441, 0x00004441, 0x00004442, 0x00004441, 0x00003333, 0x00000000, 0x00000000},
    /* East frame 0 */
    {0x00000000, 0x00000000, 0x00000000, 0x14440000, 0x14440000, 0x24440000, 0x14440000, 0x14440000, 0x00000000, 0x00000000, 0x00000000, 0x00001121, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x14440000, 0x14440000, 0x24440000, 0x14440000, 0x14440000, 0x33300000, 0x00000000, 0x00000000, 0x00001121, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x00003333, 0x00000000, 0x00000000},
    /* East frame 1 */
    {0x00000000, 0x00000000, 0x00000000, 0x14440000, 0x14440000, 0x14440000, 0x14440000, 0x24440000, 0x00000000, 0x00000000, 0x00000000, 0x00002111, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x14440000, 0x14440000, 0x14440000, 0x14440000, 0x24440000, 0x33000000, 0x00000000, 0x00000000, 0x00002111, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x00003333, 0x00000000, 0x00000000},
    /* East frame 2 */
    {0x00000000, 0x00000000, 0x00000000, 0x14440000, 0x24440000, 0x14440000, 0x14440000, 0x14440000, 0x00000000, 0x00000000, 0x00000000, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x00001121, 0x14440000, 0x24440000, 0x14440000, 0x14440000, 0x14440000, 0x30000000, 0x00000000, 0x00000000, 0x00001112, 0x00001111, 0x00002111, 0x00001211, 0x00001121, 0x00003333, 0x00000000, 0x00000000},
    /* East frame 3 */
    {0x00000000, 0x00000000, 0x00000000, 0x14440000, 0x14440000, 0x14440000, 0x24440000, 0x14440000, 0x00000000, 0x00000000, 0x00000000, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x00002111, 0x14440000, 0x14440000, 0x14440000, 0x24440000, 0x14440000, 0x00000000, 0x00000000, 0x00000000, 0x00001211, 0x00001121, 0x00001112, 0x00001111, 0x00002111, 0x00003333, 0x00000000, 0x00000000},
};

static const struct SpriteFrameImage sFollowerPilotImages[] = {
    { (const u8 *)sFollowerPilotPixels[0], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[1], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[2], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[3], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[4], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[5], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[6], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[7], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[8], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[9], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[10], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[11], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[12], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[13], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[14], 16 * 16 / 2 },
    { (const u8 *)sFollowerPilotPixels[15], 16 * 16 / 2 },
};

static const union AnimCmd sFollowerPilotFaceSouth[] = { ANIMCMD_FRAME(0, 16), ANIMCMD_JUMP(0) };
static const union AnimCmd sFollowerPilotWalkSouth[] = {
    ANIMCMD_FRAME(0, 4),
    ANIMCMD_FRAME(1, 4),
    ANIMCMD_FRAME(2, 4),
    ANIMCMD_FRAME(3, 4),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastSouth[] = {
    ANIMCMD_FRAME(0, 2),
    ANIMCMD_FRAME(1, 2),
    ANIMCMD_FRAME(2, 2),
    ANIMCMD_FRAME(3, 2),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFasterSouth[] = {
    ANIMCMD_FRAME(0, 1),
    ANIMCMD_FRAME(1, 1),
    ANIMCMD_FRAME(2, 1),
    ANIMCMD_FRAME(3, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastestSouth[] = {
    ANIMCMD_FRAME(0, 1),
    ANIMCMD_FRAME(1, 1),
    ANIMCMD_FRAME(2, 1),
    ANIMCMD_FRAME(3, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFaceNorth[] = { ANIMCMD_FRAME(4, 16), ANIMCMD_JUMP(0) };
static const union AnimCmd sFollowerPilotWalkNorth[] = {
    ANIMCMD_FRAME(4, 4),
    ANIMCMD_FRAME(5, 4),
    ANIMCMD_FRAME(6, 4),
    ANIMCMD_FRAME(7, 4),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastNorth[] = {
    ANIMCMD_FRAME(4, 2),
    ANIMCMD_FRAME(5, 2),
    ANIMCMD_FRAME(6, 2),
    ANIMCMD_FRAME(7, 2),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFasterNorth[] = {
    ANIMCMD_FRAME(4, 1),
    ANIMCMD_FRAME(5, 1),
    ANIMCMD_FRAME(6, 1),
    ANIMCMD_FRAME(7, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastestNorth[] = {
    ANIMCMD_FRAME(4, 1),
    ANIMCMD_FRAME(5, 1),
    ANIMCMD_FRAME(6, 1),
    ANIMCMD_FRAME(7, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFaceWest[] = { ANIMCMD_FRAME(8, 16), ANIMCMD_JUMP(0) };
static const union AnimCmd sFollowerPilotWalkWest[] = {
    ANIMCMD_FRAME(8, 4),
    ANIMCMD_FRAME(9, 4),
    ANIMCMD_FRAME(10, 4),
    ANIMCMD_FRAME(11, 4),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastWest[] = {
    ANIMCMD_FRAME(8, 2),
    ANIMCMD_FRAME(9, 2),
    ANIMCMD_FRAME(10, 2),
    ANIMCMD_FRAME(11, 2),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFasterWest[] = {
    ANIMCMD_FRAME(8, 1),
    ANIMCMD_FRAME(9, 1),
    ANIMCMD_FRAME(10, 1),
    ANIMCMD_FRAME(11, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastestWest[] = {
    ANIMCMD_FRAME(8, 1),
    ANIMCMD_FRAME(9, 1),
    ANIMCMD_FRAME(10, 1),
    ANIMCMD_FRAME(11, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFaceEast[] = { ANIMCMD_FRAME(12, 16), ANIMCMD_JUMP(0) };
static const union AnimCmd sFollowerPilotWalkEast[] = {
    ANIMCMD_FRAME(12, 4),
    ANIMCMD_FRAME(13, 4),
    ANIMCMD_FRAME(14, 4),
    ANIMCMD_FRAME(15, 4),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastEast[] = {
    ANIMCMD_FRAME(12, 2),
    ANIMCMD_FRAME(13, 2),
    ANIMCMD_FRAME(14, 2),
    ANIMCMD_FRAME(15, 2),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFasterEast[] = {
    ANIMCMD_FRAME(12, 1),
    ANIMCMD_FRAME(13, 1),
    ANIMCMD_FRAME(14, 1),
    ANIMCMD_FRAME(15, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd sFollowerPilotFastestEast[] = {
    ANIMCMD_FRAME(12, 1),
    ANIMCMD_FRAME(13, 1),
    ANIMCMD_FRAME(14, 1),
    ANIMCMD_FRAME(15, 1),
    ANIMCMD_JUMP(0),
};
static const union AnimCmd *const sFollowerPilotAnims[] = {
    [ANIM_STD_FACE_SOUTH] = sFollowerPilotFaceSouth,
    [ANIM_STD_FACE_NORTH] = sFollowerPilotFaceNorth,
    [ANIM_STD_FACE_WEST] = sFollowerPilotFaceWest,
    [ANIM_STD_FACE_EAST] = sFollowerPilotFaceEast,
    [ANIM_STD_GO_SOUTH] = sFollowerPilotWalkSouth,
    [ANIM_STD_GO_NORTH] = sFollowerPilotWalkNorth,
    [ANIM_STD_GO_WEST] = sFollowerPilotWalkWest,
    [ANIM_STD_GO_EAST] = sFollowerPilotWalkEast,
    [ANIM_STD_GO_FAST_SOUTH] = sFollowerPilotFastSouth,
    [ANIM_STD_GO_FAST_NORTH] = sFollowerPilotFastNorth,
    [ANIM_STD_GO_FAST_WEST] = sFollowerPilotFastWest,
    [ANIM_STD_GO_FAST_EAST] = sFollowerPilotFastEast,
    [ANIM_STD_GO_FASTER_SOUTH] = sFollowerPilotFasterSouth,
    [ANIM_STD_GO_FASTER_NORTH] = sFollowerPilotFasterNorth,
    [ANIM_STD_GO_FASTER_WEST] = sFollowerPilotFasterWest,
    [ANIM_STD_GO_FASTER_EAST] = sFollowerPilotFasterEast,
    [ANIM_STD_GO_FASTEST_SOUTH] = sFollowerPilotFastestSouth,
    [ANIM_STD_GO_FASTEST_NORTH] = sFollowerPilotFastestNorth,
    [ANIM_STD_GO_FASTEST_WEST] = sFollowerPilotFastestWest,
    [ANIM_STD_GO_FASTEST_EAST] = sFollowerPilotFastestEast,
    [ANIM_RAISE_HAND] = sFollowerPilotFaceSouth,
};

// Diagnostic-only palette data. Slot is allocated dynamically among the 4
// nonreserved OBJ palette slots; normal NPC palette slots are never patched.
#define FOLLOWER_PILOT_PALETTE_TAG 0xF0A0
static const u16 sFollowerPilotNormalPalette[16] = {
    0, 0x7FFF, 0x4210, 0x03E0, 0x001F, 0x7C00, 0x56B5, 0x294A,
    0, 0, 0, 0, 0, 0, 0, 0
};
static const u16 sFollowerPilotShinyPalette[16] = {
    0, 0x7FFF, 0x4210, 0x7C1F, 0x7FE0, 0x03FF, 0x56B5, 0x294A,
    0, 0, 0, 0, 0, 0, 0, 0
};
static const struct ObjectEventGraphicsInfo sFollowerPilotNormalGraphics = {
    .tileTag = TAG_NONE,
    .paletteTag = TAG_NONE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 16 * 16 / 2,
    .width = 16,
    .height = 16,
    .paletteSlot = PALSLOT_NPC_1,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .disableReflectionPaletteLoad = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x16,
    .subspriteTables = gObjectEventSpriteOamTables_16x16,
    .anims = sFollowerPilotAnims,
    .images = sFollowerPilotImages,
    .affineAnims = gDummySpriteAffineAnimTable,
};

static const struct ObjectEventGraphicsInfo sFollowerPilotShinyGraphics = {
    .tileTag = TAG_NONE,
    .paletteTag = TAG_NONE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 16 * 16 / 2,
    .width = 16,
    .height = 16,
    .paletteSlot = PALSLOT_NPC_2,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .disableReflectionPaletteLoad = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_16x16,
    .subspriteTables = gObjectEventSpriteOamTables_16x16,
    .anims = sFollowerPilotAnims,
    .images = sFollowerPilotImages,
    .affineAnims = gDummySpriteAffineAnimTable,
};


// Size-aware synthetic follower pilots. The only nontransparent pixels are
// small diagnostic tile markers; these are NOT Pokemon artwork. Each frame
// occupies only one size-matched OBJ tile allocation at runtime.
static const u32 sFollowerPilot32Pixels[16][128] = {
    { [40] = 0x11111111, [44] = 0x11111111 }, // direction 0, step 0
    { [40] = 0x22222222, [44] = 0x11111111 }, // direction 0, step 1
    { [40] = 0x33333333, [44] = 0x11111111 }, // direction 0, step 2
    { [40] = 0x44444444, [44] = 0x11111111 }, // direction 0, step 3
    { [40] = 0x11111111, [44] = 0x22222222 }, // direction 1, step 0
    { [40] = 0x22222222, [44] = 0x22222222 }, // direction 1, step 1
    { [40] = 0x33333333, [44] = 0x22222222 }, // direction 1, step 2
    { [40] = 0x44444444, [44] = 0x22222222 }, // direction 1, step 3
    { [40] = 0x11111111, [44] = 0x33333333 }, // direction 2, step 0
    { [40] = 0x22222222, [44] = 0x33333333 }, // direction 2, step 1
    { [40] = 0x33333333, [44] = 0x33333333 }, // direction 2, step 2
    { [40] = 0x44444444, [44] = 0x33333333 }, // direction 2, step 3
    { [40] = 0x11111111, [44] = 0x44444444 }, // direction 3, step 0
    { [40] = 0x22222222, [44] = 0x44444444 }, // direction 3, step 1
    { [40] = 0x33333333, [44] = 0x44444444 }, // direction 3, step 2
    { [40] = 0x44444444, [44] = 0x44444444 }, // direction 3, step 3
};
static const struct SpriteFrameImage sFollowerPilot32Images[] = {
    { (const u8 *)sFollowerPilot32Pixels[0], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[1], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[2], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[3], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[4], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[5], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[6], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[7], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[8], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[9], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[10], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[11], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[12], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[13], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[14], 32 * 32 / 2 },
    { (const u8 *)sFollowerPilot32Pixels[15], 32 * 32 / 2 },
};
static const struct ObjectEventGraphicsInfo sFollowerPilot32NormalGraphics = {
    .tileTag = TAG_NONE,
    .paletteTag = TAG_NONE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 32 * 32 / 2,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_NPC_1,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .disableReflectionPaletteLoad = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = gObjectEventSpriteOamTables_32x32,
    .anims = sFollowerPilotAnims,
    .images = sFollowerPilot32Images,
    .affineAnims = gDummySpriteAffineAnimTable,
};
static const struct ObjectEventGraphicsInfo sFollowerPilot32ShinyGraphics = {
    .tileTag = TAG_NONE,
    .paletteTag = TAG_NONE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 32 * 32 / 2,
    .width = 32,
    .height = 32,
    .paletteSlot = PALSLOT_NPC_2,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .disableReflectionPaletteLoad = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_32x32,
    .subspriteTables = gObjectEventSpriteOamTables_32x32,
    .anims = sFollowerPilotAnims,
    .images = sFollowerPilot32Images,
    .affineAnims = gDummySpriteAffineAnimTable,
};
static const u32 sFollowerPilot64Pixels[16][512] = {
    { [216] = 0x11111111, [220] = 0x11111111 }, // direction 0, step 0
    { [216] = 0x22222222, [220] = 0x11111111 }, // direction 0, step 1
    { [216] = 0x33333333, [220] = 0x11111111 }, // direction 0, step 2
    { [216] = 0x44444444, [220] = 0x11111111 }, // direction 0, step 3
    { [216] = 0x11111111, [220] = 0x22222222 }, // direction 1, step 0
    { [216] = 0x22222222, [220] = 0x22222222 }, // direction 1, step 1
    { [216] = 0x33333333, [220] = 0x22222222 }, // direction 1, step 2
    { [216] = 0x44444444, [220] = 0x22222222 }, // direction 1, step 3
    { [216] = 0x11111111, [220] = 0x33333333 }, // direction 2, step 0
    { [216] = 0x22222222, [220] = 0x33333333 }, // direction 2, step 1
    { [216] = 0x33333333, [220] = 0x33333333 }, // direction 2, step 2
    { [216] = 0x44444444, [220] = 0x33333333 }, // direction 2, step 3
    { [216] = 0x11111111, [220] = 0x44444444 }, // direction 3, step 0
    { [216] = 0x22222222, [220] = 0x44444444 }, // direction 3, step 1
    { [216] = 0x33333333, [220] = 0x44444444 }, // direction 3, step 2
    { [216] = 0x44444444, [220] = 0x44444444 }, // direction 3, step 3
};
static const struct SpriteFrameImage sFollowerPilot64Images[] = {
    { (const u8 *)sFollowerPilot64Pixels[0], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[1], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[2], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[3], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[4], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[5], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[6], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[7], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[8], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[9], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[10], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[11], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[12], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[13], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[14], 64 * 64 / 2 },
    { (const u8 *)sFollowerPilot64Pixels[15], 64 * 64 / 2 },
};
static const struct ObjectEventGraphicsInfo sFollowerPilot64NormalGraphics = {
    .tileTag = TAG_NONE,
    .paletteTag = TAG_NONE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 64 * 64 / 2,
    .width = 64,
    .height = 64,
    .paletteSlot = PALSLOT_NPC_1,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .disableReflectionPaletteLoad = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_64x64,
    .subspriteTables = gObjectEventSpriteOamTables_64x64,
    .anims = sFollowerPilotAnims,
    .images = sFollowerPilot64Images,
    .affineAnims = gDummySpriteAffineAnimTable,
};
static const struct ObjectEventGraphicsInfo sFollowerPilot64ShinyGraphics = {
    .tileTag = TAG_NONE,
    .paletteTag = TAG_NONE,
    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
    .size = 64 * 64 / 2,
    .width = 64,
    .height = 64,
    .paletteSlot = PALSLOT_NPC_2,
    .shadowSize = SHADOW_SIZE_M,
    .inanimate = FALSE,
    .disableReflectionPaletteLoad = FALSE,
    .tracks = TRACKS_FOOT,
    .oam = &gObjectEventBaseOam_64x64,
    .subspriteTables = gObjectEventSpriteOamTables_64x64,
    .anims = sFollowerPilotAnims,
    .images = sFollowerPilot64Images,
    .affineAnims = gDummySpriteAffineAnimTable,
};

/* B10 species-keyed animated graphics contract. The 386 entries are deliberately
 * empty until audited/cleared art is installed. This static lookup does not
 * modify ObjectEvent.graphicsId, Pokemon, saves or link serialization.
 * A later import microblock populates entries with 16 SpriteFrameImages and
 * species-specific normal/shiny palettes. No diagnostic art is considered final.
 */
#define FOLLOWER_GRAPHICS_SPECIES_COUNT 386
static const struct ObjectEventGraphicsInfo *const
sFollowerRegisteredGraphics[FOLLOWER_GRAPHICS_SPECIES_COUNT + 1][2] = {
    { NULL, NULL }, /* species 0 is invalid */
};

static const struct ObjectEventGraphicsInfo *GetFollowerRegisteredGraphicsInfo(u16 species, bool8 shiny)
{
    if (species == SPECIES_NONE || species > FOLLOWER_GRAPHICS_SPECIES_COUNT)
        return NULL;
    return sFollowerRegisteredGraphics[species][shiny ? 1 : 0];
}
