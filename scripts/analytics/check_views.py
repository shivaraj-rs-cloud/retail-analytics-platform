import sqlite3

conn = sqlite3.connect("retail.db")

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='view'
ORDER BY name
""")

views = cursor.fetchall()

print("Views found:\n")

if len(views) == 0:
    print("No views found")
else:
    for view in views:
        print(view[0])

conn.close()