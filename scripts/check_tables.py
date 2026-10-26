import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

query = """
SELECT
    COUNT(*) AS total_sales
FROM sales
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()