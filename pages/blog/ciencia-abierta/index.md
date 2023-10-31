---
title: "5 proyectos de inteligencia artificial que te sorprenderán"
slug: ciencia-abierta
date: 2021-02-08
author: Rainer Palm
tags: [datos]
categories: [ciencia abierta, ciencia de datos, inteligencia artificial]
description: |
  Una de las areas de investigación mas prometedoras de la ultima decada es sín
  duda la inteligencia artificial. No solamente reune una increible cantidad de
  regiones del conocimiento que, superficialmente, son demasiado dispares (tales
  como la filosofía de la mente, la psicología, la biología, la robotíca, la
  lógica pura, entre muchas otras), sino que también los resultados de sus
  publicaciones se vuelven relevantes de forma retroactiva para las areas de la
  ciencia de cuya historia se nutre. El estudio y la utilización de las redes
  neuronales y el aprendizaje automático (o machine learning) ha demostrado ser
  increiblemente utíl no solamente a la hora de realizar investigaciones regulares
  con estas tecnícas, sino también para crear nuevas herramientas de simulación y
  experimentación, tanto para uso científico como el particular o comercial.
draft: false
usePageBundles: true
thumbnail: "/header.png"
featureImage: "/header.png"
---

Una de las areas de investigación mas prometedoras de la ultima decada es sín
duda la inteligencia artificial. No solamente reune una increible cantidad de
regiones del conocimiento que, superficialmente, son demasiado dispares (tales
como la filosofía de la mente, la psicología, la biología, la robotíca, la
lógica pura, entre muchas otras), sino que también los resultados de sus
publicaciones se vuelven relevantes de forma retroactiva para las areas de la
ciencia de cuya historia se nutre. El estudio y la utilización de las redes
neuronales y el aprendizaje automático (o machine learning) ha demostrado ser
increiblemente utíl no solamente a la hora de realizar investigaciones regulares
con estas tecnícas, sino también para crear nuevas herramientas de simulación y
experimentación, tanto para uso científico como el particular o comercial.

