'''Delete de documentos en colección locales y centros'''

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_locales = db.locales
coleccion_centros = db.centros

# Eliminar un documento de la coleccion locales
borrado_01 = coleccion_locales.delete_one(
    {"nombre": "Baratie"}
)
print("\n1) Eliminar un solo documento")
print(f"Documentos eliminados: {borrado_01.deleted_count}")

# Eliminar multiples documentos de la coleccion centros
borrado_02 = coleccion_centros.delete_many(
    {"capacidad": 45}
)
print("\n2) Eliminar múltiples documentos")
print(f"Documentos eliminados: {borrado_02.deleted_count}")
