<!--
.. title: Herramientas de visualización en Python
.. slug: herramientas-de-visualizacion-en-python
.. date: 2020-05-29
.. author: Anavelyz Pérez
.. tags: python, visualization
.. category: python
.. link: 
.. description: 
.. type: text
-->

<!-- # Herramientas de visualización en Python -->
<!-- **Por Anavelyz Pérez** -->

![header](../../../images/blog/herramientas-de-visualizacion-en-python/header.png)

En uno de nuestros artículos, específicamente [10 razones para usar Python en tu proximo proyecto de investigación](http://opensciencelabs.org/2020/01/22/ocho/), se da un recorrido por las ventajas que brinda el lenguaje de programación Python, de allí podemos extraer algunas de sus características tales como:

<!-- TEASER_END -->

- [Python](http://python.org/) es un lenguaje de alto nivel, es decir, es un lenguaje de programación muy intuitivo, diseñado de forma tal que el código escrito sea fácil de leer y entender.
- Con pocas líneas de código se pueden hacer diversas actividades.
- Es multiplataforma, indicando que se puede ejecutar en distintos sistemas operativos, como: Windows, Linux o MacOS.
- Existe una gran cantidad de recursos y apoyo disponibles sobre este lenguaje, a través de grupos de consulta y foros de discusión.
- Posee un número importante de bibliotecas que reciben mantenimiento y apoyo regular por parte de desarrolladores y usuarios. Estas bibliotecas son utilizadas en diversos campos como la estadística y la ciencia de datos.

Tenemos entonces que Python es un lenguaje con características ideales para llevar a cabo proyectos en muchas áreas, cuenta con elementos que lo hacen potente para manipular grandes cantidades de datos y se han desarrollado herramientas que posibilitan, facilitan y hacen su uso más dinámico. En este artículo nos enfocaremos principalmente en describir algunas de las herramientas de visualización sobre este lenguaje; cuando nos referimos a visualización se alusión al hecho de ver, observar o captar a través de un gráfico lo que esta sucediendo y no vemos a simple vista en los datos.

Una de las principales herramientas de visualización son las bibliotecas destinadas a ello. Las bibliotecas de visualización son estructuras de código formalmente distribuidas de manera tal que la podemos descargar y utilizar en nuestros proyectos en el que empleamos Python. Las principales ventajas de estas bibliotecas reside en el ahorro de tiempo y el uso de pocas líneas de código al momento de programar. Al ser bibliotecas de visualización nos permiten crear, mostrar y editar uno o varios gráficos a la vez. Recuerda que, en algunos textos encontraremos la palabra **librería** en vez de **biblioteca**, se pudiesen utilizar como sinónimos.

Algunas de las bibliotecas más populares en Python son:

\*[matplotlib](https://matplotlib.org/): Es una biblioteca de visualización que
permite realizar visualizaciones estáticas, animadas e interactivas en
Python. Con ella se pueden generar gráficos de barras, histogramas,
espectros de potencia, stemplots, scatterplots, gráficos de error, gráficos
circulares y muchos otros. En su sitio oficial de Internet hay una serie de
tutoriales y ejemplos de lo que podemos hacer con ella.

\*[seaborn](https://seaborn.pydata.org/): Al igual que matplotlib, es una
biblioteca que brinda grandes opciones para realizar gráficos. De hecho,
esta biblioteca esta basada en matplotlib. La diferencia principal esta en
sus estilos y paletas de colores que son más estéticos y visualmente
atractivos.

\*[Bokeh](https://docs.bokeh.org): Es una biblioteca de visualización muy
completa porque permite realizar cualquier tipo de diagrama gráfico. Es
ideal para presentaciones basadas en la web, proporciona la construcción de
gráficos elegantes y versátiles de forma concisa. Una de las ventajas
importantes de esta biblioteca con respecto a las demás es su capacidad para
tener un alto rendimiento ante grandes cantidades de datos. Sus elementos se
pueden clasificar en tres grupos importantes:

```
- Gráficos rápidos, son aquellos que se pueden realizar con pocas líneas de código.
 
- Especialidades de matplotlib, gráficos que modifican y mejoran los gráficos de matplotlib.

- Dirigido a desarrolladores e ingenieros de software.
```

\*[Plotly](https://plotly.com/): Es una herramienta de visualización en línea
que ha desarrollado bibliotecas  tanto para Python como para R. Es la opción
más útil y fácil para crear visualizaciones altamente interactivas en la web
(dashboard).

\*[Pygal](http://www.pygal.org/): Al igual que las bibliotecas que hemos
descrito anteriormente Pygal permite realizar cualquier gráfico con pocas
líneas de código, esta tiene la particularidad de estar principalmente
orientada a la creación de gráficos en formato SVG, lo cual indica que
cualquiera de nuestros resultados puede ser editado en un editor de imágenes
e imprimirlos en una resolución de muy alta calidad.

\*[Ggplot](http://ggplot.yhathq.com/): Es un conjunto de métodos para graficar
basado en GGplot2 de R y la gramática de los gráficos. Los resultados se
generan rápidamente y con pocas líneas de código.

\*[Altair](https://altair-viz.github.io/): es una biblioteca de visualización
estadística para Python, basada en Vega y Vega-Lite (gramáticas de
visualización). Permite construir una amplia gama de visualizaciones
rápidamente.

Te dejamos la referencia de algunas de las herramientas de visualización de Python, ¡pero hay otras muchas y puedes conseguir más información en la web! Debes tener en cuenta que a diario podemos encontrar nuevas alternativas y actualizaciones importantes de cada una de ellas. Para hacer uso de las bibliotecas podemos recurrir a interfaces de visualización como [Jupyter Notebook](http://jupyter.org/), [Zeppelin Notebook](http://zeppelin.apache.org/), [Google Colab](http://colab.research.google.com/), entre otras.
