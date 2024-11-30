'''Insertar varios documentos en las colecciones locales y centros de la base de datos documentos'''

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_locales = db.locales
coleccion_centros = db.centros

# Documentos a insertar en la colección locales
insert_locales = [
    {"nombre": "Los Paisas", "direccion": "Av. Primera 123 y calle 45",
        "telefono": "1234567", "tipo_comida": "Colombiana", "capacidad": 50},
    {"nombre": "Orale Mano", "tipo_comida": "Mexicana",
        "capacidad": 70, "chef": "Sanji"},
    {"nombre": "Roma", "direccion": "Av. San Pedro #67-89",
        "telefono": "34567890", "tipo_comida": "Italiana", "capacidad": 70},
    {"nombre": "Michi", "direccion": "Calle 456 # 78-90", "telefono": "4567890",
        "tipo_comida": "China", "capacidad": 80, "estado": "Clausurado"},
    {"nombre": "No vives de ensalada", "direccion": "Los Toritos #555",
        "telefono": "5678901", "tipo_comida": "Argentina", "capacidad": 50},
    {"nombre": "Baratie", "direccion": "East Blue #300",
        "tipo_comida": "Japonesa", "capacidad": 100, "chef": "Sanji"}
]

insert_centros = [
    {"nombre": "Raza", "direccion": "Sauces 6 #567", "telefono": "1234567",
        "tipo_deporte": "Pesas", "instructor": "Zoro"},
    {"nombre": "Taurus", "direccion": "La Joya Etapa Diamante",
        "tipo_deporte": "Box", "capacidad": 45},
    {"nombre": "Maori", "direccion": "Plaza Triangulo local 10",
        "telefono": "3456789", "tipo_deporte": "Natacion", "capacidad": 45},
    {"nombre": "Urdesa Center", "direccion": "Victor Emilio Estrada # 345",
        "telefono": "4567890", "tipo_deporte": "Pesas", "capacidad": 70},
    {"nombre": "Gym Nova", "telefono": "9876543",
        "tipo_deporte": "Crossfit", "capacidad": 70},
    {"nombre": "HT Gym", "direccion": "Av. Plaza Danin y Constitucion esquina",
        "telefono": "8765432", "tipo_deporte": "Box", "capacidad": 90, "instructor": "Luffy"}
]

# Insertar los documentos en la colección locales
coleccion_locales.insert_many(insert_locales)

# Insertar los documentos en la colección centros
coleccion_centros.insert_many(insert_centros)
