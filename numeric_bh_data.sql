-- Creación de la base de datos de Numeric BH

CREATE DATABASE NumericBH;

USE NumericBH

-- Creación de las tabla: Historial

CREATE TABLE Historial (
    id_conversion INT IDENTITY(1,1) PRIMARY KEY,
    tipo_conversion VARCHAR(50) NOT NULL,
    valor_inicial VARCHAR(100) NOT NULL,
    valor_final VARCHAR(100) NOT NULL,
    fecha_conversion DATETIME DEFAULT GETDATE()
);

SELECT
    tipo_conversion AS Tipo,
    valor_inicial AS Ingreso,
    valor_final AS Resultado
FROM Historial;
