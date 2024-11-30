'''Actualización de documentos en colección locales y centros'''

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_locales = db.locales
coleccion_centros = db.centros

# Actualizar un documento de la colección locales
actualizacion01 = coleccion_locales.update_one(
    {"nombre": "Michi"},
    {"$set": {"estado": "Abierto"}}
)
print("\n1) Actualizar un solo documento en coleccion locales")
print(f"Documentos coincidentes: {actualizacion01.matched_count}")
print(f"Documentos modificados: {actualizacion01.modified_count}")

# Actualizar varios documentos de la colección locales
actualizacion02 = coleccion_locales.update_many(
    {"capacidad": {"$gte": 50}},
    {"$set": {"estado": "Abierto"}}
)
print("\n2) Actualizar múltiples documentos en coleccion locales")
print(f"Documentos coincidentes: {actualizacion02.matched_count}")
print(f"Documentos modificados: {actualizacion02.modified_count}")

# Actualizar un documento de la colección centros
actualizacion03 = coleccion_centros.update_one(
    {"nombre": "Gym Nova"},
    {"$set": {"capacidad": 50}}
)
print("\n3) Actualizar un solo documento en coleccion centros")
print(f"Documentos coincidentes: {actualizacion03.matched_count}")
print(f"Documentos modificados: {actualizacion03.modified_count}")

# Actualizar varios documentos de la colección centros
actualizacion04 = coleccion_centros.update_many(
    {"capacidad": {"$gte": 45}},
    {"$set": {"instructor": "Zoro"}}
)
print("\n4) Actualizar múltiples documentos en coleccion centros")
print(f"Documentos coincidentes: {actualizacion04.matched_count}")
print(f"Documentos modificados: {actualizacion04.modified_count}")
