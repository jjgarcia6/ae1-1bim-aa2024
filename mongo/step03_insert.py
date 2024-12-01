'''Insertar varios documentos en las colecciones locales y centros de la base de datos documentos'''

# Importar el cliente de pymongo
from conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_clinicas = db.clinicas
coleccion_parques = db.parques

# Documentos a insertar en la colección locales
insert_clinicas = [
    {"nombre": "IESS", "direccion": "Av. Primera 123 y calle 45",
        "telefono": "1234567", "jornada": "nocturna", "capacidad": 50},
    {"nombre": "Omnihospital", "jornada": "diurna",
        "capacidad": 70, "gerente": "Sanji"},
    {"nombre": "Roma Hospital", "direccion": "Av. San Pedro #67-89",
        "telefono": "34567890", "jornada": "diurna", "capacidad": 70},
    {"nombre": "Michi Veterinaria", "direccion": "Calle 456 # 78-90", "telefono": "4567890",
        "jornada": "diurna", "capacidad": 80, "estado": "Clausurado"},
    {"nombre": "Kennedy", "direccion": "Los Toritos #555",
        "telefono": "5678901", "jornada": "diurna", "capacidad": 50},
    {"nombre": "Baratie", "direccion": "East Blue #300",
        "jornada": "nocturna", "capacidad": 100, "gerente": "Sanji"}
]

insert_parques = [
    {"nombre": "Raza Park", "direccion": "Sauces 6 #567", "telefono": "1234567",
        "ubicacion": "Londres", "instructor": "Zoro"},
    {"nombre": "Taurus", "direccion": "La Joya Etapa Diamante",
        "ubicacion": "Miami", "capacidad": 450},
    {"nombre": "Maori Hawai", "direccion": "Plaza Triangulo local 10",
        "telefono": "3456789", "ubicacion": "Californa", "capacidad": 450},
    {"nombre": "Urdesa Park", "direccion": "Victor Emilio Estrada # 345",
        "telefono": "4567890", "ubicacion": "California", "capacidad": 700},
    {"nombre": "Nova Park", "telefono": "9876543",
        "tematica": "Acuatica", "capacidad": 500},
    {"nombre": "HT Gym", "direccion": "Av. Plaza Danin y Constitucion esquina",
        "telefono": "8765432", "tematica": "Montaña", "capacidad": 90, "instructor": "Luffy"}
]

# Insertar los documentos en la colección locales
coleccion_clinicas.insert_many(insert_clinicas)

# Insertar los documentos en la colección centros
coleccion_parques.insert_many(insert_parques)
