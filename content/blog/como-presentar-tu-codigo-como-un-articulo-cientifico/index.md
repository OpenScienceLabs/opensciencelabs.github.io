<!--
.. title: ¿Cómo presentar tu código como un artículo científico?
.. slug: como-presentar-tu-codigo-como-un-articulo-cientifico
.. date: 2020-03-04
.. author: Rainer Palm
.. tags: science
.. category: science
.. link: 
.. description: 
.. type: text
-->

<!-- # ¿Cómo presentar tu código como un artículo científico? -->
<!-- **Por Rainer Palm** -->

![header](../../../images/blog/como-presentar-tu-codigo-como-un-articulo-cientifico/header.png)

Muchos científicos emplean la creación de software cuando desarollan sus investigaciones, usando herramientas tales como scripts y simulaciones, personalizadas y adaptadas a sus necesidades. En los casos en que no es así, igual la mayoría termina empleando analísis computacional de alguna manera, con software prediseñado para graficar, realizar calculos elementales, visualizar estadísticas o datos que luego se mostrarán dentro de la presentación de su investigación. Sea como sea, lo cierto es que cada vez el rol del desarrolador y el del científico estan más relacionados, exigiendo que estas dos disciplinas se vinculen de forma más estrecha.

<!-- TEASER_END -->

Lo que hace esto mucho más interesante es el hecho de que el desarrollo de software está íntimamente involucrado en múltiples áreas de investigación, no sólo porque se utiliza como herramienta, si no de que este desarrollo en sí y los resultados que ofrece pueden traducirse en un problema a abarcar por un estudio. Este es un acercamiento utilizado frecuentemente en papers que tratan temas tales como simulaciones computacionales de procesos químicos variados, aplicaciones posibles de algoritmos de inteligencia artificial y comportamiento de esta en ámbitos particulares, problemas de lógica, y muchos otros más, involucrando una inmensa cantidad de ramas de la ciencia e incluso fuera de esta!

Si tienes un proyecto de desarrollo de software cualquiera relacionado con la ciencia, así sea nada más una herramienta creada durante tu investigación, quizás sea oportuno buscar la forma de publicarlo, posiblemente adjunto a un paper mas extenso. Hay muchas razones por las cuales lo deberias hacer, independientemente del propósito principal de tu trabajo (divulgación del conocimiento, estandares de reprodubilidad, dejar que los demas aprendan de tu trabajo, etc.), y la labor requerida es prácticamente nula si ya te has tomado el tiempo de escribir y documentar mínimamente tu codígo. Inclusive si consideras que tu código no es lo suficientemente bonito como para publicarse, le podría servir a alguien, así sea nada más para verificar tu investigación.

## Documentación del proceso de desarrollo

Para mostrar posibles usos de tu software, dar a conocer el razonamiento de tus meétodos, y ayudar a entender por qué tu código funciona, es muy importante que, preferiblemente durante el proceso de desarrollo, te tomes el tiempo de escribir de forma rigurosa una documentación que describa con profundidad tanto los pasos que has tomado a lo largo del proyecto, como por qué has pensado que esa ha sido la mejor forma de llevar a cabo tus metas. Esto implica decir con exactitud cuáles herramientas, lenguajes de programación, librerias, scripts, etc., has utilizado, así como dar un recuento de los problemas, tanto conceptuales como prácticos, encontrados durante el desarrollo, trazando un marco de referencia para el funcionamiento de tu código, y por supuesto, mencionar fundamentos de tu investigación, estudios y artículos anteriores escritos sobre problemas relacionados con el tema.

El uso de diagramas o esquemas para representar el modelado analítico de los problemas en cuestión o para ilustrar de una forma mas abstracta o intuitiva el funcionamiento del programa, es bastante útil a la hora de ayudar a otros entender como funciona, y es importante si piensas luego presentar tu trabajo en ámbitos menos formales.

## Visualización de resultados

Como extensión de lo que se dijo antes, puedes pensar en formas en las cuales se puede visualizar tu código, ya sea mediante una simulación en tiempo real, visualizaciones de estadísticas creadas con herramientas como R Studio, creación de interfaces gráficas u otros métodos, siempre teniendo las particularidades de tu investigación en mente. Con esto logras un mayor grado de accesibilidad y se te hace más fácil divulgar el fruto de tus labores, presentando tus conclusiones de una forma más atractiva sin perder credibilidad. Además, si presentas tu código dentro de un notebook con Jupyter o una herramienta similar, puedes hacer que tus lectores interactúen con tu código de una manera directa, sin mucha complicación, ejecutándolo en tiempo real desde una interfaz web y generando gráficas de manera inmediata.

## Publicación de datos y codigo junto al paper

Además de subir tu código junto a tu artículo en repositorios de Git o Docker, puedes usar sitios como IEEE DataPort [1] para subir bases de datos para que cualquiera pueda acceder a ellos de una forma sencilla, siendo los conjuntos de datos asignados un DOI para identificarlos rápidamente. Por lo general, subirlos a un archivo de datos de investigación te proveerá con referencias y identificadores persistentes, sin importar que luego actualices los archivos subidos. Si no es así, puedes usar Zenodo[2] o Figshare[3] para crear una copia permanente y citable, con un identificador DOI, de la versión actual de tu repositorio. Agregar las citas al propio software es también una opción.

Recuerda además siempre revisar con cuidado los lineamientos del journal para el cual estes pensando escribir, teniendo en cuenta como les será mas fácil acceder y reproducir tu código. Si subes tu código y datos para que puedan ser vistos por cualquiera, deberías también declarar abiertamente sus términos de uso, licencias y demás.

[1]: https://ieee-dataport.org/ "IEEE DataPort"
[2]: https://zenodo.org/ "Zenodo"
[3]: https://figshare.com/ "Figshare"
