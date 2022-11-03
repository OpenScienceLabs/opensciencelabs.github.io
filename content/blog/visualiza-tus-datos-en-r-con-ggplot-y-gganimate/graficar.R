#Librerías utilizadas
library(rio)
library(ggplot2)
library(gganimate)
library(dplyr)

#Importar archivo Librería requerida "rio"
libro<-import("E:/OpenScience/DatosImportacionBolivia1992-2021.csv")

#Vista previa de libro
head(libro)
View(libro)

#Simplificando nuestra tabla para realizar las gráficas
datos <- data.frame(Fecha = c(libro$Fecha,libro$Fecha,libro$Fecha,libro$Fecha), 
                    Valor = c(libro$`ALIMENTOS Y BEBIDAS`,
                              libro$`SUMINISTROS INDUSTRIALES`,
                              libro$`COMBUSTIBLES Y LUBRICANTES`,
                              libro$`EQUIPO DE TRANSPORTE Y SUS PIEZAS Y ACCESORIOS`), 
                    Clasificacion=c(rep("Alimentos y Bebidas",nrow(libro)),
                                    rep("Suministros Industriales",nrow(libro)),
                                    rep("Combustibles y Lubricantes",nrow(libro)),
                                    rep("Equipo de Transporte",nrow(libro))
                    )
)
head(datos)


datos<-filter(datos,datos$Fecha>=as.Date("2018-01-01"))

#Creando un dataframe para marcar el periodo de la Cuarentena por Covid19
periodos<-data.frame(xmin = as.Date("2020-03-22"), xmax = as.Date("2020-08-31"),
                     ymin = -Inf,ymax=Inf, Periodo = "Confinamiento por COVID19")

#Modificando el theme 
theme_set(theme_bw())

#Guardando en una variable p el objeto de ggplot


#Visualizar la gráfica estática
p1 <- ggplot(data=datos)+
  geom_line(aes(x=Fecha, y=Valor, color=Clasificacion),size=0.5) +
  theme(legend.position = "right")+
  labs(x = "Fecha", y="Valor en MM Bs", color="" , fill="",
       title = "Datos de Importación de Bolivia 1991-2021p",
       subtitle = "Expresado en Millones de Bolivianos")

p1


#Filtrando datos a partir de 2018-01-01
datos<-filter(datos,datos$Fecha>=as.Date("2019-01-01"))

#Agregando nuevos layers a la gráfica
p2 <- ggplot(data=datos)+
  geom_line(aes(x=Fecha, y=Valor, color=Clasificacion),size=1) +
  geom_rect(data = periodos,alpha=0.2,
            aes(xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax,fill=Periodo))+
  theme(legend.position = "right")+
  labs(x = "Fecha", y="Valor en MM Bs", color="" , fill="",
       title = "Datos de Importación Bolivia 2019-2021p",
       subtitle = "Expresado en Millones de Bolivianos")

p2

#Generar Animación
anim <- p2 + transition_reveal(Fecha) + 
  geom_label(aes(x=as.Date("2019-06-01"),y=280, label=format(datos$Fecha,"%Y")),  col = "gray", size = 15)

archivo<-animate(anim, fps = 25, duration = 15, width=800, height=500, end_pause = 30 ) 

anim_save(filename="datosexportpandemia.gif", animation = archivo, path = "E:/OpenScience/")


# limpiar entorno de variables
rm(list = ls()) 


# Cerrar librerías y packages
p_unload(all)  # Remove all add-ons

# Limpiar consola
cat("\014")  # ctrl+L

# Clear mind :)