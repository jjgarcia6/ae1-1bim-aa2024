'''Eliminar datos de las tablas clinicas y parques'''

from step01_conexion import conn

# Definir la sentencia SQL para eliminar registros en las tablas
delete_clinicas = [
    '''
    DELETE FROM clinicas
    WHERE nombre = 'Granados'
    '''
]

delete_parques = [
    '''
    DELETE FROM parques
    WHERE nombre = 'Natural'
    '''
]

# Eliminar los registros en las tablas
with conn:
    cursor = conn.cursor()
    for sql in delete_clinicas:
        cursor.execute(sql)
    for sql in delete_parques:
        cursor.execute(sql)
    print('Registros eliminados correctamente!!')
