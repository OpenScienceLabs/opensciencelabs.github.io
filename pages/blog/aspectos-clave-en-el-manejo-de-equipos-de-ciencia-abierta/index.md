---
title: "Aspectos clave en el manejo de equipos de ciencia abierta"
slug: aspectos-clave-en-el-manejo-de-equipos-de-ciencia-abierta
date: 2020-01-20
author: Rainer Palm
tags: [investigación colaborativa]
categories: [organización, gestión de equipos]
description: |
  Ya sea por temas de financiamiento, el uso de tecnologías de comunicación más avanzadas, o la necesidad de realizar proyectos interdisciplinarios, la investigación colaborativa es una práctica bastante frecuente. A pesar del enfoque histórico y el tratamiento en medios de comunicación, hacia descubrimientos individuales, y pese a la presencia de ciertos personajes carismáticos, la realidad hoy en día es otra: la gran mayoría de los científicos trabajan dentro de grupos donde los involucrados aportan al resultado final gracias a la retroalimentación constante, por encima de que muchas veces ni siquiera comparten la misma disciplina entre los investigadores vinculados. La eficiencia de la cooperación se hace notar por si sola, y la necesidad de dar resultados rápidos en proyectos cada vez más grandes, requiere de la creación de grupos con flujos de trabajos disciplinados y metodologías ágiles.
draft: false
usePageBundles: true
thumbnail: "/header.png"
featureImage: "/header.png"
---


<!-- # Aspectos clave en el manejo de equipos de ciencia abierta -->
<!-- **Por Rainer Palm** -->

Ya sea por temas de financiamiento, el uso de tecnologías de comunicación más avanzadas, o la necesidad de realizar proyectos interdisciplinarios, la investigación colaborativa es una práctica bastante frecuente. A pesar del enfoque histórico y el tratamiento en medios de comunicación, hacia descubrimientos individuales, y pese a la presencia de ciertos personajes carismáticos, la realidad hoy en día es otra: la gran mayoría de los científicos trabajan dentro de grupos donde los involucrados aportan al resultado final gracias a la retroalimentación constante, por encima de que muchas veces ni siquiera comparten la misma disciplina entre los investigadores vinculados. La eficiencia de la cooperación se hace notar por si sola, y la necesidad de dar resultados rápidos en proyectos cada vez más grandes, requiere de la creación de grupos con flujos de trabajos disciplinados y metodologías ágiles.

<!-- TEASER_END -->

Las prácticas de ciencia abierta (libre distribución de la información, disponibilidad de métodos, datos y herramientas usadas, colaboración abierta), son atractivas no solo por cuestiones éticas, sino también porque sirven de maravilla para el problema de organización de equipos. Además del uso de herramientas como Git para compartir código fuente y la información dentro de un grupo pequeño de investigadores para que todos puedan trabajar partiendo del mismo punto, el uso de los recursos compartidos libremente por otros y los posibles aportes o sugerencias de gente interesada en tu investigación puede resultar bastante significativo para tus proyectos.

¿Cuáles son, entonces, las principales herramientas de una investigación colaborativa de ciencia abierta? Tomando en cuenta que necesitamos rapidez, disciplina, coordinación, y libre disponibilidad y colaboración entre todos los posibles integrantes de nuestro grupo, podemos afirmar que, por lo general, debemos usar las siguientes:

## Control de versiones

El uso de software de control de versiones y de plataformas que alojen sus respectivos repositorios en la nube (como Github, Gitlab, Docker, etc.) se ha vuelto bastante esencial tanto para cuestiones de ciencia abierta como para desarrollo de todo tipo de software, desde scripts pequeños de procesamiento de archivos hasta videojuegos o modelado 3D. La seguridad que te otorga el sistema de respaldo, el alojar tus archivos en la nube, y la facilidad con la que te deja colaborar con tus colegas, añadiendo juntos archivos y revisiones al repositorio de una forma orgánica, lo hace una herramienta indispensable para todo tipo de proyecto que utilice código.

El libre acceso a tus proyectos mediante sus repositorios facilita también las tareas de divulgación de tu trabajo, localización de colaboradores, corrección errores en tu procedimiento, reproducción de tu investigación, y añadir tus proyectos a tu curriculum.

## Manejo de equipos en tus repositorios

Muchas plataformas que utilizan control de versiones, suelen ofrecer también herramientas para el manejo de equipos como la creación de cuentas, permitiendo restringir acceso a ciertas carpetas del repositorio, los cambios que hagan otros necesitan aprobación, se pueden asignar miembros del equipo para que revisen los cambios, etc.
Si no posees de manera explícita esta forma organizar tu equipo, te cuento que puede resultarte bastante beneficioso, especialmente si trabajas con colegas en distintas disciplinas. Sitios como Github permiten anexar grupos, establecer una jerarquía clara entre grupos, administrar automáticamente la membresía del equipo de Github mediante un proveedor de identidad (o IdP, tal como Azure AD), además de ofrecer una plataforma donde pueden debatir y discutir. Aprovechar estas herramientas al máximo es crucial a la hora de organizar grupos que no puedan verse en persona.

## Metodología ágil

