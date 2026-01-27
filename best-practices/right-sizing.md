# Right-Sizing AWS Resources 📊

Choosing the correct instance type and size for your workload.

## What is Right-Sizing?

**Problem:**
```
Choosing instance size is hard
- Too big: Waste money (70-80% idle)
- Too small: Slow, bottleneck, outages

Waste percentage:
- 5-10%: Acceptable
- 20%+: Too much!
- 80%+: Massive waste!
```

**Solution: Right-Sizing**
- Choose instance that matches actual needs
- Measure, don't guess
- Adjust as usage changes

## Common Right-Sizing Mistakes

### Mistake 1: Starting Too Big

**Problem:**
```
"Let's use t3.xlarge to be safe"

Actual usage:
- CPU: 5%
- Memory: 10%
- Cost: $50/month
- Wasted: 90%!
```

**Solution:**
```
Start small (t3.micro/small)
Monitor for 1-2 weeks
Scale up only if needed

Result: $10/month instead of $50/month!
```

### Mistake 2: Not Monitoring

**Problem:**
```
Launch instance
Never check metrics
3 years later: Still t3.large (original guess)

Actual needs: t3.small
Wasted: $300+ annually
```

**Solution:**
```
Monitor monthly
Adjust quarterly
Review annually
```

## Right-Sizing Process

### Step 1: Establish Baseline

**Measure for 2 weeks:**
```
CloudWatch Metrics
├─ CPU Utilization
├─ Memory Usage
├─ Network In/Out
├─ Disk I/O
└─ Custom metrics
```

**Record:**
- Average usage
- Peak usage (95th percentile)
- Off-peak usage

### Step 2: Identify Peak Vs. Baseline

**Example:**
```
CPU Utilization:
- Average: 15%
- Peak (95th percentile): 65%
- Max (100th percentile): 95%

Memory:
- Average: 8GB (50% of 16GB)
- Peak: 14GB (88% of 16GB)
```

### Step 3: Calculation

**Ideal Usage:**
- CPU: 60-80% (sweet spot)
- Memory: 70-85% (leaves headroom)
- Network: 20-50% (leaves headroom)

**Formula:**
```
Required CPU = Peak CPU / 0.75 (target utilization)
Required Memory = Peak Memory / 0.80
```

**Example:**
```
Peak CPU: 65%
Required: 65% / 0.75 = 87% of t3.medium
→ Keep t3.medium (CPU not bottleneck)

Peak Memory: 14GB
Required: 14GB / 0.80 = 17.5GB
→ Need t3.xlarge (16GB) or r5.large (16GB)
```

## Instance Type Selection

### General Purpose (t3, t4g)
**Use for:** Mixed workloads
```
t3.micro:     1 vCPU,  1GB RAM  - Free tier
t3.small:     2 vCPU,  2GB RAM  - ~$9/month
t3.medium:    2 vCPU,  4GB RAM  - $17/month
t3.large:     2 vCPU,  8GB RAM  - $35/month
t3.xlarge:    4 vCPU,  16GB RAM - $70/month
t3.2xlarge:   8 vCPU,  32GB RAM - $140/month
```

**Good for:** Web servers, apps

### Memory Optimized (r5, r6i)
**Use for:** Databases, caches
```
r5.large:     2 vCPU,  16GB RAM  - $100/month
r5.xlarge:    4 vCPU,  32GB RAM  - $200/month
r5.2xlarge:   8 vCPU,  64GB RAM  - $400/month
```

**Good for:** RDS, Redis, data processing

### Compute Optimized (c5, c6i)
**Use for:** CPU-intensive
```
c5.large:     2 vCPU,  4GB RAM  - $85/month
c5.xlarge:    4 vCPU,  8GB RAM  - $170/month
c5.2xlarge:   8 vCPU,  16GB RAM - $340/month
```

**Good for:** Video encoding, ML, scientific computing

## AWS Compute Optimizer

### Automatic Recommendations

```
AWS Console → Compute Optimizer → Analyze

Recommendations:
- EC2 instances: Too big? Recommends smaller
- RDS instances: Cost analysis
- Lambda: Memory recommendation

One-click implement
```

### Example Recommendation

```
Current: t3.large ($70/month)
Usage: 10% CPU, 20% memory

Recommendation: t3.medium ($17/month)
Savings: 76% ($53/month)
Performance Impact: None (still has headroom)

One-click deploy
```

## Cost Savings Examples

### Web Server
```
Before: t3.xlarge ($70/month) - 10% CPU
Recommendation: t3.small ($9/month)

Annual Savings: $732/month × 12 = $8,784 per instance
For 100 instances: $878,400/year!
```

### Database
```
Before: db.r5.2xlarge ($400/month) - 30% CPU, 40% memory
Recommendation: db.r5.large ($100/month)

Annual Savings: $3,600/year per instance
For 10 instances: $36,000/year!
```

### Lambda
```
Before: 1024MB memory, 10 second duration
1M invocations: 1M × 10 = 10M GB-seconds = $0.17/month

After: 256MB memory, 2 second duration (optimized)
1M invocations: 1M × 0.5 = 0.5M GB-seconds = $0.008/month

Savings: 95%!
```

## Right-Sizing Checklist

🔴 **CRITICAL**
- ✅ Baseline metrics established
- ✅ CloudWatch monitoring enabled
- ✅ Peak usage identified

🟠 **HIGH**
- ✅ Used Compute Optimizer
- ✅ Reviewed recommendations
- ✅ Implemented changes

🟡 **IMPORTANT**
- ✅ Auto Scaling configured
- ✅ Right-sizing review scheduled (quarterly)
- ✅ Cost trends monitored

## 📖 Related Resources

- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [EC2 Instance Types](../tier-1-foundational/ec2/README.md)
- [Cost Optimization](cost-optimization.md)
- [Performance Optimization](performance-optimization.md)