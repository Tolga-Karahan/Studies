from typing import List
import uuid
from pprint import pprint
from random import randint, choice

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


def get_db(client: MongoClient, db: str):
    return client.get_database(db)


def get_collection(db: Database, collection: str) -> Collection:
    return db.get_collection(collection)


def create_collection(
    db: Database,
    collection: str,
    validator: dict = None,
    validation_level: str = "strict",
    validation_action="error",
):
    db.create_collection(
        collection,
        validator=validator,
        validationLevel=validation_level,
        validationAction=validation_action,
    )


# Write Concern is used to change behaviour of write operation. With
# default values server acknowledges that we made a write request and
# at some point it'll write it to journal and the records in the journal
# will be written to database at another point in time. If we want data
# to be written to the journal immediately we can make mongodb server to
# write opration to journal immediately by setting key "j": True. "w" key
# denotes number of instances write operation must be acknowledged.
def insert_one(collection: Collection, data: dict, write_concern={"w": 1}):
    collection.insert_one(data, {"write_concern": write_concern})
    return data


def insert_many(
    collection: Collection, data: List[dict], ordered=False, write_concern={"w": 1}
):
    # If ordered insert set to false, insert operation won't stop if
    # there is an error while inserting a document, instead it'll
    # continue with others. For example, if there is a key duplication
    # error, it won't stop the operation and will insert other docs
    # that are not present in the db.
    collection.insert_many(data, {"writeConcern": write_concern, "ordered": ordered})


def find_one(collection: Collection, filter: dict, projection: list = None):
    return collection.find_one(filter=filter, projection=projection)


def find_all(collection: Collection):
    return collection.find()


def find_many(collection: Collection, filter: dict, projection: list = None):
    return collection.find(filter=filter, projection=projection)


def replace_one(collection: Collection, filter: dict, data: dict):
    # Replaces the object with the provided object
    collection.replace_one(filter=filter, replacement=data)


def update_one(collection: Collection, op: str, data: dict, filter: dict = {}):
    # We should provide the operation to update a document
    _update_stmt = {op: data}
    return collection.update_one(filter=filter, update=_update_stmt)


def update_many(
    collection: Collection, op: str, data: dict, filter: dict = {}, array_filters=None
):
    # We should provide the operation to update a document
    _update_stmt = {op: data}
    return collection.update_many(
        filter=filter, update=_update_stmt, array_filters=array_filters
    )


def delete_one(collection: Collection, filter: dict):
    return collection.delete_one(filter=filter)


def delete_all(collection: Collection):
    return collection.delete_many(filter={})


def insert_some_data(collection: Collection, n_docs=4):
    for _ in range(n_docs):
        data = {
            "name": "Intro MongoDB",
            "Product ID": str(uuid.uuid4()),
            "type": "tutorial",
            "qty": randint(0, 100),
            "sold": randint(0, 100),
            "refunded": randint(0, 100),
        }
        insert_one(collection, data)


def insert_some_embed_docs(collection: Collection, n_docs=4):
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
    insert_one(collection, data)

    for _ in range(n_docs - 1):
        data = {
            "Product ID": "7ed036fc-ba8f-4093-b691-60988f267367",
            "name": "Intro MongoDB",
            "qty": 55,
            "sold": randint(0, 100),
            "refunded": randint(0, 100),
            "type": "tutorial",
            "details": [
                {
                    "subject": choice(subjects),
                    "lastUpdated": f"2023{randint(1, 13)}{randint(10, 31)}",
                    "seen": randint(0, 1000),
                },
                {
                    "subject": choice(subjects),
                    "lastUpdated": f"2023{randint(1, 13)}{randint(10, 31)}",
                    "seen": randint(0, 1000),
                },
            ],
        }
        insert_one(collection, data)


def print_many(cursor, msg=None):
    if msg:
        print(msg)

    pprint([d for d in cursor])
    print()


