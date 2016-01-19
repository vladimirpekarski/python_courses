SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `my_game_3` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `my_game_3` ;

-- -----------------------------------------------------
-- Table `my_game_3`.`user`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `my_game_3`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `role` INT NOT NULL ,
  `nickname` VARCHAR(45) NOT NULL ,
  `email` VARCHAR(45) NOT NULL ,
  `password` VARCHAR(45) NOT NULL ,
  `banned` TINYINT(1) NULL ,
  `description` VARCHAR(200) NULL ,
  `created` DATETIME NULL ,
  `updated` DATETIME NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  UNIQUE INDEX `nickname_UNIQUE` (`nickname` ASC) ,
  UNIQUE INDEX `user_email_UNIQUE` (`email` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_game_3`.`currency`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `my_game_3`.`currency` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `user_id` INT NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `value` INT NOT NULL ,
  `type` INT NOT NULL ,
  `created` DATETIME NULL ,
  `updated` DATETIME NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  INDEX `fk_currency_user_idx` (`user_id` ASC) ,
  CONSTRAINT `fk_currency_user`
    FOREIGN KEY (`user_id` )
    REFERENCES `my_game_3`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_game_3`.`progress`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `my_game_3`.`progress` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `user_id` INT NOT NULL ,
  `type` INT NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `current_value` INT NOT NULL ,
  `target_value` INT NOT NULL ,
  `created` DATETIME NULL ,
  `updated` DATETIME NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_progess_user1_idx` (`user_id` ASC) ,
  CONSTRAINT `fk_progess_user1`
    FOREIGN KEY (`user_id` )
    REFERENCES `my_game_3`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_game_3`.`achievement`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `my_game_3`.`achievement` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `user_id` INT NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  `type` INT NOT NULL ,
  `created` DATETIME NULL ,
  `updated` DATETIME NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_achievement_user1_idx` (`user_id` ASC) ,
  CONSTRAINT `fk_achievement_user1`
    FOREIGN KEY (`user_id` )
    REFERENCES `my_game_3`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `my_game_3`.`session`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `my_game_3`.`session` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `user_id` INT NOT NULL ,
  `start_time` DATETIME NULL ,
  `end_time` DATETIME NULL ,
  `duration` INT NULL ,
  `created` DATETIME NULL ,
  `updated` DATETIME NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_session_user1_idx` (`user_id` ASC) ,
  CONSTRAINT `fk_session_user1`
    FOREIGN KEY (`user_id` )
    REFERENCES `my_game_3`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `my_game_3` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
