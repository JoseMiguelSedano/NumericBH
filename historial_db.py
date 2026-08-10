""" Archivo para la admininistración del historial """

from conexion import conexion_db


def guardar_conversion(tipo, origen, destino):
    """ Función para guardar la conversión realizada """
    conector_db = conexion_db()
    cursor = conector_db.cursor()
    consulta_sql = """INSERT INTO
    Historial (tipo_conversion, valor_inicial, valor_final)
    VALUES (?, ?, ?)"""
    datos_a_guardar = (tipo, origen, destino)
    cursor.execute(consulta_sql, datos_a_guardar)
    conector_db.commit()
    cursor.close()
    conector_db.close()


def obtener_historial():
    """ Función para consultar el historial generado """
    conector_db = conexion_db()
    cursor = conector_db.cursor()
    mostrar_historial = """SELECT
        tipo_conversion,
        valor_inicial,
        valor_final,
        fecha_conversion
        FROM Historial"""
    cursor.execute(mostrar_historial)
    mostrar_historial = cursor.fetchall()
    cursor.close()
    conector_db.close()

    return mostrar_historial
