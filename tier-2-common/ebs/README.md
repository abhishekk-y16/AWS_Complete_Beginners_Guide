# EBS - Elastic Block Store 💾

High-performance block storage volumes for EC2 instances with automatic replication.

## Overview

EBS provides persistent block-level storage for EC2 instances. Think of it as an external hard drive for your cloud server. Data persists even when instance stops. Automatically replicated within availability zone.

## Volume Types

**General Purpose (gp3)**: Default choice
- Balanced price/performance
- $0.096 per GB/month
- 3,000-16,000 IOPS
- Web servers, small databases

**SSD (io1/io2)**: High-performance
- Databases, data warehouses
- $0.125 per GB/month
- Up to 64,000 IOPS
- Higher throughput

**Throughput-Optimized (st1)**: Big data
- HDDs for sequential I/O
- Data warehouses, log processing
- $0.045 per GB/month

**Cold HDD (sc1)**: Infrequent access
- Archives, backups
- $0.015 per GB/month

## EBS Volume Lifecycle

```
Create Volume
    ↓
Attach to EC2
    ↓
Format & Mount
    ↓
Use (store data)
    ↓
Create Snapshot (backup)
    ↓
Detach when done
    ↓
Delete (optional)
```

## Creating & Using a Volume

```bash
# Create 100GB gp3 volume
aws ec2 create-volume \
  --size 100 \
  --volume-type gp3 \
  --availability-zone us-east-1a

# Attach to EC2 instance
aws ec2 attach-volume \
  --volume-id vol-12345 \
  --instance-id i-67890 \
  --device /dev/sdf

# Inside EC2 instance:
sudo mkfs -t ext4 /dev/nvme1n1
sudo mkdir /data
sudo mount /dev/nvme1n1 /data
```

## Performance Metrics

```
Volume Type    Size        IOPS      Throughput    Cost/GB
gp3            1-16TB      3-16K     125-1000 MB/s $0.096
io2            4-64TB      64-100K   1000 MB/s     $0.125
st1            125GB-16TB  500       500 MB/s      $0.045
sc1            125GB-16TB  250       250 MB/s      $0.015
```

## Snapshots (Backups)

```
EBS Volume (100GB)
    ↓ Create Snapshot
    ↓ Copies to S3 (automatic)
    ↓
Snapshot (100GB, $0.05/month)
    ↓ Can create new volume
    ↓ In any AZ
```

## Real-World Example

```
E-commerce Website:

Root Volume (gp3 10GB):
├─ OS (Ubuntu)
├─ Web server
└─ Application code

Database Volume (io2 100GB):
├─ MySQL database (high IOPS)
├─ Nightly snapshot
└─ $0.125/month per GB

Storage Volume (st1 500GB):
├─ Customer backups
├─ Infrequent access
└─ $0.045/month per GB

Total: ~$10/month + snapshots
```

## Pricing

```
gp3 (100GB):
├─ Volume: 100 × $0.096 = $9.60
├─ Snapshots: $0.05 × copies
└─ IOPS (if >3000): $0.005 extra

io2 (100GB):
├─ Volume: 100 × $0.125 = $12.50
├─ 4000 IOPS: 1000 × $0.065 = $65/month
└─ High-cost solution for DB
```

## Common Use Cases

- **Databases**: RDS backend storage
- **Web Servers**: Root volume + data volume
- **Data Warehouses**: High IOPS needs
- **Backups**: Snapshot mechanism

## When to Use EBS

✅ Need persistent storage for EC2
✅ Database workloads
✅ Structured file storage
✅ Performance-critical apps

## When NOT to Use EBS

❌ Temporary data (use instance store)
❌ Shared storage (use EFS instead)
❌ Object storage (use S3 instead)

## EBS vs S3

```
EBS: Block storage, attached to EC2, up to 16TB
S3: Object storage, standalone, unlimited
```

## Best Practices

✅ Regular snapshots for backup
✅ Monitor CloudWatch metrics
✅ Right-size volume type
✅ Enable encryption
✅ Use gp3 for general workloads
✅ Detach unused volumes
✅ Tag volumes for cost tracking

## Related Topics

- [What is EBS](./what-is-ebs.md)
- [Volume Types](./volume-types.md)
- [EC2 Storage](../ec2/storage.md)
- [EFS - Shared Storage](../efs/what-is-efs.md)

## Resources

- [EBS Documentation](https://docs.aws.amazon.com/ebs/)
- [EBS Best Practices](https://docs.aws.amazon.com/ebs/latest/userguide/best-practices-for-ebs-volumes.html)
- [Volume Types Guide](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)