## RDS
- Stands for Relational Database System.
- Managed SQL database. 
- Supports Postgres, MySQL, MariaDB, Oracle, Microsoft SQL Server, IBM Db2, Aurora.
- Supports automated database provision, OS patching, continuous backups, point in time restore, monitoring dashboards.
- Read replicas for improved read performance.
- Multi AZ setup for disaster recovery.
- Maintenance windows for updates.
- Horizontal and vertical scaling capability.
- Storage backed by EBS. gp2 or io1.
- Has a storage auto scaling feature. In case storage is running out of space, it is scaled automatically. We can set a Maximum Storage  
Threshold to prevent it grow infinetely. Decided if:
    - Free storage is less than 10% of allocated storage
    - Low-storage lasts at least 5 minutes
    - 6 hours passed since last modification
- Because it's a managed service, we can't access to underlying EC2 instance.
- RDS custom allows configuration on OS and db level and SSH access to the instance for Oracle and Microsoft SQL Server.

## Backups
- Daily full backup in backup window. Can be disabled.
- Transaction logs are backed-up every 5 minutes.
- Retention can be set between 1 and 35 days.
- Manual backups can be retented as long as desired.

## Read Replicas
- Up to 15 read replicas can be created. They can be in the same AZ, cross AZ or cross region.
- Replication is asynchronous and eventually consistent.
- Any replica can be converted to an independent database by removing it from replication.
- Connection must be handled in application level to leverage read replicas.
- If read replicas are in different AZs in the same region, no charge is applied. It is charged in case cross
region replicas are used.

## Multi-AZ Setup
- A standby instance used in another AZ and data is replicated synchronously on every change.
- In case of a failure DNS name will redirect to standby instance and an automatic failover will happen.
- Only used as a standby instance, no reads/writes are allowed.
- No downtime is required to change from single-AZ to multi-AZ setup. Steps:
    - A snapshot is created.
    - Snapshot restored to standby DB in a different AZ.
    -  Synchronization is established.

## Proxy
- We can put a proxy in front of RDS.
- RDS Proxy pools and shares connections.
- Reduces stress on database by reducing open connections.
- It's serverless, autoscaling and multi-AZ.
- Reduces RDS/Aurora failover time 66%.
- It is more important in case of Lambda functions. Because they can scale very fast and start and stop in relatively short time,  
they can left many connections. Instead RDS Proxy can be used to share connections in a pool across lambda functions.