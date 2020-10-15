from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL5:
    targetConnection: None
    insertionCounter = 0
    batchSize = 1000

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL5(self):
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
        lineCounter = 0
        searchIndexes = params[1]
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))
                lineCounter += 1

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
                    " genero, " +               # 0
                    " edad, " +                 # 1
                    " cultura, " +              # 2
                    " parentesco_al_jefe, " +   # 3
                    " estado_civil, " +         # 4
                    " lee_escribe, " +          # 5
                    " estudia_actual, " +       # 6
                    " nivel_educativo, " +      # 7
                    " ultimo_grado, " +         # 8
                    " anio " +                  # 9
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

                try:
                    self.runQuery(query_insert)
                except:
                    self.reportar(params[0], lineCounter, query_insert)
                
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.insertionCounter += 1
        if self.insertionCounter == self.batchSize:
            self.targetConnection.commitChanges()
            self.insertionCounter = 0
    
    def runPreparedQuery(self, query, params):
        results = self.targetConnection.runPreparedQueryWithoutReturn(query, params)
        self.insertionCounter += 1
        if self.insertionCounter == self.batchSize:
            self.targetConnection.commitChanges()
            self.insertionCounter = 0
    
    def reportar(self, filepath, line, query):
        query_insert = "INSERT INTO Reportes (archivo, linea, query) VALUES (%s, %i, %s);"

        self.runPreparedQuery(query_insert, (filepath, line, query))