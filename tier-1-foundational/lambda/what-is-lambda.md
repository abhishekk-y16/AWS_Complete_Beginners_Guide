# What is AWS Lambda? ⚡

Serverless compute service for running code without provisioning or managing servers.

## Core Concept

**Lambda** executes your code in response to events. Upload code → Set trigger → AWS handles infrastructure scaling.

```
Traditional Server:
├─ Provision EC2 instance
├─ Install runtime (Node, Python)
├─ Deploy code
├─ Monitor health
├─ Scale manually
├─ Pay even when idle
└─ Operational overhead

Lambda:
├─ Upload code (zip or container)
├─ Set trigger (API Gateway, S3, schedule)
├─ Code executes when triggered
├─ Auto-scales instantly
├─ Pay only for execution time
└─ Zero operational overhead
```

## How Lambda Works

```
Execution flow:

1. Event arrives:
   ├─ S3 file upload
   ├─ API request
   ├─ Schedule (CloudWatch Events)
   ├─ DynamoDB stream update
   └─ SNS notification

2. Lambda receives event:
   ├─ Extracts data from event
   ├─ Invokes function with parameters
   └─ Code executes

3. Function executes:
   ├─ Parse input
   ├─ Call AWS services
   ├─ Return response
   └─ Takes 100ms-15min

4. Billing:
   ├─ Duration: Rounded to 100ms
   ├─ Memory: 128MB-10,240MB
   ├─ Invocations: $0.20/1M
   └─ No charge if not invoked
```

## Supported Runtimes

```
Languages:

Node.js:
├─ 14.x, 16.x, 18.x (current)
├─ Support for CommonJS and ES6
└─ Popular for API backends

Python:
├─ 3.8, 3.9, 3.10, 3.11 (current)
├─ Easy to learn
└─ Great for data processing

Java:
├─ 8, 11, 17 (current)
├─ Slower startup (cold start)
└─ Good for complex logic

Go:
├─ 1.x
├─ Fast startup
└─ Efficient execution

Custom Runtime:
├─ Any language (Ruby, PHP, R, Rust)
├─ Package as Docker container
└─ Maximum flexibility
```

## Pricing Model

```
Invocations:
├─ $0.20 per 1,000,000 invocations
├─ First 1M free per month
├─ Example: 10M invocations/month
└─ Cost: (10M - 1M) × $0.20/1M = $1.80

Compute time (GB-seconds):
├─ $0.0000166667 per GB-second
├─ 128MB = 0.125GB
├─ 512MB = 0.5GB
├─ 1024MB (1GB) = 1GB
├─ Example: 1GB × 100ms × 1M invocations
│  └─ = 100,000 GB-seconds × $0.0000166667 = $1.67

Total example (10M invocations, 100ms each):
├─ Invocations: $1.80
├─ Compute: $1.67
└─ Total: ~$3.50/month (extremely cheap!)
```

## Real-World Example: Image Processing

```
Scenario: Users upload photos, auto-create thumbnails

Architecture:
├─ S3 bucket receives image upload
├─ S3 triggers Lambda
├─ Lambda downloads image
├─ Lambda creates 3 thumbnails (100x100, 300x300, 800x800)
├─ Lambda uploads thumbnails to S3
└─ Done in 2-3 seconds

Metrics:
├─ Upload frequency: 100,000/month
├─ Lambda memory: 512MB (0.5GB)
├─ Execution time: 2 seconds per image

Pricing calculation:
├─ Invocations: 100K × $0.20/1M = $0.02
├─ Compute: 100K × 2sec × 0.5GB × $0.0000166667 = $0.17
├─ S3 uploads (original): 100K × $0.005/1K = $0.50
├─ S3 thumbnails: 300K × $0.005/1K = $1.50
├─ S3 storage: Assume 50GB = $1.15
└─ Total: ~$3.34/month

Cost per image:
├─ $3.34/month / 100K images = $0.000034 per image
├─ With manual server: $400+/month
└─ Savings: 99.2% (!)
```

## Lambda Layers

```
Structure:

Application function:
├─ Code: myfunction.js (5KB)
├─ Dependencies: Included in layer
└─ Size: 5KB + dependencies from layer

Layer 1: Database client:
├─ Library: Node Postgres module (500KB)
├─ Shared across functions
└─ Versioned separately

Layer 2: Custom utilities:
├─ Code: Shared helper functions (100KB)
├─ Used by 10 functions
└─ Updated centrally

Benefits:
├─ Code reuse (DRY principle)
├─ Update libraries without changing functions
├─ Keep function size small (faster cold start)
└─ Shared dependencies managed centrally

Example cost savings:
├─ Without layers: 10 functions × 1MB = 10MB total
├─ With layers: 10 × 100KB functions + 1 × 1MB layer = 2MB
└─ Savings: 80% size reduction!
```

