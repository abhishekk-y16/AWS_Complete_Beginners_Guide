# RDS Database Engines 🗄️

Choose the right database engine for your application needs.

## Overview: Which Engine Should You Use?

```
Requirements:
├─ Need SQL? PostgreSQL, MySQL, MariaDB, Oracle, SQL Server
├─ Need NoSQL? DynamoDB (different service)
├─ Legacy system? Oracle or SQL Server
└─ Cloud-native? PostgreSQL or MySQL
```

## PostgreSQL

### What is PostgreSQL?

Open-source, advanced SQL database with JSON support and complex queries.

```
Best for:
✅ Complex queries
✅ JSON/NoSQL-like data
✅ Analytics
✅ Stored procedures
✅ Cost-effective (open source)

NOT ideal for:
❌ Real-time analytics at scale (use Redshift)
❌ Ultra-high throughput (use purpose-built)
```

### PostgreSQL Features

```
JSON Support:
├─ Store JSON in columns
├─ Query JSON like NoSQL
└─ Hybrid relational + document

Full-Text Search:
├─ Search entire documents
├─ Ranking results
└─ Multiple languages

Arrays:
├─ Array data types
├─ Array operations
└─ Efficient

Stored Procedures:
├─ PL/pgSQL language
├─ Server-side logic
└─ Complex operations
```

### PostgreSQL Performance

```
Pricing: AWS managed
└─ db.t3.micro: $0.017/hour (~$12/month)
└─ db.r5.large: $0.34/hour (~$248/month)

Throughput:
├─ Single instance: ~10K queries/sec
├─ With read replicas: 100K+ queries/sec
└─ With Aurora: 500K+ queries/sec
```

### PostgreSQL Use Case

```
Scenario: SaaS application with complex queries

Database:
├─ Users table (relational)
├─ Settings (JSON column)
├─ Logs (full-text search)
└─ Metrics (arrays)

Why PostgreSQL:
✅ Single engine handles all
✅ No need for multiple databases
✅ JSON for flexibility
✅ Full-text for search
✅ Open source (no licensing)

Cost: ~$50-200/month (single db.r5.large)
```

## MySQL

### What is MySQL?

Lightweight, fast SQL database. Popular for web applications.

```
Best for:
✅ Web applications (WordPress, Drupal)
✅ High throughput
✅ Simple schemas
✅ Cost-effective
✅ 24/7 availability

NOT ideal for:
❌ Complex transactions
❌ Analytics (PostgreSQL better)
```

### MySQL vs PostgreSQL

```
┌─────────────────────┬──────────┬────────────┐
│ Feature             │ MySQL    │ PostgreSQL │
├─────────────────────┼──────────┼────────────┤
│ JSON support        │ Basic    │ Advanced   │
│ Stored procedures   │ Simple   │ Complex    │
│ Full-text search    │ Basic    │ Advanced   │
│ Transactions        │ Good     │ Excellent  │
│ Cost                │ Low      │ Low        │
│ Throughput          │ High     │ Good       │
│ Replication         │ Easy     │ Flexible   │
└─────────────────────┴──────────┴────────────┘
```

### MySQL Use Case

```
Scenario: High-traffic web application

Traffic: 100K requests/minute
Queries: Simple, mostly SELECT
Data: Relational, standard schema

Why MySQL:
✅ Designed for throughput
✅ Easy replication (read replicas)
✅ Mature (20+ years)
✅ WordPress/Drupal standard
✅ Fast queries

Cost: ~$50-200/month (similar to PostgreSQL)
```

## MariaDB

### What is MariaDB?

MySQL fork, drop-in replacement, open-source continuation.

```
History:
MySQL 5.7 → MySQL 8.0 (now Oracle's)
        └─ MySQL developer creates MariaDB
        └─ MySQL fork, independent project
        └─ Faster, more transparent

Best for:
✅ MySQL users wanting independence
✅ Open-source only
✅ Compatibility with MySQL
```

### MariaDB vs MySQL

```
Both similar, MariaDB advantages:
├─ Independent (not Oracle)
├─ Faster performance
├─ Column compression
├─ Storage engines
└─ Open source commitment

Choose MySQL if:
└─ Need existing MySQL expertise

Choose MariaDB if:
└─ Want open-source continuity
```

## Oracle Database

### What is Oracle?

Enterprise database with advanced features. High cost, high power.

```
Best for:
✅ Enterprise (banking, government)
✅ Mission-critical systems
✅ Complex transactions
✅ Existing Oracle environment

NOT ideal for:
❌ Startups (expensive)
❌ Cost-sensitive
❌ Simple applications
```

### Oracle Features

```
Advanced Security:
├─ Encryption at rest + transit
├─ Fine-grained access control
├─ Audit trails
└─ Multiple security domains

Performance:
├─ Parallel query execution
├─ In-memory database
├─ Extreme scale
└─ Multi-terabyte capacity

Enterprise Features:
├─ Data Guard (replication)
├─ RAC (Real Application Clusters)
├─ Golden Gate (sync to other systems)
└─ GoldenGate (real-time replication)
```

### Oracle Pricing

```
AWS RDS for Oracle:
db.t3.medium: $1.47/hour
= ~$1,060/month (24/7)

SE2 License: ~$5,000/month extra
Total: ~$6,000/month

Owned Oracle License: Bring Your Own License (BYOL)
└─ Lower pricing if you have license
```

