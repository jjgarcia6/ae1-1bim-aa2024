"""Insertar múltiples registros en tablas de SQLite con Python."""

from step01_conexion import conn

# Datos a insertar para clinicas
clinicas = [
    (1, 'Los Cuervos', 'Av. Primera 123 y calle 45', '1234567', 'matutina', 50),
    (2, 'IESS', 'C.C. La Piazza locales # 56-58', '2345678', 'nocturna', 60),
    (3, 'Cruz Roja', 'Av. San Pedro # 67-89', '3456780', 'nocturna', 70),
    (4, 'Alcivar', 'Calle 456 # 78-90', '4567890', 'matutina', 80),
    (5, 'Granados', 'Los Toritos #555', '5678901', 'matutina', 90),
    (6, 'Baratie', 'East Blue #300', '6789012', 'matutina', 100)
]

# Datos a insertar para parques
parques = [
    (1, 'Disney', 'Sauces 8 #547 y peatonal 3era', '1234567', 'Guayaquil', 55),
    (2, 'Malecon', 'Av. Francisco de Orellana # 123', '2345678', 'Quito', 110),
    (3, 'Milenio', 'C.C. Alban Borja local #33', '3456780', 'Cuenca', 40),
    (4, 'Asia', 'Villa Club Etapa Neptuno', '4567890', 'Cuenca', 30),
    (5, 'Historico', 'Victor Emilio Estrada # 700', '5678901', 'Cuenca', 80),
    (6, 'Natural', 'Federacion Central # 934', '6789012', 'Guayaquil', 45)
]

# Definir la sentencia SQL para insertar registros en las tablas
INSERT_CLINICAS = '''
INSERT INTO clinicas (id, nombre, direccion, telefono, jornada, capacidad)
VALUES (?, ?, ?, ?, ?, ?)
'''

INSERT_PARQUES = '''
INSERT INTO parques (id, nombre, direccion, telefono, ubicacion, capacidad)
VALUES (?, ?, ?, ?, ?, ?)
'''

# Insertar los registros en las tablas
with conn:
    cursor = conn.cursor()
    cursor.executemany(INSERT_CLINICAS, clinicas)
    cursor.executemany(INSERT_PARQUES, parques)
    print('Registros insertados correctamente!!')
