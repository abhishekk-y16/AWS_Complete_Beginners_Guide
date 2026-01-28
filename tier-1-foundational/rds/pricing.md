# RDS Pricing 💰

Comprehensive breakdown of AWS RDS costs with real-world examples.

## Pricing Components

### Instance Cost (hourly)

```
You pay for the database instance itself:

Most common instance types:

db.t3.micro (burstable)
├─ vCPU: 2
├─ Memory: 1 GB
├─ Price: $0.0166/hour (~$12/month)
└─ Perfect for: Dev, testing, small apps

db.t3.small (burstable)
├─ vCPU: 2
├─ Memory: 2 GB
├─ Price: $0.0333/hour (~$24/month)
└─ Perfect for: Small production apps

db.t3.medium (burstable)
├─ vCPU: 2
├─ Memory: 4 GB
├─ Price: $0.0664/hour (~$48/month)
└─ Perfect for: Medium production

db.m5.large (general purpose)
├─ vCPU: 2
├─ Memory: 8 GB
├─ Price: $0.192/hour (~$140/month)
└─ Perfect for: High traffic production

db.r5.large (memory optimized)
├─ vCPU: 2
├─ Memory: 16 GB
├─ Price: $0.276/hour (~$200/month)
└─ Perfect for: In-memory intensive

Free tier (12 months):
├─ db.t3.micro: $0/hour
├─ 750 hours/month included
└─ Requires: AWS free tier account
```

### Storage Cost (per GB-month)

```
You pay for allocated storage:

General Purpose SSD (gp3)
├─ Cost: $0.115/GB/month
├─ 20GB database costs: ~$2.30/month
├─ 100GB database costs: ~$11.50/month
└─ Provisioned IOPS extra: $0.10 per IOPS/month

Provisioned IOPS (io1)
├─ Cost: $0.20/GB/month (base)
├─ Plus: $0.065 per provisioned IOPS/month
├─ Example: 100GB + 1000 IOPS = $20 + $65 = $85/month
└─ For: High-I/O intensive workloads

Magnetic (old, not recommended)
├─ Cost: $0.10/GB/month
└─ Rarely used (gp3 better value)

Storage autoscaling:
├─ Enable: Automatic growth
├─ Cost: Same rate per additional GB
├─ Max threshold: Set max size limit
└─ Good for: Unpredictable growth
```

### Data Transfer Cost

```
Outbound data (from RDS to internet):

First 1GB/month: FREE
Next 9,999 GB/month: $0.02/GB
10,000+ GB/month: $0.015/GB

Examples:
├─ 100GB: 1 free + 99 × $0.02 = $1.98
├─ 1,000GB: 1 free + 999 × $0.02 = $19.98
└─ 10,000GB: 1 free + 9,999 × $0.015 = $149.98

Inbound data: FREE
Data within same region: FREE
Data across regions: Charged as outbound
```

### Backup Storage

```
Automated backups:
├─ Retention: 1-35 days
├─ Storage: Usually 100% of database size
├─ Cost: $0.095/GB/month (first backup free)
└─ Automatic recovery point-in-time

Manual snapshots:
├─ Retained indefinitely
├─ Cost: $0.095/GB/month
└─ Not auto-deleted unless you delete

Example:
├─ Database: 50GB
├─ Backup: 50GB
├─ Monthly cost: 50GB × $0.095 = $4.75
└─ For retention of 7 days
```

## Real-World Cost Examples

### Example 1: Small Startup App

```
Scenario:
├─ Users: 1,000
├─ Database size: 10GB
├─ Traffic: 100 requests/min
└─ Redundancy: None (development)

Setup:
├─ Instance: db.t3.micro
├─ Storage: 10GB gp3
├─ Backups: 7-day retention
├─ Region: us-east-1
└─ Multi-AZ: No

Cost breakdown:

1. Instance
   ├─ db.t3.micro: $0.0166/hour
   ├─ 730 hours/month: 730 × $0.0166 = $12.12
   └─ Free tier: $0 (if eligible)

2. Storage
   ├─ 10GB gp3: 10 × $0.115 = $1.15
   └─ Subtotal: $1.15

3. Backups
   ├─ 10GB backup: 10 × $0.095 = $0.95
   └─ Subtotal: $0.95

Total monthly: $12.12 + $1.15 + $0.95 = $14.22
Total annual: ~$170 (or $0 with free tier)

Cost analysis:
├─ Per user per month: $14.22 / 1,000 = $0.014
├─ Very cheap!
└─ Excellent for learning/development
```

### Example 2: Growing SaaS Application

