<!--
.. title: pyOpenSci: un promotor de la ciencia abierta
.. slug: pyopensci-un-promotor-de-la-ciencia-abierta
.. date: 2020-08-06
.. author: Yurely Camacho
.. tags: open science, python, pyopensci, ciencia  abierta, open source
.. category: open science
.. link: 
.. description: 
.. type: text
-->

<!-- # pyOpenSci: un promotor de la ciencia abierta -->
<!-- **Por Yurely Camacho** -->

![header](../../../images/blog/pyopensci-un-promotor-de-la-ciencia-abierta/header.png)

Las distintas disciplinas que abarca la ciencia abierta trabajan de
manera conjunta; tal es el caso del código abierto, la investigación
abierta y reproducible y los datos abiertos. En el presente artículo
tratamos sobre **pyOpenSci**, un proyecto al servicio de la ciencia,
desarrollado bajo el enfoque de estas disciplinas. Si eres un
programador, quieres desarrollar (o estás desarrollando) algún paquete
científico con
[Python](https://opensciencelabs.org/blog/0011-10razonesparausarpython/razones-para-usar-python-en-tu-proximo-proyecto-de-investigacion/)
y que sea aceptado por una gran comunidad de *pythonistas*, entonces
aquí está lo que necesitas saber para lograrlo.

<!-- TEASER_END -->

## ¿Qué es [pyOpenSci](https://www.pyopensci.org/)?

pyOpenSci, también conocido como pyOpenScience, es un proyecto encargado
de promover la ciencia abierta mediante el apoyo al desarrollo, la
[*revisión por
pares*](https://es.wikipedia.org/wiki/Revisi%C3%B3n_por_pares) y la
publicación abierta de **paquetes científicos escritos en Python** que
cuenten con una buena
[documentación](https://opensciencelabs.org/blog/0031-documentacion_cienciaabierta/como-documentar-tu-proyecto-de-ciencia-abierta/)
y estén probados previamente. Estos paquetes son utilizados para
recopilar, descargar y transformar datos científicos con una metodología
de trabajo abierta y reproducible.

El modelo de trabajo del proyecto está basado en la comunidad
[rOpenSci](https://ropensci.org/). pyOpenSci no trabaja solo, tiene una
fuerte vinculación con la [Journal of Open Source Software
(JOSS)](https://joss.theoj.org/), una revista que fomenta la revisión
por pares, la aceptación y la publicación de software de código abierto.
Por tanto, estas dos comunidades pueden verse como complementarias entre
sí. El enfoque en el proceso de revisión de pyOpenSci es más práctico
que el de la JOSS. Con pyOpenSci los autores pueden publicar sus
paquetes con un [DOI](https://www.doi.org/) (Digital Object Identifier)
de manera que puedan ser citados y encontrados por los buscadores de
artículos científicos.

En este momento pyOpenSci se está trasladando a un patrocinador fiscal.
Por tal motivo, la revisión del software está en pausa y se reanudará en
septiembre de 2022.

## Inicios de pyOpenSci, un relato de su fundador

El proyecto pyOpenSci surgió por el pythonista [**Steve
Moss**](https://about.me/gawbul), el cual en el post [Facilitating Open
Science with Python](https://ropensci.org/blog/2013/05/16/pyopensci/),
publicado en el blog de rOpenSci en mayo del 2013, manifiesta las
razones de *¿Por qué Python?*, *¿Por qué pyOpenSci?* donde textualmente
dice: "quería, ante todo, facilitar la mejora del campo científico,
permitiendo y promoviendo la apertura y el intercambio dentro y entre
las comunidades científicas. Creo que solo es posible que la ciencia
progrese si se hace completamente transparente". De allí es donde se
fundamentan los ideales de pyOpenSci.

El proyecto pretende mejorar y facilitar la apertura de la investigación
científica. Para ese momento Steve Moss tenía la esperanza de poder
incentivar a los investigadores a utilizar pyOpenSci para desarrollar,
compartir y comprometerse con sus estrategias y así hacer posible la
ciencia abierta. Para esto esperaba poder ofrecer talleres, sesiones de
formación, consultoría y apoyo y que pyOpenSci participara en
actividades de divulgación dentro de las comunidades. Algo que también
expresa en su artículo.

## ¿Cómo puedes contribuir a pyOpenSci?

Puedes involucrarte en este proyecto de distintas maneras, a
continuación te las presentamos:

- [**Únete a una reunión de la
  comunidad**](https://www.pyopensci.org/#community-meetings). Son
  reuniones de video aproximadamente cada dos semanas.

- [**Súmate al foro comunitario**](https://pyopensci.discourse.group/).
  Un espacio donde se discuten los temas de interés y se publican los
  anuncios de nuevas reuniones.

- **Envía un paquete**. Hazlo para apoyar a la comunidad científica de
  Python en general y a la de pyOpenSci en específico.

- **Puedes ser un revisor de paquetes**.

- **Ayuda con la infraestructura técnica**. Tanto el sitio oficial del
  proyecto como los otros sitios web, por ejemplo, necesitan
  mantenimiento y desarrollo.

- **Participa activamente en la divulgación de pyOpenSci**. Comenta a
  tus amigos y colegas, haz mención del proyecto en eventos abiertos y
  en tus redes sociales. !Transmite la información para hacer crecer
  esta comunidad!

## Colaboradores

Según el fundador de pyOpenSci, para colaborar se necesita lo siguiente:
"Además de un amor por Python, uno debería tener un amor por ser abierto
y transparente sobre los temas que les apasionan". Esto lo expresó en su
post para la comunidad **rOpenSci** en 2013 (mencionado anteriormente).
Donde resalta que, para ese momento, solo era él en pyOpenSci y hasta la
actualidad más de 30 personas han colaborado con el proyecto,
conformando una comunidad diversa de personas con un fin común: ofrecer
un lugar práctico en torno al software científico en Python y donde se
promuevan las buenas prácticas de ciencia abierta.

Aquí te mencionamos algunas personas que han contribuido y son miembros
activos de pyOpenSci: [Leah Wasser](https://github.com/lwasser), [Chris
Holdraf](https://github.com/choldgraf), [Max
Joseph](https://github.com/mbjoseph), [Ivan
Ogasawara](https://github.com/xmnlab) miembro del Consejo Directivo de
nuestra plataforma OpenScienceLabs.

## Paquetes pyOpenSci

La comunidad pyOpenSci es la encargada de desarrollar, presentar,
revisar y promover los paquetes de software científico en Python. Al ser
una comunidad abierta, **cualquiera puede enviar un paquete para su
revisión**. Puedes conocer los paquetes que se encuentran actualmente en
revisión accediendo a [este repositorio
GitHub](https://github.com/pyOpenSci/software-review/issues) y los
aceptados [aquí](https://www.pyopensci.org/python-packages/).

Algunos de los paquetes aprobados hasta ahora por pyOpenSci son:

- Lectura, desplazamiento temporal y la escritura de datos de sensores
  [devicely](https://github.com/hpi-dhc/devicely)

- Exploración y visualización de datos espaciales
  [earthpy](https://github.com/earthlab/earthpy).

- Diapositivas de Jupyter Notebooks (enlace a artículo que-es-jupyter)
  [Nbless](https://github.com/py4ds/nbless).

- Validación de las estructuras de datos manejadas por
  [pandas](https://pandas.pydata.org/) con
  [Pandera](https://github.com/pandera-dev/pandera).

- Datos geoquímicos
  [pyrolite](https://github.com/morganjwilliams/pyrolite).

- Integrar conjuntos de datos multimétricos
  [openomics](https://github.com/BioMeCIS-Lab/OpenOmics)

Pasemos ahora a conocer algunos de los sitios y recursos técnicos que
mantiene el proyecto (además de las reuniones y el
[foro](https://pyopensci.discourse.group/)).

## pyOpenSci blog

En este [blog](https://www.pyopensci.org/blog/) se abordan distintos
tópicos, entre ellos:

- Eventos y actividades planificadas.

- Paquetes que han pasado por el proceso de revisión.

- Desafíos de pyOpenSci en la enorme comunidad de Python.

## Otros recursos y sitios relacionados

- [Organización pyOpenSci Github](https://github.com/pyOpenSci).
  Contiene el [repositorio de revisión de
  software](https://github.com/pyOpenSci/software-review) y otros.

- [pyOpenSci
  cookiecutter](https://cookiecutter-pyopensci.readthedocs.io/en/latest/)
  es una plantilla que facilita el empaquetado del código Python.

- [Guía de
  pyOpenSci](https://www.pyopensci.org/contributing-guide/intro) con
  información para los autores y revisores de los paquetes, que incluye
  todo el proceso. Es lo primero que debes leer si estás interesado en
  enviar un paquete a pyOpenSci.

- [Repositorio de Gobernanza de
  pyOpenSci](https://github.com/pyOpenSci/governance). Donde se discuten
  la dirección y el alcance de pyOpenSci.

La comunidad pyOpenSci está abierta para que envíes un paquete, te
conviertas en revisor, ayudes a difundir sus actividades y buenas
prácticas o para que participes en los foros donde tomarán en cuenta tus
dudas. De esta manera, estarás contribuyendo con la comunidad científica
de Python.

### Referencias

- [Web site del Proyecto](https://www.pyopensci.org/)

- [Web site de Steve Moss (fundador de
  pyOpenSci)](https://about.me/gawbul)

- [Facilitating Open Science with
  Python](https://ropensci.org/blog/2013/05/16/pyopensci/)

- [pyOpenSci Promoting Open Source Python Software To Support Open
  Reproducible
  Science](https://ui.adsabs.harvard.edu/abs/2019AGUFMNS21A..13W/abstract)
