from pprint import pprint
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
import uuid


def connect(client: MongoClient, db: str, collection: str) -> Collection:
    return client.get_database(db).get_collection(collection)


def insert_one(connection, data: dict):
    connection.insert_one(data)
    return data


def find(connection):
    return connection.find()


def update_one(connection, op: str, data: dict):
    # We should provide the operation to update a document
    _update_stmt = {op: data}
    return connection.update_one(filter={}, update=_update_stmt)


def delete_one(connection, filter):
    return connection.delete_one(filter=filter)


def delete_all(connection):
    return connection.delete_many(filter={})


def insert_some_data(connection, n_docs=2):
    for _ in range(n_docs):
        data = {
            "name": "Intro MongoDB",
            "Product ID": str(uuid.uuid4()),
            "type": "tutorial",
        }
        insert_one(connection, data)


if __name__ == "__main__":
    db = collection = "shop"
    client = MongoClient()
    connection = connect(client, db, collection)

    pprint(f"Server info:{client.server_info()}")
    pprint(f"Databases:{client.list_database_names()}")

    # Insert some data to work on
    insert_some_data(connection)

    cursor = find(connection)
    pprint([d for d in cursor])
    print()

    op = "$set"
    data = {"to_delete": True}
    update_one(connection, op, data)

    # Check results after update
    cursor = find(connection)
    pprint([d for d in cursor])
    print()

    delete_one(connection, filter={"to_delete": True})

    # Check results after delete one
    cursor = find(connection)
    pprint([d for d in cursor])
    print()

    # Clear the collection
    delete_all(connection)
