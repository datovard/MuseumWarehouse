# Museum Warehouse
Este repositorio contiene los datos relacionados al proyecto #1 de la materia bases de datos avanzados.

## 1. Descripción del negocio a trabajar.

El proyecto está enfocado en el análisis del consumo de contenido cultural en el país, realizando un data warehouse que reúna múltiples reportes, encuestas, CSV's y datos. Todas las fuentes de datos serán procesadas para ser analizadas con el propósito de obtener los gustos e intereses de las personas que visitan estos eventos.

## 2. Descripción de las fuentes de datos

### [Encuesta de Consumo Cultural - ECC](https://www.datos.gov.co/Cultura/Encuesta-de-Consumo-Cultural-ECC/c6xg-ctcv):

Esta fuente de datos recopila información obtenida a partir de una encuesta. Se encuentran datos de viviendas, hogares, información socio-económica y los eventos culturales realizados para los años 2017, 2016, 2014, 2012 y 2010. Se incluirán todos los años en el análisis exceptuando el año 2010, que presenta la mayor diferencia estructural de sus datos respecto a los años posteriores.

Diccionario de datos:

Debido al tamaño de cada una de las tablas respecto a la cantidad de variables, registraré aquí una tabla con la descripción de cada componente de datos, la cantidad de variables y la página donde puedes encontrar la descripción de las variables en el diccionario de datos. Éste diccionario lo puedes encontrar en siguiente carpeta dentro de este repositorio:

    ./misc/Diccionario_datos_Encuesta_de_consumo_cultural.pdf

| Tabla 	| Descripción 	| # de variables 	| # de registros 	|
|-	|-	|-	|-	|
| Viviendas 	| Caracterizar las viviendas y los hogares a través de variables<br>socio-económicas, de condición de la vivienda, de acceso a<br>servicios públicos domiciliarios y de tenencia de bienes y<br>servicios. 	| 2017: 14<br>2016: 14<br>2014: 14<br>2012: 14 	| 2017: 8392<br>2016: 8357<br>2014: 8379<br>2012: 8368 	|
| Hogares 	| Esta tabla contiente variables relacionadas con Hogares. 	| 2017: 12<br>2016: 13<br>2014: 7<br>2012: 45 	| 2017: 8532<br>2016: 8527<br>2014: 8623<br>2012: 8636 	|
| Caracteristicas generales 	| Conocer las características básicas de los encuestados para<br>obtener perfiles socio-demográficos, con el propósito de<br>relacionar esta información con el resto de variables de<br>la investigación. 	| 2017: 14<br>2016: 14<br>2014: 14<br>2012: 18 	| 2017: 26805<br>2016: 26813<br>2014: 28468<br>2012: 26859 	|
| Presentaciones y espectáculos 	| Esta tabla contiente variables relacionadas con fuerza de<br>trabajo, ingresos, tiempo libre y asistencia a presentaciones<br>y espectaculos (personas de 12 años y más). 	| 2017: 68<br>2016: 70<br>2014: 70<br>2012: - 	| 2017: 22013<br>2016: 26813<br>2014: 22826<br>2012: - 	|
| Publicaciones 	| Indagar por la asistencia (servicios culturales) y uso<br>(bienes culturales), frecuencias, tipos de acceso y razones<br>de no uso/asistencia de bienes y servicios culturales. 	| 2017: 142<br>2016: -<br>2014: 155<br>2012: 137 	| 2017: 21077<br>2016: -<br>2014: 21726<br>2012: 21933 	|
| Audiovisuales 	| Describe la asistencia y uso de los diferentes medios<br>audiovisuales a los que tuvo acceso ultimamente (cine,<br>vídeo, videojuegos, televisión, radio y música grabada). 	| 2017: 153<br>2016: 154<br>2014: 151<br>2012: 149 	| 2017: 22013<br>2016: 21883<br>2014: 22826<br>2012: 23252 	|
| Espacios culturales y<br>formación práctica 	| Determinar asistencia, frecuencia de visitas y razones<br>de no asistencia a espacios culturales. Así mismo conocer<br>las preferencias relacionadas con el acceso a ofertas<br>educativas culturales y artísticas informales. 	| 2017: 104<br>2016: 105<br>2014: 110<br>2012: 94 	| 2017: 22013<br>2016: 21883<br>2014: 22826<br>2012: 23252 	|
| Niños de 5 a 11, presentaciones<br> y espectáculos, publicaciones<br> y audiovisuales 	| Se describen las variables de las características generales<br>de las personas de 5 a 11 años, así como las relacionadas<br>con el tiempo libre, asistencia a presentaciones y espectáculos<br>culturales (conciertos,exposiciones, obras de teatro, danza y<br>ferias artesanales) y publicaciones y audiovisuales. 	| 2017: 61<br>2016: 61<br>2014: 46<br>2012: - 	| 2017: 2938<br>2016: 2950<br>2014: 3476<br>2012: - 	|
| Niños de 5 a 11 espacios culturales<br>y formación practica 	| Describe la asistencias de las personas de 5 a 11 años a los<br>diferentes espacios culturales, formación práctica y hábitos<br>de lectura. 	| 2017: 52<br>2016: 52<br>2014: 52<br>2012: 74 	| 2017: 2938<br>2016: 2950<br>2014: 3476<br>2012: 3607 	|

