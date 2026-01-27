# Hidden AWS Costs 💸

Common costs you might forget about.

## Data Transfer Costs (Often Biggest!)

### Internet Data Transfer (Out)
```
Cost: $0.09 per GB to internet
Example: 1TB video streaming = $90

Most expensive AWS cost!
```

### Optimization
```
1. Use CloudFront (87% cheaper)
   - Caching reduces origin requests
   - Closer to users = faster
   
2. Compress data
   - 10MB → 2MB (80% savings)
   - Use gzip compression
   
3. Intelligent design
   - Users download only needed data
   - Pagination instead of full dump
   - Small previews before full download
```

### Example: Video Website
```
WITHOUT CloudFront:
- 1000 users × 500MB = 500GB/month
- 500GB × $0.09 = $45/month

WITH CloudFront:
- Cache hits: 80% cached (only 20% from origin)
- 100GB × $0.09 = $9/month (origin)
- CloudFront: ~$5/month
- Total: ~$14/month
- SAVINGS: 70%
```

## Database I/O Costs

### RDS: Storage and I/O
```
Monthly cost = Database size × $0.10/GB + I/O operations

Example:
Database: 100GB = $10/month
I/O operations: 1M/day = $1/day = $30/month
Total: $40/month

The I/O can exceed storage!
```

### Optimization
```
1. Use SSD vs HDD
   - Same cost but much faster
   
2. Optimize queries
   - Slow queries = more I/O
   - Add indexes
   - Avoid full table scans
   
3. Use RDS Read Replicas for reporting
   - Separate heavy reads from production
   - Doesn't slow down main database
```

## EBS Snapshot Costs

### Snapshots Add Up
```
1 snapshot = $0.05
100 old snapshots = $5/month
10,000 forgotten snapshots = $500/month!
```

### Cleanup
```
1. List old snapshots
   aws ec2 describe-snapshots --owner-ids self

2. Delete unused
   aws ec2 delete-snapshot --snapshot-id snap-123456

3. Automate with Lifecycle Manager
   Data Lifecycle Manager → Create lifecycle policy
   Auto-delete after X days
```

## Network Address Translation (NAT)

### NAT Gateway Costs
```
Cost: $32/month per NAT gateway
Plus: $0.045/GB data processed

Common mistake:
- Create NAT gateway in each AZ "just in case"
- Each sits idle but costs $32/month
- 3 AZ × $32 = $96/month
```

### When Needed
```
Use NAT gateway if:
✓ Private instances need internet access
✓ Cannot use NAT instance (performance)

Otherwise:
✗ Delete it (costs money sitting idle)
```

## Elastic IPs

### Unassociated IP Cost
```
Cost: $0.005/hour ($3.60/month) when not in use

Common mistake:
- Allocate Elastic IP "just in case"
- Don't attach to instance
- Costs money unused

Attached to instance: FREE
Not attached: $3.60/month
```

### Cleanup
```
EC2 → Addresses
Look for: "Associated" vs "Not associated"
Release all "Not associated" IPs
```

## VPC Endpoints

### Data Processing Cost
```
Gateway endpoint (S3, DynamoDB): FREE

Interface endpoint: $7.20/month per AZ
Plus: $0.01/GB data processed

Example:
2 AZ × $7.20 = $14.40/month
Plus 100GB × $0.01 = $1/month
Total: $15.40/month (for one endpoint!)
```

### When to Use
```
Use VPC endpoints if:
✓ Private instances need AWS service access
✓ Want encrypted traffic

Otherwise:
✗ Remove it (costs money)
```

## Application Load Balancer (ALB)

### Cost Breakdown
```
Base: $16.20/month
Per LCU (Load Capacity Unit): $1.44/month

LCU includes:
- 25 new connections/second
- 3,000 connections/minute
- 1GB/hour processed

Light usage: ~$16.20/month
Heavy usage: Can be $50+/month
```

### Optimization
```
1. Delete unused load balancers
2. Use Classic Load Balancer if simpler
3. Group multiple services on one ALB
4. Remove unhealthy targets (extra checks)
```

## Lambda Costs (Surprising!)

### Concurrency
```
Default: 1000 concurrent executions

Problem:
- Lambda goes viral/traffic spike
- 10,000 concurrent invocations
- Error: "too many concurrent executions"
- BUT you can request higher limit

Solution:
- Request account limit increase
- Or use Reserved Concurrency (pay guaranteed minimum)
```

### Storage in /tmp
```
Lambda has 512MB /tmp storage

Problem:
- Lambda stores 1GB file in /tmp
- Error: "No space on disk"
- Solution: Don't store large files locally
- Use S3 instead

Layer size limit: 250MB total
Deployment package: 50MB
```

### Duration Charges
```
Cost: $0.0000166667 per GB-second

Example:
128MB function for 1 second = $0.0000020833
1M invocations × 1 second = $0.02/month

But if function is slow:
128MB for 5 seconds:
1M invocations × 5 seconds = $0.08/month (4x more!)

Optimization:
- Increase memory (faster CPU, higher cost)
- Optimize code (shorter duration)
- Cache results (fewer invocations)
```

## CloudWatch Logs

### Log Storage Cost
```
Cost: $0.50/GB ingested
Plus: $0.03/GB stored per month

Example:
1GB logs/day = 30GB/month
Ingestion: 30GB × $0.50 = $15/month
Storage: 30GB × $0.03 = $0.90/month
Total: ~$16/month

But logs can grow fast!
Misconfigured app dumping logs:
100GB logs/day = 3TB/month
Ingestion: 3TB × $0.50 = $1500/month!
```

### Cleanup
```
1. Set retention: 7-30 days (not unlimited)
   CloudWatch Logs → Log Group → Edit retention
   
2. Filter logs
   Only send important logs to CloudWatch
   Send debug logs elsewhere
   
3. Use S3 export
   Export old logs to S3
   Cheaper to store ($0.023/GB/month)
```

## Reserved Capacity Costs

### Multi-AZ Deployment
```
Cost: 2× the single-AZ cost
Example: RDS from $15 → $30/month

Use if:
✓ High availability critical
✓ Can afford 2×

Otherwise:
✗ Single-AZ is cheaper (but less reliable)
```

## Hidden Costs Checklist

🔴 **CRITICAL**
- ✅ Monitor data transfer (biggest cost)
- ✅ Delete unused snapshots
- ✅ Remove unattached Elastic IPs

🟠 **HIGH**
- ✅ Review NAT gateway usage
- ✅ Check load balancer necessity
- ✅ Monitor Lambda duration

🟡 **IMPORTANT**
- ✅ Set CloudWatch log retention
- ✅ Review VPC endpoint usage
- ✅ Check for orphaned resources

## Cost Visibility

### Setup Cost Alerts
```
Billing → Create Budget
Category: Hidden costs
Threshold: $50/month increase
Action: Alert if spending unusual
```

### Monthly Review
```
1. Check data transfer costs
2. Review unused resources
3. Look for spikes
4. Optimize top 3 costs
```

## 📖 Related Resources

- [Cost Optimization](cost-optimization.md)
- [Billing Alerts](billing-alerts.md)
- [CloudWatch Logs](../tier-2-common/cloudwatch/README.md)
- [Cost Explorer](https://console.aws.amazon.com/cost-management/)