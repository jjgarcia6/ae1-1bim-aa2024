'''Muestra los documentos de las colecciones clinicas y parques de la base de datos documentos'''

# Importar el cliente de pymongo
from conexion import client

# Seleccionar la base de datos
db = client.documentos

# Seleccionar las colecciones
coleccion_clinicas = db.clinicas
coleccion_parques = db.parques

print("Consultas sobre la colección Clinicas Particulares")
# Mostrar los documentos de la colección clinicas con nombre "Roma"
data_01 = coleccion_clinicas.find_one({"nombre": "IESS"}, {"_id": 0})
print("\n1) Clinicas con nombre IESS")
print(data_01)

# Mostrar todos los documentos de la colección clinicas donde Sanji es gerente
data_02 = coleccion_clinicas.find({"gerente": {"$eq": "Sanji"}}, {"_id": 0})
print("\n2) Clinicas donde Sanji es gerente")
for local in data_02:
    print(local)

# Mostrar todos los documentos de la colección clinicas con capacidad >= 70
data_03 = coleccion_clinicas.find(
    {"capacidad": {"$gte": 70}}, {"_id": 0})
print("\n3) Clinicas con capacidad >= 70 personas")
for local in data_03:
    print(local)

# Mostrar todos los documentos de la colección clinicas con jornada diurna
data_04 = coleccion_clinicas.find({"jornada": "diurna"}, {"_id": 0})
print("\n4) Clinicas con jornada diurna")
for local in data_04:
    print(local)


print("\n\nConsultas sobre la colección Parques")
# Mostrar un documento de la coleccion parques con nombre Taurus
data_05 = coleccion_parques.find_one({"nombre": "Taurus"}, {"_id": 0})
print("\n1) Parques con nombre Taurus")
print(data_05)


# Mostrar todos los documentos de la colección parques con capacidad >= 450
data_06 = coleccion_parques.find({"capacidad": {"$gte": 450}}, {"_id": 0})
print("\n2) Parques con capacidad > 450 personas")
for centro in data_06:
    print(centro)

# Mostrar todos los documentos de la colección parques con tematica "Acuatica"
data_07 = coleccion_parques.find({"tematica": "Acuatica"}, {"_id": 0})
print("\n3) Parques con tematica Acuatica")
for centro in data_07:
    print(centro)

# Mostrar todos los documentos de la colección parques con instructor "Zoro"
data_08 = coleccion_parques.find({"instructor": "Zoro"}, {"_id": 0})
print("\n4) Parques con instructor Zoro")
for centro in data_08:
    print(centro)