El método ágil se refiere principalmente a un conjunto de prácticas que
implementan los principios descritos en el [manifiesto
ágil](http://agilemanifesto.org/iso/es/manifesto.html), creado en el 2001 por
personas que querían innovar en los modos tradicionales de gestionar proyectos
de software. En términos generales, estas metodologías intentan enfocar el
desarrollo del software hacia las necesidades de las personas y las interacciones
cliente-desarrollador, apuntando hacia la 'entrega temprana y continua de
software con valor'. De esta forma, se logra mantener un desarrollo constante,
funcional y transparente, entregando software funcional regularmente mediante un
flujo de trabajo sencillo y eficaz.

Existen múltiples implementaciones de este método, una de las más populares siendo [Scrum](https://www.scrum.org/ ), un framework de procesos ágiles diseñado para manejar problemas complejos y adaptativos sin sacrificar valor, creatividad o productividad. Principalmente pensado para equipos pequeños de 10 miembros o menos, reemplaza un acercamiento algorítmico preprogramado, por uno heurístico que valora la capacidad de las personas de adaptarse y auto-organizarse en torno a problemas complejos emergentes. Para este objetivo, busca girar el proceso de trabajo en torno a 'sprints' que duren alrededor de un mes, donde, tras un proceso de planificación, se crea un producto usable (llamado un 'incremento') y se realiza una revisión del sprint. Se trata de una de las más famosas implementaciones gracias a que su efectividad ha sido comprobada empíricamente, para revisar esto puedes revisar el artículo [Scrum and CMMI – Going from Good to Great](https://sci-hub.se/10.1109/agile.2009.31). Scrum es comúnmente utilizado en empresas que desarrollan software, su uso en investigaciones científicas ya está siendo explorado.

## Entrenamiento en políticas de ciencia abierta

Uno de los principales problemas a la hora de llevar a cabo proyectos de ciencia abierta es que, debido a su relativa novedad, muchas empresas e instituciones no tienen un esquema de trabajo o de políticas orientadas hacia su logro, mucho menos personas capacitadas en el área que puedan ayudar. Además, una cantidad importante científicos consideran que la forma más práctica de aprender a usar estas herramientas es trabajando con ellas.

Por lo tanto, es crucial para los proyectos de ciencia abierta capacitar a sus integrantes para desarrollar implementaciones de estas políticas mientras trabajan, basándose en cómo se realizan en otras instituciones (ya sean empresas o gobiernos). Revisando temas de derechos de autor, propiedad intelectual, acceso abierto, o datos de investigación, aclarando la disponibilidad tanto de la investigación como los datos y métodos utilizados. Para leer más sobre esto puede visitar [Open Science overview in Europe](https://www.openaire.eu/member-states-overview) y [Guidelines to the Rules on Open Access to Scientific Publications and Open Access to Research Datain Horizon 2020](https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-pilot-guide_en.pdf).

## Incentivo a la ciencia abierta

Muchos científicos pueden tener dudas respecto a los métodos de remuneración o el financiamiento que pueden recibir por una investigación que se ate a principios de ciencia abierta. Actualmente buena parte de la comunidad científica no conoce en detalle el concepto de ciencia abierta, y por lo general se toma el libre acceso a publicaciones como principal requerimiento para que una investigación sea 'abierta'. También, desconocen si las instituciones de investigación y cuerpos de financiamiento tienen lineamientos y directrices en cuanto a acceso libre en cuanto a las publicaciones se refiere.

Por lo tanto, es necesario para todo grupo u organización interesado en la realización de ciencia abierta establecer reglas y políticas claras, y altamente recomendado que establezcan incentivos (tales como criterios de contratación que busquen individuos anteriormente involucrados en investigaciones abiertas o incorporación de ciencia abierta en el desarrollo, apoyo y evaluación de personal científico, que son recomendaciones de una organización danesa, [National Platform Open Science](https://www.openscience.nl/)) para integrar mas investigadores dentro de esta esfera.

Un artículo donde puedes leer más al respecto es [Open science report: How to provide the skills researchers need?](https://www.zbw-mediatalk.eu/2017/08/report-wie-bekommen-forschende-die-qualifikationen-fur-open-science/).

## Referencias

- Manifiesto por el Desarrollo Ágil de Software. (s. f.). http://agilemanifesto.org/iso/es/manifesto.html
- Home. (s. f.). Scrum.org. https://www.scrum.org/
- Jakobsen, C. R., & Sutherland, J. (2009). Scrum and CMMI Going from Good to Great. 2009 Agile Conference. doi:10.1109/agile.2009.31
- Open Science overview in Europe. OpenAire. https://www.openaire.eu/os-eu-countries
- "Guidelines to the Rules on Open Access to Scientific Publications and Open Access to Research Datain Horizon 2020" https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-pilot-guide_en.pdf
- Fingerle, B. (2022, 25 marzo). Open Science Report: How to Provide the Skills Researchers Need? ZBW MediaTalk. https://www.zbw-mediatalk.eu/2017/08/report-wie-bekommen-forschende-die-qualifikationen-fur-open-science/
- Open Science – Nationaal Programma Open Science. (s. f.). https://www.openscience.nl/