## Concurrency and Scaling

```
Automatic scaling:

Scenario: E-commerce checkout API

Normal traffic:
├─ 100 concurrent checkouts
├─ Each takes 2 seconds
├─ Lambda concurrency: 100
└─ Response time: 2 seconds

Black Friday (10x traffic):
├─ 1,000 concurrent checkouts
├─ Lambda auto-scales instantly
├─ New containers created
├─ All 1,000 requests processed
└─ Cost: 10x higher for that minute

Concurrency limit:
├─ Default: 1,000 concurrent
├─ Can reserve higher
├─ Can throttle if needed
└─ Prevents runaway costs

Cost during spike:
├─ 1,000 invocations × 2sec × 0.5GB = 1,000 GB-sec
├─ Cost: 1,000 × $0.0000166667 = $0.017
└─ Plus: Invocation cost negligible
```

## Cold Starts

```
What is a cold start?

First invocation (cold start):
├─ AWS launches container
├─ Runtime loads (50-200ms)
├─ Code downloaded (50-100ms)
├─ Code executes (variable)
└─ Total: 200-300ms before code runs

Subsequent invocations (warm):
├─ Container already running
├─ Code already loaded
├─ Direct execution
└─ Total: <10ms overhead

Cost difference:
├─ Cold start: Same price per GB-second
├─ You pay for cold start time!
└─ Important consideration

Minimizing cold starts:

1. Keep function small:
   ├─ Use layers for dependencies
   ├─ Remove unused libraries
   └─ Size < 10MB recommended

2. Choose faster runtime:
   ├─ Go: Fastest (50ms cold start)
   ├─ Node.js: Medium (150ms cold start)
   ├─ Python: Medium (150ms cold start)
   └─ Java: Slowest (500ms cold start)

3. Provisioned concurrency:
   ├─ Keep containers warm
   ├─ $0.015 per concurrent/hour
   ├─ Eliminates cold starts
   └─ Use only if critical
```

## Common Use Cases

### API Backend

```
REST API with Lambda + API Gateway:

GET /users/{id}:
├─ API Gateway receives request
├─ Triggers Lambda: getUser
├─ Lambda queries DynamoDB
├─ Returns JSON response
└─ API Gateway returns to client

Cost: ~$0.35/month (except data storage)
Alternative: 1 EC2 instance = $7/month
Savings: 95%
```

### Scheduled Tasks

```
Schedule with CloudWatch Events:

Event rule: "Every 1 hour"
├─ Triggers Lambda: dailyReport
├─ Function: Analyze S3 logs
├─ Generate report
├─ Upload to S3

Cost for 24× daily:
├─ Invocations: 24 × $0.20/1M = negligible
├─ Compute: 24 × 5min × 0.5GB × $0.0000166667 = $0.01/day = $0.30/month
└─ Extremely cheap for daily tasks!
```

### Data Processing Pipeline

```
Stream processing:

S3 upload → Lambda:
├─ Trigger: S3 event
├─ Function: Process data
├─ Example: Convert CSV to Parquet
├─ Store result: S3
└─ Repeat for each file

Benefits:
├─ Parallel processing (1,000 files simultaneously)
├─ No server management
├─ Automatic retries
└─ Cost scales with usage only
```

## Best Practices

✅ Keep functions small and focused
✅ Use Lambda layers for shared code
✅ Monitor with CloudWatch logs
✅ Set appropriate memory size
✅ Use environment variables for config
✅ Handle errors gracefully
✅ Test locally before deploying
✅ Version your functions
✅ Set concurrency limits if needed
✅ Use DynamoDB/S3 for persistence

## Common Mistakes

✗ Using 128MB memory (cold starts slow, wastes time)
✗ Storing data in /tmp (lost after execution)
✗ Long-running functions (15-min timeout limit)
✗ Hardcoding secrets (security risk)
✗ No error handling (silent failures)
✗ Not setting timeout (potential waste)
✗ Tight coupling to other services (hard to test)
✗ Synchronous for slow operations (user waits)

## Lambda vs. Other Services

```
Lambda: Best for
├─ Event-driven tasks
├─ Quick responses (< 15 minutes)
├─ Variable workloads
└─ Cost optimization

EC2: Best for
├─ Long-running services
├─ Consistent workload
├─ Complex setup needed
└─ GPU required

Containers (ECS/EKS): Best for
├─ Stateful services
├─ Strict resource guarantees
├─ Complex orchestration
└─ Existing infrastructure
```

## Next Steps

→ [Layers](./layers.md) - Code reuse and dependencies
→ [Triggers](./triggers.md) - Event sources
→ [Performance Optimization](./performance.md) - Cold start reduction