### Oracle Use Case

```
Scenario: Financial institution core banking

Data: Terabytes of mission-critical transactions
Availability: 99.99% required
Security: Regulatory compliance (SOX, PCI)
Transactions: Complex, interdependent

Why Oracle:
✅ Enterprise proven
✅ Military-grade security
✅ Extreme scale capacity
✅ Regulatory compliance
✅ Support (24/7 available)

Cost: $5,000-15,000+/month
```

## SQL Server

### What is SQL Server?

Microsoft enterprise database. Windows integration, analytics tools.

```
Best for:
✅ Microsoft Stack (Azure, .NET, Active Directory)
✅ Business Intelligence (SSRS, SSAS)
✅ Windows-integrated security
✅ Enterprise

NOT ideal for:
❌ Non-Microsoft shops
❌ Open-source culture
```

### SQL Server Features

```
Integration:
├─ Active Directory auth
├─ Windows domain login
├─ Microsoft ecosystem
└─ .NET native support

Analytics:
├─ SSRS (reporting)
├─ SSAS (analysis services)
├─ PowerBI integration
└─ BI tools

Performance:
├─ Column store indexes
├─ In-memory OLTP
├─ Parallel processing
└─ Intelligent optimization
```

### SQL Server Licensing

```
Per-core pricing (AWS RDS):
db.r5.large: $3.06/hour
= ~$2,200/month

License costs vary:
├─ Standard: ~$3,500/month
├─ Enterprise: ~$10,000+/month
└─ Developer: Free (non-production)

Total: $5,000-12,000+/month
```

## Engine Decision Tree

```
START: Which database engine?
   ↓
Is it MySQL/MariaDB or PostgreSQL?
   ├─ YES → Complex queries? JSON?
   │        ├─ YES → PostgreSQL
   │        └─ NO → MySQL or MariaDB
   │
   └─ NO → Need enterprise?
           ├─ YES → Oracle or SQL Server?
           │        ├─ Microsoft shop? → SQL Server
           │        └─ NO → Oracle
           │
           └─ NO → Error: Use DynamoDB for NoSQL
```

## Performance Comparison

```
Queries per second (single instance):
├─ MySQL: ~30K-50K
├─ PostgreSQL: ~20K-40K
├─ MariaDB: ~35K-55K
├─ Oracle: ~50K-100K
└─ SQL Server: ~40K-80K

(Varies by: Query type, schema, hardware)

Read Replicas multiply throughput:
└─ 3 replicas: 3x read capacity
└─ 5 replicas: 5x read capacity
```

## Pricing Quick Reference

```
Monthly costs (AWS RDS, db.r5.large):
├─ MySQL: ~$250/month
├─ PostgreSQL: ~$250/month
├─ MariaDB: ~$250/month
├─ Oracle: ~$6,000/month (includes license)
└─ SQL Server: ~$5,000/month (includes license)

Most cost-effective:
1. PostgreSQL (advanced, free)
2. MySQL (fast, free)
3. MariaDB (MySQL alternative)
```

## Engine Selection Criteria

```
Choose PostgreSQL if:
├─ Need JSON/document support
├─ Complex queries/analytics
├─ Full-text search
├─ Advanced features
└─ Open source

Choose MySQL/MariaDB if:
├─ High throughput needed
├─ Web/mobile app
├─ Simple queries
├─ Existing MySQL expertise
└─ Cost-sensitive

Choose Oracle if:
├─ Enterprise mission-critical
├─ Terabyte+ scale
├─ Regulatory compliance
├─ Already using Oracle
└─ Budget available

Choose SQL Server if:
├─ Microsoft Stack (.NET, Azure)
├─ Active Directory integration
├─ Business Intelligence tools
├─ Windows domain
└─ Existing SQL Server knowledge
```

## Common Mistakes

### ✗ Mistake 1: Wrong Engine for Use Case

```
Wrong: Use PostgreSQL for simple blog
Cost: Overkill, slower for simple queries

Right: Use MySQL for blog
Cost: Fast, efficient, cheap
```

### ✗ Mistake 2: Not Using Read Replicas

```
Wrong:
├─ Single database instance
├─ Database maxes out at 50K queries/sec
└─ Can't scale reads

Right:
├─ Primary database (writes)
├─ 3 read replicas
└─ Reads: 150K+ queries/sec
```

### ✗ Mistake 3: Enterprise Database for Small Project

```
Wrong: Use Oracle for 10GB database
Cost: $6,000/month
Usage: 1% of capacity

Right: Use PostgreSQL/MySQL
Cost: $250/month
Usage: 100% of capacity
```

## Backup Considerations

```
All engines support:
├─ Automated daily snapshots
├─ Point-in-time restore (35 days)
├─ Backup to S3
└─ Multi-region backup

Typical backup size:
└─ 10% of database size = free storage
└─ Retention 7 days = ~$1-3/month
```

## Best Practices

✅ Choose engine based on queries, not licensing
✅ PostgreSQL/MySQL for most applications
✅ Oracle/SQL Server for enterprise only
✅ Use read replicas for scale
✅ Enable automated backups
✅ Monitor query performance
✅ Test before migrating
✅ Plan for growth
✅ Archive old data

## Next Steps

→ [Pricing](./pricing.md) - Cost optimization
→ [Use Cases](./use-cases.md) - Real-world scenarios
→ [Creating First Database](./creating-first-database.md) - Setup guide