### 3. Análisis de la calidad de los datos

Se realiza entonces el análisis de los datos que obtenemos en cada una de las fuentes de datos que son enunciadas en el numeral anterior:

#### Encuesta de Consumo Cultural - ECC

El enfoque principal de este proyecto está basado en los eventos en ubicaciones culturales físicas de la ciudad, tales como:

* Museos
* Bibliotecas
* Teatros
* Galerías de arte
* Salas de exposiciones
* Monumentos históricos
* Sitios arqueológicos
* Monumentos nacionales
* Centros históricos

Esto nos lleva a analizar los datos que queremos extraer de la fuente de datos. Tomando como referencia la estructura de tablas y datos para la encuesta del año 2017 y se busca la información respectiva por cada un de los años anteriores (2016, 2014 y 2012). Por lo que se escogen las siguientes tablas:

| Tabla 	| Razón 	|
|-	|-	|
| Viviendas 	| Ofrece datos como los socio-económicos, de condición de vida, bienes y servicios que pueden influir en la decisión de consumir contenido cultural de la población 	|
| Hogar 	| Ofrece datos como la cantidad de personas que conforman un hogar y las tareas de tipo cultural que realizan  	|
| Características generales 	| Ofrece un perfil socio-económico (como el nivel de estudios, identificación cultural y género) de cada persona que puedan ser relacionadas con las demás variables 	|
| Presentaciones y espectáculos 	| Ofrece un vistazo del consumo de contenido cultural en distintar presentaciones y distintos lugares, por lo que se escogerán sólo las variables que están involucradas con los sitios previamente mencionados 	|
| Espacios culturales y formacion practica 	| Ofrece un vistazo sobre el uso de espacios culturales, se escogerán las variables que estén relacionadas con los sitios culturales previamente mencionados 	|
| Niños de 5 a 11 espacios culturales y formacion practica. 	| Ofrece datos sobre los espacios culturales que los niños de 5 a 11 años frecuentan, se incluirán únicamente las variables relacionadas al contenido y sitios culturales previamente definidos 	|

Se debe tener en cuenta la diferencia de cantidades de variables como se describe en el punto anterior y cuáles son estas variables que no concuerdan, por lo que se obtienen las siguientes variables:

**Vivienda**

| Nombre 	| Etiqueta 	| 2017 	| 2016 	| 2014 	| 2012 	|
|-	|-	|-	|-	|-	|-	|
| DIRECTORIO 	| Consecutivo por vivienda es único 	| Si 	| Si 	| Si 	| Si 	|
| NRO_ENCUESTA 	| Corresponde a la tabla en que se cargo la informacion<br>(233 = vivienda,<br>234=hogar,<br>235=personas) 	| Si 	| Si 	| Si 	| Si 	|
| REGION 	| Region a la que corresponde la vivienda 	| Si 	| Si 	| Si 	| Si 	|
| P4090 	| RESPONDE EL ENCUESTADOR: Condición de la vivienda a entrevistar: 	| Si 	| Si 	| Si 	| No 	|
| P4000 	| Tipo de vivienda 	| Si 	| Si 	| Si 	| Si 	|
| P4031S1 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - a. Energía eléctrica 	| Si 	| Si 	| Si 	| Si 	|
| P4031S1A1 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - a. Energía eléctrica<br>      - Estrato para tarifa 	| Si 	| Si 	| Si 	| Si 	|
| P4031S2 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - b. Gas natural conectado a red pública 	| Si 	| Si 	| Si 	| Si 	|
| P4031S3 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - c. Alcantarillado 	| Si 	| Si 	| Si 	| Si 	|
| P4031S4 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - d. Recolección de basuras 	| Si 	| Si 	| Si 	| Si 	|
| P4031S4A1 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - d. Recolección de basuras<br>      - Veces por semana 	| Si 	| Si 	| Si 	| Si 	|
| P4031S5 	| ¿Con cuáles de los siguientes servicios cuenta la vivienda?<br>   - e. Acueducto 	| Si 	| Si 	| Si 	| Si 	|
| P70 	| Total de hogares en la vivienda 	| Si 	| Si 	| Si 	| No, calculable desde:<br>Tabla de hogares 	|

**Hogares**

