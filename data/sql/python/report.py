import sqlite3
import pandas as pd

conn = sqlite3.connect('../database.db')

query = """
SELECT user_id, SUM(amount) as total
FROM transactions
GROUP BY user_id
ORDER BY total DESC
"""

df = pd.read_sql(query, conn)

df.to_csv('../report.csv', index=False)

print("Reporte generado")
