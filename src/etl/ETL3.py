from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL3:
    targetConnection: None
    insertionCounter = 0
    batchSize = 1000

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL3(self):
        self.cargarEncuestaPresentacionesEspectaculos()
        self.cargarEncuestaPresentacionesEspectaculosMenores12()
        
    def cargarEncuestaPresentacionesEspectaculos(self):
        anio2012 = [ "./Encuesta/2012/Tiempo_libre/Tiempo libre.sav",
                    [38, 39, 40, 41, 42,
                    43, 44, 45, 46, 47,
                    48, None, 49, 50, 51,
                    52, 53, 54, 55, 56,
                    57, 58, 59, 60, 61,
                    62, 63, 64, 65, 66,
                    67, 68, 69, 70, 71,
                    72, 73, 74, 75, 76,
                    77, 78, 79, 80, 81,
                    82, 83, 84, 85, 86,
                    87, 88, 89]]

        anio2014 = [ "./Encuesta/2014/Presentaciones_y_espectaculos/PRESENTACIONES Y ESPECTACULOS.sav",
                    [7, 8, 9, 10, 11,
                    12, 13, 14, 15, 16,
                    17, 18, 19, 20, 21,
                    22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31,
                    32, 33, 34, 35, 36,
                    37, 38, 39, 40, 41,
                    42, 43, 44, 45, 46,
                    47, 48, 49, 50, 51,
                    52, 53, 54, 55, 56,
                    57, 58, 59]]
        
        anio2016 = [ "./Encuesta/2016/Presentaciones_y_espectaculos/Presentaciones y espectaculos.sav",
                    [7, 8, 9, 10, 11,
                    12, 13, 14, 15, 16,
                    18, 17, 19, 20, 21,
                    22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31,
                    32, 33, 34, 35, 36,
                    37, 38, 39, 40, 41,
                    42, 43, 44, 45, 46,
                    47, 48, 49, 50, 51,
                    52, 53, 54, 55, 56,
                    57, 58, 59]]
        
        anio2017 = [ "./Encuesta/2017/Presentaciones_y_espectaculos/Presentaciones y espectaculos.sav",
                    [6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15,
                    17, 16, 18, 19, 20,
                    21, 22, 23, 24, 25,
                    26, 27, 28, 29, 30,
                    31, 32, 33, 34, 35,
                    36, 37, 38, 39, 40,
                    41, 42, 43, 44, 45,
                    46, 47, 48, 49, 50,
                    51, 52, 53, 54, 55,
                    56, 57, 58]]

        self.cargarEncuesta(anio2012)
        self.cargarEncuesta(anio2014)
        self.cargarEncuesta(anio2016)
        self.cargarEncuesta(anio2017)
    
    def cargarEncuesta(self, params):
        searchIndexes = params[1]
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO DIM_Encuesta_Presentaciones_Espectaculos " +
                    " ( DIRECTORIO, HOGAR_NUMERO, PERSONA_NUMERO, " + 
                    " asistio_teatro_danza, " + 
                    " asistio_teatro_danza_frecuencia, " + 
                    " asistio_teatro_danza_gratuitos, " + 
                    " no_asistio_teatro_danza_falta_dinero, " + 
                    " no_asistio_teatro_danza_desinteres, " + 
                    " no_asistio_teatro_danza_desconocimiento, " + 
                    " no_asistio_teatro_danza_falta_tiempo, " + 
                    " no_asistio_teatro_danza_estan_lejos, " + 
                    " no_asistio_teatro_danza_problemas_salud, " + 
                    " no_asistio_teatro_danza_ausencia_espacios, " + 
                    " no_asistio_teatro_danza_otro, " + 
                    " no_asistio_teatro_danza_falta_compania, " + 
                    " asistio_teatro_danza_pago, " + 
                    " asistio_teatro_danza_pago_total, " + 
                    " asistio_concierto_recital, " + 
                    " asistio_concierto_recital_frecuencia, " + 
                    " asistio_concierto_recital_gratuitos, " + 
                    " no_asistio_concierto_recital_falta_dinero, " + 
                    " no_asistio_concierto_recital_estan_lejos, " + 
                    " no_asistio_concierto_recital_ausencia_eventos, " + 
                    " no_asistio_concierto_recital_problemas_salud, " + 
                    " no_asistio_concierto_recital_desinteres, " + 
                    " no_asistio_concierto_recital_falta_tiempo, " + 
                    " no_asistio_concierto_recital_desconocimiento, " + 
                    " no_asistio_concierto_recital_otro, " + 
                    " asistio_concierto_recital_pago, " + 
                    " asistio_concierto_recital_pago_total, " + 
                    " asistio_expo_feria_arte_grafica, " + 
                    " asistio_expo_feria_arte_grafica_frecuencia, " + 
                    " asistio_expo_feria_arte_grafica_gratuitos, " + 
                    " no_asistio_expo_feria_arte_grafica_desconocimiento, " + 
                    " no_asistio_expo_feria_arte_grafica_falta_dinero, " + 
                    " no_asistio_expo_feria_arte_grafica_ausencia_eventos, " + 
                    " no_asistio_expo_feria_arte_grafica_problemas_salud, " + 
                    " no_asistio_expo_feria_arte_grafica_desinteres, " + 
                    " no_asistio_expo_feria_arte_grafica_estan_lejos, " + 
                    " no_asistio_expo_feria_arte_grafica_falta_tiempo, " + 
                    " no_asistio_expo_feria_arte_grafica_otro, " + 
                    " asistio_expo_feria_arte_grafica_pago, " + 
                    " asistio_expo_feria_arte_grafica_pago_total, " + 
                    " asistio_expo_artesanal, " + 
                    " asistio_expo_artesanal_frecuencia, " + 
                    " asistio_expo_artesanal_gratuitos, " + 
                    " no_asistio_expo_artesanal_desconocimiento, " + 
                    " no_asistio_expo_artesanal_falta_dinero, " + 
                    " no_asistio_expo_artesanal_ausencia_eventos, " + 
                    " no_asistio_expo_artesanal_problemas_salud, " + 
                    " no_asistio_expo_artesanal_desinteres, " + 
                    " no_asistio_expo_artesanal_estan_lejos, " + 
                    " no_asistio_expo_artesanal_falta_tiempo, " + 
                    " no_asistio_expo_artesanal_otro, " + 
                    " asistio_expo_artesanal_pago, " + 
                    " asistio_expo_artesanal_pago_total " + 
                    " ) " +
                    "values (" +
                    "\"" + line[0] + "\", " + # Directorio
                    str(line[2]) + ", " + # HOGAR_NUMERO
                    str(line[3]) + ", ") # PERSONA_NUMERO

                for i in range(len(searchIndexes)):
                    query_insert += (str(line[searchIndexes[i]]) if (searchIndexes[i] is not None and line[searchIndexes[i]] is not None) else "Null")
                    if i < len(searchIndexes) -1 :
                        query_insert += ", "
                    
                query_insert += ");"
                
                self.runQuery(query_insert)
    
    def cargarEncuestaPresentacionesEspectaculosMenores12(self):
        anio2012 = [ "./Encuesta/2012/Asistencia_a_espacios_culturales_personas_de_5_a_11_anos/Asistencia a espacios culturales personas de 5 a 11 años.sav",
                    [41, 42, 43, 44, 45, 46, 47, 48]]
        
        anio2014 = [ "./Encuesta/2014/Presentaciones_y_espectaculos_(ninos_de_5_a_11)/NIÑOS DE 5 A 11 PRESENTACIONES Y ESPECTACULOS, PUBLICACIONES Y AUDIOVISUALES.sav",
                    [10, 11, 12, 13, 14, 15, 16, 17]]
        
        anio2016 = [ "./Encuesta/2016/Ninos de 5 a 11, presentaciones y espectaculos, publicaciones y audivisuales/Niños de 5 a 11, presentaciones y espectaculos, publicaciones y audivisuales.sav",
                    [10, 11, 12, 13, 14, 15, 16, 17]]
        
        anio2017 = [ "./Encuesta/2017/Ninos_de_5_a_11_presentaciones_y_espectaculos_publicaciones_y_audivisuales/Niños de 5 a 11, presentaciones y espectaculos, publicaciones y audivisuales.sav",
                    [10, 11, 12, 13, 14, 15, 16, 17]]
        
        self.cargarEncuestaMenores(anio2012)
        self.cargarEncuestaMenores(anio2014)
        self.cargarEncuestaMenores(anio2016)
        self.cargarEncuestaMenores(anio2017)

    def cargarEncuestaMenores(self, params):
        searchIndexes = params[1]
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO DIM_Encuesta_Presentaciones_Espectaculos " +
                    " ( DIRECTORIO, HOGAR_NUMERO, PERSONA_NUMERO, " + 
                    "asistio_teatro_danza, " +
                    "asistio_teatro_danza_frecuencia, " +
                    "asistio_concierto_recital, " +
                    "asistio_concierto_recital_frecuencia, " +
                    "asistio_expo_feria_arte_grafica, " +
                    "asistio_expo_feria_arte_grafica_frecuencia, " +
                    "asistio_expo_artesanal, " +
                    "asistio_expo_artesanal_frecuencia " +
                    " ) " +
                    "values (" +
                    "\"" + line[0] + "\", " + # Directorio
                    str(line[2]) + ", " + # HOGAR_NUMERO
                    str(line[3]) + ", ") # PERSONA_NUMERO

                for i in range(len(searchIndexes)):
                    query_insert += (str(line[searchIndexes[i]]) if (searchIndexes[i] is not None and line[searchIndexes[i]] is not None) else "Null")
                    if i < len(searchIndexes) -1 :
                        query_insert += ", "
                    
                query_insert += ");"
                
                self.runQuery(query_insert)

    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.insertionCounter += 1
        if self.insertionCounter == self.batchSize:
            self.targetConnection.commitChanges()
            self.insertionCounter = 0


    
    