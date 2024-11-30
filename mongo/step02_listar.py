"""Listar Colecciones"""

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos
db = client.documentos

# Listar las colecciones de la base de datos
colecciones = db.list_collection_names()

# Imprimir las colecciones
print(colecciones)