Aunque el machine learning aun tiene sus problemas y misterios por resolver, ya
como area de investigación ha producido muchos hallazgos y descubrimientos de
increible importancia para la ingeneria de sistemas y demás areas relacionadas
con la informatica. Ya para aquellos que trabajan día a día haciendo
experimentos con librerias tales como [TensorFlow](https://www.tensorflow.org/)
se vuelve una cuestión de suma importancia el andar pendiente de que nuevos
artículos se publican o que nuevas aplicaciones se descubren para el machine
learning, por no decir de que nuevas e increibles mejoras se podrían realizar a
proyectos anteriores, tales como los llamados 'deep fake'.

Muchas de las herramientas desarrolladas con inteligencia artificial poseen
codigo fuente y bases de datos libremente disponibles para el publico. Ya sea
para fines comerciales o simplemente como demostración, estan aquellas que a su
vez poseen una aplicación web mediante la cual puedes interactuar con los
scripts de una forma directa, realizando manipulación y generación de audio,
imagenes o demás de una forma directa y sencilla, pero no por eso menos eficaz.
De esta manera los usuarios pueden ver el funcionamiento del programa sin
necesidad de compilarlo o de que el autór cree demostraciones, además que ayuda
a difundir el proyecto si se permite la creación de contenidos independientes.

## Tacotron2: Generación de audios donde se leen textos con las voces de personas reales

[Tacotron2](https://github.com/Rayhane-mamah/Tacotron-2) se trata de una
implementación por TensorFlow de una arquitectura de redes neuronales profunda
que busca sintetizar habla a partir de texto. Enlazada a un modelo generativo de
formas de ondas llamado WaveNet, el cual fue utilizado anteriormente para el
mismo proposito, Tacotron2 entrena la red neuronal utilizando una base de datos
de voces anteriormente grabadas para crear espectrogramas en la escala Mel, lo
cual a su vez permite su utilización para emular las voces de personas vivas o
inclusive ya muertas, dado que tengan la suficiente cantidad de grabaciones
disponibles. Los resultados son impresionantes, y se pueden ver, por ejemplo, en
el canal de YouTube llamado
[Vocal Synthesis](https://www.youtube.com/channel/UCRt-fquxnij9wDnFJnpPS2Q),
donde se leen copypastas y demas textos con las voces de Ronald Reagan, The
Notorious B.I.G., Ayn Rand, o inclusive la Reina Elizabeth, o en el sitio
[fifteen.ai](https://fifteen.ai/), donde se pueden generar audios con las voces
de personajes de series animadas.

## Animación de imagénes a partir de un video

En el paper
[First Order Motion Model for Image Animation](https://aliaksandrsiarohin.github.io/first-order-model-website/)
creado por Siarohin et al. en el 2019, se demostró un framework que permite la
creación de animaciónes a partir de una imagén base "fuente" y un video que
"conduce" la animación, mediante el entrenamiento de una red neuronal con videos
de una misma 'categoria'. Lo que esto permite es realizar cosas tales como
cambiar las caras de las personas presentes en una grabación por las de otras,
alterar el estilo de una animación, cambiar la ropa que tiene puesta una persona
en un video, entre otras. Como te podrás imaginar, esto permite la creación
tanto de deepfakes o videos promocionales 'falsos' como de otras alteraciones
(dar vida a la Mona Lisa, por ejemplo), y es increiblemente convincente con la
edición adecuada, como se puede observar en el video suplementario que muestran
[First Order Motion Model for Image Animation](https://www.youtube.com/watch?v=u-0cQ-grXBQ).

## MuseNet: Una red neuronal que 'continua' tu música

[MuseNet](https://openai.com/blog/musenet/) es un proyecto muy simple: se trata
simplemente de una red neuronal profunda que fue creada con el proposito de
crear música. Sus creadores afirman que es capaz de crear piezas de 4 minutos
con 10 instrumentos distintos, "y que puede combinar estilos desde el country
hasta inclusive Mozart o los Beetles". Ya que ha sido entrenada a encontrar
"patrones de armonia, ritmo y estilo aprendiendo a predecir el siguiente token
en cientos de miles de archivos MIDI", se le puede pedir que, por ejemplo,
utilize las primeras 6 notas de un Nocturne de Chopin para generar una pieza con
una instrumentación pop rock, el cual es un ejemplo que se ve en la pagina.
Además, OpenAI permite que cualquiera pruebe la generación de audio mediante
esta red desde la pagina del proyecto para que cualquiera cree nuevas
composiciones.

## Una inteligencia artificial que 'mira' a traves de las paredes mediante señales WiFi

En este paper [RF-Pose](http://rfpose.csail.mit.edu/#Paper) publicado por Zhao
et al. se presenta una aplicación llamada RF-Pose que analiza las señales radio
en las frecuencias WiFi, aprovechandose que estas señales inalambricas traspasan
las paredes y se reflejan del cuerpo humano, para estimar poses 2D. Para estimar
la pose, unicamente es necesaria la señal inalambrica, siendo aspectos
relevantes del individuo tales como altura o anchura predichos a partir de esta.
Por lo tanto, aunque sea igualmente eficaz para predecir poses 2D como lo es la
visión humana, la diferencia radica en que es capaz de predecir estas inclusive
si su 'vision' esta siendo interferida por un obstaculo, tal como una pared. Los
resultados en
[AI Senses People Through Walls](https://www.youtube.com/watch?v=HgDdaMy8KNE)
llegan a ser asombrosos, y a la vez, algo perturbadores.

## Detección de cancer de seno mediante un sistema de inteligencia artificial

La mamografía es la principal herramienta que tienen los medicos a mano para
identificar y prevenir el cancer de seno antes de que síntomas mas serios
ocurran. Sin embargo, exige que hayan expertos que identífiquen y interpreten
dentro de las imagenes generadas por este proceso ciertas anormalidades, lo cual
esta sujeto al error humano y, por lo tanto, sufre de tasas subóptimas de falsos
positivos y negativos. Por lo tanto, en este paper
[International evaluation of an AI system for breast cancer screening](https://deepmind.com/research/publications/International-evaluation-of-an-artificial-intelligence-system-to-identify-breast-cancer-in-screening-mammography)
publicado por Etemadi et al. en el 2020 se buscó crear un sistema que utilizara
la inteligencia artificial para ayudar a los medicos a identíficarlo, y
sorprendentemente, se encontro que el sistema no solamente funcionaba, sino que
reducia los errores de manera significativa, aunque obviamente no era immune a
ellos. También, los autores creen que con este tipo de sistemas se podrían
realizar de una forma mucho mas eficaz esta detección en los paises que no
posean los recursos necesarios para realizarla en números mayores.

## Referencias

- [TensorFlow](https://www.tensorflow.org/)
- [Tacotron2](https://github.com/Rayhane-mamah/Tacotron-2)
- [Vocal Synthesis](https://www.youtube.com/channel/UCRt-fquxnij9wDnFJnpPS2Q)
- [fifteen.ai](https://fifteen.ai/)
- [First Order Motion Model for Image Animation](https://aliaksandrsiarohin.github.io/first-order-model-website/)
- [First Order Motion Model for Image Animation](https://www.youtube.com/watch?v=u-0cQ-grXBQ)
- [MuseNet](https://openai.com/blog/musenet/)
- [RF-Pose](http://rfpose.csail.mit.edu/#Paper)
- [AI Senses People Through Walls](https://www.youtube.com/watch?v=HgDdaMy8KNE)
- [International evaluation of an AI system for breast cancer screening](https://deepmind.com/research/publications/International-evaluation-of-an-artificial-intelligence-system-to-identify-breast-cancer-in-screening-mammography)
