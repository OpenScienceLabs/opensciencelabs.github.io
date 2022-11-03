<!--
.. title: Te mostramos cinco librerías en Python para tu próximo proyecto de ciencia abierta
.. slug: te-mostramos-cinco-librerias-en-python-para-tu-proximo-proyecto-de-ciencia-abierta
.. date: 2020-06-09
.. author: Anavelyz Pérez
.. tags: open science, python
.. category: open science
.. link: 
.. description: 
.. type: text
-->

<!-- # Te mostramos cinco librerías en Python para tu próximo proyecto de ciencia abierta -->
<!-- **Por Anavelyz Pérez** -->

![header](../../../images/blog/te-mostramos-cinco-librerias-en-python-para-tu-proximo-proyecto-de-ciencia-abierta/header.png)

Un proyecto de ciencia abierta, así como cualquier otro, requiere de una
evaluación previa para determinar lo que se necesita hacer y cómo debe llevarse
a cabo. En el caso de ciencia abierta, debemos tener en cuenta que por su
alcance e impacto en la comunidad científica y sociedad en general es vital
estudiar las herramientas que se utilizarán porque de ellas depende la obtención
de resultados óptimos, visualmente atractivos y lo suficientemente informativos.

<!-- TEASER_END -->

Antes de continuar recordemos del artículo [¿Qué es la ciencia
abierta?]([https://opensciencelabs.org/blog/0001-ciencia_abierta/que-es-la-ciencia-abierta/),
que la ciencia abierta es un movimiento, una manera de ver y hacer ciencia, que
busca crear una cultura donde la información de todo el proceso de investigación
científica, ya sean los datos, protocolos, cuadernos de laboratorio, resultados
obtenidos en las diferentes etapas de este proceso, sean gratuitos y de libre
acceso. De esta manera, todas las personas involucradas en el proceso de
investigación, ya sean los propios científicos, instituciones de investigación y
financiamiento, y público en general, pueden contribuir y colaborar con el
esfuerzo de investigación. Con esto se garantiza que el trabajo científico sea
abierto e inclusivo, donde el investigador se dé cuenta que poner a libre
disposición sus trabajos le garantizan, entre otras cosas, el aumento del
impacto y difusión de sus investigaciones.

Allí también se menciona que la ciencia abierta es una forma de producir
conocimiento científico, promoviendo la comunicación y acceso efectivo del
contenido de las investigaciones científicas en todas las áreas (instrumentos de
trabajo, resultados intermedios y finales) mediante la digitalización y las
bondades del internet.

Ahora, podemos extraer que cuando elaboramos un proyecto bajo la modalidad de
ciencia abierta, por lo general analizamos, describimos y descubrimos
información que está contenida en datos, lo cual se hace aplicando métodos
estadísticos u otros similares. Estos se pueden complementar con una o varias
visualizaciones o gráficos que permitirán tanto a los analistas como a los
lectores tener una visión más general de lo que las medidas numéricas o palabras
describen. Además, una visualización logra presentar resultados estéticamente
más atractivos y captar la atención en puntos en los que más enfoque requieran.

Para tener esto último un poco más claro representémoslo en un ejemplo.
Supongamos que estamos estudiando las enfermedades en un periodo de tiempo dado,
en una región específica, y tenemos la información que corresponde a la edad,
sexo y la enfermedad que presentan los pacientes atendidos en los centros
hospitalarios de ese período.

Entonces podemos considerar la estadística descriptiva como una de las técnicas
ideales, en este caso se calcularían estadísticos como la media para la edad, la
proporción para el sexo y el tipo de enfermedad. A su vez podemos hacer cruces
de información a través de tablas de contingencia y a partir de estas elaborar
gráficos que complementarán esta información. Estos gráficos lograrán de forma
sintetizada mostrar lo que los datos revelan, resultará más fácil hacer
comparaciones, además los colores y las áreas de las figuras trazadas captarán
la atención de lo que requiere tener cuidado para la toma de decisiones. Todo
ello es una clara y simple noción de lo que una visualización puede ayudar.

A continuación veamos cinco bibliotecas o librerías de Python que puedes
implementar en tu proyecto de ciencia abierta:

- pandas: Es una biblioteca que permite realizar tareas de manipulación y
  análisis de datos de forma rápida y eficiente. Se complementa con la
  biblioteca de visualización Matplotlib. Puedes consultar más información en
  https://pandas.pydata.org/.

  SciPy: La biblioteca SciPy es uno de los paquetes centrales que componen la
  pila de SciPy. Proporciona muchas rutinas numéricas eficientes y fáciles de
  usar, como las rutinas de integración numérica, interpolación, optimización,
  álgebra lineal y estadística. Esta descripción se encuentra disponible en
  https://www.scipy.org/scipylib/index.html.

- Matplotlib: es una de las primeras y más populares bibliotecas de
  visualización de Python. En su [página web](https://matplotlib.org/) podemos
  encontrar una corta descripción de ella; se indica que Matplotlib es una
  biblioteca muy completa para crear visualizaciones estáticas, animadas e
  interactivas en Python. Con esta biblioteca se pueden generar gráficos de
  barras, histogramas, espectros de potencia, stemplots, scatterplots, gráficos
  de error, gráficos circulares y muchos otros.

  Es uno de los métodos más simples para las representaciones básicas, está
  diseñada con la filosofía de que deberías generar un gráfico simple con pocas
  líneas de código, o simplemente una. Además, se complementa muy bien con otras
  bibliotecas de análisis de datos, tal es el caso mencionado líneas arriba con
  *pandas*.

- Seaborn: es una biblioteca de visualización basada en Matplotlib, permite
  hacer gráficos estadísticos visualmente atractivos, posee estilos
  predeterminados y paletas de colores que están diseñados para obtener
  resultados más estéticos y modernos. Podemos obtener gráficos de barras,
  histogramas, circulares, gráficos de error y muchos otros.

  Podemos encontrar más información de esta biblioteca en su [página
  web](https://seaborn.pydata.org/).

- Bokeh: Es una biblioteca de visualización que permite crear tanto gráficos
  sencillos como gráficos especializados, dashboards y orientados a la web. Los
  resultados de las visualizaciones constan de elegancia y son estéticamente
  atractivos, los gráficos son muy versátiles.

Es posible consultar más información acerca de esta biblioteca en su [página
web](https://docs.bokeh.org/en/latest/index.html).

Todas estas bibliotecas son de código abierto y cuentan con un soporte en la
web, existen foros y varios canales de información sobre ellas. No son las
únicas que puedes incluir en tu proyecto, hay muchas opciones más, te invitamos
a que explores y pruebes estas herramientas.

En nuestro artículo [**Herramientas de visualización en
Python**](https://opensciencelabs.org/blog/0037-visualizacion_python/herramientas-de-visualizacion-en-python/)
puedes encontrar otras bibliotecas o librerías que te pueden interesar.
