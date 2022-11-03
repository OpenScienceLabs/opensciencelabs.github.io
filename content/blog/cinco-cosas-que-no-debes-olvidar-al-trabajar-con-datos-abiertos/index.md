<!--
.. title: Cinco cosas que no debes olvidar al trabajar con datos abiertos
.. slug: cinco-cosas-que-no-debes-olvidar-al-trabajar-con-datos-abiertos
.. date: 2020-02-21
.. author: Anavelyz Pérez
.. tags: open data
.. category: open data
.. link: 
.. description: 
.. type: text
-->

<!-- # Cinco cosas que no debes olvidar al trabajar con datos abiertos -->
<!-- **Por Anavelyz Pérez** -->

![header](../../../images/blog/cinco-cosas-que-no-debes-olvidar-al-trabajar-con-datos-abiertos/header.png)

Cada vez es más común leer o escuchar sobre datos abiertos pero puede que no
sepamos del todo lo que esto significa. Por ello, vamos a revisar inicialmente
este concepto.

<!-- TEASER_END -->

Los datos abiertos son aquellos que no sólo están disponibles a cualquier persona (liberados) sino que
también están disponibles en distintos formatos de manera que pueden ser
recibidos y procesados por una computadora. Además de ello, los datos abiertos se disponen bajo una licencia
'abierta', es decir, que mínimo permita su uso, modificación, y reproducción
universal (sin restricción en cuanto a quien lo puede ver), y que según sea
apropiado, permita además uso comercial.

Esto deriva en tres particularidades que los datos deben cumplir para que sean
abiertos:

https://ceweb.br/guias/dados-abertos/es/capitulo-2/

- Disponibilidad y acceso: los datos deben estar disponibles de manera integral
  y en una forma en que no genere costos exhorbitantes para la parte interesada en
  copiarlos. El escenario más favorable es poner los datos a disposición para
  que sean descargados a través de Internet. Asimismo, los datos deben ofrecerse
  en un formato conveniente y modificable.

- Reutilización y redistribución: los datos deben ponerse a disposición bajo
  términos de uso que permitan su reutilización y redistribución, e incluso que
  permitan su mezcla y entrecruzamiento con otros obtenidos de distintas bases.

- Participación universal: cualquier persona debe poder usar, reutilizar y
  redistribuir los datos. No debe existir ningún tipo de discriminación contra
  campos de actuación, individuos o grupos. Por ejemplo, restricciones "no
  comerciales" que impidieren el uso "comercial" de los datos, o bien
  restricciones de utilización para determinados fines específicos (por ejemplo,
  sólo para averiguación personal), no están permitidas.

Con lo anterior tenemos una noción más clara de lo que significa que los datos
estén o sean abiertos. Existen diversos repositorios y paginas web que nos
permiten acceder a datos abiertos. Por ejemplo, si estamos interesados en
estudiar los cultivos de Colombia podemos ingresar al sitio web en el que se
publican datos del gobierno Colombiano \[https://www.datos.gov.co\], allí
encontraremos una gama de conjuntos de datos referentes al tema, si escogemos
uno en especifico, veremos sus detalles y si deseamos tener la data en un
directorio de nuestro equipo tenemos la opción de descargarlo en formato csv.

Otra página web que nos brinda una serie de conjuntos de datos es la
correspondiente al gobierno de España https://datos.gob.es en el cual podemos
acceder a datos que abarcan el ámbito social, estos datos los podemos descargar
en diversos formatos como csv o JSON.

Ahora, si nos planteamos realizar proyectos en los cuales se tenga como materia
de estudio datos que no sean de adquisición propia sino provenientes de otras
fuentes, específicamente datos abiertos, no debemos olvidar que:

1. Los datos abiertos poseen una documentación, esta permite que se tenga una
   mejor noción de los datos, su contenido y estructura. Además de que en ella
   se menciona la procedencia, las técnicas utilizadas para su obtención y los
   metadatos. Estos últimos son datos de los datos, permiten describir los datos
   de manera detallada.

1. Todos los elementos de acceso abierto tienen la particularidad de que se
   muestra de manera explicita sus propietarios, autores y las personas
   involucradas en el trabajo, es importante que si utilizamos o reutlizamos
   alguno de sus trabajos no pasemos desapercibidos estos nombres y los
   mencionemos en nuestros proyectos. Además, si tenemos cualquier duda sobre
   los datos y no encontramos información en la documentación podemos
   contactarlos.

1. Los conjuntos datos poseen una estructura predeterminada que puede ser
   descargada en distintos formatos, lo debemos tener en cuenta para realizar un
   análisis óptimo. Esto es porque muchas veces nuestro equipo esta configurado
   de alguna manera en especifico y los archivos son leídos de manera
   equivocada. Por ejemplo, descargamos un archivo csv delimitado por comas y
   tenemos configurado en nuestro equipo la aplicación para la lectura de los
   datos con separador decimal coma(,). Entonces resulta que en la aplicación se
   mostrarán los datos de la columnas en una única columna. Para solucionar esto
   se puede cambiar la configuración o indicarle en el proceso de lectura el
   tipo de separador.

1. Los datos abiertos pueden reutilizarse, si hacemos esto de manera que unamos
   uno o más conjuntos de datos debemos tener cuidado y verificar que la
   estructura de los datos sea la misma. Esto evitaría que la información se
   confunda obteniendo una mezcla homogénea de los datos.

1. Los resultados obtenidos según sea el carácter de la investigación debieren
   ser compartidos a través de un paper o artículo científico de manera que vaya
   de la mano con el acceso abierto. Esto permitirá una retroalimentación
   constante y si es el caso brindaría otro enfoque para el análisis de estos
   datos.

En resumen, los datos abiertos son una iniciativa que permite a los
investigadores y ciudadanos en general tener una visión más amplia y sustentada
de lo que ocurre a su alrededor, proponer maneras de analizar y contrastar datos
y resultados. ¡Por eso te animamos a que consideres el uso de datos abiertos en tus próximos proyectos!
