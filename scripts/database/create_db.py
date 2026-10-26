import sqlite3

conn = sqlite3.connect(
    "retail.db"
)

print("Database Created")

conn.close()