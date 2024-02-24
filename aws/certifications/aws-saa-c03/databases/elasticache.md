## ElastiCache
- It's a managed cache service. Supports Redis and Memcached.
- Caches are in-memory databases with high performance and low latency.
- Can reduce load of databases for read-intensive operations.
- Can store states and allows the application to be stateless.
- Incorporating it will require changes in the code.
- Can store session so that user can use same session in case they redirected to another instance.
- Redis is highly-available, multi-AZ cache with data replication. Memcached doesn't have this features.  
It's a distributed cache and used for applications that tolerate data loss.

## Security
- Supports IAM authentication for Redis. IAM policies used for AWS API-level security.
- Redis AUTH can be used to set password/token.
- Support in-flight encryption for Redis.
- SASL based authentication support for Memcached.