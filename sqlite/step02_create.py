"""Creacion de tablas locales_de_comida y centros_deportivos en una base de datos SQLite3"""

# Importar la conexion a la base de datos
from step01_conexion import conn

# Definir la sentencia SQL para crear las tablas
create_tables_sql = [
    '''
    CREATE TABLE IF NOT EXISTS clinicas (
        id INT PRIMARY KEY,
        nombre TEXT,
        direccion TEXT,
        telefono TEXT,
        jornada TEXT,
        capacidad INTEGER        
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS parques (
        id INT PRIMARY KEY,
        nombre TEXT,
        direccion TEXT,
        telefono TEXT,
        ubicacion TEXT,
        capacidad INTEGER
    )
    '''
]

# Crear una conexion a la base de datos
with conn:
    cursor = conn.cursor()
    for sql in create_tables_sql:
        cursor.execute(sql)
    print("Tablas creadas con exito!!")
