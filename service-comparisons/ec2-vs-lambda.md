# EC2 vs Lambda Comparison

Choosing between running code on EC2 or Lambda.

## Quick Decision Matrix

| Feature | EC2 | Lambda |
|---------|-----|--------|
| **Best For** | Long-running apps, complex infrastructure | Event-driven, short tasks |
| **Setup Time** | Hours (OS, software, config) | Minutes (upload code) |
| **Cost Model** | Per hour regardless of usage | Per invocation + execution time |
| **Language Support** | Any | Node, Python, Java, Go, .NET, Ruby |
| **Execution Time** | Unlimited | 15 minutes max |
| **Startup Time** | ~1-5 minutes | ~100ms-3s (cold start) |
| **Scalability** | Manual or Auto Scaling | Automatic (1000s concurrently) |
| **Management** | OS patches, security, updates required | AWS handles everything |
| **Cost (idle)** | $$$  per month | Free (paying for nothing) |
| **Cost (busy)** | Same per hour | Pay only for what you use |

## EC2 Advantages ✓

**1. No time limits**
- Run jobs for hours or days
- Lambda limited to 15 minutes

**2. Persistence**
- Keep state between requests
- Local file storage persists
- Long-running connections

**3. Full control**
- Install any software
- Configure OS directly
- Custom network setup

**4. Cost predictable**
- Same cost whether running 1% or 100% capacity
- Good for sustained workloads

**5. Complex infrastructure**
- Multi-container orchestration
- Complex network topology
- Advanced security groups

## Lambda Advantages ✓

**1. Zero management**
- No OS to maintain
- No patches or updates
- Just upload code

**2. Auto-scaling**
- Handles 1 request/second or 10,000 automatically
- No capacity planning

**3. Cost efficient (variable workloads)**
- Pay only when code runs
- Idle time = $0
- Perfect for unpredictable traffic

**4. Built-in logging**
- CloudWatch logs automatically
- Easy debugging
- Performance monitoring built-in

**5. Integrations**
- Trigger from 60+ AWS services
- Event-driven architecture
- Microservices friendly

## Detailed Comparison

### Cost Analysis

**Scenario 1: Steady 24/7 web server**

EC2:
- t3.small instance: ~$10/month
- Bandwidth: ~$10/month
- Total: ~$20/month

Lambda (equivalent traffic):
- 2.6M invocations/month (100/sec)
- 1 second per request
- Cost: $0.20 (invocations) + $10.50 (execution) = ~$10.70/month
- **Lambda wins: 46% cheaper**

**Scenario 2: Occasional reports (100 runs/month)**

EC2:
- t3.small: $20/month running 24/7
- (Wastes capacity 99%+ of the time)

Lambda:
- 100 invocations × $0.0000002 = $0.00002
- 100 minutes execution × $0.0000167 = $0.00167
- Total: ~$0.002/month
- **Lambda wins: 10,000x cheaper**

### Use Cases

**Choose EC2 if you:**
- Run continuously (never stops)
- Need very high throughput (1000+ requests/sec)
- Need persistent state between requests
- Run GPU workloads
- Need custom runtime environment
- Run processes longer than 15 minutes
- Example: Web server, database, game server

**Choose Lambda if you:**
- Triggered by events (S3 upload, API call, schedule)
- Unpredictable traffic patterns
- Want zero operations work
- Processing under 15 minutes
- Example: Image resizing, email notifications, data processing

## Architecture Patterns

### EC2 Pattern: Web Server
```
Internet → Load Balancer → EC2 instances → Database
                ↑
         (Auto Scaling)
```
- Always running
- Handles user traffic
- Scales up/down based on CPU

### Lambda Pattern: Event Processing
```
S3 Upload → Lambda (trigger) → Process → Store Result
    ↓
  Log to CloudWatch
```
- Triggered by event
- Runs once
- Scales automatically

## Migration Path

**If you have EC2 app, consider Lambda if:**
1. ✓ Stateless (no stored session on server)
2. ✓ Runs under 15 minutes
3. ✓ Can be triggered by event
4. ✓ Supports Lambda runtime

**Example migration:**
```
OLD: EC2 runs 24/7 accepting API requests
NEW: API Gateway → Lambda (triggered by HTTP request)
    - Same functionality
    - Only pay when used
    - No operations
```

## Hybrid Approach

**Use both:**

```
Browser → CloudFront → API Gateway → Lambda → EC2 (background job)
```

- Lambda for quick API responses
- EC2 for long-running processing
- Best of both worlds

Example:
- Lambda: Process order (100ms)
- EC2 worker: Generate report (takes 30 minutes)
- Lambda triggers EC2 job via SQS queue

## Performance Comparison

| Metric | EC2 | Lambda |
|--------|-----|--------|
| Startup | 1-5 minutes | 100ms-3s |
| Request response time | <100ms | 1-10ms (excluding code) |
| Max execution time | Unlimited | 15 minutes |
| Memory (per instance) | 512MB - 768GB | 128MB - 10GB |
| Network | High bandwidth | Shared bandwidth |

## Recommendation Matrix

```
Sustained 24/7 traffic?
├─ YES → Use EC2
└─ NO → Use Lambda?

Lambda can handle it?
├─ NO (>15min, GPU needed) → Use EC2
└─ YES → Use Lambda!

Traffic patterns:
├─ Constant → EC2 or Lambda
├─ Spiky → Lambda (better)
└─ Unpredictable → Lambda (better)

Budget:
├─ Limited → Lambda (pay per use)
└─ Flexible → Either (EC2 usually cheaper for sustained)
```

## 📖 Related Resources

- [EC2 Documentation](../tier-1-foundational/ec2/README.md)
- [Lambda Documentation](../tier-1-foundational/lambda/README.md)
- [Cost Optimization](../best-practices/cost-optimization.md)
- [Architecture Comparison](rds-vs-dynamodb.md)