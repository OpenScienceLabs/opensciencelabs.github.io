---
title: "Crea tu nube de palabras en R a partir de un documento de texto"
date: 2022-09-25T00:08:03-04:00
draft: false
usePageBundles: true
thumbnail: '/header.png'

featureImage: '/header.png' 
tags: [nube de palabras, r, visualización de datos ]
---

Una nube de palabras o wordcloud nos sirve para visualizar la frecuencia de palabras dentro de un texto.
En este tutorial, usaremos el artículo de [inteligencia artificial](https://es.wikipedia.org/wiki/Inteligencia_artificial) de Wikipedia para construir nuestra nube de palabras usando las bibliotecas `tm` y `wordcloud`.


## Instalación de pre-requisitos

Para un mejor manejo de los paquetes, aquí vamos a utilizar la biblioteca `pacman`, esta nos permitirá hacer una instalación y activación de las bibliotecas de manera rápida. Recuerde instalar **Rtools** y la versión más reciente de **R** si está usando **Windows**.


```r
# install.packages("pacman") # Si no tiene instalada la Biblioteca Pacman ejecutar esta línea de código
library("pacman")
```

Bibliotecas adicionales requeridas, instaladas y abiertas con `pacman`.

```r
p_load("tm") # Biblioteca para realizar el preprocesado del texto,
p_load("tidyverse") # Biblioteca con funciones para manipular datos.
p_load("wordcloud") # Biblioteca para graficar nuestra nube de palabras.
p_load("RColorBrewer") # Biblioteca para seleccionar una paleta de colores de nuestra nube de palabras.
```

## Importación del texto

Para este ejemplo, descargamos nuestro artículo de formato texto de un repositorio, guardamos la dirección web en `articulo_IA` y lo descargamos usando la función `read_file()`. También puede usar los directorios locales para importar un texto de su preferencia. Si desea descargar el archivo que usamos en este ejemplo puede hacer hacerlo ejecutando `download.file("https://gist.github.com/EverVino/7bdbbe7ebdff5987970036f52f0e384f/raw/3a1997b6f9e3471555a941f8812ada0cef84977d/gistfile1.txt", paste(getwd(),"/texto.txt", sep=""))` en la línea de comando de R, esto descargará el archivo y lo guardara en la carpeta de trabajo de R con el nombre de **texto.txt**.

_Para saber la carpeta de trabajo puede ejecutar `getwd()`. puede cambiar la carpeta de trabajo con la función `setwd("/nuevo_directorio_trabajo/")`._

Luego de importar el texto, vamos a convertirlo en un objeto tipo `Source`, esto facilitará la minería del texto y su posterior modificación.

```r
articulo_IA <- "https://gist.github.com/EverVino/7bdbbe7ebdff5987970036f52f0e384f/raw/3a1997b6f9e3471555a941f8812ada0cef84977d/gistfile1.txt"
texto <- read_file(articulo_IA)
```

* `read_file(dir)`: Función de la biblioteca `tidyverse` que nos permite importar archivos de texto. El resultado de la función es un vector de un sólo elemento. `dir` es la **direción local** o **url** con el nombre del archivo de formato **txt** a importar.

```r
texto <- VCorpus(VectorSource(texto), 
                 readerControl = list(reader = readPlain, language = "es"))
```

* `VCorpus (x, readerControl(y))`: Donde `x` es un objeto del tipo `Source`, se recomienda que sea un objeto del tipo `VectorSource`. Para `readerControl(y)` `y` es una lista de parámetros para leer `x`.

* `VectorSource(vector)`: Convierte una lista o vector a un objeto tipo VectorSource. 

## Preprocesado de texto

Una vez importado el texto, tenemos que eliminar la palabras que actúan como conectores, separadores de palabras , de oraciones, y números que no aportarán al análisis del texto, para ello usamos la función `tm_map()` que nos permite aplicar funciones al texto del `Corpus`.

```r
texto <- tm_map(texto, tolower)
texto <- texto %>% 
            tm_map(removePunctuation) %>% 
            tm_map(removeNumbers) %>% 
            tm_map(removeWords, stopwords("spanish"))
texto <- tm_map(texto, removeWords, c("puede", "ser", "pues", "si", "aún", "cómo"))
texto <- tm_map(texto, stripWhitespace)
```

* `tm_map(text, funcion_de_transformacion, parametros_de_funcion)`: Transforma el contenido de texto de un objeto `Corpus` o `VCorpus`, aplicando las funciones de transformación de texto.

* `tolower`: Función de transformación de texto, usado para convertir todas la mayúsculas a minúsculas.

* `removeNumber`: Función para eliminar los números del texto.

* `removeWord`: Función para remover palabras, 

* `stopword("lang")`: Lista de palabras conectoras en el lenguaje lang, es argumento de la función `removeWord`.

* `stripWhitespace`: Función para remover los espacios blancos de un texto.

Nótese que usamos ambas notaciones para transformar el texto del `Corpus`, la notación normal `tm_map(x, FUN)` y también la notación de la biblioteca de `tydiverse` `pipeoperator` `>%>`, que toma como argumento inicial el resultado de la anterior función.

_Si quiere observar los cambios del texto puede ejecutar en la consola `writeLines(as.character(texto[[1]]))`, esto imprimirá el resultado en la consola._

## Construyendo la tabla de frecuencia

```R
texto <- tm_map(texto, PlainTextDocument)
```

* `PlainTextDocument`: Convierte texto a un objeto tipo PlainTextDocument. Para el ejemplo, convierte un `VCorpus` a `PlainTextDocument` el cuál contiene metadatos y nombres de las filas, haciendo factible la conversión a un matriz.


```R
tabla_frecuencia <- DocumentTermMatrix(texto)
```

* `DocumentTermMatrix(texto)`: Convierte texto a un objeto tipo term-document matrix. Es un objeto que va a contener la frecuencia de palabras.


```R
tabla_frecuencia <- cbind(palabras = tabla_frecuencia$dimnames$Terms, 
                          frecuencia = tabla_frecuencia$v)
```

Extraemos los datos que nos interesan del objeto `tabla_frecuencia` y los juntamos con `cbind()`.

_Ejecutando en la consola `View(tabla_frecuencia)` notamos que es un objeto, para acceder a sus valores usamos el símbolo `$` dicho de otra manera: para acceder a las `palabras` usamos `tabla_frecuencia$dimnames$Terms` y para su correspondientes frecuencia en el texto `tabla_frecuencia$v`._


```R
# Convertimos los valores enlazados con cbind a un objeto dataframe.
tabla_frecuencia<-as.data.frame(tabla_frecuencia) 
# Forzamos a que la columna de frecuencia contenga valores numéricos.
tabla_frecuencia$frecuencia<-as.numeric(tabla_frecuencia$frecuencia)
# Ordenamos muestra tabla de frecuencias de acuerdo a sus valores numéricos.
tabla_frecuencia<-tabla_frecuencia[order(tabla_frecuencia$frecuencia, decreasing=TRUE),]
```

_Con estos últimos ajustes ya tenemos nuestra tabla de frecuencias para graficarla._
_Puede verificar los resultados ejecutando en la consola `head(tabla_frecuencia)`_

## Graficando nuestra nube de palabras

Una vez obtenida nuestra tabla de frecuencia sólo es necesario aplicar la función `wordcloud()`.


```R
wordcloud(words = tabla_frecuencia$palabras, 
          freq = tabla_frecuencia$frecuencia, 
          min.freq = 5, 
          max.words = 100, 
          random.order = FALSE, 
          colors = brewer.pal(8,"Paired"))
```

![nube de palabras](../../nube.png)