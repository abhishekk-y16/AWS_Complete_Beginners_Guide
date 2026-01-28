# Aurora 🚀

High-performance MySQL and PostgreSQL compatible relational database with enterprise features.

## Overview

Aurora is AWS's relational database built for cloud. MySQL/PostgreSQL compatible but 3x faster than MySQL, 2x faster than PostgreSQL. Automatic scaling, backups, replication. Pay per second. Ideal for high-traffic applications.

## Key Features

- ✅ 3x MySQL performance, 2x PostgreSQL performance
- ✅ MySQL and PostgreSQL compatible
- ✅ Automatic scaling (up to 128 TB)
- ✅ Multi-AZ with automatic failover
- ✅ Read replicas in seconds
- ✅ Automated backups (35-day retention)

## Aurora Editions

**Aurora MySQL**:
- Compatible with MySQL 5.7 and 8.0
- Drop-in replacement for MySQL
- MySQL features + Aurora enhancements

**Aurora PostgreSQL**:
- Compatible with PostgreSQL 11-15
- Drop-in replacement for PostgreSQL
- PostGIS support for geospatial data

**Aurora Serverless**:
- Auto-scaling without managing capacity
- Pay per second for compute
- Great for variable workloads

## Architecture Advantages

- **Shared Storage**: Single logical volume across AZs
- **Fast Failover**: <30 seconds
- **Read Replicas**: Up to 15 replicas globally
- **Global Database**: Multi-region replication
- **Instant Cloning**: Clone databases in seconds

## Pricing Comparison

| Product | db.t3.medium | Monthly Cost |
|---------|---|---|
| MySQL RDS | Yes | ~$90 |
| Aurora MySQL | Yes | ~$110 |
| Aurora Serverless | N/A | $0.06/ACU (pay per second) |

Aurora: Better performance, similar/slightly higher cost

## Read Replicas

Create read-only copies:
- Same region (seconds to setup)
- Different region (minutes to setup)
- Automatic promotion on primary failure

Use cases:
- Scale read workload
- Analytics queries
- Multi-region availability

## Backups & Recovery

- **Automatic Backups**: 35-day retention
- **Snapshots**: Manual backups (unlimited)
- **Point-in-Time Recovery**: Any second in retention window
- **Backup Cost**: Only storage charged (incremental)

## Global Database

- Primary region: Read/Write
- Secondary regions: Read-only
- <1 second replication lag
- Regional failover

Example: 
- US Primary → EU Read Replica
- Application queries local replica
- RPO: <1 second, RTO: <1 minute

## Use Cases

- **High-Traffic Applications**: E-commerce, SaaS
- **Real-time Analytics**: Fast queries on large datasets
- **Global Applications**: Multi-region deployment
- **Demanding Workloads**: Financial systems, gaming

## Best Practices

✅ Use Aurora MySQL 8.0 for new projects
✅ Enable backtrack (point-in-time recovery)
✅ Multi-AZ deployment for production
✅ Read replicas for scaling reads
✅ Enable encryption at rest and transit
✅ Monitor query performance
✅ Use Aurora Serverless for variable loads

## Performance Features

- **Connection Pooling**: PgBouncer support
- **Query Cache**: Automatic result caching
- **Parallel Query**: Distribute queries across nodes
- **Intelligent Tiering**: Automatic volume optimization

## Next Steps

→ [Aurora Documentation](https://docs.aws.amazon.com/rds/latest/userguide/Aurora.html)
→ [Global Database Setup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-databases.html)
→ [RDS Console](https://console.aws.amazon.com/rds/)