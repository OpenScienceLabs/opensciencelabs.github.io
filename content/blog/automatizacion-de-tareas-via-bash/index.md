<!--
.. title: Automatización de tareas vía bash
.. slug: automatizacion-de-tareas-via-bash
.. date: 2020-06-21
.. author: Anavelyz Pérez
.. tags: bash, automation
.. category: bash
.. link: 
.. description: 
.. type: text
-->

<!-- # Automatización de tareas vía bash -->
<!-- **Por Anavelyz Pérez** -->

![header](../../../images/blog/automatizacion-de-tareas-via-bash/header.png)

¿Qué es Bash?

Es un shell, o intérprete de lenguaje de comandos, para el sistema operativo
GNU. Su nombre es un acrónimo de "*Bourne-Again SHell*", un juego de palabras
sobre Stephen Bourne, el autor del antepasado directo del actual shell de Unix
sh, que apareció en la séptima edición de la versión de *Bell Labs Research* de
Unix.

<!-- TEASER_END -->

El shell también es conocido como **terminal**; una interfaz entre el usuario
y el propio sistema operativo. Podemos acceder a él a través del menú o una
combinación teclas. Linux proporciona por defecto seis terminales de este tipo,
de Control+Alt+F1 a Control+Alt+F6. Si queremos volver al modo gráfico lo
hacemos con Alt+F7 (estos atajos pueden variar según la distribución).

Es importante destacar que el sistema operativo GNU proporciona otros shell sin
embargo, Bash es el shell por defecto. Este, al igual que otros programas de GNU,
es bastante portátil. Actualmente funciona en casi todas las versiones de Unix y
otros sistemas operativos como Mac OS X Tiger. También se ha llevado a Microsoft
Windows por el proyecto Cygwin.

Ahora bien, cuando desde una distribución Linux abrimos o activamos un terminal se indica que estamos en
nuestro home mediante el signo ~.Veremos en pantalla algo similar a:

![Terminal](../../../images/blog/automatizacion-de-tareas-via-bash/terminal1.png)

El home es el sitio donde se pueden aplicar inicialmente las tareas.

Un par de comandos que nos brindan ayuda o referencias en Bash son `man` e
`info`, ideales cuando se tienen dudas acerca de uno o varios comandos.

- `man` muestra la información del manual de bash en el sistema sobre el comando
  o página indicado.

- `info` permite consultar la información que se almacena en archivos INFO
  (archivos de formato [Texinfo](https://es.wikipedia.org/wiki/Texinfo)) de
  algún comando o software.

Para utilizar estos comandos solo es necesario escribirlos seguido de un espacio
y la palabra de la cual tenemos duda. Por ejemplo si tecleamos `info bash` o
`man bash`, tenemos la posibilidad de leer un texto sobre lo que es bash y sus
características principales.

![Comandos man e info](../../../images/blog/automatizacion-de-tareas-via-bash/ayuda.gif)

## Crear, eliminar y editar carpetas o directorios

Entre las tareas que podemos realizar con bash están  crear, eliminar y editar
carpetas o directorios. Algunos de los comandos asociados a estas son:

`pwd` nos indica el directorio en el que estamos actualmente. Si probamos este
comando en el home obtendremos algo similar a

![pwd en home](../../../images/blog/automatizacion-de-tareas-via-bash/pwd.png)

`ls` nos permite ver la lista de los directorios, carpetas y archivos contenidos
en el sitio o carpeta en la que estemos. `ls -a` nos muestra todos los archivos
incluyendo los ocultos.

Si queremos movernos por las carpetas el comando `cd` seguido de la dirección a
la que se desea ir nos permitirá realizar esta tarea. De modo que `cd /` te
llevara a la raíz, `cd ~` al home ( `cd` solo hace lo mismo), `cd /usr/doc` te
lleva al directorio de documentación del sistema.

Si quieres crear una carpeta (o varias) lo puedes hacer en tu home, usando `mkdir`
y el nombre de la carpeta que quieres crear, luego entra en ella con cd.

Para borrar una carpeta escribe `rmdir` seguido por un espacio y el nombre, pero
la carpeta tiene que estar vacía y contar con permiso para borrarla.

## Mover, renombrar y eliminar archivos o ficheros

El comando `mv`, permite dos operaciones. Cambiar un fichero de sitio, para lo
cual es necesario que se tenga permiso de escritura sobre ese fichero y el lugar
de destino. Se utiliza simplemente indicando mv nombre_origen ruta_destino.

*Con este comando también es posible mover directorios, o todos los ficheros de
un directorio.*

La otra operación que se puede realizar con `mv` es el cambio de nombre, así basta con
indicar el nombre de un fichero o directorio, y luego su nuevo nombre.

*Los comandos cat, more y less sirven para mostrar el contenido de ficheros de
texto.*

El comando `rm` se utiliza para borrar ficheros. Es importante destacar que estos
ficheros no se envían a una papelera así que NO SE PUEDEN RECUPERAR UNA VEZ
BORRADOS.

Otro comando útil es `cp` sirve para copiar ficheros. En el proceso de copia
intervienen tres elementos: lo que se copia, la ruta de origen y la ruta de
destino. La ruta de origen se especifica junto con lo que se quiere copiar.

De la misma manera que se copian, se borran o se mueven ficheros, se puede hacer
lo mismo con los directorios. Hay que tener en cuenta que un directorio puede
contener muchos ficheros y, además, otros directorios que, a su vez, pueden
contener más ficheros y directorios. Por tanto, si se quiere copiar un fichero
completo, con todo lo que tiene dentro, hay que indicarlo con la opción -R. A
esto último se suele llamar “copiar de forma recursiva”.

Otro comando que puede ser util es `rm -rf nombre_del_directorio`, borra el
directorio y todo lo que contiene (lo que se elimina no se puede recuperar).

## Comodines

Recordemos que Bash es el interprete de comandos, el programa que intenta
comprender lo que tu dices y lo ejecuta, este nos permite utilizar comodines a
la hora de escribir un nombre de fichero o directorio. Además la tecla tab
permite completar rutas o algún comando a la hora de escribir. Por ejemplo,
escribe /ho y pulsa tab verás cómo aparece /home/).

Los principales comodines son \*, ? y los corchetes \[\].

- El asterisco sustituye a cualquier grupo de letras.

- El signo de interrogación ? sólo vale para una letra.

- Los corchetes valen por un conjunto definido de letras.

Debes tener en cuenta que son muy importantes las mayúsculas y la minúsculas al
momento de escribir tus comandos, porque el intérprete es sensible a ellas. Esto
trae como consecuencia la posibilidad de tener dos ficheros que se llamen igual,
por ejemplo proyectos y Proyectos, uno tiene mayúsculas y otro no.

En resumén, tenemos que Bash nos permite realizar diversas tareas asociadas a
directorio y ficheros. Existen distintos comandos que pueden ser bastante útiles
y si tenemos cualquier duda podremos recurrir rápidamente a un manual o
documento de ayuda.

Puedes consultar más de los comandos en https://ss64.com/bash/index.html

## Referencias

Manual Práctico de Linux con ejercicios por Luis José Sánchez González.
Manual de Linux por Álvaro Alea Fdz.
[EcuRed-Terminal](https://www.ecured.cu/Terminal_de_GNU/Linux)
[EcuRed-Bash](https://www.ecured.cu/Bash)
