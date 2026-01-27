# AWS Pricing Models 💰

Understanding how AWS charges and how to save money.

## Pay-As-You-Go Philosophy

**Think of it as:** Your electricity bill

```
No upfront costs
No minimum commitments
Pay only for what you use
Stop using = Stop paying

Example:
- Launch EC2 instance
- Run for 100 hours
- Pay for 100 hours
- Stop instance
- $0 charge
```

## Core Pricing Models

### 1. On-Demand (Default)
```
Pay per hour/second
No commitment
Start/stop anytime

When to use:
- Learning/testing
- Short-term workloads
- Unpredictable traffic
- Can't commit

Cost: HIGHEST (100% of list price)

Example:
- EC2 t3.medium: $0.0416/hour
- Run 730 hours (1 month)
- Cost: $30.37/month
```

### 2. Reserved Instances (RI)
```
Commit to 1 or 3 years
Up to 72% discount
Pay upfront/monthly/no-upfront

When to use:
- Steady-state workloads
- Predictable usage
- Production servers 24/7

Discount examples:
- 1 year: 30-40% off
- 3 years: 60-72% off

Example:
- EC2 t3.medium On-Demand: $0.0416/hour
- 1-year RI: $0.0265/hour (-36%)
- 3-year RI: $0.0178/hour (-57%)

Savings:
- On-Demand: $30.37/month
- 1-year RI: $19.35/month (save $11/month)
- 3-year RI: $12.99/month (save $17/month)
```

### 3. Savings Plans
```
Commit to $/hour usage
More flexible than RIs
Up to 72% discount

When to use:
- Mix of instance types
- Flexibility needed
- Changing workloads

Types:
1. Compute Savings Plan:
   - Any instance type
   - Any region
   - Up to 66% off

2. EC2 Instance Savings Plan:
   - Specific instance family
   - Specific region
   - Up to 72% off

Example:
- Commit: $50/month
- Use any compute (EC2, Lambda, Fargate)
- Savings: Up to 66% off
```

### 4. Spot Instances
```
Bid on unused EC2 capacity
Up to 90% discount!
Can be terminated with 2-min warning

When to use:
- Fault-tolerant apps
- Batch processing
- Data analysis
- CI/CD pipelines
- Flexible workloads

Not for:
- Databases
- Critical apps
- Stateful services

Example:
- On-Demand: $0.0416/hour
- Spot: $0.0125/hour (-70%!)

Savings:
- On-Demand: $30.37/month
- Spot: $9.13/month (save $21/month!)
```

## Pricing Model Comparison

```
+------------------+----------+-----------+---------+
| Model            | Discount | Flexible  | Risk    |
+------------------+----------+-----------+---------+
| On-Demand        | 0%       | ★★★★★    | None    |
| Reserved 1yr     | 30-40%   | ★★        | Low     |
| Reserved 3yr     | 60-72%   | ★         | Medium  |
| Savings Plan     | up to 66%| ★★★★      | Low     |
| Spot             | up to 90%| ★★★       | High    |
+------------------+----------+-----------+---------+
```

## Service-Specific Pricing

### EC2 Pricing
```
Charged for:
1. Instance hours (per second, 60s minimum)
2. Instance type (t3.micro to p4d.24xlarge)
3. Region (varies by region)
4. Operating system (Linux cheaper than Windows)

Example (us-east-1, Linux):
- t3.micro: $0.0104/hour ($7.59/month)
- t3.small: $0.0208/hour ($15.18/month)
- t3.medium: $0.0416/hour ($30.37/month)
- t3.large: $0.0832/hour ($60.74/month)

Stopped instance:
- Compute: $0
- EBS storage: Still charged!
```

### S3 Pricing
```
Charged for:
1. Storage (per GB/month)
2. Requests (PUT, GET, DELETE)
3. Data transfer OUT

Storage tiers:
- Standard: $0.023/GB (first 50TB)
- Intelligent-Tiering: $0.023/GB + $0.0025 per 1000 objects
- Infrequent Access: $0.0125/GB
- Glacier: $0.004/GB
- Glacier Deep Archive: $0.00099/GB

Requests:
- PUT: $0.005 per 1,000
- GET: $0.0004 per 1,000

Data transfer:
- IN: FREE
- OUT to internet: $0.09/GB (first 10TB)

Example:
- 100GB Standard: $2.30/month
- 10,000 PUT: $0.05/month
- 100,000 GET: $0.04/month
- 10GB transfer: $0.90/month
- Total: $3.29/month
```

