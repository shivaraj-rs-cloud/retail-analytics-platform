import sqlite3

conn = sqlite3.connect("retail.db")

cursor = conn.cursor()

# Revenue by Product
cursor.execute("""
CREATE VIEW IF NOT EXISTS revenue_by_product AS
SELECT
    p.product_name,
    p.category,
    SUM(s.sale_amount) AS revenue
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY p.product_name, p.category
""")

# Revenue by Store
cursor.execute("""
CREATE VIEW IF NOT EXISTS revenue_by_store AS
SELECT
    st.store_name,
    st.region,
    SUM(s.sale_amount) AS revenue
FROM sales s
JOIN stores st
ON s.store_id = st.store_id
GROUP BY st.store_name, st.region
""")

# Revenue by Month
cursor.execute("""
CREATE VIEW IF NOT EXISTS revenue_by_month AS
SELECT
    substr(sale_date,1,7) AS month,
    SUM(sale_amount) AS revenue
FROM sales
GROUP BY month
""")

cursor.execute("""
CREATE VIEW IF NOT EXISTS top_customers AS

SELECT
    customer_id,
    SUM(sale_amount) AS revenue
FROM sales
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 20
""")

cursor.execute("""
CREATE VIEW IF NOT EXISTS category_revenue AS

SELECT
    p.category,
    SUM(s.sale_amount) AS revenue
FROM sales s
JOIN products p
ON s.product_id = p.product_id
GROUP BY p.category
""")

conn.commit()

print("Views created successfully")

conn.close()