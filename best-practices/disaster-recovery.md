# Disaster Recovery Plan 🚨

How to prepare for and recover from AWS failures.

## Disaster Recovery Basics

### RTO vs RPO

**RTO (Recovery Time Objective)**
- How long can you be down? (minutes, hours)
- Example: RTO = 1 hour (maximum downtime)

**RPO (Recovery Point Objective)**
- How much data can you lose? (minutes, hours)
- Example: RPO = 15 minutes (maximum data loss)

### Recovery Strategies

| Strategy | RTO | RPO | Cost |
|----------|-----|-----|------|
| **Backup & Restore** | Hours | Hours | $ |
| **Pilot Light** | Minutes | Minutes | $$ |
| **Warm Standby** | Seconds | Seconds | $$$ |
| **Hot-Hot** | None | None | $$$$ |

## Strategy 1: Backup & Restore (Cheapest)

### What It Means
```
Primary Region (Production)
    ↓ (backup)
Backup Storage (S3 in different region)
    ↓ (on disaster)
Restored in Secondary Region (after hours)
```

### Setup
```
1. Automated backups to different region
2. RDS snapshots copied daily
3. S3 cross-region replication
4. Document restore procedures
5. Test monthly
```

### RTO/RPO
- RTO: 4-24 hours
- RPO: 1-24 hours
- Cost: Very low (~$50/month)

### When to Use
- Non-critical applications
- Can afford hours of downtime
- Low budget

## Strategy 2: Pilot Light

### What It Means
```
Primary Region (Production)
    ↓ (continuous sync)
Secondary Region (Small standby instance)
    ↓ (on disaster)
Scale up secondary (takes minutes)
```

### Setup
```
1. Replica database in secondary region
2. Small standby EC2 instances
3. Lambda replicated (automatic)
4. Data synchronized continuously
5. On disaster: Scale up standby
```

### RTO/RPO
- RTO: 10-15 minutes (scale time)
- RPO: Minutes (continuous sync)
- Cost: Medium (~$200/month for small standby)

### When to Use
- Important applications
- Can afford 10-15 minute downtime
- Medium budget

## Strategy 3: Warm Standby

### What It Means
```
Primary Region (Production - full size)
    ↓ (continuous sync)
Secondary Region (Half-size standby)
    ↓ (on disaster)
Ready to serve traffic (seconds)
```

### Setup
```
1. Full database replica in secondary region
2. Half-size EC2 fleet in secondary
3. Elastic Load Balancer can route to secondary
4. Auto Scaling ready to handle full load
5. DNS can switch instantly
```

### RTO/RPO
- RTO: Seconds (just DNS switch)
- RPO: Seconds (continuous sync)
- Cost: High (~$500/month for half-size standby)

### When to Use
- Critical applications
- Cannot afford significant downtime
- High budget

### Example Setup
```
Route 53 → Primary ALB (90% traffic)
       ↘ Secondary ALB (10% traffic - warm)

On disaster:
Route 53 → Secondary ALB (100% traffic)
```

## Strategy 4: Hot-Hot (Most Expensive)

### What It Means
```
Region A (Full size, active)  ←→ Region B (Full size, active)
    ↓                             ↓
Both serving traffic simultaneously
```

### Setup
```
1. Both regions fully active
2. Database multi-region writes
3. Both ALBs receiving traffic
4. Data synchronized in real-time
5. Instant failover (automatic)
```

### RTO/RPO
- RTO: Zero (no failover needed)
- RPO: Near zero (real-time sync)
- Cost: Very high (~$1000+/month for full duplication)

### When to Use
- Mission-critical applications
- Financial systems, emergency services
- Cannot afford any downtime
- Unlimited budget

## Implementing Disaster Recovery

### Step 1: Multi-Region Database

**RDS with Read Replica**
```
Primary RDS (us-east-1)
    ↓ continuous replication
Read Replica (us-west-2)
    ↓ on disaster
Promote to primary
```

**Setup:**
```
RDS Instance → Create Read Replica
Destination region: Different region
Multi-AZ: Enable
Backup retention: 30 days
```

### Step 2: Multi-Region Application

