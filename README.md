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
| Viviendas 	| Caracterizar las viviendas y los hogares a través de variables socio-económicas, de condición de la vivienda, de acceso a servicios públicos domiciliarios y de tenencia de bienes y servicios. 	| 2017: 14<br>2016: 14<br>2014: 14<br>2012: 14 	| 2017: 8392<br>2016: 8357<br>2014: 8379<br>2012: 8368 	|
| Hogares 	| Esta tabla contiente variables relacionadas con Hogares. 	| 2017: 12<br>2016: 13<br>2014: 7<br>2012: 45 	| 2017: 8532<br>2016: 8527<br>2014: 8623<br>2012: 8636 	|
| Caracteristicas generales 	| Conocer las características básicas de los encuestados para obtener perfiles socio-demográficos, con elpropósito de relacionar esta información con el resto de variables de la investigación. 	| 2017: 14<br>2016: 14<br>2014: 14<br>2012: 18 	| 2017: 26805<br>2016: 26813<br>2014: 28468<br>2012: 26859 	|
| Presentaciones y espectáculos 	| Esta tabla contiente variables relacionadas con fuerza de trabajo, ingresos, tiempo libre y asistencia a presentaciones y espectaculos (personas de 12 años y más). 	| 2017: 68<br>2016: 70<br>2014: 70<br>2012: - 	| 2017: 22013<br>2016: 26813<br>2014: 22826<br>2012: - 	|
| Publicaciones 	| Indagar por la asistencia (servicios culturales) y uso (bienes culturales), frecuencias, tipos de acceso y razones de no uso/asistencia de bienes y servicios culturales. 	| 2017: 142<br>2016: -<br>2014: 155<br>2012: 137 	| 2017: 21077<br>2016: -<br>2014: 21726<br>2012: 21933 	|
| Audiovisuales 	| Describe la asistencia y uso de los diferentes medios audiovisuales a los que tuvo acceso ultimamente (cine, vídeo, videojuegos, televisión, radio y música grabada). 	| 2017: 153<br>2016: 154<br>2014: 151<br>2012: 149 	| 2017: 22013<br>2016: 21883<br>2014: 22826<br>2012: 23252 	|
| Espacios culturales y formacion práctica 	| Determinar asistencia, frecuencia de visitas y razones de no asistencia a espacios culturales. Así mismo conocer las preferencias relacionadas con el acceso a ofertas educativas culturales y artísticas informales. 	| 2017: 104<br>2016: 105<br>2014: 110<br>2012: 94 	| 2017: 22013<br>2016: 21883<br>2014: 22826<br>2012: 23252 	|
| Niños de 5 a 11, presentaciones y espectáculos, publicaciones y audiovisuales 	| Se describen las variables de las características generales de las personas de 5 a 11 años, así como las relacionadas con el tiempo libre, asistencia a presentaciones y espectáculos culturales (conciertos,exposiciones, obras de teatro, danza y ferias artesanales) y publicaciones y audiovisuales. 	| 2017: 61<br>2016: 61<br>2014: 46<br>2012: - 	| 2017: 2938<br>2016: 2950<br>2014: 3476<br>2012: - 	|
| Niños de 5 a 11 espacios culturales y formación practica 	| Describe la asistencias de las personas de 5 a 11 años a los diferentes espacios culturales, formación práctica y hábitos de lectura. 	| 2017: 52<br>2016: 52<br>2014: 52<br>2012: 74 	| 2017: 2938<br>2016: 2950<br>2014: 3476<br>2012: 3607 	|

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

Esto nos lleva a analizar los datos que queremos extraer de la fuente de datos, por lo que se escogen las siguientes tablas:

| Tabla 	| Razón 	|
|-	|-	|
| Viviendas 	| Ofrece datos como los socio-económicos, de condición de vida, bienes y servicios que pueden influir en la decisión de consumir contenido cultural de la población 	|
| Hogar 	| Ofrece datos como la cantidad de personas que conforman un hogar y las tareas de tipo cultural que realizan  	|
| Características generales 	| Ofrece un perfil socio-económico (como el nivel de estudios, identificación cultural y género) de cada persona que puedan ser relacionadas con las demás variables 	|
| Presentaciones y espectáculos 	| Ofrece un vistazo del consumo de contenido cultural en distintar presentaciones y distintos lugares, por lo que se escogerán sólo las variables que están involucradas con los sitios previamente mencionados 	|
| Espacios culturales y formacion practica 	| Ofrece un vistazo sobre el uso de espacios culturales, se escogerán las variables que estén relacionadas con los sitios culturales previamente mencionados 	|
| Niños de 5 a 11, presentaciones y espectáculos, publicaciones y audiovisuales 	| Ofrece un vistazo sobre el contenido cultural consumido por niños entre 5 a 11 años, se incluirán únicamente las variables relacionadas al contenido de los sitios culturales previamente definidos 	|
| Niños de 5 a 11 espacios culturales y formacion practica. 	| Ofrece datos sobre los espacios culturales que los niños de 5 a 11 años frecuentan, se incluirán únicamente las variables relacionadas al contenido y sitios culturales previamente definidos 	|

Y se escogen las siguientes variables:


