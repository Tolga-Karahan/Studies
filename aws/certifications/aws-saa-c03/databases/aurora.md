## Aurora
- Has Postgres and MySQL compatible drivers.
- Storage is automatically scaled with 10GB increments up to 128TB.
- Can have up to 15 read replicas.
- Failover is instantaneous. There is one master.
- HA by default.
- Point in time restoration without using backups.
- Storage is split to 100s of volumes.
- There is a reader endpoint besides writer endpoint. It's a load balancer across all read replicas, so there
is no need to manually track them.
- We can also set read replica auto scaling in case read replicas are overloaded.
- Custom endpoints can be created. For example for a subset of replicas.
- Can be set up as serverless.
- Aurora Global Database provides more availability. There is 1 primary region for r/w operations, and up to 5 secondary regions. Allows 16  
read replicas for each secondary region. Promoting another region is under 1 minutes, cross-region replication takes less than 1 second.
- ML integration.

## Backups
- Automated backups can't be disabled.
- Manual back-up can stay as long as desired.
- Allows cloing databases which is faster than snapshot&restore thanks to copy-on-write protocol.

## High Availability and Scaling
- Data is replicated through 6 copies across 3 AZs. Needs 4 copies for writes, 3 copies for reads.
- Self-healing for corrupted data via peer-to-peer replication.

