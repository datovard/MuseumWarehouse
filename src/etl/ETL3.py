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
        "Null": "Null"
    }

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL3(self):
        self.cargarAnio2012()
    
    def cargarAnio2012(self):
        filepath = "./Encuesta/2012/Caracteristicas_generales/Características generales.sav"

        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: str(int(x)) if (x is not None and x != b'') else "Null" , line))

                query = ("INSERT INTO CaracteristicasGenerales " +
                        " ( ID_HOGAR, P6020, P5785, P5465, P5501, P6160, P6170, P260, P261 ) " +
                        "values (" +
                        "1" + # ID_HOGAR
                        self.definirSexo[line[6]] + ", " + # P6020
                        line[9] + ", " + # P5785
                        self.definirCultura[line[10]] + ", " + # P5465
                        self.definirParentezco[line[11]] + ", " + # P5501
                        self.respuestaBooleana[line[13]] + ", " + # P6160
                        self.respuestaBooleana[line[14]] + ", " + # P6170
                        self.definirEstudios[line[15]] + ", " + # P260
                        line[16] + # P261
                        ");")

                print(line)


    
    