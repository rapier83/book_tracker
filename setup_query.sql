use trackers;
CREATE TABLE `trackers`.`book_list` (
  `id` VARCHAR(45) NOT NULL COMMENT '',
  `title` VARCHAR(100) NOT NULL COMMENT '',
  `yes24` VARCHAR(45) NULL COMMENT '',
  `ISBN` VARCHAR(45) NULL COMMENT '',
  `aladin` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '');
  
  CREATE TABLE `trackers`.`score` (
  `id` INT NOT NULL COMMENT '',
  `time` DATETIME NULL COMMENT '',
  `kyobo_score` INT NULL COMMENT '',
  `aladin_score` INT NULL COMMENT '',
  `yes24_score` INT NULL COMMENT '',
  `book_id` VARCHAR(100) NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `id_idx` (`book_id` ASC)  COMMENT '',
  CONSTRAINT `id`
    FOREIGN KEY (`book_id`)
    REFERENCES `trackers`.`book_list` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

INSERT INTO `trackers`.`book_list`
  (`id`, `title`, `yes24`, `ISBN`, `aladin`)
  VALUES ('1', '하트마크', '22750663', '9791195623617', '69353271');
INSERT INTO `trackers`.`book_list`
  (`id`, `title`, `yes24`, `ISBN`, `aladin`)
  VALUES ('2', '고흥, 고흥 사람들', '22793592', '9791195623624', '69353271');
  
SELECT id, ISBN FROM book_list WHERE id='1';