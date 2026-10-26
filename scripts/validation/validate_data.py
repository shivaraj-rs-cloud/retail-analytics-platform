import pandas as pd

customers = pd.read_csv("data/source/customers.csv")
products = pd.read_csv("data/source/products.csv")
sales = pd.read_csv("data/source/sales.csv")
stores = pd.read_csv("data/source/stores.csv")
inventory = pd.read_csv("data/source/inventory.csv")

print("\n===== DATA QUALITY CHECKS =====")

# Customer Checks
print("\nCustomers")

print(
    "Null Customer IDs:",
    customers["customer_id"].isnull().sum()
)

print(
    "Duplicate Customer IDs:",
    customers["customer_id"].duplicated().sum()
)

# Product Checks
print("\nProducts")

print(
    "Negative Prices:",
    len(products[products["price"] <= 0])
)

# Sales Checks
print("\nSales")

print(
    "Duplicate Sale IDs:",
    sales["sale_id"].duplicated().sum()
)

print(
    "Negative Sales:",
    len(sales[sales["sale_amount"] <= 0])
)

# Inventory Checks
print("\nInventory")

print(
    "Negative Stock:",
    len(
        inventory[
            inventory["stock_quantity"] < 0
        ]
    )
)

print("\nValidation Complete")