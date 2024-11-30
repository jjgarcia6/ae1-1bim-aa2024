"""Crear la base de datos de Python con SQLite"""

import sqlite3

# Ruta de la base de datos SQLite
DB_PATH = 'sqlite/baseDB.db'

# Crear una nueva conexión a la base de datos
conn = sqlite3.connect(DB_PATH)
