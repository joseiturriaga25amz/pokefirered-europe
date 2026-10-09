PewterCity_Gym_Text_BrockIntro::
    .string "¡Soy BROCK, LÍDER de PLATEADA!\p"
    .string "La roca resiste golpes, pero\ntambién exige disciplina.\p"
    .string "Mis POKéMON no retrocederán.\p"
    .string "¡Demuéstrame de qué está hecho\ntu equipo!{PLAY_BGM}{MUS_ENCOUNTER_GYM_LEADER}$"

@ NOTE: This defeat text actually causes a buffer overflow. It's too long for the gDisplayedStringBattle
@ buffer that it's put into, and it stomps all over the gBattleTextBuffs after, as well as the otherwise
@ unused array after that, sFlickerArray. Perhaps that's the reason why said array exists.
PewterCity_Gym_Text_BrockDefeat::
    .string "Te he subestimado.\p"
    .string "¡Como prueba de tu victoria, aquí\n"
    .string "tienes la MEDALLA ROCA!\p"
    .string "{FONT_NORMAL}¡{PLAYER} obtuvo la MEDALLA ROCA!{PAUSE_MUSIC}{PLAY_BGM}{MUS_OBTAIN_BADGE}{PAUSE 0xFE}{PAUSE 0x56}{RESUME_MUSIC}\p"
    .string "{FONT_MALE}¡Es una MEDALLA oficial de la LIGA\n"
    .string "POKéMON!\p"
    .string "¡Hará que tus POKéMON sean\n"
    .string "mucho más fuertes!\p"
    .string "¡Y la técnica del DESTELLO podrá\n"
    .string "ser utilizada en todo momento!$"

PewterCity_Gym_Text_TakeThisWithYou::
    .string "Un último consejo antes de irte.\n¡Llévate esta MT!$"

PewterCity_Gym_Text_ReceivedTM39FromBrock::
    .string "¡{PLAYER} obtuvo la MT39\n"
    .string "de manos de BROCK!$"

PewterCity_Gym_Text_ExplainTM39::
    .string "La MT39 contiene TUMBA ROCAS.\p"
    .string "Golpea y reduce la VELOCIDAD\ndel rival. Úsala con cabeza.\p"
    .string "¡Puedes usar una MT tantas\nveces como quieras!\p"
    .string "¡Prueba nuevas estrategias!$"

PewterCity_Gym_Text_BrockPostBattle::
    .string "Has demostrado algo más que\nfuerza: sabes mantenerte firme.\p"
    .string "Ahora sigue hacia CELESTE.\n¡Aún te espera mucho camino!$"

PewterCity_Gym_Text_DontHaveRoomForThis::
    .string "Tu mochila está llena.\nHaz sitio y vuelve a hablarme.$"

PewterCity_Gym_Text_LiamIntro::
    .string "¡Alto ahí, enclenque!\p"
    .string "¡Todavía estás a años luz de retar\n"
    .string "a BROCK!$"

PewterCity_Gym_Text_LiamDefeat::
    .string "¡Vaya!\p"
    .string "¡Años luz no suponen tiempo!\n"
    .string "¡Miden distancia!$"

PewterCity_Gym_Text_LiamPostBattle::
    .string "¡Eres bastante fuerte, pero no\n"
    .string "tanto como BROCK!$"

PewterCity_Gym_Text_LetMeTakeYouToTheTop::
    .string "¡Puedo decirte lo que se requiere\n"
    .string "para ser un campeón de POKéMON!\p"
    .string "¡No soy ENTRENADOR, pero puedo\n"
    .string "decirte cómo ganar!\p"
    .string "¡Déjame que te lleve a la\n"
    .string "victoria!$"

PewterCity_Gym_Text_LetsGetHappening::
    .string "¡Muy bien!\n"
    .string "¡Vamos allá!$"

PewterCity_Gym_Text_TryDifferentPartyOrders::
    .string "¡El 1.{SUPER_ER} POKéMON que sale a luchar\n"
    .string "es el primero de la LISTA\l"
    .string "de los POKéMON!\p"
    .string "¡Cambiar el orden de los POKéMON\n"
    .string "podría facilitarte las cosas\l"
    .string "en combate!$"

PewterCity_Gym_Text_ItsFreeLetsGetHappening::
    .string "¡Es gratis!\n"
    .string "¡Venga!$"

PewterCity_Gym_Text_YoureChampMaterial::
    .string "¡Lo sabía!\n"
    .string "¡Tienes madera!$"

PewterCity_Gym_Text_GymStatue::
    .string "LÍDER del GIMNASIO POKéMON\n"
    .string "de PLATEADA: BROCK\p"
    .string "ENTRENADOR GANADOR:\n"
    .string "{RIVAL}$"

PewterCity_Gym_Text_GymStatuePlayerWon::
    .string "LÍDER del GIMNASIO POKéMON\n"
    .string "de PLATEADA: BROCK\p"
    .string "ENTRENADORES GANADORES:\n"
    .string "{RIVAL} y {PLAYER}$"
