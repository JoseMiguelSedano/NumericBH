""" Archivo para la conexión con la base de datos """
import pyodbc


def conexion_db():
    """ Función para la conexión con la base de datos """
    try:
        conexion = pyodbc.connect(  
            'DRIVER={SQL Server};'
            'SERVER=.;'
            'DATABASE=NumericBH;'
            'Trusted_Connection=yes;'
        )
        return conexion

    except pyodbc.Error as e:
        print(f"Ocurrió un error al conectar: {e}")
        return None
