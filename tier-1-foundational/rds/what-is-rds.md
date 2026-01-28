# What is RDS? 🗄️

AWS's fully managed relational database service supporting MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.

## Core Concept

**RDS** (Relational Database Service) manages database infrastructure so you focus on your data. Automated backups, patching, replication, and failover.

```
Self-Managed Database:
├─ Buy servers
├─ Install OS
├─ Install database
├─ Configure backups
├─ Handle security patches
├─ Monitor health
├─ Scale manually
└─ Complex, error-prone

RDS:
├─ Select engine (MySQL, PostgreSQL)
├─ Choose instance size
├─ RDS handles everything else
├─ Automated backups
├─ Auto-failover for HA
├─ Easy scaling
└─ Simple, managed
```

## Database Engines

### MySQL/MariaDB

```
MySQL:
├─ Popular open-source relational DB
├─ Version: 5.7, 8.0
├─ Use case: Web applications, content sites
└─ InnoDB storage engine (default)

MariaDB:
├─ MySQL fork with improvements
├─ Version: 10.3, 10.4, 10.5, 10.6
├─ Better performance than MySQL 5.7
└─ Use case: MySQL replacement

Cost: Similar (~$0.12/hour for small instance)
Performance: MariaDB > MySQL
Compatibility: High (drop-in replacement)
```

### PostgreSQL

```
PostgreSQL:
├─ Advanced open-source relational DB
├─ Version: 11, 12, 13, 14, 15
├─ Most advanced features (JSON, arrays)
├─ Best for complex queries
└─ ACID transactions guaranteed

Use cases:
├─ Data warehousing
├─ Complex analytics
├─ JSON document storage
└─ Geographic data (PostGIS)

Cost: Similar to MySQL
Performance: Better for complex queries
Advantages: Better dev experience (advanced features)
```

### Oracle Database

```
Oracle:
├─ Enterprise relational database
├─ Version: 12c, 19c, 21c
├─ Most feature-rich database
├─ Highest cost, most powerful
└─ Critical enterprise systems

Use cases:
├─ Large enterprises
├─ Mission-critical systems
├─ Heavy licensing investment
└─ Advanced features needed

Cost: 3-5x more than open-source
Performance: Extremely high
Support: Enterprise-grade SLA
```

### SQL Server

```
Microsoft SQL Server:
├─ Enterprise relational database
├─ Version: 2019, 2022
├─ Windows integration
├─ T-SQL language
└─ Microsoft ecosystem

Use cases:
├─ .NET applications
├─ Windows-integrated environments
├─ Microsoft licensing already invested
└─ Business intelligence

Cost: 2-4x more than open-source
Performance: Enterprise-grade
Licensing: Per-core or subscription
```

## Instance Types

```
General Purpose (db.t3, db.m5):
├─ t3.small: 2 vCPU, 2GB RAM = $0.09/hour
├─ t3.large: 2 vCPU, 8GB RAM = $0.36/hour
├─ m5.large: 2 vCPU, 8GB RAM = $0.27/hour
└─ Use case: Most applications (web, APIs)

Memory Optimized (db.r5, db.r6):
├─ r5.large: 2 vCPU, 16GB RAM = $0.51/hour
├─ r5.2xlarge: 8 vCPU, 64GB RAM = $2.05/hour
└─ Use case: In-memory performance, caching

Storage Optimized (db.i3):
├─ i3.large: 2 vCPU, 16GB RAM + NVMe = $1.58/hour
└─ Use case: Data warehousing, high IOPS

Burst-capable (db.t3):
├─ Free tier eligible (t2.micro)
├─ Good for development
└─ Limited for production
```

## High Availability Setup

```
Multi-AZ Architecture:

Primary Instance (us-east-1a):
├─ Your main database
├─ Accepts reads and writes
├─ Continuously backed up
└─ Cost: Instance charges only

Standby Instance (us-east-1b):
├─ Synchronous replica
├─ Read-only (cannot access directly)
├─ Auto-promoted on primary failure
└─ Cost: Instance charges (double cost)

Failover process:
├─ Primary fails (hardware, software)
├─ DNS updated (~30-60 seconds)
├─ Standby promoted to primary
├─ New standby launched
└─ Zero data loss (synchronous replication)

Total cost: 2× instance cost
Example: 2× db.t3.large = $0.72/hour = $526/month
Benefits: 99.95% availability SLA
```

