"""Conexion a la base Documentos de mongoDB desde Python"""

# Importar el cliente de pymongo
from pymongo import MongoClient
URI = (
    'mongodb+srv://jjgarcia6:pdcluVNsMZOmTigq@cluster0.u3mhx.mongodb.net/'
    '?retryWrites=true&w=majority&appName=Cluster0'
)

# Crear el cliente de pymongo
# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient(URI)
