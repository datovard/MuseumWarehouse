from connections.TargetConnection import TargetConnection

import savReaderWriter
import numpy as np

class ETL4:
    targetConnection: None
    insertionCounter = 0
    batchSize = 1000

    genero = {
        1: "Hombre",
        2: "Mujer"
    }

    cultura = {
        1: "Indigena",
        2: "Gitano(a)",
        3: "Raizal del archipiélago de San Andrés, Providiencia y Santa Catalina",
        4: "Palenquero(a) de San Basilio odescendiente",
        5: "Negro(a), mulato(a), afrocolombiano(a) o afrodescendiente",
        6: "Mestizo(a)",
        7: "Blanco(a)",
        8: "Otro",
        99: "No sabe/no informa",
        "Null": "No registrado",
        None: "No registrado"
    }

    parentezco = {
        1: "Jefe(a) del hogar",
        2: "Pareja, esposo(a), cónyuge, compañero(a)",
        3: "Hijo(a) o hijastro(a)",
        4: "Nieto(a)",
        5: "Otro pariente",
        6: "Empleado(a) del servicio doméstico y sus parientes",
        7: "Pensionista, compañero(a) del pensionista",
        8: "Trabajador",
        9: "Otro no pariente",
        None: "No registrado"
    }

    estado_civil = {
        1: "No está casado(a) y vive en pareja hace menos de dos años",
        2: "No está casado(a) y vive en pareja hace dos años o más",
        3: "Está casado(a)",
        4: "Está separado(a) o divorciado(a)",
        5: "Está viudo(a)",
        6: "Está soltero(a)",
        None: "No registrado"
    }

    respuesta_booleana = {
        1: "1",
        2: "0",
        None: "-1",
        99: "-1"
    }

    nivel_educativo = {
        1: "Ninguno",
        2: "Presscolar",
        3: "Básica Primaria (1°-5°)",
        4: "Básica Secundaria (6°-9°)",
        5: "Media (10°-13°)",
        6: "Superior (Técnica, Tecnológica, Universitaria - pregrado)",
        7: "Posgrado (especialización, maestría, doctorado)",
        8: "No registrado",
        99: "No sabe/No informa",
        None: "No registrado"
    }

    actividad_semana_pasada = {
        1: "Trabajando",
        2: "Buscando trabajo",
        3: "Estudiando",
        4: "Oficios del hogar",
        5: "Incapacitado permanente para trabajar",
        6: "Otra actividad",
        None: "No registrado"
    }

    def __init__(self):
        self.targetConnection = TargetConnection()
    
    def startETL4(self):
        self.cargarPersonas()
        self.cargarActividades()
        self.cargarPersonasMenores12()

    def cargarPersonas(self):
        anio2012 = [ "/db/Encuesta/2012/Caracteristicas_generales/Características generales.sav",
                    [6, 9, 10, 11, 12, 13, 14, 15, 16],
                    2012]
        
        anio2014 = ["/db/Encuesta/2014/Caracteristicas_Generales/CARACTERISTICAS GENERALES.sav",
                    [4, 5, 6, 7, 8, 9, 10, 11, 12],
                    2014]
        
        anio2016 = ["/db/Encuesta/2016/Caracteristicas_generales/Características generales.sav",
                    [4, 5, 6, 7, 8, 9, 10, 11, 12],
                    2016]
        
        anio2017 = ["/db/Encuesta/2017/Caracteristicas_generales/Caracteristicas generales.sav",
                    [4, 5, 6, 7, 8, 9, 10, 11, 12],
                    2017]
        
        self.cargarEncuesta(anio2012[0], anio2012[1], anio2012[2])
        self.cargarEncuesta(anio2014[0], anio2014[1], anio2014[2])
        self.cargarEncuesta(anio2016[0], anio2016[1], anio2016[2])
        self.cargarEncuesta(anio2017[0], anio2017[1], anio2017[2])

    def cargarEncuesta(self, filepath, index, year):
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: int(x) if (x is not None and x != b'') else None, line))
 
                '''query_hogar = "SELECT ID_HOGAR FROM DIM_Hogar WHERE DIRECTORIO = \""+ line[0] +"\" AND HOGAR_NUMERO = " + str(line[2])
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
                encuesta_eventos_id = str(encuesta_eventos_id[0][0]) if( encuesta_eventos_id ) else "Null"'''

                query_insert = ("INSERT INTO FACT_Persona " +
                    " (  " + 
                    " DIRECTORIO, " + 
                    " HOGAR_NUMERO, " + 
                    " PERSONA_NUMERO, " + 
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
                    "values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );" )

                query_params = (
                    str(line[0]), 
                    line[2],
                    line[3],
                    self.genero[line[index[0]]],
                    line[index[1]],
                    self.cultura[line[index[2]]],
                    self.parentezco[line[index[3]]],
                    self.estado_civil[line[index[4]]],
                    self.respuesta_booleana[line[index[5]]],
                    self.respuesta_booleana[line[index[6]]],
                    self.nivel_educativo[line[index[7]]],
                    line[index[8]],
                    year
                )

                self.runPreparedQuery(query_insert, query_params)
                 
    def cargarActividades(self):
        anio2012 = [ "/db/Encuesta/2012/Tiempo_libre/Tiempo libre.sav",
                    [4, 5, 6]]
        
        anio2014 = ["/db/Encuesta/2014/Presentaciones_y_espectaculos/PRESENTACIONES Y ESPECTACULOS.sav",
                    [4, 5, 6]]
        
        anio2016 = ["/db/Encuesta/2016/Presentaciones_y_espectaculos/Presentaciones y espectaculos.sav",
                    [4, 5, 6]]
        
        anio2017 = ["/db/Encuesta/2017/Presentaciones_y_espectaculos/Presentaciones y espectaculos.sav",
                    [3, 4, 5]]
        
        self.cargarActividadesEnPersonas(anio2012[0], anio2012[1])
        self.cargarActividadesEnPersonas(anio2014[0], anio2014[1])
        self.cargarActividadesEnPersonas(anio2016[0], anio2016[1])
        self.cargarActividadesEnPersonas(anio2017[0], anio2017[1])
    
    def cargarActividadesEnPersonas(self, filepath, index):
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: int(x) if (x is not None and x != b'') else None, line))

                query_insert = ("UPDATE FACT_Persona SET " +
                    "actividad_semana_pasada = %s, " +
                    "recibe_ingreso_mensual = %s, " +
                    "ingreso_total = %s " +
                    " WHERE DIRECTORIO = %s AND HOGAR_NUMERO = %s AND PERSONA_NUMERO = %s;" )
                
                query_params = (
                    self.actividad_semana_pasada[line[index[0]]],
                    self.respuesta_booleana[line[index[1]]],
                    line[index[2]],
                    str(line[0]),
                    line[2],
                    line[3],
                )

                self.runPreparedQuery(query_insert, query_params)


    def cargarPersonasMenores12(self):
        anio2012 = [ "/db/Encuesta/2012/Caracteristicas_generales_personas_de_5_a_11_anos/Características generales personas de 5 a 11 años.sav",
                    [4, 5, 6, 7, 8, 9]]
        
        anio2014 = [ "/db/Encuesta/2014/Presentaciones_y_espectaculos_(ninos_de_5_a_11)/NIÑOS DE 5 A 11 PRESENTACIONES Y ESPECTACULOS, PUBLICACIONES Y AUDIOVISUALES.sav",
                    [4, 5, 6, 7, 8, 9]]
        
        anio2016 = [ "/db/Encuesta/2016/Ninos de 5 a 11, presentaciones y espectaculos, publicaciones y audivisuales/Niños de 5 a 11, presentaciones y espectaculos, publicaciones y audivisuales.sav",
                    [4, 5, 6, 7, 8, 9]]
        
        anio2017 = [ "/db/Encuesta/2017/Ninos_de_5_a_11_presentaciones_y_espectaculos_publicaciones_y_audivisuales/Niños de 5 a 11, presentaciones y espectaculos, publicaciones y audivisuales.sav",
                    [4, 5, 6, 7, 8, 9]]
        
        self.cargarEncuestaMenores12(anio2012[0], anio2012[1])
        self.cargarEncuestaMenores12(anio2014[0], anio2014[1])
        self.cargarEncuestaMenores12(anio2016[0], anio2016[1])
        self.cargarEncuestaMenores12(anio2017[0], anio2017[1])

    def cargarEncuestaMenores12(self, filepath, index):
        counter = 0
        lineCounter = 0
        with savReaderWriter.SavReader(filepath) as reader:
            header = reader.header
            for line in reader:
                line = list(map(lambda x: int(x) if (x is not None and x != b'') else None, line))
                lineCounter += 1

                query_insert = ("UPDATE FACT_Persona SET " +
                    " cultura = %s, " + 
                    " parentesco_al_jefe = %s, " + 
                    " lee_escribe = %s, " + 
                    " estudia_actual = %s, " + 
                    " nivel_educativo = %s, " +
                    " ultimo_grado = %s " +
                    " WHERE DIRECTORIO = %s AND HOGAR_NUMERO = %s AND PERSONA_NUMERO = %s;" )

                query_params = (
                    self.cultura[line[index[0]]],
                    self.parentezco[line[index[1]]],
                    self.respuesta_booleana[line[index[2]]],
                    self.respuesta_booleana[line[index[3]]],
                    self.nivel_educativo[line[index[4]]],
                    line[index[5]],
                    str(line[0]), 
                    line[2],
                    line[3]
                )

                self.runPreparedQuery(query_insert, query_params)
                
        
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