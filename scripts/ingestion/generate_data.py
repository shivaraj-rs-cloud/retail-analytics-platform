from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for i in range(1, 101):
    customers.append([
        i,
        fake.name(),
        fake.city(),
        fake.state()
    ])

df = pd.DataFrame(
    customers,
    columns=[
        "customer_id",
        "name",
        "city",
        "state"
    ]
)

df.to_csv(
    "data/source/customers.csv",
    index=False
)

print("Customers data created")