# Pokémon Rojo Fuego Full — Decision Log v1.0

**Fecha de freeze:** 2026-09-19  
**Estado:** preproducción congelada; producción aún no iniciada.

Este archivo registra las decisiones vigentes. Si una conversación previa contradice este documento, prevalece la decisión más reciente aquí registrada, salvo que el usuario apruebe explícitamente una modificación posterior.

| ID | Tema | Decisión | Racional | Estado |
|---|---|---|---|---|
| D-001 | Filosofía | Mantener FireRed reconocible; quitar fricción artificial y dependencias externas. | Modernización selectiva, no remake. | CERRADA |
| D-002 | Especies | V1.0 limitada a Gen I–III (#001–386). | Compatibilidad Gen III y alcance controlado. | CERRADA |
| D-003 | IDs | No crear nuevos IDs de Pokémon, movimientos ni objetos. | Prioriza trading seguro y futuro Emerald Full. | CERRADA |
| D-004 | MO | Mantener sistema original de MO. | El usuario no considera sustancial la modernización. | CERRADA |
| D-005 | Split | Adoptar split físico/especial por movimiento. | Mejora coherencia sin importar stats/moves modernos. | CERRADA |
| D-006 | Contacto | Usar contacto moderno independiente de categoría. | Evita incoherencias con habilidades. | CERRADA |
| D-007 | Datos moves | Categoría/contacto modernos; potencia/precisión/PP/efectos Gen III. | Regla híbrida explícita. | CERRADA |
| D-008 | Learnsets | Solo corregir víctimas severas del split. | Evita rebalance masivo. | CERRADA |
| D-009 | Arbok | Añadir Colmillo Veneno por nivel. | STAB físico razonable. | CERRADA |
| D-010 | Banette/Shedinja | Sustituir Bola Sombra por Puño Sombra en nivel; MT30 queda. | Compensación mínima del split. | CERRADA |
| D-011 | MT | MT reutilizables, máximo una copia, no vender/tirar. | QoL sin crear IDs. | CERRADA |
| D-012 | Recordador | $2.000 por movimiento. | Quita farmeo de setas. | CERRADA |
| D-013 | Tutores | Primera vez gratis; luego precio fijo. | Renovabilidad con coste. | CERRADA |
| D-014 | Correr | Permitir correr en interiores tras zapatillas. | QoL menor y segura. | CERRADA |
| D-015 | Repel | Prompt de auto-reuso. | Reduce fricción. | CERRADA |
| D-016 | Bolsa | 142 slots en bolsillo normal usando 400 bytes unused. | Elimina límite práctico sin mover offsets. | CERRADA |
| D-017 | EV UI | Mostrar EVs en resumen con toggle. | Apoya crianza/entrenamiento del usuario. | CERRADA |
| D-018 | Synchronize | 50% naturaleza salvaje como Emerald. | QoL de captura sin alterar combate. | CERRADA |
| D-019 | Safari | Sin límite de pasos; 30 Safari Balls mantienen fin. | Quita tedium sin borrar minijuego. | CERRADA |
| D-020 | Trade evolutions | Kadabra/Machoke/Graveler/Haunter evolucionan al 36. | Autosuficiencia single-save. | CERRADA |
| D-021 | Held evolutions | Trade-item evolutions pasan a uso directo del objeto. | Elimina dependencia de trade. | CERRADA |
| D-022 | Eevee | Piedra Solar→Espeon; Piedra Lunar→Umbreon. | No hay reloj funcional para day/night. | CERRADA |
| D-023 | National Dex | Permitir evoluciones Gen II/III pre-Nacional pero ocultar Dex Nacional hasta Oak. | Separa mecánica de UI/progresión. | CERRADA |
| D-024 | Trade pre-Nat | Conservar restricciones vanilla de link pre-Nacional. | Compatibilidad FRLG. | CERRADA |
| D-025 | Exclusivas LG | Integrarlas en hábitats oficiales LG sin reemplazar toda tabla FR. | Preserva identidad FireRed. | CERRADA |
| D-026 | Iniciales | Bulbasaur/Charmander/Squirtle y evoluciones salvajes con tasas 15/5/4%. | Autosuficiencia y rareza controlada. | CERRADA |
| D-027 | Eevee | Eevee 15% Ruta 7; Vaporeon/Jolteon/Flareon 4% en hábitats temáticos. | Reduce dependencia de regalo único. | CERRADA |
| D-028 | Fósiles | Segundo fósil por excavación tras revivir el primero. | Conserva la elección inicial temporal. | CERRADA |
| D-029 | Dojo | Segundo combate tras Sabrina; premio = Hitmon no elegido. | Completa Pokédex sin invalidar elección temprana. | CERRADA |
| D-030 | Changing Cave | Restaurar las 9 tablas mediante investigador selector. | Usa contenido original ya programado. | CERRADA |
| D-031 | Legendarios estáticos | Huida reentra; KO respawn tras HOF; captura permanente. | Evita pérdidas accidentales sin trivializar. | CERRADA |
| D-032 | Roamers | Suicune→Raikou→Entei secuenciales, una activa. | Cabe en struct Roamer existente. | CERRADA |
| D-033 | Roamer KO/Roar | KO reactiva misma identidad; Rugido no borra. | Corrige frustraciones/bugs. | CERRADA |
| D-034 | MysticTicket | Quest Celio tras Network + 3 aves capturadas. | Sustituye distribución externa con lore mínimo. | CERRADA |
| D-035 | AuroraTicket | Celio→Museo Pewter→Celio. | Sustituye distribución externa manteniendo Birth Island. | CERRADA |
| D-036 | Deoxys | Birth Island original, Attack Forme, Nv.50. | Evento original con nivel ajustado. | CERRADA |
| D-037 | Mew | Mansion hide-and-seek tras capturar Mewtwo; Nv.50 fateful. | No importar Faraway Island. | CERRADA |
| D-038 | Celebi | Berry Forest tras National + Network + 3 bestias; Nv.50. | Cierra hilo Johto sin mapa nuevo. | CERRADA |
| D-039 | Hoenn legends | No incluir Jirachi/Latios/Latias/Regis/Groudon/Kyogre/Rayquaza. | Reservados a Emerald Full. | CERRADA |
| D-040 | Economía | Sin multiplicador global de dinero. | Ajustes localizados. | CERRADA |
| D-041 | Type boosters | 16 potenciadores a $3.000, efecto Gen III 10%. | Acceso razonable sin buff moderno. | CERRADA |
| D-042 | Porygon | 5.000 fichas, repetible. | Living Dex y menor grind. | CERRADA |
| D-043 | Lucky Egg | Método Chansey + tienda postgame $30.000. | Renovable sin quitar método clásico. | CERRADA |
| D-044 | Gary | Siempre Squirtle/Blastoise como ace. | Híbrido natural anime + FireRed. | CERRADA |
| D-045 | Gary roster | Plantilla rotativa; no exigir mostrar preevolución de cada miembro. | Gary anime captura y rota mucho. | CERRADA |
| D-046 | Gary Champion | Pidgeot/Alakazam/Nidoking/Rhydon/Arcanine/Blastoise. | Cinco piezas FireRed + Nidoking anime. | CERRADA |
| D-047 | Gary dificultad | Ace 5→12→22→28→34→49→61→69; IV progresivos. | Cada encuentro debe sentirse como jefe. | CERRADA |
| D-048 | Líderes | Equipos anime/históricos con dificultad moderada, no hardcore. | Identidad temática + reto razonable. | CERRADA |
| D-049 | Rematches | Repetibles indefinidamente, roster histórico hasta Gen III. | Postgame con identidad. | CERRADA |
| D-050 | Curación bosses | Máximo 2 curaciones; Champion no usa 4 Full Restores. | Evita desgaste artificial. | CERRADA |
| D-051 | IV bosses | Curva progresiva; no 31 universal. | Dificultad transparente sin EV ocultos. | CERRADA |
| D-052 | Naturalezas bosses | No optimizar competitivamente. | Evita minmax oculto. | CERRADA |
| D-053 | IA | Mantener núcleo probado de FRLG, hacerlo split-aware. | Robustez sobre complejidad. | CERRADA |
| D-054 | Bugfixes | Aprobar 8 bugs auditados + UBFIX/BUGFIX modernos. | Estabilidad técnica. | CERRADA |
| D-055 | Base | Producción en pokefirered-europe español; pret como upstream. | Evita traducción secundaria. | CERRADA |
| D-056 | Build | firered_es_modern; baseline SHA-1 verificado antes de cambios. | Reproducibilidad. | CERRADA |
| D-057 | Save | No mover offsets ni cambiar tamaño SaveBlock1. | Reduce riesgo/compatibilidad. | CERRADA |
| D-058 | Flags/vars Full | Reservar bloques unused 0x8C3–0x8E2 y 0x408C–0x409B. | Evita colisiones. | CERRADA |
| D-059 | Save header | Usar unused_3D24[16] para magic/schema; bag extra en unused_348C. | Migración y versionado. | CERRADA |
| D-060 | Trading | Trading Gen III es objetivo oficial; round-trip del mismo .sav con vanilla no. | Prioriza Pokémon, no save modded. | CERRADA |
| D-061 | Producción | No empezar código sin paquete v1.0 + matrices + QA + decision log + prompt. | Evita reinterpretación. | CERRADA |