### RDS Pricing
```
Charged for:
1. Instance hours
2. Storage (EBS)
3. Backup storage (automated backups)
4. Data transfer

Example (db.t3.micro, 20GB):
- Instance: $0.017/hour ($12.41/month)
- Storage: 20GB × $0.115 = $2.30/month
- Backups: Same as storage (first 20GB free)
- Total: ~$15/month

Multi-AZ (high availability):
- Cost: 2x instance price
- Example: $24.82 + $2.30 = $27/month
```

### Lambda Pricing
```
Charged for:
1. Requests
2. Duration (GB-seconds)

Free tier (FOREVER!):
- 1M requests/month
- 400,000 GB-seconds

Pricing:
- Requests: $0.20 per 1M
- Duration: $0.0000166667 per GB-second

Example (128MB, 200ms):
- 10M requests/month
- Requests: 9M paid × $0.20 / 1M = $1.80
- Duration: 10M × 0.2s × 0.125GB = 250,000 GB-s
- Duration cost: 250,000 × $0.0000166667 = $4.17
- Total: $5.97/month

Compare to EC2 t3.micro: $7.59/month
Lambda can be cheaper!
```

### DynamoDB Pricing
```
2 modes:

1. On-Demand:
   - Pay per request
   - No capacity planning
   - Write: $1.25 per million
   - Read: $0.25 per million

2. Provisioned:
   - Reserve capacity
   - Write: $0.00065 per hour per WCU
   - Read: $0.00013 per hour per RCU
   - Cheaper for steady traffic

Free tier (FOREVER!):
- 25GB storage
- 25 WCU
- 25 RCU

Small app = FREE!
```

## Data Transfer Pricing

### The Golden Rules
```
1. IN: Always FREE ✅
2. OUT to internet: $$$$ 💸
3. Between services (same region): FREE ✅
4. Between AZs: $0.01/GB
5. Between regions: $0.02/GB
```

### Data Transfer Costs
```
OUT to internet (per GB):
- First 10TB: $0.09/GB
- Next 40TB: $0.085/GB
- Next 100TB: $0.07/GB
- Over 150TB: $0.05/GB

Example:
- Website: 1TB/month traffic
- Cost: $90/month
- Use CloudFront: $10/month (85% savings!)
```

## Free Tier

### 12 Months Free
```
From account creation:

EC2:
- 750 hours/month t2.micro or t3.micro
- Enough for 1 instance 24/7

S3:
- 5GB storage
- 20,000 GET requests
- 2,000 PUT requests

RDS:
- 750 hours/month db.t2.micro or db.t3.micro
- 20GB storage

CloudFront:
- 50GB data transfer OUT
- 2M HTTP/HTTPS requests
```

### Always Free
```
Lambda:
- 1M requests/month
- 400,000 GB-seconds

DynamoDB:
- 25GB storage
- 25 WCU, 25 RCU

CloudWatch:
- 10 custom metrics
- 10 alarms
- 1M API requests

SNS:
- 1M publishes
- 100,000 HTTP deliveries
- 1,000 email deliveries
```

## Cost Optimization Strategies

### 1. Right-Size Instances
```
❌ Problem: t3.large for small app
Cost: $60/month

✅ Solution: t3.micro
Cost: $7.59/month

Savings: $52/month (87%!)

Use AWS Compute Optimizer for recommendations
```

### 2. Reserved Instances for Steady State
```
Production database 24/7:

On-Demand: $30/month
1-year RI: $19/month (-36%)
3-year RI: $13/month (-57%)

Breakeven: 6-8 months
```

### 3. Spot for Flexible Workloads
```
Batch processing:

On-Demand: $100/month
Spot: $15/month (-85%!)

Must tolerate interruptions
```

### 4. S3 Lifecycle Policies
```
Auto-move old data:

- 0-30 days: Standard ($0.023/GB)
- 30-90 days: IA ($0.0125/GB)
- 90+ days: Glacier ($0.004/GB)

1TB for 1 year:
- All Standard: $276
- With lifecycle: $87
- Savings: $189/year (68%!)
```

### 5. Use Savings Plans
```
Commit $50/month:

Before: $80/month On-Demand
After: $50/month + overages
Savings: $30/month (37%)

Flexible across services!
```