**Auto Scaling Groups**
```
Primary ASG (us-east-1) - production
    ↓ synchronized
Secondary ASG (us-west-2) - standby
    ↓ on disaster
Scale secondary to match primary load
```

**Setup:**
```
Create ASG in secondary region
Same configuration as primary
Min: 0 or 1
Max: Equal to primary
```

### Step 3: Route 53 Failover

**Automatic DNS Failover**
```
Route 53 Hosted Zone
├─ Primary: us-east-1 ALB (primary)
└─ Secondary: us-west-2 ALB (failover)

Health check:
- Check primary every 10 seconds
- If unhealthy for 30 seconds
- Automatically switch to secondary
```

**Setup:**
```
Route 53 → Hosted Zone → Records
Record: example.com
Type: Failover routing
Primary: us-east-1
Secondary: us-west-2
Health check: Enable

Health Check Settings:
- Check HTTP /health endpoint
- Failure threshold: 3 consecutive failures
```

### Step 4: Data Synchronization

**S3 Cross-Region Replication**
```
S3 Bucket (us-east-1)
    ↓ continuous replication
S3 Bucket (us-west-2)
    ↓ automatic
Identical buckets in both regions
```

**Setup:**
```
S3 Bucket → Replication Rules
Destination: Bucket in different region
Status: Enable
Replicate existing objects: Yes
```

**DynamoDB Multi-Region**
```
DynamoDB Table (us-east-1)
    ↓ global tables
DynamoDB Table (us-west-2)
    ↓ real-time sync
```

**Setup:**
```
DynamoDB Table → Global Tables
Replicate to: us-west-2
Billing: Pay for writes in both regions
```

## Disaster Recovery Testing

### Monthly DR Drill

**Scenario: Primary region down**

```
Step 1: Notify team
"Testing DR - this is a drill"

Step 2: Check secondary region
"Health of secondary region?"

Step 3: Perform DNS failover
Route 53 → Manually test failover

Step 4: Verify service works
"Can customers access service?"

Step 5: Check data integrity
"Is recent data present?"

Step 6: Document results
"How long did failover take?"

Step 7: Failback to primary
Switch traffic back to primary

Step 8: Lessons learned
"What can we improve?"
```

### Document Results
```
Date: 2024-01-15
Region Failed: us-east-1
Failover Time: 2 minutes
Data Loss: 0 (RTO met)
Issues Found:
- DNS took 90 seconds to propagate
- Some connections timed out
Action Items:
- Reduce TTL from 300s to 60s
- Update connection timeout settings
```

## Disaster Recovery Checklist

🔴 **CRITICAL**
- ✅ Backup strategy implemented
- ✅ RTO/RPO defined
- ✅ Cross-region replication enabled
- ✅ Route 53 failover configured

🟠 **HIGH**
- ✅ Regular DR tests (monthly)
- ✅ Secondary region prepared
- ✅ Database replicated
- ✅ DNS tested

🟡 **IMPORTANT**
- ✅ Documentation updated
- ✅ Team trained on procedures
- ✅ Failback procedure documented
- ✅ Lessons learned documented

## Common DR Issues

**DNS Propagation Delays**
```
Problem: Failover takes 10 minutes due to DNS
Solution: Reduce TTL from 300s to 60s
```

**Data Replication Lag**
```
Problem: Secondary region 1 hour behind
Solution: Use multi-region database
```

**Insufficient Capacity**
```
Problem: Secondary region out of capacity
Solution: Pre-allocate capacity or use different region
```

## Cost Optimization

```
Strategy: Pilot Light
Primary: $500/month
Standby: $50/month
Total: $550/month

Strategy: Warm Standby
Primary: $500/month
Standby: $250/month (50% size)
Total: $750/month

Choice: Pilot Light saves $200/month
But takes 15 minutes to failover instead of seconds
```

## 📖 Related Resources

- [Backup Strategy](backup-strategy.md)
- [Route 53 Documentation](../tier-2-common/route-53/README.md)
- [RDS Documentation](../tier-1-foundational/rds/README.md)
- [EC2 Auto Scaling](../tier-2-common/auto-scaling/README.md)