<PARSED TEXT FOR PAGE: 1 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
POKÉMON ROJO FUEGO FULL
Especificación de Preproducción v1.0
Documento de freeze previo a producción
Campo Valor
Estado FROZEN — diseño cerrado; código de Full aún no 
iniciado
Fecha 19 de septiembre de 2026
Base de producto CompuMaxx/pokefirered-europe @ e184c5cf898c…
Upstream técnico pret/pokefirered @ c75f352304d5…
Build objetivo firered_es_modern
Baseline SHA-1 ab8f6bfe0ccdaf41188cd015c8c74c314d02296a
Este documento y las matrices asociadas son la fuente de verdad del proyecto.
<PARSED TEXT FOR PAGE: 2 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
1. Visión del proyecto
Pokémon Rojo Fuego Full es una versión autosuficiente de FireRed que conserva la historia, mapas, estética, 
estructura general y ADN de la versión de 2004, pero elimina dependencias externas y fricciones consideradas 
artificiales. La meta no es crear un remake moderno ni un hack competitivo: es construir el FireRed más 
completo, coherente y cómodo posible dentro del universo Gen I–III.
 Un solo archivo de guardado debe permitir acceder razonablemente al contenido Kanto/FRLG relevante sin 
LeafGreen, distribuciones de evento ni otro cartucho.
 Se elimina tedio, no desafío significativo.
 La dificultad aumenta de forma moderada mediante equipos coherentes, niveles, IV progresivos, objetos e IA
corregida; no mediante EV ocultos ni counter-picking.
 La compatibilidad de intercambio con juegos Gen III es una restricción arquitectónica real.
 El proyecto hermano futuro será Pokémon Esmeralda Full.
