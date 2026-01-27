# RDS - Relational Database Service

Managed SQL databases. AWS handles backups, patches, scaling - you just use it.

## 📚 Learning Path

1. **[What is RDS?](what-is-rds.md)** - Overview and benefits
2. **[Database Engines](database-engines.md)** - MySQL vs PostgreSQL vs Aurora
3. **[Pricing](pricing.md)** - Cost estimation
4. **[Use Cases](use-cases.md)** - Real-world applications
5. **[Create Database](creating-first-database.md)** - Hands-on guide

## 🎯 Quick Summary

RDS = Database with zero management overhead. AWS handles backups, patches, replication, scaling.

| Aspect | Value |
|--------|-------|
| **Engines** | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora |
| **Cost** | $12-200+/month depending on size |
| **Backups** | Automatic, 35-day retention |
| **High Availability** | Multi-AZ with automatic failover (99.95% SLA) |
| **Scaling** | Vertical (bigger instance) or read replicas |

## 🔄 RDS vs Traditional Database

### Traditional (EC2 + Manual Database)
**You Do**:
- Install database software
- Apply security patches
- Create backups
- Monitor performance
- Handle failover
- Manage storage

**Time**: 40% of your effort

### RDS
**AWS Does**:
- Installation ✓
- Patches ✓
- Backups ✓
- Monitoring ✓
- Failover ✓
- Storage ✓

**You Do**: Just use the database

## 📊 Supported Engines

| Engine | Best For | Cost | Learning Curve |
|--------|----------|------|-----------------|
| **MySQL** | Web apps | Cheapest | Easy |
| **PostgreSQL** | Advanced SQL, JSON | Medium | Medium |
| **MariaDB** | MySQL replacement | Cheapest | Easy |
| **Aurora** | Speed + scale | Premium | Medium |
| **Oracle** | Enterprise | Expensive | Hard |
| **SQL Server** | Windows/.NET | Expensive | Hard |

## 🏗️ Deployment Options

### Single-AZ (Development/Test)
```
Single EC2 instance
- Cheapest
- Sufficient for dev
- No redundancy
- Downtime if fails
```

### Multi-AZ (Production Recommended!)
```
Primary + Standby replica (different AZ)
- 99.95% availability SLA
- Automatic failover
- Synchronous replication
- ~50% more expensive
```

### Read Replicas (Scale Reads)
```
Primary + read-only replicas
- Scale read queries
- Can be in different regions
- Can be promoted to primary
- Extra cost
```

## 💡 Real-World Architecture

```
Application Servers
├─ Write to Primary RDS (us-east-1a)
├─ Failover to Standby (us-east-1b) if primary down
└─ Read from Replicas (worldwide)
   ├─ Replica 1 (us-west-1)
   ├─ Replica 2 (eu-west-1)
   └─ Replica 3 (ap-southeast-1)
```

## 💰 Pricing Example: Small Database

```
Instance: db.t3.micro
- $0.017/hour × 730 hours = $12.41/month

Storage: 20 GB
- $20 × $0.115/GB = $2.30/month

Backups: 20 GB
- $20 × $0.095/GB = $1.90/month

Total: ~$17/month

Multi-AZ: +50% = ~$25/month
Reserved 1-year: Save 45% = ~$9/month
```

## 🔐 Security Features

- **Encryption at-rest**: AES-256 (all engines)
- **Encryption in-transit**: SSL/TLS (automatic)
- **Network isolation**: Runs in VPC (private)
- **IAM authentication**: Alternative to passwords
- **Automated patching**: Security updates
- **Audit logging**: CloudTrail integration

## 🚀 Common Scenarios

### Scenario 1: WordPress Blog
```
db.t3.micro, 20 GB
Single-AZ
Cost: ~$17/month
```

### Scenario 2: Production Web App
```
db.m5.large, 100 GB + read replicas
Multi-AZ
Cost: ~$300/month
```

### Scenario 3: Analytics Database
```
db.r5.xlarge, 1 TB + read replicas
Multi-AZ
Cost: ~$800/month
```

## ⚠️ Common Mistakes

1. Single-AZ production (no HA)
2. Too small instance (slow queries)
3. No backups configured (data loss)
4. Outdated patches (security risk)
5. No monitoring (problems unnoticed)

## ✅ Best Practices

- Use Multi-AZ for production
- Enable automated backups (35 days)
- Use read replicas for scale
- Monitor with CloudWatch
- Apply patches in maintenance window
- Use IAM authentication
- Enable encryption at-rest
- Regular restore tests

## 🔗 RDS vs Aurora

| Feature | RDS (MySQL/PostgreSQL) | Aurora |
|---------|--------|--------|
| Speed | Standard | 5-15x faster |
| Cost | Standard | +25-50% |
| Auto-scaling | No | Yes |
| Replication | 6-way | 6-way |
| Failover | Manual | Automatic |

**Recommendation**: Start with RDS, upgrade to Aurora when you need speed.

---
**Start**: [What is RDS?](what-is-rds.md)  
- **MariaDB**: MySQL alternative, drop-in replacement
- **Oracle Database**: Enterprise-grade with most features
- **SQL Server**: Microsoft's database, Windows/.NET integration

## 💡 AWS Managed Benefits

**AWS Automatically Handles:**
- ✅ Daily automated backups
- ✅ Security patches and OS updates
- ✅ Database engine version upgrades
- ✅ High availability with Multi-AZ failover
- ✅ Read replicas for scaling reads
- ✅ Hardware provisioning and maintenance

**You Handle:**
- ✓ Writing SQL queries
- ✓ Database schema design
- ✓ Who can access (IAM/Security Groups)
- ✓ Application code

## 🚀 Quick Start

1. Go to RDS Console → Create Database
2. Choose engine (MySQL recommended for beginners)
3. Choose size: **db.t3.micro** (free tier eligible)
4. Set master username and password (strong password!)
5. Configure backup settings
6. Click "Create Database"
7. Wait 5 minutes for creation
8. Connect using SQL client (MySQL Workbench, pgAdmin, etc.)

## 💰 Free Tier Includes

- db.t3.micro or db.t2.micro instance (1 year)
- 20 GB storage
- Automated daily backups
- Multi-AZ for high availability

**Perfect for learning and testing!**

## ⭐ Best Practices

- ✓ Enable automated backups (minimum 7 days)
- ✓ Use Multi-AZ for production (automatic failover)
- ✓ Place in private subnet, not public
- ✓ Use Security Groups to allow only app servers
- ✓ Enable encryption at rest
- ✓ Use read replicas for read-heavy workloads

## 📖 Official Resources

- [RDS Documentation](https://docs.aws.amazon.com/rds/)
- [RDS Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)
- [RDS vs DynamoDB Comparison](../../service-comparisons/rds-vs-dynamodb.md)