| Nombre 	| Etiqueta 	| 2017 	| 2016 	| 2014 	| 2012 	|
|-	|-	|-	|-	|-	|-	|
| DIRECTORIO 	| Consecutivo por vivienda es único 	| Si 	| Si 	| Si 	| Si 	|
| NRO_ENCUESTA 	| Corresponde a la tabla en que se cargo la informacion<br>(233= vivienda,<br>234=hogar,<br>235=personas) 	| Si 	| Si 	| Si 	| Si 	|
| HOGAR_NUMERO 	| Corresponde al número del Hogar 	| Si 	| Si 	| Si 	| Si 	|
| P6008 	| Total de personas en el hogar 	| Si 	| Si 	| Si 	| Si, en:<br>Características generales personas de 5 a 11 años 	|
| P5345 	| Total de personas menores de 5 años en el hogar 	| Si 	| Si 	| No, Calculable 	| Si, en:<br>Características generales personas de 5 a 11 años 	|
| P258 	| Total de personas de 5 a 11 años 	| Si 	| Si 	| No, Calculable:<br>NIÑOS DE 5 A 11 ESPACIOS CULTURALES Y FORMACION Y PRACTICA 	| No, Calculable:<br>Características generales personas de 5 a 11 años 	|
| P259 	| Total de personas de 12 años y más en el hogar 	| Si 	| Si 	| No, Calculable:<br>NIÑOS DE 5 A 11 ESPACIOS CULTURALES Y FORMACION Y PRACTICA 	| No, Calculable:<br>Características generales personas de 5 a 11 años 	|
| P1700S1 	| ¿Cada cuánto se comparten las siguientes actividades con los niños menores de 5 años?<br>   - a. Cantar 	| Si 	| Si 	| No 	| No 	|
| P1700S2 	| ¿Cada cuánto se comparten las siguientes actividades con los niños menores de 5 años?<br>   - b. Leer 	| Si 	| Si 	| No 	| No 	|
| P1700S3 	| ¿Cada cuánto se comparten las siguientes actividades con los niños menores de 5 años?<br>   - c. Contar historias 	| Si 	| Si 	| No 	| No 	|
| P1700S4 	| ¿Cada cuánto se comparten las siguientes actividades con los niños menores de 5 años?<br>   - d. Jugar 	| Si 	| Si 	| No 	| No 	|

**Caracteristicas Generales**

| Nombre 	| Etiqueta 	| 2017 	| 2016 	| 2014 	| 2012 	|
|-	|-	|-	|-	|-	|-	|
| DIRECTORIO 	| Consecutivo por vivienda es único 	| Si 	| Si 	| Si 	| Si 	|
| NRO_ENCUESTA 	| Corresponde a la tabla en que se cargo la informacion<br>(233=vivienda,<br>234=hogar,<br>235= personas) 	| Si 	| Si 	| Si 	| Si 	|
| HOGAR_NUMERO 	| Corresponde al número del Hogar 	| Si 	| Si 	| Si 	| Si 	|
| PERSONA_NUMERO 	| Número de la persona dentro del hogar 	| Si 	| Si 	| Si 	| Si 	|
| P6020 	| Sexo 	| Si 	| Si 	| Si 	| Si 	|
| P5785 	| ¿Cuántos años cumplidos tiene? 	| Si 	| Si 	| Si 	| Si 	|
| P5465 	| De acuerdo con su cultura, pueblo o rasgos físicos usted se reconoce como 	| Si 	| Si 	| Si 	| Si 	|
| P5501 	| ¿Cuál es el parentesco de con el(la) jefe(a) del hogar? 	| Si 	| Si 	| Si 	| Si 	|
| P6160 	| ¿Sabe leer y escribir? 	| Si 	| Si 	| Si 	| Si 	|
| P6170 	| ¿Actualmente asiste al preescolar, escuela, colegio o universidad? 	| Si 	| Si 	| Si 	| Si 	|
| P260 	| ¿cuál es el nivel educativo más alto alcanzado por usted? 	| Si 	| Si 	| Si 	| Si 	|
| P261 	| ¿Actualmente asiste al preescolar, escuela, colegio o universidad?<br>   - a. ¿Cuál es el último año o grado aprobado en este nivel? 	| Si 	| Si 	| Si 	| Si 	|

**Presentaciones y espectaculos**