### 6. CloudFront for Static Content
```
Direct from S3:
- 1TB transfer: $90/month

Through CloudFront:
- 1TB transfer: $10-15/month

Savings: $75/month (83%!)
```

### 7. Stop Unused Resources
```
Development instances:

Running 24/7: $30/month
Running business hours (40%): $12/month
Savings: $18/month (60%)

Automate with Lambda!
```

## Hidden Costs

### 1. EBS Snapshots
```
⚠️ Keep adding up!

10 snapshots × 50GB × $0.05/GB = $25/month

Solution: Delete old snapshots
```

### 2. Elastic IPs (Unused)
```
⚠️ Charged if not attached!

Unused EIP: $3.60/month

Solution: Release unused IPs
```

### 3. NAT Gateway
```
⚠️ Not free!

Cost: $32/month + $0.045/GB

For dev: Use NAT instance ($7/month)
```

### 4. Load Balancers
```
⚠️ Cost even if idle!

ALB: $16/month + $0.008/LCU
NLB: $16/month + $0.006/NLCU

Small app: Consider CloudFront + Lambda
```

### 5. Data Transfer
```
⚠️ Biggest surprise!

Example:
- 500GB out to internet: $45/month
- Between regions: $10/month

Optimize:
- Use CloudFront
- Compress data
- Keep data in same region
```

## Pricing Calculators

### AWS Pricing Calculator
```
https://calculator.aws/

Estimate costs:
1. Add services
2. Configure (instance type, storage, etc.)
3. See monthly cost
4. Compare options

Example output:
- EC2: $30/month
- RDS: $15/month
- S3: $5/month
- Data transfer: $10/month
- Total: $60/month
```

### Cost Explorer
```
Analyze actual costs:

1. Billing → Cost Explorer
2. View by:
   - Service
   - Region
   - Tag
   - Time period
3. Filter and group
4. Forecast future costs

Find optimization opportunities!
```

## Cost Management Best Practices

### 1. Tag Everything
```
Tags:
- Environment: production/dev/test
- Project: web-app/mobile-app
- Owner: team-name
- Cost-center: department

Track costs by project/team
```

### 2. Set Budgets
```
Create budgets:
- Monthly: $100
- Alerts: 50%, 80%, 100%
- Email notifications

Catch overages early!
```

### 3. Review Monthly
```
Monthly checklist:
- Top 5 services
- Unexpected charges
- Unused resources
- Optimization opportunities

Delete unused resources!
```

### 4. Use Cost Anomaly Detection
```
ML-powered monitoring:
- Learns normal spending
- Alerts on unusual spikes
- "$500 spike in EC2 detected!"

Catch mistakes fast!
```

## Pricing Checklist

🔴 **Before Launching:**
- ✅ Estimate costs
- ✅ Choose right instance size
- ✅ Consider Reserved/Savings Plan
- ✅ Plan for data transfer

🟠 **After Launch:**
- ✅ Enable billing alerts
- ✅ Create budgets
- ✅ Tag resources
- ✅ Monitor costs weekly

🟡 **Monthly:**
- ✅ Review spending
- ✅ Right-size resources
- ✅ Delete unused resources
- ✅ Implement optimizations

## Quick Reference

### Typical Small App Costs
```
EC2 t3.micro: $7.59/month
RDS db.t3.micro: $15/month
S3 (10GB): $0.23/month
CloudFront (50GB): $0.85/month
Route 53: $0.50/month

Total: ~$25/month
```

### Typical Medium App Costs
```
EC2 t3.medium (2): $60/month
RDS Multi-AZ: $27/month
ALB: $16/month
S3 (100GB): $2.30/month
CloudFront (500GB): $8.50/month

Total: ~$115/month
```

### Savings Summary
```
Reserved (1yr): Save 30-40%
Reserved (3yr): Save 60-72%
Savings Plan: Save up to 66%
Spot: Save up to 90%
Right-sizing: Save 20-40%
CloudFront: Save 80-90% on transfer
Lifecycle policies: Save 60-80% on storage
```

## 📖 Next Steps

1. [Cost Management Basics](../getting-started/cost-management-basics.md)
2. [Cost Optimization Guide](../best-practices/cost-optimization.md)
3. [Hidden Costs](../best-practices/hidden-costs.md)

## Related Resources

- [AWS Free Tier](../getting-started/aws-free-tier.md)
- [Billing Alerts](../getting-started/setting-up-billing-alerts.md)
- [AWS Pricing Calculator](https://calculator.aws/)