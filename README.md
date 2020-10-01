# Museum Warehouse
Este repositorio contiene los datos relacionados al proyecto #1 de la materia bases de datos avanzados.

## 1. Descripción del negocio a trabajar.

El proyecto está enfocado en el análisis del consumo de contenido cultural en la ciudad de Bogotá realizando un data warehouse que reúna múltiples reportes, encuestas, CSV's y datos. Todas las fuentes de datos serán procesadas para ser analizadas con el propósito de obtener los gustos e intereses de las personas que visitan estos eventos.

## 2. Descripción de las fuentes de datos

Varias fuentes de datos que van a ser usadas en este ejercicio son recopiladas de fuentes de datos abiertas tales como la [página de datos abiertos del gobierno de Colombia](https://www.datos.gov.co/). Los que serán usados son lo siguientes:

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

Esto nos lleva a analizar los datos que queremos extraer de la fuente de datos. Tomando como referencia la estructura de tablas y datos para la encuesta del año 2017 por lo que se escogen las siguientes tablas:

| Tabla 	| Razón 	|
|-	|-	|
| Viviendas 	| Ofrece datos como los socio-económicos, de condición de vida, bienes y servicios que pueden influir en la decisión de consumir contenido cultural de la población 	|
| Hogar 	| Ofrece datos como la cantidad de personas que conforman un hogar y las tareas de tipo cultural que realizan  	|
| Características generales 	| Ofrece un perfil socio-económico (como el nivel de estudios, identificación cultural y género) de cada persona que puedan ser relacionadas con las demás variables 	|
| Presentaciones y espectáculos 	| Ofrece un vistazo del consumo de contenido cultural en distintar presentaciones y distintos lugares, por lo que se escogerán sólo las variables que están involucradas con los sitios previamente mencionados 	|
| Espacios culturales y formacion practica 	| Ofrece un vistazo sobre el uso de espacios culturales, se escogerán las variables que estén relacionadas con los sitios culturales previamente mencionados 	|
| Niños de 5 a 11, presentaciones y espectáculos, publicaciones y audiovisuales 	| Ofrece un vistazo sobre el contenido cultural consumido por niños entre 5 a 11 años, se incluirán únicamente las variables relacionadas al contenido de los sitios culturales previamente definidos 	|
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
| P5378S1 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - a. Ferias taurinas, novilladas, becerradas, coleo o corralejas 	| Si 	| Si 	| Si 	| Si 	|
| P5378S2 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - b. Festivales, ferias de publicaciones (libros) o audiovisuales (cine, televisión, radio y video) 	| Si 	| Si 	| Si 	| Si 	|
| P5378S3 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - c. Carnavales, fiestas o eventos nacionales 	| Si 	| Si 	| Si 	| Si 	|
| P5378S4 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - d. Vio títeres o escuchó cuenteros 	| Si 	| Si 	| Si 	| Si 	|
| P5378S5 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - e. Visitó parques, reservas naturales o zoológicos 	| Si 	| Si 	| Si 	| Si 	|
| P5378S6 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - f. Festivales gastronómicos 	| Si 	| Si 	| Si 	| Si 	|
| P5378S7 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - g. Fiestas municipales o departamentales 	| Si 	| Si 	| Si 	| Si 	|
| P5378S8 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - h. Fue al circo 	| Si 	| Si 	| Si 	| Si 	|
| P5378S9 	| En los últimos 12 meses, ¿asistió a las siguientes actividades culturales?<br>   - i. Asistió a parques temáticos o de diversiones 	| Si 	| Si 	| Si 	| Si 	|


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