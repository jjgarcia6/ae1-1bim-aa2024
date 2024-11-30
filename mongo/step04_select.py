'''Muestra los documentos de las colecciones locales y centros de la base de datos documentos'''

# Importar el cliente de pymongo
from step01_conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_locales = db.locales
coleccion_centros = db.centros

print("Consultas sobre la colección Locales")
# Mostrar los documentos de la colección locales con nombre "Roma"
data_01 = coleccion_locales.find_one({"nombre": "Roma"}, {"_id": 0})
print("\n1) Locales con nombre Roma")
print(data_01)

# Mostrar todos los documentos de la colección locales donde atiende Sanji
data_02 = coleccion_locales.find({"chef": {"$eq": "Sanji"}}, {"_id": 0})
print("\n2) Locales donde atiende Sanji")
for local in data_02:
    print(local)

# Mostrar todos los documentos de la colección locales con capacidad >= 70
data_03 = coleccion_locales.find(
    {"capacidad": {"$gte": 70}}, {"_id": 0})
print("\n3) Locales con capacidad >= 70 personas")
for local in data_03:
    print(local)

# Mostrar todos los documentos de la colección locales con tipo_comida "Argentina"
data_04 = coleccion_locales.find({"tipo_comida": "Argentina"}, {"_id": 0})
print("\n4) Locales de comida Argentina")
for local in data_04:
    print(local)


print("\n\nConsultas sobre la colección Centros")
# Mostrar un documento de la coleccion centros con nombre Taurus
data_05 = coleccion_centros.find_one({"nombre": "Taurus"}, {"_id": 0})
print("\n1) Centros con nombre Taurus")
print(data_05)


# Mostrar todos los documentos de la colección centros con capacidad >= 70
data_06 = coleccion_centros.find({"capacidad": {"$gte": 70}}, {"_id": 0})
print("\n2) Centros con capacidad > 70 personas")
for centro in data_06:
    print(centro)

# Mostrar todos los documentos de la colección centros con tipo_deporte "Box"
data_07 = coleccion_centros.find({"tipo_deporte": "Box"}, {"_id": 0})
print("\n3) Centros de Box")
for centro in data_07:
    print(centro)

# Mostrar todos los documentos de la colección centros con instructor "Zoro"
data_08 = coleccion_centros.find({"instructor": "Zoro"}, {"_id": 0})
print("\n4) Centros con instructor Zoro")
for centro in data_08:
    print(centro)
