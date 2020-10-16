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
        self.cargarUniones()

    def cargarUniones(self):
        query = "SELECT COUNT(*) FROM FACT_Persona"
        result = self.targetConnection.runQueryWithReturn(query)
        size = result[0][0]

        query = "SELECT ID_CARACTERISTICAS_GENERALES, DIRECTORIO, HOGAR_NUMERO, PERSONA_NUMERO FROM FACT_Persona"
        result = self.targetConnection.runQueryWithReturn(query)
        
        for persona in result:
            query_hogar = "SELECT ID_HOGAR FROM DIM_Hogar WHERE DIRECTORIO = %s AND HOGAR_NUMERO = %s;"
            query_params = (persona[1], persona[2])
            result = self.targetConnection.runPreparedQueryWithReturn(query_hogar, query_params)
            hogar_id = result[0][0]

            query_params = (persona[1], persona[2], persona[3])
            query_encuesta_cultural = (
                "SELECT ID_ENCUESTA_ESPACIOS_CULTURALES FROM DIM_Encuesta_Espacios_Culturales " +
                " WHERE DIRECTORIO = %s AND HOGAR_NUMERO = %s AND PERSONA_NUMERO = %s" )
            result = self.targetConnection.runPreparedQueryWithReturn(query_encuesta_cultural, query_params)
            encuesta_cultural_id = result[0][0] if( result ) else None

            query_encuesta_cultural_menores = (
                "SELECT ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES FROM DIM_Encuesta_Espacios_Culturales_Menores " + 
                " WHERE DIRECTORIO = %s AND HOGAR_NUMERO = %s AND PERSONA_NUMERO = %s" )
            result = self.targetConnection.runPreparedQueryWithReturn(query_encuesta_cultural_menores, query_params)
            encuesta_cultural_menores_id = result[0][0] if( result ) else None

            query_encuesta_eventos = (
                "SELECT ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS FROM DIM_Encuesta_Presentaciones_Espectaculos "+ 
                " WHERE DIRECTORIO = %s AND HOGAR_NUMERO = %s AND PERSONA_NUMERO = %s")
            result = self.targetConnection.runPreparedQueryWithReturn(query_encuesta_eventos, query_params)
            encuesta_eventos_id = result[0][0] if( result ) else None

            query_update = ("UPDATE FACT_Persona SET " +
                " ID_HOGAR = %s, " + 
                " ID_ENCUESTA_ESPACIOS_CULTURALES = %s, " + 
                " ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES = %s, " + 
                " ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS = %s " + 
                                   
                " WHERE ID_CARACTERISTICAS_GENERALES = %s;" )
            
            query_params = (
                hogar_id,
                encuesta_cultural_id,
                encuesta_cultural_menores_id,
                encuesta_eventos_id,
                persona[0])

            self.runPreparedQuery(query_update, query_params)
                
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