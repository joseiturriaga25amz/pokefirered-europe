#ifndef GUARD_WILD_POKEMON_AREA_H
#define GUARD_WILD_POKEMON_AREA_H

#define DEX_ENCOUNTER_LAND  (1 << 0)
#define DEX_ENCOUNTER_SURF  (1 << 1)
#define DEX_ENCOUNTER_ROCK  (1 << 2)
#define DEX_ENCOUNTER_FISH  (1 << 3)

struct PokedexEncounterSummary
{
    u8 methods;
    u8 minLevel;
    u8 maxLevel;
};

s32 GetSpeciesPokedexAreaMarkers(u16 species, struct Subsprite * subsprites);
bool8 GetPokedexEncounterSummary(u16 species, struct PokedexEncounterSummary *summary);

#endif //GUARD_WILD_POKEMON_AREA_H
