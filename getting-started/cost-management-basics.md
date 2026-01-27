# Cost Management Basics 💰

How to understand and control your AWS costs.

## Understanding AWS Pricing

### Pay-As-You-Go Model
```
No upfront costs
No termination fees
Pay only for:
- What you use
- When you use it
- How much you use

Stop using → Stop paying
```

### Pricing Factors

**1. Compute (EC2):**
- Instance type (t3.micro vs t3.large)
- Hours running
- Region

**2. Storage (S3, EBS):**
- GB stored
- Storage class
- Requests made

**3. Data Transfer:**
- Transfer OUT to internet (expensive!)
- Transfer between regions
- Transfer IN (usually free)

**4. Requests:**
- API calls
- Lambda invocations
- Database queries

## Viewing Your Costs

### Billing Dashboard
```
1. Click account name (top right)
2. Billing and Cost Management
3. See:
   - Month-to-date: $12.34
   - Forecasted: $25.00
   - Last month: $8.50
```

### Cost Explorer
```
Billing → Cost Explorer

View costs by:
- Service (EC2, S3, RDS)
- Region (us-east-1, eu-west-1)
- Tag (project, environment)
- Time period (daily, monthly)

Filters:
- Last 3 months
- Top 5 services
- Production only
```

### Bills
```
Billing → Bills → Select month

Detailed breakdown:
- EC2:
  - Compute: $10.50
  - Data transfer: $2.30
  - EBS volumes: $1.20
- S3:
  - Storage: $0.50
  - Requests: $0.10
- Total: $14.60

Download CSV for analysis
```

## Setting Budgets

### Create Monthly Budget
```
1. Billing → Budgets → Create budget

2. Budget type: Cost budget

3. Budget amount: $50/month

4. Alerts:
   - 50% ($25) → Email warning
   - 80% ($40) → Email alert
   - 100% ($50) → Email + SMS

5. Email: your-email@example.com

6. Create budget

✅ Alerts when approaching limit!
```

### Budget Types

**Cost Budget:**
```
Track total spending
Example: Alert at $100/month
Best for: Overall cost control
```

**Usage Budget:**
```
Track specific usage
Example: Alert at 750 EC2 hours
Best for: Free tier monitoring
```

**RI Utilization Budget:**
```
Track Reserved Instance usage
Example: Alert if < 80% utilized
Best for: Optimizing RIs
```

## Cost Allocation Tags

### Why Tags Matter
```
Track costs by:
- Project (web-app, mobile-app)
- Environment (prod, dev, test)
- Team (frontend, backend)
- Cost center (engineering, marketing)
```

### Enable Cost Allocation
```
1. Tag all resources:
   Environment: production
   Project: web-app
   Owner: john@company.com

2. Billing → Cost Allocation Tags

3. Activate tags:
   ☑ Environment
   ☑ Project
   ☑ Owner

4. Wait 24 hours

5. Cost Explorer → Group by tag

✅ See costs by project!
```

## Common Cost Surprises

### 1. Data Transfer
```
Cost: $0.09/GB to internet

Example:
- Stream 1TB video = $90!
- Website with 100GB traffic = $9

Optimization:
- Use CloudFront CDN (87% cheaper)
- Compress files
- Cache aggressively
```

### 2. NAT Gateway
```
Cost: $32/month + $0.045/GB

Just sitting there = $32/month!

Optimization:
- Delete if not needed
- Use NAT instance (cheaper)
- Avoid for dev/test
```

### 3. Idle Resources
```
Forgotten resources:
- Stopped EC2: EBS still charged ($8/month)
- Unattached EBS: Still charged
- Elastic IP not attached: $3.60/month
- Old snapshots: $0.05 each

Action: Weekly cleanup!
```

### 4. Wrong Instance Type
```
Mistake:
- Launched t3.large
- Needed t3.micro
- Cost: $70/month vs $7/month

Solution: Right-size instances
```

## Cost Optimization Tips

### 1. Stop When Not Using
```
Development instances:
- Stop at 6 PM
- Start at 9 AM
- Savings: 60% of compute costs

Weekends:
- Stop Friday evening
- Start Monday morning
- Additional 30% savings
```

