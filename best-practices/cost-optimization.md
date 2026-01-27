# AWS Cost Optimization Guide 💰

Practical strategies to reduce AWS bills without sacrificing performance.

## Quick Wins (High Impact, Easy)

### Stop Unused Resources
```
Typical savings: 20-30% of bill
```

- [ ] **Delete unused EC2 instances**
  - Console → EC2 → Instances
  - Stop instances if not used for 7 days
  - Delete after 30 days if not restarted
  - Savings: $0.01-0.05/hour per instance

- [ ] **Delete unused EBS volumes**
  - EC2 → Volumes → Look for "Available"
  - Savings: $0.10/GB/month

- [ ] **Delete old snapshots**
  - EC2 → Snapshots → Delete old ones
  - Savings: $0.05/GB/month

- [ ] **Remove unused NAT Gateways**
  - VPC → NAT Gateways
  - Costs $32/month each!
  - Delete if not needed

- [ ] **Clean RDS snapshots**
  - RDS → Snapshots → Keep 1-2 recent
  - Savings: $0.21/GB/month

### Right-Size Instances
```
Typical savings: 15-25% of compute costs
```

- [ ] **Review EC2 CPU utilization**
  - CloudWatch → Metrics → CPU
  - If under 20%, downsize
  - t3.large → t3.medium = 50% savings

- [ ] **Use t3 instead of t2**
  - Newer, 20% cheaper
  - Drop-in replacement

- [ ] **Review RDS sizes**
  - CloudWatch → DB Load
  - Scale down if low utilization

## Medium Effort, High Savings

### Use Reserved Instances
```
Savings: 30-70% of compute costs
Example: t3.medium 1-year RI saves $180/year vs on-demand
```

**Strategy:**
- Start with on-demand to find stable workloads
- After 3 months, buy 1-year RI (40% savings)
- Better: 3-year RI (70% savings)

### Use Spot Instances  
```
Savings: 70-90% of compute costs
Example: t3.medium spot = 76% cheaper
```

**Good for:**
- Batch processing
- Development/testing
- CI/CD pipelines
- Non-critical workloads

### Optimize S3 Storage
```
Savings: 50-70% on old data
```

- [ ] **Enable S3 Intelligent-Tiering**
  - Automatically moves between tiers
  - Reduces manual work

- [ ] **Use lifecycle policies**
  - After 30 days → Infrequent Access (-60%)
  - After 90 days → Glacier (-90%)

- [ ] **Delete old versions**
  - Keep versioning for safety
  - Delete versions over 90 days old

### Optimize Data Transfer
```
Savings: 10-30% of data transfer
Tip: Data to internet costs $0.09/GB - expensive!
```

- [ ] **Use CloudFront for static content**
  - 80% cheaper than direct transfer
  - Same performance, better price

- [ ] **Keep resources in same region**
  - EC2 to S3 within region = FREE
  - EC2 to S3 cross-region = CHARGED

- [ ] **Use VPC endpoints**
  - Free data transfer
  - Keep traffic private

## Monitoring & Control

### Set Up Billing Alerts
- [ ] Enable Cost Anomaly Detection
- [ ] Create Budget Alerts
- [ ] Review monthly spending

### Tag Everything
- [ ] Tag by project, team, environment
- [ ] Analyze spending by tag
- [ ] Charge costs correctly

## Cost Reduction Examples

**Example: Reduce EC2 costs**
```
Before: t3.large always on = $600/month
After: 1-year RI t3.medium + Auto Scaling = $180/month
Savings: $420/month (-70%)
```

**Example: Reduce S3 costs**
```
Before: All standard storage = $150/month
After: Lifecycle to Glacier = $20/month
Savings: $130/month (-87%)
```

## Avoid These Mistakes

- ❌ Leave dev/test running 24/7 → Schedule shutdown
- ❌ Store everything in standard S3 → Use lifecycle policies
- ❌ Don't monitor unused resources → Tag and audit monthly
- ❌ Use NAT Gateway for everything → Use NAT instance for dev
- ❌ Multi-AZ RDS for dev → Single-AZ for testing

## 📖 Related Resources

- [Right-Sizing Recommendations](right-sizing.md)
- [Hidden Costs Guide](hidden-costs.md)
- [Billing Issues Troubleshooting](../troubleshooting/billing-issues.md)