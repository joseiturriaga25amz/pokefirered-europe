# RC Requirement Reconciliation — 154 implementation requirements

**Branch:** `feature/full-gameplay-core`  
**Authority:** frozen v1.0 spec/matrix + A-001..A-004 + current implementation.  

This table is the Gate 1 disposition ledger. “Runtime evidence required” is intentionally not a PASS claim: the implementation exists, but final acceptance remains in MyBoy. Superseded rows are preserved historically and must not be restored.

| ID | Area | Requirement | Classification | Evidence / remaining gate |
|---|---|---|---|---|
| BASE-001 | Base técnica | Base española oficial | **implemented + automated evidence** | Exact branch build + compile/static invariant checks. |
| BASE-002 | Base técnica | Upstream técnico | **implemented + automated evidence** | Exact branch build + compile/static invariant checks. |
| BASE-003 | Base técnica | Build moderno español | **implemented + automated evidence** | Exact branch build + compile/static invariant checks. |
| BASE-004 | Base técnica | Baseline reproducible | **implemented + automated evidence** | Exact branch build + compile/static invariant checks. |
| BASE-005 | Base técnica | Gobernanza Git | **implemented + automated evidence** | Exact branch build + compile/static invariant checks. |
| BASE-006 | Base técnica | Correcciones upstream posteriores | **implemented + automated evidence** | Exact branch build + compile/static invariant checks. |
| BTL-001 | Combate | Split físico/especial por movimiento | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-002 | Combate | Poder Oculto | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-003 | Combate | Contacto moderno | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-004 | Combate | Híbrido de generaciones | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-005 | Combate | Interacciones del split | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-006 | Combate | IA split-aware | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-007 | Combate | No IA competitiva nueva | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-008 | Combate | Naturalezas de entrenadores | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| BTL-009 | Combate | Sin EV ocultos enemigos | **implemented + runtime evidence required** | CI locks engine/data hooks; Gate 10 MyBoy proves battle behavior. |
| MOV-001 | Movimientos | Arbok aprende Colmillo Veneno | **implemented + automated evidence** | CI move/category data + validate_full_trainer_sets.py. |
| MOV-002 | Movimientos | Banette: Puño Sombra | **implemented + automated evidence** | CI move/category data + validate_full_trainer_sets.py. |
| MOV-003 | Movimientos | Shedinja: Puño Sombra | **implemented + automated evidence** | CI move/category data + validate_full_trainer_sets.py. |
| MOV-004 | Movimientos | No rebalance masivo de learnsets | **implemented + automated evidence** | CI move/category data + validate_full_trainer_sets.py. |
| MOV-005 | Movimientos | Categorías especiales fijadas | **implemented + automated evidence** | CI move/category data + validate_full_trainer_sets.py. |
| MOV-006 | Movimientos | Validador de sets | **implemented + automated evidence** | CI move/category data + validate_full_trainer_sets.py. |
| EVO-001 | Evoluciones | Kadabra → Alakazam | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-002 | Evoluciones | Machoke → Machamp | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-003 | Evoluciones | Graveler → Golem | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-004 | Evoluciones | Haunter → Gengar | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-005 | Evoluciones | Scyther + Revest. Metálico → Scizor | **implemented + runtime evidence required** | Evolution table/item UI path locked; actual direct-item evolution must be exercised in MyBoy. |
| EVO-006 | Evoluciones | Onix + Revest. Metálico → Steelix | **implemented + runtime evidence required** | Evolution table/item UI path locked; actual direct-item evolution must be exercised in MyBoy. |
| EVO-007 | Evoluciones | Seadra + Escama Dragón → Kingdra | **implemented + runtime evidence required** | Evolution table/item UI path locked; actual direct-item evolution must be exercised in MyBoy. |
| EVO-008 | Evoluciones | Porygon + Mejora → Porygon2 | **implemented + runtime evidence required** | Evolution table/item UI path locked; actual direct-item evolution must be exercised in MyBoy. |
| EVO-009 | Evoluciones | Poliwhirl + Roca del Rey → Politoed | **implemented + runtime evidence required** | Evolution table/item UI path locked; actual direct-item evolution must be exercised in MyBoy. |
| EVO-010 | Evoluciones | Slowpoke + Roca del Rey → Slowking | **implemented + runtime evidence required** | Evolution table/item UI path locked; actual direct-item evolution must be exercised in MyBoy. |
| EVO-011 | Evoluciones | Espeon | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-012 | Evoluciones | Umbreon | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-013 | Evoluciones | Evoluciones Gen II/III antes de Nacional | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| EVO-014 | Evoluciones | Ceremonia de Oak intacta | **implemented + automated evidence** | validate_rc_freeze.py + evolution table assertions. |
| QOL-001 | QoL | MT reutilizables | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-002 | QoL | MO sistema original | **superseded by amendment** | A-008/QOL-HM-002 replaces the vanilla learned-HM requirement with HM-item + badge/story field licenses and makes learned HM moves normally forgettable. |
| QOL-003 | QoL | Recordador de movimientos | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-004 | QoL | Tutores repetibles | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-005 | QoL | Tutores definitivos de iniciales | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-006 | QoL | Correr interiores | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-007 | QoL | Cadena de repelentes | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-008 | QoL | Bolsa ampliada | **superseded by amendment** | A-002: normal Items pocket remains vanilla 42 slots. |
| QOL-009 | QoL | EV visibles | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-010 | QoL | Sincronía fuera de combate | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-011 | QoL | Safari sin pasos | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-012 | QoL | Safari mantiene minijuego | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-013 | QoL | MT44 respaldo | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| QOL-014 | QoL | PP Up comercial | **implemented + runtime evidence required** | Static implementation evidence exists; interaction/behavior remains final MyBoy evidence. |
| ENC-001 | Encuentros | Base FireRed + exclusivas LG | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-002 | Encuentros | Sandshrew disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-003 | Encuentros | Vulpix disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-004 | Encuentros | Bellsprout disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-005 | Encuentros | Slowpoke disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-006 | Encuentros | Staryu disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-007 | Encuentros | Magmar disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-008 | Encuentros | Marill disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-009 | Encuentros | Sneasel disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-010 | Encuentros | Misdreavus disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-011 | Encuentros | Remoraid disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-012 | Encuentros | Mantine disponible | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-013 | Encuentros | Iniciales salvajes: Bulbasaur/Ivysaur/Venusaur | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-014 | Encuentros | Iniciales salvajes: Charmander/Charmeleon/Charizard | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-015 | Encuentros | Iniciales salvajes: Squirtle/Wartortle/Blastoise | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-016 | Encuentros | Eevee salvaje | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-017 | Encuentros | Vaporeon salvaje | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-018 | Encuentros | Jolteon salvaje | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-019 | Encuentros | Flareon salvaje | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-020 | Encuentros | Safari raros | **implemented + automated evidence** | CI encounter-rate/table assertions + validate_rc_freeze.py where applicable. |
| ENC-021 | Encuentros | Changing Cave restaurada | **implemented + runtime evidence required** | Nine tables/selector statically locked; MyBoy must prove selection persistence/table switching. |
| ENC-022 | Encuentros | Bebés por crianza | **implemented + automated evidence** | tools/validate_full_obtainability.py proves parents, Ditto, incense and gift/trade prerequisites. |
| EVT-001 | Eventos | Segundo fósil | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-002 | Eventos | Laboratorio admite ambos fósiles | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-003 | Eventos | Segundo Dojo | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-004 | Eventos | Premio segundo Dojo | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-005 | Eventos | Articuno/Zapdos/Moltres/Mewtwo respawn | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-006 | Eventos | Lugia/Ho-Oh/Deoxys respawn | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-007 | Eventos | Bestias errantes secuenciales | **A-005 redesign pending** | Old sequential implementation exists, but A-005 supersedes its introduction/UX; validate only after V2 cinematic + Suicune→Raikou→Entei flow is implemented. |
| EVT-008 | Eventos | Roamer persistente | **implemented core + A-005 UX pending** | Vanilla single-roamer persistence remains the compatibility core; V2 route reliability/combat-window polish still requires implementation and runtime evidence. |
| EVT-009 | Eventos | Pokédex del roamer | **A-005 redesign pending** | Final acceptance must cover the initial all-three-seen cinematic plus tracking of only the currently active roamer. |
| EVT-010 | Eventos | MysticTicket quest | **A-005 redesign pending** | Celio distribution is obsolete; final truth is the maritime/birds-seen investigation leading to Lugia while Ho-Oh remains separately gated. |
| EVT-011 | Eventos | AuroraTicket quest | **A-005 redesign pending** | Celio handoff is obsolete; final truth is the Pewter Museum / space-anomaly investigation and scientist handoff. |
| EVT-012 | Eventos | Deoxys | **encounter implemented; A-005 access redesign pending** | Birth Island encounter/respawn core exists; final acceptance waits for the new AuroraTicket ownership path. |
| EVT-013 | Eventos | Mew | **functional core runtime-proven; A-005 presentation pending** | Old RC proved capture flow; final acceptance requires preserved diary history plus visible overworld/interactable final Mew staging. |
| EVT-014 | Eventos | Mew moveset | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-015 | Eventos | Celebi | **A-005 redesign pending** | Berry Forest identity remains, but all-three-beasts causal gating is obsolete; final acceptance waits for the independent nature investigation. |
| EVT-016 | Eventos | Celebi moveset | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-017 | Eventos | Navel Rock | **destination core implemented; A-005 access split pending** | MysticTicket destination/IDs remain compatible; final acceptance must distinguish Lugia access from Ho-Oh beast-capstone gating. |
| EVT-018 | Eventos | Leyenda niveles | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| EVT-019 | Eventos | Hoenn legendarios excluidos | **implemented + runtime evidence required** | Scripts/state inspected; Gate 6 + final MyBoy checklist must execute terminal branches. |
| ECO-001 | Economía | Potenciadores de tipo en Azulona | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| ECO-002 | Economía | Tienda objetos equipados | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| ECO-003 | Economía | Objetos evolución renovables post-Nacional | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| ECO-004 | Economía | Tienda de bayas | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| ECO-005 | Economía | Consumibles PP postgame | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| ECO-006 | Economía | Porygon | **superseded by amendment** | A-008/ECO-CASINO-001 changes the repeatable prize from 5,000 to 5,500 coins and requires localized aligned presentation. |
| ECO-007 | Economía | Huevo Suerte | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| ECO-008 | Economía | Circuito Resort Gorgeous | **implemented + runtime evidence required** | Trainer classes/payout identity locked; VS Seeker repeatability remains runtime. |
| ECO-009 | Economía | Sin boost global de dinero | **implemented + automated evidence** | validate_rc_freeze.py locks prices/stock/renewable data. |
| BOSS-001 | Jefes | Curva líderes primera vuelta | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-002 | Jefes | Revanchas líderes | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-003 | Jefes | Curva IV líderes | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-004 | Jefes | Curva IV Liga | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-005 | Jefes | IV postgame | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-006 | Jefes | Curación primera vuelta | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-007 | Jefes | Curación rematches/Liga | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-008 | Jefes | Objetos equipados moderados | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-009 | Jefes | 7 correcciones de legalidad | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-010 | Jefes | Liga primera vuelta | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| BOSS-011 | Jefes | Liga revancha | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-001 | Gary | Inicial fijo | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-002 | Gary | Híbrido anime + FireRed | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-003 | Gary | Gary — Laboratorio | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-004 | Gary | Gary — Ruta 22 I | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-005 | Gary | Gary — Celeste | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-006 | Gary | Gary — S.S. Anne | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-007 | Gary | Gary — Torre Pokémon | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-008 | Gary | Gary — Silph S.A. | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-009 | Gary | Gary — Ruta 22 II | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-010 | Gary | Gary — Campeón | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-011 | Gary | Gary — Revancha | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-012 | Gary | Movesets tempranos legalizados | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| RIV-013 | Gary | IV progresivos | **implemented + runtime evidence required** | Frozen roster validator protects data; MyBoy verifies live fight/rematch/AI behavior. |
| SAVE-001 | Guardado | No cambiar tamaño SaveBlock1 | **implemented + automated evidence** | compile/static layout assertions + validate_rc_freeze.py. |
| SAVE-002 | Guardado | Extensión bolsa | **superseded by amendment** | A-002: normal Items pocket remains vanilla 42 slots. |
| SAVE-003 | Guardado | Header Full | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-004 | Guardado | Inicialización/migración | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-005 | Guardado | Namespace flags Full | **implemented + automated evidence** | compile/static layout assertions + validate_rc_freeze.py. |
| SAVE-006 | Guardado | Namespace vars Full | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-007 | Guardado | Flags KO aves/Mewtwo | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-008 | Guardado | Mew/Celebi state | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-009 | Guardado | Dojo choice state | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-010 | Guardado | Quest vars | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-011 | Guardado | Roamer save | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-012 | Guardado | Tickets evento existentes | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| SAVE-013 | Guardado | No auto-ticket por Hall of Fame | **implemented + runtime evidence required** | Static layout/state evidence exists; MyBoy save/load/import/persistence required. |
| BUG-001 | Bugs | Roamer IV setter | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-002 | Bugs | Roamer Roar | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-003 | Bugs | Roamer status size | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-004 | Bugs | Pokédex fishing OOB | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-005 | Bugs | Trade Egg check | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-006 | Bugs | HP recalculation | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-007 | Bugs | Move Reminder scroll indicator | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-008 | Bugs | L=A key repeat | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-009 | Bugs | Party menu memory leak | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-010 | Bugs | Berry Crush sparkle | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-011 | Bugs | UBFIX general | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| BUG-012 | Bugs | LOCALID_RUBY Mt Ember | **implemented + runtime evidence required** | Repair present/static checks where applicable; Gate 13 reproduces/falsifies historical bug class. |
| COMP-001 | Compatibilidad | Sin IDs nuevos de Pokémon/moves/items | **implemented + automated evidence** | compile/static ID/struct assertions + validate_rc_freeze.py. |
| COMP-002 | Compatibilidad | Estructura Pokémon intacta | **implemented + runtime evidence required** | Static Gen III layout/guard evidence exists; MyBoy link/trade acceptance required. |
| COMP-003 | Compatibilidad | Trading Gen III | **implemented + runtime evidence required** | Static Gen III layout/guard evidence exists; MyBoy link/trade acceptance required. |
| COMP-004 | Compatibilidad | Trade pre-Nacional | **implemented + runtime evidence required** | Static Gen III layout/guard evidence exists; MyBoy link/trade acceptance required. |
| COMP-005 | Compatibilidad | Save vanilla no es contrato bidireccional | **implemented + runtime evidence required** | Static Gen III layout/guard evidence exists; MyBoy link/trade acceptance required. |
| COMP-006 | Compatibilidad | mGBA como prueba principal | **superseded by amendment** | A-001: MyBoy replaces mandatory mGBA acceptance. |

## Counts

- **implemented + automated evidence: 52**
- **implemented + runtime evidence required: 99**
- **superseded by amendment: 3**

Total classified: **154/154**.

## Gate 1 interpretation

- Historical bag-expansion rows resolve only through A-002; no 142-slot implementation is accepted.
- Historical mGBA acceptance wording resolves only through A-001; MyBoy is authoritative for runtime.
- Runtime-classified rows remain open for final functional evidence even when their source/data is already guarded by CI.
- Cross-cutting RC blockers discovered outside an individual matrix row (for example build reproducibility) remain tracked in `RC_AUDIT_LOG.md` and can still prevent RC freeze.
