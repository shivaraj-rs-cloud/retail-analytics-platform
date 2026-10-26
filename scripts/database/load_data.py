import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")

tables = {
    "customers": "data/source/customers.csv",
    "products": "data/source/products.csv",
    "stores": "data/source/stores.csv",
    "sales": "data/source/sales.csv",
    "inventory": "data/source/inventory.csv"
}

for table, file_path in tables.items():

    print(f"Loading {table}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table} loaded successfully")

conn.close()

print("All tables loaded")