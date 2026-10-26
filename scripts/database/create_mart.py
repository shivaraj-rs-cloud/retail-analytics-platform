import sqlite3

conn = sqlite3.connect(
    "retail.db"
)

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS dim_customer AS

SELECT

customer_id,
customer_name,
city,
state

FROM customers

""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS dim_product AS

SELECT

product_id,
product_name,
category,
brand,
price

FROM products

""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS dim_store AS

SELECT

store_id,
store_name,
city,
state,
region

FROM stores

""")

cursor.execute("""

CREATE TABLE IF NOT EXISTS fact_sales AS

SELECT

sale_id,
customer_id,
product_id,
store_id,
quantity,
sale_amount,
sale_date

FROM sales

""")

conn.commit()

conn.close()

print("Star schema created")