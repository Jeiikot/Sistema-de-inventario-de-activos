DROP DATABASE IF EXISTS Inventory_System;
CREATE DATABASE IF NOT EXISTS Inventory_System;
USE Inventory_System;

CREATE TABLE Laboratory(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(45) NOT NULL,
	description TEXT,
	PRIMARY KEY(id)
);

CREATE TABLE Elements(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	uid VARCHAR(25) NOT NULL,
	name VARCHAR(45) NOT NULL,
	serial VARCHAR(25) NOT NULL,
	description TEXT,
	id_laboratory INT NOT NULL,
	FOREIGN KEY(id_laboratory) REFERENCES Laboratory(id)
);

CREATE TABLE Records(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	datetime datetime,
	id_element INT NOT NULL,
	id_laboratory INT NOT NULL,
	FOREIGN KEY(id_element) REFERENCES Elements(id),
	FOREIGN KEY(id_laboratory) REFERENCES Laboratory(id)
);