if __name__ == "__main__":
    client = MongoClient()
    db = get_db(client, "tutorial")
    collection = get_collection(db, "tutorial")

    pprint(f"Server info:{client.server_info()}")
    pprint(f"Databases:{client.list_database_names()}")

    # Insert some data to work on
    insert_some_data(collection)

    cursor = find_all(collection)
    print_many(cursor, "Initial Docs")

    op = "$set"
    data = {"to_delete": True}
    update_one(collection, op, data)

    # Check results after update
    cursor = find_all(collection)
    print_many(cursor, "Docs After Update")

    delete_one(collection, filter={"to_delete": True})

    # Check results after delete one
    cursor = find_all(collection)
    print_many(cursor, "Docs After Delete One")

    # Get docs with qty greater than 10
    cursor = find_many(collection, {"qty": {"$gt": 10}})
    print_many(cursor, "Docs with qty>10")

    # Get docs with qty less than 30 or greater than 60
    cursor = find_many(
        collection, {"$or": [{"qty": {"$lt": 30}}, {"qty": {"$gt": 60}}]}
    )
    print_many(cursor, "Docs with 30<qty<60")

    # Get id of the first object and replace it
    obj_id = find_one(collection, filter={})["_id"]
    data = {
        "Product ID": "7ed036fc-ba8f-4093-b691-60988f267367",
        "name": "Intro MongoDB",
        "qty": 55,
        "type": "tutorial",
        "sold": randint(0, 100),
        "refunded": randint(0, 100),
    }
    replace_one(collection, filter={"_id": obj_id}, data=data)

    # Check results after replace one
    cursor = find_all(collection)
    print_many(cursor, "Docs After Replace One")

    # Insert some embed docs
    insert_some_embed_docs(collection)

    # Check docs after insertion of embed docs
    print_many(find_all(collection), "Docs after inserting embed docs:")

    # Retrieve an embedded doc
    print("Get embedded doc")
    pprint(find_one(collection, {"details.subject": "crud"}, projection=["details"]))

    # Update one embed doc with subject crud
    # $ only updates first matched element in the array,
    # to update all we must use $[] operator.
    update_one(
        collection, "$set", {"details.$.available": False}, {"details.subject": "crud"}
    )

    # Add available field to all matching embedded
    # documents in the array.
    update_many(
        collection,
        "$set",
        {"details.$[].available": False},
        {"details.subject": "crud"},
    )
    print_many(find_all(collection), "Docs after updating availability:")

    # We can also filter based on matched array elements
    update_many(
        collection,
        "$set",
        {"details.$[elem].popular": True},
        {"details.subject": "crud"},
        [{"elem.seen": {"$gt": 100}}],
    )

    # Increment qty
    update_many(collection, "$inc", {"qty": 1}, {"name": "Intro MongoDB"})
    print_many(
        find_many(collection, {"name": "Intro MongoDB"}), "Docs After Incrementing qty:"
    )

    # Check docs after updating an embedded doc
    print_many(find_all(collection), "Docs After Updating An Embedded Doc:")

    # Get all docs which have details.available key
    cursor = find_many(collection, {"details.available": {"$exists": True}})
    print_many(cursor, "Docs with details.available key")

    # Drop details.available field
    update_many(collection, "$unset", {"details.available": ""})

    # Get all docs where sold > refunded
    cursor = find_many(collection, {"$expr": {"$gt": ["$sold", "$refunded"]}})
    print_many(cursor, "Docs with sold > refunded")

    # Get all docs with subject crud and have more than
    # 100 views. In this case, It'll return all docs that
    # have crud and more than 100 views in details array
    # no matter they are in the same object in the array
    # or not.
    cursor = find_many(
        collection,
        {"$and": [{"details.subject": "crud"}, {"details.seen": {"$gt": 100}}]},
    )
    print_many(cursor, "Docs with subject is crud and have more than 100 views:")

    # If we want to match conditions only to one element
    # in the array, we should use $elemMatch operator.
    cursor = find_many(
        collection,
        {"details": {"$elemMatch": {"subject": "crud", "seen": {"$gt": 100}}}},
    )
    print_many(
        cursor,
        "Docs with detail elements that have subject crud and more than 100 views:",
    )

    # We can push new elements to arrays via $push operation
    # Pushing one element
    update_many(
        collection,
        "$push",
        {"details": {"subject": "TCP/IP", "seen": 17}},
        {"details.subject": "security"},
    )

    # Pushing multiple elements at once
    update_many(
        collection,
        "$push",
        {
            "details": {
                "$each": [
                    {"subject": "ACID", "seen": 15},
                    {"subject": "Lazy Evaluation", "seen": 113},
                ]
            }
        },
        {"details.subject": "crud"},
    )
    print_many(
        find_all(collection),
        "Docs After Pushing New Details:",
    )

    # Clear the collection
    delete_all(collection)
