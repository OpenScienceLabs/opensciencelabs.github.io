<!--
.. title: Te hablamos del uso de dashboards para visualización de datos de tu próximo proyecto
.. slug: te-hablamos-del-uso-de-dashboards-para-visualizacion-de-datos-de-tu-proximo-proyecto
.. date: 2020-03-11
.. author: Rainer Palm
.. tags: open science
.. category: dashboard
.. link: 
.. description: 
.. type: text
-->

<!-- # Te hablamos del uso de dashboards para visualización de datos de tu próximo proyecto -->
<!-- **Por Rainer Palm** -->

![header](../../../images/blog/te-hablamos-del-uso-de-dashboards-para-visualizacion-de-datos-de-tu-proximo-proyecto/header.png)

Muchas veces ocurre que, a pesar de que te has tomado el tiempo para analizar y modelar un problema, escribir código, depurarlo y asegurarte de que todo funcione bien, necesitas simplificar y compartimentar los datos y la salida de tu programa para que puedas presentar tu trabajo y que este sea entendido, usualmente mediante un informe y/o una visualización de lo realizado. Las herramientas comúnmente usadas para este propósito tienen varias dificultades: suelen ser estáticas (tal como las diapositivas o los informes escritos), ser diseñadas en mente solo para gente con conocimiento técnico, o permitir solo el uso de ciertos lenguajes de programación o librerías.

<!-- TEASER_END -->

Aquí es donde entran en juego los dashboards. Estas son herramientas de manejo de información que se vinculan entre sí a través de APIs, servicios, librerías y código de una manera dinámica por 'debajo' de la interfaces de usuarios, es decir, mostrando los resultados de esta interacción en una interfaz web o aplicación móvil, a través de gráficos y visualizaciones que al instante presentan los llamados indicadores de rendimiento (Key Performance Indicators KPI por sus siglas en inglés), o cualquier otro tipo de indicadores, acerca de un negocio, proceso, departamento, sitio web, o servidor. Prácticamente cualquier cosa que necesite ser monitorizada de forma constante puede utilizar los dashboards. Debido a su naturaleza como frontend, son completamente personalizables para cualquier propósito al que los quieras aplicar, sólo hace falta crear los scripts necesarios para hacerlo.

¿Por qué utilizar un dashboard?

La principal razón de su popularidad radica en que ofrecen una plataforma central de monitoreo, y a través de ella se puede observar minuto a minuto el rendimiento de cualquier cosa. El backend (comúnmente alojado en un servidor de forma separada de la interfaz del usuario), recibirá también los datos de entrada y se encarga de realizar el análisis en tiempo real. El backend también transmite los resultados a la aplicación web o móvil, lo que constituye de cara al usuario el dashboard como tal, permitiendo a los usuarios conocer el estado actual del servicio de forma instantánea. Un dashboard requiere, por lo tanto, de una red por debajo que grabe, maneje y suba los datos para el análisis que se mostrará en el dashboard. El dashboard permite no solamente la realización del análisis sino también su modificación, ya sea para verlo de maneras distintas o con más detalle, para ajustar los periodos de recolección de datos, o quizás para explorar las predicciones realizadas por el backend.

El dashboard, por lo tanto, intenta responder preguntas acerca de tu negocio o servicio al instante, mediante análisis rápido y presentación de la información en un sitio web. Se construye a partir de aquellas preguntas que se realizan con bastante frecuencia en el manejo de un servicio, tales como: ¿Estará el servidor funcionando? ¿Cuáles son las principales entradas de dinero? ¿Cuál contenido es el que suelen revisar nuestros usuarios con más frecuencia? ¿Cuánto contenido/trabajo se ha realizado en una semana?, entre otras. Para responderlas, se centra en presentar de forma clara datos operacionales, con tablas, gráficos de líneas o barras, medidores, en un diseño sencillo que utiliza elementos y símbolos comunes e intuitivos.

Frameworks y librerias diseñadas para dashboards

Un framework es una plataforma reutilizable útil en el desarrollo de aplicaciones de software de forma que sirve de soporte como base para el desarrollo de nuevas aplicaciones. El framework que ha ganado mayor difusión recientemente, quizás debido a que se construyó a partir de otros que han habido antes (tales como React.js, Plotly.js, o Flask), es Dash, un framework de Python principalmente diseñado para crear aplicaciones web orientadas a la visualización de datos. La idea general esta en vincular una interfaz gráfica alrededor de tu código Python de una forma rápida y sencilla, renderizando esta en un navegador web apoyándose en Javascript y HTML, sin necesitar que el usuario utilice estos lenguajes. Cuenta con paquetes en pip, y una galería de ejemplos, además de ser completamente código abierto y usar la licencia MIT. La popularidad de Dash también se debe a que el código escrito para este framework es bastante compacto (aquí hay una aplicación que muestra una variedad de gráficas en 43 líneas), y tiene bastante capacidad de personalización estética para quién lo desee, mediante CSS.

Por supuesto, hay también bastantes otras opciones. Está Shiny, que es un paquete de R que permite la creación de aplicaciones web directamente desde R, ya sea alojándolas directamente en un sitio web o integrándolas en documentos R Markdown, que también soporta el uso de temas CSS y Javascript. Shiny también tiene una comunidad bastante dedicada y activa. También esta Cube.js, un framework de código abierto diseñado desde abajo para análisis inteligente accesible instantáneamente desde un sitio web. O JDash, o Mozaïk.Todo es cuestión de utilizar el que mas se acerque a tus necesidades.

Los dashboards son una herramienta bastante poderosa. Con un proceso automatizado de subida y recolecta de datos por debajo, y un diseño funcional, sencillo y bien pensado, pueden volverse un instrumento muy importante para presentar tu proyecto y/o desarrollarlo en grupo, y en áreas de marketing, o negocios son prácticamente indispensables. Si tienes dificultades con cuestiones de coordinación de equipos, monitoreo de proyectos o manejo de finanzas, ¿por qué no probarlos?
\[1\]: https://dash.plot.ly/ "Dash"
\[2\]: https://dash-gallery.plotly.host/Portal/ "Dash App Gallery"
\[3\]: https://gist.github.com/chriddyp/3d2454905d8f01886d651f207e2419f0 "Hello World Dash app"
\[4\]: https://shiny.rstudio.com/ "R Shiny"
\[5\]: https://shiny.rstudio.com/gallery/#user-showcase "R Shine | User Showcase"
\[6\]: https://cube.dev/ "Cube.js"
\[7\]: http://jdash.io/ "JDash"
\[8\]: http://mozaik.rocks/ "Mozaïk"
