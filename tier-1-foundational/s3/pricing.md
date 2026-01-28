# S3 Pricing 💰

Comprehensive breakdown of AWS S3 costs with real-world examples and optimization strategies.

## Storage Cost Breakdown

### Storage Classes Pricing (per GB/month)

```
Standard: $0.023/GB
├─ Tier 1: First 50TB/month
├─ Tier 2: 50-500TB/month → $0.0220/GB
├─ Tier 3: >500TB/month → $0.0210/GB
└─ Use case: Frequently accessed data

Intelligent-Tiering: $0.0125/GB
├─ Frequent access: $0.023/GB
├─ Infrequent access: $0.0125/GB
├─ Auto-moves between tiers
└─ Use case: Unknown access patterns

Standard-IA: $0.0125/GB
├─ Monthly retrieval cost: $0.01/GB
├─ Minimum billable object: 128KB
├─ Minimum retention: 30 days
└─ Use case: Infrequent, but fast access

Glacier Instant: $0.003/GB
├─ Retrieval cost: $0.03/GB
├─ Retrieval time: 1ms
├─ Minimum retention: 90 days
└─ Use case: Quarterly access

Glacier Flexible: $0.0036/GB
├─ Expedited retrieval: $0.03/GB (1-5 min)
├─ Standard retrieval: $0.01/GB (3-5 hrs)
├─ Bulk retrieval: Free (5-12 hrs)
├─ Minimum retention: 90 days
└─ Use case: Occasional archive access

Deep Archive: $0.00099/GB
├─ Standard retrieval: $0.02/GB (12 hrs)
├─ Bulk retrieval: Free (48 hrs)
├─ Minimum retention: 180 days
└─ Use case: 7-year compliance, rare access
```

## Real-World Pricing Examples

### Example 1: Website Media (Hot Storage)

```
Scenario: Photography website, 100K daily users

Data stored:
├─ Images: 500GB (high-res photos)
├─ Thumbnails: 50GB (pre-generated)
├─ Metadata: 5GB (database backup)
└─ Total: 555GB

Storage cost:
├─ 555GB × $0.023/month = $12.76/month

Data access patterns:
├─ Page loads: 100K × 5 images = 500K requests/day
├─ Monthly requests: 500K × 30 = 15M requests
├─ Data transferred OUT: 15M × 200KB avg = 3TB/month

Request costs:
├─ GET requests: 15M × $0.0004 = $6
├─ PUT requests: Negligible (uploads rare)
└─ Total requests: $6/month

Data transfer:
├─ First 1GB/month: Free
├─ Next 9.999TB: 3TB × $0.09/GB = $270
├─ Regional transfer: Free (same region)
└─ Total transfer: $270/month

Total monthly cost: $12.76 + $6 + $270 = $288.76
Annual cost: $3,465

Cost per user: $3,465 / (100K × 365 days) = $0.000095/user/day
Or: ~$2.88/user/year for S3 alone
```

### Example 2: Cold Archive (Compliance)

```
Scenario: Enterprise retains 7 years of audit logs

Data volume:
├─ 2024: 100GB
├─ 2023: 100GB
├─ 2022: 100GB
├─ 2021-2018: 400GB total (100GB each)
└─ Total: 700GB

Storage strategy:

Current year (2024) - Standard:
├─ Size: 100GB
├─ Cost: 100 × $0.023 = $2.30/month

Recent years (2023-2022) - Glacier Instant:
├─ Size: 200GB
├─ Cost: 200 × $0.003 = $0.60/month

Older years (2021-2018) - Deep Archive:
├─ Size: 400GB
├─ Cost: 400 × $0.00099 = $0.40/month

Total storage: $3.30/month = $39.60/year

If all were Standard:
├─ 700 × $0.023 × 12 = $194.40/year

Savings: $194.40 - $39.60 = $154.80/year (80% savings!)

Retrieval assumption (annual audit):
├─ Retrieve 100GB via bulk (Deep Archive): Free
├─ All other retrievals: Free or minimal
└─ Retrieval cost: ~$0/year
```

### Example 3: Data Lake (Mixed Access)

