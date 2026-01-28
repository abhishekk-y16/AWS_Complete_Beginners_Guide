# Lambda Pricing 💰

Comprehensive breakdown of AWS Lambda costs with optimization strategies.

## Pricing Components

### Invocations

```
Cost: $0.20 per 1,000,000 invocations
Free: First 1M invocations per month (every month)

Example calculation:
├─ 500,000 invocations/month
├─ Free tier covers: 1,000,000/month
├─ Cost: $0 (within free tier)
└─ Annual cost: $0

Example 2:
├─ 10,000,000 invocations/month
├─ Free tier: 1,000,000
├─ Billable: 9,000,000
├─ Cost: 9,000,000 × $0.20/1M = $1.80
└─ Annual cost: $21.60

Breakdown by volume:
├─ 100K invocations/month: $0 (free tier)
├─ 1M invocations/month: $0 (free tier)
├─ 10M invocations/month: $1.80
├─ 100M invocations/month: $18
└─ 1B invocations/month: $180
```

### Compute Duration (GB-seconds)

```
Cost: $0.0000166667 per GB-second
Formula: Memory (GB) × Duration (seconds) × Invocations

Memory tiers (128MB - 10,240MB):
├─ 128MB (0.125GB): $0.0000020833/second
├─ 256MB (0.25GB): $0.0000041667/second
├─ 512MB (0.5GB): $0.0000083333/second
├─ 1,024MB (1GB): $0.0000166667/second
├─ 1,769MB: Most cost-effective (price increase changes)
└─ 10,240MB (10GB): $0.000166667/second

Example 1: Small function
├─ Memory: 128MB
├─ Duration: 100ms per invocation
├─ Frequency: 10,000 invocations/month
├─ Calculation: 0.125GB × 0.1sec × 10,000 = 125 GB-seconds
├─ Cost: 125 × $0.0000166667 = $0.0208
└─ Annual: ~$0.25

Example 2: Medium function
├─ Memory: 512MB
├─ Duration: 1 second per invocation
├─ Frequency: 1,000,000 invocations/month
├─ Calculation: 0.5GB × 1sec × 1,000,000 = 500,000 GB-seconds
├─ Cost: 500,000 × $0.0000166667 = $8.33
└─ Annual: ~$100

Example 3: Large function
├─ Memory: 3,008MB
├─ Duration: 5 seconds per invocation
├─ Frequency: 100,000 invocations/month
├─ Calculation: 3.008GB × 5sec × 100,000 = 1,504,000 GB-seconds
├─ Cost: 1,504,000 × $0.0000166667 = $25.07
└─ Annual: ~$300
```

## Real-World Cost Examples

### Web API (Medium Traffic)

```
Scenario: REST API serving web/mobile app

Metrics:
├─ Requests: 10M/month = 10M invocations
├─ Avg response time: 200ms
├─ Memory: 512MB (good for Node.js/Python)
└─ Concurrent users: 1,000

Cost calculation:

1. Invocation cost:
   ├─ Free: 1,000,000
   ├─ Billable: 9,000,000
   └─ Cost: 9,000,000 × $0.20/1M = $1.80

2. Compute cost:
   ├─ Duration: 10M × 0.2sec × 0.5GB = 1M GB-seconds
   ├─ Cost: 1,000,000 × $0.0000166667 = $16.67
   └─ Subtotal: $16.67

3. API Gateway cost:
   ├─ 10M requests × $0.0035 = $35
   └─ Subtotal: $35

4. Data transfer (optional):
   ├─ 10M requests × 10KB avg response = 100GB
   ├─ First 1GB free, next 99GB × $0.09 = $8.91
   └─ Subtotal: $8.91

Total monthly: $1.80 + $16.67 + $35 + $8.91 = $62.38
Total annual: ~$748

Comparison to alternatives:
├─ EC2 (t3.large): $0.1104/hour × 730 = $80.59/month = $967/year
├─ Lambda savings: 23% cheaper
├─ Plus: No ops overhead, auto-scaling
└─ Verdict: Lambda better for this workload
```

### Batch Processing (Scheduled)

```
Scenario: Daily report generation

Metrics:
├─ Schedule: 2 AM UTC daily (30 invocations/month)
├─ Duration: 30 seconds per run
├─ Memory: 1,024MB
└─ Storage: S3 (separate cost)

Cost calculation:

1. Invocations:
   ├─ 30/month (all free tier)
   └─ Cost: $0

2. Compute:
   ├─ 30 runs × 30sec × 1GB = 900 GB-seconds
   ├─ Cost: 900 × $0.0000166667 = $0.015
   └─ Subtotal: $0.015

3. S3 API calls:
   ├─ 30 PUT operations × $0.005/1K = $0.00015
   └─ Subtotal: $0.00015

Total monthly: ~$0.015
Total annual: ~$0.18

Comparison:
├─ Scheduled EC2 instance: $0.11/hour = $80/month = $960/year
├─ Lambda savings: 99.98% cheaper!
└─ Verdict: Lambda is massive win for scheduled tasks
```

## Memory Selection Impact

