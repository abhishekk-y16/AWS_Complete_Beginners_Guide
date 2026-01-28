# What is S3 Glacier? ❄️

AWS's long-term cold storage service for data that's rarely accessed but must be retained for compliance.

## Core Concept

**S3 Glacier** provides ultra-low-cost storage for data you don't access frequently. Trade immediate access for massive savings.

```
S3 Standard:
├─ Cost: $0.023/GB/month
├─ Retrieval: Instant
├─ Use case: Frequently accessed data
└─ 1TB/month cost: $23

S3 Glacier:
├─ Cost: $0.004/GB/month (5x cheaper!)
├─ Retrieval: 1-5 minutes to hours
├─ Use case: Compliance, backups, archives
└─ 1TB/month cost: $4

Savings: $19/month per TB (82% cheaper)
```

## Glacier Classes

### Glacier Instant Retrieval

```
Retrieval time: 1 millisecond
Cost: $0.003/GB/month
Minimum retention: 90 days
Retrieval cost: $0.03/GB

Use cases:
├─ Quarterly access patterns
├─ Backup archives (accessed occasionally)
├─ Compliance archives (legal holds)
└─ Disaster recovery snapshots

Example:
├─ Store 100GB of quarterly backups
├─ Cost: 100 × $0.003 = $0.30/month
├─ Retrieve 10GB: 10 × $0.03 = $0.30
└─ Total cost: $0.60 (vs $2.30 in S3 Standard)
```

### Glacier Flexible Retrieval

```
Retrieval options:
├─ Expedited: 1-5 minutes ($0.03/GB)
├─ Standard: 3-5 hours ($0.01/GB)
└─ Bulk: 5-12 hours (free, best savings!)

Cost: $0.0036/GB/month
Minimum retention: 90 days

Example: Backup archive restoration
├─ Store 500GB annual backups
├─ Cost: 500 × $0.0036 = $1.80/month
├─ Retrieve 50GB via bulk: 50 × $0 = $0
└─ Total: $1.80/month (vs $11.50 in S3)
```

### Deep Archive

```
Retrieval options:
├─ Standard: 12 hours ($0.02/GB)
└─ Bulk: 48 hours (free!)

Cost: $0.00099/GB/month (99% savings!)
Minimum retention: 180 days

Use cases:
├─ 7-year compliance archives (HIPAA, SOX)
├─ Long-term backup archives
├─ Historical data warehouses
└─ Rarely accessed research data

Example: 7-year tax document storage
├─ Store 2TB documents per year × 7 years = 14TB
├─ Cost: 14,000 × $0.00099 = $13.86/month
├─ Annual cost: $166 (vs $3,220 in S3 Standard!)
└─ Savings: $3,054/year
```

## Real-World Use Cases

### Compliance Archive

```
Scenario: E-commerce company retains 7 years of data

Data volume:
├─ 2023: 500GB
├─ 2022: 450GB
├─ 2021: 400GB
├─ 2020-2017: 300GB each (1.2TB)
└─ Total: 3.05TB

Storage strategy:
├─ 2023 data: S3 Standard (might be audited)
│  └─ Cost: 500 × $0.023 = $11.50/month
├─ 2022-2021: Glacier Instant (faster if needed)
│  └─ Cost: 850 × $0.003 = $2.55/month
├─ 2020-2017: Deep Archive (rarely accessed)
│  └─ Cost: 1,200 × $0.00099 = $1.19/month
└─ Total: $15.24/month

If all in S3 Standard:
├─ Cost: 3,050 × $0.023 = $70.15/month
├─ Annual: $841.80

Actual cost: $15.24 × 12 = $182.88
Savings: $659/year (78% savings!)
```

### Disaster Recovery

```
Backup strategy:

Daily backups:
├─ Store 30 days: S3 Standard
├─ Cost: 30 × 100GB × $0.023 = $69/month
└─ Use case: Quick recovery

Monthly archives:
├─ Store 12 months: Glacier Instant
├─ Cost: 12 × 100GB × $0.003 = $3.60/month
└─ Use case: Monthly-level restores

Annual archives:
├─ Store 10 years: Deep Archive
├─ Cost: 10 × 100GB × $0.00099 = $9.90/month
└─ Use case: 7-year legal requirement + extra

Total: $69 + $3.60 + $9.90 = $82.50/month
If all Standard: 4,300GB × $0.023 = $98.90/month
Savings: $16.40/month = $196.80/year
```

