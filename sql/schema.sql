
-- Crear base de datos y tablas
CREATE DATABASE IF NOT EXISTS eva2_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE eva2_db;

-- Tabla trabajadores
CREATE TABLE IF NOT EXISTS trabajadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    email VARCHAR(150) UNIQUE,
    password_md5 CHAR(32) NOT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(12,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices útiles
CREATE INDEX idx_trabajadores_nombre ON trabajadores(nombre);
CREATE INDEX idx_productos_nombre ON productos(nombre);
