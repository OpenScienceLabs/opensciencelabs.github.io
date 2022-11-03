<!--
.. title: Investigación Colaborativa con Git
.. slug: investigacion-colaborativa-con-git
.. date: 2020-01-20
.. author: Anavelyz Pérez
.. tags: open science
.. category: git
.. link: 
.. description: 
.. type: text
-->

<!-- # Investigación Colaborativa con Git -->
<!-- **Por Anavelyz Pérez** -->

![header](../../../images/blog/investigacion-colaborativa-con-git/header.png)

La Investigación colaborativa surge en el momento en el que varias
entidades, que pueden estar especializadas en diferentes áreas, se
establecen un mismo objetivo o proyecto. La finalidad de una
investigación bajo este modelo es encontrar soluciones, descubrir o
explicar comportamientos de un fenómeno en particular el cual puede ser
económico, social, político, científico, entre otros.

<!-- TEASER_END -->

La investigación colaborativa se presenta en distintas ocasiones donde
se requiera un ciclo colaborativo de acuerdo a las necesidades que se
presenten en un proyecto, se busca brindar aportes significativos en la
sociedad o entorno.

A continuación te mostramos algunos ejemplos en los cuales puede resultar
útil implementar este tipo de investigación:

- Un departamento de una organización está ayudando a otro que tiene una
  deficiencia con respecto a la optimización de sus actividades.

- Los cultivos de una localidad se están viendo afectados por una plaga;
  esa plaga es similar a una ocurrida años atrás. Para estudiar las
  causas, consecuencias y prevenir futuros episodios como este, se han
  reunido varios biólogos expertos junto con historiadores, ingenieros
  agrónomos y especialistas en otras áreas.

- Un grupo de expertos en diversas disciplinas tienen en mente crear un
  documento que sea pieza fundamental en la conformación del presupuesto
  nacional del siguiente año fiscal.

- Un diseñador industrial está proponiendo un rediseño de uno de los
  productos de la empresa en la que trabaja. Para ello realiza un
  estudio con la ayuda de sus compañeros expertos en marketing y
  estadística. Con esto busca obtener una mejor perspectiva de los
  usuarios, sus necesidades y aceptación del mercado en general.

- Una institución privada desea financiar las actividades de una
  fundación. Para lo cual recurre a un grupo de expertos con la
  finalidad de evaluar y presentar un esquema del presupuesto y la
  descripción de lo que debe invertir para obtener los mejores
  resultados.

Cada una de las situaciones ejemplificadas requieren de la participación
de distintos grupos multidisciplinarios que pueden estar formados por
personas, entidades, institutos o grupos de trabajo que interactúen a la
vez con la información. Esto puede ser de manera individual, en paralelo
o en conjunto para conformar lo que sería el proyecto final. La idea es
que, todos los miembros del equipo que llevarán a cabo el proyecto,
cumplan con tareas especificas según sus conocimientos o aptitudes.

Las tareas asignadas a cada miembro pueden o no depender
condicionalmente unas de otras y deben promover el cambio y fomentar la
participación. Esto implica que el proyecto estará sujeto a cambios
constantes por la integración de nuevas ideas. Es aquí cuando nos
podemos plantear ¿Cómo almacenamos todos los cambios que ocurren hasta
que es alcanzado el objetivo final? ¿Qué debemos hacer si un miembro del
proyecto elimina por accidente información importante?.

Para esto proponemos el uso de los *sistemas de control de versiones*
(VCS, por sus siglas en inglés) pues nos permiten almacenar todos los
cambios realizados y la información asociada a ellos. En este caso te
recomendamos el uso de **Git**.

## Git

Es un sistema de control de versiones que se diferencia de sus similares
por la forma en la que manejan sus datos; Git lo hace como una secuencia
de copias instantáneas. Además, "todo es verificado mediante una suma de
comprobación (*checksum* en inglés) antes de ser almacenado, y a partir
de ese momento es identificado mediante esta, esto quiere decir que es
imposible cambiar el contenido de cualquier archivo o directorio sin
que Git lo sepa".

Para ejecutar la mayoría de las operaciones en Git solo se necesitan
archivos y recursos locales. Estas funcionalidades te permiten hacer
investigación colaborativa y que la información siempre esté
salvaguardada.

Por otro lado Git, al igual que otros VCS, posee un sistema de
ramificación; el cual consiste en tomar la versión principal del
proyecto para poder trabajar en ella individualmente, pero sin alterar
la versión original, manejando así una especie de copia de esta. Hechas
las modificaciones, la rama puede volver a fusionarse con el archivo de
origen.

Tal vez pienses que el proceso de creación de ramas es lento y tedioso,
debido a la cantidad de contenido o información en el proyecto, pero en
Git esto resulta rápido y sencillo. Una de las ventajas de utilizar
ramas es que, como colaborador, puedes trabajar de manera separada y
eficiente, sin alterar la versión principal. Así mismo, puedes crear
subproyectos constituidos por ramas de las cuales se deriven otras
ramas.

Git te permite obtener tu propio repositorio remoto o utilizar otros
alternativos, con lo cual obtendrás el máximo provecho a la información
y a su vez compartirás conocimiento rompiendo barreras de distancia.

La investigación colaborativa con Git es ideal para crear grandes movimientos y
proyectos. Los avances y cambios llegarán en poco tiempo, los equipos de trabajo
pueden crear ambientes amigables de trabajo y cada aporte puede ser cuestionado
de manera positiva consultando a los involucrados oportunamente, respetando su
autoría y tiempo de dedicación al proyecto.

Referencia:
**The entire Pro Git book**. Autores: Scott Chacon y Ben Straub