```
Scenario: Data analytics platform

Data tiers:

Hot tier (Current month - queries daily):
├─ Size: 2TB
├─ Storage class: Standard
├─ Cost: 2,000 × $0.023 = $46/month
├─ Query frequency: Daily (expensive if slow)

Warm tier (Last 3 months - weekly queries):
├─ Size: 6TB
├─ Storage class: Intelligent-Tiering
├─ Cost: 6,000 × $0.0125 = $75/month
├─ Query frequency: Weekly (moderate access)

Cold tier (6 months - monthly analytics):
├─ Size: 12TB
├─ Storage class: Glacier Instant
├─ Cost: 12,000 × $0.003 = $36/month
├─ Query frequency: Monthly (infrequent)
├─ Retrieval: 12,000 × $0.03 × 1/month = $360/month (occasional)

Archive (1+ years - compliance):
├─ Size: 50TB
├─ Storage class: Deep Archive
├─ Cost: 50,000 × $0.00099 = $49.50/month
├─ Query frequency: Never (archive)

Total storage cost: $46 + $75 + $36 + $49.50 = $206.50/month
Total retrieval cost: $360/month (occasional)
Total monthly: ~$567/month

If all Standard:
├─ (2 + 6 + 12 + 50)TB × $0.023 = 70 × $23 = $1,610/month

Savings: $1,610 - $567 = $1,043/month (65% savings!)
```

## Request Pricing

```
Operation costs (per 1,000 requests):

GET/HEAD requests:
├─ Standard/Intelligent-Tiering: $0.0004/1K
├─ Standard-IA: $0.001/1K
├─ Glacier/Deep Archive: $0.001/1K
└─ Example: 1M GETs/month = $0.40 (Standard)

PUT/COPY/POST requests:
├─ All storage classes: $0.005/1K
└─ Example: 100K PUTs/month = $0.50

DELETE requests: Free

LIST requests:
├─ Standard/Intelligent-Tiering: $0.005/1K
├─ Standard-IA/Glacier: $0.005/1K
└─ Example: 10K LIST calls/month = $0.05

SELECT requests:
├─ Data scanned: $0.002 per GB
├─ Data returned: $0.0007 per GB
└─ Great for filtering large datasets
```

## Data Transfer Costs

```
OUT of S3 (egress):

First 1GB/month: FREE (always)

Tiered pricing:
├─ 1GB - 10TB/month: $0.09/GB
├─ 10TB - 100TB/month: $0.085/GB
├─ 100TB+/month: $0.08/GB
└─ Savings increase with volume!

CloudFront delivery:
├─ Much cheaper for content delivery
├─ $0.0075 - $0.085/GB (vs $0.09)
├─ Caching reduces actual costs
└─ Recommended for high-traffic sites

Same-region access:
├─ EC2 to S3 (same region): FREE
├─ Much cheaper than cross-region
└─ Design for local access when possible

Cross-region replication:
├─ $0.02/GB per replication
├─ HA setup cost to consider
└─ Budget for ongoing replication
```

## Advanced Pricing Scenarios

### Multi-Region High Availability

```
Setup: App in US, EU, and APAC regions

Data replication strategy:

US region (primary):
├─ Storage: 100GB Standard = $2.30/month
├─ Requests: 10M/month = $4/month
└─ Subtotal: $6.30/month

EU region (replica):
├─ Storage: 100GB Standard = $2.30/month
├─ Replication cost: 100GB × $0.02 = $2/month
├─ Requests: 5M/month = $2/month
└─ Subtotal: $6.30/month

APAC region (replica):
├─ Storage: 100GB Standard = $2.30/month
├─ Replication cost: 100GB × $0.02 = $2/month
├─ Requests: 5M/month = $2/month
└─ Subtotal: $6.30/month

Total monthly: $18.90/month
Total annual: $227/year

Benefits:
├─ 99.99% availability (SLA)
├─ Faster access (regional buckets)
├─ Disaster recovery included
└─ Peace of mind for mission-critical data
```

### Versioning Impact

```
Scenario: 10GB object, 5 versions kept

Cost multiplier:
├─ 1 version: 10GB × $0.023 = $0.23/month
├─ 5 versions: 50GB × $0.023 = $1.15/month
├─ 10 versions: 100GB × $0.023 = $2.30/month
└─ 100 versions: 1TB × $0.023 = $23/month

Cost growth: Exponential with versions!

Cost reduction strategies:
├─ Use lifecycle policies to delete old versions
├─ Transition old versions to Glacier ($0.003/GB)
├─ Set retention limit (keep 5 versions max)
└─ Monitor bucket metrics
```

## Cost Optimization Strategies

### 1. Storage Class Selection