| Nombre 	| Etiqueta 	| 2017 	| 2016 	| 2014 	| 2012 * como Tiempo Libre	|
|-	|-	|-	|-	|-	|-	|
| DIRECTORIO 	| Consecutivo por vivienda esúnico 	| Si 	| Si 	| Si 	| Si 	|
| HOGAR_NUMERO 	| Número del Hogar 	| Si 	| Si 	| Si 	| Si 	|
| PERSONA_NUMERO 	| Número de la persona dentro del hogar 	| Si 	| Si 	| Si 	| Si 	|
| P6240 	| ¿En qué actividad ocupó la mayor parte del tiempo la semana pasada? 	| Si 	| Si 	| Si 	| Si 	|
| P203 	| ¿Usted recibe algún ingreso mensual? 	| Si 	| Si 	| Si 	| Si 	|
| P203S1 	| ¿Usted recibe algún ingreso mensual?<br>   - ¿cuánto recibe? 	| Si 	| Si 	| Si 	| Si 	|
| P5355 	| En los últimos 12 meses, ¿usted asistió a teatro, danza y ópera? 	| Si 	| Si 	| Si 	| Si 	|
| P5355S1 	| En los últimos 12 meses, ¿usted asistió a teatro, danza y ópera?<br>   - ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5355S2 	| En los últimos 12 meses, ¿usted asistió a teatro, danza y ópera?<br>   - ¿algunas de estas entradas fueron gratuitas? 	| Si 	| Si 	| Si 	| Si 	|
| P204S1 	| Usted no asistió a teatro, danza y ópera por:<br>   - a. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P204S2 	| Usted no asistió a teatro, danza y ópera por:<br>   - b. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P204S3 	| Usted no asistió a teatro, danza y ópera por:<br>   - c. Desconocimiento de la realización de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P204S4 	| Usted no asistió a teatro, danza y ópera por:<br>   - d. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P204S5 	| Usted no asistió a teatro, danza y ópera por:<br>   - e. Las salas y espacios donde realizan estas presentaciones están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P204S6 	| Usted no asistió a teatro, danza y ópera por:<br>   - f. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P204S7 	| Usted no asistió a teatro, danza y ópera por:<br>   - g. Ausencia de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P204S9 	| Usted no asistió a teatro, danza y ópera por:<br>   - h. Falta de compañía 	| Si 	| Si 	| Si 	| Si 	|
| P204S8 	| Usted no asistió a teatro, danza y ópera por:<br>   - i. Otro 	| Si 	| Si 	| Si 	| No 	|
| P5360 	| ¿Pagó usted por entradas a teatro, danza y ópera en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5360S1 	| ¿Pagó usted por entradas a teatro, danza y ópera en los últimos 12 meses?<br>   - ¿cuánto pago? 	| Si 	| Si 	| Si 	| Si 	|
| P5361 	| En los últimos 12 meses, ¿usted asistió a conciertos, recitales, presentaciones de música en espacios abiertos o cerrados en vivo? 	| Si 	| Si 	| Si 	| Si 	|
| P5361S1 	| En los últimos 12 meses, ¿usted asistió a conciertos, recitales, presentaciones de música en espacios abiertos o cerrados en vivo?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5361S2 	| En los últimos 12 meses, ¿usted asistió a conciertos, recitales, presentaciones de música en espacios abiertos o cerrados en vivo?<br>   - b. ¿Algunas de estas entradas fueron gratuitas? 	| Si 	| Si 	| Si 	| Si 	|
| P272S1 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - a. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P272S2 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - b. Las salas y espacios donde los presentan están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P272S3 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - c. Ausencia de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P272S4 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - d. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P272S5 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - e. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P272S6 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - f. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P272S7 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - g. Desconocimiento de la realización de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P272S8 	| Usted no asistió a conciertos, recitales o presentaciones de música en vivo por:<br>   - h. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5366 	| ¿Pagó usted por entradas a conciertos o espectáculos de música en vivo en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5366S1 	| ¿Pagó usted por entradas a conciertos o espectáculos de música en vivo en los últimos 12 meses?<br>   - a. ¿cuánto pagó? 	| Si 	| Si 	| Si 	| Si 	|
| P5367 	| En los últimos 12 meses, ¿usted asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas? 	| Si 	| Si 	| Si 	| Si 	|
| P5367S1 	| En los últimos 12 meses, ¿usted asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5367S2 	| En los últimos 12 meses, ¿usted asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas?<br>   - b. ¿Algunas de estas entradas fueron gratuitas? 	| Si 	| Si 	| Si 	| Si 	|
| P206S1 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - a. Desconocimiento de la realización de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P206S2 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - b. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P206S3 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - c. Ausencia de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P206S4 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - d. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P206S5 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - e. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P206S6 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - f. Las salas y espacios donde realizan estas presentaciones están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P206S7 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - h. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P206S8 	| Usted no asistió a exposiciones, ferias y muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas porque:<br>   - h. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5371 	| ¿Pagó usted por entradas a exposiciones, ferias o muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5371S1 	| ¿Pagó usted por entradas a exposiciones, ferias o muestras de fotografía, pintura, grabado, dibujo, escultura o artes gráficas en los últimos 12 meses?<br>   - a. ¿cuánto pago? 	| Si 	| Si 	| Si 	| Si 	|
| P5372 	| En los últimos 12 meses, ¿asistió a ferias o exposiciones artesanales? 	| Si 	| Si 	| Si 	| Si 	|
| P5372S1 	| En los últimos 12 meses, ¿asistió a ferias o exposiciones artesanales?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5372S2 	| En los últimos 12 meses, ¿asistió a ferias o exposiciones artesanales?<br>   - b. ¿Algunas de estas entradas fueron gratuitas? 	| Si 	| Si 	| Si 	| Si 	|
| P207S1 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - a. Desconocimiento de la realización de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P207S2 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - b. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P207S3 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - c. Ausencia de este tipo de presentaciones 	| Si 	| Si 	| Si 	| Si 	|
| P207S4 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - d. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P207S5 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - e. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P207S6 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - f. Las salas y espacios donde realizan estas presentaciones están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P207S7 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - g. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P207S8 	| Usted no asistió a ferias o exposiciones artesanales por:<br>   - h. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5377 	| ¿Pagó usted por entradas a ferias o exposiciones artesanales en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5377S1 	| ¿Pagó usted por entradas a ferias o exposiciones artesanales en los últimos 12 meses?<br>   - a. ¿cuánto pagó? 	| Si 	| Si 	| Si 	| Si 	|


