import uuid
from pprint import pprint
from random import randint, choice

from pymongo import MongoClient
from pymongo.collection import Collection


def connect(client: MongoClient, db: str, collection: str) -> Collection:
    return client.get_database(db).get_collection(collection)


def insert_one(connection: Collection, data: dict):
    connection.insert_one(data)
    return data


def find_one(connection: Collection, filter: dict, projection: list = None):
    return connection.find_one(filter=filter, projection=projection)


def find_all(connection: Collection):
    return connection.find()


def find_many(connection: Collection, filter: dict, projection: list = None):
    return connection.find(filter=filter, projection=projection)


def replace_one(connection: Collection, filter: dict, data: dict):
    # Replaces the object with the provided object
    connection.replace_one(filter=filter, replacement=data)


def update_one(connection: Collection, op: str, data: dict, filter: dict = {}):
    # We should provide the operation to update a document
    _update_stmt = {op: data}
    return connection.update_one(filter=filter, update=_update_stmt)


def delete_one(connection: Collection, filter: dict):
    return connection.delete_one(filter=filter)


def delete_all(connection: Collection):
    return connection.delete_many(filter={})


def insert_some_data(connection: Collection, n_docs=4):
    for _ in range(n_docs):
        data = {
            "name": "Intro MongoDB",
            "Product ID": str(uuid.uuid4()),
            "type": "tutorial",
            "qty": randint(0, 100),
        }
        insert_one(connection, data)


def insert_some_embed_docs(connection: Collection, n_docs=4):
    subjects = [
        "crud",
        "relations",
        "security",
        "Indexes",
        "Deployment",
        "Performance",
        "Architecture",
        "Drivers",
    ]

    data = {
        "Product ID": "7ed036fc-ba8f-4093-b691-60988f267367",
        "name": "Intro MongoDB",
        "qty": 55,
        "type": "tutorial",
        "details": [
            {
                "subject": "crud",
                "lastUpdated": f"2023{randint(1, 13)}{randint(10, 31)}",
            },
            {
                "subject": choice(subjects),
                "lastUpdated": f"2023{randint(1, 13)}{randint(10, 31)}",
            },
        ],
    }
    insert_one(connection, data)

    for _ in range(n_docs - 1):
        data = {
            "Product ID": "7ed036fc-ba8f-4093-b691-60988f267367",
            "name": "Intro MongoDB",
            "qty": 55,
            "type": "tutorial",
            "details": [
                {
                    "subject": choice(subjects),
                    "lastUpdated": f"2023{randint(1, 13)}{randint(10, 31)}",
                },
                {
                    "subject": choice(subjects),
                    "lastUpdated": f"2023{randint(1, 13)}{randint(10, 31)}",
                },
            ],
        }
        insert_one(connection, data)


def print_many(cursor, msg=None):
    if msg:
        print(msg)

    pprint([d for d in cursor])
    print()


if __name__ == "__main__":
    db = collection = "tutorial"
    client = MongoClient()
    connection = connect(client, db, collection)

    pprint(f"Server info:{client.server_info()}")
    pprint(f"Databases:{client.list_database_names()}")

    # Insert some data to work on
    insert_some_data(connection)

    cursor = find_all(connection)
    print_many(cursor, "Initial Docs")

    op = "$set"
    data = {"to_delete": True}
    update_one(connection, op, data)

    # Check results after update
    cursor = find_all(connection)
    print_many(cursor, "Docs After Update")

    delete_one(connection, filter={"to_delete": True})

    # Check results after delete one
    cursor = find_all(connection)
    print_many(cursor, "Docs After Delete One")

    # Get docs with qty greater than 10
    cursor = find_many(connection, {"qty": {"$gt": 10}})
    print_many(cursor, "Docs with qty>10")

    # Get id of the first object and replace it
    obj_id = find_one(connection, filter={})["_id"]
    data = {
        "Product ID": "7ed036fc-ba8f-4093-b691-60988f267367",
        "name": "Intro MongoDB",
        "qty": 55,
        "type": "tutorial",
    }
    replace_one(connection, filter={"_id": obj_id}, data=data)

    # Check results after replace one
    cursor = find_all(connection)
    print_many(cursor, "Docs After Replace One")

    # Insert some embed docs
    insert_some_embed_docs(connection)

    # Check docs after insertion of embed docs
    print_many(find_all(connection), "Docs after inserting embed docs:")

    # Retrieve an embedded doc
    print("Get embedded doc")
    pprint(find_one(connection, {"details.subject": "crud"}, projection=["details"]))

    # Update one embed doc with subject crud
    update_one(
        connection, "$set", {"details.$.available": False}, {"details.subject": "crud"}
    )

    # Check docs after updating an embedded doc
    print_many(find_all(connection), "Docs After Updating An Embedded Doc:")

    # Clear the collection
    delete_all(connection)
