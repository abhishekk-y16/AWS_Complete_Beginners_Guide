# AWS Free Tier 🆓

What's free and how to stay within limits.

## What is Free Tier?

AWS gives new users FREE services for 12 months + some services free forever!

**Goal:** Learn AWS without spending money

## Free Tier Types

### 1. 12 Months Free (New Accounts)

Starts when you create account

### 2. Always Free (Forever!)

Never expires, even after 12 months

### 3. Trials

Short-term free trials (30-60 days)

## Top Free Services

### EC2 (Compute)

```
Free: 750 hours/month t2.micro or t3.micro
      = 1 instance running 24/7

Example:
- 1 instance for 720 hours = FREE
- 2 instances for 360 hours each = FREE
- 1 instance for 800 hours = 50 hours charged

Duration: 12 months
After: $7.50/month for t3.micro
```

### S3 (Storage)

```
Free: 5GB standard storage
      20,000 GET requests
      2,000 PUT requests

Example:
- Store 3GB photos = FREE
- Store 10GB = 5GB FREE + $0.11 for extra 5GB

Duration: 12 months
After: $0.023/GB/month
```

### RDS (Database)

```
Free: 750 hours/month db.t2.micro
      20GB storage
      20GB backup storage

Example:
- MySQL db.t2.micro 24/7 = FREE
- PostgreSQL db.t2.micro 24/7 = FREE

Duration: 12 months
After: $15/month for db.t3.micro
```

### Lambda (Serverless)

```
Free: 1 million requests/month
      400,000 GB-seconds compute

Example:
- 1M quick functions = FREE
- Website with 10K users = FREE

Duration: FOREVER! 🎉
Always free, even after 12 months
```

### DynamoDB (NoSQL)

```
Free: 25GB storage
      25 read/write capacity units
      2.5M read requests

Example:
- Small app database = FREE
- Store user profiles = FREE

Duration: FOREVER! 🎉
Always free
```

### CloudFront (CDN)

```
Free: 1TB data transfer out
      10M HTTP requests

Example:
- Host website images = FREE
- Deliver static files = FREE

Duration: 12 months
After: $0.085/GB
```

### SNS (Notifications)

```
Free: 1M requests
      1,000 email notifications

Example:
- Send alerts = FREE
- Email notifications = FREE

Duration: FOREVER! 🎉
```

### CloudWatch (Monitoring)

```
Free: 10 custom metrics
      10 alarms
      5GB logs

Example:
- Monitor CPU usage = FREE
- Set billing alarms = FREE

Duration: FOREVER! 🎉
```

## Free Tier Example Projects

### Project 1: Simple Website

```
Services:
- EC2 t3.micro (web server): FREE
- S3 5GB (images): FREE
- CloudFront 1TB (CDN): FREE
- Route 53 (DNS): $0.50/month

Total: $0.50/month for 12 months
After 12 months: $8-10/month
```

### Project 2: Serverless API

```
Services:
- Lambda 1M requests: FREE (forever!)
- API Gateway 1M requests: FREE
- DynamoDB 25GB: FREE (forever!)
- S3 5GB: FREE

Total: $0/month
After 12 months: Still mostly FREE!
```

### Project 3: Learning Setup

```
Services:
- 1 EC2 for practice: FREE
- RDS for database learning: FREE
- S3 for file uploads: FREE
- CloudWatch for monitoring: FREE

Total: $0/month for first year
Perfect for learning!
```

## Staying Within Free Tier

### Rule 1: Watch Your Hours

```
✅ Good: 1 t3.micro 24/7 = 720 hours (FREE)
❌ Bad: 2 t3.micro 24/7 = 1440 hours (720 charged!)

Tip: Stop instances when not using
```

### Rule 2: Right Instance Type

```
✅ Free: t2.micro, t3.micro
❌ Not Free: t2.small, t3.medium, any other type

Always choose t2.micro or t3.micro!
```

### Rule 3: Monitor Usage

```
Billing Dashboard:
1. Account → Billing
2. Click "Free Tier"
3. See usage:
   - EC2: 350/750 hours used
   - S3: 2GB/5GB used
   - RDS: 480/750 hours used

Check weekly!
```

### Rule 4: Set Alerts

```
Billing Preferences:
☑ Receive Free Tier Usage Alerts
Email: your-email@example.com

Get warnings at 85% usage
```

### Rule 5: Delete When Done

```
After testing:
1. Stop EC2 instances
2. Delete unused volumes
3. Delete old snapshots
4. Empty S3 buckets
5. Delete RDS databases

Costs $0 when deleted!
```

## Common Free Tier Mistakes

### Mistake 1: Wrong Instance Type

```
❌ Launched t2.small instead of t2.micro
Result: Charged $17/month

Solution: Always choose t2.micro or t3.micro
```

### Mistake 2: Forgot to Stop

```
❌ Left 2 instances running
Result: 1500 hours used (750 over limit)
Cost: $5.50 overage

Solution: Stop when not using
```

### Mistake 3: EBS Snapshots

```
❌ Created 50 snapshots
Result: $2.50/month (snapshots not fully free)

Solution: Delete old snapshots
```

### Mistake 4: NAT Gateway

```
❌ Created NAT gateway
Result: $32/month (NOT FREE!)

Solution: Use NAT instance or avoid for learning
```

### Mistake 5: Data Transfer

```
❌ Downloaded 100GB from S3
Result: $9/month transfer cost

Solution: Use CloudFront (1TB free)
```

## After Free Tier Expires

### Month 13 Costs

```
Same usage, now paid:

- EC2 t3.micro 24/7: $7.50/month
- RDS db.t3.micro: $15/month
- S3 5GB: $0.11/month
- CloudFront 50GB: $4.25/month

Total: ~$27/month

Still cheap!
```

### Cost Reduction Tips

```
1. Use Lambda instead of EC2 (forever free!)
2. Use DynamoDB instead of RDS (forever free!)
3. Stop instances when not using (50% savings)
4. Use Spot instances (70% discount)
5. Buy Reserved Instances (30% discount)
```

## Monitoring Free Tier Usage

### AWS Budgets

```
1. Billing → Budgets
2. Create budget
3. Type: Cost budget
4. Amount: $1 (or $0)
5. Alert at: $0.01
6. Email: your-email@example.com

✅ Get alerts if any charges!
```

### Cost Explorer

```
1. Billing → Cost Explorer
2. Enable (free)
3. View costs by:
   - Service
   - Region
   - Tag
4. See what's costing money
```

## Free Tier Checklist

✅ **Setup:**
- Enabled free tier alerts
- Set $1 budget alarm
- Bookmarked free tier dashboard

✅ **Using:**
- Only t2.micro or t3.micro instances
- Monitoring usage weekly
- Stopping instances when not using

✅ **Cleanup:**
- Deleted test resources
- Removed unused snapshots
- Emptied unused S3 buckets

## Free Tier Resources

**Check Usage:**
```
Billing → Free Tier
See remaining hours/GB
```

**Full List:**
```
aws.amazon.com/free
All free tier services listed
```

## 📖 Next Steps

1. [Cost Management Basics](cost-management-basics.md)
2. [Setting Up Billing Alerts](setting-up-billing-alerts.md)
3. [Launch First EC2](../tutorials/deploy-web-server.md)

## Related Resources

- [AWS Free Tier Official](https://aws.amazon.com/free/)
- [Cost Optimization](../best-practices/cost-optimization.md)
- [Billing Alerts](../best-practices/billing-alerts.md)