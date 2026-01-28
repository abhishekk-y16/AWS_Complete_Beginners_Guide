# What is Aurora? 🌟

AWS's advanced relational database engine combining MySQL/PostgreSQL compatibility with enterprise reliability.

## Core Concept

**Aurora** is a relational database reimagined for cloud. It offers MySQL/PostgreSQL compatibility with 5x better performance and 3x better durability than standard RDS.

```
Traditional MySQL (RDS):
├─ Single master instance
├─ Replication lag (seconds)
├─ Manual failover (minutes)
├─ Storage: 64GB max per instance
└─ Performance: Baseline (100%)

Aurora:
├─ Multi-master or single-master
├─ Replication lag (milliseconds)
├─ Auto failover (30 seconds)
├─ Storage: Auto-expands to 128TB
└─ Performance: 5x faster reads
```

## How Aurora Works

```
Aurora Cluster Architecture:

Cluster Endpoints:
├─ Writer endpoint: Master instance
│  └─ Accepts reads and writes
├─ Reader endpoints: Read replicas
│  ├─ Replica 1: US-East-1a
│  ├─ Replica 2: US-East-1b
│  └─ Replica 3: US-East-1c
└─ Read-only cluster endpoint (auto-scale)

Storage Layer:
├─ 6-way replication across AZs
├─ Automatic failover within 30 seconds
├─ Self-healing (bit errors detected and fixed)
└─ Quorum-based commits for durability
```

## Aurora Editions

### Aurora MySQL

```
Compatible with MySQL 5.7 and 8.0
├─ Drop-in replacement
├─ Better performance (10,000 commits/sec)
├─ Enterprise features (no extra cost)
└─ 99.99% availability

Versions:
├─ Aurora MySQL 5.7 (EOL soon)
├─ Aurora MySQL 8.0 (current)
└─ Aurora MySQL 8.1 (latest)

Real-world: Migrating from RDS MySQL = 0 app changes
```

### Aurora PostgreSQL

```
Compatible with PostgreSQL 11-15
├─ Full compatibility
├─ Better performance (millions queries/sec)
├─ Aurora Babelfish for T-SQL (recent)
└─ 99.99% availability

Versions:
├─ PostgreSQL 11 (support ending)
├─ PostgreSQL 12-14 (current)
└─ PostgreSQL 15 (latest)

Advanced features:
├─ Native JSON queries
├─ Advanced analytics
└─ Machine learning integration
```

## Performance Comparison

```
Workload: E-commerce site, 100K concurrent users
Reads: 10M/minute, Writes: 500K/minute

Standard RDS MySQL:
├─ Instance: db.r6i.2xlarge (8 vCPU, 64GB RAM)
├─ Read replicas: 3 (3× cost)
├─ Queries/sec: 15,000
├─ Latency: 10ms (with replication lag)
└─ Total cost: ~$800/month

Aurora MySQL:
├─ Instance: db.r6g.2xlarge (8 vCPU, 64GB RAM)
├─ Read replicas: 5 (included!)
├─ Queries/sec: 75,000 (5x faster)
├─ Latency: 1ms (no replication lag)
└─ Total cost: ~$900/month (lower with auto-scaling)
```

## Read Scaling

```
Application traffic pattern:

Peak hours (5 PM - 9 PM):
├─ Reads: 500K queries/min
├─ Writes: 50K queries/min
├─ Ratio: 90% reads, 10% writes

Architecture:
├─ 1 writer instance (db.r6g.xlarge)
├─ 3 reader instances (auto-scaled)
│  ├─ Reader 1: ~167K reads/min
│  ├─ Reader 2: ~167K reads/min
│  └─ Reader 3: ~166K reads/min
└─ Connection pooling: Aurora Proxy

Application code: Just use reader endpoint!
```

## Backup and Recovery

```
Automated Backups:
├─ Retention: 1-35 days (default 7)
├─ Backups: Continuous (no snapshot needed)
├─ RPO: < 1 second
├─ RTO: < 1 minute
└─ Cost: Included in storage

Backup restoration:
├─ Restore to any point in time
├─ New cluster created (not original modified)
├─ Available within 5 minutes
└─ Billing: Separate cluster charges

Manual snapshots:
├─ Unlimited retention
├─ Share across accounts
├─ Export to S3 (Parquet format)
└─ Cost: $0.02/GB/month
```

## Pricing Model

```
Monthly cost breakdown for r6g.xlarge (4 vCPU, 32GB):

Writer instance: 730 hours × $0.48 = $350
Reader 1: 730 hours × $0.48 = $350
Reader 2: 730 hours × $0.48 = $350
Storage: 500GB × $0.10 = $50
I/O: 1M/month × $0.20 = $0.20
Backup: Included
Data transfer: ~$10

Total: ~$1,110/month (3-node cluster)

Savings vs RDS:
├─ RDS MySQL cluster: ~$1,450/month
├─ Aurora savings: $340/month (30% cheaper)
└─ With auto-scaling: Potential 50% savings
```

## Best Practices

✅ Use Aurora for production workloads
✅ Enable auto-scaling for read replicas
✅ Use connection pooling (Aurora Proxy)
✅ Implement read/write separation
✅ Monitor CPU and memory
✅ Use parameter groups for tuning
✅ Enable enhanced monitoring
✅ Regular backup testing
✅ Enable automatic minor version upgrades
✅ Use read-only cluster endpoint for reports

## Common Mistakes

✗ Not using Aurora Proxy (connection limits)
✗ Not separating reads and writes (bottleneck)
✗ Over-provisioning instances (cost waste)
✗ Ignoring storage auto-growth (surprises)
✗ Not testing read replica lag
✗ Using reader endpoint for writes
✗ Not monitoring slow query logs

## Next Steps

→ [Scaling Read Replicas](./read-replicas.md) - Advanced read scaling
→ [Global Database](./global-database.md) - Cross-region replication
→ [Performance Tuning](./performance.md) - Query optimization