## Retrieval Methods

### Expedited Retrieval

```
Retrieval time: 1-5 minutes
Cost: $0.03/GB (Flexible) or $0.015/GB (Deep)

Use case: Urgent data recovery
Example: Database corruption discovered
├─ Affected data: 50GB
├─ Cost: 50 × $0.03 = $1.50
├─ Time: Get data back in 3 minutes
└─ Business impact: Minimal downtime

When to use: Critical situations where time > cost
```

### Standard Retrieval

```
Retrieval time: 3-5 hours
Cost: $0.01/GB (Flexible) or free (Deep)

Use case: Normal operations
Example: Restore monthly backup
├─ Data size: 100GB
├─ Cost: 100 × $0.01 = $1.00
├─ Time: Get in 4 hours
└─ Business impact: Planned recovery

When to use: Regular, non-urgent retrieval
```

### Bulk Retrieval

```
Retrieval time: 5-12 hours (Flexible) or 48 hours (Deep)
Cost: Free!

Use case: Maximum savings
Example: Annual compliance archive restore
├─ Data size: 1TB (1,000GB)
├─ Cost: 1,000 × $0 = $0
├─ Time: 48 hours for Deep Archive
└─ Business impact: Planned, can wait

When to use: Non-urgent restores, cost sensitive
```

## Lifecycle Policies

### Automatic Tiering

```yaml
Version: '2012-10-17'
Statement:
  - Effect: Allow
    Action:
      - s3:GetObject
      - s3:ListBucket
    Principal: "*"
    Resource: "arn:aws:s3:::my-bucket/*"
    Condition:
      StringEquals:
        s3:x-amz-storage-class: GLACIER
```

```
Rules:
├─ Day 0: Create file (S3 Standard)
├─ Day 30: Move to Glacier Instant
│  └─ Saves $20/GB/year
├─ Day 90: Move to Deep Archive
│  └─ Saves $23/GB/year
└─ Year 7: Delete (compliance met)

Example: 100TB of documents
├─ S3 Standard (30 days): 3TB × $0.023 = $69
├─ Glacier Instant (60 days): 6TB × $0.003 = $18
├─ Deep Archive (next 6+ years): 91TB × $0.00099 = $90
└─ Total annual: ~$360 (vs $2,300 if all Standard)
```

## Best Practices

✅ Use Glacier for backups (low retrieval rate)
✅ Use Deep Archive for compliance archives
✅ Set lifecycle policies for automatic tiering
✅ Test retrieval procedures regularly
✅ Document retention requirements
✅ Monitor actual vs. planned retrieval costs
✅ Use bulk retrieval for cost savings
✅ Combine with S3 versioning for safety
✅ Tag archives for compliance tracking
✅ Calculate multi-year total cost of ownership

## Common Mistakes

✗ Archiving data without retrieval testing (surprise failures)
✗ Not using lifecycle policies (manual management burden)
✗ Using Instant when Deep would suffice (cost waste)
✗ Forgetting minimum retention days (unexpected costs)
✗ Not planning for retrieval costs (budget surprises)
✗ No retention policy (compliance violations)
✗ Archiving without proper tagging (can't find data)
✗ Bulk retrieval for urgent data (too slow)

## Glacier vs. Other Storage

```
Comparison:

S3 Standard:
├─ Cost: $0.023/GB/month
├─ Access: Instant
└─ Use: Frequently accessed

Glacier Instant:
├─ Cost: $0.003/GB/month (87% cheaper)
├─ Access: 1ms
└─ Use: Occasional access

Deep Archive:
├─ Cost: $0.00099/GB/month (96% cheaper!)
├─ Access: 48 hours
└─ Use: Rare access

EBS snapshots:
├─ Cost: $0.05/GB/month
├─ Access: Instant
└─ Use: EC2 volumes only
```

## Next Steps

→ [Lifecycle Policies](./lifecycle.md) - Automation strategies
→ [Cost Optimization](./cost.md) - Maximize savings
→ [Compliance Archives](./compliance.md) - Retention rules