```
Test: Same function, different memory tiers
Function: Image resize (1,000 invocations)
Target memory: Find sweet spot

128MB:
├─ Duration: 15 seconds (slow, CPU throttled)
├─ Cost: 0.125GB × 15sec × 1000 = 1,875 GB-sec = $0.0313
└─ Verdict: Cheap but very slow

512MB:
├─ Duration: 4 seconds (good balance)
├─ Cost: 0.5GB × 4sec × 1000 = 2,000 GB-sec = $0.0333
└─ Verdict: Only $0.002 more but 3.75x faster!

1,024MB:
├─ Duration: 2 seconds (fast)
├─ Cost: 1GB × 2sec × 1000 = 2,000 GB-sec = $0.0333
└─ Verdict: Same cost as 512MB! (CPU scales with memory)

3,008MB:
├─ Duration: 1 second (very fast)
├─ Cost: 3GB × 1sec × 1000 = 3,000 GB-sec = $0.05
└─ Verdict: 50% more cost for 4x speed

Conclusion:
├─ Don't pick minimum memory (trade-off not worth it)
├─ Find sweet spot: 512-1,024MB for most workloads
├─ Higher memory only if duration improvement > cost increase
└─ Use CloudWatch to measure actual duration
```

## Cost Optimization Strategies

### 1. Right-Size Memory

```
Action: Increase memory if duration drops significantly

Before (128MB):
├─ Duration: 10 seconds
├─ Cost: 0.125GB × 10 × 1,000 = 1,250 GB-sec = $0.0208

After (512MB):
├─ Duration: 3 seconds
├─ Cost: 0.5GB × 3 × 1,000 = 1,500 GB-sec = $0.025
├─ Cost increase: $0.0042
├─ Speed improvement: 70%
└─ Benefit: Much faster (worth it!)
```

### 2. Use Layers for Dependencies

```
Without layers:
├─ Package size: 50MB
├─ Cold start: 2 seconds
├─ First invocation: Unzip + load
└─ Cost per cold start: Higher (paying for unzip time)

With layers:
├─ Function code: 5MB
├─ Layer (dependency): 45MB (separate)
├─ Cold start: 0.5 seconds
├─ Layer cached separately
└─ Cost per cold start: Lower
```

### 3. Implement Connection Pooling

```
Without pooling:
├─ Each invocation creates DB connection
├─ Overhead: 500ms per invocation
├─ 1,000 invocations = 500 extra seconds
├─ Cost: 500 GB-sec × 0.0000166667 = $0.0083

With pooling (RDS Proxy):
├─ Reuse connections across invocations
├─ Overhead: 50ms per invocation
├─ 1,000 invocations = 50 extra seconds
├─ Cost: 50 GB-sec × 0.0000166667 = $0.00083
└─ Savings: 90% reduction!
```

### 4. Batch Processing

```
Without batching:
├─ Process 1 message per invocation
├─ 1,000 messages = 1,000 invocations
├─ Invocation cost: $0.20
└─ Total: Very high

With batching (SQS batch size = 100):
├─ Process 100 messages per invocation
├─ 1,000 messages = 10 invocations
├─ Invocation cost: $0.002
└─ Savings: 99% reduction in invocation cost!
```

## Free Tier

```
Every month, you get:

1. 1,000,000 free invocations
   ├─ Equivalent to:
   │  ├─ 33,000 daily invocations
   │  ├─ 1,380 per hour
   │  └─ 23 per minute (continuous)
   └─ No expiration (every month)

2. 400,000 GB-seconds free compute
   ├─ Example: 512MB memory
   │  ├─ = 800,000 seconds of compute
   │  ├─ = 222 hours of continuous execution
   │  └─ Per month!
   └─ Example: 1,024MB memory
      ├─ = 400,000 seconds of compute
      ├─ = 111 hours of continuous execution
      └─ Per month!

Example workload within free tier:
├─ 1M API requests/month = $0
├─ 0.1s average duration = $0
├─ 512MB memory = $0
└─ Total: $0 (completely free!)
```

## Cost Tracking

### CloudWatch Metrics to Monitor

```
Key metrics:
├─ Duration (ms) - How long functions run
├─ Invocations - How many times triggered
├─ Errors - Failed executions (waste money if retried)
├─ Throttles - Concurrent limit exceeded (need to increase)
└─ ConcurrentExecutions - Current running functions
```

### AWS Billing Dashboard

```
Check monthly:
├─ AWS Cost Explorer
│  ├─ Filter by service: Lambda
│  ├─ View by: Invocations, Compute
│  └─ Compare month-over-month
└─ Set budget alerts
   ├─ Alert if Lambda costs > $50/month
   ├─ Prevents surprises
   └─ Review daily
```

## Best Practices

✅ Monitor duration (CloudWatch)
✅ Find optimal memory size
✅ Use layers for shared dependencies
✅ Implement connection pooling
✅ Batch process events
✅ Clean up old versions
✅ Set CloudWatch alarms for cost
✅ Use free tier effectively
✅ Test performance before production
✅ Regular cost reviews

## Next Steps

→ [Use Cases](./use-cases.md) - Real-world scenarios
→ [Triggers](./triggers.md) - Event sources
→ [First Lambda Function](./first-lambda-function.md) - Hands-on