**Espacios culturales y formacion practica**

| Nombre 	| Etiqueta 	| 2017 	| 2016 	| 2014 	| 2012 * como Asistencia a espacios culturales 	|
|-	|-	|-	|-	|-	|-	|
| DIRECTORIO 	| Consecutivo por vivienda es único 	| Si 	| Si 	| Si 	| Si 	|
| NRO_ENCUESTA 	| Corresponde a la tabla en que se cargo la información<br>(233=vivienda,<br>234=hogar,<br>235=personas) 	| Si 	| Si 	| Si 	| Si 	|
| HOGAR_NUMERO 	| Número del Hogar 	| Si 	| Si 	| Si 	| Si 	|
| PERSONA_NUMERO 	| Número de la persona dentro del hogar 	| Si 	| Si 	| Si 	| Si 	|
| P5436 	| ¿Asistió a bibliotecas en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5436S1 	| ¿Asistió a bibliotecas en los últimos 12 meses?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5438S1 	| A qué tipo de bibliotecas asistió en los últimos 12 meses:<br>   - a. Biblioteca escolar 	| Si 	| Si 	| Si 	| Si 	|
| P5438S2 	| A qué tipo de bibliotecas asistió en los últimos 12 meses:<br>   - b. Biblioteca universitaria 	| Si 	| Si 	| Si 	| Si 	|
| P5438S3 	| A qué tipo de bibliotecas asistió en los últimos 12 meses:<br>   - c. Biblioteca especializada 	| Si 	| Si 	| Si 	| Si 	|
| P5438S4 	| A qué tipo de bibliotecas asistió en los últimos 12 meses:<br>   - d. Biblioteca pública 	| Si 	| Si 	| Si 	| Si 	|
| P1064S1 	| ¿A qué ha ido a la biblioteca en los últimos 12 meses?:<br>   - a. Leer o consultar libros, periódicos o revistas 	| Si 	| Si 	| Si 	| Si 	|
| P1064S2 	| ¿A qué ha ido a la biblioteca en los últimos 12 meses?:<br>   - b. Realizar préstamo externo de libros 	| Si 	| Si 	| Si 	| Si 	|
| P1064S3 	| ¿A qué ha ido a la biblioteca en los últimos 12 meses?:<br>   - c. Hacer uso de materiales audiovisuales (música, películas, documentales) 	| Si 	| Si 	| Si 	| Si 	|
| P1064S4 	| ¿A qué ha ido a la biblioteca en los últimos 12 meses?:<br>   - d. Acceder a computadores e internet 	| Si 	| Si 	| Si 	| Si 	|
| P1064S5 	| ¿A qué ha ido a la biblioteca en los últimos 12 meses?:<br>   - e. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P223S1 	| Usted no asistió a bibliotecas por:<br>   - a. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P223S2 	| Usted no asistió a bibliotecas por:<br>   - b. Están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P223S3 	| Usted no asistió a bibliotecas por:<br>   - c. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P223S4 	| Usted no asistió a bibliotecas por:<br>   - d. Desconocimiento de la existencia de este tipo de espacios 	| Si 	| Si 	| Si 	| Si 	|
| P223S5 	| Usted no asistió a bibliotecas por:<br>   - e. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P223S6 	| Usted no asistió a bibliotecas por:<br>   - f. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P223S7 	| Usted no asistió a bibliotecas por:<br>   - g. Ausencia de este tipo de espacios culturales 	| Si 	| Si 	| Si 	| Si 	|
| P223S9 	| Usted no asistió a bibliotecas por:<br>   - h. Prefiere buscar o consultar información en internet 	| Si 	| Si 	| Si 	| No 	|
| P223S8 	| Usted no asistió a bibliotecas por:<br>   - i. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5447 	| En los últimos 12 meses, ¿visitó museos? 	| Si 	| Si 	| Si 	| Si 	|
| P5447S1 	| En los últimos 12 meses, ¿visitó museos?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P273S2 	| Usted no asistió a museos por:<br>   - a. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P273S1 	| Usted no asistió a museos por:<br>   - b. Están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P273S3 	| Usted no asistió a museos por:<br>   - c. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P273S4 	| Usted no asistió a museos por:<br>   - d. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P273S5 	| Usted no asistió a museos por:<br>   - e. Ausencia de este tipo de espacios culturales 	| Si 	| Si 	| Si 	| Si 	|
| P273S6 	| Usted no asistió a museos por:<br>   - f. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P273S7 	| Usted no asistió a museos por:<br>   - g. Desconocimiento de la existencia de este tipo de espacios 	| Si 	| Si 	| Si 	| Si 	|
| P273S8 	| Usted no asistió a museos por:<br>   - h. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5451 	| ¿Asistió a galerías de arte y salas de exposiciones en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5451S1 	| ¿Asistió a galerías de arte y salas de exposiciones en los últimos 12 meses?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P227S1 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - a. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P227S2 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - b. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P227S3 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - c. Desconocimiento de la existencia de este tipo de espacios 	| Si 	| Si 	| Si 	| Si 	|
| P227S4 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - d. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P227S5 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - e. Están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P227S6 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - f. Ausencia de este tipo de espacios culturales 	| Si 	| Si 	| Si 	| Si 	|
| P227S7 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - g. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P227S8 	| Usted no asistió a galerías de arte y salas de exposiciones por:<br>   - h. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5454 	| En los últimos 12 meses, ¿fue a monumentos históricos, sitios arqueológicos, monumentos nacionales o centros históricos? 	| Si 	| Si 	| Si 	| Si 	|
| P5454S1 	| En los últimos 12 meses, ¿fue a monumentos históricos, sitios arqueológicos,monumentos nacionales o centros históricos?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P228S1 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - a. Problemas de salud o discapacidad 	| Si 	| Si 	| Si 	| Si 	|
| P228S2 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - b. Están lejos 	| Si 	| Si 	| Si 	| Si 	|
| P228S3 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - c. Falta de tiempo 	| Si 	| Si 	| Si 	| Si 	|
| P228S4 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - d. Desinterés/no le gusta 	| Si 	| Si 	| Si 	| Si 	|
| P228S5 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - e. Ausencia de este tipo de espacios culturales 	| Si 	| Si 	| Si 	| Si 	|
| P228S6 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - f. Falta de dinero 	| Si 	| Si 	| Si 	| Si 	|
| P228S7 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - g. Desconocimiento de la existencia de este tipo de espacios 	| Si 	| Si 	| Si 	| Si 	|
| P228S8 	| Usted no fue a monumentos históricos, sitios arqueológicos, monumentos nacionales y centros históricos por:<br>   - h. Otro 	| Si 	| Si 	| Si 	| Si 	|
| P5458 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A1 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - a. Cine, televisión, radio, video 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A2 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - b. Música 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A3 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - c. Teatro, ópera o danza 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A4 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - d. Cuentería o títeres 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A5 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - e. Fotografía, pintura, grabados, dibujos, escultura o artes gráficas 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A6 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - f. Literatura (cuento, narrativa, novela, poesía) o prensa (redacción, géneros periodísticos, revistas, periódicos, magazines digitales o impresos) 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A7 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - g. Artesanías 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A8 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - h. Manualidades 	| Si 	| Si 	| Si 	| Si 	|
| P5458S1A9 	| ¿Usted tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? ¿En qué área?:<br>   - i. Otra área 	| Si 	| Si 	| Si 	| Si 	|

