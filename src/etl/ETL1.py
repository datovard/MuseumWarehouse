from connections.TargetConnection import TargetConnection


import savReaderWriter
import numpy as np

class ETL1:
    targetConnection: None

    condicionVivienda = {
        "1": "Ocupada",
        "2": "Vacante/desocupada",
        "3": "Otra"
    }

    regionNames = {
            "1": "Bogotá",
            "2": "Atlantica",
            "3": "Oriental",
            "4": "Central",
            "5": "Pacifica",
            "6": "Amazonía/Orinoquia"
        }
    
    tipoViviendas = {
            "1": "Casa",
            "2": "Apartamento",
            "3": "Cuarto(s) en inquilinato",
            "4": "Cuarto(s) en otro tipo de estructura",
            "5": "Vivienda indígena",
            "6": "Otra vivienda (carpa, vagón, embarcación, cueva, refugio natural, etc.)"
        }
    
    estratoTarifa = {
        "0": "0 (conexión ilegal - pirata)",
        "1": "Estrato 1",
        "2": "Estrato 2",
        "3": "Estrato 3",
        "4": "Estrato 4",
        "5": "Estrato 5",
        "6": "Estrato 6",
        "9": "(planta eléctrica o no se puede establecer el estrato)",
        "Null": "Null"
    }
    
    respuestaBooleana = {
            "1": "Si",
            "2": "No",
            "3": "No sabe/no responde",
            "Null": "Null"
        }

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL1(self):
        self.cargarAnio2012()
        self.cargarAnio2014()
        self.cargarAnio2016()
        self.cargarAnio2017()
    
    def cargarAnio2012(self):
        filepath = "./Encuesta/2012/Tabla_de_viviendas/Tabla de vivendas.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None) else "Null" , line))

                query = ("INSERT INTO Vivienda " +
                        " ( Directorio, Region, P4090, P4000, P4031S1, P4031S1A1, P4031S2, P4031S3, P4031S4, P4031S4A1, P4031S5, P70 ) " +
                        "values (" +
                        "\"" + line[0] + "\", " +
                        "\"" + self.regionNames[line[2]] + "\", " +
                        "NULL, " +
                        "\"" + self.tipoViviendas[line[6]] + "\", " +
                        "\"" + self.respuestaBooleana[line[7]] + "\", " +
                        "\"" + self.estratoTarifa[line[8]] + "\", " +
                        "\"" + self.respuestaBooleana[line[9]] + "\", " +
                        "\"" + self.respuestaBooleana[line[10]] + "\", " +
                        "\"" + self.respuestaBooleana[line[11]] + "\", " +
                        line[12] + ", " +
                        "\"" + self.respuestaBooleana[line[13]] + "\", " +
                        "NULL " +
                        ")")
                self.runQuery(query)
    
    def cargarAnio2014(self):
        filepath = "./Encuesta/2014/Viviendas/VIVIENDAS.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None) else "Null" , line))

                query = ("INSERT INTO Vivienda " +
                        " ( Directorio, Region, P4090, P4000, P4031S1, P4031S1A1, P4031S2, P4031S3, P4031S4, P4031S4A1, P4031S5, P70 ) " +
                        "values (" +
                        "\"" + line[0] + "\", " + # Directorio
                        "\"" + self.regionNames[line[2]] + "\", " + # Region
                        "\"" + self.condicionVivienda[line[4]] + "\"," + # P4090
                        "\"" + self.tipoViviendas[line[5]] + "\", " + # P4000
                        "\"" + self.respuestaBooleana[line[6]] + "\", " + #P4031S1
                        "\"" + self.estratoTarifa[line[7]] + "\", " + # P4031S1A1
                        "\"" + self.respuestaBooleana[line[8]] + "\", " + # P4031S2
                        "\"" + self.respuestaBooleana[line[9]] + "\", " + # P4031S3
                        "\"" + self.respuestaBooleana[line[10]] + "\", " + # P4031S4
                        line[11] + ", " + #P4031S4A1
                        "\"" + self.respuestaBooleana[line[12]] + "\", " + # P4031S5
                        line[13] + # P70
                        ")")
                self.runQuery(query)

    def cargarAnio2016(self):
        filepath = "./Encuesta/2016/Viviendas/Viviendas.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None) else "Null" , line))

                query = ("INSERT INTO Vivienda " +
                        " ( Directorio, Region, P4090, P4000, P4031S1, P4031S1A1, P4031S2, P4031S3, P4031S4, P4031S4A1, P4031S5, P70 ) " +
                        "values (" +
                        "\"" + line[0] + "\", " + # Directorio
                        "\"" + self.regionNames[line[2]] + "\", " + # Region
                        "\"" + self.condicionVivienda[line[3]] + "\"," + # P4090
                        "\"" + self.tipoViviendas[line[4]] + "\", " + # P4000
                        "\"" + self.respuestaBooleana[line[5]] + "\", " + #P4031S1
                        "\"" + self.estratoTarifa[line[6]] + "\", " + # P4031S1A1
                        "\"" + self.respuestaBooleana[line[7]] + "\", " + # P4031S2
                        "\"" + self.respuestaBooleana[line[8]] + "\", " + # P4031S3
                        "\"" + self.respuestaBooleana[line[9]] + "\", " + # P4031S4
                        line[10] + ", " + #P4031S4A1
                        "\"" + self.respuestaBooleana[line[11]] + "\", " + # P4031S5
                        line[12] + # P70
                        ")")
                self.runQuery(query)
    
    def cargarAnio2017(self):
        filepath = "./Encuesta/2017/Viviendas/Viviendas.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO Vivienda " +
                        " ( Directorio, Region, P4090, P4000, P4031S1, P4031S1A1, P4031S2, P4031S3, P4031S4, P4031S4A1, P4031S5, P70 ) " +
                        "values (" +
                        "\"" + line[0] + "\", " + # Directorio
                        "\"" + self.regionNames[line[2]] + "\", " + # Region
                        "\"" + self.condicionVivienda[line[3]] + "\"," + # P4090
                        "\"" + self.tipoViviendas[line[4]] + "\", " + # P4000
                        "\"" + self.respuestaBooleana[line[5]] + "\", " + #P4031S1
                        "\"" + self.estratoTarifa[line[6]] + "\", " + # P4031S1A1
                        "\"" + self.respuestaBooleana[line[7]] + "\", " + # P4031S2
                        "\"" + self.respuestaBooleana[line[8]] + "\", " + # P4031S3
                        "\"" + self.respuestaBooleana[line[9]] + "\", " + # P4031S4
                        line[10] + ", " + #P4031S4A1
                        "\"" + self.respuestaBooleana[line[11]] + "\", " + # P4031S5
                        line[12] + # P70
                        ")")
                self.runQuery(query)
    
    def runQuery(self, query):
        results = self.targetConnection.runQueryWithoutReturn(query)
        self.targetConnection.commitChanges()