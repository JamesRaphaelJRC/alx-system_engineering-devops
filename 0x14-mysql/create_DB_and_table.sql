-- Creates a database named tyrell_corp with table nexus6
-- inserts a name Leon to the table
-- Grants SELECT permission to holberton_user to the table
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS `nexus6` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256)
);
INSERT INTO `nexus6` (`name`) VALUES ("Leon");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
