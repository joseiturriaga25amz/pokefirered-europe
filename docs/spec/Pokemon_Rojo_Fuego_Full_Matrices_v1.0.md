<PARSED TEXT FOR SHEET: 1 / 8 TABS
TAB NAME: Resumen>
index,Pokémon Rojo Fuego Full — Matriz Maestra de Preproducción v1.0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
0,,,,,,,,
1,Freeze,2026-09-19,Estado,PREPRODUCCIÓN CONGELADA,Producción,NO INICIADA,Build objetivo,firered_es_modern
2,,,,,,,,
3,KPIs del freeze,,,Riesgo de implementación,,,Prioridad QA,
4,Requisitos de implementación,154,,Alto,24,,Crítica,58
5,Casos QA,139,,Medio,62,,Alta,52
6,Decisiones cerradas,61,,Bajo,68,,Media,29
7,Slots de jefes/Liga/Gary,131,,,,,,
8,Slots historia de Gary,27,,,,,,
9,,,,,,,,
10,Requisitos por área,,,,,,,
11,Área,Requisitos,% del total,,,,,
12,Base técnica,6,0.03896103896103896,,,,,
13,Bugs,12,0.07792207792207792,,,,,
14,Combate,9,0.05844155844155844,,,,,
15,Compatibilidad,6,0.03896103896103896,,,,,
16,Economía,9,0.05844155844155844,,,,,
17,Encuentros,22,0.14285714285714285,,,,,
18,Eventos,19,0.12337662337662338,,,,,
19,Evoluciones,14,0.09090909090909091,,,,,
20,Gary,13,0.08441558441558442,,,,,
21,Guardado,13,0.08441558441558442,,,,,
22,Jefes,11,0.07142857142857142,,,,,
23,Movimientos,6,0.03896103896103896,,,,,
24,QoL,14,0.09090909090909091,,,,,
25,,,,,,,,
26,,,,,,,,
27,,,,,,,,
28,,,,,,,,
29,,,,,,,,
30,,,,,,,,
31,Regla de uso,,,,,,,
32,"Este workbook es la fuente operativa de producción. Una fila CERRADA define el resultado esperado; no autoriza reinterpretar requisitos. Un bloque solo puede marcarse COMPLETADO después de compilar, pasar smoke test, ejecutar los QA vinculados y actualizar el Decision Log cuando corresponda.",,,,,,,
<PARSED TEXT FOR SHEET: 2 / 8 TABS
TAB NAME: Implementacion>
index,ID,Área,Requisito,Vanilla,Cambio Full,Riesgo,Dependencias,Archivos probables,Criterio de aceptación,Notas,Estado,Referencia técnica
0,BASE-001,Base técnica,Base española oficial,Base inglesa habitual en pret.,"Usar pokefirered-europe como base de producción, fijada inicialmente en e184c5c…; no traducir desde inglés.",Alto,,Repositorio completo,Build español reproduce baseline antes de cambios.,,CERRADO / POR IMPLEMENTAR,https://github.com/CompuMaxx/pokefirered-europe
1,BASE-002,Base técnica,Upstream técnico,Sin upstream adicional.,Usar pret/pokefirered como referencia para correcciones y auditorías; portar selectivamente cambios relevantes.,Medio,Base española,Múltiples,Cada cherry-pick/port se documenta y prueba; no perseguir master automáticamente.,,CERRADO / POR IMPLEMENTAR,https://github.com/pret/pokefirered
2,BASE-003,Base técnica,Build moderno español,Build retail/reproducible.,Producción sobre firered_es_modern con BUGFIX + UBFIX activados por config.,Alto,Toolchain,"Makefile, include/config.h",Compila ROM funcional española y smoke test pasa.,,CERRADO / POR IMPLEMENTAR,
3,BASE-004,Base técnica,Baseline reproducible,,"Antes de modificar, ejecutar compare_firered_es y verificar SHA-1 documentada.",Alto,Toolchain,Makefile/*.sha1,SHA-1 = ab8f6bfe0ccdaf41188cd015c8c74c314d02296a,,CERRADO / POR IMPLEMENTAR,
4,BASE-005,Base técnica,Gobernanza Git,,main siempre integrado/probado; cambios por ramas feature/*; tag baseline-spanish-vanilla antes de Full.,Bajo,Repositorio,Git,Cada merge tiene build + prueba específica + registro.,,CERRADO / POR IMPLEMENTAR,
5,BASE-006,Base técnica,Correcciones upstream posteriores,Base europea mayo 2026.,"Portar al menos return UB, latin_small/gbagfx y LOCALID_RUBY de Mt. Ember, tras diff técnico.",Medio,Upstream,Archivos afectados por commits,Correcciones presentes sin regresiones españolas.,,CERRADO / POR IMPLEMENTAR,
6,BTL-001,Combate,Split físico/especial por movimiento,Categoría por tipo.,"Añadir categoría por movimiento: físico/especial/estado. Potencia, precisión, PP y efectos siguen Gen III.",Alto,"Datos de movimientos, IA, UI","include/pokemon.h, src/data/battle_moves.h, src/pokemon.c, battle_*",Daño usa Atq/Def o At. Esp./Def. Esp. según move.category; tests de casos frontera.,,CERRADO / POR IMPLEMENTAR,
7,BTL-002,Combate,Poder Oculto,Categoría dependiente de tipo.,Siempre especial aunque cambie de tipo.,Alto,Split,battle engine,Todos los tipos generados usan At. Esp./Def. Esp.,,CERRADO / POR IMPLEMENTAR,
8,BTL-003,Combate,Contacto moderno,Flags Gen III.,"Asignar propiedades de contacto modernas a movimientos Gen I–III, independiente de categoría.",Medio,Battle moves,src/data/battle_moves.h,Static/Poison Point/Effect Spore/Rough Skin responden solo a contacto real.,,CERRADO / POR IMPLEMENTAR,
9,BTL-004,Combate,Híbrido de generaciones,Todo Gen III.,Categoría y contacto modernos; resto de datos del movimiento Gen III.,Medio,Split,src/data/battle_moves.h,No se importan buffs/efectos Gen IV+ accidentalmente.,,CERRADO / POR IMPLEMENTAR,
10,BTL-005,Combate,Interacciones del split,Basados en tipo.,"Actualizar quemadura, Reflejo, Pantalla Luz, Contador, Manto Espejo, Hustle, último daño y cálculos relacionados.",Alto,Split,"src/pokemon.c, battle_script_commands.c, battle_util.c",Cada interacción se prueba con movimiento que cambió de categoría.,,CERRADO / POR IMPLEMENTAR,
11,BTL-006,Combate,IA split-aware,IA asume físico/especial por tipo.,Mantener núcleo AI_CHECK_BAD_MOVE + TRY_TO_FAINT + CHECK_VIABILITY y corregir cálculos para categoría por movimiento.,Alto,Split,"data/battle_ai_scripts.s, battle_ai_*",IA elige y evalúa daño coherentemente; sin lectura de equipo ni counter-picking.,,CERRADO / POR IMPLEMENTAR,
12,BTL-007,Combate,No IA competitiva nueva,Flags extra prácticamente no usados.,"No activar flags dormidos de IA por defecto; dificultad por niveles, sets, IV, objetos y curación.",Bajo,IA,src/data/trainers.h,Jefes no exhiben conductas erráticas de scripts no validados.,,CERRADO / POR IMPLEMENTAR,
13,BTL-008,Combate,Naturalezas de entrenadores,Deterministas por PID derivado.,No optimizar naturalezas competitivamente; conservar determinismo/semántica original.,Bajo,Trainer party creation,src/battle_main.c,No se fuerzan naturalezas perfectas por rol.,,CERRADO / POR IMPLEMENTAR,
14,BTL-009,Combate,Sin EV ocultos enemigos,0 EV en party creada.,Entrenadores normales siguen sin EV entrenados artificiales.,Bajo,,src/battle_main.c,Inspección de party enemiga confirma EV 0 salvo sistemas ajenos.,,CERRADO / POR IMPLEMENTAR,
15,MOV-001,Movimientos,Arbok aprende Colmillo Veneno,No disponible por nivel.,Añadir Colmillo Veneno por nivel para compensar split sin rehacer learnset completo.,Bajo,Split,level_up_learnsets.h,Arbok puede aprenderlo por nivel/reminder.,,CERRADO / POR IMPLEMENTAR,
16,MOV-002,Movimientos,Banette: Puño Sombra,Bola Sombra por nivel.,"En el nivel donde vanilla aprende Bola Sombra, enseñar Puño Sombra; MT30 sigue disponible.",Bajo,Split,level_up_learnsets.h,Banette obtiene STAB físico razonable.,,CERRADO / POR IMPLEMENTAR,
17,MOV-003,Movimientos,Shedinja: Puño Sombra,Bola Sombra por nivel.,Mismo criterio que Banette; MT30 permanece.,Bajo,Split,level_up_learnsets.h,Shedinja obtiene STAB físico.,,CERRADO / POR IMPLEMENTAR,
18,MOV-004,Movimientos,No rebalance masivo de learnsets,Learnsets Gen III.,Flareon/Houndoom/Muk/Sceptile y otros no reciben parches arbitrarios.,Bajo,,pokemon data,Diff limitado a cambios aprobados.,,CERRADO / POR IMPLEMENTAR,
19,MOV-005,Movimientos,Categorías especiales fijadas,Por tipo.,Cascada físico; Triturar físico; Bola Sombra especial; Bomba Lodo especial; Hoja Aguda físico; puños elementales físicos; Meteorobola especial; Premonición/Deseo Oculto especial.,Alto,Split,battle_moves.h,Tabla de categorías coincide con mapeo aprobado.,,CERRADO / POR IMPLEMENTAR,
20,MOV-006,Movimientos,Validador de sets,No existe.,Crear script de validación especie/nivel/move legal/objeto/ID para todos los jefes.,Medio,Datos de entrenadores,tools/ o scripts/,CI/local reporta 0 incompatibilidades no exceptuadas.,,CERRADO / POR IMPLEMENTAR,
21,EVO-001,Evoluciones,Kadabra → Alakazam,Intercambio,Nivel 36,Bajo,,src/data/pokemon/evolution.h,Kadabra evoluciona al 36 sin trade.,,CERRADO / POR IMPLEMENTAR,
22,EVO-002,Evoluciones,Machoke → Machamp,Intercambio,Nivel 36,Bajo,,src/data/pokemon/evolution.h,Machoke evoluciona al 36 sin trade.,,CERRADO / POR IMPLEMENTAR,
23,EVO-003,Evoluciones,Graveler → Golem,Intercambio,Nivel 36,Bajo,,src/data/pokemon/evolution.h,Graveler evoluciona al 36 sin trade.,,CERRADO / POR IMPLEMENTAR,
24,EVO-004,Evoluciones,Haunter → Gengar,Intercambio,Nivel 36,Bajo,,src/data/pokemon/evolution.h,Haunter evoluciona al 36 sin trade.,,CERRADO / POR IMPLEMENTAR,
25,EVO-005,Evoluciones,Scyther + Revest. Metálico → Scizor,Intercambio sosteniendo objeto,Usar el objeto directamente sobre el Pokémon.,Medio,Sistema de objetos/evolución,"evolution.h, party/item use",Evolución ocurre con uso directo y consume 1 objeto.,,CERRADO / POR IMPLEMENTAR,
26,EVO-006,Evoluciones,Onix + Revest. Metálico → Steelix,Intercambio sosteniendo objeto,Usar el objeto directamente sobre el Pokémon.,Medio,Sistema de objetos/evolución,"evolution.h, party/item use",Evolución ocurre con uso directo y consume 1 objeto.,,CERRADO / POR IMPLEMENTAR,
27,EVO-007,Evoluciones,Seadra + Escama Dragón → Kingdra,Intercambio sosteniendo objeto,Usar el objeto directamente sobre el Pokémon.,Medio,Sistema de objetos/evolución,"evolution.h, party/item use",Evolución ocurre con uso directo y consume 1 objeto.,,CERRADO / POR IMPLEMENTAR,
28,EVO-008,Evoluciones,Porygon + Mejora → Porygon2,Intercambio sosteniendo objeto,Usar el objeto directamente sobre el Pokémon.,Medio,Sistema de objetos/evolución,"evolution.h, party/item use",Evolución ocurre con uso directo y consume 1 objeto.,,CERRADO / POR IMPLEMENTAR,
29,EVO-009,Evoluciones,Poliwhirl + Roca del Rey → Politoed,Intercambio sosteniendo objeto,Usar el objeto directamente sobre el Pokémon.,Medio,Sistema de objetos/evolución,"evolution.h, party/item use",Evolución ocurre con uso directo y consume 1 objeto.,,CERRADO / POR IMPLEMENTAR,
30,EVO-010,Evoluciones,Slowpoke + Roca del Rey → Slowking,Intercambio sosteniendo objeto,Usar el objeto directamente sobre el Pokémon.,Medio,Sistema de objetos/evolución,"evolution.h, party/item use",Evolución ocurre con uso directo y consume 1 objeto.,,CERRADO / POR IMPLEMENTAR,
31,EVO-011,Evoluciones,Espeon,Amistad + día,Piedra Solar sobre Eevee.,Medio,Eevee,evolution.h,Eevee evoluciona a Espeon con Piedra Solar.,,CERRADO / POR IMPLEMENTAR,
32,EVO-012,Evoluciones,Umbreon,Amistad + noche,Piedra Lunar sobre Eevee.,Medio,Eevee,evolution.h,Eevee evoluciona a Umbreon con Piedra Lunar.,,CERRADO / POR IMPLEMENTAR,
33,EVO-013,Evoluciones,Evoluciones Gen II/III antes de Nacional,Varias rutas bloquean target > Mew.,Eliminar bloqueos de evolución pre-National sin mostrar aún Dex Nacional.,Alto,Pokédex/save,"evolution_scene.c, party_menu.c, pokemon.c",Golbat→Crobat y evoluciones aprobadas funcionan; datos Seen/Caught persisten.,,CERRADO / POR IMPLEMENTAR,
34,EVO-014,Evoluciones,Ceremonia de Oak intacta,Ceremonia original.,La Pokédex visible sigue Kanto hasta la ceremonia original post-Liga; luego revela Nacional.,Alto,Pre-Nat evolutions,pokedex/event scripts,Antes de ceremonia UI Kanto; después entradas Nacionales ya capturadas aparecen.,,CERRADO / POR IMPLEMENTAR,
35,QOL-001,QoL,MT reutilizables,Consumibles y vendibles.,Enseñar una MT no la consume; cantidad máxima 1; no vender ni tirar.,Medio,Bag/TM Case,"party_menu.c, tm_case.c, item/shop",Misma MT enseña a múltiples Pokémon y permanece.,,CERRADO / POR IMPLEMENTAR,
36,QOL-002,QoL,MO sistema original,Original.,Mantener exactamente el paradigma FireRed: Pokémon compatible debe conocer MO + medalla requerida.,Bajo,,party_menu/field moves,Corte/Surf/Vuelo/etc. se usan como vanilla.,,CERRADO / POR IMPLEMENTAR,
37,QOL-003,QoL,Recordador de movimientos,Tiny/Big Mushroom.,"$2.000 por movimiento, sin Setas Grande/Pequeña.",Bajo,Economía,move relearner scripts,Cobra exactamente $2.000 y funciona reiteradamente.,,CERRADO / POR IMPLEMENTAR,
38,QOL-004,QoL,Tutores repetibles,Una vez.,Primera enseñanza gratis; repeticiones pagadas con tabla aprobada.,Medio,Economía,tutor scripts,"Tras primer uso, tutor sigue disponible y cobra precio correcto.",,CERRADO / POR IMPLEMENTAR,
39,QOL-005,QoL,Tutores definitivos de iniciales,Restricciones vanilla/una vez.,"Venusaur/Charizard/Blastoise apropiado: primera gratis, repeticiones $10.000.",Bajo,Tutores,scripts,Planta Feroz/Anillo Ígneo/Hidrocañón según especie; repetición paga.,,CERRADO / POR IMPLEMENTAR,
40,QOL-006,QoL,Correr interiores,Restricción por mapa.,Zapatillas permiten correr también en interiores una vez obtenidas.,Bajo,,player movement,Puede correr en interiores sin alterar mapas prohibidos especiales.,,CERRADO / POR IMPLEMENTAR,
41,QOL-007,QoL,Cadena de repelentes,Solo mensaje de fin.,"Al agotarse, prompt inmediato para usar otro repelente disponible.",Medio,Bag,"wild_encounter.c, scripts",Prompt aparece y aplica repelente elegido sin abrir navegación manual.,,CERRADO / POR IMPLEMENTAR,
42,QOL-008,QoL,Bolsa ampliada,42 ItemSlot.,Bolsillo normal: 42 + 100 slots extra = 142 tipos; sin rediseño visual radical.,Alto,Guardado,"global.h, item.c/bag.c",Puede almacenar >42 tipos; 142 slots operan sin corrupción.,,CERRADO / POR IMPLEMENTAR,
43,QOL-009,QoL,EV visibles,Ocultos.,"Toggle en resumen (p.ej. R): EV por stat, total/510, barras y 252; boxed si es práctico.",Medio,UI,pokemon_summary_screen.c,Valores coinciden con MON_DATA_*_EV; no aparece en batalla.,,CERRADO / POR IMPLEMENTAR,
44,QOL-010,QoL,Sincronía fuera de combate,Sin efecto de campo FRLG.,"50% de probabilidad de naturaleza del líder de party para salvajes, estilo Emerald.",Medio,Wild creation,wild_encounter/pokemon,Muestra estadísticamente ~50% en prueba automatizada/semilla controlada.,,CERRADO / POR IMPLEMENTAR,
45,QOL-011,QoL,Safari sin pasos,600 pasos + 30 balls.,Eliminar contador de 600 pasos; termina solo al gastar 30 Safari Balls o salir.,Medio,Safari,"safari_zone.c, start_menu.c",Tras >600 pasos sigue activo; 30ª bola termina.,,CERRADO / POR IMPLEMENTAR,
46,QOL-012,QoL,Safari mantiene minijuego,Original.,"Conservar catch/flee, comida/piedra y 30 Safari Balls.",Bajo,Safari,battle safari,No se convierte en captura normal.,,CERRADO / POR IMPLEMENTAR,
47,QOL-013,QoL,MT44 respaldo,Fuente missable S.S. Anne.,MT44 Descanso sigue en S.S. Anne y además se vende en Azulona por $3.000.,Bajo,MT reusable/shop,Celadon shop,Save que perdió S.S. Anne puede comprarla.,,CERRADO / POR IMPLEMENTAR,
48,QOL-014,QoL,PP Up comercial,No estándar tienda.,PP Up $9.800; PP Max sigue raro/no comercial.,Bajo,Economía,marts/items,Precio correcto; PP Max no aparece en shop.,,CERRADO / POR IMPLEMENTAR,
49,ENC-001,Encuentros,Base FireRed + exclusivas LG,Version exclusives.,"No fusionar tablas completas: añadir familias faltantes en hábitats oficiales LG, conservando población FireRed.",Alto,Wild tables,src/data/wild_encounters.json,Todas familias LG aprobadas obtenibles y exclusivas FR siguen disponibles.,,CERRADO / POR IMPLEMENTAR,
50,ENC-002,Encuentros,Sandshrew disponible,Ausente o exclusiva LG,Ruta 8; tasa objetivo 20%.,Bajo,Integración LG,wild_encounters.json,Sandshrew aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
51,ENC-003,Encuentros,Vulpix disponible,Ausente o exclusiva LG,Ruta 8; tasa objetivo 20%.,Bajo,Integración LG,wild_encounters.json,Vulpix aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
52,ENC-004,Encuentros,Bellsprout disponible,Ausente o exclusiva LG,Ruta 5; tasa objetivo 25%.,Bajo,Integración LG,wild_encounters.json,Bellsprout aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
53,ENC-005,Encuentros,Slowpoke disponible,Ausente o exclusiva LG,zona acuática oficial LG (p.ej. Ruta 6); tasa objetivo 100% Surf en esa tabla.,Bajo,Integración LG,wild_encounters.json,Slowpoke aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
54,ENC-006,Encuentros,Staryu disponible,Ausente o exclusiva LG,Ciudad Carmín; tasa objetivo 40% Supercaña.,Bajo,Integración LG,wild_encounters.json,Staryu aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
55,ENC-007,Encuentros,Magmar disponible,Ausente o exclusiva LG,Monte Ascuas; tasa objetivo 5%.,Bajo,Integración LG,wild_encounters.json,Magmar aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
56,ENC-008,Encuentros,Marill disponible,Ausente o exclusiva LG,Valle Ruinas; tasa objetivo 10%.,Bajo,Integración LG,wild_encounters.json,Marill aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
57,ENC-009,Encuentros,Sneasel disponible,Ausente o exclusiva LG,Cueva Glaciada; tasa objetivo 5%.,Bajo,Integración LG,wild_encounters.json,Sneasel aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
58,ENC-010,Encuentros,Misdreavus disponible,Ausente o exclusiva LG,"Cueva Perdida, habitaciones seleccionadas; tasa objetivo 5%.",Bajo,Integración LG,wild_encounters.json,Misdreavus aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
59,ENC-011,Encuentros,Remoraid disponible,Ausente o exclusiva LG,Laberinto Acuático / Isla 5; tasa objetivo 40% Supercaña.,Bajo,Integración LG,wild_encounters.json,Remoraid aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
60,ENC-012,Encuentros,Mantine disponible,Ausente o exclusiva LG,aguas de Isla 7; tasa objetivo 5% Surf.,Bajo,Integración LG,wild_encounters.json,Mantine aparece con tasa definida sin borrar familia FR.,,CERRADO / POR IMPLEMENTAR,
61,ENC-013,Encuentros,Iniciales salvajes: Bulbasaur/Ivysaur/Venusaur,No salvajes.,Bosque Baya: 15% / 5% / 4%; niveles >= evolución natural para formas evolucionadas.,Medio,Slots,wild_encounters.json,Tasas por slots exactas y niveles coherentes.,,CERRADO / POR IMPLEMENTAR,
62,ENC-014,Encuentros,Iniciales salvajes: Charmander/Charmeleon/Charizard,No salvajes.,Monte Ascuas: 15% / 5% / 4%; niveles >= evolución natural para formas evolucionadas.,Medio,Slots,wild_encounters.json,Tasas por slots exactas y niveles coherentes.,,CERRADO / POR IMPLEMENTAR,
63,ENC-015,Encuentros,Iniciales salvajes: Squirtle/Wartortle/Blastoise,No salvajes.,Islas Espuma: 15% / 5% / 4%; niveles >= evolución natural para formas evolucionadas.,Medio,Slots,wild_encounters.json,Tasas por slots exactas y niveles coherentes.,,CERRADO / POR IMPLEMENTAR,
64,ENC-016,Encuentros,Eevee salvaje,Regalo único.,Ruta 7: 15%.,Bajo,,wild_encounters.json,Eevee aparece ~15%.,,CERRADO / POR IMPLEMENTAR,
65,ENC-017,Encuentros,Vaporeon salvaje,No salvaje.,"Islas Espuma: 4%, ~Nv.35.",Bajo,,wild_encounters.json,Vaporeon aparece ~4%.,,CERRADO / POR IMPLEMENTAR,
66,ENC-018,Encuentros,Jolteon salvaje,No salvaje.,"Central de Energía: 4%, ~Nv.35.",Bajo,,wild_encounters.json,Jolteon aparece ~4%.,,CERRADO / POR IMPLEMENTAR,
67,ENC-019,Encuentros,Flareon salvaje,No salvaje.,"Mansión Pokémon: 4%, ~Nv.35.",Bajo,,wild_encounters.json,Flareon aparece ~4%.,,CERRADO / POR IMPLEMENTAR,
68,ENC-020,Encuentros,Safari raros,Tasas muy bajas.,En la mejor zona individual: Chansey/Kangaskhan/Tauros/Scyther/Pinsir mínimo 15%; otras zonas pueden ser menores.,Medio,Safari,wild_encounters.json,Cada especie tiene al menos una tabla con 15%.,,CERRADO / POR IMPLEMENTAR,
69,ENC-021,Encuentros,Changing Cave restaurada,Tablas ocultas de Mystery Event.,Investigador selecciona avistamiento: Zubat normal o Mareep/Pineco/Houndour/Teddiursa/Aipom/Shuckle/Stantler/Smeargle; usa tablas originales y niveles originales.,Bajo,VAR_ALTERING_CAVE_WILD_SET,scripts + wild encounter,Cambiar selección cambia tabla completa; persiste.,,CERRADO / POR IMPLEMENTAR,
70,ENC-022,Encuentros,Bebés por crianza,Dependencias de versión/eventos.,No añadir bebés artificialmente; Elekid/Magby/Smoochum/Tyrogue/Azurill/Wynaut/etc. derivan de padres/objetos accesibles.,Bajo,Disponibilidad,daycare,Cada bebé relevante es obtenible en un solo save.,,CERRADO / POR IMPLEMENTAR,
71,EVT-001,Eventos,Segundo fósil,Uno de dos para siempre.,"Tras revivir el fósil elegido, punto de excavación en Mt. Moon entrega el fósil no elegido una vez.",Medio,Fossil flags/lab,"MtMoon_B2F scripts, Cinnabar lab",El otro fósil se obtiene solo después de revivir primero; no es repetible.,,CERRADO / POR IMPLEMENTAR,
72,EVT-002,Eventos,Laboratorio admite ambos fósiles,Asume nunca poseer ambos.,Corregir lógica 'todos revividos' para exigir Helix + Domo + Ámbar correctamente.,Medio,Segundo fósil,lab scripts,Puede revivir ambos fósiles Mt Moon y Ámbar sin bloqueo.,,CERRADO / POR IMPLEMENTAR,
73,EVT-003,Eventos,Segundo Dojo,Solo primera pelea.,Después de Sabrina: Koichi Primeape43/Poliwrath44/Hitmonlee45/Hitmonchan45/Machamp47; Machamp ace.,Medio,Dojo flags/trainer,Saffron Dojo scripts/trainers,Batalla aparece tras Sabrina y solo se recompensa una vez.,,CERRADO / POR IMPLEMENTAR,
74,EVT-004,Eventos,Premio segundo Dojo,Elección única.,"Entrega el Hitmon no elegido a Nv.35; si no hay espacio, premio queda pendiente.",Medio,Registro de elección,Dojo scripts,Obtiene exactamente el otro Hitmon y nunca se pierde por storage full.,,CERRADO / POR IMPLEMENTAR,
75,EVT-005,Eventos,Articuno/Zapdos/Moltres/Mewtwo respawn,KO suele eliminar permanentemente.,Captura = permanente; huida = vuelve al reentrar; KO = reaparece tras siguiente Hall of Fame con reroll total.,Alto,Flags/HOF,"legend scripts, hall_of_fame.inc",Tres resultados se comportan distinto según especificación.,,CERRADO / POR IMPLEMENTAR,
76,EVT-006,Eventos,Lugia/Ho-Oh/Deoxys respawn,Mecánica similar pero tickets evento.,Reusar flags FLEW_AWAY como KO pendiente y FOUGHT como capturado; HOF ya limpia FLEW_AWAY.,Medio,HOF,Navel/Birth scripts,Captura no reaparece; KO sí tras HOF; huida reentrada.,,CERRADO / POR IMPLEMENTAR,
77,EVT-007,Eventos,Bestias errantes secuenciales,Una bestia según inicial.,"Tras Liga + Rocket Sevii derrotado + Zafiro entregado: Suicune50 → Raikou50 → Entei50, una activa.",Alto,Roamer save + quest state,"roamer.c, scripts",Captura activa siguiente; al final estado completo.,,CERRADO / POR IMPLEMENTAR,
78,EVT-008,Eventos,Roamer persistente,Roar puede borrar; KO desactiva.,"Huida conserva PID/IV/shiny/HP/status; Rugido solo huye; KO reactiva tras cambio de ruta, curada, misma PID/IV/shiny.",Alto,Bugfix roamer,"roamer.c, battle_main.c",Casos de escape/Roar/KO probados.,,CERRADO / POR IMPLEMENTAR,
79,EVT-009,Eventos,Pokédex del roamer,Comportamiento vanilla limitado.,Antes del primer encuentro área desconocida; tras visto muestra ruta actual exacta.,Medio,Roamer,pokedex area/roamer,Ruta se actualiza al moverse.,,CERRADO / POR IMPLEMENTAR,
80,EVT-010,Eventos,MysticTicket quest,Distribución evento.,Network Machine restaurada + Articuno/Zapdos/Moltres capturados; volver con Celio → MysticTicket/Navel Rock.,Medio,Bird capture flags,"OneIsland PC, ferry",No se entrega por HOF; solo requisitos + quest.,,CERRADO / POR IMPLEMENTAR,
81,EVT-011,Eventos,AuroraTicket quest,Distribución evento.,Network Machine restaurada → Celio detecta señal → Museo Pewter → volver a Celio → AuroraTicket/Birth Island.,Medio,Quest state,Celio/Pewter/ferry,Secuencia no saltable y no repetible.,,CERRADO / POR IMPLEMENTAR,
82,EVT-012,Eventos,Deoxys,Nv.30 evento.,Birth Island/puzzle original; Attack Forme FireRed; Nv.50.,Bajo,AuroraTicket,Birth Island,Aparece Nv.50 y puzzle sigue intacto.,,CERRADO / POR IMPLEMENTAR,
83,EVT-013,Eventos,Mew,No disponible.,Requiere Mewtwo capturado; Mansion: grito + 3–4 apariciones hide-and-seek; combate final Nv.50 en sótano/journals; fateful encounter.,Alto,Mew quest flags,Pokemon Mansion scripts/map,"Secuencia completa, captura con fateful bit, respawn KO según regla.",,CERRADO / POR IMPLEMENTAR,
84,EVT-014,Eventos,Mew moveset,,Destructor / Transformación / Megapuño / Metrónomo.,Bajo,Mew event,seteventmon/custom move set,Mew Nv.50 entra con set exacto.,,CERRADO / POR IMPLEMENTAR,
85,EVT-015,Eventos,Celebi,No disponible.,Nacional + Network Machine + tres bestias capturadas; árbol especial Berry Forest; Celebi Nv.50.,Alto,Roamer sequence,Berry Forest scripts/map,Evento solo aparece con requisitos completos.,,CERRADO / POR IMPLEMENTAR,
86,EVT-016,Eventos,Celebi moveset,,Psíquico / Poder Pasado / Recuperación / Campana Cura.,Bajo,Celebi event,event mon setup,Set exacto.,,CERRADO / POR IMPLEMENTAR,
87,EVT-017,Eventos,Navel Rock,Evento externo.,Lugia70 + Ho-Oh70; Ceniza Sagrada oculta original conservada.,Bajo,MysticTicket,Navel Rock,Ambos accesibles en mismo save; hidden Sacred Ash intacta.,,CERRADO / POR IMPLEMENTAR,
88,EVT-018,Eventos,Leyenda niveles,Mixto.,"50: aves, bestias, Mew, Celebi, Deoxys. 70: Mewtwo, Lugia, Ho-Oh.",Bajo,Eventos,scripts,Niveles exactos.,,CERRADO / POR IMPLEMENTAR,
89,EVT-019,Eventos,Hoenn legendarios excluidos,No disponibles FRLG.,Jirachi/Latios/Latias/Regis/Groudon/Kyogre/Rayquaza no se insertan en FireRed Full; reservados a Emerald Full.,Bajo,,,Ningún evento/encuentro nuevo los concede.,,CERRADO / POR IMPLEMENTAR,
90,ECO-001,Economía,Potenciadores de tipo en Azulona,Disponibilidad dispersa.,Vender los 16 potenciadores aprobados a $3.000; mantienen +10% Gen III.,Bajo,Items,Celadon mart,Todos disponibles $3.000 y efecto 10%.,"Arena Fina, Roca Dura, Semilla Milagro, Gafas de Sol, Cinturón Negro, Imán, Agua Mística, Pico Afilado, Flecha Veneno, Antiderretir, Hechizo, Cuchara Torcida, Carbón, Colmillo Dragón, Pañuelo Seda, Polvo Plata",CERRADO / POR IMPLEMENTAR,
91,ECO-002,Economía,Tienda objetos equipados,Fuentes limitadas.,"Añadir tabla de objetos especiales con precios aprobados; no vender Repartir Exp., Moneda Amuleto, Campana Alivio ni Brazal Firme.",Bajo,Items,mart scripts,Precios coinciden con especificación.,Garra Rápida $4000; Puño Suerte $4000; Palo $4000; Periscopio $5000; Cinta Focus $5000; Polvo Metálico $6000; Campana Concha $6000; Polvo Brillo $7500; Bola Luminosa $8000; Restos $12000; Hueso Grueso $12000; Cin. Elegida $15000,CERRADO / POR IMPLEMENTAR,
92,ECO-003,Economía,Objetos evolución renovables post-Nacional,Limitados.,Piedra Solar/Lunar $3.000; Roca del Rey/Revest. Metálico/Escama Dragón $5.000; Mejora $7.500.,Bajo,National Dex,postgame shop,Shop solo post-Nacional y precios exactos.,,CERRADO / POR IMPLEMENTAR,
93,ECO-004,Economía,Tienda de bayas,Disponibilidad limitada.,Aventura: estados/Oran/Leppa/Sitrus/Lum/pinch; post-Nacional: EV berries y Liechi/Ganlon/Salac/Petaya/Apicot/Lansat/Starf con precios aprobados.,Medio,National Dex,berry shop scripts,Inventario cambia según progreso; efectos Gen III/Emerald aprobados.,,CERRADO / POR IMPLEMENTAR,
94,ECO-005,Economía,Consumibles PP postgame,No comerciales.,Éter 1200 / Éter Máx 2000 / Elixir 3000 / Elixir Máx 4500 postgame.,Bajo,Postgame,mart,No aparecen antes del postgame.,,CERRADO / POR IMPLEMENTAR,
95,ECO-006,Economía,Porygon,9.999 fichas FR.,"Casino Azulona: 5.000 fichas, repetible.",Bajo,Game Corner,prize scripts,Puede comprar múltiples Porygon a 5000.,,CERRADO / POR IMPLEMENTAR,
96,ECO-007,Economía,Huevo Suerte,Solo Chansey raro.,Método Chansey original + compra postgame $30.000.,Bajo,Postgame,shop,Disponible postgame sin eliminar método original.,,CERRADO / POR IMPLEMENTAR,
97,ECO-008,Economía,Circuito Resort Gorgeous,Payouts vanilla.,Jacki/Gillian/Celina forman circuito VS Seeker ~30k antes de bonuses; Celina pasa a Lady y ~10k payout.,Medio,Trainer payouts/VS Seeker,trainers/maps,Una carga de VS Seeker puede incluir los tres cuando posición lo permite; probar in-game.,,CERRADO / POR IMPLEMENTAR,
98,ECO-009,Economía,Sin boost global de dinero,Vanilla.,No multiplicar dinero de todo el juego; ajustes localizados.,Bajo,,trainers,Payouts normales fuera de cambios aprobados.,,CERRADO / POR IMPLEMENTAR,
99,BOSS-001,Jefes,Curva líderes primera vuelta,Equipos vanilla.,"Equipos/niveles cerrados con anime/historia Gen III; dificultad moderada, ace +2 aprox.",Medio,Trainer data,trainer_parties.h,Roster exacto según hoja Jefes.,,CERRADO / POR IMPLEMENTAR,
100,BOSS-002,Jefes,Revanchas líderes,Rematches vanilla distintas/limitadas.,"Repetibles indefinidamente, roster histórico/anime hasta Gen III; niveles ~60–74.",Medio,Postgame,trainer scripts/data,Pueden repetirse; equipos según hoja Jefes.,,CERRADO / POR IMPLEMENTAR,
101,BOSS-003,Jefes,Curva IV líderes,Todos IV0.,"Brock6, Misty10, Surge12, Erika14, Koga16, Sabrina17, Blaine18, Giovanni20.",Medio,Trainer iv field,trainer_parties.h,IV reales equivalen a targets ±0; sin EV.,,CERRADO / POR IMPLEMENTAR,
102,BOSS-004,Jefes,Curva IV Liga,"Liga ~30, Champion31.","Lorelei24, Bruno25, Agatha26, Lance27, Gary28; Blastoise Gary30.",Medio,Trainer iv field,trainer_parties.h,Progresión gradual y sin 31 universal.,,CERRADO / POR IMPLEMENTAR,
103,BOSS-005,Jefes,IV postgame,Varía vanilla.,"Líderes tempranos26; Koga–Giovanni28; Liga revancha29, ace30; Gary postgame29, Blastoise30.",Medio,,trainer_parties.h,Targets se reflejan en stats.,,CERRADO / POR IMPLEMENTAR,
104,BOSS-006,Jefes,Curación primera vuelta,Más/otros ítems.,Brock 1 Poción; Misty/Surge 1 Superpoción; Erika 2 Superpociones; Koga/Sabrina/Blaine/Giovanni 2 Hiperpociones máx según diseño.,Bajo,AI item use,trainers.h,Nunca supera máximos.,,CERRADO / POR IMPLEMENTAR,
105,BOSS-007,Jefes,Curación rematches/Liga,Champion vanilla 4 Full Restore.,Líderes tempranos máx 2 Hiperpociones; Koga–Giovanni máx 2 Restaurar Todo; Liga/Champion máx 2 Restaurar Todo.,Bajo,,trainers.h,Máximo 2 por combate.,,CERRADO / POR IMPLEMENTAR,
106,BOSS-008,Jefes,Objetos equipados moderados,Pocos/ninguno.,"Primera vuelta principalmente ace; rematches 3–5 items, max 1 Restos por equipo salvo justificación.",Bajo,Held items,trainer_parties.h,Hoja Jefes respeta límite.,,CERRADO / POR IMPLEMENTAR,
107,BOSS-009,Jefes,7 correcciones de legalidad,Propuestas previas ilegales.,Staryu: Pantalla Luz; Raichu: At. Rápido; Tangela: Polvo Veneno; Rhydon Giovanni: Demolición; Arbok Agatha: Deslumbrar; Dragonair Lance: Enfado x2.,Bajo,Validator,trainer_parties.h,Validador 0 errores no exceptuados.,,CERRADO / POR IMPLEMENTAR,
108,BOSS-010,Jefes,Liga primera vuelta,Vanilla más baja.,Lorelei 57–61; Bruno 58–62; Agatha 59–63; Lance 61–65; Gary Champion 64–69.,Medio,Gary,trainer_parties.h,Curva ascendente exacta.,,CERRADO / POR IMPLEMENTAR,
109,BOSS-011,Jefes,Liga revancha,Vanilla rematch distinta.,Lorelei74–79; Bruno75–80; Agatha76–81 (5 mons); Lance78–82 (5 mons); Gary80–85.,Medio,Postgame,trainer_parties.h,Equipos/moves/items exactos según hoja Jefes.,,CERRADO / POR IMPLEMENTAR,
110,RIV-001,Gary,Inicial fijo,Starter contraventaja al jugador.,"Gary siempre Squirtle → Wartortle → Blastoise, independiente del starter del jugador.",Medio,Rival script selection,trainers/scripts,Todas apariciones usan rama Squirtle.,,CERRADO / POR IMPLEMENTAR,
111,RIV-002,Gary,Híbrido anime + FireRed,Blue puro.,"Estructura de Blue FireRed + identidad/rotación de Gary anime; Blastoise eje, resto plantilla rotativa.",Bajo,,trainer data,Equipos exactos según hoja Gary.,,CERRADO / POR IMPLEMENTAR,
112,RIV-003,Gary,Gary — Laboratorio,Equipo rival vanilla variable por starter,Squirtle 5,Bajo,Gary fixed starter,trainer_parties.h,Combate Laboratorio coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
113,RIV-004,Gary,Gary — Ruta 22 I,Equipo rival vanilla variable por starter,Pidgey 10 / Squirtle 12,Bajo,Gary fixed starter,trainer_parties.h,Combate Ruta 22 I coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
114,RIV-005,Gary,Gary — Celeste,Equipo rival vanilla variable por starter,Abra 18 / Rattata 19 / Pidgeotto 20 / Squirtle 22,Bajo,Gary fixed starter,trainer_parties.h,Combate Celeste coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
115,RIV-006,Gary,Gary — S.S. Anne,Equipo rival vanilla variable por starter,Krabby 24 / Pidgeotto 25 / Kadabra 25 / Wartortle 28,Bajo,Gary fixed starter,trainer_parties.h,Combate S.S. Anne coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
116,RIV-007,Gary,Gary — Torre Pokémon,Equipo rival vanilla variable por starter,Exeggcute 30 / Pidgeotto 31 / Growlithe 31 / Kadabra 32 / Wartortle 34,Bajo,Gary fixed starter,trainer_parties.h,Combate Torre Pokémon coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
117,RIV-008,Gary,Gary — Silph S.A.,Equipo rival vanilla variable por starter,Exeggutor 43 / Pidgeot 44 / Growlithe 44 / Alakazam 46 / Blastoise 49,Bajo,Gary fixed starter,trainer_parties.h,Combate Silph S.A. coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
118,RIV-009,Gary,Gary — Ruta 22 II,Equipo rival vanilla variable por starter,Rhyhorn 56 / Pidgeot 56 / Nidoking 57 / Alakazam 58 / Arcanine 59 / Blastoise 61,Bajo,Gary fixed starter,trainer_parties.h,Combate Ruta 22 II coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
119,RIV-010,Gary,Gary — Campeón,Equipo rival vanilla variable por starter,Pidgeot 64 / Alakazam 65 / Nidoking 65 / Rhydon 66 / Arcanine 67 / Blastoise 69,Bajo,Gary fixed starter,trainer_parties.h,Combate Campeón coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
120,RIV-011,Gary,Gary — Revancha,Equipo rival vanilla variable por starter,Nidoqueen 80 / Magmar 80 / Golem 81 / Scizor 82 / Arcanine 83 / Blastoise 85,Bajo,Gary fixed starter,trainer_parties.h,Combate Revancha coincide con roster/niveles cerrados.,,CERRADO / POR IMPLEMENTAR,
121,RIV-012,Gary,Movesets tempranos legalizados,Sets vanilla variables.,Fijar sets legales y progresivos; Abra de Celeste usa MTs legales para no ser un turno vacío.,Medio,Validator,trainer_parties.h,Todos los moves del rival pasan validador FRLG/Full.,,CERRADO / POR IMPLEMENTAR,
122,RIV-013,Gary,IV progresivos,Muchos 0 y Champion31.,0 → 6 → 10 → 12 → 14 → 18 → 24 → 28; Blastoise Champion 30.,Medio,Trainer IV,trainer_parties.h,Stats reflejan progresión sin EV/nature minmax.,,CERRADO / POR IMPLEMENTAR,
123,SAVE-001,Guardado,No cambiar tamaño SaveBlock1,0x3D68.,Reutilizar zonas unused manteniendo size 0x3D68 y offsets estándar.,Alto,Compatibilidad,include/global.h,sizeof SaveBlock1 permanece 0x3D68.,,CERRADO / POR IMPLEMENTAR,
124,SAVE-002,Guardado,Extensión bolsa,400 bytes sin uso.,Reemplazar unused_348C[400] por 100 ItemSlot adicionales.,Alto,Bag,"global.h, item/bag",Exactamente 400 bytes; offsets posteriores idénticos.,,CERRADO / POR IMPLEMENTAR,
125,SAVE-003,Guardado,Header Full,16 bytes sin uso.,Usar unused_3D24[16] como header RFFL + schemaVersion + reservado; no tocar unused_3A94.,Medio,Migración,global.h/load save,Save nuevo contiene magic/version; offsets posteriores idénticos.,,CERRADO / POR IMPLEMENTAR,
126,SAVE-004,Guardado,Inicialización/migración,,"Si magic Full ausente, tratar save como schema 0: limpiar slots extra y escribir header, sin modificar campos vanilla.",Alto,Header Full,load_save,Vanilla compatible importado no interpreta basura como items.,,CERRADO / POR IMPLEMENTAR,
127,SAVE-005,Guardado,Namespace flags Full,Flags sin uso.,Reservar 0x8C3–0x8E2 (32 flags) para Full; usar inicialmente solo flags nombradas.,Medio,Events,flags.h,No colisiona con flags originales; bloque documentado.,,CERRADO / POR IMPLEMENTAR,
128,SAVE-006,Guardado,Namespace vars Full,Vars sin uso.,Reservar 0x408C–0x409B (16 vars) para estados Full.,Medio,Events,vars.h,No colisiona con map scenes/Quest Log.,,CERRADO / POR IMPLEMENTAR,
129,SAVE-007,Guardado,Flags KO aves/Mewtwo,FOUGHT mezcla KO/captura.,4 flags Full: KO pendiente Articuno/Zapdos/Moltres/Mewtwo; FOUGHT pasa a significar capturado.,Alto,Legend scripts/HOF,flags.h/scripts,HOF limpia solo KO; capturados siguen ausentes.,,CERRADO / POR IMPLEMENTAR,
130,SAVE-008,Guardado,Mew/Celebi state,No existe.,Cada uno: captured + KO pending; quest stage en var Full.,Medio,Custom events,flags.h/vars.h,Flee/KO/capture se distinguen y sobreviven save/load.,,CERRADO / POR IMPLEMENTAR,
131,SAVE-009,Guardado,Dojo choice state,No recuerda cuál se eligió.,FLAG_FULL_DOJO_CHOSE_HITMONLEE + FLAG_FULL_DOJO_SECOND_REWARD_RECEIVED; FLAG_GOT_HITMON vanilla indica que primera elección ocurrió.,Medio,Second dojo,flags.h/scripts,Segundo premio siempre es el opuesto.,,CERRADO / POR IMPLEMENTAR,
132,SAVE-010,Guardado,Quest vars,No existe.,Mystic/Aurora/Mew/Celebi + roamer sequence usan VAR_FULL_* dedicadas.,Medio,Events,vars.h/scripts,Estados no se pisan entre quests.,,CERRADO / POR IMPLEMENTAR,
133,SAVE-011,Guardado,Roamer save,Un struct Roamer.,Reusar struct Roamer único vanilla; no expandir save para 3 bestias porque solo una está activa.,Bajo,Roamer sequence,roamer.c,Secuencia completa cabe en estructura existente.,,CERRADO / POR IMPLEMENTAR,
134,SAVE-012,Guardado,Tickets evento existentes,IDs/event flags existentes.,Reusar ITEM_MYSTIC_TICKET/ITEM_AURORA_TICKET y flags ENABLE_SHIP/RECEIVED originales; no crear IDs.,Bajo,Quests,items/flags/scripts,Ferry reconoce tickets Full con lógica original.,,CERRADO / POR IMPLEMENTAR,
135,SAVE-013,Guardado,No auto-ticket por Hall of Fame,Solo rev10 auto-entrega.,Build firered_es_modern es REVISION=0 y bloque REVISION>=0xA no compila; añadir test para impedir regresión futura.,Bajo,Build config,post_battle_event_funcs.c,Tras HOF sin quests no hay tickets en bolsa ni flags.,,CERRADO / POR IMPLEMENTAR,
136,BUG-001,Bugs,Roamer IV setter,Bug/UB vanilla,Corregir MON_DATA_IVS para leer 4 bytes.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
137,BUG-002,Bugs,Roamer Roar,Bug/UB vanilla,Rugido no desactiva permanentemente al roamer.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
138,BUG-003,Bugs,Roamer status size,Bug/UB vanilla,Escribir status con tamaño correcto.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
139,BUG-004,Bugs,Pokédex fishing OOB,Bug/UB vanilla,Usar contador correcto de fishing slots.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
140,BUG-005,Bugs,Trade Egg check,Bug/UB vanilla,Corregir condición pre-Nacional.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
141,BUG-006,Bugs,HP recalculation,Bug/UB vanilla,Pokémon vivo nunca queda con HP<=0 tras recalcular max HP.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
142,BUG-007,Bugs,Move Reminder scroll indicator,Bug/UB vanilla,Corregir sprite ID del segundo indicador.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
143,BUG-008,Bugs,L=A key repeat,Bug/UB vanilla,Comparar entrada remapeada correctamente.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
144,BUG-009,Bugs,Party menu memory leak,Bug/UB vanilla,Liberar buffers de slots en ruta afectada.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
145,BUG-010,Bugs,Berry Crush sparkle,Bug/UB vanilla,Usar campo correcto para sparkleAmount.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
146,BUG-011,Bugs,UBFIX general,Bug/UB vanilla,Mantener UBFIX forced en modern y aceptar correcciones de seguridad.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
147,BUG-012,Bugs,LOCALID_RUBY Mt Ember,Bug/UB vanilla,Portar corrección upstream relevante al Rubí/Celio.,Medio,Build modern/upstream,varios,Caso de reproducción no vuelve a fallar.,,CERRADO / POR IMPLEMENTAR,
148,COMP-001,Compatibilidad,Sin IDs nuevos de Pokémon/moves/items,,Usar #001–386 y assets/IDs Gen III existentes; eventos reusan tickets/items originales.,Alto,Todo el diseño,constants/data,Trade no recibe IDs desconocidos por vanilla Gen III.,,CERRADO / POR IMPLEMENTAR,
149,COMP-002,Compatibilidad,Estructura Pokémon intacta,Vanilla.,No añadir campos a Pokemon/BoxPokemon ni cambiar PID/OT/EV/IV/moves/held item layout.,Alto,Split/UI,pokemon structs,sizeof/layout de Pokémon idéntico.,,CERRADO / POR IMPLEMENTAR,
150,COMP-003,Compatibilidad,Trading Gen III,Vanilla.,Objetivo oficial: Full ↔ Emerald Full ↔ vanilla Gen III donde protocolo FRLG lo permita.,Alto,"No new IDs, pre-Nat rules",trade/link,mGBA link test bidireccional pasa con mons representativos.,,CERRADO / POR IMPLEMENTAR,
151,COMP-004,Compatibilidad,Trade pre-Nacional,Restricción vanilla.,Mantener restricción vanilla para huevos/no-Kanto antes de Nacional.,Medio,Pre-Nat local evolutions,trade.c,Local Gen II/III puede existir; link pre-Nat sigue bloqueando casos vanilla.,,CERRADO / POR IMPLEMENTAR,
152,COMP-005,Compatibilidad,Save vanilla no es contrato bidireccional,,No garantizar ida/vuelta del mismo .sav entre Full y ROM vanilla; sí permitir inicialización segura de un save sin header cuando sea viable.,Bajo,Save extension,load/save,No se documenta round-trip como soportado.,,CERRADO / POR IMPLEMENTAR,
153,COMP-006,Compatibilidad,mGBA como prueba principal,,Pruebas funcionales y link con mGBA; hardware real opcional.,Bajo,Build,QA,Matriz QA incluye link/trade/save.,,CERRADO / POR IMPLEMENTAR,
<PARSED TEXT FOR SHEET: 3 / 8 TABS
TAB NAME: QA>
index,Test ID,Área,Caso,Precondiciones,Pasos,Resultado esperado,Prioridad,ID implementación,Estado
0,QA-001,Base técnica,Baseline español reproduce SHA-1,Checkout base sin cambios y toolchain listo,Ejecutar compare_firered_es.,SHA-1 coincide exactamente con baseline documentado.,Crítica,,PENDIENTE
1,QA-002,Base técnica,Build moderno español arranca,Build firered_es_modern limpio,Compilar; abrir ROM en mGBA; iniciar partida; guardar/cargar.,Sin crash; textos españoles; save funcional.,Crítica,,PENDIENTE
2,QA-003,Guardado,SaveBlock1 mantiene tamaño,Build Full compilado,Assert/compilación de sizeof(SaveBlock1); revisar offsets clave.,Tamaño 0x3D68 y offsets posteriores a extensiones no cambian.,Crítica,,PENDIENTE
3,QA-004,Guardado,Migración header ausente,Save vanilla español válido,Abrir save en Full; inspeccionar bolsa extra y header; guardar/reabrir.,Slots extra vacíos; header RFFL creado; progreso vanilla intacto.,Crítica,,PENDIENTE
4,QA-005,Guardado,Bolsa >42 tipos,Partida con acceso a objetos variados,Añadir 60+ tipos distintos al bolsillo normal; guardar/cargar.,Todos persisten y son utilizables.,Crítica,,PENDIENTE
5,QA-006,Guardado,Bolsa llena hasta 142,Herramienta/debug para inyectar items,Llenar 142 slots; intentar 143.º; guardar/cargar.,142 aceptados; 143.º rechazado de forma segura; checksum válido.,Alta,,PENDIENTE
6,QA-007,Guardado,Flags Full no colisionan,Build debug,Activar cada flag Full y recorrer eventos originales cercanos.,Ningún evento original cambia por flags Full.,Alta,,PENDIENTE
7,QA-008,Guardado,Vars Full no colisionan,Build debug,Asignar estados máximos de quests Full; visitar mapas con scene vars.,Scene vars originales intactos.,Alta,,PENDIENTE
8,QA-009,Combate,Bola Sombra especial,Pokémon de prueba con stats diferenciados,Ejecutar Bola Sombra contra objetivo controlado y comparar daño con fórmula.,Usa At. Esp. atacante y Def. Esp. objetivo.,Crítica,,PENDIENTE
9,QA-010,Combate,Triturar físico,Pokémon de prueba con stats diferenciados,Ejecutar Triturar contra objetivo controlado y comparar daño con fórmula.,Usa Ataque y Defensa.,Crítica,,PENDIENTE
10,QA-011,Combate,Cascada físico,Pokémon de prueba con stats diferenciados,Ejecutar Cascada contra objetivo controlado y comparar daño con fórmula.,Usa Ataque y Defensa.,Crítica,,PENDIENTE
11,QA-012,Combate,Puño Fuego físico,Pokémon de prueba con stats diferenciados,Ejecutar Puño Fuego contra objetivo controlado y comparar daño con fórmula.,Usa Ataque y Defensa.,Crítica,,PENDIENTE
12,QA-013,Combate,Bomba Lodo especial,Pokémon de prueba con stats diferenciados,Ejecutar Bomba Lodo contra objetivo controlado y comparar daño con fórmula.,Usa At. Esp. y Def. Esp.,Crítica,,PENDIENTE
13,QA-014,Combate,Hoja Aguda físico,Pokémon de prueba con stats diferenciados,Ejecutar Hoja Aguda contra objetivo controlado y comparar daño con fórmula.,Usa Ataque y Defensa.,Crítica,,PENDIENTE
14,QA-015,Combate,Poder Oculto especial,Pokémon de prueba con stats diferenciados,Ejecutar Poder Oculto de tipo físico clásico contra objetivo controlado y comparar daño con fórmula.,Siempre usa At. Esp./Def. Esp.,Crítica,,PENDIENTE
15,QA-016,Combate,Contacto independiente de categoría,Atacante con Terremoto y Puño Fuego; objetivo con Static/Poison Point,Golpear repetidamente con ambos.,Puño Fuego puede disparar contacto; Terremoto nunca.,Alta,,PENDIENTE
16,QA-017,Combate,Quemadura afecta físicos nuevos,Atacante quemado con Cascada y Surf,Comparar daño antes/después de quemadura.,Cascada se reduce; Surf no.,Alta,,PENDIENTE
17,QA-018,Combate,Reflejo/Pantalla Luz,Objetivo usa ambas pantallas,Recibir Bola Sombra y Triturar.,Reflejo reduce Triturar; Pantalla Luz reduce Bola Sombra.,Crítica,,PENDIENTE
18,QA-019,Combate,Contador/Manto Espejo,Objetivo conoce ambos,Recibir daño de Triturar y Bola Sombra por separado.,Contador responde a Triturar; Manto Espejo a Bola Sombra.,Crítica,,PENDIENTE
19,QA-020,Combate,IA entiende split,Jefe con opción física/especial y objetivo con defensas muy desiguales,Repetir combate con RNG controlado.,Scoring de IA refleja categoría real y no tipo antiguo.,Alta,,PENDIENTE
20,QA-021,Combate,No EV enemigos,Batalla debug contra líder y Champion,Inspeccionar MON_DATA_*_EV de party enemiga.,0 EV en todos los stats.,Alta,,PENDIENTE
21,QA-022,Combate,IV progresivos,Captura/inspección debug de party enemiga,Comparar stats con targets de IV por jefe.,IV reales coinciden con curva documentada.,Alta,,PENDIENTE
22,QA-023,Evoluciones,Kadabra → Alakazam,"Kadabra válido, sin Nacional cuando aplique",Subir a nivel 36.,Evoluciona a Alakazam; método anterior no es requerido.,Alta,,PENDIENTE
23,QA-024,Evoluciones,Machoke → Machamp,"Machoke válido, sin Nacional cuando aplique",Subir a nivel 36.,Evoluciona a Machamp; método anterior no es requerido.,Alta,,PENDIENTE
24,QA-025,Evoluciones,Graveler → Golem,"Graveler válido, sin Nacional cuando aplique",Subir a nivel 36.,Evoluciona a Golem; método anterior no es requerido.,Alta,,PENDIENTE
25,QA-026,Evoluciones,Haunter → Gengar,"Haunter válido, sin Nacional cuando aplique",Subir a nivel 36.,Evoluciona a Gengar; método anterior no es requerido.,Alta,,PENDIENTE
26,QA-027,Evoluciones,Scyther → Scizor,"Scyther válido, sin Nacional cuando aplique",Usar revest. metálico.,Evoluciona a Scizor; método anterior no es requerido.,Alta,,PENDIENTE
27,QA-028,Evoluciones,Onix → Steelix,"Onix válido, sin Nacional cuando aplique",Usar revest. metálico.,Evoluciona a Steelix; método anterior no es requerido.,Alta,,PENDIENTE
28,QA-029,Evoluciones,Seadra → Kingdra,"Seadra válido, sin Nacional cuando aplique",Usar escama dragón.,Evoluciona a Kingdra; método anterior no es requerido.,Alta,,PENDIENTE
29,QA-030,Evoluciones,Porygon → Porygon2,"Porygon válido, sin Nacional cuando aplique",Usar mejora.,Evoluciona a Porygon2; método anterior no es requerido.,Alta,,PENDIENTE
30,QA-031,Evoluciones,Poliwhirl → Politoed,"Poliwhirl válido, sin Nacional cuando aplique",Usar roca del rey.,Evoluciona a Politoed; método anterior no es requerido.,Alta,,PENDIENTE
31,QA-032,Evoluciones,Slowpoke → Slowking,"Slowpoke válido, sin Nacional cuando aplique",Usar roca del rey.,Evoluciona a Slowking; método anterior no es requerido.,Alta,,PENDIENTE
32,QA-033,Evoluciones,Eevee → Espeon,"Eevee válido, sin Nacional cuando aplique",Usar piedra solar.,Evoluciona a Espeon; método anterior no es requerido.,Alta,,PENDIENTE
33,QA-034,Evoluciones,Eevee → Umbreon,"Eevee válido, sin Nacional cuando aplique",Usar piedra lunar.,Evoluciona a Umbreon; método anterior no es requerido.,Alta,,PENDIENTE
34,QA-035,Evoluciones,Crobat pre-Nacional,Golbat con amistad suficiente antes de Liga,Subir nivel.,Evoluciona a Crobat; save registra especie aunque UI siga Kanto.,Crítica,,PENDIENTE
35,QA-036,Pokédex,UI pre-Nacional,Crobat capturado/evolucionado antes de ceremonia Oak,Abrir Pokédex antes y después de ceremonia.,Antes: Dex Kanto sin corrupción; después: Crobat aparece con Seen/Caught.,Crítica,,PENDIENTE
36,QA-037,Compatibilidad,Trade pre-Nacional no-Kanto bloqueado,Dos instancias link pre-Nacional,Intentar intercambiar Crobat/huevo.,Se mantiene restricción vanilla correspondiente.,Alta,,PENDIENTE
37,QA-038,QoL,MT reusable,Poseer MT24,Enseñar Rayo a dos Pokémon compatibles.,MT24 sigue en estuche tras ambas enseñanzas.,Crítica,,PENDIENTE
38,QA-039,QoL,MT máximo 1,Ya poseer MT24; tienda/casino ofrece MT24,Intentar comprar otra.,Compra bloqueada/mensaje 'ya la tienes'; no se cobra.,Alta,,PENDIENTE
39,QA-040,QoL,MT no vendible/descartable,Poseer una MT,Abrir opciones de venta y descarte.,No permite perder la MT.,Alta,,PENDIENTE
40,QA-041,QoL,MO original,MO03 + medalla pero ningún Pokémon conoce Surf,Intentar Surf.,No se puede; al enseñar Surf a Pokémon compatible sí funciona.,Crítica,,PENDIENTE
41,QA-042,QoL,Recordador $2000,Pokémon con move recordable y $2000+,Recordar movimiento.,Cobra exactamente $2000; no pide setas.,Alta,,PENDIENTE
42,QA-043,QoL,Tutor primera gratis/repeat paga,Tutor sin usar,Enseñar una vez; volver; enseñar otra vez.,Primera $0; segunda cobra precio de tabla.,Alta,,PENDIENTE
43,QA-044,QoL,Correr interior,Zapatillas obtenidas,Correr en Centro Pokémon/casa normal.,Se permite correr sin romper mapas/scripted movement.,Media,,PENDIENTE
44,QA-045,QoL,Repel chain sí,Repelente activo y otro disponible,Agotar pasos; elegir sí.,Nuevo repelente se aplica y contador reinicia.,Alta,,PENDIENTE
45,QA-046,QoL,Repel chain no,Repelente activo,Agotar pasos; elegir no.,No se aplica otro; control vuelve al jugador.,Media,,PENDIENTE
46,QA-047,QoL,Repel sin stock,Último repelente,Agotar pasos.,No ofrece opción inválida/loop.,Media,,PENDIENTE
47,QA-048,UI,EV summary,Pokémon con EV conocidos,Abrir resumen; alternar vista EV.,"Se ven seis EV, total, barras/252; valores exactos.",Alta,,PENDIENTE
48,QA-049,Encuentros,Synchronize 50%,Líder con Sincronía y naturaleza conocida,Generar muestra grande con RNG/seed controlada.,"≈50% de salvajes comparten naturaleza, dentro tolerancia estadística.",Media,,PENDIENTE
49,QA-050,Safari,Sin límite 600 pasos,Entrar Safari con 30 balls,Caminar >650 pasos sin lanzar todas las balls.,Safari continúa; no aparece Times Up por pasos.,Crítica,,PENDIENTE
50,QA-051,Safari,Fin por 30 balls,Entrar Safari,Consumir las 30 Safari Balls.,Expedición termina al quedar 0.,Crítica,,PENDIENTE
51,QA-052,Encuentros,Tasa Sandshrew,Ruta 8,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Sandshrew ocupa slots equivalentes a 20% y niveles definidos.,Media,,PENDIENTE
52,QA-053,Encuentros,Tasa Vulpix,Ruta 8,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Vulpix ocupa slots equivalentes a 20% y niveles definidos.,Media,,PENDIENTE
53,QA-054,Encuentros,Tasa Bellsprout,Ruta 5,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Bellsprout ocupa slots equivalentes a 25% y niveles definidos.,Media,,PENDIENTE
54,QA-055,Encuentros,Tasa Magmar,Monte Ascuas,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Magmar ocupa slots equivalentes a 5% y niveles definidos.,Media,,PENDIENTE
55,QA-056,Encuentros,Tasa Marill,Valle Ruinas,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Marill ocupa slots equivalentes a 10% y niveles definidos.,Media,,PENDIENTE
56,QA-057,Encuentros,Tasa Sneasel,Cueva Glaciada,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Sneasel ocupa slots equivalentes a 5% y niveles definidos.,Media,,PENDIENTE
57,QA-058,Encuentros,Tasa Misdreavus,Cueva Perdida,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Misdreavus ocupa slots equivalentes a 5% y niveles definidos.,Media,,PENDIENTE
58,QA-059,Encuentros,Tasa Mantine,Isla 7 Surf,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Mantine ocupa slots equivalentes a 5% y niveles definidos.,Media,,PENDIENTE
59,QA-060,Encuentros,Tasa Bulbasaur,Bosque Baya,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Bulbasaur ocupa slots equivalentes a 15% y niveles definidos.,Media,,PENDIENTE
60,QA-061,Encuentros,Tasa Ivysaur,Bosque Baya,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Ivysaur ocupa slots equivalentes a 5% y niveles definidos.,Media,,PENDIENTE
61,QA-062,Encuentros,Tasa Venusaur,Bosque Baya,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Venusaur ocupa slots equivalentes a 4% y niveles definidos.,Media,,PENDIENTE
62,QA-063,Encuentros,Tasa Charmander,Monte Ascuas,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Charmander ocupa slots equivalentes a 15% y niveles definidos.,Media,,PENDIENTE
63,QA-064,Encuentros,Tasa Squirtle,Islas Espuma,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Squirtle ocupa slots equivalentes a 15% y niveles definidos.,Media,,PENDIENTE
64,QA-065,Encuentros,Tasa Eevee,Ruta 7,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Eevee ocupa slots equivalentes a 15% y niveles definidos.,Media,,PENDIENTE
65,QA-066,Encuentros,Tasa Vaporeon,Islas Espuma,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Vaporeon ocupa slots equivalentes a 4% y niveles definidos.,Media,,PENDIENTE
66,QA-067,Encuentros,Tasa Jolteon,Central de Energía,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Jolteon ocupa slots equivalentes a 4% y niveles definidos.,Media,,PENDIENTE
67,QA-068,Encuentros,Tasa Flareon,Mansión Pokémon,Simular/registrar muchos encuentros o inspeccionar tabla compilada.,Flareon ocupa slots equivalentes a 4% y niveles definidos.,Media,,PENDIENTE
68,QA-069,Encuentros,Exclusivas FR preservadas,Tablas fusionadas,Auditar familias FR en todas las rutas modificadas.,Ninguna familia FR queda inobtenible.,Alta,,PENDIENTE
69,QA-070,Changing Cave,Selector de avistamiento,Acceso a Six Island,Elegir cada una de 9 opciones y entrar en cueva.,Tabla cambia a especie seleccionada; niveles originales; elección persiste.,Alta,,PENDIENTE
70,QA-071,Fósiles,Segundo fósil bloqueado antes de revivir,Primer fósil obtenido pero no revivido,Volver al punto de Mt. Moon.,No aparece/activa excavación.,Alta,,PENDIENTE
71,QA-072,Fósiles,Segundo fósil tras revivir,Primer fósil revivido,Volver a Mt. Moon; interactuar excavación.,Recibe exactamente el otro fósil una vez.,Crítica,,PENDIENTE
72,QA-073,Fósiles,Revivir ambos + Ámbar,Poseer/revivir secuencialmente los tres,Hablar con científico después de cada proceso.,No bloquea segundo fósil; 'todos revividos' solo al completar los tres.,Crítica,,PENDIENTE
73,QA-074,Dojo,Rematch bloqueado antes de Sabrina,Koichi original derrotado; Sabrina no,Hablar con Koichi.,No ofrece segunda prueba.,Alta,,PENDIENTE
74,QA-075,Dojo,Rematch post-Sabrina,Sabrina derrotada y primer Hitmon recibido,Hablar con Koichi; ganar.,Equipo exacto; se habilita premio opuesto.,Crítica,,PENDIENTE
75,QA-076,Dojo,Premio opuesto a Hitmonlee,Primera elección Hitmonlee,Ganar rematch; recibir premio.,Entrega Hitmonchan Nv.35.,Crítica,,PENDIENTE
76,QA-077,Dojo,Premio opuesto a Hitmonchan,Primera elección Hitmonchan,Ganar rematch; recibir premio.,Entrega Hitmonlee Nv.35.,Crítica,,PENDIENTE
77,QA-078,Dojo,Storage lleno no pierde premio,Party + boxes llenos,Ganar rematch; intentar premio; liberar espacio; volver.,Premio queda pendiente y luego se recibe una vez.,Alta,,PENDIENTE
78,QA-079,Legendarios,Articuno huida,Articuno disponible,Entrar en combate y huir; salir/reentrar al área.,Articuno vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
79,QA-080,Legendarios,Articuno KO,Articuno disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
80,QA-081,Legendarios,Articuno captura,Articuno disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
81,QA-082,Legendarios,Zapdos huida,Zapdos disponible,Entrar en combate y huir; salir/reentrar al área.,Zapdos vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
82,QA-083,Legendarios,Zapdos KO,Zapdos disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
83,QA-084,Legendarios,Zapdos captura,Zapdos disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
84,QA-085,Legendarios,Moltres huida,Moltres disponible,Entrar en combate y huir; salir/reentrar al área.,Moltres vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
85,QA-086,Legendarios,Moltres KO,Moltres disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
86,QA-087,Legendarios,Moltres captura,Moltres disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
87,QA-088,Legendarios,Mewtwo huida,Mewtwo disponible,Entrar en combate y huir; salir/reentrar al área.,Mewtwo vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
88,QA-089,Legendarios,Mewtwo KO,Mewtwo disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
89,QA-090,Legendarios,Mewtwo captura,Mewtwo disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
90,QA-091,Legendarios,Lugia huida,Lugia disponible,Entrar en combate y huir; salir/reentrar al área.,Lugia vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
91,QA-092,Legendarios,Lugia KO,Lugia disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
92,QA-093,Legendarios,Lugia captura,Lugia disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
93,QA-094,Legendarios,Ho-Oh huida,Ho-Oh disponible,Entrar en combate y huir; salir/reentrar al área.,Ho-Oh vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
94,QA-095,Legendarios,Ho-Oh KO,Ho-Oh disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
95,QA-096,Legendarios,Ho-Oh captura,Ho-Oh disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
96,QA-097,Legendarios,Deoxys huida,Deoxys disponible,Entrar en combate y huir; salir/reentrar al área.,Deoxys vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
97,QA-098,Legendarios,Deoxys KO,Deoxys disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
98,QA-099,Legendarios,Deoxys captura,Deoxys disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
99,QA-100,Legendarios,Mew huida,Mew disponible,Entrar en combate y huir; salir/reentrar al área.,Mew vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
100,QA-101,Legendarios,Mew KO,Mew disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
101,QA-102,Legendarios,Mew captura,Mew disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
102,QA-103,Legendarios,Celebi huida,Celebi disponible,Entrar en combate y huir; salir/reentrar al área.,Celebi vuelve sin requerir Hall of Fame.,Alta,,PENDIENTE
103,QA-104,Legendarios,Celebi KO,Celebi disponible,Debilitarlo; reentrar área; luego completar Hall of Fame y volver.,Antes del HOF no aparece; después reaparece con nuevo roll de PID/IV/shiny.,Crítica,,PENDIENTE
104,QA-105,Legendarios,Celebi captura,Celebi disponible,Capturarlo; reentrar; completar HOF; volver.,No reaparece nunca por flujo normal.,Crítica,,PENDIENTE
105,QA-106,Eventos,No tickets automáticos por HOF,Sin quests completadas,Completar Liga y Hall of Fame.,No AuroraTicket/MysticTicket ni flags de ferry.,Crítica,,PENDIENTE
106,QA-107,Eventos,MysticTicket requisitos incompletos,Network Machine restaurada pero falta un ave capturada,Hablar con Celio.,No entrega MysticTicket.,Alta,,PENDIENTE
107,QA-108,Eventos,MysticTicket requisitos completos,Network Machine + 3 aves capturadas,Hablar con Celio.,Entrega MysticTicket y habilita Navel Rock una vez.,Crítica,,PENDIENTE
108,QA-109,Eventos,Aurora quest orden,Network Machine restaurada,Celio → intentar volver sin museo → museo → Celio.,Solo tras museo entrega AuroraTicket y habilita Birth Island.,Crítica,,PENDIENTE
109,QA-110,Eventos,Deoxys nivel/forma,AuroraTicket y puzzle resuelto,Iniciar combate.,Deoxys Attack Forme Nv.50.,Alta,,PENDIENTE
110,QA-111,Eventos,Mew bloqueado sin Mewtwo,Mewtwo no capturado,Explorar Mansion.,No arranca hide-and-seek.,Alta,,PENDIENTE
111,QA-112,Eventos,Mew secuencia,Mewtwo capturado,Recorrer las 3–4 apariciones y combate final.,Orden correcto; Mew Nv.50 con set exacto y fateful bit.,Crítica,,PENDIENTE
112,QA-113,Eventos,Celebi requisitos,Nacional + Network restored + bestias capturadas,Visitar árbol especial Berry Forest.,Evento activo; Celebi Nv.50 con set exacto.,Crítica,,PENDIENTE
113,QA-114,Roamer,Activación secuencial,Liga + Rocket Sevii + Zafiro/Celio completado,Provocar activación y capturar cada bestia.,Suicune → Raikou → Entei; una activa cada vez.,Crítica,,PENDIENTE
114,QA-115,Roamer,Huida conserva estado,Bestia vista con daño/status,Huir; reencontrar.,"Misma PID/IV/shiny, HP y status persisten.",Crítica,,PENDIENTE
115,QA-116,Roamer,Rugido no borra,Bestia puede usar Rugido,Dejar que use Rugido; reencontrar.,Sigue activa con mismo estado.,Crítica,,PENDIENTE
116,QA-117,Roamer,KO reactiva al cambio de ruta,Bestia activa,Debilitar; cambiar de ruta; reencontrar.,"Reaparece full HP, mismo PID/IV/shiny; siguiente bestia no se activa.",Crítica,,PENDIENTE
117,QA-118,Roamer,Pokédex área,Bestia aún no vista y luego vista,Consultar área antes/después y tras mover rutas.,Antes desconocida; después ruta exacta actual.,Alta,,PENDIENTE
118,QA-119,Economía,Porygon 5000 repetible,5000+ fichas,Comprar Porygon dos veces.,Cada compra cuesta 5000; segundo permitido si hay espacio.,Alta,,PENDIENTE
119,QA-120,Economía,Objetos evolución post-Nacional,Antes y después de National Dex,Revisar tienda.,No están antes; aparecen después con precios exactos.,Alta,,PENDIENTE
120,QA-121,Economía,Lucky Egg postgame,Postgame,Comprar Huevo Suerte.,Cuesta $30.000; método Chansey sigue existiendo.,Media,,PENDIENTE
121,QA-122,Economía,Circuito Resort Gorgeous,VS Seeker cargado,Ubicarse en punto óptimo y activar; combatir Jacki/Gillian/Celina.,Los tres pueden entrar en circuito; payout total objetivo ~30k antes bonuses.,Media,,PENDIENTE
122,QA-123,Economía,Tutor price table,Todos los tutores usados una vez,Intentar repetir cada tutor.,Cada uno cobra su precio documentado.,Alta,,PENDIENTE
123,QA-124,Economía,Berry shop progression,Partida historia y post-Nacional,Comparar inventario/precios.,Aventura y postgame muestran listas correctas.,Media,,PENDIENTE
124,QA-125,Jefes,Validador 0 ilegalidades,Datos finales de trainers,Ejecutar validador automático.,0 movimientos/objetos/IDs incompatibles salvo excepciones Full explícitas.,Crítica,,PENDIENTE
125,QA-126,Jefes,Máx curación Champion,Combate Gary Champion,Forzar múltiples oportunidades de curación.,Usa como máximo 2 Restaurar Todo.,Alta,,PENDIENTE
126,QA-127,Jefes,Held items rematch,Datos compilados,Auditar cada rematch.,3–5 objetos equipados aprox.; máximo 1 Restos por team según tabla.,Media,,PENDIENTE
127,QA-128,Gary,Inicial siempre Squirtle,Elegir cada starter en tres saves,Jugar hasta varios encuentros del rival.,Gary usa siempre la rama Squirtle/Blastoise.,Crítica,,PENDIENTE
128,QA-129,Gary,Curva de niveles,Jugar/inspeccionar todos los encuentros,Registrar ace de cada combate.,Ace: 5 → 12 → 22 → 28 → 34 → 49 → 61 → 69.,Alta,,PENDIENTE
129,QA-130,Gary,Movesets tempranos,Datos finales,Ejecutar validador y smoke de cada encuentro.,Todos legales y cada pelea tiene amenaza real; Abra no queda inútil.,Alta,,PENDIENTE
130,QA-131,Gary,Revancha postgame,Liga rematch disponible,Combatir Gary revancha.,Nidoqueen80/Magmar80/Golem81/Scizor82/Arcanine83/Blastoise85; set/items exactos.,Crítica,,PENDIENTE
131,QA-132,Compatibilidad,Trade Full → vanilla,Full con Pokémon representativos Gen I/II/III y moves cambiados,Intercambiar a FireRed/Emerald vanilla en mGBA.,Datos válidos; juego receptor interpreta categoría según su propio motor sin corrupción.,Crítica,,PENDIENTE
132,QA-133,Compatibilidad,Trade vanilla → Full,Vanilla con Pokémon representativos,Intercambiar a Full; guardar/cargar.,Pokémon conserva PID/OT/IV/EV/moves/item.,Crítica,,PENDIENTE
133,QA-134,Bugs,Roamer IV setter,Crear roamer con IV conocidos,Instanciar batalla y leer IV.,Los 6 IV coinciden con valor almacenado; no quedan bits en cero por bug.,Crítica,,PENDIENTE
134,QA-135,Bugs,Fishing area OOB,Consultar Pokédex area de especies de pesca en mapas extremos,Abrir área repetidamente / sanitizers si disponible.,Sin lectura fuera de límites/crash/datos basura.,Alta,,PENDIENTE
135,QA-136,Bugs,L=A repeat,Configurar L=A,Mantener/repetir inputs en menús.,Repetición coherente; no se pierde/remapea incorrectamente.,Media,,PENDIENTE
136,QA-137,Bugs,Move Reminder scroll,Lista larga de movimientos,Desplazar arriba/abajo hasta extremos.,Indicadores correctos; no sprite corrupto.,Media,,PENDIENTE
137,QA-138,Bugs,Party menu leak,Repetir ruta afectada de acción de dos mons muchas veces,Monitorear heap/memoria.,Buffers se liberan; no degradación/crash.,Media,,PENDIENTE
138,QA-139,Bugs,Berry Crush sparkle,Berry Crush multiplayer,Ejecutar valores altos de sparkle.,Rango completo válido y sin campo incorrecto.,Media,,PENDIENTE
<PARSED TEXT FOR SHEET: 4 / 8 TABS
TAB NAME: Jefes>
index,Entrenador,Fase,Pokémon,Nivel,Movimientos,Objeto,IV objetivo,Notas
0,Brock,Historia,Geodude,14,Lanzarrocas / Placaje / Rizo Defensa / Chapoteolodo,—,6,
1,Brock,Historia,Onix,17,Tumba Rocas / Lanzarrocas / Atadura / Chirrido,Baya Aranja,6,
2,Misty,Historia,Goldeen,21,Hidropulso / Cornada / Picotazo / Supersónico,—,10,
3,Misty,Historia,Staryu,23,Hidropulso / Pantalla Luz / Recuperación / Giro Rápido,—,10,
4,Misty,Historia,Starmie,26,Hidropulso / Psíquico / Recuperación / Rapidez,Baya Zidra,10,
5,Lt. Surge,Historia,Voltorb,25,Onda Voltio / Chispa / Bomba Sónica / Chirrido,—,12,
6,Lt. Surge,Historia,Pikachu,26,Rayo / Onda Trueno / At. Rápido / Doble Equipo,—,12,
7,Lt. Surge,Historia,Raichu,30,Rayo / Golpe Cuerpo / Megapatada / At. Rápido,Baya Zidra,12,
8,Erika,Historia,Tangela,31,Gigadrenado / Somnífero / Desarrollo / Polvo Veneno,—,14,
9,Erika,Historia,Weepinbell,32,Gigadrenado / Ácido / Somnífero / Desarrollo,—,14,
10,Erika,Historia,Vileplume,33,Gigadrenado / Ácido / Paralizador / Aromaterapia,—,14,
11,Erika,Historia,Gloom,35,Gigadrenado / Somnífero / Luz Lunar / Ácido,Baya Zidra,14,
12,Koga,Historia,Venomoth,40,Viento Plata / Psicorrayo / Somnífero / Tóxico,—,16,
13,Koga,Historia,Golbat,41,Ataque Ala / Mordisco / Rayo Confuso / Tóxico,—,16,
14,Koga,Historia,Muk,43,Bomba Lodo / Reducción / Armadura Ácida / Tóxico,—,16,
15,Koga,Historia,Weezing,46,Bomba Lodo / Tóxico / Pantallahumo / Explosión,Baya Zidra,16,
16,Sabrina,Historia,Mr. Mime,42,Psíquico / Hoja Mágica / Reflejo / Pantalla Luz,—,17,
17,Sabrina,Historia,Venomoth,43,Psíquico / Viento Plata / Somnífero / Gigadrenado,—,17,
18,Sabrina,Historia,Kadabra,45,Psíquico / Recuperación / Reflejo / Paz Mental,—,17,
19,Sabrina,Historia,Alakazam,47,Psíquico / Paz Mental / Recuperación / Onda Voltio,Cuchara Torcida,17,
20,Blaine,Historia,Ninetales,47,Lanzallamas / Rayo Confuso / Día Soleado / Giro Fuego,—,18,
21,Blaine,Historia,Rhydon,48,Terremoto / Pedrada / Demolición / Derribo,—,18,
22,Blaine,Historia,Rapidash,49,Lanzallamas / Bote / Derribo / Agilidad,—,18,
23,Blaine,Historia,Arcanine,50,Lanzallamas / Velocidad Extrema / Mordisco / Rugido,—,18,
24,Blaine,Historia,Magmar,52,Llamarada / Puño Fuego / Demolición / Rayo Confuso,Carbón,18,
25,Giovanni,Historia,Persian,50,Sorpresa / Cuchillada / Finta / Chirrido,—,20,
26,Giovanni,Historia,Kingler,51,Martillazo / Pisotón / Protección / Disparo Lodo,—,20,
27,Giovanni,Historia,Nidoqueen,52,Terremoto / Golpe Cuerpo / Fuerza Bruta / Rayo Hielo,—,20,
28,Giovanni,Historia,Nidoking,53,Terremoto / Megacuerno / Demolición / Rayo,—,20,
29,Giovanni,Historia,Golem,54,Terremoto / Avalancha / Doble Filo / Explosión,—,20,
30,Giovanni,Historia,Rhydon,56,Terremoto / Avalancha / Demolición / Doble Filo,Arena Fina,20,
31,Brock,Revancha,Vulpix,60,Lanzallamas / Fuego Fatuo / Rayo Confuso / Protección,—,26,
32,Brock,Revancha,Crobat,61,Golpe Aéreo / Colmillo Veneno / Mordisco / Rayo Confuso,Pico Afilado,26,
33,Brock,Revancha,Forretress,62,Púas / Giro Rápido / Protección / Explosión,—,26,
34,Brock,Revancha,Ludicolo,63,Surf / Gigadrenado / Rayo Hielo / Danza Lluvia,Agua Mística,26,
35,Brock,Revancha,Marshtomp,64,Terremoto / Agua Lodosa / Rayo Hielo / Protección,Arena Fina,26,
36,Brock,Revancha,Steelix,66,Terremoto / Avalancha / Cola Férrea / Triturar,Restos,26,
37,Misty,Revancha,Corsola,61,Surf / Poder Pasado / Recuperación / Manto Espejo,Roca Dura,26,
38,Misty,Revancha,Luvdisc,62,Surf / Rayo Hielo / Beso Dulce / Atracción,—,26,
39,Misty,Revancha,Politoed,63,Surf / Rayo Hielo / Hipnosis / Canto Mortal,Baya Zidra,26,
40,Misty,Revancha,Togetic,63,Hoja Mágica / Poder Pasado / Deseo / Bostezo,Restos,26,
41,Misty,Revancha,Starmie,65,Surf / Psíquico / Rayo / Recuperación,Cuchara Torcida,26,
42,Misty,Revancha,Gyarados,67,Cascada / Terremoto / Danza Dragón / Hiperrayo,Agua Mística,26,
43,Lt. Surge,Revancha,Electrode,64,Rayo / Pantalla Luz / Manto Espejo / Explosión,Imán,26,
44,Lt. Surge,Revancha,Magneton,65,Rayo / Onda Trueno / Triataque / Eco Metálico,Baya Zidra,26,
45,Lt. Surge,Revancha,Electabuzz,66,Rayo / Demolición / Psíquico / Pantalla Luz,—,26,
46,Lt. Surge,Revancha,Raichu,69,Rayo / Demolición / Cola Férrea / Onda Trueno,Restos,26,
47,Erika,Revancha,Tangela,62,Gigadrenado / Somnífero / Desarrollo / Paralizador,—,26,
48,Erika,Revancha,Jumpluff,63,Gigadrenado / Somnífero / Drenadoras / Síntesis,Restos,26,
49,Erika,Revancha,Bellossom,64,Gigadrenado / Danza Pétalo / Día Soleado / Rayo Solar,—,26,
50,Erika,Revancha,Victreebel,65,Gigadrenado / Bomba Lodo / Somnífero / Hoja Afilada,Semilla Milagro,26,
51,Erika,Revancha,Vileplume,66,Gigadrenado / Bomba Lodo / Somnífero / Luz Lunar,—,26,
52,Erika,Revancha,Vileplume,69,Rayo Solar / Bomba Lodo / Somnífero / Día Soleado,Semilla Milagro,26,
53,Koga,Revancha,Ariados,64,Bomba Lodo / Psíquico / Telaraña / Agilidad,—,28,
54,Koga,Revancha,Forretress,65,Púas / Giro Rápido / Protección / Explosión,Cinta Focus,28,
55,Koga,Revancha,Venomoth,65,Psíquico / Viento Plata / Somnífero / Gigadrenado,—,28,
56,Koga,Revancha,Muk,67,Bomba Lodo / Golpe Cuerpo / Demolición / Reducción,Restos,28,
57,Koga,Revancha,Weezing,68,Bomba Lodo / Lanzallamas / Rayo / Explosión,—,28,
58,Koga,Revancha,Crobat,71,Golpe Aéreo / Colmillo Veneno / Mordisco / Rayo Confuso,Pico Afilado,28,
59,Sabrina,Revancha,Venomoth,65,Psíquico / Viento Plata / Somnífero / Gigadrenado,—,28,
60,Sabrina,Revancha,Mr. Mime,65,Psíquico / Hoja Mágica / Reflejo / Pantalla Luz,Restos,28,
61,Sabrina,Revancha,Kadabra,66,Psíquico / Paz Mental / Recuperación / Reflejo,—,28,
62,Sabrina,Revancha,Espeon,68,Psíquico / Paz Mental / Sol Matinal / Reflejo,Cuchara Torcida,28,
63,Sabrina,Revancha,Gengar,69,Bola Sombra / Rayo / Hipnosis / Come Sueños,Hechizo,28,
64,Sabrina,Revancha,Alakazam,72,Psíquico / Paz Mental / Recuperación / Onda Voltio,Cuchara Torcida,28,
65,Blaine,Revancha,Ninetales,66,Lanzallamas / Fuego Fatuo / Rayo Confuso / Día Soleado,Carbón,28,
66,Blaine,Revancha,Rapidash,67,Llamarada / Bote / Doble Filo / Agilidad,—,28,
67,Blaine,Revancha,Arcanine,68,Lanzallamas / Velocidad Extrema / Cola Férrea / Mordisco,Restos,28,
68,Blaine,Revancha,Magcargo,68,Lanzallamas / Avalancha / Golpe Cuerpo / Bostezo,—,28,
69,Blaine,Revancha,Rhydon,70,Terremoto / Avalancha / Megacuerno / Demolición,Arena Fina,28,
70,Blaine,Revancha,Magmar,73,Llamarada / Puño Fuego / Demolición / Rayo Confuso,Carbón,28,
71,Giovanni,Revancha,Persian,67,Sorpresa / Cuchillada / Mordisco / Contoneo,—,28,
72,Giovanni,Revancha,Cloyster,68,Surf / Rayo Hielo / Púas / Protección,Antiderretir,28,
73,Giovanni,Revancha,Machamp,69,Tajo Cruzado / Avalancha / Terremoto / Corpulencia,Cinturón Negro,28,
74,Giovanni,Revancha,Nidoqueen,70,Terremoto / Rayo Hielo / Rayo / Fuerza Bruta,—,28,
75,Giovanni,Revancha,Nidoking,71,Terremoto / Megacuerno / Rayo / Rayo Hielo,Arena Fina,28,
76,Giovanni,Revancha,Rhydon,74,Terremoto / Avalancha / Megacuerno / Doble Filo,Restos,28,
77,Lorelei,Liga inicial,Dewgong,57,Rayo Hielo / Surf / Granizo / Velo Sagrado,—,24,
78,Lorelei,Liga inicial,Slowbro,58,Surf / Psíquico / Rayo Hielo / Amnesia,—,24,
79,Lorelei,Liga inicial,Jynx,59,Rayo Hielo / Psíquico / Beso Amoroso / Atracción,—,24,
80,Lorelei,Liga inicial,Cloyster,60,Rayo Hielo / Surf / Púas / Protección,Antiderretir,24,
81,Lorelei,Liga inicial,Lapras,61,Rayo Hielo / Surf / Rayo / Golpe Cuerpo,Baya Zidra,24,
82,Bruno,Liga inicial,Onix,58,Terremoto / Tumba Rocas / Cola Férrea / Tormenta Arena,—,25,
83,Bruno,Liga inicial,Hitmonchan,59,Gancho Alto / Ultrapuño / Puño Hielo / Puño Trueno,Cinta Focus,25,
84,Bruno,Liga inicial,Hitmonlee,60,Demolición / Megapatada / Avalancha / Terremoto,—,25,
85,Bruno,Liga inicial,Onix,60,Terremoto / Avalancha / Doble Filo / Cola Férrea,—,25,
86,Bruno,Liga inicial,Machamp,62,Tajo Cruzado / Corpulencia / Avalancha / Terremoto,Cinturón Negro,25,
87,Agatha,Liga inicial,Haunter,59,Bola Sombra / Hipnosis / Come Sueños / Mal de Ojo,—,26,
88,Agatha,Liga inicial,Gengar,60,Bola Sombra / Psíquico / Rayo Confuso / Tóxico,—,26,
89,Agatha,Liga inicial,Golbat,60,Golpe Aéreo / Colmillo Veneno / Mordisco / Rayo Confuso,—,26,
90,Agatha,Liga inicial,Arbok,61,Colmillo Veneno / Terremoto / Avalancha / Deslumbrar,—,26,
91,Agatha,Liga inicial,Gengar,63,Bola Sombra / Bomba Lodo / Rayo / Hipnosis,Hechizo,26,
92,Lance,Liga inicial,Gyarados,61,Cascada / Danza Dragón / Terremoto / Hiperrayo,—,27,
93,Lance,Liga inicial,Dragonair,61,Enfado / Onda Trueno / Rayo Hielo / Velo Sagrado,—,27,
94,Lance,Liga inicial,Dragonair,62,Enfado / Lanzallamas / Rayo / Onda Trueno,—,27,
95,Lance,Liga inicial,Aerodactyl,63,Avalancha / Golpe Aéreo / Terremoto / Doble Filo,Roca Dura,27,
96,Lance,Liga inicial,Dragonite,65,Enfado / Golpe Aéreo / Rayo Hielo / Lanzallamas,Colmillo Dragón,27,
97,Gary,Liga inicial,Pidgeot,64,Golpe Aéreo / Retroceso / Ala de Acero / Danza Pluma,—,28,
98,Gary,Liga inicial,Alakazam,65,Psíquico / Paz Mental / Recuperación / Onda Voltio,—,28,
99,Gary,Liga inicial,Nidoking,65,Terremoto / Megacuerno / Rayo Hielo / Rayo,—,28,
100,Gary,Liga inicial,Rhydon,66,Terremoto / Avalancha / Megacuerno / Doble Filo,Arena Fina,28,
101,Gary,Liga inicial,Arcanine,67,Lanzallamas / Velocidad Extrema / Cola Férrea / Mordisco,Carbón,28,
102,Gary,Liga inicial,Blastoise,69,Hidrobomba / Rayo Hielo / Terremoto / Danza Lluvia,Restos,30,
103,Lorelei,Liga revancha,Dewgong,74,Rayo Hielo / Surf / Granizo / Velo Sagrado,Antiderretir,29,
104,Lorelei,Liga revancha,Cloyster,75,Rayo Hielo / Surf / Púas / Protección,—,29,
105,Lorelei,Liga revancha,Slowbro,75,Surf / Psíquico / Rayo Hielo / Paz Mental,Cuchara Torcida,29,
106,Lorelei,Liga revancha,Piloswine,76,Terremoto / Avalancha / Ventisca / Granizo,—,29,
107,Lorelei,Liga revancha,Jynx,77,Rayo Hielo / Psíquico / Beso Amoroso / Paz Mental,—,29,
108,Lorelei,Liga revancha,Lapras,79,Rayo Hielo / Surf / Rayo / Golpe Cuerpo,Restos,30,
109,Bruno,Liga revancha,Onix,75,Terremoto / Avalancha / Cola Férrea / Tormenta Arena,Roca Dura,29,
110,Bruno,Liga revancha,Steelix,76,Terremoto / Avalancha / Cola Férrea / Triturar,—,29,
111,Bruno,Liga revancha,Hitmonchan,76,Gancho Alto / Ultrapuño / Puño Hielo / Puño Trueno,Cinturón Negro,29,
112,Bruno,Liga revancha,Hitmonlee,77,Demolición / Megapatada / Avalancha / Terremoto,—,29,
113,Bruno,Liga revancha,Hitmontop,78,Triple Patada / Avalancha / Contador / Corpulencia,Cinta Focus,29,
114,Bruno,Liga revancha,Machamp,80,Tajo Cruzado / Corpulencia / Avalancha / Terremoto,Restos,30,
115,Agatha,Liga revancha,Gengar,76,Bola Sombra / Psíquico / Hipnosis / Come Sueños,—,30,
116,Agatha,Liga revancha,Crobat,77,Golpe Aéreo / Colmillo Veneno / Mordisco / Rayo Confuso,Pico Afilado,29,
117,Agatha,Liga revancha,Misdreavus,77,Bola Sombra / Psíquico / Rayo / Canto Mortal,Hechizo,29,
118,Agatha,Liga revancha,Arbok,79,Colmillo Veneno / Terremoto / Avalancha / Deslumbrar,Flecha Veneno,29,
119,Agatha,Liga revancha,Gengar,81,Bola Sombra / Bomba Lodo / Rayo / Hipnosis,Restos,30,
120,Lance,Liga revancha,Gyarados,78,Cascada / Danza Dragón / Terremoto / Hiperrayo,Agua Mística,29,
121,Lance,Liga revancha,Kingdra,79,Cascada / Rayo Hielo / Danza Dragón / Hiperrayo,—,29,
122,Lance,Liga revancha,Dragonite,79,Terremoto / Garra Dragón / Lanzallamas / Rayo Hielo,Colmillo Dragón,30,
123,Lance,Liga revancha,Aerodactyl,81,Avalancha / Golpe Aéreo / Terremoto / Doble Filo,Roca Dura,29,
124,Lance,Liga revancha,Dragonite,82,Enfado / Rayo / Rayo Hielo / Lanzallamas,Restos,30,
125,Gary,Liga revancha,Nidoqueen,80,Terremoto / Fuerza Bruta / Rayo Hielo / Rayo,Arena Fina,29,
126,Gary,Liga revancha,Magmar,80,Lanzallamas / Llamarada / Demolición / Rayo Confuso,Carbón,29,
127,Gary,Liga revancha,Golem,81,Terremoto / Avalancha / Doble Filo / Explosión,Roca Dura,29,
128,Gary,Liga revancha,Scizor,82,Danza Espada / Ala de Acero / Golpe Aéreo / At. Rápido,Revest. Metálico,29,
129,Gary,Liga revancha,Arcanine,83,Lanzallamas / Velocidad Extrema / Cola Férrea / Mordisco,—,29,
130,Gary,Liga revancha,Blastoise,85,Hidrobomba / Rayo Hielo / Terremoto / Danza Lluvia,Restos,30,
<PARSED TEXT FOR SHEET: 5 / 8 TABS
TAB NAME: Gary>
index,Encuentro,Pokémon,Nivel,Movimientos,Objeto,IV objetivo
0,Laboratorio,Squirtle,5,Placaje / Látigo,—,0
1,Ruta 22 I,Pidgey,10,Placaje / Ataque Arena / Tornado,—,6
2,Ruta 22 I,Squirtle,12,Placaje / Látigo / Burbuja / Refugio,—,6
3,Celeste,Abra,18,Psíquico / Reflejo / Pantalla Luz / Teletransporte,—,10
4,Celeste,Rattata,19,Hipercolmillo / At. Rápido / Látigo / Placaje,—,10
5,Celeste,Pidgeotto,20,At. Rápido / Tornado / Ataque Arena / Remolino,—,10
6,Celeste,Squirtle,22,Pistola Agua / Mordisco / Refugio / Burbuja,—,10
7,S.S. Anne,Krabby,24,Disparo Lodo / Agarre / Burbuja / Fortaleza,—,12
8,S.S. Anne,Pidgeotto,25,Golpe Aéreo / At. Rápido / Ataque Arena / Remolino,—,12
9,S.S. Anne,Kadabra,25,Psicorrayo / Recuperación / Reflejo / Anulación,—,12
10,S.S. Anne,Wartortle,28,Hidropulso / Mordisco / Giro Rápido / Protección,—,12
11,Torre Pokémon,Exeggcute,30,Psíquico / Gigadrenado / Paralizador / Drenadoras,—,14
12,Torre Pokémon,Pidgeotto,31,Golpe Aéreo / Retroceso / Ataque Arena / Remolino,—,14
13,Torre Pokémon,Growlithe,31,Rueda Fuego / Derribo / Mordisco / Rugido,—,14
14,Torre Pokémon,Kadabra,32,Psicorrayo / Recuperación / Reflejo / Premonición,—,14
15,Torre Pokémon,Wartortle,34,Hidropulso / Mordisco / Protección / Giro Rápido,—,14
16,Silph S.A.,Exeggutor,43,Psíquico / Gigadrenado / Somnífero / Reflejo,—,18
17,Silph S.A.,Pidgeot,44,Golpe Aéreo / Retroceso / Danza Pluma / Ataque Arena,—,18
18,Silph S.A.,Growlithe,44,Lanzallamas / Mordisco / Derribo / Rugido,—,18
19,Silph S.A.,Alakazam,46,Psíquico / Paz Mental / Recuperación / Reflejo,—,18
20,Silph S.A.,Blastoise,49,Surf / Rayo Hielo / Mordisco / Protección,Baya Zidra,18
21,Ruta 22 II,Rhyhorn,56,Terremoto / Avalancha / Doble Filo / Cola Férrea,—,24
22,Ruta 22 II,Pidgeot,56,Golpe Aéreo / Retroceso / Ala de Acero / Danza Pluma,—,24
23,Ruta 22 II,Nidoking,57,Terremoto / Megacuerno / Rayo Hielo / Rayo,—,24
24,Ruta 22 II,Alakazam,58,Psíquico / Paz Mental / Recuperación / Onda Voltio,—,24
25,Ruta 22 II,Arcanine,59,Lanzallamas / Velocidad Extrema / Cola Férrea / Mordisco,—,24
26,Ruta 22 II,Blastoise,61,Surf / Rayo Hielo / Terremoto / Danza Lluvia,Agua Mística,24
<PARSED TEXT FOR SHEET: 6 / 8 TABS
TAB NAME: Decisiones>
index,ID,Tema,Decisión,Racional,Estado
0,D-001,Filosofía,Mantener FireRed reconocible; quitar fricción artificial y dependencias externas.,"Modernización selectiva, no remake.",CERRADA
1,D-002,Especies,V1.0 limitada a Gen I–III (#001–386).,Compatibilidad Gen III y alcance controlado.,CERRADA
2,D-003,IDs,"No crear nuevos IDs de Pokémon, movimientos ni objetos.",Prioriza trading seguro y futuro Emerald Full.,CERRADA
3,D-004,MO,Mantener sistema original de MO.,El usuario no considera sustancial la modernización.,CERRADA
4,D-005,Split,Adoptar split físico/especial por movimiento.,Mejora coherencia sin importar stats/moves modernos.,CERRADA
5,D-006,Contacto,Usar contacto moderno independiente de categoría.,Evita incoherencias con habilidades.,CERRADA
6,D-007,Datos moves,Categoría/contacto modernos; potencia/precisión/PP/efectos Gen III.,Regla híbrida explícita.,CERRADA
7,D-008,Learnsets,Solo corregir víctimas severas del split.,Evita rebalance masivo.,CERRADA
8,D-009,Arbok,Añadir Colmillo Veneno por nivel.,STAB físico razonable.,CERRADA
9,D-010,Banette/Shedinja,Sustituir Bola Sombra por Puño Sombra en nivel; MT30 queda.,Compensación mínima del split.,CERRADA
10,D-011,MT,"MT reutilizables, máximo una copia, no vender/tirar.",QoL sin crear IDs.,CERRADA
11,D-012,Recordador,$2.000 por movimiento.,Quita farmeo de setas.,CERRADA
12,D-013,Tutores,Primera vez gratis; luego precio fijo.,Renovabilidad con coste.,CERRADA
13,D-014,Correr,Permitir correr en interiores tras zapatillas.,QoL menor y segura.,CERRADA
14,D-015,Repel,Prompt de auto-reuso.,Reduce fricción.,CERRADA
15,D-016,Bolsa,142 slots en bolsillo normal usando 400 bytes unused.,Elimina límite práctico sin mover offsets.,CERRADA
16,D-017,EV UI,Mostrar EVs en resumen con toggle.,Apoya crianza/entrenamiento del usuario.,CERRADA
17,D-018,Synchronize,50% naturaleza salvaje como Emerald.,QoL de captura sin alterar combate.,CERRADA
18,D-019,Safari,Sin límite de pasos; 30 Safari Balls mantienen fin.,Quita tedium sin borrar minijuego.,CERRADA
19,D-020,Trade evolutions,Kadabra/Machoke/Graveler/Haunter evolucionan al 36.,Autosuficiencia single-save.,CERRADA
20,D-021,Held evolutions,Trade-item evolutions pasan a uso directo del objeto.,Elimina dependencia de trade.,CERRADA
21,D-022,Eevee,Piedra Solar→Espeon; Piedra Lunar→Umbreon.,No hay reloj funcional para day/night.,CERRADA
22,D-023,National Dex,Permitir evoluciones Gen II/III pre-Nacional pero ocultar Dex Nacional hasta Oak.,Separa mecánica de UI/progresión.,CERRADA
23,D-024,Trade pre-Nat,Conservar restricciones vanilla de link pre-Nacional.,Compatibilidad FRLG.,CERRADA
24,D-025,Exclusivas LG,Integrarlas en hábitats oficiales LG sin reemplazar toda tabla FR.,Preserva identidad FireRed.,CERRADA
25,D-026,Iniciales,Bulbasaur/Charmander/Squirtle y evoluciones salvajes con tasas 15/5/4%.,Autosuficiencia y rareza controlada.,CERRADA
26,D-027,Eevee,Eevee 15% Ruta 7; Vaporeon/Jolteon/Flareon 4% en hábitats temáticos.,Reduce dependencia de regalo único.,CERRADA
27,D-028,Fósiles,Segundo fósil por excavación tras revivir el primero.,Conserva la elección inicial temporal.,CERRADA
28,D-029,Dojo,Segundo combate tras Sabrina; premio = Hitmon no elegido.,Completa Pokédex sin invalidar elección temprana.,CERRADA
29,D-030,Changing Cave,Restaurar las 9 tablas mediante investigador selector.,Usa contenido original ya programado.,CERRADA
30,D-031,Legendarios estáticos,Huida reentra; KO respawn tras HOF; captura permanente.,Evita pérdidas accidentales sin trivializar.,CERRADA
31,D-032,Roamers,"Suicune→Raikou→Entei secuenciales, una activa.",Cabe en struct Roamer existente.,CERRADA
32,D-033,Roamer KO/Roar,KO reactiva misma identidad; Rugido no borra.,Corrige frustraciones/bugs.,CERRADA
33,D-034,MysticTicket,Quest Celio tras Network + 3 aves capturadas.,Sustituye distribución externa con lore mínimo.,CERRADA
34,D-035,AuroraTicket,Celio→Museo Pewter→Celio.,Sustituye distribución externa manteniendo Birth Island.,CERRADA
35,D-036,Deoxys,"Birth Island original, Attack Forme, Nv.50.",Evento original con nivel ajustado.,CERRADA
36,D-037,Mew,Mansion hide-and-seek tras capturar Mewtwo; Nv.50 fateful.,No importar Faraway Island.,CERRADA
37,D-038,Celebi,Berry Forest tras National + Network + 3 bestias; Nv.50.,Cierra hilo Johto sin mapa nuevo.,CERRADA
38,D-039,Hoenn legends,No incluir Jirachi/Latios/Latias/Regis/Groudon/Kyogre/Rayquaza.,Reservados a Emerald Full.,CERRADA
39,D-040,Economía,Sin multiplicador global de dinero.,Ajustes localizados.,CERRADA
40,D-041,Type boosters,"16 potenciadores a $3.000, efecto Gen III 10%.",Acceso razonable sin buff moderno.,CERRADA
41,D-042,Porygon,"5.000 fichas, repetible.",Living Dex y menor grind.,CERRADA
42,D-043,Lucky Egg,Método Chansey + tienda postgame $30.000.,Renovable sin quitar método clásico.,CERRADA
43,D-044,Gary,Siempre Squirtle/Blastoise como ace.,Híbrido natural anime + FireRed.,CERRADA
44,D-045,Gary roster,Plantilla rotativa; no exigir mostrar preevolución de cada miembro.,Gary anime captura y rota mucho.,CERRADA
45,D-046,Gary Champion,Pidgeot/Alakazam/Nidoking/Rhydon/Arcanine/Blastoise.,Cinco piezas FireRed + Nidoking anime.,CERRADA
46,D-047,Gary dificultad,Ace 5→12→22→28→34→49→61→69; IV progresivos.,Cada encuentro debe sentirse como jefe.,CERRADA
47,D-048,Líderes,"Equipos anime/históricos con dificultad moderada, no hardcore.",Identidad temática + reto razonable.,CERRADA
48,D-049,Rematches,"Repetibles indefinidamente, roster histórico hasta Gen III.",Postgame con identidad.,CERRADA
49,D-050,Curación bosses,Máximo 2 curaciones; Champion no usa 4 Full Restores.,Evita desgaste artificial.,CERRADA
50,D-051,IV bosses,Curva progresiva; no 31 universal.,Dificultad transparente sin EV ocultos.,CERRADA
51,D-052,Naturalezas bosses,No optimizar competitivamente.,Evita minmax oculto.,CERRADA
52,D-053,IA,"Mantener núcleo probado de FRLG, hacerlo split-aware.",Robustez sobre complejidad.,CERRADA
53,D-054,Bugfixes,Aprobar 8 bugs auditados + UBFIX/BUGFIX modernos.,Estabilidad técnica.,CERRADA
54,D-055,Base,Producción en pokefirered-europe español; pret como upstream.,Evita traducción secundaria.,CERRADA
55,D-056,Build,firered_es_modern; baseline SHA-1 verificado antes de cambios.,Reproducibilidad.,CERRADA
56,D-057,Save,No mover offsets ni cambiar tamaño SaveBlock1.,Reduce riesgo/compatibilidad.,CERRADA
57,D-058,Flags/vars Full,Reservar bloques unused 0x8C3–0x8E2 y 0x408C–0x409B.,Evita colisiones.,CERRADA
58,D-059,Save header,Usar unused_3D24[16] para magic/schema; bag extra en unused_348C.,Migración y versionado.,CERRADA
59,D-060,Trading,Trading Gen III es objetivo oficial; round-trip del mismo .sav con vanilla no.,"Prioriza Pokémon, no save modded.",CERRADA
60,D-061,Producción,No empezar código sin paquete v1.0 + matrices + QA + decision log + prompt.,Evita reinterpretación.,CERRADA
<PARSED TEXT FOR SHEET: 7 / 8 TABS
TAB NAME: Estados_Save>
index,Arquitectura de guardado Full,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
0,,,,,
1,Zona,Dirección,Capacidad,Uso Full,Notas
2,SaveBlock1,Tamaño,0x3D68,Sin cambio,Mantener offsets estándar.
3,Bolsa normal,0x348C–0x361B,400 bytes,100 ItemSlot extra,42 + 100 = 142 slots lógicos.
4,Header Full,0x3D24–0x3D33,16 bytes,magic RFFL + schemaVersion=1 + reserva,Importación schema0 si falta magic.
5,Reserva intacta,0x3A94–0x3AD3,64 bytes,No usar v1.0,Margen futuro.
6,Flags Full,0x8C3–0x8E2,32 flags,Namespace reservado,Persistentes.
7,Vars Full,0x408C–0x409B,16 vars,Namespace reservado,Persistentes.
8,,,,,
9,Asignaciones iniciales del namespace,,,,
10,Símbolo,Tipo,ID,Sistema,Uso
11,FLAG_FULL_DOJO_CHOSE_HITMONLEE,Flag,0x8C3,Dojo,Marca elección original Hitmonlee; unset con premio original = Hitmonchan.
12,FLAG_FULL_DOJO_SECOND_REWARD,Flag,0x8C4,Dojo,Segundo Hitmon entregado.
13,FLAG_FULL_ZAPDOS_KO_PENDING,Flag,0x8C5,Legendarios,KO; reset en próxima entrada Hall of Fame.
14,FLAG_FULL_ARTICUNO_KO_PENDING,Flag,0x8C6,Legendarios,KO; reset en próxima entrada Hall of Fame.
15,FLAG_FULL_MOLTRES_KO_PENDING,Flag,0x8C7,Legendarios,KO; reset en próxima entrada Hall of Fame.
16,FLAG_FULL_MEWTWO_KO_PENDING,Flag,0x8C8,Legendarios,KO; reset en próxima entrada Hall of Fame.
17,FLAG_FULL_MEW_CAUGHT,Flag,0x8C9,Mew,Capturado.
18,FLAG_FULL_MEW_KO_PENDING,Flag,0x8CA,Mew,KO; elegible para respawn HOF.
19,FLAG_FULL_CELEBI_CAUGHT,Flag,0x8CB,Celebi,Capturado.
20,FLAG_FULL_CELEBI_KO_PENDING,Flag,0x8CC,Celebi,KO; elegible para respawn HOF.
21,VAR_FULL_MYSTIC_QUEST,Var,0x408C,MysticTicket,Estado miniquest Celio/aves.
22,VAR_FULL_AURORA_QUEST,Var,0x408D,AuroraTicket,Estado Celio→Museo Pewter→Celio.
23,VAR_FULL_MEW_QUEST,Var,0x408E,Mew,Estado hide-and-seek Mansión.
24,VAR_FULL_CELEBI_QUEST,Var,0x408F,Celebi,Estado anomalía Bosque Baya.
25,VAR_FULL_ROAMER_SEQUENCE,Var,0x4090,Roamers,0/1/2/3 para Suicune→Raikou→Entei/completo.
<PARSED TEXT FOR SHEET: 8 / 8 TABS
TAB NAME: Precios>
index,Categoría,Contenido,Precio,Disponibilidad,Notas
0,Potenciador de tipo,Arena Fina,3000,Historia/postgame,Efecto Gen III +10%
1,Potenciador de tipo,Roca Dura,3000,Historia/postgame,Efecto Gen III +10%
2,Potenciador de tipo,Semilla Milagro,3000,Historia/postgame,Efecto Gen III +10%
3,Potenciador de tipo,Gafas de Sol,3000,Historia/postgame,Efecto Gen III +10%
4,Potenciador de tipo,Cinturón Negro,3000,Historia/postgame,Efecto Gen III +10%
5,Potenciador de tipo,Imán,3000,Historia/postgame,Efecto Gen III +10%
6,Potenciador de tipo,Agua Mística,3000,Historia/postgame,Efecto Gen III +10%
7,Potenciador de tipo,Pico Afilado,3000,Historia/postgame,Efecto Gen III +10%
8,Potenciador de tipo,Flecha Veneno,3000,Historia/postgame,Efecto Gen III +10%
9,Potenciador de tipo,Antiderretir,3000,Historia/postgame,Efecto Gen III +10%
10,Potenciador de tipo,Hechizo,3000,Historia/postgame,Efecto Gen III +10%
11,Potenciador de tipo,Cuchara Torcida,3000,Historia/postgame,Efecto Gen III +10%
12,Potenciador de tipo,Carbón,3000,Historia/postgame,Efecto Gen III +10%
13,Potenciador de tipo,Colmillo Dragón,3000,Historia/postgame,Efecto Gen III +10%
14,Potenciador de tipo,Pañuelo Seda,3000,Historia/postgame,Efecto Gen III +10%
15,Potenciador de tipo,Polvo Plata,3000,Historia/postgame,Efecto Gen III +10%
16,Objeto equipado,Garra Rápida,4000,Según tienda Full,
17,Objeto equipado,Puño Suerte,4000,Según tienda Full,
18,Objeto equipado,Palo,4000,Según tienda Full,
19,Objeto equipado,Periscopio,5000,Según tienda Full,
20,Objeto equipado,Cinta Focus,5000,Según tienda Full,
21,Objeto equipado,Polvo Metálico,6000,Según tienda Full,
22,Objeto equipado,Campana Concha,6000,Según tienda Full,
23,Objeto equipado,Polvo Brillo,7500,Según tienda Full,
24,Objeto equipado,Bola Luminosa,8000,Según tienda Full,
25,Objeto equipado,Restos,12000,Según tienda Full,
26,Objeto equipado,Hueso Grueso,12000,Según tienda Full,
27,Objeto equipado,Cin. Elegida,15000,Según tienda Full,
28,Evolución,Piedra Solar,3000,Post-Nacional,Renovable
29,Evolución,Piedra Lunar,3000,Post-Nacional,Renovable
30,Evolución,Roca del Rey,5000,Post-Nacional,Renovable
31,Evolución,Revest. Metálico,5000,Post-Nacional,Renovable
32,Evolución,Escama Dragón,5000,Post-Nacional,Renovable
33,Evolución,Mejora,7500,Post-Nacional,Renovable
34,Recurso,PP Up,9800,Historia,
35,Recurso,Éter,1200,Postgame,
36,Recurso,Éter Máx.,2000,Postgame,
37,Recurso,Elixir,3000,Postgame,
38,Recurso,Elixir Máx.,4500,Postgame,
39,Recurso,Huevo Suerte,30000,Postgame,
40,Recurso,MT44 Descanso,3000,Historia,
41,Baya,Baya Zreza,200,Historia,
42,Baya,Baya Atania,200,Historia,
43,Baya,Baya Meloc,200,Historia,
44,Baya,Baya Safre,200,Historia,
45,Baya,Baya Perasi,200,Historia,
46,Baya,Baya Caquic,300,Historia,
47,Baya,Baya Aranja,300,Historia,
48,Baya,Baya Zanama,500,Historia,
49,Baya,Baya Zidra,800,Historia,
50,Baya,Baya Ziuela,1200,Historia,
51,Baya,Baya Higog,600,Historia,
52,Baya,Baya Wiki,600,Historia,
53,Baya,Baya Ango,600,Historia,
54,Baya,Baya Guaya,600,Historia,
55,Baya,Baya Pabaya,600,Historia,
56,Baya,Baya Grana,1500,Post-Nacional,
57,Baya,Baya Algama,1500,Post-Nacional,
58,Baya,Baya Ispero,1500,Post-Nacional,
59,Baya,Baya Meluce,1500,Post-Nacional,
60,Baya,Baya Uvav,1500,Post-Nacional,
61,Baya,Baya Tamate,1500,Post-Nacional,
62,Baya,Baya Lichi,2500,Post-Nacional,
63,Baya,Baya Gonlan,2500,Post-Nacional,
64,Baya,Baya Aslac,2500,Post-Nacional,
65,Baya,Baya Yapati,2500,Post-Nacional,
66,Baya,Baya Aricoc,2500,Post-Nacional,
67,Baya,Baya Zonlan,5000,Post-Nacional,
68,Baya,Baya Arabol,5000,Post-Nacional,