```
Scenario:
├─ Users: 50,000
├─ Database size: 500GB
├─ Traffic: 50,000 requests/min
├─ Redundancy: Multi-AZ (production)
└─ Read replicas: 2

Setup:
├─ Primary instance: db.m5.large
├─ Read replicas: 2 × db.m5.large
├─ Storage: 500GB gp3 (all instances)
├─ Backups: 30-day retention
└─ Multi-AZ: Yes (standby replica)

Cost breakdown:

1. Primary instance
   ├─ db.m5.large: $0.192/hour
   ├─ 730 hours/month: 730 × $0.192 = $140.16
   └─ Subtotal: $140.16

2. Standby (Multi-AZ)
   ├─ db.m5.large: $0.192/hour (included in Multi-AZ)
   └─ No additional cost!

3. Read replicas
   ├─ 2 × db.m5.large: 2 × 730 × $0.192 = $280.32
   └─ Subtotal: $280.32

4. Storage (all 3 instances)
   ├─ 3 × 500GB × $0.115 = $172.50
   └─ Subtotal: $172.50

5. Backups
   ├─ 500GB × 30 days × $0.095 / 30 = $47.50
   ├─ (30-day retention cost)
   └─ Subtotal: $47.50

6. Data transfer (outbound)
   ├─ 500GB/month × $0.02 = $10
   └─ Subtotal: $10

Total monthly: $140.16 + $0 + $280.32 + $172.50 + $47.50 + $10 = $650.48
Total annual: ~$7,806

Cost per user: $650.48 / 50,000 = $0.013/month
├─ Excellent scalability!
└─ Still very affordable
```

### Example 3: High-Traffic E-Commerce

```
Scenario:
├─ Users: 500,000
├─ Database size: 2TB
├─ Traffic: 100,000 requests/sec (peak)
├─ Redundancy: Multi-AZ + cross-region
└─ Read replicas: 5 (distributed)

Setup:
├─ Primary: db.r5.2xlarge (memory-optimized)
├─ Standby: db.r5.2xlarge (Multi-AZ)
├─ Read replicas: 5 × db.r5.2xlarge
├─ Storage: 2TB gp3, provisioned IOPS
├─ Backups: Continuous (backup retention)
└─ Plus: Amazon Aurora (better for scale)

Cost breakdown:

1. Primary instance
   ├─ db.r5.2xlarge: $1.008/hour
   ├─ 730 hours/month: $736 (approx)
   └─ Subtotal: $736

2. Standby (Multi-AZ)
   ├─ Included in Multi-AZ cost
   └─ No additional cost!

3. Read replicas
   ├─ 5 × $736 = $3,680
   └─ Subtotal: $3,680

4. Storage
   ├─ 2TB = 2,000GB
   ├─ Base cost: 2,000 × $0.115 = $230
   ├─ Provisioned IOPS (5,000): 5,000 × $0.10 = $500
   ├─ 3 instances total cost: 3 × $730 = $2,190
   └─ Subtotal: $2,190

5. Backups
   ├─ 2TB backup size: 2,000GB
   ├─ Cost: 2,000 × $0.095 = $190
   └─ Subtotal: $190

6. Data transfer
   ├─ 10TB/month (high traffic): 10,000GB
   ├─ First 1GB free: 9,999 × $0.015 = $149.985
   └─ Subtotal: $150

Total monthly: $736 + $3,680 + $2,190 + $190 + $150 = $6,946
Total annual: ~$83,352

Cost per user: $6,946 / 500,000 = $0.014/month
├─ Still very affordable at scale!
└─ Benefits: High availability, performance

Alternative: Amazon Aurora
├─ More cost-efficient at scale
├─ Auto-scaling for reads
├─ Could reduce cost 30-40%
└─ Worth evaluating
```

## Cost Optimization Strategies

### 1. Use Burstable Instances

```
db.t3 instances are cheaper:

Compare (monthly, 730 hours):
├─ db.t3.small: 730 × $0.0333 = $24.31
├─ db.m5.small: 730 × $0.102 = $74.46
└─ Savings: $50/month (68% cheaper!)

When to use:
├─ Average load is low
├─ Occasional traffic spikes acceptable
├─ Dev/test environments
└─ Small production apps

When NOT to use:
├─ Sustained high load
├─ Cannot tolerate throttling
└─ Consistent CPU demand > 20%
```

### 2. Right-Size Your Database

