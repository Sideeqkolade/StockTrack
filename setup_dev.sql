-- create a database named stocktrack_db

CREATE DATABASE IF NOT EXISTS stocktrack_db;
CREATE USER IF NOT EXISTS 'stocktrack_usr'@'localhost' IDENTIFIED BY 'stocktrack_usr_pwd';
GRANT ALL PRIVILEGES ON `stocktrack_db`.* TO 'stocktrack_usr'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'stocktrack_usr'@'localhost';
FLUSH PRIVILEGES;