## Data Types
    - Text
    - Boolean
    - Number
        - Integer(int32)
        - NumberLong(int64)
        - NumberDecimal()
    - ObjectId: Used to assign unique ids to each document. It also has a temporal component. Older ones come earlier.
    - ISODate
    - Timestamp: It is also unique for each document.
    - Embedded Document
    - Array

## Schemas
    Although MongoDB doesn't enforce schemas, we can still utilize schemas to store our data in more structured way.

    For one-to-one or one-to-many relationships we can use embedded documents to prevent unnecessary queries unless we don't
    have a specific requirement. One obstracle might be document size limit. For example, if many side of an one-to-man
    relationship is huge than we can opt for using different collections instead to bypass size limit.

    For many-to-many relationships we can opt for using different collections to prevent data duplication.

    In general this decision depends on relationships in our data, how frequently we make changes and application specific
    requirements.

    We can add validation to our schemas as well. To do it we use $jsonSchema object in PyMongo.
