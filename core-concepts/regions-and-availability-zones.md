# Regions and Availability Zones 🌍

Understanding AWS's global infrastructure.

## What are Regions?

**Think of it as:** AWS data centers around the world

```
Region = Geographic area

Examples:
- us-east-1 (N. Virginia)
- eu-west-1 (Ireland)
- ap-southeast-1 (Singapore)

Each region:
- Completely independent
- Multiple data centers
- Low-latency connections within
```

## What are Availability Zones?

**Think of it as:** Separate buildings in same city

```
Availability Zone (AZ) = Data center

Example (us-east-1):
- us-east-1a
- us-east-1b
- us-east-1c
- us-east-1d
- us-east-1e
- us-east-1f

Each AZ:
- Physically separate
- Own power/cooling
- Connected by fiber
- < 1ms latency between AZs
```

## Visual Hierarchy

```
AWS Global Infrastructure
|
+-- Region: us-east-1 (N. Virginia)
|   |
|   +-- AZ: us-east-1a [Data Center 1]
|   +-- AZ: us-east-1b [Data Center 2]
|   +-- AZ: us-east-1c [Data Center 3]
|   +-- AZ: us-east-1d [Data Center 4]
|
+-- Region: eu-west-1 (Ireland)
|   |
|   +-- AZ: eu-west-1a [Data Center 1]
|   +-- AZ: eu-west-1b [Data Center 2]
|   +-- AZ: eu-west-1c [Data Center 3]
|
+-- Region: ap-southeast-1 (Singapore)
    |
    +-- AZ: ap-southeast-1a [Data Center 1]
    +-- AZ: ap-southeast-1b [Data Center 2]
    +-- AZ: ap-southeast-1c [Data Center 3]
```

## AWS Regions Worldwide

### North America
```
us-east-1      N. Virginia      (6 AZs) ⭐ Oldest, most services
us-east-2      Ohio             (3 AZs)
us-west-1      N. California    (3 AZs)
us-west-2      Oregon           (4 AZs)
ca-central-1   Canada           (3 AZs)
```

### Europe
```
eu-west-1      Ireland          (3 AZs) ⭐ Popular
eu-west-2      London           (3 AZs)
eu-west-3      Paris            (3 AZs)
eu-central-1   Frankfurt        (3 AZs)
eu-north-1     Stockholm        (3 AZs)
eu-south-1     Milan            (3 AZs)
```

### Asia Pacific
```
ap-southeast-1 Singapore        (3 AZs) ⭐ Popular in Asia
ap-southeast-2 Sydney           (3 AZs)
ap-northeast-1 Tokyo            (4 AZs)
ap-northeast-2 Seoul            (4 AZs)
ap-south-1     Mumbai           (3 AZs)
ap-east-1      Hong Kong        (3 AZs)
```

### South America
```
sa-east-1      São Paulo        (3 AZs)
```

### Middle East & Africa
```
me-south-1     Bahrain          (3 AZs)
af-south-1     Cape Town        (3 AZs)
```

**Total:** 30+ regions, 90+ AZs

## Why Regions Matter

### 1. Latency
```
User location → Nearest region = Faster

Example:
- User in London
- App in us-east-1: ~80ms latency
- App in eu-west-2: ~5ms latency

16x faster!
```

### 2. Compliance/Data Residency
```
Legal requirements:

GDPR (Europe):
- EU data must stay in EU
- Use eu-west-1 or eu-central-1

China:
- Data must stay in China
- Use special China regions

Australia:
- Government data in Australia
- Use ap-southeast-2
```

### 3. Pricing
```
Same service, different cost!

EC2 t3.medium:
- us-east-1: $0.0416/hour ($30/month)
- eu-west-1: $0.0456/hour ($33/month)
- ap-southeast-1: $0.0504/hour ($36/month)

Cheapest → Most expensive: 20% difference!
```

### 4. Service Availability
```
New services launch in stages:

1. us-east-1 (first, always)
2. us-west-2, eu-west-1 (few weeks later)
3. Other major regions (months later)
4. Smaller regions (varies)

Check availability before choosing!
```

### 5. Disaster Recovery
```
Multi-region = Ultimate redundancy

Scenario:
- Primary: us-east-1
- Disaster: Entire region down
- Backup: us-west-2 takes over

App stays online!
```

## Why Availability Zones Matter

