import pandas as pd
import sqlite3

# Leer archivo CSV
df = pd.read_csv('../data/raw_transactions.csv')

# Crear base de datos
conn = sqlite3.connect('../database.db')

# Guardar datos en tabla
df.to_sql('transactions', conn, if_exists='replace', index=False)

print("Datos cargados correctamente")
