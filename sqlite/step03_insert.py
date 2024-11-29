"""Insertar múltiples registros en tablas de SQLite con Python."""

from step01_conexion import conn

# Datos a insertar para locales de comida
locales_de_comida = [
    (1, 'Los Paisas', 'Av. Primera 123 y calle 45', '1234567', 'Colombiana', 50),
    (2, 'Orale Mano', 'C.C. La Piazza locales # 56-58', '2345678', 'Mexicana', 60),
    (3, 'Roma', 'Av. San Pedro # 67-89', '3456780', 'Italiana', 70),
    (4, 'Michi', 'Calle 456 # 78-90', '4567890', 'China', 80),
    (5, 'No vives de ensalada', 'Los Toritos #555', '5678901', 'Argentina', 90),
    (6, 'Baratie', 'East Blue #300', '6789012', 'Japonesa', 100)
]

# Datos a insertar para centros deportivos
centros_deportivos = [
    (1, 'Taurus', 'Sauces 8 #547 y peatonal 3era', '1234567', 'Pesas', 55),
    (2, 'Gym Nova', 'Av. Francisco de Orellana # 123', '2345678', 'Cardio', 110),
    (3, 'Maori', 'C.C. Alban Borja local #33', '3456780', 'Crossfit', 40),
    (4, 'HT Gym', 'Villa Club Etapa Neptuno', '4567890', 'Pesas', 30),
    (5, 'Urdesa Center', 'Victor Emilio Estrada # 700', '5678901', 'Cardio', 80),
    (6, 'Raza', 'Federacion Central # 934', '6789012', 'Crossfit', 45)
]

# Definir la sentencia SQL para insertar registros en las tablas
insert_locales_de_comida = '''
INSERT INTO locales_de_comida (id, nombre, direccion, telefono, tipo_comida, capacidad)
VALUES (?, ?, ?, ?, ?, ?)
'''

insert_centros_deportivos = '''
INSERT INTO centros_deportivos (id, nombre, direccion, telefono, tipo_deporte, capacidad)
VALUES (?, ?, ?, ?, ?, ?)
'''

# Insertar los registros en las tablas
with conn:
    cursor = conn.cursor()
    cursor.executemany(insert_locales_de_comida, locales_de_comida)
    cursor.executemany(insert_centros_deportivos, centros_deportivos)
    print('Registros insertados correctamente!!')
