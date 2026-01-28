# EC2 Pricing 💰

EC2 pricing varies based on instance type, size, region, and usage model.

## Pricing Models

### 1. On-Demand

**Pay per hour/second - no commitment**

```
t3.micro: $0.0104/hour
t3.small: $0.0208/hour
m5.large: $0.096/hour
c5.xlarge: $0.17/hour

Best for: Testing, development, unpredictable workloads
```

### 2. Reserved Instances (RI)

**Commit 1-3 years, get 30-72% discount**

```
Example (us-east-1):
t3.micro on-demand:    $0.0104/hour = $91/year
t3.micro 1-year RI:    $64/year (30% discount)
t3.micro 3-year RI:    $48/year (47% discount)

Best for: Production, predictable workloads, cost savings
```

### 3. Spot Instances

**Bid for spare capacity, up to 90% discount**

```
t3.micro on-demand:    $0.0104/hour
t3.micro spot:         $0.003/hour (70% discount!)
Risk: Can be interrupted without notice

Best for: Batch jobs, data processing, flexible timing
```

### 4. Savings Plans

**Commit to usage (not specific instance), flexible**

```
Compute Savings Plan:
- 1-year: 20-21% discount
- 3-year: 32-37% discount

Flexibility: Change instance type, region, etc.

Best for: Flexible workloads across regions
```

## Cost by Instance Type

### Micro (Free Tier)
```
t3.micro: $0.0104/hour = $9/month (continuous)
Annual: ~$91/year on-demand

Best for: Low-traffic websites, learning, free tier
```

### Small/Medium (General Purpose)
```
t3.small: $0.0208/hour = $15/month
m5.large: $0.096/hour = $70/month
t4g.medium: $0.0336/hour = $25/month

Best for: Most applications, web apps, databases
```

### Compute Optimized
```
c5.large: $0.085/hour = $62/month
c5.xlarge: $0.17/hour = $125/month

Best for: Batch processing, ML, gaming servers
```

### Memory Optimized
```
r5.large: $0.126/hour = $92/month
r5.xlarge: $0.252/hour = $185/month

Best for: In-memory databases, caching, SAP
```

## Monthly Cost Examples

### Simple Blog
```
1x t3.micro instance: $9/month
Elastic IP (if unused): $0
Total: ~$9/month

Annual: ~$108
```

### Small Web App
```
1x t3.small web: $15/month
1x t3.micro database: $9/month
Total: ~$24/month

Annual: ~$288
```

### Production HA App
```
2x m5.large web (multi-AZ): $140/month
2x t3.medium app: $30/month
2x m5.large database: $140/month (RDS often cheaper)
NAT Gateway: $32/month
Total: ~$340/month

Annual: ~$4,080
```

## Cost Optimization Tips

### 1. Use Appropriate Instance Type
```
t3 (burstable) for: Web apps, small databases
m5 (general) for: Mid-size apps
c5 (compute) for: Heavy CPU workloads
r5 (memory) for: Databases, caching

Don't overprovision - start small, scale up
```

### 2. Use Reserved Instances for Predictable
```
Dev/Prod mixed 70/30:
- 70% always on → Buy 1-year RI
- 30% variable → On-demand for flexibility

Savings: 30-50% vs pure on-demand
```

### 3. Use Spot for Flexible Workloads
```
Good for: Batch jobs, data processing, testing
Bad for: Production requiring 24/7 uptime

Savings: Up to 90% off on-demand
```

### 4. Stop Instances When Not Needed
```
Dev environment only during business hours:
- Running 9-5 (50 hours/week)
- 8 hours/day × 5 days = 40 hours
- 4 hours weekend testing = 4 hours
- Total: 216 hours/month (vs 730 if always running)

Savings: 70% if stopped nights/weekends
```

### 5. Right-Size Instances
```
Monitor CloudWatch:
- CPU: If consistently <20%, downsize
- Memory: If consistently <40%, downsize
- Network: If not saturated, smaller is fine

Cost vs Performance: Find the sweet spot
```

## Regional Pricing Variation

```
On-Demand t3.micro:
- us-east-1: $0.0104/hour (cheapest)
- us-west-2: $0.0117/hour (+12%)
- eu-west-1: $0.0117/hour (+12%)
- ap-south-1: $0.0094/hour (-10%)
- ap-northeast-1: $0.0117/hour (+12%)

Savings: Choose cheaper region (if possible)
```

## Free Tier (First 12 Months)

```
Eligible:
- 1x t2/t3.micro instance
- Per month: 750 hours (31 days × 24 hours)
- Meaning: 1 always-on instance = free!

Includes:
- EC2 compute hours
- EBS storage (30 GB/month)
- Data transfer out (1 GB/month)

Free for 12 months after account creation
```

## Additional Costs

```
Not included in hourly cost:
- Elastic IP (unused): $0.005/hour
- EBS storage: $0.10/GB/month
- Data transfer out: $0.09/GB (varies by region)
- NAT Gateway: $0.045/hour
- Load Balancer: $0.0225/hour

Total usually: 2-3x instance cost
```

## Estimating Your Costs

```
1. Choose instance type: m5.large
2. Base: $0.096/hour = $70/month (730 hours)
3. Add EBS (20GB): $2/month
4. Add data transfer out (100GB): $9/month
5. Add NAT (high traffic): $32/month

Total: ~$113/month = $1,356/year
```

## Cost Monitoring

```
AWS Console:
- Billing Dashboard → EC2 costs
- Cost Explorer → Filter by service
- CloudWatch → Track utilization
- AWS Budgets → Set alerts

Best practice: Monitor weekly, review monthly
```

## Next Steps

→ [Instance Types](./instance-types.md) - Choosing right size
→ [What is EC2](./what-is-ec2.md) - Overview
→ [Launching Instances](./launching-first-instance.md) - Getting started