**Niños de 5 a 11 espacios culturales y formacion practica**

| Nombre 	| Etiqueta 	| 2017 	| 2016 	| 2014 	| 2012 	|
|-	|-	|-	|-	|-	|-	|
| DIRECTORIO 	| Consecutivo por vivienda es único 	| Si 	| Si 	| Si 	| Si 	|
| NRO_ENCUESTA 	| Corresponde a la tabla en que se cargo la informacion<br>(233=vivienda,<br>234=hogar,<br>235=personas) 	| Si 	| Si 	| Si 	| Si 	|
| HOGAR_NUMERO 	| Número del Hogar 	| Si 	| Si 	| Si 	| Si 	|
| PERSONA_NUMERO 	| Número de la persona dentro del hogar 	| Si 	| Si 	| Si 	| Si 	|
| P5485 	| ¿El niño o la niña asistió a bibliotecas en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5485S1 	| ¿El niño o la niña asistió a bibliotecas en los últimos 12 meses? <br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5486 	| En los últimos 12 meses, ¿el niño o la niña visitó casas de la cultura?  	| Si 	| Si 	| Si 	| Si 	|
| P5486S1 	| En los últimos 12 meses, ¿el niño o la niña visitó casas de la cultura? <br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5487 	| ¿el niño o la niña asistió a centros culturales en los últimos 12 meses?  	| Si 	| Si 	| Si 	| Si 	|
| P5487S1 	| ¿el niño o la niña asistió a centros culturales en los últimos 12 meses? <br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5488 	| En los últimos 12 meses, ¿el niño o la niña visitó museos? 	| Si 	| Si 	| Si 	| Si 	|
| P5488S1 	| En los últimos 12 meses, ¿el niño o la niña visitó museos?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5489 	| ¿El niño o la niña asistió a galerías de arte y salas de exposiciones en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5489S1 	| ¿El niño o la niña asistió a galerías de arte y salas de exposiciones en los últimos 12 meses?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5490 	| En los últimos 12 meses, ¿el niño o la niña visitó monumentos históricos, sitios arqueológicos, monumentos nacionales o centros históricos? 	| Si 	| Si 	| Si 	| Si 	|
| P5490S1 	| En los últimos 12 meses, ¿el niño o la niña visitó monumentos históricos, sitios arqueológicos, monumentos nacionales o centros históricos?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5491 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5492S1 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - a. Cine, televisión, radio, video 	| Si 	| Si 	| Si 	| Si 	|
| P5492S2 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - b. Música 	| Si 	| Si 	| Si 	| Si 	|
| P5492S3 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - c. Teatro, ópera o danza 	| Si 	| Si 	| Si 	| Si 	|
| P5492S4 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - d. Cuentería o títeres 	| Si 	| Si 	| Si 	| Si 	|
| P5492S5 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - e. Fotografía, pintura, grabados, dibujos, escultura o artes gráficas 	| Si 	| Si 	| Si 	| Si 	|
| P5492S6 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - f. Literatura (cuento, narrativa, novela, poesía) o prensa (redacción, géneros periodísticos, revistas, periódicos, magazines digitales o impresos) 	| Si 	| Si 	| Si 	| Si 	|
| P5492S7 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - g. Artesanías 	| Si 	| Si 	| Si 	| Si 	|
| P5492S8 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - h. Manualidades 	| Si 	| Si 	| Si 	| Si 	|
| P5492S9 	| ¿El niño o la niña tomó cursos o talleres en áreas artísticas y culturales en los últimos 12 meses?<br>   ¿En qué área?:<br>      - i. Otra área 	| Si 	| Si 	| Si 	| Si 	|
| P5494 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural? 	| Si 	| Si 	| Si 	| Si 	|
| P5495S1 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - a. Hizo videos, produjo radio, realizó televisión o participó en producciones de cine 	| Si 	| Si 	| Si 	| Si 	|
| P5495S2 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - b. Tocó algún instrumento, compuso o cantó 	| Si 	| Si 	| Si 	| Si 	|
| P5495S3 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - c. Hizo teatro, practicó danza, participó en ópera 	| Si 	| Si 	| Si 	| Si 	|
| P5495S4 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - d. Hizo títeres, participó en cuentería 	| Si 	| Si 	| Si 	| Si 	|
| P5495S5 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - e. Tomó fotos, pintó, hizo alguna escultura y/o grabado, realizó algún dibujo o arte gráfica 	| Si 	| Si 	| Si 	| Si 	|
| P5495S6 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - f. Escribió textos literarios(cuentos, novelas, poesías) o periodísticos para revistas, periódicos, magazines, blogs 	| Si 	| Si 	| Si 	| Si 	|
| P5495S7 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - g. Realizó algún tipo de artesanía 	| Si 	| Si 	| Si 	| Si 	|
| P5495S8 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - h. Elaboró alguna manualidad 	| Si 	| Si 	| Si 	| Si 	|
| P5495S9 	| En los últimos 12 meses, ¿el niño o la niña hizo alguna práctica cultural?<br>   ¿Qué práctica cultural realizó?:<br>      - i. Otra práctica cultural 	| Si 	| Si 	| Si 	| Si 	|
| P5497 	| ¿El niño o la niña usóinternet en los últimos 3 meses?(en cualquier lugar) 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A1 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - a. Buscar, descargar o escuchar música en línea 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A2 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - b. Ver televisión o escuchar radio en línea 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A3 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - c. Buscar, descargar o leer revistas y periódicos en línea 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A4 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - d. Visitar o acceder a servicios en línea en espacios culturales virtuales (bibliotecas virtuales, museos, galerías) 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A5 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - e. Buscar, descargar o leer libros en línea 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A6 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - f. Buscar, descargar o jugar videojuegos en línea 	| Si 	| Si 	| Si 	| Si 	|
| P5497S1A7 	| ¿El niño o la niña usó internet en los últimos 3 meses? (en cualquier lugar)<br>   Cuando usó internet, ¿lo utilizó para alguna de las siguientes actividades?:<br>       - g. Buscar, descargar o ver películas y/o videos en línea 	| Si 	| Si 	| Si 	| Si 	|
| P5498 	| ¿el niño o la niña desarrolló alguna actividad lúdica o de juego en los últimos 12 meses? 	| Si 	| Si 	| Si 	| Si 	|
| P5498S1 	| ¿el niño o la niña desarrolló alguna actividad lúdica o de juego en los últimos 12 meses?<br>   - a. ¿con qué frecuencia? 	| Si 	| Si 	| Si 	| Si 	|
| P5499S1 	| ¿con quiénes realizó actividades lúdicas o de juego el niño o la niña?<br>   - a. Con su familia 	| Si 	| Si 	| Si 	| Si 	|
| P5499S2 	| ¿con quiénes realizó actividades lúdicas o de juego el niño o la niña?<br>   - b. Con los amigos o compañeros de estudio 	| Si 	| Si 	| Si 	| Si 	|
| P5499S3 	| ¿con quiénes realizó actividades lúdicas o de juego el niño o la niña?<br>   - c. Lo hizo solo(a) 	| Si 	| Si 	| Si 	| Si 	|