2. Alcance y exclusiones
Incluido Excluido
Especies Gen I–III (#001–386) Especies Gen IV+
Split físico/especial por movimiento Tipo Hada
QoL selectivo Megaevoluciones / formas regionales
Eventos Mew/Celebi/Deoxys/Lugia/Ho-Oh Jirachi, Lati@s, Regis, Groudon/Kyogre/Rayquaza
MT reutilizables y tutores repetibles Exp. Share moderno de equipo
Encuentros LG integrados Región/historia nueva de gran escala
Trading Gen III como objetivo Garantía de round-trip del mismo save con ROM vanilla
3. Gobierno de decisiones
Las decisiones marcadas como cerradas no se reinterpretan durante producción. Una mejora nueva, aunque 
parezca conveniente, se registra como propuesta y requiere aprobación del usuario. Las correcciones técnicas 
necesarias para cumplir una mecánica ya aprobada pueden implementarse sin reabrir el diseño.
 Las MO son una decisión explícita: se conserva el sistema original de FireRed.
 Si una conversación antigua contradice este freeze, prevalece este documento y el Decision Log.
 Cada merge a main exige build, smoke test y QA vinculado.
4. Base técnica y build
Elemento Decisión
Base CompuMaxx/pokefirered-europe; producto español nativo, 
no traducción desde inglés.
Commit inicial e184c5cf898cd29efebd33bc1bfe5994277e21ab
Upstream pret/pokefirered para auditoría/correcciones selectivas.
Build firered_es_modern; activa BUGFIX + UBFIX en config.
Baseline compare_firered_es debe reproducir SHA-1 
ab8f6bfe0ccdaf41188cd015c8c74c314d02296a.
Pruebas mGBA como emulador principal; Porymap auxiliar para 
mapas/eventos.
<PARSED TEXT FOR PAGE: 3 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
Antes del primer cambio de Full se crea un tag inmutable `baseline-spanish-vanilla`. Se portan selectivamente 
correcciones upstream relevantes, incluyendo el return de comportamiento indefinido, latin_small/gbagfx y 
LOCALID_RUBY de Mt. Ember, siempre con diff y prueba.
5. Motor de combate
5.1 Split físico/especial
Cada movimiento tendrá una categoría explícita FÍSICO / ESPECIAL / ESTADO almacenada en datos de ROM. La 
categoría deja de deducirse del tipo. Poder Oculto es siempre especial. La estructura de Pokémon y el save no 
cambian.
Movimiento Categoría Full
Cascada Físico
Triturar Físico
Bola Sombra Especial
Bomba Lodo Especial
Hoja Aguda Físico
Puño Fuego/Hielo/Trueno Físico
Poder Oculto Especial siempre
Meteorobola Especial
Premonición Especial
Deseo Oculto Especial
Combate Físico
Regla híbrida: categoría y contacto modernos; potencia, precisión, PP y efectos secundarios Gen III. No se 
importan buffs Gen IV+.
5.2 Contacto e interacciones
 Contact flags modernos para todos los movimientos Gen I–III; categoría y contacto son conceptos 
independientes.
 Quemadura, Reflejo, Pantalla Luz, Contador, Manto Espejo, Hustle, registro de daño y cálculos relacionados 
deben consultar la categoría del movimiento.
 La IA conserva el núcleo probado de FRLG (CHECK_BAD_MOVE + TRY_TO_FAINT + CHECK_VIABILITY), pero 
se vuelve split-aware.
 No se activan por defecto scripts de IA dormidos/experimentales.
5.3 Learnsets mínimos
Pokémon Cambio
Ekans/Arbok Añadir Colmillo Veneno por nivel.
Banette En el punto de Bola Sombra por nivel, enseñar Puño 
Sombra; MT30 se mantiene.
Shedinja Mismo criterio que Banette.
Resto No rehacer learnsets para compensar sistemáticamente el 
split.
6. Evoluciones y Pokédex Nacional
Caso Full
<PARSED TEXT FOR PAGE: 4 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
Kadabra / Machoke / Graveler / Haunter Evolucionan al nivel 36.
Scyther / Onix + Revest. Metálico Usar objeto directamente.
Seadra + Escama Dragón Usar objeto directamente.
Porygon + Mejora Usar objeto directamente.
Poliwhirl / Slowpoke + Roca del Rey Usar objeto directamente.
Eevee + Piedra Solar Espeon.
Eevee + Piedra Lunar Umbreon.
Se eliminan todos los bloqueos de evolución a especies > Mew antes de la Pokédex Nacional, pero la Pokédex 
visible continúa siendo Kanto hasta la ceremonia original de Oak. Los datos Seen/Caught de especies Gen II/III 
deben persistir y aparecer correctamente cuando se habilite la Nacional. Las restricciones de intercambio pre￾Nacional para huevos/no-Kanto se conservan.
7. Calidad de vida
Sistema Especificación
MT Reutilizables; máximo una copia; no vender ni tirar.
MO Sistema original: Pokémon compatible debe conocerla + 
medalla.
Recordador $2.000 por movimiento.
Tutores Primera enseñanza gratis; luego precio fijo.
Correr Permitido en interiores tras Zapatillas.
Repelentes Prompt de encadenamiento al agotarse.
Bolsa 142 slots de objetos normales; sin rediseño radical.
EV Vista toggle en resumen: seis EV + total/510 + barras/252.
Sincronía 50% naturaleza salvaje igual al líder, estilo Emerald.
Safari Sin límite de pasos; 30 Safari Balls; catch/flee original.
7.1 Tutores — precios de repetición
Tutor Precio
Metronomo $1.000
Megapuño $1.500
Mimético $2.000
Megapatada $2.500
Come Sueños $3.000
Movimiento Sísmico $3.500
Contador $4.000
Doble Filo $5.000
Amortiguador $5.000
Golpe Cuerpo $6.000
Explosión $6.000
Onda Trueno $6.500
Avalancha $7.500
Sustituto $8.000
Danza Espada $10.000
8. Disponibilidad y encuentros
FireRed es la tabla base. No se fusionan indiscriminadamente las tablas de LeafGreen; solo se añaden familias 
ausentes en hábitats oficiales de LeafGreen, preservando la disponibilidad de familias exclusivas de FireRed.
<PARSED TEXT FOR PAGE: 5 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
Pokémon Hábitat Full Tasa objetivo
Sandshrew Ruta 8 20%
Vulpix Ruta 8 20%
Bellsprout Ruta 5 25%
Slowpoke Agua oficial LG (p.ej. Ruta 6) 100% Surf en esa tabla
Staryu Ciudad Carmín 40% Supercaña
Magmar Monte Ascuas 5%
Marill Valle Ruinas 10%
Sneasel Cueva Glaciada 5%
Misdreavus Cueva Perdida 5%
Remoraid Aguas Isla 5 40% Supercaña
Mantine Aguas Isla 7 5% Surf
Familia Zona Tasas
Bulbasaur / Ivysaur / Venusaur Bosque Baya 15% / 5% / 4%
Charmander / Charmeleon / Charizard Monte Ascuas 15% / 5% / 4%
Squirtle / Wartortle / Blastoise Islas Espuma 15% / 5% / 4%
Eevee Ruta 7 15%
Vaporeon / Jolteon / Flareon Espuma / Central / Mansión 4% cada uno
Safari: Chansey, Kangaskhan, Tauros, Scyther y Pinsir tienen al menos una zona óptima individual con 15%. 
Changing Cave usa las nueve tablas originales mediante un investigador que selecciona el avistamiento.
9. Eventos, fósiles y Dojo
9.1 Fósiles
La elección original de Mt. Moon se mantiene. Tras revivir el primer fósil en Isla Canela, un punto de excavación 
en Mt. Moon entrega el fósil que no se eligió. Una sola vez. El laboratorio se corrige para admitir Helix + Domo + 
Ámbar y solo declarar «todos revividos» al completar los tres.
9.2 Dojo
Después de derrotar a Sabrina, Koichi ofrece una segunda prueba. Equipo: Primeape 43 / Poliwrath 44 / 
Hitmonlee 45 / Hitmonchan 45 / Machamp 47 (ace). El premio es el Hitmon no elegido originalmente, Nv.35. El 
premio no se pierde si party y cajas están llenas.
9.3 Changing Cave
El investigador permite seleccionar Zubat (normal) o Mareep, Pineco, Houndour, Teddiursa, Aipom, Shuckle, 
Stantler o Smeargle. Se reutiliza VAR_ALTERING_CAVE_WILD_SET y las tablas/niveles originales.
10. Legendarios y míticos
Grupo Regla
Articuno / Zapdos / Moltres / Mewtwo Captura: desaparece; huida: vuelve al reentrar; KO: vuelve tras 
siguiente Hall of Fame con nuevo PID/IV/shiny.
Lugia / Ho-Oh / Deoxys Misma regla; se aprovechan flags FLEW_AWAY/FOUGHT 
originales.
Roamers Suicune Raikou Entei, una activa; KO reactiva misma → →
identidad al cambiar ruta; Rugido no borra.
Pokémon Nivel Acceso
<PARSED TEXT FOR PAGE: 6 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
Articuno / Zapdos / Moltres 50 Ubicaciones originales.
Mewtwo 70 Cueva Celeste original.
Suicune / Raikou / Entei 50 Liga + Rocket Sevii + Zafiro/Celio; 
secuenciales.
Lugia / Ho-Oh 70 MysticTicket Navel Rock. →
Deoxys 50 AuroraTicket Birth Island; Attack →
Forme.
Mew 50 Mewtwo capturado hide-and-seek en →
Mansión Pokémon.
Celebi 50 Nacional + Network + tres bestias árbol →
de Bosque Baya.
MysticTicket: Network Machine restaurada + tres aves capturadas Celio. AuroraTicket: Celio detecta señal → →
Museo de Pewter Celio. La revisión española objetivo es REVISION=0: no se compila el auto-regalo de tickets de →
la revisión 10, y QA lo protege.
Mew: Destructor / Transformación / Megapuño / Metrónomo; fateful encounter. Celebi: Psíquico / Poder Pasado / 
Recuperación / Campana Cura. No se añaden legendarios propios de Hoenn.
11. Economía
11.1 Tiendas y precios clave
Contenido Precio / regla
16 potenciadores de tipo $3.000 cada uno; efecto Gen III +10%.
Porygon 5.000 fichas; repetible.
PP Up $9.800; PP Máx no comercial.
Éter / Éter Máx / Elixir / Elixir Máx Postgame: $1.200 / $2.000 / $3.000 / $4.500.
Huevo Suerte Método Chansey original + postgame $30.000.
Piedra Solar/Lunar $3.000 post-Nacional.
Roca del Rey/Revest. Metálico/Escama Dragón $5.000 post-Nacional.
Mejora $7.500 post-Nacional.
No hay multiplicador global de dinero. El circuito de Resort Gorgeous usa Lady Jacki, Lady Gillian y 
Painter Lady Celina con objetivo de ~30.000 por circuito antes de bonus. VS Seeker conserva recarga de 100 →
pasos.
12. Jefes, Liga e IV
Jefe Primera batalla (niveles) IV objetivo
Brock Geodude14 / Onix17 6
Misty Goldeen21 / Staryu23 / Starmie26 10
Lt. Surge Voltorb25 / Pikachu26 / Raichu30 12
Erika Tangela31 / Weepinbell32 / Vileplume33 / 
Gloom35 14
Koga Venomoth40 / Golbat41 / Muk43 / Weezing46 16
Sabrina Mr. Mime42 / Venomoth43 / Kadabra45 / 
Alakazam47 17
Blaine Ninetales47 / Rhydon48 / Rapidash49 / 
Arcanine50 / Magmar52 18
Giovanni Persian50 / Kingler51 / Nidoqueen52 / 
Nidoking53 / Golem54 / Rhydon56 20
<PARSED TEXT FOR PAGE: 7 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
Curación limitada: primera vuelta usa cantidades moderadas; rematches y Liga máximo 2 Restaurar Todo donde
corresponda. No hay 31 IV universal ni EV ocultos. Las naturalezas no se optimizan competitivamente.
La hoja `Jefes` del workbook contiene los 131 slots detallados de líderes, revanchas, Liga y Gary con nivel, 
moveset, objeto e IV. El validador de producción debe dejar 0 incompatibilidades no exceptuadas.
12.1 Correcciones de legalidad cerradas
Pokémon Corrección
Staryu de Misty Rapidez Pantalla Luz →
Raichu de Surge Derribo At. Rápido →
Tangela de Erika Paralizador Polvo Veneno →
Rhydon de Giovanni Megacuerno Demolición →
Arbok de Agatha Triturar Deslumbrar →
Dragonair de Lance x2 Garra Dragón Enfado →
13. Gary — híbrido FireRed + anime
La estructura de progresión viene de Blue en FireRed; la identidad y rotación vienen de Gary del anime. 
Blastoise es la única línea obligatoriamente persistente. El resto es una plantilla amplia que rota, pero cada 
encuentro sube de calidad.
Encuentro Equipo Ace
Laboratorio Squirtle 5 5
Ruta 22 I Pidgey 10 / Squirtle 12 12
Celeste Abra 18 / Rattata 19 / Pidgeotto 20 / Squirtle 
22 22
S.S. Anne Krabby 24 / Pidgeotto 25 / Kadabra 25 / 
Wartortle 28 28
Torre Pokémon Exeggcute 30 / Pidgeotto 31 / Growlithe 31 / 
Kadabra 32 / Wartortle 34 34
Silph S.A. Exeggutor 43 / Pidgeot 44 / Growlithe 44 / 
Alakazam 46 / Blastoise 49 49
Ruta 22 II Rhyhorn 56 / Pidgeot 56 / Nidoking 57 / 
Alakazam 58 / Arcanine 59 / Blastoise 61 61
Campeón Pidgeot 64 / Alakazam 65 / Nidoking 65 / 
Rhydon 66 / Arcanine 67 / Blastoise 69 69
Revancha Nidoqueen80 / Magmar80 / Golem81 / 
Scizor82 / Arcanine83 / Blastoise85 85
IV de Gary: 0 6 10 12 14 18 24 28; Blastoise Campeón 30. Revancha: base 29, Blastoise 30. La hoja → → → → → → →
`Gary` fija también los movesets tempranos legales.
14. Arquitectura de guardado y estados
Zona Uso Full
SaveBlock1 size Se mantiene 0x3D68.
0x348C..0x361B (400 bytes) 100 ItemSlot extra del bolsillo normal.
0x3D24..0x3D33 (16 bytes) Header Full: magic RFFL + schemaVersion=1 + reservado.
Flags 0x8C3–0x8E2 Namespace reservado Full (32 flags).
Vars 0x408C–0x409B Namespace reservado Full (16 vars).
struct Roamer Reutilizado; una bestia activa.
<PARSED TEXT FOR PAGE: 8 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
Asignaciones iniciales: flags de elección/premio Dojo; KO pendiente de las tres aves y Mewtwo; captured/KO de 
Mew y Celebi. Vars: Mystic quest, Aurora quest, Mew quest, Celebi quest y secuencia de roamers. El resto del 
bloque queda reservado.
Si un save no contiene el magic Full, se inicializa como schema 0: los 100 ItemSlot extra se ponen a vacío y se 
escribe el header, sin alterar campos estándar. Esto es robustez de importación; no convierte el round-trip con 
vanilla en una función soportada.
15. Correcciones técnicas
Bug / seguridad Acción
Setter IV roamer Leer/escribir los 4 bytes correctamente.
Rugido roamer No desactivar permanentemente.
Status roamer Corregir tamaño de dato.
Pokédex pesca OOB Índice correcto de tabla de pesca.
Trade Egg check Condición BUGFIX.
Recalc HP Pokémon vivo se clampa a mínimo 1 PS.
Move Reminder scroll Corregir ID del segundo indicador.
L=A key repeat Corregir comparación remapeada.
Party menu leak Liberar buffers.
Berry Crush sparkle Corregir campo usado.
UBFIX general Mantener correcciones de seguridad del build moderno.
16. Compatibilidad
 No se añaden IDs nuevos de especies, movimientos ni objetos.
 Pokemon y BoxPokemon mantienen layout vanilla: PID, OT, IV, EV, moves, item, etc.
 El split cambia cómo Full interpreta un movimiento en batalla, no el dato almacenado; al intercambiar a 
vanilla, el juego receptor aplica sus propias reglas.
 Se conserva la restricción de link pre-Nacional para huevos/no-Kanto.
 mGBA link será parte de la regresión oficial.
17. Criterios de aceptación y producción
La matriz de implementación contiene 154 requisitos y la matriz QA contiene 139 casos. Ningún bloque se 
considera terminado solo porque compile.
 Build limpio del target español moderno.
 Smoke test funcional.
 QA vinculados PASS.
 Validador de sets PASS si se tocaron entrenadores/moves.
 Sin regresiones conocidas del bloque.
 Matriz y Decision Log actualizados.
17.1 Orden recomendado
1. Baseline/toolchain y bugfixes upstream.
2. Infraestructura de save Full + bag + namespaces.
3. Split/contacto/UI/IA.
<PARSED TEXT FOR PAGE: 9 / 9>
Pokémon Rojo Fuego Full — Especificación de Preproducción v1.0
Freeze 2026-09-19 · Producción no iniciada
4. Evoluciones + National Dex.
5. QoL (MT/tutores/recordador/repel/running/EV/Synchronize).
6. Safari y encuentros.
7. Economía.
8. Fósiles/Dojo.
9. Legendarios estáticos + HOF respawn.
10. Roamers.
11. Mystic/Aurora/Mew/Celebi.
12. Jefes/Gary/Liga.
13. Link/trade + regresión completa.
18. Estado del freeze
PREPRODUCCIÓN v1.0: CONGELADA.
No quedan decisiones de diseño mayores abiertas. Durante producción pueden aparecer incidencias técnicas; 
deben resolverse respetando la especificación. Cualquier mejora nueva de diseño se registra como propuesta y 
no se incorpora sin aprobación.
Archivos asociados: matriz XLSX, Decision Log y Prompt Maestro de Producción.