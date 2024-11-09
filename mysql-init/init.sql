-- init.sql
CREATE DATABASE IF NOT EXISTS search_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE search_db;

CREATE TABLE IF NOT EXISTS documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    language VARCHAR(10),
    FULLTEXT(title, description)
) ENGINE=InnoDB;