### High Availability
```
Spread across AZs = Resilience

Single AZ:
- AZ fails → App down ❌

Multi-AZ:
- AZ fails → Other AZ serves ✅

Example:
- Web servers: us-east-1a + us-east-1b
- Database: Multi-AZ RDS
- Load balancer: Spans all AZs
```

### Real-World Example
```
2011: EBS outage in us-east-1

Single-AZ apps:
- Down for 12+ hours ❌

Multi-AZ apps:
- No downtime ✅

Lesson: Always use multiple AZs!
```

## Choosing a Region

### Decision Factors

**1. User Location (Most Important)**
```
Users in USA → us-east-1 or us-west-2
Users in Europe → eu-west-1
Users in Asia → ap-southeast-1

Closer = Faster
```

**2. Compliance**
```
EU users → EU region (GDPR)
China users → China regions
Government → GovCloud
```

**3. Cost**
```
Budget tight?
- Use us-east-1 (cheapest)

Example savings:
- 1000 hours EC2
- us-east-1: $42
- ap-south-1: $52
- Savings: $10/month
```

**4. Service Availability**
```
Need specific service?
- Check service availability
- Example: Some ML services only in us-east-1
```

**5. Disaster Recovery**
```
Mission critical?
- Primary: Closest region
- Backup: Another region
```

### Decision Matrix

```
+-------------------+------------+------------+------------+
| Factor            | us-east-1  | eu-west-1  | ap-south-1 |
+-------------------+------------+------------+------------+
| US users          | ⭐⭐⭐        | ⭐         | ⭐         |
| EU users          | ⭐         | ⭐⭐⭐        | ⭐         |
| Asia users        | ⭐         | ⭐         | ⭐⭐⭐        |
| Cost              | ⭐⭐⭐        | ⭐⭐         | ⭐⭐         |
| Services          | ⭐⭐⭐        | ⭐⭐⭐        | ⭐⭐         |
| Stability         | ⭐⭐         | ⭐⭐⭐        | ⭐⭐         |
+-------------------+------------+------------+------------+
```

## Multi-AZ Architecture

### Pattern 1: Load Balanced Web App
```
[Application Load Balancer] (spans all AZs)
         /              \
  [us-east-1a]      [us-east-1b]
  Web Server 1      Web Server 2
         \              /
      [RDS Multi-AZ]
      Primary: 1a
      Standby: 1b

✅ One AZ fails → App still works!
```

### Pattern 2: Auto Scaling
```
Auto Scaling Group:
- Min: 2 instances
- Desired: 4 instances
- Max: 10 instances

Distribution:
- 2 in us-east-1a
- 2 in us-east-1b

✅ Automatic failover
```

### Pattern 3: Database Replication
```
RDS Multi-AZ:
- Primary: us-east-1a
- Standby: us-east-1b (automatic)
- Failover: < 60 seconds

Aurora:
- Writer: us-east-1a
- Readers: us-east-1a, us-east-1b, us-east-1c
- Even better!
```

## Multi-Region Architecture

### Pattern 1: Active-Passive
```
Primary Region (us-east-1):
- Handles all traffic
- Full infrastructure

Backup Region (us-west-2):
- Standby infrastructure
- Data replicated
- Activated if primary fails

Cost: ~150% of single region
```

### Pattern 2: Active-Active
```
US Region (us-east-1):
- Serves US users

EU Region (eu-west-1):
- Serves EU users

Route 53:
- Geo-routing
- Automatic failover

Cost: ~200% of single region
Performance: 2x better (local to users)
```

### Pattern 3: Global CDN
```
Origin: us-east-1
CloudFront: Edge locations worldwide

Users connect to nearest edge:
- London user → London edge
- Tokyo user → Tokyo edge
- All serve same content

Cost: Minimal
Performance: Excellent
```

## Latency Between Regions

### Approximate Latency
```
From us-east-1 to:
- us-west-2: 60ms
- eu-west-1: 80ms
- ap-southeast-1: 200ms
- ap-northeast-1: 150ms
- sa-east-1: 120ms

From eu-west-1 to:
- us-east-1: 80ms
- ap-southeast-1: 160ms
- ap-northeast-1: 240ms

Important for:
- Multi-region apps
- Data replication
- API calls
```

## Region & AZ Costs