### 4. Análisis de requerimientos y pasos par construir modelo multidimensional

#### Objetivos

##### Principal

Se debe recordar que el objetivo principal del proyecto es: <br><br>
El análisis de consumo de contenido cultural en sitios físicos del país.

##### Particulares

Esto define los siguientes objetivos particulares:

1. Analizar los gustos de contenido cultural de la población entrevistada
2. Analizar la relación de las condiciones socio-económicas y demográficas del consumo de contenido cultural
3. Analizar el interés y la asistencia a sitios culturales como museos, galerias de arte, bibliotecas, monumentos históricos, etc.
4. Descubrir contenido cultural que esté fomentando el incremento de consumo cultural.

#### Temporalidad

La máxima granularidad temporal en los datos utilizados es la anualidad, debido a que la realización de la encuesta de consumo es anualmente (2012, 2014, 2016 y 2017) y se presentan años en los que no ha sido realizada (2013, 2015).

#### Dimensionalidad y Hechos

##### Hechos

A partir del objetivo principal del proyecto y de un análisis de las relaciones entre los componentes de las entrevistas se llega a la conclusión de que la tabla de hechos estará compuesta por las Características Generales del entrevistado, conteniendo relaciones importantes para solucionar cada uno de los intereses del proyecto.

##### Dimensiones

