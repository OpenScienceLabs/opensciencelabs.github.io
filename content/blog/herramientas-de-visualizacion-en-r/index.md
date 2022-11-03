<!--
.. title: Herramientas de visualización en R
.. slug: herramientas-de-visualizacion-en-r
.. date: 2020-04-09
.. author: Yurely Camacho
.. tags: r, visualization, lattice, ggplot2, tidyverse, ggmap, plotly, shiny
.. category: r
.. link: 
.. description: 
.. type: text
-->

<!-- # Herramientas de visualización en R -->
<!-- **Por Yurely Camacho** -->

![header](../../../images/blog/herramientas-de-visualizacion-en-r/header.png)

Sin duda, los datos deben considerarse como la materia prima para
cualquier proyecto de ciencia abierta, pues todos se basan en el manejo
de datos de distintos tipos. Para *entender esos datos* debe realizarse
una inspección visual de su comportamiento. Esto se conoce como la
*Visualización de Datos* que consiste en generar representaciones
gráficas de las variables que componen un conjunto de datos para obtener
información fácilmente interpretable de lo que ellos nos quieren decir y
así, poder comunicarla de una manera asertiva.

<!-- TEASER_END -->

La visualización es un método de exploración de datos que muestra, de una
mirada, algunas cosas que de otra forma hubiese sido muy difícil observar. Por
tanto, se suele realizar al comienzo de cualquier análisis estadístico formal
que se haga con ellos o para la presentación de resultados en informes
descriptivos de datos. La visualización de datos se ve grandemente influenciada
por su calidad y capacidades de las herramientas computacionales y software
estadísticos utilizados para ello. Es aquí donde la decisión del analista de
datos por escoger entre uno u otro lenguaje de programación y/o paquete
estadístico es sumamente importante.

