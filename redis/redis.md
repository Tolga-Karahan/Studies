## Redis

Redis stands for remote dictionary server. It's a in-memory database. Mostly used as a cache to improve performance, but can be used as a fully-fledged database as   
well. It's a multi-model database and able to store different data structures. We can use Redis Core as key-value store, and extend Redis with Redis modules such as  
RediSearch, RedisGraph, RedisTimeSeries, etc to support different data types. 

Redis doesn't need schemas, it is a schemaless database. Because it doesn't need to create schemas, it initializes fast.

It's a in-memory database, and if server goes down it means we lose data. To prevent it we can use replicas, or even persistence. We can use snapshots to persist  
data point-in-time in disk. We can still lose data written between snapshots. To even prevent that we can use append only files which is a continuous record of  
every write operation. When Redis restarts, it will replay AOF and rebuild the state.

To scale Redis we can use clustering. One instance acts as a primary which handles both reads and writes, and others act as read replicas. In case primary fails,  
one of the read replicas can take the role of primary. In case data is too much to fit into one server's ram, or the primary is not able to handle all write operations  
we can use sharding. In this setup, each server works on a shard of the data and handles all read/write oprations.