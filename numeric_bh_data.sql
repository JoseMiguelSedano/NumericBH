-- Creación de la base de datos de Numeric BH

CREATE DATABASE NumericBH;

USE NumericBH
-- Creación de las tablas: Usuario e Historial_de_Conversiones

CREATE TABLE Usuarios (
    id_usuario INT IDENTITY(1,1) PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    correo_usuario VARCHAR(200) UNIQUE NOT NULL,
    contrasenha VARCHAR(200) NOT NULL,
)

CREATE TABLE Historial_de_Conversiones (
    id_conversion INT IDENTITY(1,1) PRIMARY KEY,
    id_usuario INT NULL,
    tipo_conversion VARCHAR(50) NOT NULL,
    valor_inicial VARCHAR(100) NOT NULL,
    valor_final VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)