## Backup and Recovery

```
Automated Backups:
├─ Retention: 1-35 days (default 7)
├─ Frequency: Daily + transaction logs
├─ Restore window: Any point in time
├─ RPO: < 1 second
├─ RTO: < 1 minute
└─ Cost: Included in backup storage tier

Manual Snapshots:
├─ Unlimited retention
├─ Take anytime (even during queries)
├─ Share across accounts
└─ Cost: $0.095/GB/month storage

Backup storage cost:
├─ Automated: Up to DB size free, then $0.095/GB
├─ Snapshots: $0.095/GB/month
└─ Example: 100GB DB + 300GB snapshots = $38/month
```

## Real-World Pricing Example

```
Scenario: SaaS web application

Database Setup:
├─ Primary: db.t3.large (us-east-1a) = $0.36/hour
├─ Standby: db.t3.large (us-east-1b) = $0.36/hour (HA)
├─ Storage: 200GB SSD = $20/month
├─ Backup: Included
└─ Subtotal: $530/month

Monthly calculation:
├─ 2 instances × $0.36/hour × 730 hours = $526/month
├─ Storage: 200GB × $0.10 = $20/month
└─ Total: ~$546/month

Scaling scenario (traffic growth):
├─ Current: db.t3.large (production)
├─ 6 months later: Need db.m5.xlarge (10x traffic)
├─ Upgrade cost: $0.27/hour extra = ~$197/month
└─ Manual process: Minimal downtime (blue-green)

Annual cost: ~$6,600
Cost per transaction: Depends on volume
```

## Scaling Strategies

### Read Replicas

```
Setup: Add read-only copies

Master (db.t3.large) - $0.36/hour:
├─ Accepts reads and writes
├─ Continuously replicates
└─ Primary database

Read Replica 1 - $0.36/hour:
├─ Read-only (queries only)
├─ Low replication lag (< 100ms)
├─ Same region or different
└─ Load distributed

Read Replica 2 - $0.36/hour:
├─ Another read-only copy
├─ Separate workload (reports, analytics)
└─ Minimal impact on master

Cost with 2 replicas: $1.08/hour ($790/month)
Benefit: 3x read capacity, master unburdened
```

### Aurora Alternative

```
Why consider Aurora instead:

RDS MySQL (3 replicas):
├─ Cost: 3 × $0.36 = $1.08/hour
├─ Storage: 200GB × $0.10 = $20/month
└─ Total: $810/month

Aurora MySQL (reader auto-scale):
├─ Writer: db.r6g.large = $0.48/hour
├─ 5 readers (auto-added): Included
├─ Storage: 200GB × $0.10 = $20/month
└─ Total: ~$370/month

Savings: 50% cheaper with Aurora
Trade-off: Need to retest compatibility
```

## Best Practices

✅ Use Multi-AZ for production
✅ Enable automated backups
✅ Use read replicas for scaling reads
✅ Monitor with CloudWatch
✅ Regular maintenance windows
✅ Test restores quarterly
✅ Use Parameter Groups for tuning
✅ Enable encryption at rest
✅ Use Security Groups properly
✅ Version instances before major changes

## Common Mistakes

✗ Single-AZ for critical data (no HA)
✗ Leaving backups disabled (data loss risk)
✗ Oversizing instances (cost waste)
✗ No monitoring (surprises)
✗ Poor maintenance schedule (downtime)
✗ Hardcoding credentials (security risk)
✗ Not testing backup restoration
✗ Using wrong engine for workload

## Next Steps

→ [Database Engines](./database-engines.md) - Detailed comparison
→ [Performance Optimization](./performance.md) - Tuning guide
→ [Migration Guide](./migration.md) - From self-managed