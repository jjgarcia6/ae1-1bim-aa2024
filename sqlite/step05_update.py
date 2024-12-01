'''Actualizar datos de tablas clinicas y parques'''

from step01_conexion import conn

# Definir la sentencia SQL para actualizar registros en las tablas
update_clinicas = [
    '''
    UPDATE clinicas
    SET nombre = 'Interhospital'
    WHERE id = 1
    ''',
    '''
    UPDATE clinicas
    SET capacidad = 80
    WHERE nombre = 'IESS'
    '''
]

update_parques = [
    '''
    UPDATE parques
    SET nombre = 'Disneyland'
    WHERE id = 1
    ''',
    '''
    UPDATE parques
    SET capacidad = 60
    WHERE nombre = 'Asia'
    '''
]

# Actualizar los registros en las tablas
with conn:
    cursor = conn.cursor()
    for sql in update_clinicas:
        cursor.execute(sql)
    for sql in update_parques:
        cursor.execute(sql)
    print('Registros actualizados correctamente!!')