### 2. Right-Size Instances
```
Use AWS Compute Optimizer:
1. Services → Compute Optimizer
2. View recommendations
3. See:
   - Current: t3.large ($70/month)
   - Recommended: t3.small ($17/month)
   - Savings: $53/month (76%!)
4. Implement changes
```

### 3. Use Free Tier
```
First 12 months:
- EC2: 750 hours/month FREE
- S3: 5GB FREE
- RDS: 750 hours/month FREE
- Lambda: 1M requests FREE (forever!)
- DynamoDB: 25GB FREE (forever!)

Stay within limits = $0 cost
```

### 4. Reserved Instances
```
Production servers running 24/7:

On-Demand: $70/month
Reserved (1 year): $49/month (-30%)
Reserved (3 years): $28/month (-60%)

Breakeven: If runs > 6 months
```

### 5. Spot Instances
```
Non-critical workloads:

On-Demand: $70/month
Spot: $10-20/month (-70-90%!)

Catch: Can be terminated

Good for:
- Batch processing
- Data analysis
- Development
```

### 6. S3 Lifecycle Policies
```
Auto-move old data:

- 0-30 days: Standard ($0.023/GB)
- 30-90 days: Infrequent Access ($0.0125/GB)
- 90+ days: Glacier ($0.004/GB)
- 365+ days: Deep Archive ($0.00099/GB)

Savings: 95% for old data!
```

## Cost Monitoring Tools

### CloudWatch Billing Alarm
```
1. CloudWatch (us-east-1 only!)
2. Create Alarm
3. Billing → Total Estimated Charge
4. Threshold: > $50
5. Email: your-email@example.com

✅ Alert when bill exceeds threshold
```

### AWS Cost Anomaly Detection
```
1. Cost Management → Anomaly Detection
2. Enable
3. ML learns your patterns
4. Alerts on unusual spending

Example:
- Normal: $50/month
- Spike: $500/month
- Alert: "Unusual spending detected!"
```

### Third-Party Tools
```
Free tools:
- CloudHealth (free tier)
- CloudCheckr (free tier)
- AWS Cost Explorer (built-in)

Paid tools:
- Datadog ($15/month)
- New Relic ($25/month)
```

## Monthly Cost Review

### Week 1: Check Current Spend
```
1. Billing Dashboard
2. Month-to-date: $X
3. Forecasted: $Y
4. On track? Yes/No
```

### Week 2: Analyze Top Costs
```
1. Cost Explorer
2. Top 5 services
3. Top 5 regions
4. Any surprises?
```

### Week 3: Cleanup
```
1. List unused resources:
   - Stopped instances
   - Unattached volumes
   - Old snapshots
   - Unused Elastic IPs

2. Delete them

3. Potential savings: $10-50/month
```

### Week 4: Optimize
```
1. Right-size instances
2. Buy Reserved Instances
3. Enable lifecycle policies
4. Implement auto-scaling

Potential savings: 20-40%
```

## Cost Management Checklist

🔴 **Setup (Do Once):**
- ✅ Billing alerts enabled
- ✅ Budget created
- ✅ Cost allocation tags activated
- ✅ Cost Explorer enabled

🟠 **Weekly:**
- ✅ Check current spend
- ✅ Delete unused resources
- ✅ Review free tier usage

🟡 **Monthly:**
- ✅ Analyze costs by service
- ✅ Right-size instances
- ✅ Review and optimize

## Sample Cost Breakdown

### Small Startup ($50/month)
```
EC2 (t3.small): $17/month
RDS (db.t3.micro): $15/month
S3: $5/month
CloudFront: $8/month
Route 53: $1/month
Data transfer: $4/month

Total: $50/month
```

### Growing App ($200/month)
```
EC2 Auto Scaling: $70/month
RDS Multi-AZ: $50/month
ElastiCache: $30/month
S3 + CloudFront: $20/month
Load Balancer: $16/month
Other: $14/month

Total: $200/month
```

## 📖 Next Steps

1. [Setting Up Billing Alerts](setting-up-billing-alerts.md)
2. [Cost Optimization Guide](../best-practices/cost-optimization.md)
3. [Hidden Costs](../best-practices/hidden-costs.md)

## Related Resources

- [AWS Free Tier](aws-free-tier.md)
- [Billing Alerts](../best-practices/billing-alerts.md)
- [AWS Pricing Calculator](https://calculator.aws/)