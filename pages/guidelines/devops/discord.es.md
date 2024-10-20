---
title: Discord
slug: discord-es
date: 2019-04-08
authors: ["Ivan Ogasawara"]
tags: ["devops", "discord"]
category: ["devops"]
---

<!-- # [ES] Discord -->

Discord es nuestra principal herramienta de comunicación con la comunidad. El
enlace directo a nuestro discord es [/discord](/discord).

## Convenciones

Cada canal tiene un nombre único con un prefijo, según la categoría. Por
ejemplo, un canal dentro de la categoría Python comienza con el prefijo `py-`.

Algunos nombres de categorías son largos y a veces es difícil encontrar un
prefijo para eso. Pero, es importante que el prefijo tenga alguna relación con
la categoría.

## Configuración

Por determinar

## Bots

Utilizamos bots para ayudar a mantener nuestro servidor.

### MEE6

Para la clasificación estamos utilizando **MEE6**. No tenemos ninguna actividad
ni ninguna recompensa utilizando la puntuación de la clasificación, pero tal vez
en el futuro podamos utilizarla.

### Dyno

**Dyno bot** se utiliza para tareas de mantenimiento, tales como:

- Mensaje de bienvenida
- Prohibir usuarios
- Bloquear usuarios
- etc

### YAGPDB.xyz

El bot **YAGPDB.xyz** se utiliza para la suscripción en categorías.

Para más información de cómo utilizarlo, consulte el siguiente tutorial:

https://docs.yagpdb.xyz/tools-and-utilities/self-assignable-roles

Cuando tengas el grupo y los roles configurados en **YAGPDB.xyz**, el siguiente
paso es crear un mensaje personalizado en **discord**, en el canal que quieras
tener este mecanismo de suscripción.

1. En el mensaje, añade un título, una descripción general y los emoticones y
   sus significados (https://unicode.org/emoji/charts/full-emoji-list.html).

2. Obtén el ID del mensaje (necesitas activar el modo de desarrollo).

3. Ejecuta el siguiente comando
   `!yagpdb-rolemenu create (group name) -m (message id) -nodm`, donde
   `(group name)` y `(message id)` son marcadores de posición y deben ser
   reemplazados por los valores correctos.

**Nota**: Una alternativa a **yagpdb** sería
[**carl-bot**](https://top.gg/bot/235148962103951360). Pero por ahora,
**yagpdb.xyz** parece funcionar correctamente según nuestras necesidades.

## Desarrollo

Tenemos un canal interno para discusiones sobre discord:
`#collab-devops-discord`.

Además, hay un servidor de discord para desarrollo donde podemos probar bots,
nuevas configuraciones o nuevas características.

Si quieres unirte a ese servidor, necesitas pedirlo en el canal
`#collab-devops-discord`.
