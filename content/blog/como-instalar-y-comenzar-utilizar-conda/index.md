<!--
.. title: Cómo instalar y comenzar a utilizar Conda
.. slug: como-instalar-y-comenzar-utilizar-conda
.. date: 2020-12-03
.. author: Yurely Camacho
.. tags: devops, packaging
.. category: packaging
.. link: 
.. description: 
.. type: text
-->

<!-- # Cómo instalar y comenzar a utilizar Conda -->
<!-- **Por Yurely Camacho** -->

![header](../../../images/blog/como-instalar-y-comenzar-utilizar-conda/header.png)

Conda es un sistema de gestión de entornos y de paquetes que funciona en
Windows, Linux y MacOs. Inicialmente se creó para programas Python y
está escrito en python, pero puede implementarse para cualquier
lenguaje.

<!-- TEASER_END -->

Es de código abierto y está publicado bajo la licencia BSD por
[Continuum Analytics](http://www.continuumanalytics.com/). Trabaja con
"canales"(channels); las ubicaciones de los repositorios en los que
busca paquetes. Te permite instalar, ejecutar y actualizar paquetes y
sus dependencias de manera rápida. Se utiliza mediante línea de comandos
en el Anaconda Prompt o en una ventana de terminal. En lo referente a la
gestión de entornos, con conda puedes crear, guardar, cargar y cambiarte
de entorno fácilmente en tu ordenador local.

Un **entorno de conda** es un directorio con una colección específica de
paquetes de conda que has instalado. Puedes activar o desactivar
fácilmente los entornos y los demás que tengas no se verán afectados.
Con conda también puedes crear ***entornos virtuales***; una herramienta
que crea espacios aislados con las dependencias que requieren los
diferentes proyectos que tengas.

Conda también es un paquete y está incluido en todas las versiones de
[Anaconda](https://anaconda.org/); una distribución libre y abierta​ de
Python y R, [Miniconda](https://docs.conda.io/en/latest/miniconda.html),
una pequeña versión de Anaconda que incluye pocos paquetes en
comparación con esta, [Anaconda
Repository](https://docs.continuum.io/anaconda-repository/) y [Anaconda
Enterprise](https://www.anaconda.com/products/enterprise). Está
disponible también en
[conda-forge](https://anaconda.org/conda-forge/conda); un canal
comunitario.

## Instalando Conda

Como mencionamos en líneas anteriores, conda está incluido en todas las
versiones de Anaconda y Miniconda. Por tal motivo, para obtenerla debes
instalar alguna de ellas o comprar [Anaconda
Enterprise](https://www.anaconda.com/products/enterprise). Necesitas una
computadora con sistema de 32 o 64 bits. Para Miniconda 400MB de espacio
en disco y 3GB para descargar e instalar Anaconda.

- *Elige Anaconda* si estás comenzando en conda o python, quieres tener
  instalados automáticamente más de 7500 paquetes científicos y si
  cuentas con el espacio suficiente en disco.

- *Elige Miniconda* si estás dispuesto a instalar individualmente el
  paquete que necesites, cuentas con poco espacio en disco y por eso no
  puedes instalar Anaconda y/o si deseas un acceso rápido a conda y
  python.

A continuación detallamos los pasos a seguir para una instalación
regular de acuerdo al sistema operativo.

1. **Descarga Anaconda o Miniconda según el sistema operativo**

- Puedes descargar Anaconda [en este enlace](https://www.anaconda.com/products/individual)

- Para descargar Miniconda [ingresa en este enlace](http://www.bicentenariobu.com/)

Puedes escoger, según el sistema operativo, una versión con un
instalador gráfico o instalador por línea de comandos. Si no deseas
ingresar comandos en una ventana de terminal, elige el instalador
gráfico (Interfaz gráfica de usuario *GUI*).

Independiente de que uses Anaconda o Miniconda y si no estás seguro de
la opción a descargar, te recomendamos elegir su versión más reciente.
Asimismo, si cuentas con otras instalaciones o paquetes de python, no es
necesario desinstalarlas o borrarlas. Solo instala Anaconda o Miniconda
normalmente.

2. **Una vez descargado el instalador debes hacer lo siguiente**:

### En Windows

- Dirígete a la carpeta donde se encuentra el archivo descargado y haz
  doble click. Es un archivo .exe.

- Sigue las instrucciones.

### En MacOS

- Miniconda:

  - En una ventana del terminal ejecute `bash Miniconda3-latest-MacOSX-x86_64.sh`

- Anaconda:

  - Dirígete a la carpeta donde se encuentra el archivo descargado y haz
    doble click. Es un archivo .pkg.

* Sigue las instrucciones de las pantallas de instalación

* Debes cerrar y volver a abrir la ventana del terminal para que los
  cambios se realicen.

### En Linux

En una ventana del terminal ejecuta:

- Miniconda:

`bash Miniconda3-latest-Linux-x86_64.sh`

- Anaconda:

`bash Anaconda3-latest-Linux-x86_64.sh`

- Sigue las instrucciones de las pantallas de instalación.

- Debes cerrar y volver a abrir la ventana del terminal para que los
  cambios se realicen.

Para todos los casos *Acepta los valores por defecto si durante la
instalación no estás seguro de alguna configuración. Luego puedes
cambiarlos*

**Para probar la instalación independientemente del sistema operativo haz lo siguiente:**

- Abre una ventana del terminal o Anaconda Prompt (en Windows desde el
  menú de inicio), luego ejecuta el comando `conda list`. Si la
  instalación ha sido exitosa debe aparecer una lista con los paquetes
  instalados.

## Actualización de conda

Para actualizar conda debes abrir una ventana del terminal o Anaconda
Prompt (en Windows desde el menú de inicio), luego navega hasta la
carpeta de Anaconda o Miniconda (según el caso) y allí ejecutar el
comando `conda update conda`.

## Primeros pasos con conda

Para que te familiarices, el comando `conda` es el principal y con él
puedes, entre otras cosas, consultar y buscar el índice del paquete que
desees, crear nuevos entornos de conda e instalar y actualizar paquetes
en los entornos existentes.

A continuación te presentamos algunos de los comandos de conda que puedes probar inicialmente:

`conda --version` Verifica que conda está instalado y funcionando en tu sistema.

`conda list` Muestra una lista de los paquetes instalados.

`conda search nombre_paquete` Busca un paquete.

`conda install nombre_paquete` Instala un paquete.

`conda update nombre_paquete` Actualiza un paquete.

Puedes consultar sobre los argumentos y usos de algunos comandos conda
en [este
enlace](https://docs.conda.io/projects/conda/en/latest/commands.html).
La documentación oficial de conda te ofrece una [guía de 20 minutos para
iniciarte en
conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
y probar sus principales características.

Si necesitas de la gestión de paquetes y entornos, no dudes en usar
conda. En un próximo artículo te dejaremos algunos tips para que saques
el mayor provecho a trabajar con conda, no te lo pierdas.

#### Referencias

- [Documentación oficial Conda](https://docs.conda.io/projects/conda/en/latest/index.html)
