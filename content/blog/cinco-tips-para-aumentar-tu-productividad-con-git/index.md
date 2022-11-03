<!--
.. title: Cinco tips para aumentar tu productividad con Git
.. slug: cinco-tips-para-aumentar-tu-productividad-con-git
.. date: 2020-02-05
.. author: Yurely Camacho
.. tags: versioning
.. category: git
.. link: 
.. description: 
.. type: text
-->

<!-- # Cinco tips para aumentar tu productividad con Git -->
<!-- **Por Yurely Camacho** -->

![header](../../../images/blog/cinco-tips-para-aumentar-tu-productividad-con-git/header.png)

En artículos anteriores publicados, te hablamos sobre Git de 0 a 100 e
investigación colaborativa con Git. Allí hemos repasado sobre las
bondades de este sistema de control de versiones y su uso actual en la
colaboración en proyectos abiertos, grandes o pequeños, manejándolos con
mayor eficiencia y control al ser un sistema de control de versiones
distribuido, lo que indica que cada desarrollador tiene el historial
completo de su repositorio de manera local y existe una copia central.

<!-- TEASER_END -->

No solo los desarrolladores de software utilizan Git. Esta herramienta
es útil en los casos donde necesites llevar a cabo proyectos
colaborativos: por ejemplo si tienes un blog, puedes gestionar los
artículos y almacenarlos en un repositorio de Git.

En este post te presentamos algunos tips para que tu trabajo en git sea
más productivo, posiblemente, que lo que ha sido hasta ahora.

1. **Maneja las ramas adecuadamente**

Como te mencionamos en nuestro artículo [Git de 0 a 100 en diez sencillos pasos](https://opensciencelabs.org/blog/0002-GitCeroACien/git-de-en-diez-sencillos-pasos/) puedes manejar distintas ramas en tu
repositorio. En cada rama, se registran todos los cambios hechos por
quienes la utilizan y también puedes realizar operaciones entre las
ramas como su fusión, por ejemplo. Generalmente, las ramas son
utilizadas para desarrollar funcionalidades aisladas unas de otras. Por
defecto el repositorio se crea con una rama, denominada "master".

En el manejo de ramas debes considerar, entre otras cosas, lo siguiente:

- Cualquier repositorio tiene o debería tener mínimo dos ramas: una
  conocida como *master*, que es la rama de producción y la segunda
  rama, que se deriva de master, en la cual se desarrollan nuevas
  funciones o se corrigen fallos encontrados en master. A esta rama se
  le suele denominar *develop*.

- Puedes crear ramas derivadas de *develop* para desarrollar otras
  funcionalidades y/o corregir detalles de esta rama, suelen denominarse
  *features*.

- En la rama *master* solo deben estar las modificaciones definitivas del
  proyecto, es decir, no debes "tocarla" hasta que estés seguro
  que los cambios en el proyecto no arrojen problemas al momento de
  hacer pruebas.

- Debes mantener actualizada la rama donde trabajes con la rama de donde se derivó.

- Evita mezclar cambios de diferentes ramas.

- Verifica la rama donde te encuentras al momento de editar cualquier
  archivo, así evitas realizar cambios y subirlos a la rama equivocada y
  afectar el desarrollo de todo el equipo de trabajo. Esto es sumamente
  necesario.

2. **Crea alias para los comandos de git que más utilices**

Con Git, a diario tecleas cierta cantidad de comandos, algunos que
pueden tornarse repetitivos. Además esta herramienta no ofrece la
función de autocompletado. Puedes ser más productivo, si creas *alias*
para aquellos que más utilices. El alias es un "nombre" que, en este
caso, le asignamos a un comando de Git para que sea más corto, esto nos
permite ejecutar la misma acción tecleando menos, es decir, nos ayuda a
ahorrar tiempo y son más fáciles de recordar.

Para fijar alias a los comandos utiliza `git config --global`. Por ejemplo:

`$ git config --global alias.br branch`
`$ git config --global alias.st status`
`$ git config --global alias.ci commit`

De ahora en adelante escribes `git br` en lugar de `git branch` y así
para los demás del ejemplo. No existe un estándar para la creación de
alias, todo dependerá de que te sientas a gusto con ellos. A medida que
aumentes tu trabajo con Git, utilizarás frecuentemente otros comandos,
si te sientes a gusto no dudes en crear alias para ellos.

3. **Juntar commits en uno solo**

En la mayoría de ocasiones existen proyectos con muchas ramas, varios
colaboradores y por tanto muchos commits. Para ahorrar tiempo y hacer el
trabajo menos tedioso, puedes unir los commits.

Esta alternativa requiere que tomes en cuenta algunas cosas:

- No se recomienda mezclar cambios de diferentes ramas.

- Evita, en la medida de lo posible, que los cambios sean de distinto
  tipo (por ejemplo, un cambio en un archivo de texto y otro en uno de
  código), previniendo inconvenientes si por algún motivo debes luego
  deshacer los cambios.

4. **Puedes utilizar alguna interfaz gráfica para manejar Git**

Tal vez utilizar el terminal para gestionar Git puede resultarte al
principio algo complejo, mayormente si estás iniciándote con el control
de versiones. Por eso puede resultarte conveniente utilizar algunos
clientes gráficos de Git, para gestionar los proyectos de una forma
visual e intuitiva y acelerar tu trabajo. Muchos de ellos son totalmente
gratuitos, de código abierto y los hay para cualquier sistema operativo.

En la wiki de Git puedes encontrar una lista más completa de los
[clientes de Git](https://git.wiki.kernel.org/index.php/Interfaces,_frontends,_and_tools#Graphical_Interfaces)

Las interfaces gráficas se adaptan a distintos flujos de trabajo, es
decir, algunas incluyen más funcionalidades que otras. No obstante,
ninguna puede considerarse mejor que otra, solamente que cada una se
ajusta a las necesidades de los usuarios. Vamos ¡anímate a usar alguna de ellas!

5. **Más sobre los commits y otras recomendaciones**

- - Al comenzar una nueva sesión de trabajo, deberías hacer un `fetch` o
  un `pull` para traerte los últimos cambios. De esta  manera, evitas
  conflictos en el futuro al sobrescribir el trabajo de los demás sin
  necesidad.

- Haz commit con frecuencia, no tengas miedo de hacer
  commits con cosas sin terminar y que se muestren así en el
  histórico.

- Cada vez que tengas código que deseas guardar puedes hacer commit. Ten
  presente que al hacerlo no necesariamente debes hacer un push.
  Puedes hacer commits en tu repositorio local para proteger y llevar un
  control de tu trabajo.

- Revisa siempre los cambios antes de subirlos y asegúrate de confirmar
  en el commit lo que realmente necesites.

- El mensaje de commit debe ser conciso pero al mismo tiempo
  informativo.

- No subas cambios directamente a la rama *master*, siempre y cuando no lo
  amerite.

Te hemos presentado algunos tips para que tengas un mejor manejo y mayor
productividad al utilizar git en tus proyectos. Tal vez muchas de ellas
son evidentes; sin embargo, por más mínimas que nos puedan parecer
debemos tenerlas presentes para evitar molestias en el proyecto y en el
grupo de trabajo y aumentar así nuestra productividad en el control de
versiones con Git.

**Referencias**

[Git Book](https://git-scm.com/book/es/v2)

[Domina Git desde cero](https://sargantanacode.es/post/using-git-aliases-to-increase-our-productivity)

[Los 10 mandamientos del control de código fuente](https://www.campusmvp.es/recursos/post/los-10-mandamientos-del-control-de-codigo-fuente.aspx)
