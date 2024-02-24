## EBS Volume
- Stands for Elastic Block Store.
- It's based on network, so can be attached to instances while they're running. Also can be detached and attached to other instances.
- Persists data after termination.
- Bound to a specific AZ.
- Because it is network based, there might be some latency.
- Capacity can be increased over time.
- By default deleted on termination for the root, and persisted for other attached EBS volumes.

## EBS Volume Types
- There are 6 types of EBS volumes.
- gp2/gp3: General purpose SSD. Balances price and performance. For gp2 size and IOPS are linked. For gp3 IOPS and throughput can increase independently.
- io1/io2: Highest-performance SSD for mission critical low-latency or high-throughput workloads. They are known as Provisioned IOPS SSD. Good for databases.<br>
They also support multi-attachment. io2 block express even provides more IOPS and IOPS:GiB ratio.
- st1: Low cost HDD. Can't be boot volume.
- sc1: Lowest cost HDD for less frequently accessed data such as archives. Can't be boot volume.
- Multi-attach feature allows attaching the same EBS volume to multi EC2 instances in the same AZ. Only valid for io1/io2 EBS types. Useful for higher-availability<br>
and concurrent write operations. Allows multi-attach up to 16 EC2 instances at a time. Requires cluster-aware filesystem not XFS, EXT4, etc.

## Snapshots
- Allows copying data across different AZs or regions.
- EBS Snapshot Archive is the cheapest option, but takes 24-72 hours to restore archive.
- Recycle Bin for EBS Snapshots allows specifying retention from 1 day to 1 year and allows recovery after an accidental deletion.
- Fast Snapshot Restore have no latency on the first use, but expensive.
- We can create AMIs from EC2 instances and snapshot it into EBS volumes for later usage.

## Instance Store
- High-performance hardware disk on the physical machine that EC2 instance is running.
- Ephemeral.
- Good for short-term storage such as buffer, cache, temporary content etc.

## Encryption
- When a volume is encrypted:
    - Data at rest is encrypted.
    - Data moving between instance and the volume is encrypted.
    - All snapshots are encrypted.
    - All volumes created from snapshots are encrypted.
- How to encrypt an unencrypted EBS volume harder way:
    - Create an EBS snapshot.
    - Encrypt the EBS snapshot via copy function.
    - Create a new EBS volume from the snapshot.
    - Attach the encrypted volume to the instance.
- There is also a shortcut which is creating a new encrypted volume directly from unencrypted snapshot.

## EFS Volume
- It's a managed NFS. Thus, can be mounted to many EC2s across different AZs.
- Expensive. Paid by usage, no provision in advance. 
- Highly available and scalable. File system scales automatically.
- Uses NFSv4.1 protocol.
- Use cases are content management, web serving, data sharing, wordpress etc.
- Access control via security groups.
- Only compatible with Linux based AMI.
- Encryption at rest via KMS.

## EFS Modes & Storage Classes
- Performance mode:
    - General purpose: Default mode. It is for latency-sensitive use cases such as CMS, web server etc.
    - Max I/O: High latency, but high throughput and parallelism. Use cases such as big data processing, media processing etc.
- Throughput mode:
    - Bursting: Provides a throughput rate based on size + a burst rate up to a limit. For example for 1TB, 50MiB/s + 100MiB/s burst
    - Provisioned: Allows setting throughput regardless of storage size.
    - Elastic: Automatically scales throughput up and down based on workloads. Good if workload is unpredictable.
- Storage tiers:
    - Standard: For frequently accessed files.
    - Infrequent access(EFS-IA): Enabled with a Life-cycle Policy to move less frequently accessed files from standard tier to EFS-IA tier.
- Availability and durability:
    - Regional: Multi-AZ setup, great for prod.
    - One Zone: One AZ setuo, great for dev. Backup enabled by default. One Zone-IA provided most cost savings.

## Comparison of EBS and EFS
- EBS volumes are attached to one instance except io1/io2 which have multi-attach feature.
- EBS volumes are AZ scoped. We must use snapshots to create same data in different AZs.
- EFS can be mounted to 100s instances across different AZs.
- EFS only works with Linux instances.
- EFS expensive than EBS, but we can introduce cost saving via EFS-IA. 

## AMI
- AMIs are region scoped.