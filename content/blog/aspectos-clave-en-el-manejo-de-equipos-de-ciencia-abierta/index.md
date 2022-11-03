<!--
.. title: Aspectos clave en el manejo de equipos de ciencia abierta
.. slug: aspectos-clave-en-el-manejo-de-equipos-de-ciencia-abierta
.. date: 2020-01-20
.. author: Rainer Palm
.. tags: open science
.. category: open science
.. link: 
.. description: 
.. type: text
-->

<!-- # Aspectos clave en el manejo de equipos de ciencia abierta -->
<!-- **Por Rainer Palm** -->

![header](../../../images/blog/aspectos-clave-en-el-manejo-de-equipos-de-ciencia-abierta/header.png)

Ya sea por temas de financiamiento, el uso de tecnologías de comunicación más avanzadas, o la necesidad de realizar proyectos interdisciplinarios, la investigación colaborativa es una práctica bastante frecuente. A pesar de el enfoque historico y el tratamiento en medios de comunicación, hacia descubrimientos individuales, y pese a la presencia de ciertos personajes carismáticos, la realidad hoy en dia es otra: la gran mayoría de los científicos trabajan dentro de grupos donde los involucrados aportan al resultado final gracias a la retroalimentación constante, a pesar de que muchas veces ni siquiera comparten la misma disciplina entre los investigadores involucrados. La eficiencia de la cooperación se hace notar por si sola, y la necesidad de dar resultados rápidos en proyectos cada vez más grandes, requiere de la creación de grupos con flujos de trabajos disciplinados y metodologías ágiles.

<!-- TEASER_END -->

Las prácticas de ciencia abierta (libre distribución de la información, disponibilidad de métodos, datos y herramientas usadas, colaboración abierta), son atractivas no solo por cuestiones éticas, sino también porque sirven de maravilla para el problema de organización de equipos. No solamente es bastante útil el uso de herramientas como Git para compartir codigo fuente y demás información dentro de un grupo pequeño de investigadores para que todos puedan trabajar desde lo mismo partiendo del mismo punto, sino que también el uso de los recursos compartidos libremente por otros y los posibles aportes o sugerencias de gente interesada en tu investigación puede resultar bastante significativo para tus proyectos.

¿Cuales son, entonces, las principales herramientas de una investigación colaborativa de ciencia abierta? Tomando en cuenta que necesitamos rapidez, disciplina, coordinación, y libre disponibilidad y colaboración entre todos los posibles integrantes de nuestro grupo, podemos afirmar que, por lo general, debemos usar las siguientes:

## Control de versiones

El uso de software de control de versiones y de plataformas que alojen sus respectivos repositorios en la nube (como Github, Gitlab, Docker, etc.) se ha vuelto bastante esencial no solamente para cuestiones de ciencia abierta, sino para desarollo de todo tipo de software, desde scripts pequeños de procesamiento de archivos hasta videojuegos o modelado 3D. La seguridad que te otorga el sistema de respaldo, el alojar tus archivos en la nube, y la facilidad con la que te deja colaborar con tus colegas, añadiendo juntos archivos y revisiones al repositorio de una forma organica, lo hace una herramienta indispensable para todo tipo de proyecto que utilize codigo.

El libre acceso a tus proyectos mediante sus repositorios facilita también la tareas de divulgación de tu trabajo, localización de  colaboradores, corregir errores en tu procedimiento, reproducir tu investigación, y añadir tus proyectos a tu curriculum.

## Manejo de equipos en tus repositorios

Muchas plataformas que utilizan control de versiones, suelen ofrecer también herramientas para el manejo de equipos como la creacion de cuentas, permitiendo restringir acceso a ciertas carpetas del repositorio, requerir que los cambios que hagan otros necesiten aprobación, la asignación de ciertos miembros del equipo para que revisen estos cambios, etc. Inclusive si no la poseen de manera explicita, organizar tu equipo de esta forma puede resultarte bastante beneficioso, especialmente si trabajas con colegas en distintas disciplinas. Sitios como Github también permiten anexar grupos, establecer una jerarquía clara entre grupos, administrar automáticamente la membresía del equipo de Github mediante un proveedor de identidad (o IdP, tal como Azure AD), además de ofrecer una plataforma donde pueden debatir y discutir. Aprovechar estas herramientas al maximo es crucial a la hora de organizar grupos que no puedan verse en persona.

## Metodología ágil

