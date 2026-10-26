import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

df = pd.read_sql(
    "SELECT COUNT(*) AS total_sales FROM sales",
    conn
)

print(df)

conn.close()