Las dimensiones en este proyecto estarán compuestas por:

* Viviendas
* Hogares
* Presentaciones y espectáculos
* Espacios culturales y formación práctica.
* Niños de 5 a 11 espacios culturales y formación práctica.

Las cuales complementan la tabla de hechos sumando datos importantes para los objetivos particulares como el análisis socio-económico y la demografía.

### 5. Modelo Multidimensional

#### Diagrama

![Diagrama](./misc/warehouse-model.png "Warehouse")

### 5. ETL's y llenado de datos

Para el proceso de migración y llenado de datos se analiza el formato en el que está almacenada cada entrevista por cada uno de los años.

Para el año 2017 se almacenó la información en un formato CSV, para los años anteriores se realiza la lectura a partir de archivos .txt

|  	| **Fuentes de extracción** 	| **Transformaciones en los datos** 	|
|-	|-	|-	|
| ETL #1:<br>Vivienda 	| * Tabla de viviendas (2012)<br>* Viviendas (2014)<br>* Viviendas (2016)<br>* Viviendas (2017) 	| - Se pasaron los datos convirtiendo la representación numérica en una cadena que representa la respuesta del entrevistado 	|
| ETL #2:<br>Hogares 	| * Tabla de hogares (2012)<br>* Caracteristicas generales (2012)<br>* Hogares (2014)<br>* Caracteristicas generales (2014)<br>* Hogares (2016)<br>* Hogares (2017) 	| - Se pasaron los datos convirtiendo la representación numérica en una cadena que representa la respuesta del entrevistado<br>- Se tuvo que añadir valores faltantes que podían calcular a partir de valores en otras fuentes 	|
| ETL #3:<br>Caracteristicas Generales 	| * Características generales (2012)<br>* Características generales (2014)<br>* Características generales (2016)<br>* Características generales (2017) 	| - Se pasaron los datos convirtiendo la representación numérica en una cadena que representa la respuesta del entrevistado 	|
| ETL #4:<br>Espacios culturales y formación práctica 	| * Asistencia a espacios culturales (2012)<br>* Asistencia a espacios culturales niños de 5 a 11 años (2012)<br>* Espacios culturales formacion y practica (2014)<br>* Espacios culturales (niños de 5 a 11) (2014)<br>* Espacios culturales y formacion practica (2016)<br>* Ninos de 5 a 11 espacios culturales y formacion practica (2016)<br>* Espacios culturales y formacion practica (2017)<br>* Ninos de 5 a 11 espacios culturales y formacion_practica (2017) 	| - Se pasaron los datos convirtiendo la representación numérica en una cadena que representa la respuesta del entrevistado<br>- Se tuvo que añadir valores faltantes que podían calcular a partir de valores en otras fuentes 	|