```
Decision tree:

Do you need instant access?
├─ YES → Standard ($0.023/GB)
└─ NO → Continue...

Accessed weekly or more?
├─ YES → Standard-IA ($0.0125/GB) or Intelligent-Tiering
└─ NO → Continue...

Accessed monthly or less?
├─ YES → Glacier Instant ($0.003/GB)
└─ NO → Continue...

Compliance/archive (7+ years)?
├─ YES → Deep Archive ($0.00099/GB)
└─ NO → Re-evaluate

Savings example:
├─ Wrong class: 1TB Standard = $276/year
├─ Right class: 1TB Deep Archive = $12/year
└─ Annual savings: $264
```

### 2. Use Intelligent-Tiering

```
Automatic optimization:

Set it and forget it:
├─ Upload file to Intelligent-Tiering
├─ If accessed daily → Keep in Standard ($0.023/GB)
├─ If accessed <monthly → Move to IA ($0.0125/GB)
├─ If not accessed >90 days → Move to Archive ($0.003/GB)
└─ No manual work needed

Cost benefit:
├─ Unknown pattern: $0.0125/GB (tiering overhead)
├─ Auto-optimizes based on real usage
└─ Avoid paying Standard for rarely-used data
```

### 3. Lifecycle Policies

```
Automatic transitions:

Example policy:

Day 0: Upload to Standard
├─ Metadata: Indexed, searchable
└─ Cost: $0.023/GB

Day 30: Transition to Standard-IA
├─ Reason: Probably not needed immediately
├─ Retrieval cost: $0.01/GB if accessed
└─ Cost: $0.0125/GB (savings begin)

Day 90: Transition to Glacier
├─ Reason: Very unlikely to be accessed
├─ Retrieval cost: $0.03/GB if needed
└─ Cost: $0.003/GB (major savings!)

Day 365: Transition to Deep Archive
├─ Reason: Archive for compliance
├─ Retrieval cost: $0.02/GB
└─ Cost: $0.00099/GB (maximum savings!)

Effect: 1TB file
├─ Day 0-30: 1TB × $0.023 = $0.77
├─ Day 30-90: 1TB × $0.0125 = $2.50
├─ Day 90-365: 1TB × $0.003 = $9.95
├─ Year total: $13.22
└─ Savings vs Standard year-round: $13.22/TB
```

### 4. CloudFront for Distribution

```
Comparison:

Without CloudFront:
├─ 10M downloads/month
├─ 500MB per download = 5TB
├─ Cost: 5TB × $0.09/GB = $450/month
└─ Annual: $5,400

With CloudFront:
├─ CloudFront requests: 10M × $0.0075 = $75
├─ S3 origin requests: 1M (80% cache hit) × $0.0004 = $0.40
├─ Data transfer (20% miss): 1TB × $0.085 = $85
└─ Total: $160.40/month

Annual savings: $5,400 - $1,925 = $3,475/year (64% savings!)
```

## Monitoring and Alerts

```
Key metrics to track:

Storage growth:
├─ Alert if > 20% month-over-month growth
├─ Could indicate misconfig or unnecessary data
└─ Reduce via lifecycle policies

Data egress:
├─ Alert if egress > 50% of storage/month
├─ Indicates high retrieval costs
└─ Consider CloudFront or local caching

Request volume:
├─ Monitor API calls
├─ High DELETE/PUT might indicate automation issues
└─ Batch operations to reduce request count

Unversioned objects:
├─ Monitor old versions stored
├─ Set expiration for versions
└─ Save 10x cost per object
```

## Best Practices

✅ Use Intelligent-Tiering for unknown patterns
✅ Set lifecycle policies to auto-transition
✅ Use Deep Archive for compliance data
✅ Enable versioning only when needed
✅ Monitor bucket metrics monthly
✅ Use CloudFront for frequent downloads
✅ Compress data before uploading
✅ Enable access logging (minimal cost)
✅ Delete test data regularly
✅ Review bucket inventory reports

## Common Cost Mistakes

✗ Using Standard for archival data (9x cost!)
✗ Keeping unlimited versions (100x cost!)
✗ Not using CloudFront (massive overpay on egress)
✗ Transferring between regions unnecessarily ($0.02/GB)
✗ Not setting lifecycle policies (manual management)
✗ Leaving versioning on indefinitely
✗ Not compressing data before uploading
✗ Replicating data that doesn't need HA
✗ Using SELECT on large unfiltered datasets
✗ Not deleting test/temporary data

## Next Steps

→ [Cost Calculator](./calculator.md) - Estimate your costs
→ [Optimization Guide](./optimization.md) - Advanced savings
→ [Billing Alerts](./billing-alerts.md) - Monitor spending