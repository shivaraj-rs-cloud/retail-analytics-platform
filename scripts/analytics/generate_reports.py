import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

reports = {
    "Revenue By Product":
    "SELECT * FROM revenue_by_product LIMIT 10",

    "Revenue By Store":
    "SELECT * FROM revenue_by_store LIMIT 10",

    "Revenue By Month":
    "SELECT * FROM revenue_by_month"
}

for report_name, query in reports.items():

    print("\n" + "=" * 50)
    print(report_name)
    print("=" * 50)

    try:
        df = pd.read_sql(query, conn)
        print(df.head())
    except Exception as e:
        print(f"Error: {e}")

conn.close()