En esta oportunidad, te hablamos de las capacidades para la
visualización de datos que posee el [Lenguaje estadístico
R](https://www.r-project.org/).

R es fundamentalmente un lenguaje de análisis estadístico y por tanto,
tiene en su librería "base" soporte incorporado para gráficos. Otras
funcionalidades avanzadas se incorporan mediante la instalación de
paquetes encontrados en \[https://cran.r-project.org\] y son generados por
una gran comunidad activa de desarrolladores de R. Puedes acceder a más
información que te proporcionamos acerca de R en nuestro artículo \[¿Qué
es el Lenguaje R y cómo puede ayudarte en tus proyectos?\](enlace a
artículo LenguajeR).

R posee una [**Galería de gráficos**](https://www.r-graph-gallery.com/),
esto es una colección de gráficos hechos en R, cuyos ejemplos están
basados mayormente en el uso de tidyverse y ggplot2. En ella se muestran
cientos de gráficos con su código reproducible disponible. Cualquier
persona puede sugerir un gráfico o informar de errores.

En cuanto a la parte de generación de gráficos, en R existen dos
*motores gráficos*, esto se trata de una serie de funciones que permiten
realizar manipulaciones gráficas básicas: como: trazar líneas, dibujar
puntos, curvas, entre otros elementos. Estas funciones no son manejadas
directamente por los usuarios, si no utiliza funciones de alto nivel
(como la función `plot`). Estos motores son: "El motor tradicional o
base de R" y "El motor *grid*".

Las funciones básicas de R para gráficos como, `plot`, `hist`, `boxplot` y
otras, están desarrolladas bajo el motor tradicional de R. No obstante, para
construir otro tipo de gráficos no es suficientemente adecuada. Por tal motivo,
[Paul Murrell](https://www.stat.auckland.ac.nz/~paul/) desarrolló el motor grid.

## Algunas consideraciones sobre el motor tradicional de R

En su paquete base R cuenta con varias funciones para la producción de
gráficas, la mayoría de las cuales se encuentran en el paquete
`graphics`. Algunas de las funciones son:

- `plot()` por defecto realiza un diagrama de dispersión. Si se cambia
  el argumento `type`, permite realizar, por ejemplo, gráficos de líneas
  o series de tiempo, entre otras.

- `hist()` para un histograma.

- `barplot()` permite hacer un gráfico de barras.

- `boxplot()` para un diagrama de caja y bigotes.

- `pie()` o `piechart()` gráfico circular o de sectores.

Para todos los gráficos que se pueden realizar bajo el motor tradicional
de R, se pueden fijar múltiples elementos, algunos son: márgenes,
espacios, títulos, colores, tipos de marcadores, grosor de líneas.
Además de los gráficos mencionados anteriormente también se pueden
realizar gráficos de coordenadas polares, eventos, pirámides de edades,
matrices de dispersión, gráficos de independencia y de estrellas,
realizar combinaciones de gráficos, colocar curvas a histogramas,
efectos de sombreado. También se pueden obtener gráficos para
representar la salida de un modelo estadístico como: regresión lineal
simple, análisis de componentes principales, series de tiempo, cartas o
diagramas de control.

Esos gráficos pueden ser almacenados para su posterior reutilización en
cualquier tipo de documento. Para lo cual se usa el paquete base
`grDevices` que permite aplicar funciones de dispositivos gráficos como
`pdf()` y `png()`.

A continuación daremos una descripción breve sobre algunos paquetes
útiles para la visualización de datos en R.

### lattice

El paquete fue escrito por [Deepayan Sarkar](https://www.isid.ac.in/~deepayan/)
con el objetivo de mejorar los gráficos básicos de R, proporcionando mejores
valores por defecto y tiene la capacidad de mostrar, de una manera fácil, las
relaciones multivariantes. Está desarrollado bajo el motor gráfico grid. Con
este paquete puedes realizar los gráficos *trellis*, que describen situaciones
complejas (mayormente multivariantes) como la relación entre variables
condicionada a una o más variables, representándolo en un sólo gráfico
organizado en paneles. Además tiene la funcionalidad para generar gráficos en
3D, puedes consultar la [documentación de este
paquete](http://cran.fhcrc.org/web/packages/lattice/) para más información.

### ggplot2

Es un paquete apoyado en el motor grid. Fue desarrollado por [Hardley
Wickham](https://hadley.nz/) como una implementación de como una implementación
de la metodología de visualización de datos llamada *The Grammar of Graphics*
cuya idea consiste en especificar de manera independiente las componentes del
gráfico y luego combinarlas. Es un paquete ampliamente difundido y utilizado en
la actualidad por los analistas de datos. Mantiene una estética elegante y
profesional. Este paquete viene incluido dentro de
[tidyverse](https://www.tidyverse.org/) que engloba un conjunto de paquetes para
ciencia de datos. Se pueden realizar gráficos interactivos y animados.

Básicamente, los componentes del paquete son: **Estéticas** (color, forma
de un punto, relleno, entre otras), **Capas** (o geoms en el paquete)
por ejemplo, `geom_point`, `geom_line`, `geom_histogram`, `geom_bar`,
`geom_boxplot`, **Facetas** y **Temas**, referentes a aspectos
estéticos, por ejemplo, ejes, etiquetas, colores de fondo, tamaño de los
márgenes y otros. Puedes consultar más sobre este poderoso paquete en
\[http://www.ggplot2.org\]

### ggmap

Permite la representación de información georreferenciada, tiene la misma
arquitectura que ggplot2. Ggmap permite añadir a los gráficos de ggplot2, una
capa cartográfica adicional para lo cual usa recursos disponibles en la web a
través de APIs de Google y otros. Puedes encontrar más información en la
[documentación de
ggmap](https://www.rdocumentation.org/packages/ggmap/versions/3.0.0).

### plotly

Con plotly puedes realizar gráficos interactivos y dinámicos de calidad
de publicación, sumamente útiles para los resultados que se difunden a
través de Internet. Permite hacer gráficos de líneas, dispersión, área,
barras, error, cajas, histogramas, mapas térmicos, subgráficos, de
múltiples ejes y gráficos 3D. Es gratuito y de código abierto con
licencia del MIT, puedes ver la fuente, informar de los problemas o
contribuir en GitHub. Funciona sin conexión y no requiere ningún
registro de cuenta. Más información en \[https://plot.ly/r/\].

### shiny

Es una herramienta que permite crear aplicaciones web interactivas de
una manera fácil, con esto los usuarios interactúan con sus datos sin
tener que manipular el código, para lo cual solo hace falta conocimiento
de R y no HTML, por ejemplo. Por medio de este paquete se pueden
construir y personalizar fácilmente interfaces gráficas sobre páginas
web mediante pocas líneas de código.
El paquete proporciona varias aplicaciones de ejemplo que puedes usar
para aprender sus principios básicos. Consulta más información en
(enlace a documentación o sitio web de shiny).

### Otros paquetes

- El paquete **rgl** con el que se realizan gráficos interactivos en 3D.
  Se pueden representar incluso formas geométricas en 3D.

- Existen librerías en R para poder conectar y explorar los datos desde Google
  Analytics: **googleAuthR** y **googleAnalyticsR**. Para utilizarlas se
  necesitan en una el token Google Analytics, y en la otra, habilitar Google
  Cloud y su API, respectivamente.

- Paquete **ellipse** y **scatterplot3d** poseen varias funciones para
  realizar gráficos básicos y en 3D respectivamente.

R es muy potente para el análisis estadístico, puedes probar con
distintos paquetes y adoptar el que cumpla tus necesidades y
expectativas. Esperamos que este repaso por algunos de ellos te haya
motivado a indagar un poco más sobre la importancia de la visualización
de los datos y la potencia de R para hacerlo.

#### Referencias

- *R para profesionales de los datos: una introducción*. Gil Carlos.
  Abril 2018.

- *Gráficos Estadísticos con R*. Correa Juan y González Nelfi.
  Universidad Nacional de Colombia, Sede Medellín. 2002.

- [R Users Group Ecuador](https://rpubs.com/RUsersGroup-Ecuador/graf).
