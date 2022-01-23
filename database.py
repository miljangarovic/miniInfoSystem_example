# https://docs.python.org/3/library/sqlite3.html
# PL SQL, TRANSACT SQL
# Security
# SQL injection

import sqlite3

conn = sqlite3.connect('mini-info-sistem.db')

c = conn.cursor()

# c.execute('''
# DROP TABLE gradovi;
# ''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`gradovi`
-- -----------------------------------------------------
CREATE TABLE `gradovi` (
  `id` INT NOT NULL,
  `naziv` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Fakulteti`
-- -----------------------------------------------------
CREATE TABLE `Fakulteti` (
  `id` INT NOT NULL,
  `naziv` VARCHAR(45) NULL,
  `grad_id` INT NOT NULL,
  PRIMARY KEY (`id`, `grad_id`));
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Smjer`
-- -----------------------------------------------------

CREATE TABLE `Smjer` (
  `id` INT NOT NULL,
  `naziv` VARCHAR(45) NULL,
  `Fakulteti_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Fakulteti_id`));
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Saradnici`
-- -----------------------------------------------------
CREATE TABLE `Saradnici` (
  `jmbg` INT NOT NULL,
  `ime` VARCHAR(45) NULL,
  PRIMARY KEY (`jmbg`));
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`zvanje`
-- -----------------------------------------------------
CREATE TABLE `zvanje` (
  `id` INT NOT NULL,
  `naziv` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Profesori`
-- -----------------------------------------------------
CREATE TABLE `Profesori` (
  `jmbg` INT NOT NULL,
  `ime` VARCHAR(45) NULL,
  `zvanje_id` INT NOT NULL,
  PRIMARY KEY (`jmbg`, `zvanje_id`))
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Predmeti`
-- -----------------------------------------------------
CREATE TABLE `Predmeti` (
  `id` INT NOT NULL,
  `naziv` VARCHAR(45) NULL,
  `smjer_id` INT NOT NULL,
  `saradnik_jmbg` INT NOT NULL,
  `profesor_jmbg` INT NOT NULL,
  PRIMARY KEY (`id`, `smjer_id`, `saradnik_jmbg`, `profesor_jmbg`));
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Studenti`
-- -----------------------------------------------------
CREATE TABLE `Studenti` (
  `jmbg` INT NOT NULL,
  `ime` VARCHAR(45) NULL,
  `smjer` VARCHAR(45) NULL,
  `br_index` VARCHAR(45) NULL,
  PRIMARY KEY (`jmbg`));

''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Profesori_has_Fakulteti`
-- -----------------------------------------------------
CREATE TABLE `Profesori_has_Fakulteti` (
  `Profesori_jmbg` INT NOT NULL,
  `Fakulteti_id` INT NOT NULL,
  PRIMARY KEY (`Profesori_jmbg`, `Fakulteti_id`));
''')

c.execute('''
-- -----------------------------------------------------
-- Table `mini_info_sistem`.`Studenti_has_Predmeti`
-- -----------------------------------------------------
CREATE TABLE `Studenti_has_Predmeti` (
  `Studenti_jmbg` INT NOT NULL,
  `Predmeti_id` INT NOT NULL,
  PRIMARY KEY (`Studenti_jmbg`, `Predmeti_id`));
''')


#
#
#
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)






conn.commit()
conn.close()