```
Problem: Over-provisioned storage

Example:
├─ Allocated: 500GB
├─ Used: 50GB (only 10%!)
├─ Cost: 500 × $0.115 = $57.50/month
├─ Wasted: ~$52/month
└─ Annual waste: $624

Solution:
1. Analyze actual usage
   └─ RDS console → Storage metrics

2. Reduce allocated storage
   ├─ But maintain: 20% buffer
   └─ Allocated: 60GB (50GB used + buffer)

3. Enable autoscaling
   └─ Growth handled automatically

Savings:
├─ New cost: 60 × $0.115 = $6.90/month
├─ Savings: $50.60/month = $607/year
└─ Same performance!
```

### 3. Use RDS Proxying

```
Amazon RDS Proxy:
├─ Connection pooling service
├─ Reduces Lambda cold starts
├─ Cost: $0.015/hour (~$11/month)
├─ Reduces instance connections needed
└─ Better for: Serverless + Lambda

ROI:
├─ If reduces instance size: db.m5.large → db.t3.small
├─ Monthly savings: $140 → $24 = $116/month
├─ Proxy cost: $11/month
└─ Net savings: $105/month = $1,260/year
```

### 4. Use Read Replicas Strategically

```
When to use read replicas:
✅ Read-heavy workload (80% reads, 20% writes)
✅ Analytics queries don't impact primary
✅ Geographic distribution needed
✅ Can accept some replication lag (typically <100ms)

When NOT to use:
❌ Write-heavy workload
❌ Need real-time consistency
❌ Budget is tight (doubles cost!)
❌ Can use database caching instead (cheaper)

Cost comparison:
No replicas:
├─ Primary: db.m5.large = $140/month
└─ Total: $140/month

With 2 read replicas:
├─ Primary: $140
├─ Replicas: 2 × $140 = $280
└─ Total: $420/month (+200%)

Better alternative: ElastiCache
├─ Redis cache: $0.017/hour = $12/month
├─ Handles most read traffic
├─ Primary cost stays: $140
└─ Total: $152/month (8% increase vs 200%!)
```

### 5. Scheduled Backup Cleanup

```
Problem: Manual snapshots accumulate

Example:
├─ Create snapshot for backup: 100GB
├─ Cost: 100 × $0.095 = $9.50/month
├─ Forgot about it (1 year): $114
└─ Never used it!

Solution:
1. Regular snapshot cleanup
   └─ Delete old snapshots monthly

2. Lifecycle policies
   └─ Auto-delete after X days

3. Only keep what you need
   ├─ Recent backup: 7 days
   ├─ Weekly: 4 weeks
   ├─ Monthly: 12 months
   └─ Yearly: 7 years (if required)
```

## Free Tier Limits

```
AWS RDS Free Tier (12 months):

1. Compute
   ├─ db.t3.micro: Free
   ├─ 750 hours/month (24-25 days)
   └─ Exceeding: $0.0166/hour

2. Storage
   ├─ 20GB SSD: Free
   └─ Exceeding: $0.115/GB/month

3. Backups
   ├─ 20GB automated backups: Free
   └─ Exceeding: $0.095/GB/month

4. Data transfer
   ├─ Outbound: 100GB/month free
   └─ Exceeding: $0.02/GB

Example within free tier:
├─ db.t3.micro
├─ 20GB storage
├─ Light usage
└─ Total cost: $0 (completely free!)
```

## Cost Monitoring

### CloudWatch Metrics

```
Monitor these metrics:
├─ DatabaseConnections: Number of active connections
├─ CPUUtilization: % CPU usage
├─ StorageSpace: Current data size
├─ FreeStorageSpace: Available space
└─ NetworkReceiveThroughput: Data per second

Set alarms:
├─ CPU > 80%: Scale up instance
├─ Storage > 80%: Increase allocated space
├─ Connections > 100: Check for leaks
└─ Network > 1GB/sec: Check traffic
```

### AWS Cost Explorer

```
Check costs regularly:

1. Go to: Billing → Cost Explorer
2. Filter by: Service = RDS
3. Group by: Instance type
4. View: Daily, monthly, yearly trends
5. Compare: Month-over-month changes
6. Set: Budget alerts ($50/month threshold)
```

## Best Practices

✅ Start with smallest instance (db.t3.micro)
✅ Monitor storage and grow only when needed
✅ Use autoscaling for storage
✅ Delete unused snapshots monthly
✅ Multi-AZ only for production
✅ Read replicas only when read-heavy
✅ Use ElastiCache for caching instead of replicas
✅ Regular cost reviews
✅ Set up billing alerts
✅ Right-size instance based on actual metrics

## Next Steps

→ [What is RDS](./what-is-rds.md) - Full overview
→ [Use Cases](./use-cases.md) - When to use RDS
→ [Creating First Database](./creating-first-database.md) - Hands-on guide