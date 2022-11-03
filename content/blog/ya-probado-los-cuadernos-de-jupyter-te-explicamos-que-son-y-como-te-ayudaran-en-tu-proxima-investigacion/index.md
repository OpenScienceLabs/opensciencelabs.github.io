<!--
.. title: ¿Ya has probado los Cuadernos de Jupyter? Te explicamos qué son y cómo te ayudarán en tu próxima investigación.
.. slug: ya-probado-los-cuadernos-de-jupyter-te-explicamos-que-son-y-como-te-ayudaran-en-tu-proxima-investigacion
.. date: 2020-01-13
.. author: Rainer Palm
.. tags: open science
.. category: jupyter
.. link: 
.. description: 
.. type: text
-->

<!-- # ¿Ya has probado los cuadernos de Jupyter? Te explicamos qué son y cómo te ayudarán en tu próxima investigación. -->
<!-- **Por Rainer Palm** -->

![header](../../../images/blog/ya-probado-los-cuadernos-de-jupyter-te-explicamos-que-son-y-como-te-ayudaran-en-tu-proxima-investigacion/header.png)

¿Quieres cambiar tus artículos a un formato más intuitivo, legible y
fácil de editar? Si tu respuesta es sí, puedes hacerlo con los [Jupyter
Notebook](https://jupyter.org), una aplicación web que permite
incorporar código y texto a los documentos de una forma sencilla y
fluida; facilitando que otras personas colaboren en tu investigación.
Utilizar estos elementos permitirá ver la descripción y resultados de tu
analísis de una forma más gráfica y en tiempo real, algo especialmente
útil para garantizar la reproducibilidad de tus resultados.

<!-- TEASER_END -->

El uso de Jupyter Notebook es bastante común en las comunidades
científicas actuales: por ejemplo, la creación de la foto de un agujero
negro utilizó un cuaderno de Jupyter cuyo código está en [este
repositorio de GitHub](https://github.com/achael/eht-imaging). Así como
este, existe una gran variedad de ejemplos de uso de cuadernos de
Jupyter en todo tipo de áreas, los cuales usualmente están disponibles
en un repositorio público de [GitHub](https://github.com). Veamos a
continuación, con más profundidad, de qué se trata esta aplicación.

## ¿Qué es Jupyter?

Jupyter se refiere a la organización de código abierto sin fines de
lucro llamada **Project Jupyter**, que es la principal organización que
desarolla una multitud de proyectos, entornos de ejecución
principalmente en [Julia](https://julialang.org),
[Python](https://www.python.org) y [R](https://www.r-project.org), de
allí se construye su nombre. El principal propósito de Jupyter es
“apoyar la ciencia de datos interactiva y la computación científica en
todos los lenguajes de programación”
[(Jupyter)](https://jupyter.org/about). De hecho, todos sus proyectos
son desarrollados de forma abierta en GitHub bajo la licencia modificada
de [BSD](https://whatis.techtarget.com/definition/BSD-licenses). El
proyecto promete mantener disponible tanto el software como su código,
para su uso libre.

Sin duda, la característica más popular de Jupyter Notebook, es ser una
aplicación web que permite editar y compartir documentos (llamados
"cuadernos de jupyter") que contienen trozos de código, visualizaciones,
ecuaciones, entre otras, todas interactivas y ejecutadas en tiempo real.
La integración de los elementos *rich media* en documentos intuitivos y
sencillos de editar, la ha convertido en una herramienta muy popular en
la elaboración de artículos, análisis e investigaciones científicas.

Además de Notebook, el proyecto Jupyter ofrece un entorno de desarrollo
llamado [JupyterLab](https://jupyterlab.readthedocs.io), que posee una
interfaz simple, personalizable y capacidades modulares para que puedas
añadir nuevos componentes o plugins según lo consideres necesario.
Jupyter Notebook y Jupyter-lab tienen una interfaz muy parecida, sin
embargo, este último ofrece más funcionalidades.

## ¿Qué es un cuaderno de Jupyter?

Un cuaderno de Jupyter es simplemente un archivo *.ipynb* generado por
la aplicación web, que contiene una multitud de ‘celdas’ con código,
texto Markdown (en formato [LaTeX](https://www.latex-project.org)), o
metadatos (*raw*). Al ser interpretadas por Jupyter, estas celdas
terminan teniendo una apariencia muy similar a la de un documento de
texto, y tras ejecutar las celdas que contienen código, se muestra la
salida en otra celda. Es muy común el uso de bibliotecas como
[matplotlib](https://matplotlib.org) para mostrar gráficos (dentro de
las celdas de código), pero gracias a su versatilidad, puede ser
utilizado también para mostrar videos o imágenes que cambien o se
actualizen a lo largo del tiempo, para mostrar enlaces a archivos
locales o instalar *kernels* de otros lenguajes, lo cual amplía sus
posibilidades.

## ¿Cómo uso Jupyter?

Si deseas hacer tu propio cuaderno de Jupyter y experimentar un poco,
solamente tienes que ir al [sitio web](https://jupyter.org/try), donde
encontrarás varias opciones para probar Jupyter con varios lenguajes de
programación desde una interfaz web, sin tener que instalar nada. Dentro
de esta página, puedes acceder a enlaces de entornos virtuales
prefabricados dentro del sitio como [MyBinder](https://mybinder.org).
Mybinder es un sitio en el cual podrás crear un entorno virtual a partir
de un repositorio de github, con el que podrás interactuar y
experimentar con tus cuadernos de Jupyter.

Si deseas utilizar Jupyter desde tu computadora, basta con instalarlo
utilizando *pip* o *conda*. Sin embargo, la popular distribución
[Anaconda](https://www.anaconda.com) incluye los paquetes necesarios
para utilizar Jupyter, y es la opción recomendada por el propio Project
Jupyter. Simplemente tendrás que dirigirte al [enlace de
descarga](https://www.anaconda.com/distribution/) para instalarla.
Después de esto, podrás ejecutar Jupyter Notebook desde la terminal, y
acceder a la interfaz web desde la URL http://localhost:8888 (por
defecto).

## ¿Quién usa Jupyter?

Jupyter es un proyecto apoyado abiertamente por empresas como Google (de
hecho, puedes hacer cuadernos de Jupyter en el propio Google Drive,
utilizando Google Colab), Microsoft e IBM. Además de una gran cantidad
de universidades alrededor del mundo. No es extraño, que en el propio
GitHub se encuentren alrededor de 5 millones de cuadernos de Jupyter
(según un análisis que utiliza también un cuaderno para mostrar sus
resultados! [(nbestimate)](https://github.com/parente/nbestimate), y que
abarquen áreas desde la ciencia de datos, estadística o economía, hasta
las ciencias sociales o psicología. También existe una gran cantidad de
listas curadas [(A gallery of interesting Jupyter
Notebooks)](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
con ejemplos de aplicaciones reales de Jupyter.

Jupyter es, sin duda, una de las iniciativas de ciencia abierta más
prometedoras que hay. Cuenta con una popularidad inmensa incluso fuera
de su área de enfoque, y una accesibilidad bastante impresionante que
permite a científicos, de todo tipo de trasfondos, aprovechar de sus
capacidades rich media en cuestión de segundos. Y para aquellos que
deseen entrar un poco más profundo en el tema, existe una gran cantidad
de recursos y documentación de apoyo dedicado a Jupyter [(Jupyter
Guide)](https://github.com/jupyter-guide/jupyter-guide) que hace de tu
aprendizaje algo bastante sencillo e indoloro. Llevar tus
investigaciones a otro nivel es cuestión de comenzar a aprender, ¡nada
más!

### Referencias

- [Jupyter](https://jupyter.org/about)

- [nbestimate](https://github.com/parente/nbestimate)

- [A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)

- [Jupyter Guide](https://github.com/jupyter-guide/jupyter-guide)