El método ágil se refiere principalmente a un conjunto de prácticas que implementan los principios descritos en el manifiesto ágil[1], creado en el 2001 por personas que querian innovar en los modos tradicionales de gestionar proyectos de software. En términos generales, estas metodologías intentan enfocar el desarollo del software hacia las necesidades de las personas y las interacciones cliente-desarollador, apuntando hacia la 'entrega temprana y continua de software con valor'. De esta forma, se logra mantener un desarollo constante, funcional y transparente, entregando software funcional regularmente mediante un flujo de trabajo sencillo y eficaz.

Existen múltiples implementaciones de este método, una de las más populares siendo Scrum[2], un framework de procesos ágiles diseñado para manejar problemas complejos y adaptativos sin sacrificar valor, creatividad o productividad. Principalmente pensado para equipos pequeños de 10 miembros o menos, reemplaza un acercamiento algorítmico preprogramado, por uno heurístico que valora la capacidad de las personas de adaptarse y auto-organizarse en torno a problemas complejos emergentes. Para este objetivo, busca girar el proceso de trabajo en torno a 'sprints' que duren alrededor de un mes, donde, tras un proceso de planificación, se crea un producto usable (llamado un 'incremento') y se realiza una revisión del sprint. Se trata de una de las mas famosas implementaciones gracias a que su efectividad ha sido comprobada empiricamente[3], y a pesar de que es comúnmente utilizado en empresas que desarollen software su uso en investigaciones científicas ya esta siendo explorado.

## Entrenamiento en políticas de ciencia abierta

Uno de los principales problemas a la hora de realizar proyectos de ciencia abierta es que, debido a su relativa novedad, muchas empresas e instituciones no tienen un esquema de trabajo o de políticas orientadas hacia su logro, mucho menos personas capacitadas en el área que puedan ayudar. Además, muchos científicos consideran que la forma más práctica de aprender a usar estas herramientas es trabajando con ellas.

Por lo tanto, es crucial para los proyectos de ciencia abierta capacitar a sus integrantes para desarollar implementaciones de estas políticas mientras trabajan, basándose en cómo se realizan en otras[4] instituciones[5] (ya sean empresas o gobiernos). Revisando temas de derechos de autor, propiedad intelectual, acceso abierto, o datos de investigación, aclarando la disponibilidad tanto de la investigación como los datos y métodos utilizados.

## Incentivo a la ciencia abierta

Muchos científicos pueden tener dudas respecto a los métodos de remuneración o el financiamiento que pueden recibir por una investigación que se ate a principios de ciencia abierta. Actualmente buena parte de la comunidad científica no conoce en detalle el concepto de ciencia abierta[6], y por lo general se toma el libre acceso a publicaciones como principal requerimiento para que una investigación sea 'abierta'. También, por lo general, desconocen si las instituciones de investigación y cuerpos de financiamiento tienen lineamientos y directrices en cuanto a acceso libre a las publicaciones se refiere.

Por lo tanto, es necesario para todo grupo o organización interesado en la realización de ciencia abierta establecer reglas y políticas claras, y altamente recomendado que establezcan incentivos (tales como criterios de contratación que busquen individuos anteriormente involucrados en investigaciones abiertas o incorporación de ciencia abierta en el desarollo, apoyo y evaluación de personal científico, que son recomendaciones de una organización danesa, National Platform Open Science[7]) para integrar mas investigadores dentro de esta esfera.

[1]: http://agilemanifesto.org/iso/es/manifesto.html "Manifiesto por el Desarrollo Ágil de Software"
[2]: https://www.scrum.org/ "Home | Scrum.org"
[3]: https://34slpa7u66f159hfp1fhl9aur1-wpengine.netdna-ssl.com/wp-content/uploads/2014/05/Scrum-CMMI-Going-from-Good-to-GreatAgile.pdf "Scrum and CMMI – Going from Good to Great"
[4]: https://www.openaire.eu/member-states-overview "Open Science overview in Europe"
[5]: https://ec.europa.eu/research/participants/data/ref/h2020/grants_manual/hi/oa_pilot/h2020-hi-oa-pilot-guide_en.pdf "Guidelines to the Rules on Open Access to Scientific Publications and Open Access to Research Datain Horizon 2020"
[6]: https://www.zbw-mediatalk.eu/2017/08/report-wie-bekommen-forschende-die-qualifikationen-fur-open-science/ "Open science report: How to provide the skills researchers need?"
[7]: https://www.openscience.nl/files/openscience/2019-02/notitie-erkennen-en-waarderen-van-onderzoekers_en-gb.pdf "Memo – Researcher Recognition and Rewarding"
