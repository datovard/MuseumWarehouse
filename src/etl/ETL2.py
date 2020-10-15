from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL2:
    targetConnection: None
    insertionCounter = 0
    batchSize = 50

    respuesta_booleana = {
        "1": "1",
        "2": "0",
        "Null": "-1"
    }

    frecuencia = {
        "1": "Varias veces a la semana",
        "2": "Una vez a la semana",
        "3": "Una vez al mes",
        "4": "Una vez cada tres meses",
        "5": "Por lo menos una vez al año",
        "Null": "No definido"
    }

    frecuencia_2 = {
        "1": "Casi todos los das",
        "2": "Varias veces a la semana",
        "3": "Una vez a la semana",
        "4": "Una vez al mes",
        "5": "Una vez cada tres meses",
        "6": "Por lo menos una vez al año",
        "Null": "No definido"
    }

    def __init__(self):
       self.targetConnection = TargetConnection()
    
    def startETL2(self):
        self.cargarEncuestaEspaciosCulturales()
        self.cargarEncuestaEspaciosCulturalesMenores12()
        
    def cargarEncuestaEspaciosCulturales(self):
        anio2012 = [ "./Encuesta/2012/Asistencia_a_espacios_culturales/Asistencia a espacios culturales.sav",
                    [4, 14, 15, 16, 17, 
                    None, None, None, None, None, 
                    6, 7, 8, 9, 10, 
                    11, 12, 13, None, 28, 
                    30, 31, 32, 33, 34, 
                    35, 36, 37, 38, 40,
                    41, 42, 43, 44, 45,
                    46, 47, 48, 50, 51,
                    52, 53, 54, 55, 56, 
                    57, 58, 59, 60, 61,
                    62, 63, 64, 65, 66, 
                    67 ],
                    [5, 29, 39, 49 ]]

        anio2014 = [ "./Encuesta/2014/Espacios_culturales_formacion_y_practica/ESPACIOS CULTURALES Y FORMACION Y PRÁCTICA.sav",
                    [4, 15, 16, 17, 18, 
                    19, 20, 21, 22, 23, 
                    6, 7, 8, 9, 10, 
                    11, 12, 13, 14, 44, 
                    46, 47, 48, 49, 50, 
                    51, 52, 53, 54, 56, 
                    57, 58, 59, 60, 61,
                    62, 63, 64, 66, 67,
                    68, 69, 70, 71, 72,
                    73, 74, 75, 76, 77,
                    78, 79, 80, 81, 82,
                    83],
                    [5, 45, 55, 65]]
        
        anio2016 = [ "./Encuesta/2016/Espacios_culturales_y_formacion_practica/Espacios culturales y formación práctica.sav",
                    [4, 15, 16, 17, 18, 
                    19, 20, 21, 22, 23, 
                    6, 7, 8, 9, 10, 
                    11, 12, 13, 14, 44, 
                    46, 47, 48, 49, 50, 
                    51, 52, 53, 54, 56, 
                    57, 58, 59, 60, 61,
                    62, 63, 64, 66, 67,
                    68, 69, 70, 71, 72,
                    73, 74, 75, 76, 77,
                    78, 79, 80, 81, 82,
                    83],
                    [5, 45, 55, 65]]

        anio2017 = [ "./Encuesta/2017/Espacios_culturales_y_formacion_practica/Espacios culturales y formacion practica.sav",
                    [4, 15, 16, 17, 18, 
                    19, 20, 21, 22, 23, 
                    6, 7, 8, 9, 10, 
                    11, 12, 13, 14, 44, 
                    46, 47, 48, 49, 50, 
                    51, 52, 53, 54, 56, 
                    57, 58, 59, 60, 61,
                    62, 63, 64, 66, 67,
                    68, 69, 70, 71, 72,
                    73, 74, 75, 76, 77,
                    78, 79, 80, 81, 82,
                    83],
                    [5, 45, 55, 65]]

        self.cargarEncuesta(anio2012)
        self.cargarEncuesta(anio2014)
        self.cargarEncuesta(anio2016)
        self.cargarEncuesta(anio2017)

    def cargarEncuesta(self, params):
        searchIndexes1 = params[1]
        searchIndexes2 = params[2]
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO DIM_Encuesta_Espacios_Culturales " +
                    " ( DIRECTORIO, HOGAR_NUMERO, PERSONA_NUMERO, " + 
                    " asistio_biblio, " + 
                    " asistio_biblio_escolar, " + 
                    " asistio_biblio_universitaria, " + 
                    " asistio_biblio_especializada, " + 
                    " asistio_biblio_publica, " + 
                    " asistio_biblio_leer_libro, " + 
                    " asistio_biblio_prestamo_libro, " + 
                    " asistio_biblio_consultar_audiovisuales, " + 
                    " asistio_biblio_acceder_internet, " + 
                    " asistio_biblioteca_otro, " + 
                    " no_asistio_biblio_falta_dinero, " + 
                    " no_asistio_biblio_estan_lejos, " + 
                    " no_asistio_biblio_desinteres, " + 
                    " no_asistio_biblio_desconocimiento, " + 
                    " no_asistio_biblio_falta_tiempo, " + 
                    " no_asistio_biblio_problemas_salud, " + 
                    " no_asistio_biblio_ausencia_espacios, " + 
                    " no_asistio_biblio_otro, " + 
                    " no_asistio_biblio_prefiere_internet, " + 
                    " asistio_museos, " + 
                    " no_asistio_museos_estan_lejos, " + 
                    " no_asistio_museos_problemas_salud, " + 
                    " no_asistio_museos_falta_tiempo, " + 
                    " no_asistio_museos_desinteres, " + 
                    " no_asistio_museos_ausencia_espacios, " + 
                    " no_asistio_museos_falta_dinero, " + 
                    " no_asistio_museos_desconocimiento, " + 
                    " no_asistio_museos_otro, " + 
                    " asistio_galeria, " + 
                    " no_asistio_galeria_falta_dinero, " + 
                    " no_asistio_galeria_desinteres, " + 
                    " no_asistio_galeria_desconocimiento, " + 
                    " no_asistio_galeria_problemas_salud, " + 
                    " no_asistio_galeria_estan_lejos, " + 
                    " no_asistio_galeria_ausencia_espacios, " + 
                    " no_asistio_galeria_falta_tiempo, " + 
                    " no_asistio_galeria_otro, " + 
                    " asistio_monumentos, " + 
                    " no_asistio_monumentos_problemas_salud, " + 
                    " no_asistio_monumentos_estan_lejos, " + 
                    " no_asistio_monumentos_falta_tiempo, " + 
                    " no_asistio_monumentos_desinteres, " + 
                    " no_asistio_monumentos_ausencia_espacios, " + 
                    " no_asistio_monumentos_falta_dinero, " + 
                    " no_asistio_monumentos_desconocimiento, " + 
                    " no_asistio_monumentos_otro, " + 
                    " tomo_talleres_artisticos, " + 
                    " tomo_talleres_artisticos_cine_tv_radio, " + 
                    " tomo_talleres_artisticos_musica, " + 
                    " tomo_talleres_artisticos_teatro_danza, " + 
                    " tomo_talleres_artisticos_cuenteria, " + 
                    " tomo_talleres_artisticos_foto_pintura, " + 
                    " tomo_talleres_artisticos_literatura, " + 
                    " tomo_talleres_artisticos_artesanias, " + 
                    " tomo_talleres_artisticos_manualidades, " + 
                    " tomo_talleres_artisticos_otros, " + 

                    " asistio_biblio_frecuencia, " + 
                    " asistio_museos_frecuencia, " + 
                    " asistio_galeria_frecuencia, " + 
                    " asistio_monumentos_frecuencia " + 
                    " ) " +
                    "values (" +
                    "\"" + line[0] + "\", " + # Directorio
                    str(line[2]) + ", " + # HOGAR_NUMERO
                    str(line[3]) + ", ") # PERSONA_NUMERO
                
                for i in range(len(searchIndexes1)):
                    query_insert += self.respuesta_booleana[(str(line[searchIndexes1[i]]) if (searchIndexes1[i] is not None and line[searchIndexes1[i]] is not None) else "Null")] + ", "
                
                for i in range(len(searchIndexes2)):
                    query_insert += "\"" + self.frecuencia[(str(line[searchIndexes2[i]]) if (searchIndexes2[i] is not None and line[searchIndexes2[i]] is not None) else "Null")] + "\""
                    if i < len(searchIndexes2) -1 :
                        query_insert += ", "

                query_insert += ");"

                self.runQuery(query_insert)
    
    def cargarEncuestaEspaciosCulturalesMenores12(self):
        anio2012 = [ "./Encuesta/2012/Asistencia_a_espacios_culturales_personas_de_5_a_11_anos/Asistencia a espacios culturales personas de 5 a 11 años.sav",
                    [4, 5, 10, 11, 12, 
                    13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 
                    23, 24, 25],
                    [5, 11, 13, 15],
                    [46, 48, 49, 50], 47]

        anio2014 = [ "./Encuesta/2014/Espacios_culturales_(ninos_de_5_a_11)/NIÑOS DE 5 A 11 ESPACIOS CULTURALES Y FORMACION Y PRACTICA.sav",
                    [4, 5, 10, 11, 12, 
                    13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 
                    23, 24, 25],
                    [5, 11, 13, 15],
                    [46, 48, 49, 50], 47]
        
        anio2016 = [ "./Encuesta/2016/Ninos_de_5_a_11_espacios_culturales_y_formacion_practica/Niños de 5 a 11 espacios culturales y formación práctica..sav",
                    [4, 5, 10, 11, 12, 
                    13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 
                    23, 24, 25],
                    [5, 11, 13, 15],
                    [46, 48, 49, 50], 47]
        
        anio2017 = [ "./Encuesta/2017/Ninos_de_5_a_11_espacios_culturales_y_formacion_practica/Niños de 5 a 11 espacios culturales y formacion practica..sav",
                    [4, 5, 10, 11, 12, 
                    13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 
                    23, 24, 25],
                    [5, 11, 13, 15],
                    [46, 48, 49, 50], 47]
        
        self.cargarEncuestaMenores(anio2012)
        self.cargarEncuestaMenores(anio2014)
        self.cargarEncuestaMenores(anio2016)
        self.cargarEncuestaMenores(anio2017)
    
    def cargarEncuestaMenores(self, params):
        searchIndexes1 = params[1]
        searchIndexes2 = params[2]
        searchIndexes3 = params[3]
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO DIM_Encuesta_Espacios_Culturales " +
                    " ( DIRECTORIO, HOGAR_NUMERO, PERSONA_NUMERO, " + 
                    "asistio_biblio, " +
                    "asistio_biblio_frecuencia, " +
                    "asistio_museos, " +
                    "asistio_museos_frecuencia, " +
                    "asistio_galeria, " +
                    "asistio_galeria_frecuencia, " +
                    "asistio_monumentos, " +
                    "asistio_monumentos_frecuencia, " +
                    "tomo_talleres_artisticos, " +
                    "tomo_talleres_artisticos_cine_tv_radio, " +
                    "tomo_talleres_artisticos_musica, " +
                    "tomo_talleres_artisticos_teatro_danza, " +
                    "tomo_talleres_artisticos_cuenteria, " +
                    "tomo_talleres_artisticos_foto_pintura, " +
                    "tomo_talleres_artisticos_literatura, " +
                    "tomo_talleres_artisticos_artesanias, " +
                    "tomo_talleres_artisticos_manualidades, " +
                    "tomo_talleres_artisticos_otros " +
                    
                    " ) " +
                    "values (" +
                    "\"" + line[0] + "\", " + # Directorio
                    str(line[2]) + ", " + # HOGAR_NUMERO
                    str(line[3]) + ", ") # PERSONA_NUMERO

                for i in range(len(searchIndexes1)):
                    if(searchIndexes1[i] in searchIndexes2):
                        query_insert += "\"" + self.frecuencia[(str(line[searchIndexes1[i]]) if (searchIndexes1[i] is not None and line[searchIndexes1[i]] is not None) else "Null")] + "\""
                    else:
                        query_insert += self.respuesta_booleana[(str(line[searchIndexes1[i]]) if (searchIndexes1[i] is not None and line[searchIndexes1[i]] is not None) else "Null")]
                    if i < len(searchIndexes1) -1 :
                        query_insert += ", "
                    
                query_insert += ");"

                self.runQuery(query_insert)

                query_insert = ("INSERT INTO DIM_Encuesta_Espacios_Culturales_Menores " +
                    " ( DIRECTORIO, HOGAR_NUMERO, PERSONA_NUMERO, " + 
                    "nino_tomo_actividades_ludicas, " +
                    "nino_actividades_lud_con_familia, " +
                    "nino_actividades_lud_con_companeros, " +
                    "nino_actividades_lud_solo, " +
                    "nino_tomo_actividades_ludicas_frecuencia " +
                    " ) " +
                    "values (" +
                    "\"" + line[0] + "\", " + # Directorio
                    str(line[2]) + ", " + # HOGAR_NUMERO
                    str(line[3]) + ", ") # PERSONA_NUMERO

                for i in range(len(searchIndexes3)):
                    query_insert += self.respuesta_booleana[(str(line[searchIndexes3[i]]) if (searchIndexes3[i] is not None and line[searchIndexes3[i]] is not None) else "Null")] + ", "
                   
                query_insert += "\"" + self.frecuencia_2[ (str(line[params[4]]) if (line[params[4]] is not None) else "Null") ] + "\" "
                    
                query_insert += ");"
                
                self.runQuery(query_insert)
            
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.insertionCounter += 1
        if self.insertionCounter == self.batchSize:
            self.targetConnection.commitChanges()
            self.insertionCounter = 0