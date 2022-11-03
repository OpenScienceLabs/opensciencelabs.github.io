<!--
.. title: Cómo instalar y comenzar a utilizar Tensorflow
.. slug: como-instalar-y-comenzar-utilizar-tensorflow
.. date: 2020-09-10
.. author: Anavelyz Pérez
.. tags: machine learning
.. category: machine learning
.. link: 
.. description: 
.. type: text
-->

<!-- # Cómo instalar y comenzar a utilizar Tensorflow -->

![header](../../../images/blog/como-instalar-y-comenzar-utilizar-tensorflow/header.png)

Hablar de Tensorflow, es hablar de Machine Learning porque es una plataforma que
permite y facilita la creación de modelos asociados a algoritmos en los que se
configura al equipo involucrado. Esto de manera tal que se obtengan sistemas capaces
de construir y entrenar redes neuronales para detectar y descifrar patrones y
correlaciones análogos al aprendizaje y razonamiento usados por los humanos.

<!-- TEASER_END -->

Tensorflow fue ideado y desarrollado por un equipo de programadores de Google.
El 9 de noviembre de 2015 se publicó bajo una licencia de código abierto Apache 2.0.

## Cómo comenzar a utilizar Tensorflow

Es importante tener en cuenta que antes de instalar y comenzar a utilizar
Tensorflow es necesario contar con conocimientos previos de Machine
Learning, Codificación, Matemáticas y Estadística; esto permitirá que las tareas
de implementación de la plataforma en cualquiera de nuestros proyectos sea más
eficiente.

En el caso de que no se cuente con conocimiento alguno o si simplemente se
quiera ampliar lo que se sabe de estos ámbitos, en el sitio web oficial de
Tensorflow se encuentra una [página
educativa](https://www.tensorflow.org/resources/learn-ml?hl=es) donde está
disponible una serie de herramientas ideadas para instruirse.

Ahora bien, para instalar y utilizar Tensorflow tenemos tres opciones: pip,
docker y Gooogle Colab. Veamos el procedimiento en cada caso.

- Instalar Tensorflow con pip:

1. Se debe tener un entorno de desarrollo de Python en el sistema o tener
   instalado Python a través de una de sus distribuciones. Por ejemplo,
   Anaconda.

Si no tienes idea de los entornos que están disponibles te recomendamos que le
des un vistazo a la información que Real Python nos brinda acerca de ello en:
https://realpython.com/python-ides-code-editors-guide/

2. Luego de que tengas Python en tu sistema verifica que este configurado; se
   requiere la versión de Python entre 3.5 a 3.7 y pip 19.0 o posterior. Para
   esto puedes ejecutar las siguientes líneas de código y observar las versiones.

`python3 --version`
`pip3 --version`
`virtualenv --version`

3. Crear un entorno virtual, este paso es opcional pero se recomienda para
   trabajar de forma separada de los archivos del sistema y así evitar algún error o
   actualización que puede alterar el rendimiento y funcionamiento de este. En
   la página de Tensorflow hay un espacio dedicado a este punto
   https://www.tensorflow.org/install/pip?lang=python3#2.-create-a-virtual-environment-recommended

1. Instalar el paquete de tensorflow con pip, utilizando:

`pip install --upgrade pip` # Esta línea de código permite actualizar pip

`pip install tensorflow`# Con esta línea de código instalaremos Tensorflow

Luego, puedes importar tensorflow como una biblioteca, colocando:

`import tensorflow as tf`

- Docker. Ejecutar un contenedor de Tensorflow.

Docker es una plataforma abierta para desarrollar, enviar y ejecutar
aplicaciones. Con Docker podemos mantener aislados los programas que estemos
ejecutando con los elementos del sistema, aprovechando mejor los recursos lo cual
agregaría velocidad y eficiencia al momento de compilar o ejecutar código.

Para obtener información sobre la instalación de esta plataforma puedes visitar
su [página web](https://docs.docker.com/get-docker/) o seguir la guía que nos
brindan los desarrolladores de Tensorflow en su página
https://www.tensorflow.org/install/docker.

En el caso de tener o haber instalado Docker en tu equipo, con las siguientes
líneas de código puedes obtener Tensorflow:

`docker pull tensorflow/tensorflow:latest-py3`  # Descarga la imagen estable más reciente de Tensorflow

`docker run -it -p 8888:8888 tensorflow/tensorflow:latest-py3-jupyter`  #Inicia un servidor de Jupyter

- Ejecutar Tensorflow desde Google Colab.

Google Colab: Es una plataforma basada en los cuadernos de Jupyter, la cual
permite ejecutar y programar código de Python en tu navegador. No requiere
configuración previa, tendrás acceso gratuito a GPUs y puedes compartir
fácilmente los archivos que hayas creado.

Si no conoces sobre esta herramienta puedes ingresar en
https://colab.research.google.com/notebooks/welcome.ipynbvisitar y seguir la
guía de bienvenida que sus desarrolladores han ideado.

Para comenzar a utilizar Tensorflow en esta herramienta es necesario que se cree
un archivo en esta plataforma, lo cual se puede hacer desde una cuenta de Google
Drive en la opción nuevo, luego seleccionando la opción **más** y finalmente la
opción **Google colaboratory**.

Una vez creado el archivo se tendrán disponibles celdas en las cuales podemos
escribir código de Python. En este caso debemos escribir inicialmente una línea
de código que permita instalar a través de pip la versión de Tensorflow que
necesitemos, esto sería ejecutando:

!pip install tensorflow

Luego podemos verificar la versión mediante

`import tensorflow as tf`

`print(tf.__version__)`

## Lo que puedo hacer con Tensorflow

Después de escoger la herramienta con la cual se trabajará Tensorflow, debemos
tener en cuenta las características del proyecto que se llevará a cabo para de
esta forma establecer el tipo, los parámetros y aquellos elementos esenciales
sobre el modelo. Sin embargo, si aún no se tiene un proyecto definido y solo se
desea empezar a utilizar esta herramienta puedes visitar
https://www.tensorflow.org/tutorials; un sitio web donde se presentan algunas
guías, blogs, vídeos y otros materiales de ayuda.

Por otro lado, es importante destacar que Tensorflow es una plataforma que se
actualiza constantemente y que en el paso del tiempo ha venido incluyendo nuevas
funcionalidades que permiten construir y entrenar modelos de forma tal que el
usuario cuente con una interfaz más amigable, la información sobre los procesos
y errores es más clara y concisa. Un claro ejemplo de esto es tf.keras, una API
que se utiliza para la creación rápida de prototipos, la investigación de
vanguardia (estado-del-arte) y en producción.

Este artículo se puede resumir en que la mejor forma de instruirte sobre esta
herramienta de Machine Learning es visitando su página web
**https://www.tensorflow.org/**, allí tienes mucha información y referencias
educativas bastante completas.
