-- Top 10 Products by Revenue

SELECT
    product_id,
    SUM(sale_amount) AS revenue
FROM sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

-- Revenue by Region

SELECT
    st.region,
    SUM(s.sale_amount) AS revenue
FROM sales s
JOIN stores st
    ON s.store_id = st.store_id
GROUP BY st.region;


-- Top 10 Customers

SELECT
    customer_id,
    SUM(sale_amount) AS revenue
FROM sales
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 10;

-- Monthly Revenue

SELECT
    substr(sale_date,1,7) AS month,
    SUM(sale_amount) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Category Revenue

SELECT
    p.category,
    SUM(s.sale_amount) AS revenue
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- Total Revenue

SELECT
SUM(sale_amount) AS revenue
FROM fact_sales;

-- Top Products

SELECT
product_id,
SUM(sale_amount) revenue
FROM fact_sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

-- Top Stores

SELECT
store_id,
SUM(sale_amount) revenue
FROM fact_sales
GROUP BY store_id
ORDER BY revenue DESC
LIMIT 10;

-- Monthly Revenue

SELECT
substr(sale_date,1,7) month,
SUM(sale_amount) revenue
FROM fact_sales
GROUP BY month;