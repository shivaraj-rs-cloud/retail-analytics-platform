import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

df = pd.read_sql("""
SELECT *
FROM revenue_by_product
LIMIT 10
""", conn)

print(df)

conn.close()