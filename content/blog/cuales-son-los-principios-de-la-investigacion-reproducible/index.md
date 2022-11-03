<!--
.. title: ¿Cuáles son los principios de la investigación reproducible?
.. slug: cuales-son-los-principios-de-la-investigacion-reproducible
.. date: 2020-01-31
.. author: Rainer Palm
.. tags: open science
.. category: open science
.. link: 
.. description: 
.. type: text
-->

<!-- # ¿Cuáles son los principios de la investigación reproducible? -->
<!-- **Por Rainer Palm** -->

¿Como puedes tener total confianza y seguridad en que tu metodología es sensata, y de que tu investigación ha dado resultados certeros y facil de verificar? ¿Son veraces los estudios y descubrimientos de otros científicos?

<!-- TEASER_END -->

Ciertamente, la capacidad de validar y repetir el proceso llevado a cabo por los investigadores es algo crucial a la hora de responder estas preguntas. Nos encontramos en un momento historico en el que podemos, mediante tecnologías digitales, acercarnos cada vez mas a satisfacer un criterio infalible de reproducibilidad en algunas areas (como la ciencia de datos). Escribir cada uno de los pasos realizados ya es una practica inherente al proceso de investigación en sí, debido a la necesidad de coordinar proyectos en los que colaboran cientos de personas, y al desarrollo de software que permite grabar y  compartir este proceso de una forma eficiente y completa.

Aun así, paradojicamente, nos encontramos también en medio de una crisis en las ciencias, donde los resultados de una gran cantidad de experimentos son dificiles o imposibles de replicar \[1\], ya sea debido a ciertos limites en la investigación en sí o por otras razones. Siendo la reproducibilidad uno de los pilares del método científico como tal, estos dos hechos, tomados juntos, se hacen algo desconcertantes. Quizás sea importante repasar exactamente que consideramos como investigación reproducible y cuales son sus principios o metas, y que iniciativas o herramientas hay para asegurar esa condición.

## ¿Qué hace reproducible una investigación?

Podemos llamar a una investigación reproducible si ésta puede ser repetida por otros. En términos estrictos, esto simplemente significa que, contando con las herramientas necesarias, cualquiera puede tomar la descripción o grabación del experimento o estudio en cuestión para volverlo a realizar y verificar si el resultado es el mismo o lo suficientemente parecido (en tal caso, se dice que los resultados son replicables).

Para que una investigación sea reproducible, por ende, se requiere que sus métodos, datos, herramientas y configuración, sean descritos de una forma detallada y precisa, dependiendo del área de conocimiento, y que esta información sea legible tanto por un ser humano como por una computadora. Esto, obviamente, se complica cada vez más dependiendo del tamaño de la investigación y su complejidad. Ciertas herramientas, como [Jupyter](https://jupyter.org), permiten realizar el analísis y, a la vez esquematizan y muestran comentarios sobre los pasos del experimento, dentro de un mismo entorno de trabajo, lo cual ayuda bastante. Sín embargo, al final del dia esto depende primordialmente de las decisiones que tome el investigador, y no hay ninguna herramienta que garantiza la reproducibilidad simplemente por ser usada.

En ese caso, ¿en torno a qué aspectos deberían tomar las decisiones los usuarios? ¿Cuáles preceptos éticos deben seguir para dirigirse hacia una investigación reproducible? En la siguiente sección hablaremos de los principios de la investigación reproducible.

## Cuales són los principios de la investigación reproducible?

- **Transparencia**. Es importante recordar que, tal como cualquier otra cosa que te puedas imaginar (la realización de un plato de cocina, una canción, una pintura, etc.), sólo se puede decir que una investigación es reproducible si se pueden ver y entender los pasos que llevaron a su realización. Si realizas análisis de datos o elaboras algún tipo de código, por ejemplo, es necesario que tengas disponible toda la información referente al entorno (paquetes, configuraciones, carpetas del proyecto, dependencias, etc.) gracias a los cuales ejecutar el código, además de que es necesario que esté comentado rigurosamente para que otros puedan entender exactamente por qué funciona.

- **Métodologia abierta.** Siendo la ciencia una práctica colaborativa, es de bastante importancia mantener un alto grado de transparencia, como anteriormente mencionamos. Es importante también añadir que obligarte a compartir el procedimiento que llevaste a cabo no sólo te da mas confianza a la hora de compartir tus resultados, sino que también te anima a revisar cada paso dado y pensar si fue el correcto (y permite a otros verificar lo mismo, también).

- **Enlazamiento de los resultados a los datos iniciales.** Una investigación reproducible sistematiza su procedimiento de forma tal que se pueden ver claramente los datos de entrada, como estos fueron generados y por que proceso se analizan estos, ademas de hacerlos disponibles libremente (en cuanto sea aplicable). De esta forma, se traza una ruta desde los datos de salida hacia los de entrada, y viceversa.

Estos tres principios se pueden aplicar independientemente del tipo de investigación. Claramente, será mucho más fácil compartir un entorno virtual que el Acelerador de partículas (en inglés Large Hadron Collider, LHC), pero lo importante es hacer tanto los datos como detalles respecto a la forma en la que fueron generados libremente disponibles, haciendo el experimento repetible, y por tanto, verificable por la comunidad científica.

##Que herramientas hay para realizar investigación reproducible?

Sin duda, independientemente del tipo de trabajo que estés realizando, existe una variedad de opciones de software para lidiar con el problema de documentar, archivar, y esquematizar datos y archivos de una forma limpia y organizada, sin necesidad de tardar muchas horas describiendo estos en texto plano. Según Stodden et. al (2013)\[2\], hay cuatro tipos generales de herramientas en uso:

- **Computación autoría y publicación alfabetizada.** Ésta describe herramientas que permiten la creación de documentos que integran elementos rich media (codigo y demás) junto a texto (por lo general en Markdown o LaTeX) y demas archivos multimedia para presentar reportes que generan resultados tanto visuales como textuales en tiempo real. En este ambito, sin duda una de las mas populares es Jupyter, que soporta una cantidad abrumadora de lenguajes de programación (principalmente Julia, Python y R) sin perder sencillez o intuitividad.

- **Control de versiones.** Se refiere a aquellas herramientas que te permiten rastrear tu trabajo a lo largo del tiempo, tomando registro de los cambios y evoluciones que toma. De esta forma, permiten tanto volver a un punto anterior en el analísis sin empezar desde cero, como observar como cambia la investigación y las ideas referentes a ella cronologicamente. El sistema de control de versiones git es sin duda el mas popular, con una variedad de servicios web disponibles dependiendo de tus necesidades (tales como GitHub o Gitlab).

- **Registro de procedencia de los datos.** Procedencia se refiere a mantener un registro de la cronologia y historia de los objetos de investigación, tales como datos, codigo fuentes, figuras, y resultados. Entre estas herramientas estan VisTrails, Kepler y Taverna.

- **Herramientas que capturan y preservan un entorno de software.** Algo increiblemente importante pero a la vez dificil y complicado de hacer es instalar y configurar una red de versiones especificas de  dependencias, paquetes y herramientas para uso compartido entre tus colaboradores. Existen varios niveles de virtualización disponibles para llevar a cabo esta tarea, tanto la emulación completa de un entorno virtual especifico (como lo hacen Virtualbox of VMWare) o nada mas la creación de instancias separadas de espacios de usuario (como Docker).

\[1\] https://www.displayr.com/what-is-the-replication-crisis/
\[2\] http://stodden.net/icerm_report.pdf
