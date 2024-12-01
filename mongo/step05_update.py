'''Actualización de documentos en colección clinicas y parques'''

# Importar el cliente de pymongo
from conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_clinicas = db.clinicas
coleccion_parques = db.parques

# Actualizar un documento de la colección clinicas
actualizacion01 = coleccion_clinicas.update_one(
    {"nombre": "Michi Veterinaria"},
    {"$set": {"estado": "Abierto"}}
)
print("\n1) Actualizar un solo documento en coleccion clinicas")
print(f"Documentos coincidentes: {actualizacion01.matched_count}")
print(f"Documentos modificados: {actualizacion01.modified_count}")

# Actualizar varios documentos de la colección clinicas
actualizacion02 = coleccion_clinicas.update_many(
    {"capacidad": {"$gte": 50}},
    {"$set": {"estado": "Abierto"}}
)
print("\n2) Actualizar múltiples documentos en coleccion clinicas")
print(f"Documentos coincidentes: {actualizacion02.matched_count}")
print(f"Documentos modificados: {actualizacion02.modified_count}")

# Actualizar un documento de la colección parques
actualizacion03 = coleccion_parques.update_one(
    {"nombre": "Nova Park"},
    {"$set": {"capacidad": 700}}
)
print("\n3) Actualizar un solo documento en coleccion parques")
print(f"Documentos coincidentes: {actualizacion03.matched_count}")
print(f"Documentos modificados: {actualizacion03.modified_count}")

# Actualizar varios documentos de la colección parques
actualizacion04 = coleccion_parques.update_many(
    {"capacidad": {"$gte": 450}},
    {"$set": {"instructor": "Zoro"}}
)
print("\n4) Actualizar múltiples documentos en coleccion parques")
print(f"Documentos coincidentes: {actualizacion04.matched_count}")
print(f"Documentos modificados: {actualizacion04.modified_count}")
