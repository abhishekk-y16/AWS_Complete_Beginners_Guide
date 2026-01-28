# What is EBS? 💾

Elastic Block Storage - persistent storage volumes for EC2 instances.

## Core Concept

**EBS** provides block storage volumes that attach to EC2 instances, like a USB drive for servers.

```
Without EBS:
├─ EC2 instance storage: Lost when instance stops!
├─ No persistence
├─ Can't backup data
└─ Data loss on crash

With EBS:
├─ Persistent storage
├─ Survives instance stop/reboot
├─ Create snapshots (backup)
├─ Clone volumes
└─ Data always available!
```

## Volume Types

### General Purpose (gp3/gp2)

```
Best for: Most workloads

gp3 (Latest):
├─ 3,000-16,000 IOPS
├─ 125-1,000 MB/s throughput
├─ 1GB-16TB size
├─ Cost: $0.08/GB/month
└─ Use case: Web servers, databases

gp2 (Older):
├─ 100-16,000 IOPS (burst)
├─ 1GB-16TB size
├─ Cost: $0.10/GB/month
└─ Use case: Legacy systems
```

### Provisioned IOPS (io1/io2)

```
Best for: High-performance databases

io2:
├─ Up to 64,000 IOPS
├─ Consistent performance
├─ Size: 4GB-16TB
├─ Cost: $0.125/GB/month + IOPS costs
└─ IOPS pricing: $0.065 per IOPS/month

Example: 100GB, 5,000 IOPS:
├─ Volume: 100 × $0.125 = $12.50
├─ IOPS: 5,000 × $0.065 = $325
└─ Total: $337.50/month

Use case: Databases, analytics
```

### Throughput Optimized (st1)

```
Best for: Big data, data warehouses

Characteristics:
├─ Up to 500 MB/s throughput
├─ 125 IOPS
├─ Cost: $0.045/GB/month
└─ Size: 125GB-16TB

Use case:
├─ MapReduce
├─ Hadoop
├─ Redshift
└─ Log processing
```

### Cold Storage (sc1)

```
Best for: Infrequently accessed data

Characteristics:
├─ Up to 250 MB/s throughput
├─ 250 IOPS
├─ Cost: $0.015/GB/month
└─ Size: 125GB-16TB

Use case:
├─ Cold backups
├─ Disaster recovery
├─ Old archives
└─ Rarely accessed data
```

## Snapshots

Backup volumes to S3:

```
Volume Snapshot Workflow:

EBS Volume (10GB):
├─ Full Snapshot (10GB)
└─ S3 storage: $0.05 per GB/month = $0.50

Next Week - Incremental Snapshot:
├─ Only 2GB changed
├─ Snapshot (2GB)
└─ S3 storage: $0.10 (incremental)

Two weeks later:
├─ Total snapshots: 10GB + 2GB + 1.5GB
├─ Total storage: 13.5GB
└─ Cost: $0.675/month

Restore:
└─ Create new volume from any snapshot (seconds)
```

## Encryption

Protect data at rest:

```
Encrypted Volume:

Writing:
└─ Data encrypted before storage

Reading:
└─ Data decrypted automatically

Key Management:
├─ AWS managed key: Default
├─ Customer managed key: KMS
└─ Separate from root account

Performance:
└─ No overhead (CPU accelerated)

Cost:
└─ No additional charge for encryption
```

## Volume Performance

```
Volume Types Comparison:

┌─────────────┬────────┬─────────┬───────┐
│ Type        │ IOPS   │ MB/s    │ Cost  │
├─────────────┼────────┼─────────┼───────┤
│ gp3         │ 3K-16K │ 125-1K  │ $0.08 │
│ io2         │ 64K    │ 1K      │ $0.13 │
│ st1         │ 500    │ 500     │ $0.045│
│ sc1         │ 250    │ 250     │ $0.015│
└─────────────┴────────┴─────────┴───────┘
```

## Real-World Example: Database Server

```
Setup: MySQL Database on EC2

Volumes:

1. Root Volume (gp3):
   ├─ Size: 30GB
   ├─ IOPS: 5,000
   ├─ Mount: /
   └─ Cost: $2.40 + IOPS

2. Data Volume (io2):
   ├─ Size: 1TB
   ├─ IOPS: 20,000
   ├─ Mount: /var/lib/mysql
   └─ Cost: $130 + IOPS

3. Backup Volume (sc1):
   ├─ Size: 2TB
   ├─ Mount: /backup
   └─ Cost: $30/month

Daily Backup:
├─ Create snapshot of data volume
├─ Cost: $0.05 per GB = $50/month
└─ Can restore in seconds

Total cost: ~$215/month
Performance: 20K IOPS (fast!)
Reliability: Daily snapshots
```

