---
title: "Implementaciones recientes en SciCookie gracias a la subvención de la PSF"
slug: avances-scicookie-grant-2024
date: 2024-06-21
authors: ["Yurely Camacho"]
tags: [psf, osl, scicookie, subvención, grant, comunidad, colaboración, desarrollo]
categories: [código abierto, desarrollo de software, python]
description: |
  Descripción de las mejoras y tareas realizadas en SciCookie gracias a la subvención de la PSF.
thumbnail: "/header.png"
template: "blog-post.html"
---

Como mencionamos en el post anterior [SciCookie recibe nueva subvención de PSF para mejoras y crecimiento](https://opensciencelabs.org/blog/scicookie-recibe-nueva-subvencion-de-psf-para-mejoras-crecimiento/), en enero de 2024 la PSF aprobó nuestra solicitud de subvención. Esto nos ha permitido implementar una serie de mejoras significativas en SciCookie. A continuación, presentamos los avances y tareas realizadas.

<!-- TEASER_END -->

Se han incorporado nuevas opciones de herramientas a la plantilla, incluyendo los códigos de conducta (CoC) de Python (adaptado) y de NumFOCUS. También se ha añadido soporte para prettier como una opción de linter, proporcionando más flexibilidad a los usuarios.

![Nuevas opciones de CoC](scr1.png)

En cuanto a la estructura de la herramienta, se han realizado varias optimizaciones. Se implementó una opción condicional para las preguntas de uso de herramientas en el proyecto (`depends_on`) y se corrigió la indentación en algunos archivos de configuración para mejorar la legibilidad. Además, se unificaron estos archivos según las distintas opciones de sistemas de construcción (*build systems*) para evitar la repetición innecesaria de código y texto. También se creó un ejemplo para la opción de Interfaz de línea de comandos (CLI) como base del contenido de ese archivo.

En el ámbito de la documentación, se ha automatizado el proceso de mover archivos de configuración a la raíz del proyecto, manteniendo una estructura ordenada. La selección del motor de documentación sphinx se ha dividido en `sphinx-rst` y `sphinx-md(myst)` para ofrecer opciones específicas. Se ha generado la documentación de la API para estas opciones, añadido `quarto` como un motor de documentación adicional, y se han incorporado distintos temas para cada motor de documentación disponible en la plantilla.

![Nuevas opciones de documentación](scr2.png)

Se ha iniciado comunicación con Leah Wasser, directora ejecutiva de pyOpenSci, quien ha revisado directamente el uso de SciCookie para las necesidades de pyOpenSci como plantilla de proyectos para recomendar a su comunidad. A partir de sus revisiones y sugerencias, se ha mejorado SciCookie para cumplir con sus principales expectativas. Leah también ha comenzado la creación de un perfil (conjunto de configuraciones por defecto) específico para pyOpenSci en [SciCookie](https://github.com/osl-incubator/scicookie/pull/273). Debido a sus prioridades y cronograma, este trabajo aún está en progreso.

Con estos avances, SciCookie se presenta como una herramienta más completa y adaptable a diversas necesidades. Continuaremos trabajando para ofrecer mejoras a la comunidad de código abierto.

Puedes consultar nuestro post [Collaborating and learning from SciCookie](https://opensciencelabs.org/blog/scicookie-collaborating-and-learning/) para más información sobre la herramienta.

Mantente atento a futuras actualizaciones sobre SciCookie en próximos posts.

Elementos gráficos de la portada fueron extraídos de [Job illustrations by Storyset](https://storyset.com/job)
