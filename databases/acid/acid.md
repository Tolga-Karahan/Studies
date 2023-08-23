## ACID
    ACID is a set of principles to ensure that transactions are processed in a reliable way. Although, relational database  
    systems offer ACID in general, some of the NOSQL databases are also ACID compliant. Those principles are as below:

            - Atomicity
            - Consistency
            - Isolation
            - Durability

    WAL can be used to ensure atomicity and durability. All changes are first written to a write-ahead log which must be  
    recorded in a stable storage. These changes are then flushed to disk in an appropriate time. 

### Atomicity
    Atomicity ensure that operations in a transaction either fail together or succeed together. They execute as a single  
    unit and in case of a failure of any operation, whole transaction fails and database is left unchanged. Otherwise, partially  
    successful operations can left database in an inconsistent state.

### Consistency
    Changes a transaction made must comply with database constraints and must left database in a consistent state. Otherwise  
    whole transaction fails.

### Isolation
    Concurrent transactions execute in isolation without affecting other transactions. They left the database in the same  
    state as if they are executed sequentially.

### Durability
    If a transaction is committed, changes it made must be persistent even in case of a failure.