## Multi-Attach Volumes

Share volume across instances:

```
Traditional:
└─ 1 Volume → 1 Instance

Multi-Attach (io1/io2 only):
└─ 1 Volume → Up to 16 Instances
   └─ Shared storage
   └─ All see same data
   └─ Use cases: Shared database, cluster

Configuration:
├─ All instances: Same AZ required
├─ Filesystem: Must support multi-attach (Ext4, XFS)
├─ Locking: Application must manage
└─ Cost: $0.15 per 100 IOPS (additional)
```

## Availability & Redundancy

```
Single AZ:
├─ Volume in single availability zone
├─ Instance failure → Can't access
├─ Risk: AZ-level outage

Multi-AZ (with snapshots):
├─ Create snapshot
├─ Restore to different AZ
├─ New instance in AZ-2
├─ Failover: Automatic with setup
└─ Result: High availability
```

## Cost Optimization

```
Scenario: 10 database servers, each 500GB

Current (io2, 10K IOPS each):
├─ Volume: 10 × 500GB × $0.125 = $625
├─ IOPS: 10 × 10K × $0.065 = $6,500
└─ Monthly: $7,125

Optimization 1: Use gp3 instead:
├─ Volume: 10 × 500GB × $0.08 = $400
├─ IOPS: Included (3K baseline)
└─ Monthly: $400 (saves $6,725!)

Optimization 2: Archive old data to S3:
├─ Remove old volumes
├─ 5TB data → S3
├─ S3 cost: 5TB × $0.023 = $115
└─ Save entire EBS volumes!
```

## Common Mistakes

### ✗ Mistake 1: No Snapshots

```
Wrong:
├─ EBS volume fails
├─ Data lost permanently
├─ No backups exist
└─ Disaster!

Right:
├─ Daily automatic snapshots
├─ Can restore in seconds
├─ Disaster averted!
```

### ✗ Mistake 2: Wrong Volume Type

```
Wrong:
├─ Use gp3 for database (insufficient IOPS)
├─ Performance degrades
├─ Queries slow down
└─ Users complain

Right:
├─ Measure IOPS needed
├─ Use io2 for high IOPS
├─ Performance excellent
```

### ✗ Mistake 3: No Encryption

```
Wrong:
├─ Unencrypted volume
├─ Breach → Data exposed
├─ Compliance violation
└─ Liability!

Right:
├─ Enable encryption (default)
├─ No performance impact
├─ Data secure
```

### ✗ Mistake 4: Ignoring Snapshots Cost

```
Wrong:
├─ Create snapshot daily
├─ 1000 snapshots accumulate
├─ Snapshot storage: $50/month
└─ Unnoticed cost creep

Right:
├─ Implement lifecycle policy
├─ Keep 7 daily, 4 weekly, 12 monthly
├─ Automatic cleanup
└─ Controlled cost
```

## Best Practices

✅ Use gp3 for most workloads
✅ Enable snapshots for all volumes
✅ Encrypt important data
✅ Monitor volume metrics
✅ Size volumes appropriately
✅ Use provisioned IOPS for databases
✅ Implement backup policies
✅ Clean up old snapshots
✅ Test volume restoration
✅ Document volume configurations

## CLI Examples

```bash
# Create EBS volume
aws ec2 create-volume \
  --size 100 \
  --availability-zone us-east-1a \
  --volume-type gp3 \
  --iops 5000 \
  --throughput 250

# Create snapshot
aws ec2 create-snapshot \
  --volume-id vol-123456 \
  --description "Database backup"

# Create volume from snapshot
aws ec2 create-volume \
  --snapshot-id snap-123456 \
  --availability-zone us-east-1b \
  --volume-type gp3

# List volumes
aws ec2 describe-volumes \
  --filters "Name=status,Values=in-use"
```

## Next Steps

→ [EBS Performance Tuning](./performance.md) - Optimize IOPS
→ [Snapshots & Backups](./snapshots.md) - Disaster recovery
→ [Encryption](./encryption.md) - Data security