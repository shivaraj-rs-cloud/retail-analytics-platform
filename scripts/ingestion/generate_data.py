print("Script Started")

import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

print("Database Connected")

queries = {
    "Total Orders":
        "SELECT COUNT(*) AS total_orders FROM sales",

    "Total Revenue":
        "SELECT SUM(sale_amount) AS total_revenue FROM sales",

    "Total Customers":
        "SELECT COUNT(*) AS total_customers FROM customers",

    "Total Products":
        "SELECT COUNT(*) AS total_products FROM products"
}

for report_name, query in queries.items():

    print("\n" + "="*40)
    print(report_name)
    print("="*40)

    df = pd.read_sql(query, conn)

    print(df)

conn.close()

print("\nReports Generated Successfully")