from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL4:
    targetConnection: None
    insertionCounter = 0
    batchSize = 1000

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL4(self):
        self.cargarEncuestaPresentacionesEspectaculos()

    def cargarEncuestaPresentacionesEspectaculos(self):
        anio2012 = [ "./Encuesta/2012/Caracteristicas_generales/Características generales.sav",
                    [6, 9, 10, 11, 12, 13, 14, 15, 16],
                    "./Encuesta/2012/Tiempo_libre/Tiempo libre.sav",
                    [4, 5, 6],
                    2012]
        
        anio2014 = ["./Encuesta/2014/Caracteristicas_Generales/CARACTERISTICAS GENERALES.sav",
                    [4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "./Encuesta/2014/Presentaciones_y_espectaculos/PRESENTACIONES Y ESPECTACULOS.sav",
                    [4, 5, 6],
                    2014]
        
        anio2016 = ["./Encuesta/2016/Caracteristicas_generales/Características generales.sav",
                    [4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "./Encuesta/2016/Presentaciones_y_espectaculos/Presentaciones y espectaculos.sav",
                    [4, 5, 6],
                    2016]
        
        anio2017 = ["./Encuesta/2017/Caracteristicas_generales/Caracteristicas generales.sav",
                    [4, 5, 6, 7, 8, 9, 10, 11, 12],
                    "./Encuesta/2017/Presentaciones_y_espectaculos/Presentaciones y espectaculos.sav",
                    [3, 4, 5],
                    2017]
        
        self.cargarEncuesta(anio2012)
        self.cargarEncuesta(anio2014)
        self.cargarEncuesta(anio2016)
        self.cargarEncuesta(anio2017)

    def cargarEncuesta(self, params):
        counter = 0
        searchIndexes = params[1]
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_hogar = "SELECT ID_HOGAR FROM DIM_Hogar WHERE DIRECTORIO = \""+ line[0] +"\" AND HOGAR_NUMERO = " + str(line[2])
                hogar_id = self.targetConnection.runQueryWithReturn(query_hogar)
                hogar_id = str(hogar_id[0][0]) if( hogar_id ) else "Null"
                
                query_encuesta_cultural = "SELECT ID_ENCUESTA_ESPACIOS_CULTURALES FROM DIM_Encuesta_Espacios_Culturales WHERE DIRECTORIO = \""+ line[0] +"\" AND HOGAR_NUMERO = " + str(line[2]) + " AND PERSONA_NUMERO = " + str(line[3])
                encuesta_cultural_id = self.targetConnection.runQueryWithReturn(query_encuesta_cultural)
                encuesta_cultural_id = str(encuesta_cultural_id[0][0]) if( encuesta_cultural_id ) else "Null"

                query_encuesta_cultural_menores = "SELECT ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES FROM DIM_Encuesta_Espacios_Culturales_Menores WHERE DIRECTORIO = \""+ line[0] +"\" AND HOGAR_NUMERO = " + str(line[2]) + " AND PERSONA_NUMERO = " + str(line[3])
                encuesta_cultural_menores_id = self.targetConnection.runQueryWithReturn(query_encuesta_cultural_menores)
                encuesta_cultural_menores_id = str(encuesta_cultural_menores_id[0][0]) if( encuesta_cultural_menores_id ) else "Null"

                query_encuesta_eventos = "SELECT ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS FROM DIM_Encuesta_Presentaciones_Espectaculos WHERE DIRECTORIO = \""+ line[0] +"\" AND HOGAR_NUMERO = " + str(line[2]) + " AND PERSONA_NUMERO = " + str(line[3])
                encuesta_eventos_id = self.targetConnection.runQueryWithReturn(query_encuesta_eventos)
                encuesta_eventos_id = str(encuesta_eventos_id[0][0]) if( encuesta_eventos_id ) else "Null"

                query_insert = ("INSERT INTO FACT_Persona " +
                    " (  " + 
                    " DIRECTORIO, " + 
                    " HOGAR_NUMERO, " + 
                    " PERSONA_NUMERO, " + 
                    " ID_HOGAR, " + 
                    " ID_ENCUESTA_ESPACIOS_CULTURALES, " + 
                    " ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES, " + 
                    " ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS, " + 
                    " genero, " + 
                    " edad, " + 
                    " cultura, " + 
                    " parentesco_al_jefe, " + 
                    " estado_civil, " + 
                    " lee_escribe, " + 
                    " estudia_actual, " + 
                    " nivel_educativo, " + 
                    " ultimo_grado, " + 
                    " anio " + 
                    " ) " +
                    "values (" +
                    "\"" + line[0] + "\", " +
                    str(line[2]) + ", " +
                    str(line[3]) + ", " +
                    (hogar_id) + ", " +
                    (encuesta_cultural_id) + ", " + 
                    (encuesta_cultural_menores_id) + ", " +
                    (encuesta_eventos_id) + ", "
                    )

                for i in range(len(searchIndexes)):
                    query_insert += (str(line[searchIndexes[i]]) if (searchIndexes[i] is not None and line[searchIndexes[i]] is not None) else "Null") + ", "
                
                query_insert += str(params[4]) + ");"
                
                self.runQuery(query_insert)
        
        counter = 0
        searchIndexes = params[3]
        with savReaderWriter.SavReader(params[2]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("UPDATE FACT_Persona SET " +
                    "actividad_semana_pasada = " + str(line[searchIndexes[0]]) + ", " +
                    "recibe_ingreso_mensual = " + str(line[searchIndexes[1]]) + ", " +
                    "ingreso_total = " + str(line[searchIndexes[2]]) +
                    " WHERE DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + str(line[2]) + " AND PERSONA_NUMERO = " + str(line[3]) +
                    ";")
                
                self.runQuery(query_insert)
        
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.insertionCounter += 1
        if self.insertionCounter == self.batchSize:
            self.targetConnection.commitChanges()
            self.insertionCounter = 0