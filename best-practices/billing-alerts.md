# AWS Billing Alerts 💰

How to monitor costs and avoid bill surprises.

## Why Billing Alerts Matter

**Real stories:**
- Dev accidentally created 1,000 EC2 instances → $15,000 bill in 1 hour
- Lambda infinite loop → $5,000/month bill spike
- Database query inefficiency → $2,000/month increase
- Unattached EBS volumes → $300/month wasted

**Prevention:** Set billing alerts!

## Step 1: Enable Cost Management

```
AWS Console → Billing and Cost Management
Preferences:
☑ Receive Free Tier alerts
☑ Receive billing alerts
☑ Receive cost optimization recommendations
```

## Step 2: Set Billing Alerts

### Create Alert via CloudWatch

```
Billing → Billing Preferences → Edit
Billing Alerts → Create Alert
```

**Setup:**
1. Alert threshold: $50 (or your budget)
2. Email recipients: your-email@company.com
3. Enable: Yes

### Create Advanced Alert

```
CloudWatch → Alarms → Create Alarm
Metric: Estimated Charges
Threshold: $100
Period: Daily
Action: Send email
```

## Step 3: Setup Cost Anomaly Detection

```
AWS Cost Management → Anomaly Detection
Enable Anomaly Detection:
✓ Automatically detect unusual spending
✓ Alert when spending deviates from baseline
✓ ML-powered (learns your patterns)

Threshold: 100% increase (doubles)
```

## Common Cost Surprises

### 1. Unattached EBS Volumes
```
Cost: $0.10/GB/month per volume
Example: 100GB unused volume = $10/month

Check:
EC2 → Volumes → Filter "available"
Delete unused volumes
```

### 2. Idle NAT Gateways
```
Cost: $32/month per NAT gateway
Plus $0.045/GB data processed

Check:
VPC → NAT Gateways
Delete if not actively processing traffic
```

### 3. Old EBS Snapshots
```
Cost: $0.05 per snapshot
Example: 1,000 old snapshots = $50/month

Check:
EC2 → Snapshots → Delete old snapshots
Or use Lifecycle Manager for auto-cleanup
```

### 4. Unused Elastic IPs
```
Cost: $0.005/hour when not attached ($3.60/month)

Check:
EC2 → Addresses → Look for "Not associated"
Release unused IPs
```

### 5. High Data Transfer Costs
```
Cost: $0.09/GB to internet (can be $1000s/month)

Optimization:
- Use CloudFront CDN (87% cheaper)
- Optimize video quality
- Compress data before transfer
```

### 6. RDS Backup Storage
```
Cost: $0.095/GB/month
Example: 500GB backups = $47.50/month

Optimize:
- Reduce retention (30 days vs 35)
- Delete manual snapshots
- Use Glacier for long-term storage
```

### 7. DynamoDB Over-provisioning
```
Cost: $1.25/million writes, $0.25/million reads
Example: Provisioned for 1000 writes/sec but using 10 = $1190/month wasted

Optimization:
- Switch to on-demand pricing
- Use auto-scaling
- Monitor actual usage
```

## Cost Tracking Techniques

### Use Tags for Tracking
```
All resources tagged:
tagName: project-name (web-app, analytics, etc)
tagEnv: production, development, testing
tagTeam: backend, frontend, devops

Billing → Cost Allocation → Enable Tags
Cost Analysis: Group by project/team
```

### Setup Budget
```
Budgeting → Budgets → Create Budget

Budget Name: Monthly Limit
Budget Limit: $500
Alert Threshold:
- 50% ($250) → email
- 80% ($400) → email
- 100% ($500) → email + SNS

Filter: By tag (project-name: web-app)
```

### Cost Analysis by Service
```
Cost Management → Cost Explorer → Analyze
Grouped by: Service
Time period: Last 3 months
Looking for: Unexpected spikes
```

### Example Report
```
Monthly Breakdown:
- EC2: $45 (compute)
- RDS: $30 (database)
- S3: $5 (storage)
- Data Transfer: $15 (internet traffic)
- Lambda: $2 (serverless functions)
- Other: $3
Total: $100/month
```

## Free Tier Monitoring

```
Billing → Free Tier
Monitor usage:
✓ EC2 hours (750/month)
✓ RDS database (750 hours)
✓ S3 storage (5GB)
✓ Lambda (1M requests)
✓ DynamoDB (25GB)
```

**Set alert for:** 80% of free tier limit

## Shared Responsibility Model

### AWS Pays For
- Infrastructure maintenance
- Security of cloud

### You Pay For
- Running instances (even when idle)
- Data transfer out
- Storage usage
- Requests made

### Cost Control Measures
```
EC2:
- Right-size instances
- Use Spot instances (70% savings)
- Use Reserved Instances (30% savings)
- Delete stopped instances if not needed

Storage:
- Lifecycle policies (archive old data)
- Delete unused snapshots
- Enable S3 Intelligent-Tiering

Data Transfer:
- Use CloudFront (87% cheaper)
- Transfer within same region (free)
- Batch operations (fewer requests)

Databases:
- Right-size instance type
- Auto-scaling for DynamoDB
- Multi-AZ costs extra (pay for redundancy)

Serverless:
- Monitor Lambda concurrency
- Batch small Lambda calls
- Use Reserved Concurrency
```

## Automated Cost Reduction

### AWS Compute Optimizer
```
Compute Optimizer → Analyze
Recommendations for:
- Oversized EC2 instances (-20-30%)
- Inefficient Lambda functions
- Inefficient RDS instances

One-click implement recommendations
```

### Scheduled Shutdowns
```
For development/test resources:
Schedules → Create Schedule
Action: Stop/Start at specific times

Example:
- 22:00 → Stop dev instances
- 08:00 → Start dev instances
Savings: 50% of compute costs
```

## Billing Alert Checklist

🔴 **CRITICAL**
- ✅ Billing alerts enabled ($50-100)
- ✅ Cost anomaly detection on
- ✅ Budget set monthly

🟠 **HIGH**
- ✅ Monthly cost review
- ✅ Unused resources cleaned up
- ✅ Tags used for tracking

🟡 **IMPORTANT**
- ✅ Free tier monitoring
- ✅ Reserved instances purchased (30% savings)
- ✅ Spot instances used where appropriate

## 📖 Related Resources

- [AWS Cost Management](https://aws.amazon.com/aws-cost-management/)
- [Cost Optimization Guide](cost-optimization.md)
- [Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)