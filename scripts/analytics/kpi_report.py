import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

queries = {

    "total_revenue":
    "SELECT SUM(sale_amount) revenue FROM sales",

    "total_orders":
    "SELECT COUNT(*) orders FROM sales",

    "total_customers":
    "SELECT COUNT(*) customers FROM customers",

    "total_products":
    "SELECT COUNT(*) products FROM products"
}

for name, query in queries.items():

    result = pd.read_sql(query, conn)

    print("\n")
    print(name.upper())
    print(result)

conn.close()