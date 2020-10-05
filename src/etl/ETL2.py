from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL2:
    targetConnection: None

    actividadFrecuecia = {
        "1": "Todos los días",
        "2": "Varias veces a la semana",
        "3": "Una vez a la semana",
        "4": "Una vez al mes",
        "5": "Una vez cada tres meses",
        "6": "Por lo menos una vez al año",
        "7": "Nunca",
        "Null": "Null"
    }

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL2(self):
        self.cargarAnio2012()
        self.cargarAnio2014()
        self.cargarAnio2016()
        self.cargarAnio2017()
    
    def createTemporalTable1(self):
        filepath_1 = "./Encuesta/2012/Caracteristicas_generales/Características generales.sav"
        
        query = "CREATE TEMPORARY TABLE caracteristicas_generales_corte(ID_CARACTERISTICAS_GENERALES_CORTE INT NOT NULL PRIMARY KEY AUTO_INCREMENT, DIRECTORIO VARCHAR(100), Hogarnmero INT, P6008 INT, P5345 INT);"

        self.runQuery(query)

        with savReaderWriter.SavReader(filepath_1) as reader_1:
            header = reader_1.header
            for line in reader_1:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO caracteristicas_generales_corte " +
                        " ( DIRECTORIO, Hogarnmero, P6008, P5345 ) " +
                        "values (" +
                        "\"" + line[0] + "\", " + # Directorio
                        line[2] + ", " + # Hogarnmero
                        line[4] + ", " + # P6008
                        line[5] + " " # P5345
                        ");")
                self.runQuery(query)
    
    def createTemporalTable2(self):
        filepath_2 = "./Encuesta/2012/Caracteristicas_generales_personas_de_5_a_11_anos/Características generales personas de 5 a 11 años.sav"

        query = "CREATE TEMPORARY TABLE caracteristicas_generales_corte_2(ID_CARACTERISTICAS_GENERALES_CORTE_2 INT NOT NULL PRIMARY KEY AUTO_INCREMENT, DIRECTORIO VARCHAR(100), Hogarnmero INT, Personanmero INT);"

        self.runQuery(query)

        with savReaderWriter.SavReader(filepath_2) as reader_2:
            header = reader_2.header
            for line in reader_2:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO caracteristicas_generales_corte_2 " +
                        " ( DIRECTORIO, Hogarnmero, Personanmero ) " +
                        "values (" +
                        "\"" + line[0] + "\", " + # Directorio
                        line[2] + ", " + # Hogarnmero
                        line[3] + "" + # Personanmero
                        ");")
                
                self.runQuery(query)
    
    def createTemporalTable3(self):
        filepath_1 = "./Encuesta/2014/Caracteristicas_Generales/CARACTERISTICAS GENERALES.sav"
        
        query = "CREATE TEMPORARY TABLE caracteristicas_generales_sub(ID_CARACTERISTICAS_GENERALES_SUB INT NOT NULL PRIMARY KEY AUTO_INCREMENT, DIRECTORIO VARCHAR(100), HOGAR_NUMERO INT, P5785 INT);"

        self.runQuery(query)

        with savReaderWriter.SavReader(filepath_1) as reader_1:
            header = reader_1.header
            for line in reader_1:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO caracteristicas_generales_sub " +
                        " ( DIRECTORIO, HOGAR_NUMERO, P5785 ) " +
                        "values (" +
                        "\"" + line[0] + "\", " + # Directorio
                        line[2] + ", " + # HOGAR_NUMERO
                        line[5] + # P6008
                        ");")
                
                self.runQuery(query)
    
    def cargarAnio2012(self):
        self.createTemporalTable1()
        self.createTemporalTable2()

        filepath = "./Encuesta/2012/Tabla_de_hogares/Tabla de hogares.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_temp_1 = "SELECT * FROM caracteristicas_generales_corte WHERE P6008 IS NOT NULL AND P5345 IS NOT NULL AND DIRECTORIO = \""+ line[0] +"\" AND Hogarnmero =  " + line[2]

                temp_1 = self.targetConnection.runQueryWithReturn(query_temp_1)
                temp_1 = temp_1[0] if len(temp_1) > 0 else (0, '', 0, 0, 0 )

                query_temp_2 = "SELECT DIRECTORIO, COUNT(Personanmero) FROM caracteristicas_generales_corte_2 where DIRECTORIO = \"" + line[0] + "\" AND Hogarnmero = " + line[2] + " group by DIRECTORIO" ;
                
                temp_2 = self.targetConnection.runQueryWithReturn(query_temp_2)
                temp_2 = temp_2[0][1] if (len(temp_2) != 0) else 0

                query_insert = ("INSERT INTO Hogares " + 
                    " (DIRECTORIO, HOGAR_NUMERO, P6008, P5345, P258, P259) values (" + 
                    "\"" + line[0] + "\"," + # DIRECTORIO
                    line[2] + ", " + # 
                    str(temp_1[3]) + ", " + # P6008
                    str(temp_1[4]) + ", " + # P5345
                    str(temp_2) + ", " + # P258
                    str(temp_1[3] - temp_1[4] - temp_2 ) + # P259
                    ");")

                self.runQuery(query_insert)

    
    def cargarAnio2014(self):
        self.createTemporalTable3()

        filepath = "./Encuesta/2014/Hogares/HOGARES.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_plus_12 = "SELECT DIRECTORIO, COUNT(P5785) FROM caracteristicas_generales_sub WHERE P5785 >= 12 AND DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2] + " GROUP BY DIRECTORIO;"
                query_5_to_10 = "SELECT DIRECTORIO, COUNT(P5785) FROM caracteristicas_generales_sub WHERE P5785 >= 5 AND P5785 <= 11 AND DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2] + " GROUP BY DIRECTORIO;" 
                query_less_5 = "SELECT DIRECTORIO, COUNT(P5785) FROM caracteristicas_generales_sub WHERE P5785 < 5 AND DIRECTORIO = \"" + line[0] + "\" AND HOGAR_NUMERO = " + line[2] + "  GROUP BY DIRECTORIO;"

                results_plus_12 = self.targetConnection.runQueryWithReturn(query_plus_12)
                results_5_to_10 = self.targetConnection.runQueryWithReturn(query_5_to_10)
                results_less_5 = self.targetConnection.runQueryWithReturn(query_less_5)
                
                results_plus_12 = results_plus_12[0][1] if (len(results_plus_12) != 0) else 0
                results_5_to_11 = results_5_to_10[0][1] if (len(results_5_to_10) != 0) else 0
                results_less_5 = results_less_5[0][1] if (len(results_less_5) != 0) else 0
            
                query_insert = ("INSERT INTO Hogares " + 
                    " (DIRECTORIO, HOGAR_NUMERO, P6008, P5345, P258, P259) values (" + 
                    "\"" + line[0] + "\"," + # DIRECTORIO
                    line[2] + ", " + # HOGAR_NUMERO
                    line[3] + ", " + # P6008
                    str(results_less_5) + ", " + # P5345
                    str(results_5_to_11) + ", " + # P258
                    str(results_plus_12) + # P259
                    ");")

                self.runQuery(query_insert)
    
    def cargarAnio2016(self):
        filepath = "./Encuesta/2016/Hogares/Hogares.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO Hogares " + 
                    " (DIRECTORIO, HOGAR_NUMERO, P6008, P5345, P258, P259, P1700S1, P1700S2, P1700S3, P1700S4) values (" + 
                    "\"" + line[0] + "\"," + 
                    line[2] + ", " + 
                    line[3] + ", " + 
                    line[4] + ", " + 
                    line[5] + ", " + 
                    line[6] + ", " +
                    "\"" + self.actividadFrecuecia[line[8]] + "\", " +
                    "\"" + self.actividadFrecuecia[line[9]] + "\", " +
                    "\"" + self.actividadFrecuecia[line[10]] + "\", " +
                    "\"" + self.actividadFrecuecia[line[11]] + "\"" +
                    ");")

                self.runQuery(query_insert)
    
    def cargarAnio2017(self):
        filepath = "./Encuesta/2017/Hogares/Hogares.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO Hogares " + 
                    " (DIRECTORIO, HOGAR_NUMERO, P6008, P5345, P258, P259, P1700S1, P1700S2, P1700S3, P1700S4) values (" + 
                    "\"" + line[0] + "\"," + # DIRECTORIO
                    line[2] + ", " + # HOGAR_NUMERO
                    line[3] + ", " + # P6008
                    line[4] + ", " + # P5345
                    line[5] + ", " + # P258
                    line[6] + ", " + # P259
                    "\"" + self.actividadFrecuecia[line[7]] + "\", " + # P1700S1
                    "\"" + self.actividadFrecuecia[line[8]] + "\", " + # P1700S2
                    "\"" + self.actividadFrecuecia[line[9]] + "\", " + # P1700S3
                    "\"" + self.actividadFrecuecia[line[10]] + "\"" + # P1700S4
                    ");")
                self.runQuery(query_insert)
    
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.targetConnection.commitChanges()
    
    