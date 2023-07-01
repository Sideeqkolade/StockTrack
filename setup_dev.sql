-- create a database named stocktrack_db

CREATE DATABASE IF NOT EXISTS stocktrack_dev_db;
CREATE USER IF NOT EXISTS 'stocktrack_dev'@'localhost' IDENTIFIED BY 'stocktrack_dev_pwd';
GRANT ALL PRIVILEGES ON `stocktrack_dev_db`.* TO 'stocktrack_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'stocktrack_dev'@'localhost';
FLUSH PRIVILEGES;