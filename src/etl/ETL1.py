from connections.TargetConnection import TargetConnection


import savReaderWriter
import numpy as np

class ETL1:
    targetConnection: None

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL1(self):
        self.crearTemporales()
        anio2012 = ["./Encuesta/2012/Tabla_de_viviendas/Tabla de vivendas.sav", 
                    [0,2,6,7,8,9,10,11,12,13], 
                    "./Encuesta/2012/Caracteristicas_generales/Características generales.sav", 
                    [0,2,9]]
        anio2014 = ["./Encuesta/2014/Viviendas/VIVIENDAS.sav", 
                    [0,2,5,6,7,8,9,10,11,12], 
                    "./Encuesta/2014/Caracteristicas_Generales/CARACTERISTICAS GENERALES.sav", 
                    [0,2,5]]
        anio2016 = ["./Encuesta/2016/Viviendas/Viviendas.sav", 
                    [0,2,4,5,6,7,8,9,10,11], 
                    "./Encuesta/2016/Caracteristicas_generales/Características generales.sav", 
                    [0,2,5]]
        anio2017 = ["./Encuesta/2017/Viviendas/Viviendas.sav", 
                    [0,2,4,5,6,7,8,9,10,11], 
                    "./Encuesta/2017/Caracteristicas_generales/Caracteristicas generales.sav", 
                    [0,2,5]]
        self.cargarTemporales(anio2012)
        self.cargarTemporales(anio2014)
        self.cargarTemporales(anio2016)
        self.cargarHogares("./Encuesta/2012/Tabla_de_hogares/Tabla de hogares.sav")
        self.cargarHogares("./Encuesta/2014/Hogares/HOGARES.sav")
        self.cargarHogares("./Encuesta/2016/Hogares/Hogares.sav")
        self.cargarHogares("./Encuesta/2017/Hogares/Hogares.sav")
        
        self.borrarTemporales()
    
    def crearTemporales(self):
        query_1 = 'CREATE TEMPORARY TABLE vivendas_temporal( id_vivienda INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Directorio VARCHAR(100), Region INT, P4000 INT, P4031S1 INT, P4031S1A1 INT, P4031S2 INT, P4031S3 INT, P4031S4 INT, P4031S4A1 INT, P4031S5 INT );'
        self.runQuery(query_1)
        
        query_2 = 'CREATE TEMPORARY TABLE caracteristicas_temporal( id_persona INT NOT NULL PRIMARY KEY AUTO_INCREMENT,  Directorio VARCHAR(100), Hogarnmero INT, P5785 INT );'
        self.runQuery(query_2)

    def borrarTemporales(self):
        query_1 = 'DROP TABLE IF EXISTS vivendas_temporal;'
        self.runQuery(query_1)
        
        query_2 = 'DROP TABLE IF EXISTS caracteristicas_temporal;'
        self.runQuery(query_2)

    def cargarTemporales(self, params):
        with savReaderWriter.SavReader(params[0]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO vivendas_temporal " +
                        " ( Directorio, Region, P4000, P4031S1, P4031S1A1, P4031S2, P4031S3, P4031S4, P4031S4A1, P4031S5 ) " +
                        "values (" +
                        "\"" + line[params[1][0]] + "\", " +
                        str(line[params[1][1]]) + "," +
                        str(line[params[1][2]]) + "," +
                        str(line[params[1][3]]) + "," +
                        str(line[params[1][4]]) + "," +
                        str(line[params[1][5]]) + "," +
                        str(line[params[1][6]]) + "," +
                        str(line[params[1][7]]) + "," +
                        str(line[params[1][8]]) + "," +
                        str(line[params[1][9]]) +
                        ");" )
                self.runQuery(query)

        with savReaderWriter.SavReader(params[2]) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO caracteristicas_temporal " +
                        " ( Directorio, Hogarnmero, P5785 ) " +
                        "values (" +
                        "\"" + line[params[3][0]] + "\", " +
                        str(line[params[3][1]]) + "," +
                        str(line[params[3][2]]) + 
                        ");")
                self.runQuery(query)

    def cargarHogares(self, filepath):
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_vivienda = "SELECT * FROM vivendas_temporal WHERE Directorio = \"" + line[0] + "\";"
                vivienda = self.targetConnection.runQueryWithReturn(query_vivienda)[0]

                query_total_personas = "SELECT count(Directorio) FROM caracteristicas_temporal WHERE Directorio = \"" + line[0] + "\" AND Hogarnmero = " + str(line[2]) +  ";"
                total_personas = self.targetConnection.runQueryWithReturn(query_total_personas)[0][0]

                query_5_a_11 = "SELECT count(P5785) FROM caracteristicas_temporal WHERE Directorio = \"" + line[0] + "\" AND Hogarnmero = " + str(line[2]) +  "  AND P5785 BETWEEN 5 AND 11;"
                total_5_a_11 = self.targetConnection.runQueryWithReturn(query_5_a_11)[0][0]

                query_mayor_12 = "SELECT count(P5785) FROM caracteristicas_temporal WHERE Directorio = \"" + line[0] + "\" AND Hogarnmero = " + str(line[2]) +  "  AND P5785 >= 12;"
                total_mayor_12 = self.targetConnection.runQueryWithReturn(query_mayor_12)[0][0]

                query = ("INSERT INTO DIM_Hogar " + 
                "(DIRECTORIO, HOGAR_NUMERO, total_personas, total_personas_5_a_11, total_personas_mayor_12, region, tipo_vivienda, servicio_electricidad, servicio_electricidad_estrato, servicio_gas, servicio_alcantarillado, servicio_basura, servicio_basura_recoleccion, servicio_acueducto ) " + 
                " VALUES ( " + 
                "\"" + line[0] + "\", " + 
                str(line[2]) + ", " +
                str(total_personas) + ", " +
                str(total_5_a_11) + ", " +
                str(total_mayor_12) + ", " +
                (str(vivienda[2]) if (vivienda[2] is not None) else "Null") + ", " +
                (str(vivienda[3]) if (vivienda[3] is not None) else "Null") + ", " +
                (str(vivienda[4]) if (vivienda[4] is not None) else "Null") + ", " +
                (str(vivienda[5]) if (vivienda[5] is not None) else "Null") + ", " +
                (str(vivienda[6]) if (vivienda[6] is not None) else "Null") + ", " +
                (str(vivienda[7]) if (vivienda[7] is not None) else "Null") + ", " +
                (str(vivienda[8]) if (vivienda[8] is not None) else "Null") + ", " +
                (str(vivienda[9]) if (vivienda[9] is not None) else "Null") + ", " +
                (str(vivienda[10]) if (vivienda[10] is not None) else "Null") + 
                " );")
                
                self.runQuery(query) 
    
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.targetConnection.commitChanges()