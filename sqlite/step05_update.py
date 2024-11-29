'''Actualizar datos de tablas locales_de_comida y centros_deportivos'''

from step01_conexion import conn

# Definir la sentencia SQL para actualizar registros en las tablas
update_locales_de_comida = [
    '''
    UPDATE locales_de_comida
    SET nombre = 'Los Paisas Parceros'
    WHERE id = 1
    ''',
    '''
    UPDATE locales_de_comida
    SET capacidad = 65
    WHERE nombre = 'Roma'
    '''
]

update_centros_deportivos = [
    '''
    UPDATE centros_deportivos
    SET nombre = 'Taurus Fit Center'
    WHERE id = 1
    ''',
    '''
    UPDATE centros_deportivos
    SET capacidad = 60
    WHERE nombre = 'Raza'
    '''
]

# Actualizar los registros en las tablas
with conn:
    cursor = conn.cursor()
    for sql in update_locales_de_comida:
        cursor.execute(sql)
    for sql in update_centros_deportivos:
        cursor.execute(sql)
    print('Registros actualizados correctamente!!')
