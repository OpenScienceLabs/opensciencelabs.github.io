<!--
.. title: Git de 0 a 100 en diez sencillos pasos
.. slug: git-de-en-diez-sencillos-pasos
.. date: 2020-01-08
.. author: Por Rainer Palm
.. tags: versioning
.. category: git
.. link: 
.. description: 
.. type: text
-->

<!-- # Git de 0 a 100 en diez sencillos pasos -->
<!-- **Por Rainer Palm** -->

![header](../../../images/blog/git-de-en-diez-sencillos-pasos/header.png)

¿Necesitas aprender [Git](https://git-scm.com/) para manejar con mayor
eficiencia y control tus projectos y trabajos? Ya sea para desarrollo de
software, creación de páginas web, investigaciones científicas, o para
manejar tus escritos, te podría ser muy útil aprovechar la seguridad que
te da Git para el control de versiones, o la facilidad con la que
permite la investigación colaborativa. Además, podría serte de mucha
ayuda a la hora de buscar empleo en tu área de trabajo, ya que los
proyectos y contribuciones que tengas almacenados en Git te servirán como
parte de tu currículo. Sin embargo, puede parecerte algo intimidante
debido a la gran diversidad de opciones que te proporciona, además del
uso requerido de la línea de comandos en la aplicación Git. Pero si
sigues los 10 pasos que presentamos a continuación, te darás cuenta de
lo sencillo que puede resultar subir y manejar archivos en tu primer
repositorio, crear varias ramas en el mismo y compartir archivos con
colaboradores.

<!-- TEASER_END -->

## 1. Crea tu cuenta en Github

Aunque es posible emplear git a nivel local, es preferible que utilices
una plataforma que te permita alojar repositorios en la nube, tal como
[Github](https://github.com/) o [Gitlab](https://about.gitlab.com/) para
difundir fácilmente tu trabajo. Puedes [registrar una cuenta
Github](https://github.com/join), donde simplemente tendrás que
proporcionar tus datos y seguir los pasos de creación de cuenta. Luego
de registrarla, podrás seleccionar un plan de pago cuando
quieras, o simplemente usarlo de forma gratuita.

## 2. Crea tu primer repositorio

Inmediatamente después de crear tu primera cuenta, Github te guiará
hacia la creación de tu primer repositorio, a través de
https://github.com/new, donde tendrás que ponerle un nombre y una
descripción. Github automáticamente crea el repositorio con un archivo
`README.md`, el cual es un simple archivo de texto que será visto al
entrar en la página del repositorio. Este archivo tiene información
importante acerca del repositorio, el propósito de los archivos que
están allí y de cómo está organizado el repositorio. También puedes
colocar allí algún enlace a la página web del proyecto (si la tienes), o
un correo para contactos e información.

## 3. Instala Git en tu computadora

Para poder subir archivos a tu repositorio desde tu disco duro, tendrás
que instalar Git en tu computadora. Simplemente descárgalo desde
https://git-scm.com/, o, si estás usando Linux, instálalo mediante el
gestor de paquetes de tu distribución buscando el paquete git. Después
podrás usarlo en la línea de comandos. Verifica si se instaló
correctamente ejecutando `git –-help`

## 4. Clona un repositorio

Cuando creas un repositorio Git, automáticamente se crea una carpeta
oculta `.git` con información de los archivos y ramas de tu repositorio,
los cambios a estos y el último commit. Tu repositorio en Github también
contiene esta carpeta, así que, para ahorrarte un dolor de cabeza,
deberías clonarlo (copiarlo en tu ordenador), ya sea descargándolo desde
su página o en la línea de comandos escribiendo: `git clone
https://github.com/(tu usuario)/(nombre del repositorio).git`. También
puedes copiar la URL del repositorio desde la página.

## 5. Agrega archivos a tu repositorio y haz tu primer commit

Cada vez que realizas cambios en tu repositorio (ya sea modificando,
agregando o borrando archivos), deberás sincronizarlos haciendo lo que
se conoce como un commit. Puedes utilizar los comandos:

- `git add {nombre de tu archivo}`

- `git rm {nombre de tu archivo}`

para hacer cambios en la copia local de tu repositorio, ya sea añadir y
modificar o eliminar archivos, respectivamente. Antes de sincronizar los
cambios, debes ‘empaquetarlos’ en un commit, mediante el comando `git commit -m “{descripción de los cambios}”`

Después podrás sincronizar ese commit con el servidor de Github
utilizando el comando `git push origin master`. 

Con aplicaciones gráficas como Github Desktop u otra similar, podrás
realizar estos cambios de una forma mucho más intuitiva.

## 6. Maneja distintas ramas de tu repositorio

Cuando creas tu repositorio con git, este solo tiene una rama principal
o “default”, la cual se denomina `master`. En git, una rama es una
especie de ‘apuntador’ que señala a una serie específica de commits.
Cuando quieras hacer cambios en tus archivos, para realizar pruebas sin
afectar el funcionamiento del código alojado en la nube que ya sabes que
funciona, puedes crear otra rama. Si los resultados son de tu agrado,
podrás sincronizar ambas ramas más tarde.

Para crear otra rama, simplemente ejecuta:

`git checkout -b {nombre de tu rama}`

Esto hará que, a partir de ahora, todos los cambios que realices a
tus archivos sean parte de la rama que has creado. 

Si deseas sincronizar tu nueva rama con el servidor de Github, ejecutas:

`git push origin {nombre de tu rama}`

Igual que para hacer cambios en master, deberás hacer un commit para
sincronizar los cambios locales con el repositorio de Github.

## 7. Realiza un merge

El comando `git checkout` nos permite cambiar de rama dentro del
repositorio. Puedes usarlo para volver a hacer cambios en la rama master
con el siguiente comando:

`git checkout master`

Si estás satisfecho con los cambios que has hecho en la rama, puedes
hacer un merge, lo que quiere decir que se fusionan los cambios hechos
en la rama secundaria con los de la rama en la que estás ubicado
actualmente (en este caso, master) de la siguiente manera:

`git merge {rama con cambios}`

Git intentará hacer este proceso automáticamente, pero puede ser que
hayan conflictos entre ramas con los cambios hechos. En este caso,
tendrás que editar los archivos que te muestra Git, y agregarlos
manualmente ejecutando `git add {nombre de archivo}`.

## 8. Verifica cambios con tu copia local

En caso de que tu copia local del repositorio no tenga los cambios
hechos hasta el último commit en la rama que estás trabajando, puedes
actualizarla ejecutando `git pull`.

Para ver los cambios que se han realizado entre las distintas ramas del
repositorio, ejecuta el comando `git diff {rama fuente} {rama a comparar}`

También puedes ver la historia del repositorio (los commits hechos a lo
largo del tiempo) usando el comando `git log`. Recomendamos que primero
ejecutes `git log –help` para ver como puedes aprovechar mejor esta
herramienta.

## 9. Propone cambios a repositorios de terceros

En caso de que quieras hacer un commit a un repositorio que sea de otra
persona, simplemente tendrás que ir a la página del repositorio en
Github, hacer un **fork** (una copia personal de ese repositorio, como un
puente hacia el original), y clonarlo en tu computadora.

Luego de crear los commit deseados y subirlos a tu fork, podrás
dirigirte a la página donde este se encuentra y dar click a **New pull
request** (o solicitud de extracción). Esto te llevará a una página
donde puedes evaluar los cambios que has hecho y crear una solicitud
para que los propietarios del repositorio los fusionen con su rama
master.

## 10. Acepta o niega cambios propuestos

Cuando un colaborador siga los pasos descritos anteriormente y haga una
solicitud de extracción en tu repositorio, podrás verificar los cambios
que se han realizado en el commit de su fork, además puedes ver su
descripción y las sugerencias que han dado. Podrás entonces conversar
con ellos en los comentarios de la solicitud de extracción, y
dependiendo de lo que consideres apropiado, aceptar o negar los commit
propuestos y fusionar su fork con la rama master de tu repositorio.

En caso de que quieras que un colaborador pueda contribuir al proyecto
sin necesidad de aprobar sus commit, podrás invitarlos mediante la
página de *Parámetros* (accesible desde la página del repositorio),
simplemente dando click a *Colaboradores* en la barra lateral izquierda
y añadiendo su nombre de usuario de GitHub.

Si has seguido todos los pasos hasta ahora, felicidades, ya puedes
considerarte oficialmente un usuario de git. Mantener y actualizar tus
propios repositorios y colaborar con los demás usuarios de Github es más
sencillo de lo que parece. Si así lo deseas, puedes seguir buscando
información acerca de cómo aprovechar git al máximo, ya sea a través del
libro [Pro Git](https://git-scm.com/book/es/v2/) o en la documentación
de [Github](https://help.github.com/en/github).
