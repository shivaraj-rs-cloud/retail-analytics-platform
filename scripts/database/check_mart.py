# scripts/database/check_mart.py

import sqlite3

conn = sqlite3.connect("retail.db")

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name
""")

tables = cursor.fetchall()

for table in tables:
    print(table[0])

conn.close()