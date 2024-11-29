'''Eliminar datos de la tabla locales_de_comida y centros_deportivos'''

from step01_conexion import conn

# Definir la sentencia SQL para eliminar registros en las tablas
delete_locales_de_comida = [
    '''
    DELETE FROM locales_de_comida
    WHERE nombre = 'Michi'
    '''
]

delete_centros_deportivos = [
    '''
    DELETE FROM centros_deportivos
    WHERE nombre = 'Maori'
    '''
]

# Eliminar los registros en las tablas
with conn:
    cursor = conn.cursor()
    for sql in delete_locales_de_comida:
        cursor.execute(sql)
    for sql in delete_centros_deportivos:
        cursor.execute(sql)
    print('Registros eliminados correctamente!!')