### Region Differences
```
EC2 t3.medium ($/month):

us-east-1:      $30 (baseline)
us-west-2:      $30 (same)
eu-west-1:      $33 (+10%)
eu-central-1:   $33 (+10%)
ap-southeast-1: $36 (+20%)
ap-northeast-1: $38 (+27%)
sa-east-1:      $45 (+50%!)

Choose wisely for cost savings!
```

### AZ Data Transfer
```
Within same AZ: FREE
Between AZs: $0.01/GB
Between regions: $0.02/GB

Example:
- 1TB between AZs: $10
- 1TB between regions: $20

Design apps to minimize cross-AZ traffic
```

## Edge Locations

### What are Edge Locations?
```
Not full regions
CDN cache points
CloudFront & Route 53

400+ edge locations worldwide

Major cities:
- New York, Los Angeles, London
- Paris, Tokyo, Sydney
- Mumbai, São Paulo, etc.

Benefit: Content closer to users
```

### CloudFront Example
```
Origin: S3 in us-east-1
User: In London

Without CloudFront:
- Request → us-east-1 (80ms)
- Response → London (80ms)
- Total: 160ms

With CloudFront:
- Request → London edge (5ms)
- (First time: cache from us-east-1)
- Total: 5ms

32x faster!
```

## Best Practices

### 1. Choose Right Region
```
✅ Closest to users
✅ Meets compliance
✅ Has required services
✅ Consider cost

❌ Don't randomly pick
❌ Don't assume all regions same
```

### 2. Always Multi-AZ
```
✅ Spread across 2+ AZs
✅ Use Multi-AZ RDS
✅ Load balancer in all AZs
✅ Auto Scaling across AZs

❌ Don't use single AZ for production
```

### 3. Test Failover
```
✅ Simulate AZ failure
✅ Verify automatic failover
✅ Measure recovery time
✅ Document procedures

Test before you need it!
```

### 4. Monitor Latency
```
✅ CloudWatch metrics
✅ Route 53 health checks
✅ Synthetic monitoring
✅ Real user monitoring

Know your performance!
```

### 5. Plan for Growth
```
✅ Start single region
✅ Always multi-AZ
✅ Add regions as you grow
✅ Use CloudFront early

Scale globally when needed
```

## Common Mistakes

### 1. Single AZ Deployment
```
❌ All resources in one AZ
❌ No redundancy
❌ AZ fails → App down

✅ Solution: Deploy across 2+ AZs
```

### 2. Wrong Region
```
❌ US app in ap-southeast-1
❌ High latency
❌ Unhappy users

✅ Solution: Region close to users
```

### 3. Ignoring Compliance
```
❌ EU data in US region
❌ GDPR violation
❌ Huge fines

✅ Solution: Check compliance requirements
```

### 4. Not Testing Failover
```
❌ Multi-AZ setup
❌ Never tested
❌ Fails when needed

✅ Solution: Regular failover tests
```

## Region & AZ Checklist

🔴 **Planning:**
- ✅ Identify user locations
- ✅ Check compliance requirements
- ✅ Verify service availability
- ✅ Compare costs
- ✅ Choose region

🟠 **Deployment:**
- ✅ Deploy to 2+ AZs
- ✅ Enable Multi-AZ RDS
- ✅ Load balancer spans AZs
- ✅ Auto Scaling across AZs

🟡 **Monitoring:**
- ✅ Monitor latency
- ✅ Health checks configured
- ✅ Failover tested
- ✅ Recovery procedures documented

## Quick Reference

### Region Codes
```
us-east-1      = N. Virginia (cheapest, most services)
us-west-2      = Oregon
eu-west-1      = Ireland (Europe default)
ap-southeast-1 = Singapore (Asia default)

Always check: Which region am I in?
```

### AZ Naming
```
Format: [region][letter]

Examples:
- us-east-1a
- eu-west-1b
- ap-southeast-1c

⚠️ AZ letters different per account!
Your us-east-1a ≠ My us-east-1a
```

### Latency Targets
```
Same AZ:      < 1ms
Same region:  1-2ms
Nearby region: 60-100ms
Far region:   150-250ms
Global:       Use CloudFront!
```

## 📖 Next Steps

1. [VPC Fundamentals](vpc-fundamentals.md)
2. [Pricing Models](pricing-models.md)
3. [Service Limits](service-limits-quotas.md)

## Related Resources

- [Disaster Recovery](../best-practices/disaster-recovery.md)
- [Performance Optimization](../best-practices/performance-optimization.md)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)