'''Select data from tables locales_de_comida and centros_deportivos'''

from step01_conexion import conn

# Definir las sentencias SQL para seleccionar todos los registros de las tablas
SELECT_LOCALES_DE_COMIDA = '''SELECT * FROM locales_de_comida'''
SELECT_CENTROS_DEPORTIVOS = '''SELECT * FROM centros_deportivos'''


def fetch_and_print(cursor, query):
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    print()


# Seleccionar todos los registros de las tablas
with conn:
    cursor = conn.cursor()
    fetch_and_print(cursor, SELECT_LOCALES_DE_COMIDA)
    fetch_and_print(cursor, SELECT_CENTROS_DEPORTIVOS)
