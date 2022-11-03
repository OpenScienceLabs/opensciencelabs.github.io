<!--
.. title: ¿Cómo documentar tu proyecto de ciencia abierta?
.. slug: como-documentar-tu-proyecto-de-ciencia-abierta
.. date: 2020-05-04
.. author: Yurely Camacho
.. tags: open science, documentation
.. category: open science
.. link: 
.. description: 
.. type: text
-->

<!-- # ¿Cómo documentar tu proyecto de ciencia abierta? -->
<!-- **Por Yurely Camacho** -->

![header](../../../images/blog/como-documentar-tu-proyecto-de-ciencia-abierta/header.png)

Para hacer reproducible una investigación y que ésta pueda ser verificada a largo plazo, debes contar con un registro donde tomes nota de todos los pasos realizados durante este proceso, lo cual servirá, al mismo tiempo, para que tu proyecto sea comprensible por personas ajenas a él y así puedan desarrollar algún interés sobre el mismo. A todo el proceso de registro de esa información se le conoce como **Documentación**.

<!-- TEASER_END -->

La documentación es una buena práctica de la investigación y es de suma importancia en cualquier proyecto de ciencia abierta. Si no documentamos, al pasar el tiempo las personas tendrán que comenzar de cero y terminarán sin entender el contenido de nuestro proyecto. Además, estando bajo los estándares de la ciencia abierta, el «no documentar» sería una falta grave a sus principios.

De una manera un poco formal, podemos decir que la documentación es un proceso o una práctica que consiste en registrar y/o informar sobre la ejecución de ciertas tareas en algún tema determinado. La documentación de un proyecto se fundamenta, en última instancia, en la realización de varios documentos explicativos que van a depender del alcance y la temática del proyecto en desarrollo.

En cualquier proyecto de ciencia abierta que desarrolles o participes, debes tener presente la importancia de contar con una buena documentación que respalde e informe las labores durante todo el proceso, es decir, un registro de actividades, herramientas y recursos que comprende desde la conceptualización del proyecto, planificación, recolección de los datos, herramientas computacionales y recursos utilizados, la metodología del procesamiento de los datos, los resultados, cuadernos de investigación y otros. Esto quiere decir que, en general, debes documentar toda la metodología utilizada en el desarrollo del proyecto, es decir, la manera cómo se va a realizar cada paso dentro de la misma, incluyendo los resultados.

En lo que respecta a los datos, es necesaria información descriptiva de
los conjuntos de datos utilizados, el código informático resultante de
su procesamiento estadístico (puedes usar
[Jupyter](https://jupyter.org/) para juntar el código informático con
texto), las pautas de la gestión de datos (o propiamente un *Plan de
Gestión de datos*) donde se reflejen la normativa para hacer que el
proyecto se lleve a cabo bajo los estándares de la ciencia abierta
(plataformas de acceso abierto empleadas para la disponibilidad de los
datos, licencia utilizada, entre otras). En pocas palabras te
recomendamos el registro de toda la información referente a la
investigación para lograr, además, que los datos de investigación
cumplan los principios [FAIR](https://www.go-fair.org/fair-principles/),
es decir, sean **localizables, accesibles, interoperables y reutilizables**.

El proceso de documentación generalmente lo lleva a cabo solo una persona y lo comparte con las demás, o se reparten esta tarea entre varios miembros del proyecto. Sea cual sea la persona que lo hace, los documentos varían a lo largo del tiempo y como deben estar compartidos, te recomendamos usar cualquier opción para el control de versiones con [Git](https://git-scm.com/)
para centralizar la información, implementando también otra herramienta
para la gestión de los documentos como
[Sphinx](https://www.sphinx-doc.org/en/master/).

La documentación de un proyecto de ciencia abierta, en general, debe estar estructurada de la siguiente manera: una introducción de todos los apartados de la documentación y que sirva como una visión general de todo el contenido incluyendo el problema, enfoque, objetivos, requisitos y producto final. Debe incluir un desglose de las funciones que cada persona tiene dentro del proyecto y las tareas que debe realizar para cumplir los objetivos propuestos, con fechas tentativas de entrega de resultados para llevar un control efectivo de las tareas y sus datos de contacto. Asimismo debe incorporarse en el documento información referente a las herramientas informáticas utilizadas en el proyecto, el tipo de licencia asignada al proyecto, el lugar donde se guardarán los datos (según corresponda) del proyecto, siempre cumpliendo con los principios de la ciencia abierta. Y no debes olvidar incluir toda la información referente a los conjuntos de datos, código informático generado y los resultados obtenidos.

La documentación no sólo es importante para la reproducibilidad sino que también aumenta la probabilidad que las personas ajenas al proyecto puedan entenderlo, interesarse en él y, además, realizar aportes. Si, por ejemplo, se está ejecutando un proyecto de desarrollo, la documentación del código es muy importante para que, pasado el tiempo, el mismo equipo de desarrollo pueda recordar lo que hicieron en algún momento o intentar replicar el código escrito por otros. Información adicional sobre la documentación en este tipo de proyectos puedes consultarla en este post sobre [Documentación
con Sphinx y
Python](https://medium.com/qu4nt/documentaci%C3%B3n-con-sphinx-y-python-9a777403cb68).

A continuación, te dejamos tips y comentarios adicionales que consideramos pueden ser útiles para elaborar la documentación de tu proyecto de ciencia abierta:

- Si estás en un proyecto y no has comenzado a documentarlo te recomendamos que empieces pronto, la documentación aunque es un proceso que requiere dedicación y tiempo, al final te ahorrará muchos inconvenientes.

- Resulta más fácil documentar el material de un proyecto, si se hace en correspondencia con cada etapa del proceso.

- Si necesitas hacer visible tu proyecto, en muchas ocasiones, es una buena práctica documentar en inglés, debido a la gran cantidad de investigaciones y organismos financiadores que se encuentran en países de habla inglesa.

- Al momento de documentar debes usar un lenguaje claro y comprensible. El documento final debe ser lo suficientemente extenso para especificar todas las características del proyecto pero también contar con la mayor precisión posible.

- Cuando documentes, todo debe estar detallado, no deben existir las obviedades. Cosas que para ti son obvias, no lo son para los demás.

- Los documentos deben estar escritos empleando un lenguaje adecuado para las personas que lo utilizarán.

- La documentación puede incluir todos los gráficos, bosquejos y esquemas que ayuden a complementar la información.

En líneas generales, la documentación te ayudará a organizar las tareas, delegar funciones, establecer fechas y tener un control sobre la metodología, recursos y resultados antes, durante y después de la finalización del proyecto. Asimismo servirá de soporte, permitirá su trascendencia en el tiempo y facilitará su reproducción o replicación
En OpenScienceLabs te animamos a que comiences a documentar tu proyecto
y que tomes en cuenta esta buena práctica para futuros desafíos.

## Referencias

[Manual de Capacitación sobre Ciencia abierta](<(https://book.fosteropenscience.eu/es/)>)
[Guía de expertos en Gestión de Datos](https://www.cessda.eu/Training/Training-Resources/Library/Data-Management-Expert-Guide)
[5 reglas básicas y 5 pasos para documentar tu proyecto web](https://www.socialancer.com/como-documentar-un-proyecto-web/)
