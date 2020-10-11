from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL4:
    targetConnection: None

    respuestaBooleana = {
            "1": "Si",
            "2": "No",
            "3": "No sabe/no responde",
            "Null": "Null"
        }

    frecuencias = {
        "1": "Varias veces a la semana",
        "2". "Una vez a la semana",
        "3": "Una vez al mes",
        "4": "Una vez cada tres meses",
        "5": "Por lo menos una vez al año",
        "Null": "Null"
    }

    def __init__(self):
       self.targetConnection = TargetConnection()
    
    def startETL4(self):
        self.cargarAnio2012()
    
    def cargarAnio2012(self):
        filepath = "./Encuesta/2012/Asistencia_a_espacios_culturales/Asistencia a espacios culturales.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query_insert = ("INSERT INTO EspaciosCulturales " +
                        " ( Directorio, P5436, P5436S1, " + 
                        " P5438S1, P5438S2, P5438S3, P5438S4," + 
                        " P1064S1, P1064S2, P1064S3, P1064S4, P1064S5," +
                        " P223S1, P223S2, P223S3, P223S4, P223S5, P223S6, P223S7, P223S8, P223S9, "+
                        " P5447, P5447S1," +
                        " P273S1, P273S2, P273S3, P273S4, P273S5, P273S6, P273S7, P273S8, "+
                        " P5451, P5451S1, P227S1, P227S2, P227S3, P227S4, P227S5, P227S6, P227S7, P227S8, "+
                        " P5454, P5454S1, P228S1, P228S2, P228S3, P228S4, P228S5, P228S6, P228S7, P228S8, "+
                        " P5458, P5458S1A1, P5458S1A2, P5458S1A3, P5458S1A4, P5458S1A5, P5458S1A6, P5458S1A7, P5458S1A8, P5458S1A9 ) " +
                        "values (" +
                        
                        "\"" + line[0] + "\", " + # Directorio
                        
                        (( "\"" + self.respuestaBooleana[line[4]] + "\", " ) if (self.respuestaBooleana[line[4]] != "Null") else ("Null, "))  + # P5436
                        (( "\"" + self.frecuencias[line[5]] + "\", " ) if (self.frecuencias[line[5]] != "Null") else ("Null, "))  + # P5436S1
                        (( "\"" + self.respuestaBooleana[line[14]] + "\", " ) if (self.respuestaBooleana[line[14]] != "Null") else ("Null, "))  + # P5438S1
                        (( "\"" + self.respuestaBooleana[line[15]] + "\", " ) if (self.respuestaBooleana[line[15]] != "Null") else ("Null, "))  + # P5438S2
                        (( "\"" + self.respuestaBooleana[line[16]] + "\", " ) if (self.respuestaBooleana[line[16]] != "Null") else ("Null, "))  + # P5438S3
                        (( "\"" + self.respuestaBooleana[line[17]] + "\", " ) if (self.respuestaBooleana[line[17]] != "Null") else ("Null, "))  + # P5438S4
                        
                        "NULL, " + #P1064S1
                        "NULL, " + #P1064S2
                        "NULL, " + #P1064S3
                        "NULL, " + #P1064S4
                        "NULL, " + #P1064S5

                        (( "\"" + self.respuestaBooleana[line[6]] + "\", " ) if (self.respuestaBooleana[line[6]] != "Null") else ("Null, "))  + # P223S1
                        (( "\"" + self.respuestaBooleana[line[7]] + "\", " ) if (self.respuestaBooleana[line[7]] != "Null") else ("Null, "))  + # P223S2
                        (( "\"" + self.respuestaBooleana[line[8]] + "\", " ) if (self.respuestaBooleana[line[8]] != "Null") else ("Null, "))  + # P223S3
                        (( "\"" + self.respuestaBooleana[line[9]] + "\", " ) if (self.respuestaBooleana[line[9]] != "Null") else ("Null, "))  + # P223S4
                        (( "\"" + self.respuestaBooleana[line[10]] + "\", " ) if (self.respuestaBooleana[line[10]] != "Null") else ("Null, "))  + # P223S5
                        (( "\"" + self.respuestaBooleana[line[11]] + "\", " ) if (self.respuestaBooleana[line[11]] != "Null") else ("Null, "))  + # P223S6
                        (( "\"" + self.respuestaBooleana[line[12]] + "\", " ) if (self.respuestaBooleana[line[12]] != "Null") else ("Null, "))  + # P223S7
                        (( "\"" + self.respuestaBooleana[line[13]] + "\", " ) if (self.respuestaBooleana[line[13]] != "Null") else ("Null, "))  + # P223S8
                        "NULL, " + #P223S9    
                        (( "\"" + self.respuestaBooleana[line[31]] + "\", " ) if (self.respuestaBooleana[line[31]] != "Null") else ("Null, "))  + # P5447
                        (( "\"" + self.frecuencias[line[32]] + "\", " ) if (self.frecuencias[line[32]] != "Null") else ("Null, "))  + # P5447S1

                        (( "\"" + self.respuestaBooleana[line[33]] + "\", " ) if (self.respuestaBooleana[line[33]] != "Null") else ("Null, "))  + # P273S1
                        (( "\"" + self.respuestaBooleana[line[34]] + "\", " ) if (self.respuestaBooleana[line[34]] != "Null") else ("Null, "))  + # P273S2
                        (( "\"" + self.respuestaBooleana[line[35]] + "\", " ) if (self.respuestaBooleana[line[35]] != "Null") else ("Null, "))  + # P273S3
                        (( "\"" + self.respuestaBooleana[line[36]] + "\", " ) if (self.respuestaBooleana[line[36]] != "Null") else ("Null, "))  + # P273S4
                        (( "\"" + self.respuestaBooleana[line[37]] + "\", " ) if (self.respuestaBooleana[line[37]] != "Null") else ("Null, "))  + # P273S5
                        (( "\"" + self.respuestaBooleana[line[38]] + "\", " ) if (self.respuestaBooleana[line[38]] != "Null") else ("Null, "))  + # P273S6
                        (( "\"" + self.respuestaBooleana[line[39]] + "\", " ) if (self.respuestaBooleana[line[39]] != "Null") else ("Null, "))  + # P273S7
                        (( "\"" + self.respuestaBooleana[line[40]] + "\", " ) if (self.respuestaBooleana[line[40]] != "Null") else ("Null, "))  + # P273S8

                        (( "\"" + self.respuestaBooleana[line[41]] + "\", " ) if (self.respuestaBooleana[line[41]] != "Null") else ("Null, "))  + # P5451
                        (( "\"" + self.frecuencias[line[42]] + "\", " ) if (self.frecuencias[line[42]] != "Null") else ("Null, "))  + # P5451S1

                        (( "\"" + self.respuestaBooleana[line[43]] + "\", " ) if (self.respuestaBooleana[line[43]] != "Null") else ("Null, "))  + # P227S1
                        (( "\"" + self.respuestaBooleana[line[44]] + "\", " ) if (self.respuestaBooleana[line[44]] != "Null") else ("Null, "))  + # P227S2
                        (( "\"" + self.respuestaBooleana[line[45]] + "\", " ) if (self.respuestaBooleana[line[45]] != "Null") else ("Null, "))  + # P227S3
                        (( "\"" + self.respuestaBooleana[line[46]] + "\", " ) if (self.respuestaBooleana[line[46]] != "Null") else ("Null, "))  + # P227S4
                        (( "\"" + self.respuestaBooleana[line[47]] + "\", " ) if (self.respuestaBooleana[line[47]] != "Null") else ("Null, "))  + # P227S5
                        (( "\"" + self.respuestaBooleana[line[48]] + "\", " ) if (self.respuestaBooleana[line[48]] != "Null") else ("Null, "))  + # P227S6
                        (( "\"" + self.respuestaBooleana[line[49]] + "\", " ) if (self.respuestaBooleana[line[49]] != "Null") else ("Null, "))  + # P227S7
                        (( "\"" + self.respuestaBooleana[line[50]] + "\", " ) if (self.respuestaBooleana[line[50]] != "Null") else ("Null, "))  + # P227S8

                        (( "\"" + self.respuestaBooleana[line[51]] + "\", " ) if (self.respuestaBooleana[line[51]] != "Null") else ("Null, "))  + # P5454
                        (( "\"" + self.frecuencias[line[52]] + "\", " ) if (self.frecuencias[line[52]] != "Null") else ("Null, "))  + # P5454

                        (( "\"" + self.respuestaBooleana[line[53]] + "\", " ) if (self.respuestaBooleana[line[53]] != "Null") else ("Null, "))  + # P228S1
                        (( "\"" + self.respuestaBooleana[line[54]] + "\", " ) if (self.respuestaBooleana[line[54]] != "Null") else ("Null, "))  + # P228S2
                        (( "\"" + self.respuestaBooleana[line[55]] + "\", " ) if (self.respuestaBooleana[line[55]] != "Null") else ("Null, "))  + # P228S3
                        (( "\"" + self.respuestaBooleana[line[56]] + "\", " ) if (self.respuestaBooleana[line[56]] != "Null") else ("Null, "))  + # P228S4
                        (( "\"" + self.respuestaBooleana[line[57]] + "\", " ) if (self.respuestaBooleana[line[57]] != "Null") else ("Null, "))  + # P228S5
                        (( "\"" + self.respuestaBooleana[line[58]] + "\", " ) if (self.respuestaBooleana[line[58]] != "Null") else ("Null, "))  + # P228S6
                        (( "\"" + self.respuestaBooleana[line[59]] + "\", " ) if (self.respuestaBooleana[line[59]] != "Null") else ("Null, "))  + # P228S7
                        (( "\"" + self.respuestaBooleana[line[60]] + "\", " ) if (self.respuestaBooleana[line[60]] != "Null") else ("Null, "))  + # P228S8

                        (( "\"" + self.respuestaBooleana[line[61]] + "\", " ) if (self.respuestaBooleana[line[61]] != "Null") else ("Null, "))  + # P5458

                        (( "\"" + self.respuestaBooleana[line[62]] + "\", " ) if (self.respuestaBooleana[line[62]] != "Null") else ("Null, "))  + # P5458S1A1
                        (( "\"" + self.respuestaBooleana[line[63]] + "\", " ) if (self.respuestaBooleana[line[63]] != "Null") else ("Null, "))  + # P5458S1A2
                        (( "\"" + self.respuestaBooleana[line[64]] + "\", " ) if (self.respuestaBooleana[line[64]] != "Null") else ("Null, "))  + # P5458S1A3
                        (( "\"" + self.respuestaBooleana[line[65]] + "\", " ) if (self.respuestaBooleana[line[65]] != "Null") else ("Null, "))  + # P5458S1A4
                        (( "\"" + self.respuestaBooleana[line[66]] + "\", " ) if (self.respuestaBooleana[line[66]] != "Null") else ("Null, "))  + # P5458S1A5
                        (( "\"" + self.respuestaBooleana[line[67]] + "\", " ) if (self.respuestaBooleana[line[67]] != "Null") else ("Null, "))  + # P5458S1A6
                        (( "\"" + self.respuestaBooleana[line[68]] + "\", " ) if (self.respuestaBooleana[line[68]] != "Null") else ("Null, "))  + # P5458S1A7
                        (( "\"" + self.respuestaBooleana[line[69]] + "\", " ) if (self.respuestaBooleana[line[69]] != "Null") else ("Null, "))  + # P5458S1A8



                        ")")

                print(line)

    
    