-- MySQL Script generated by MySQL Workbench
-- Tue Oct 13 21:29:48 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema target
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `target` ;

-- -----------------------------------------------------
-- Schema target
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `target` DEFAULT CHARACTER SET utf8 ;
USE `target` ;

-- -----------------------------------------------------
-- Table `target`.`DIM_Encuesta_Espacios_Culturales`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`DIM_Encuesta_Espacios_Culturales` ;

CREATE TABLE IF NOT EXISTS `target`.`DIM_Encuesta_Espacios_Culturales` (
  `ID_ENCUESTA_ESPACIOS_CULTURALES` INT NOT NULL AUTO_INCREMENT,
  `DIRECTORIO` VARCHAR(45) NULL,
  `HOGAR_NUMERO` INT NULL,
  `PERSONA_NUMERO` INT NULL,
  `asistio_biblio` TINYINT NULL,
  `asistio_biblio_frecuencia` VARCHAR(100) NULL,
  `asistio_biblio_escolar` TINYINT NULL,
  `asistio_biblio_universitaria` TINYINT NULL,
  `asistio_biblio_especializada` TINYINT NULL,
  `asistio_biblio_publica` TINYINT NULL,
  `asistio_biblio_leer_libro` TINYINT NULL,
  `asistio_biblio_prestamo_libro` TINYINT NULL,
  `asistio_biblio_consultar_audiovisuales` TINYINT NULL,
  `asistio_biblio_acceder_internet` TINYINT NULL,
  `asistio_biblioteca_otro` TINYINT NULL,
  `no_asistio_biblio_falta_dinero` TINYINT NULL,
  `no_asistio_biblio_estan_lejos` TINYINT NULL,
  `no_asistio_biblio_desinteres` TINYINT NULL,
  `no_asistio_biblio_desconocimiento` TINYINT NULL,
  `no_asistio_biblio_falta_tiempo` TINYINT NULL,
  `no_asistio_biblio_problemas_salud` TINYINT NULL,
  `no_asistio_biblio_ausencia_espacios` TINYINT NULL,
  `no_asistio_biblio_otro` TINYINT NULL,
  `no_asistio_biblio_prefiere_internet` TINYINT NULL,
  `asistio_museos` TINYINT NULL,
  `asistio_museos_frecuencia` VARCHAR(100) NULL,
  `no_asistio_museos_estan_lejos` TINYINT NULL,
  `no_asistio_museos_problemas_salud` TINYINT NULL,
  `no_asistio_museos_falta_tiempo` TINYINT NULL,
  `no_asistio_museos_desinteres` TINYINT NULL,
  `no_asistio_museos_ausencia_espacios` TINYINT NULL,
  `no_asistio_museos_falta_dinero` TINYINT NULL,
  `no_asistio_museos_desconocimiento` TINYINT NULL,
  `no_asistio_museos_otro` TINYINT NULL,
  `asistio_galeria` TINYINT NULL,
  `asistio_galeria_frecuencia` VARCHAR(100) NULL,
  `no_asistio_galeria_falta_dinero` TINYINT NULL,
  `no_asistio_galeria_desinteres` TINYINT NULL,
  `no_asistio_galeria_desconocimiento` TINYINT NULL,
  `no_asistio_galeria_problemas_salud` TINYINT NULL,
  `no_asistio_galeria_estan_lejos` TINYINT NULL,
  `no_asistio_galeria_ausencia_espacios` TINYINT NULL,
  `no_asistio_galeria_falta_tiempo` TINYINT NULL,
  `no_asistio_galeria_otro` TINYINT NULL,
  `asistio_monumentos` TINYINT NULL,
  `asistio_monumentos_frecuencia` VARCHAR(100) NULL,
  `no_asistio_monumentos_problemas_salud` TINYINT NULL,
  `no_asistio_monumentos_estan_lejos` TINYINT NULL,
  `no_asistio_monumentos_falta_tiempo` TINYINT NULL,
  `no_asistio_monumentos_desinteres` TINYINT NULL,
  `no_asistio_monumentos_ausencia_espacios` TINYINT NULL,
  `no_asistio_monumentos_falta_dinero` TINYINT NULL,
  `no_asistio_monumentos_desconocimiento` TINYINT NULL,
  `no_asistio_monumentos_otro` TINYINT NULL,
  `tomo_talleres_artisticos` TINYINT NULL,
  `tomo_talleres_artisticos_cine_tv_radio` TINYINT NULL,
  `tomo_talleres_artisticos_musica` TINYINT NULL,
  `tomo_talleres_artisticos_teatro_danza` TINYINT NULL,
  `tomo_talleres_artisticos_cuenteria` TINYINT NULL,
  `tomo_talleres_artisticos_foto_pintura` TINYINT NULL,
  `tomo_talleres_artisticos_literatura` TINYINT NULL,
  `tomo_talleres_artisticos_artesanias` TINYINT NULL,
  `tomo_talleres_artisticos_manualidades` TINYINT NULL,
  `tomo_talleres_artisticos_otros` TINYINT NULL,
  PRIMARY KEY (`ID_ENCUESTA_ESPACIOS_CULTURALES`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`DIM_Encuesta_Espacios_Culturales_Menores`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`DIM_Encuesta_Espacios_Culturales_Menores` ;

CREATE TABLE IF NOT EXISTS `target`.`DIM_Encuesta_Espacios_Culturales_Menores` (
  `ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES` INT NOT NULL AUTO_INCREMENT,
  `DIRECTORIO` VARCHAR(45) NULL,
  `HOGAR_NUMERO` INT NULL,
  `PERSONA_NUMERO` INT NULL,
  `nino_tomo_actividades_ludicas` TINYINT NULL,
  `nino_tomo_actividades_ludicas_frecuencia` VARCHAR(100) NULL,
  `nino_actividades_lud_con_familia` TINYINT NULL,
  `nino_actividades_lud_con_companeros` TINYINT NULL,
  `nino_actividades_lud_solo` TINYINT NULL,
  PRIMARY KEY (`ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`DIM_Hogar`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`DIM_Hogar` ;

CREATE TABLE IF NOT EXISTS `target`.`DIM_Hogar` (
  `ID_HOGAR` INT NOT NULL AUTO_INCREMENT,
  `DIRECTORIO` VARCHAR(45) NULL,
  `HOGAR_NUMERO` INT NULL,
  `region` INT NULL,
  `total_personas` INT NULL,
  `total_personas_5_a_11` INT NULL,
  `total_personas_mayor_12` INT NULL,
  `tipo_vivienda` VARCHAR(100) NULL,
  `servicio_electricidad` TINYINT NULL,
  `servicio_electricidad_estrato` VARCHAR(100) NULL,
  `servicio_gas` TINYINT NULL,
  `servicio_alcantarillado` TINYINT NULL,
  `servicio_basura` TINYINT NULL,
  `servicio_basura_recoleccion` INT NULL,
  `servicio_acueducto` TINYINT NULL,
  PRIMARY KEY (`ID_HOGAR`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`DIM_Encuesta_Presentaciones_Espectaculos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`DIM_Encuesta_Presentaciones_Espectaculos` ;

CREATE TABLE IF NOT EXISTS `target`.`DIM_Encuesta_Presentaciones_Espectaculos` (
  `ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS` INT NOT NULL AUTO_INCREMENT,
  `DIRECTORIO` VARCHAR(45) NULL,
  `HOGAR_NUMERO` INT NULL,
  `PERSONA_NUMERO` INT NULL,
  `asistio_teatro_danza` TINYINT NULL,
  `asistio_teatro_danza_frecuencia` VARCHAR(100) NULL,
  `asistio_teatro_danza_gratuitos` INT NULL,
  `no_asistio_teatro_danza_falta_dinero` TINYINT NULL,
  `no_asistio_teatro_danza_desinteres` TINYINT NULL,
  `no_asistio_teatro_danza_desconocimiento` TINYINT NULL,
  `no_asistio_teatro_danza_falta_tiempo` TINYINT NULL,
  `no_asistio_teatro_danza_estan_lejos` TINYINT NULL,
  `no_asistio_teatro_danza_problemas_salud` TINYINT NULL,
  `no_asistio_teatro_danza_ausencia_espacios` TINYINT NULL,
  `no_asistio_teatro_danza_otro` TINYINT NULL,
  `no_asistio_teatro_danza_falta_compania` TINYINT NULL,
  `asistio_teatro_danza_pago` INT NULL,
  `asistio_teatro_danza_pago_total` FLOAT NULL,
  `asistio_concierto_recital` TINYINT NULL,
  `asistio_concierto_recital_frecuencia` VARCHAR(100) NULL,
  `asistio_concierto_recital_gratuitos` INT NULL,
  `no_asistio_concierto_recital_falta_dinero` TINYINT NULL,
  `no_asistio_concierto_recital_estan_lejos` TINYINT NULL,
  `no_asistio_concierto_recital_ausencia_eventos` TINYINT NULL,
  `no_asistio_concierto_recital_problemas_salud` TINYINT NULL,
  `no_asistio_concierto_recital_desinteres` TINYINT NULL,
  `no_asistio_concierto_recital_falta_tiempo` TINYINT NULL,
  `no_asistio_concierto_recital_desconocimiento` TINYINT NULL,
  `no_asistio_concierto_recital_otro` TINYINT NULL,
  `asistio_concierto_recital_pago` INT NULL,
  `asistio_concierto_recital_pago_total` FLOAT NULL,
  `asistio_expo_feria_arte_grafica` TINYINT NULL,
  `asistio_expo_feria_arte_grafica_frecuencia` VARCHAR(100) NULL,
  `asistio_expo_feria_arte_grafica_gratuitos` INT NULL,
  `no_asistio_expo_feria_arte_grafica_desconocimiento` TINYINT NULL,
  `no_asistio_expo_feria_arte_grafica_falta_dinero` TINYINT NULL,
  `no_asistio_expo_feria_arte_grafica_ausencia_eventos` TINYINT NULL,
  `no_asistio_expo_feria_arte_grafica_problemas_salud` VARCHAR(2) NULL,
  `no_asistio_expo_feria_arte_grafica_desinteres` TINYINT NULL,
  `no_asistio_expo_feria_arte_grafica_estan_lejos` TINYINT NULL,
  `no_asistio_expo_feria_arte_grafica_falta_tiempo` TINYINT NULL,
  `no_asistio_expo_feria_arte_grafica_otro` TINYINT NULL,
  `asistio_expo_feria_arte_grafica_pago` INT NULL,
  `asistio_expo_feria_arte_grafica_pago_total` FLOAT NULL,
  `asistio_expo_artesanal` TINYINT NULL,
  `asistio_expo_artesanal_frecuencia` VARCHAR(100) NULL,
  `asistio_expo_artesanal_gratuitos` INT NULL,
  `no_asistio_expo_artesanal_desconocimiento` TINYINT NULL,
  `no_asistio_expo_artesanal_falta_dinero` TINYINT NULL,
  `no_asistio_expo_artesanal_ausencia_eventos` TINYINT NULL,
  `no_asistio_expo_artesanal_problemas_salud` TINYINT NULL,
  `no_asistio_expo_artesanal_desinteres` TINYINT NULL,
  `no_asistio_expo_artesanal_estan_lejos` TINYINT NULL,
  `no_asistio_expo_artesanal_falta_tiempo` TINYINT NULL,
  `no_asistio_expo_artesanal_otro` TINYINT NULL,
  `asistio_expo_artesanal_pago` INT NULL,
  `asistio_expo_artesanal_pago_total` FLOAT NULL,
  PRIMARY KEY (`ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`FACT_Persona`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`FACT_Persona` ;

CREATE TABLE IF NOT EXISTS `target`.`FACT_Persona` (
  `ID_CARACTERISTICAS_GENERALES` INT NOT NULL AUTO_INCREMENT,
  `DIRECTORIO` VARCHAR(45) NULL,
  `HOGAR_NUMERO` INT NULL,
  `PERSONA_NUMERO` INT NULL,
  `ID_HOGAR` INT NULL,
  `ID_ENCUESTA_ESPACIOS_CULTURALES` INT NULL,
  `ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES` INT NULL,
  `ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS` INT NULL,
  `genero` VARCHAR(100) NULL,
  `edad` INT NULL,
  `cultura` VARCHAR(100) NULL,
  `parentesco_al_jefe` VARCHAR(100) NULL,
  `estado_civil` VARCHAR(100) NULL,
  `lee_escribe` TINYINT NULL,
  `estudia_actual` TINYINT NULL,
  `nivel_educativo` INT NULL,
  `ultimo_grado` VARCHAR(100) NULL,
  `actividad_semana_pasada` VARCHAR(100) NULL,
  `recibe_ingreso_mensual` INT NULL,
  `ingreso_total` FLOAT NULL,
  `anio` YEAR NULL,
  INDEX `fk_CaracteristicasGenerales_Hogares1_idx` (`ID_HOGAR` ASC) VISIBLE,
  INDEX `fk_FACT_Persona_DIM_Encuesta_Espacios_Culturales_Menores1_idx` (`ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES` ASC) VISIBLE,
  INDEX `fk_FACT_Persona_DIM_Entrevista_Espacios_Culturales1_idx` (`ID_ENCUESTA_ESPACIOS_CULTURALES` ASC) VISIBLE,
  PRIMARY KEY (`ID_CARACTERISTICAS_GENERALES`),
  INDEX `fk_FACT_Persona_PresentacionesEspectaculos1_idx` (`ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS` ASC) VISIBLE,
  CONSTRAINT `fk_CaracteristicasGenerales_Hogares1`
    FOREIGN KEY (`ID_HOGAR`)
    REFERENCES `target`.`DIM_Hogar` (`ID_HOGAR`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_Persona_DIM_Encuesta_Espacios_Culturales_Menores1`
    FOREIGN KEY (`ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES`)
    REFERENCES `target`.`DIM_Encuesta_Espacios_Culturales_Menores` (`ID_ENCUESTA_ESPACIOS_CULTURALES_MENORES`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_Persona_DIM_Entrevista_Espacios_Culturales1`
    FOREIGN KEY (`ID_ENCUESTA_ESPACIOS_CULTURALES`)
    REFERENCES `target`.`DIM_Encuesta_Espacios_Culturales` (`ID_ENCUESTA_ESPACIOS_CULTURALES`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_FACT_Persona_PresentacionesEspectaculos1`
    FOREIGN KEY (`ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS`)
    REFERENCES `target`.`DIM_Encuesta_Presentaciones_Espectaculos` (`ID_ENCUESTA_PRESENTACIONES_ESPECTACULOS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
