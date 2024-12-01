'''Delete de documentos en colección clinicas y parques'''

# Importar el cliente de pymongo
from conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_clinicas = db.clinicas
coleccion_parques = db.parques

# Eliminar un documento de la coleccion clinicas
borrado_01 = coleccion_clinicas.delete_one(
    {"nombre": "Baratie"}
)
print("\n1) Eliminar un solo documento")
print(f"Documentos eliminados: {borrado_01.deleted_count}")

# Eliminar multiples documentos de la coleccion parques
borrado_02 = coleccion_parques.delete_many(
    {"capacidad": 450}
)
print("\n2) Eliminar múltiples documentos")
print(f"Documentos eliminados: {borrado_02.deleted_count}")
