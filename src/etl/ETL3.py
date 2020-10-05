from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL3:
    targetConnection: None

    definirSexo = {
        "1": "Hombre",
        "2": "Mujer"
    }

    definirCultura = {
        "1": "¿Indigena?",
        "2": "¿Gitano (a), rom?",
        "3": "¿Raizal del archipielago de San And´res, Provediencia y Santa Catalina?",
        "4": "¿Palenquero(a) de San Basilio o descendiente?",
        "5": "¿Negro(a), mulato(a), afrocolombiano(a) o afrodescendiente?",
        "6": "¿Mestizo(a)?",
        "7": "¿Blanco(a)?",
        "8": "¿Otro?",
        "99": "No sabe/no informa",
        "Null": "Null"
    }

    definirParentezco = {
        "1": "Jefe(a) del hogar",
        "2": "Pareja, esposo(a), cónyuge, compañero(a)",
        "3": "Hijo(a) o hijastro(a)",
        "4": "Nieto(a)",
        "5": "Otro pariente",
        "6": "Empleado(a) del servicio doméstico y sus parientes",
        "7": "Pensionista, compañero(a) del pensionista",
        "8": "Trabajador",
        "9": "Otro no pariente",
        "Null": "Null"
    }
    
    respuestaBooleana = {
            "1": "Si",
            "2": "No",
            "3": "No sabe/no responde",
            "Null": "Null"
        }
    
    definirEstudios = {
        "1": "Ninguno",
        "2": "Presscolar",
        "3": "Básica Primaria (1°-5°)",
        "4": "Básica Secundaria (6°-9°)",
        "5": "Media (10°-13°)",
        "6": "Superior (Técnica, Tecnológica, Universitaria - pregrado)",
        "7": "Posgrado (especialización, maestría, doctorado)",
        "8": "No sabe/No informa",
        "99": "No sabe/No informa",
        "Null": "Null"
    }

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL3(self):
        self.cargarAnio2012()
        self.cargarAnio2014()
        self.cargarAnio2016()
        self.cargarAnio2017()
    
    def cargarAnio2012(self):
        filepath = "./Encuesta/2012/Caracteristicas_generales/Características generales.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_id_hogar = "SELECT ID_HOGAR FROM Hogares WHERE DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2]

                id_hogar = self.targetConnection.runQueryWithReturn(query_id_hogar)
                id_hogar = id_hogar[0][0]
                
                query_insert = ("INSERT INTO CaracteristicasGenerales " +
                        " ( ID_HOGAR, P6020, P5785, P5465, P5501, P6160, P6170, P260, P261 ) " +
                        "values (" +
                        str(id_hogar) + ", " +  # ID_HOGAR
                        "\"" + self.definirSexo[line[6]] + "\", " + # P6020
                        line[9] + ", " + # P5785
                        (( "\"" + self.definirCultura[line[10]] + "\", " ) if (self.definirCultura[line[10]] != "Null") else ("Null, "))  + # P5465
                        (( "\"" + self.definirParentezco[line[11]] + "\", " ) if (self.definirParentezco[line[11]] != "Null") else ("Null, "))  + # P5501
                        (( "\"" + self.respuestaBooleana[line[13]] + "\", " ) if (self.respuestaBooleana[line[13]] != "Null") else ("Null, "))  + # P6160
                        (( "\"" + self.respuestaBooleana[line[14]] + "\", " ) if (self.respuestaBooleana[line[14]] != "Null") else ("Null, "))  + # P6170
                        (( "\"" + self.definirEstudios[line[15]] + "\", " ) if (self.definirEstudios[line[15]] != "Null") else ("Null, "))  + # P260
                        line[16] + # P261
                        ");")

                self.runQuery(query_insert)
    
    def cargarAnio2014(self):
        filepath = "./Encuesta/2014/Caracteristicas_Generales/CARACTERISTICAS GENERALES.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_id_hogar = "SELECT ID_HOGAR FROM Hogares WHERE DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2]

                id_hogar = self.targetConnection.runQueryWithReturn(query_id_hogar)
                id_hogar = id_hogar[0][0]
                
                query_insert = ("INSERT INTO CaracteristicasGenerales " +
                        " ( ID_HOGAR, P6020, P5785, P5465, P5501, P6160, P6170, P260, P261 ) " +
                        "values (" +
                        str(id_hogar) + ", " +  # ID_HOGAR
                        "\"" + self.definirSexo[line[4]] + "\", " + # P6020
                        line[5] + ", " + # P5785
                        (( "\"" + self.definirCultura[line[6]] + "\", " ) if (self.definirCultura[line[6]] != "Null") else ("Null, "))  + # P5465
                        (( "\"" + self.definirParentezco[line[7]] + "\", " ) if (self.definirParentezco[line[7]] != "Null") else ("Null, "))  + # P5501
                        (( "\"" + self.respuestaBooleana[line[9]] + "\", " ) if (self.respuestaBooleana[line[9]] != "Null") else ("Null, "))  + # P6160
                        (( "\"" + self.respuestaBooleana[line[10]] + "\", " ) if (self.respuestaBooleana[line[10]] != "Null") else ("Null, "))  + # P6170
                        (( "\"" + self.definirEstudios[line[11]] + "\", " ) if (self.definirEstudios[line[11]] != "Null") else ("Null, "))  + # P260
                        line[12] + # P261
                        ");")

                self.runQuery(query_insert)
    
    def cargarAnio2016(self):
        filepath = "./Encuesta/2016/Caracteristicas_generales/Características generales.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_id_hogar = "SELECT ID_HOGAR FROM Hogares WHERE DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2]

                id_hogar = self.targetConnection.runQueryWithReturn(query_id_hogar)
                id_hogar = id_hogar[0][0]
                
                query_insert = ("INSERT INTO CaracteristicasGenerales " +
                        " ( ID_HOGAR, P6020, P5785, P5465, P5501, P6160, P6170, P260, P261 ) " +
                        "values (" +
                        str(id_hogar) + ", " +  # ID_HOGAR
                        "\"" + self.definirSexo[line[4]] + "\", " + # P6020
                        line[5] + ", " + # P5785
                        (( "\"" + self.definirCultura[line[6]] + "\", " ) if (self.definirCultura[line[6]] != "Null") else ("Null, "))  + # P5465
                        (( "\"" + self.definirParentezco[line[7]] + "\", " ) if (self.definirParentezco[line[7]] != "Null") else ("Null, "))  + # P5501
                        (( "\"" + self.respuestaBooleana[line[9]] + "\", " ) if (self.respuestaBooleana[line[9]] != "Null") else ("Null, "))  + # P6160
                        (( "\"" + self.respuestaBooleana[line[10]] + "\", " ) if (self.respuestaBooleana[line[10]] != "Null") else ("Null, "))  + # P6170
                        (( "\"" + self.definirEstudios[line[11]] + "\", " ) if (self.definirEstudios[line[11]] != "Null") else ("Null, "))  + # P260
                        line[12] + # P261
                        ");")

                self.runQuery(query_insert)
    
    def cargarAnio2017(self):
        filepath = "./Encuesta/2017/Caracteristicas_generales/Caracteristicas generales.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_id_hogar = "SELECT ID_HOGAR FROM Hogares WHERE DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2]

                id_hogar = self.targetConnection.runQueryWithReturn(query_id_hogar)
                id_hogar = id_hogar[0][0]
                
                query_insert = ("INSERT INTO CaracteristicasGenerales " +
                        " ( ID_HOGAR, P6020, P5785, P5465, P5501, P6160, P6170, P260, P261 ) " +
                        "values (" +
                        str(id_hogar) + ", " +  # ID_HOGAR
                        "\"" + self.definirSexo[line[4]] + "\", " + # P6020
                        line[5] + ", " + # P5785
                        (( "\"" + self.definirCultura[line[6]] + "\", " ) if (self.definirCultura[line[6]] != "Null") else ("Null, "))  + # P5465
                        (( "\"" + self.definirParentezco[line[7]] + "\", " ) if (self.definirParentezco[line[7]] != "Null") else ("Null, "))  + # P5501
                        (( "\"" + self.respuestaBooleana[line[9]] + "\", " ) if (self.respuestaBooleana[line[9]] != "Null") else ("Null, "))  + # P6160
                        (( "\"" + self.respuestaBooleana[line[10]] + "\", " ) if (self.respuestaBooleana[line[10]] != "Null") else ("Null, "))  + # P6170
                        (( "\"" + self.definirEstudios[line[11]] + "\", " ) if (self.definirEstudios[line[11]] != "Null") else ("Null, "))  + # P260
                        line[12] + # P261
                        ");")

                self.runQuery(query_insert)
    
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.targetConnection.commitChanges()


    
    