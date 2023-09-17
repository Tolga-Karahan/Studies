from pprint import pprint
from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection

from crud.crud import find_all, delete_all, print_many


def connect(client: MongoClient, db: str, collection: str) -> Collection:
    return client.get_database(db).get_collection(collection)


def insert_many(collection: Collection, data: List[dict]):
    collection.insert_many(data)


def insert_some_data(customers_collection: Collection, products_collection: Collection):
    customers = [
        {"name": "Bob", "orders": ["id1", "id2"]},
        {"name": "Sarah", "orders": ["id2", "id3"]},
    ]

    products = [
        {"_id": "id1", "type": "Book"},
        {"_id": "id2", "type": "T-shirt"},
        {"_id": "id3", "type": "Food"},
    ]

    insert_many(customers_collection, customers)
    insert_many(products_collection, products)


def aggregate(collection: Collection, aggregations: List[dict]):
    return collection.aggregate(aggregations)


if __name__ == "__main__":
    client = MongoClient()
    db = "shop"
    customers = connect(client, db, "customers")
    products = connect(client, db, "products")

    # Clear the DB
    delete_all(customers)
    delete_all(products)

    # Insert data
    insert_some_data(customers, products)

    # Check docs after insert
    print_many(find_all(customers), "Customers Docs After Insert:")
    print_many(find_all(products), "Products Docs After Insert:")

    # We can use lookup to join different collections
    lookup_stmt = {
        "$lookup": {
            "from": "products",
            "localField": "orders",
            "foreignField": "_id",
            "as": "order_products",
        }
    }
    print_many(aggregate(customers, [lookup_stmt]), "Lookup:")
