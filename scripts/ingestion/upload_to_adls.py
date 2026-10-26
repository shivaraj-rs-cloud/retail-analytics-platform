from azure.storage.blob import BlobServiceClient
import os

CONNECTION_STRING = "paste_connection_string"

container_name = "bronze"

blob_service_client = (
    BlobServiceClient.from_connection_string(
        CONNECTION_STRING
    )
)

container_client = (
    blob_service_client.get_container_client(
        container_name
    )
)

files = [
    "customers.csv",
    "products.csv",
    "sales.csv",
    "stores.csv",
    "inventory.csv"
]

for file in files:

    path = f"data/source/{file}"

    with open(path, "rb") as data:

        container_client.upload_blob(
            name=file,
            data=data,
            overwrite=True
        )

print("Upload Completed")