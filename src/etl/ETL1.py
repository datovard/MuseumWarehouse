from connections.TargetConnection import TargetConnection

import threading
import savReaderWriter
import numpy as np

class ETL1:
    targetConnection: None
    insertionCounter = 0
    batchSize = 50
    threads = 8
    
    tipo_vivienda = {
        "1": "Casa",
        "2": "Apartamento",
        "3": "Cuarto(s) en inquilinato",
        "4": "Cuarto(s) en otro tipo de estructura",
        "5": "Vivienda indígena",
        "6": "Otra vivienda (carpa, vagón,embarcación, cueva, refugio natural, etc.)"
    }

    respuesta_booleana = {
        "1": "1",
        "2": "0",
        "Null": "-1"
    }

    servicio_electricidad_estrato = {
        "0": "Conexión ilegal",
        "1": "Estrato 1",
        "2": "Estrato 2",
        "3": "Estrato 3",
        "4": "Estrato 4",
        "5": "Estrato 5",
        "6": "Estrato 6",
        "9": "Planta eléctrica o no se puede establecer el estrato",
        "Null": "No definido"
    }

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL1(self):
        anios = [["./Encuesta/2012/Tabla_de_hogares/Tabla de hogares.sav",
                    "./Encuesta/2012/Tabla_de_viviendas/Tabla de vivendas.sav", 
                    [0,2,6,7,8,9,10,11,12,13], 
                    "./Encuesta/2012/Caracteristicas_generales/Características generales.sav", 
                    [0,2,9]],
                ["./Encuesta/2014/Hogares/HOGARES.sav",
                    "./Encuesta/2014/Viviendas/VIVIENDAS.sav", 
                    [0,2,5,6,7,8,9,10,11,12], 
                    "./Encuesta/2014/Caracteristicas_Generales/CARACTERISTICAS GENERALES.sav", 
                    [0,2,5]],
                ["./Encuesta/2016/Hogares/Hogares.sav",
                    "./Encuesta/2016/Viviendas/Viviendas.sav", 
                    [0,2,4,5,6,7,8,9,10,11], 
                    "./Encuesta/2016/Caracteristicas_generales/Características generales.sav", 
                    [0,2,5]],
                ["./Encuesta/2017/Hogares/Hogares.sav",
                    "./Encuesta/2017/Viviendas/Viviendas.sav", 
                    [0,2,4,5,6,7,8,9,10,11], 
                    "./Encuesta/2017/Caracteristicas_generales/Caracteristicas generales.sav", 
                    [0,2,5]]
        ]
        size2012 = len(savReaderWriter.SavReader(anios[0][0]))
        size2014 = len(savReaderWriter.SavReader(anios[1][0]))
        size2016 = len(savReaderWriter.SavReader(anios[2][0]))
        size2017 = len(savReaderWriter.SavReader(anios[3][0]))
        
        self.cargarAnio(anios[0], 0)
        self.cargarAnio(anios[1], size2012)
        self.cargarAnio(anios[2], size2012+size2014)
        self.cargarAnio(anios[3], size2012+size2014+size2016)
        

    def cargarAnio(self, params, start):
        self.cargarHogares(params[0], start)
        self.cargarViviendas(params[1], params[2])
        #self.cargarTotales(params[3], params[4])

    def cargarHogares(self, filepath, start):
        reader = savReaderWriter.SavReader(filepath)
            
        size = len(reader)
        segment = int(size/self.threads)
        threads = list()

        for i in range(self.threads):
            first = i*segment + start
            last = (i+1)*segment - 1 + start if( i < self.threads - 1 ) else (size-1 + start)
            
            t = threading.Thread(target = self.cargarHogaresSegmento, args=(i, first, last, filepath, start))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
    
    def cargarHogaresSegmento(self, thread, first, last, filepath, start):
        insertionCounter = 0
        targetConnection = TargetConnection()
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for i in range(first, last+1):
                line = reader[i-start]
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO DIM_Hogar " + 
                "(ID_HOGAR, DIRECTORIO, HOGAR_NUMERO, total_personas, total_personas_5_a_11, total_personas_mayor_12 ) " + 
                " VALUES ( " + 
                str(i+1) + ", " +
                "\"" + line[0] + "\", " + 
                str(line[2]) + ", " +
                "0,0,0 );")

                targetConnection.runQueryWithoutReturn(query)
                insertionCounter += 1
                if insertionCounter == self.batchSize:
                    targetConnection.commitChanges()
                    insertionCounter = 0
        targetConnection.commitChanges()
            
    def cargarViviendas(self, filepath, index):
        reader = savReaderWriter.SavReader(filepath)
            
        size = len(reader)
        segment = int(size/self.threads)
        threads = list()

        for i in range(self.threads):
            first = i*segment
            last = (i+1)*segment - 1 if( i < self.threads - 1 ) else (size-1)

            t = threading.Thread(target = self.cargarViviendasSegmento, args=(i, filepath, index, first, last ))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
    
    def cargarViviendasSegmento(self, thread, filepath, index, first, last):
        insertionCounter = 0
        targetConnection = TargetConnection()
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for i in range(first, last+1):
                line = reader[i]
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("UPDATE DIM_Hogar SET " + 
                "region = "                         + line[index[1]] + ", " + 
                "tipo_vivienda = \""                + self.tipo_vivienda[line[index[2]]] + "\", " + 
                "servicio_electricidad = "          + self.respuesta_booleana[line[index[3]]] + ", " + 
                "servicio_electricidad_estrato = \""  + self.servicio_electricidad_estrato[line[index[4]]] + "\", " + 
                "servicio_gas = "                   + self.respuesta_booleana[line[index[5]]] + ", " + 
                "servicio_alcantarillado = "        + self.respuesta_booleana[line[index[6]]] + ", " + 
                "servicio_basura = "                + self.respuesta_booleana[line[index[7]]] + ", " + 
                "servicio_basura_recoleccion = "    + line[index[8]] + ", " + 
                "servicio_acueducto = "             + self.respuesta_booleana[line[index[9]]] + " " + 
                " WHERE DIRECTORIO = \"" + line[0] + "\""
                ";")
                
                targetConnection.runQueryWithoutReturn(query)
                insertionCounter += 1
                if insertionCounter == self.batchSize:
                    targetConnection.commitChanges()
                    insertionCounter = 0
        targetConnection.commitChanges()
    
    def cargarTotales(self, filepath, index):
        reader = savReaderWriter.SavReader(filepath)

        size = len(reader)
        segment = int(size/self.threads)
        threads = list()

        for i in range(self.threads):
            first = i*segment
            last = (i+1)*segment - 1 if( i < self.threads - 1 ) else (size-1)
            
            t = threading.Thread(target = self.cargarTotalesSegmento, args=(i, filepath, index, first, last ))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()

    def cargarTotalesSegmento(self, thread, filepath, index, first, last ):
        insertionCounter = 0
        targetConnection = TargetConnection()
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for i in range(first, last+1):
                line = reader[i]
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("UPDATE DIM_Hogar SET " +
                        " total_personas = total_personas + 1 " )
                
                if( int(line[index[2]]) >= 12 ):
                    query += ", total_personas_mayor_12 = total_personas_mayor_12 + 1 "
                else:
                    query += ", total_personas_5_a_11 = total_personas_5_a_11 + 1 "

                query += " WHERE DIRECTORIO = \"" + line[index[0]] + "\" AND HOGAR_NUMERO = " + line[index[1]] + " ;"

                targetConnection.runQueryWithoutReturn(query)
                insertionCounter += 1
                if insertionCounter == self.batchSize:
                    targetConnection.commitChanges()
                    insertionCounter = 0
        targetConnection.commitChanges()