<!--
.. title: Características y tips útiles que te ayudarán a sacar el máximo provecho de CONDA
.. slug: caracteristicas-y-tips-utiles-que-te-ayudaran-sacar-el-maximo-provecho-de-conda
.. date: 2020-12-14
.. author: Yurely Camacho
.. tags: devops, packaging
.. category: packaging
.. link: 
.. description: 
.. type: text
-->

<!-- # Características y tips útiles que te ayudarán a sacar el máximo provecho de CONDA -->
<!-- **Por Yurely Camacho** -->

![header](../../../images/blog/caracteristicas-y-tips-utiles-que-te-ayudaran-sacar-el-maximo-provecho-de-conda/header.png)

Si posees algún conocimiento sobre conda o visitaste anteriormente
nuestro artículo sobre Cómo instalar y comenzar a utilizar Conda (enlace
a artículo) donde dimos una breve definición sobre este potente gestor
de paquetes y entornos; puedes ahora, con el presente post, nutrirte de
más información pues mencionamos algunas características y
recomendaciones para que conozcas los usos de conda y puedas usarla de
manera eficiente y sin complicaciones.

<!-- TEASER_END -->

**Si usas Conda**

- Puedes crear y configurar entornos virtuales solo con teclear unos
  pocos comandos. Te recomendamos crear un entorno virtual para cada
  proyecto que ejecutes o cada actividad donde los requerimientos sean
  distintos. Específicamente el comando que permite crear el entorno es
  `conda create --name nombre_entorno python x.x`, donde x.x es la versión
  de python que deseas correr en ese entorno.

- Este gestor analiza tu entorno actual, en lo referente a los paquetes
  instalados y a las limitaciones de versión de los paquetes que
  especifiques y analiza la forma de instalar dependencias compatibles.
  Si esto no es posible, te informa que no puede ejecutar tu petición.
  Esta es una ventaja muy importante en comparación con otros gestores
  de paquetes como [pip](https://pip.pypa.io/en/stable/), el cual
  instala el paquete que especifiques y sus dependencias, sin antes
  verificar cualquier inconveniente que pueda llegar hasta dañar otros
  paquetes.

- Puedes abreviar muchas opciones de los comandos que usas con
  frecuencia las cuales están precedidas por dos guiones (--) a sólo un
  guión y la primera letra. Por ejemplo, `--name` y `-n`, `--envs` y
  `-e` son lo mismo, es decir, si escribes uno u otro se ejecuta la
  misma acción.

- Para consultar los entornos virtuales que haz creado, ejecuta el
  comando `conda info --envs`. Si tienes varios creados, el que aparezca
  con un asterisco (\*) al lado del nombre es el que tienes activado
  actualmente.

- Para trabajar en cualquiera de los entornos virtuales que tengas
  disponibles debes primero activarlo. Esto se realiza con el comando
  `conda activate nombre_entorno` y cuando necesites salir del entorno
  ejecuta `conda deactivate`.

- Si deseas remover un paquete específico del entorno de trabajo actual,
  ejecuta el comando `conda remove nombre_paquete` y si deseas eliminar
  un paquete de otro entorno entonces ejecuta `conda remove -n nombre_entorno nombre_paquete`.

- Para ver una lista de los paquetes que tienes instalados en el entorno
  actual ejecuta `conda list` y para consultar los paquetes instalados
  en otros entornos teclea `conda list -n nombre_entorno`. También
  puedes acceder a la ayuda de los comandos de conda tecleando `--help`
  o `-h` al final del comando. Por ejemplo, para mostrar la ayuda de
  cómo instalar un paquete ejecuta `conda install -h`.

- La documentación oficial de conda proporciona gran variedad de
  comandos de conda para que puedas manejar paquetes y entornos
  virtuales, accede a esta información en [este
  enlace](https://docs.conda.io/projects/conda/en/latest/commands.html).
  En los enlaces de la página señalada encontrarás ayuda para cada uno
  de los comandos.

- Recomendamos que accedas a [Bioconda](https://bioconda.github.io/), un
  canal popular de conda que ofrece una gran variedad de distribuciones
  de software para biología computacional.

- Si te surgen dudas sobre el significado de algunas palabras referentes
  a lo que es y lo que hace conda, puedes acceder a este
  [Glosario](https://docs.conda.io/projects/conda/en/latest/glossary.html#)
  para aclararlas.

A continuación encontrarás enlaces con información y comandos que te
serán de gran ayuda para el manejo de paquetes y entornos virtuales con
conda.

- [Cheat sheets de terceros](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index)

- [Cheat sheets de Continuum Analytics, compañía creadora de conda](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)

En OpenScienceLabs te invitamos a indagar y a que comiences a usar
conda. Con la ayuda de este post y los recursos que hemos señalado,
estamos seguros que sacarás el mayor provecho de conda en tus proyectos.

### Referencias

- [Documentación Conda](https://conda.io/en/latest/)
