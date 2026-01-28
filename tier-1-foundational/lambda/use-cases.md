# Lambda Use Cases 🎯

Real-world scenarios where AWS Lambda excels and delivers maximum value.

## Web and API Applications

### REST API Backend

```
Architecture:
├─ Client makes HTTP request
├─ API Gateway receives request
├─ Triggers Lambda function
├─ Lambda queries DynamoDB
├─ Returns JSON response
└─ API Gateway returns to client

Benefits:
├─ Auto-scaling (handles 1M requests/sec)
├─ Pay per request (no idle costs)
├─ Built-in monitoring (CloudWatch)
├─ Integration with API Gateway (easy)
└─ No server management

Example: Serverless microservices
├─ GET /users/{id} → Lambda function
├─ POST /users → Lambda function
├─ DELETE /users/{id} → Lambda function
└─ Each function handles one operation

Cost: ~$1/month for 1M requests (vs $100+/month for EC2)
```

### Webhooks and Callbacks

```
Scenario: GitHub webhook on code push

Flow:
├─ Developer pushes to main
├─ GitHub webhook POST to API Gateway
├─ Triggers Lambda: build-and-deploy
├─ Lambda clones repo, builds, deploys
├─ GitHub comment: "Deploy complete"
└─ All automated!

Implementation:
├─ Lambda function: 200 lines
├─ API Gateway endpoint: 1 endpoint
├─ Execution: <2 seconds
└─ Cost per deploy: ~$0.01
```

## Data Processing and ETL

### Real-Time Data Pipeline

```
Scenario: E-commerce order processing

Flow:
├─ Customer places order (S3 JSON file)
├─ S3 triggers Lambda: processOrder
├─ Lambda extracts data
├─ Lambda validates payment
├─ Lambda updates inventory (DynamoDB)
├─ Lambda sends confirmation email (SNS)
├─ Lambda logs to analytics (S3)
└─ Order processed in 1-2 seconds

Benefits:
├─ Automatic retry (on failure)
├─ Dead letter queue (failed orders)
├─ Metrics and logs (CloudWatch)
├─ Scales to 1,000 concurrent orders
└─ Cost: ~$0.50/month for 10K orders
```

### Batch Processing

```
Scenario: Daily report generation

Setup:
├─ CloudWatch Events: Trigger daily at 2 AM
├─ Lambda: generateDailyReport
├─ Execution:
│  ├─ Query RDS for yesterday's data
│  ├─ Generate PDF report
│  ├─ Upload to S3
│  └─ Send via email (SNS)
└─ Duration: 30 seconds, runs once daily

Cost calculation:
├─ Invocations: 30 × $0.20/1M = negligible
├─ Compute: 0.5GB × 30sec × 30 days = $0.007
└─ Annual: ~$0.10 (extremely cheap!)

Alternative (with EC2):
├─ t3.small instance: $7/month
├─ Only using 1% of capacity
└─ Lambda saves $83.84/year per report
```

### Machine Learning Inference

```
Scenario: Real-time image classification

Flow:
├─ Mobile app uploads image
├─ API Gateway → Lambda
├─ Lambda loads ML model (from S3)
├─ Lambda runs inference
├─ Returns prediction + confidence
└─ Response to app: <500ms

Model size: 200MB (pre-downloaded)
Latency:
├─ Cold start: ~1 second (model load)
├─ Subsequent: ~100ms (model in memory)
└─ With provisioned concurrency: Always <100ms

Scaling:
├─ 1 request: 1 container
├─ 100 requests: 100 containers (auto)
├─ 1,000 requests: 1,000 containers (auto)
└─ All automatic!
```

## Event-Driven Workflows

### IoT Data Processing

```
Scenario: IoT sensors sending temperature data

Architecture:
├─ 10,000 sensors worldwide
├─ Send data every 5 minutes = 120K messages/day
├─ IoT Core → Kinesis Stream
├─ Lambda processes each batch (async)
├─ Lambda checks if temperature abnormal
├─ If abnormal: Alert to SNS
├─ Store data in DynamoDB (time-series)
└─ Visualize in CloudWatch

Benefits:
├─ Scales to millions of messages
├─ Pay per message processed
├─ Automatic retries
├─ Real-time alerts
└─ Cost: ~$2/month for 120K messages
```

### Scheduled Cleanup Tasks

```
Scenario: Delete old S3 objects daily

Setup:
├─ CloudWatch Events: Every day at 3 AM
├─ Triggers Lambda: cleanupOldFiles
├─ Lambda:
│  ├─ Lists S3 objects > 30 days old
│  ├─ Deletes them
│  ├─ Logs count deleted
│  └─ Sends report to Slack
└─ Duration: 2 seconds

Scenario: S3 storage was 500GB
├─ After cleanup: 200GB (60% reduction)
├─ Cost savings: 300GB × $0.023 = $6.90/month
├─ Annual savings: $82.80
└─ Lambda cost: ~$0.01/year (saves itself!)
```

### File Format Conversion

```
Scenario: Convert images to different formats

Flow:
├─ User uploads PNG
├─ S3 triggers Lambda: convertImage
├─ Lambda:
│  ├─ Download PNG from S3
│  ├─ Convert to WEBP (better compression)
│  ├─ Resize for thumbnails
│  ├─ Upload all versions to S3
│  └─ Done in 2 seconds
└─ Automatic for every upload!

Metrics (1M images/month):
├─ Lambda invocations: 1M × $0.20/1M = $0.20
├─ Compute: 1M × 2sec × 0.5GB × $0.0000166667 = $16.67
├─ Total: ~$17/month
└─ Alternative (EC2): ~$400/month (23x cheaper!)
```

## Monitoring and DevOps

### Application Logging and Insights

```
Scenario: Aggregate logs from multiple services

Setup:
├─ EC2 instance logs → CloudWatch
├─ Lambda logs → CloudWatch
├─ API Gateway logs → CloudWatch
├─ RDS logs → CloudWatch
└─ Trigger Lambda: processLogs

Lambda function:
├─ Parses logs from all sources
├─ Extracts errors and warnings
├─ Aggregates by service
├─ Sends summary to Slack
└─ Stores metrics in DynamoDB

Schedule: Every 1 hour
Cost: ~$1/month
```

### Infrastructure Maintenance

```
Scenario: Auto-stop idle EC2 instances

Lambda function:
├─ Lists all EC2 instances
├─ Checks CloudWatch metrics
├─ If CPU < 5% for 8 hours
├─ And no traffic
├─ Stops instance (saves $)
├─ Logs action
└─ Sends notification

Benefit:
├─ Automatic cost optimization
├─ Prevents runaway costs
├─ Dev instances: 0% cost overnight
├─ Savings: 50-70% for dev environments
└─ Cost to run: ~$0.20/month
```

### Backup and Disaster Recovery

```
Scenario: Daily RDS snapshot

Setup:
├─ CloudWatch Events: 2 AM daily
├─ Triggers Lambda: backupDatabase
├─ Lambda:
│  ├─ Creates RDS snapshot
│  ├─ Tags with date
│  ├─ Deletes snapshots > 30 days old
│  ├─ Sends summary email
│  └─ Logs to CloudWatch
└─ Duration: 3 seconds

Automation benefits:
├─ Never forget backup
├─ Cleanup automatic (no manual cleanup)
├─ Disaster recovery tested (snapshots exist)
└─ Cost: ~$0.01/month (snapshot storage cost separate)
```

## Integration Scenarios

### Third-Party Service Integration

```
Scenario: Sync Shopify orders to Salesforce

Flow:
├─ Order placed in Shopify
├─ Shopify webhook → API Gateway
├─ Triggers Lambda: syncOrder
├─ Lambda:
│  ├─ Parse Shopify order data
│  ├─ Transform to Salesforce format
│  ├─ Call Salesforce API
│  ├─ Create opportunity in CRM
│  └─ Log to DynamoDB
└─ Salesforce updated instantly!

Benefit:
├─ Real-time sync (no manual entry)
├─ Sales team always has current data
├─ Reduces errors (no manual copy-paste)
└─ Cost: ~$2/month for 100 orders/day
```

### Document Processing

```
Scenario: Extract data from uploaded PDFs

Flow:
├─ User uploads invoice (PDF)
├─ S3 triggers Lambda: extractInvoiceData
├─ Lambda:
│  ├─ Uses Textract (OCR)
│  ├─ Extracts vendor, amount, date
│  ├─ Validates data
│  ├─ Stores in DynamoDB
│  └─ Returns structured JSON
└─ Frontend displays extracted data

Metrics:
├─ 1,000 invoices/month
├─ Lambda cost: ~$5/month
├─ Textract cost: ~$50/month
├─ Total: ~$55/month
└─ Manual data entry: 40+ hours/month
```

## When NOT to Use Lambda

✗ Long-running jobs (>15 minutes)
- Solution: Step Functions for orchestration

✗ Real-time streaming (sub-millisecond)
- Solution: Kinesis or MSK

✗ Stateful applications
- Solution: EC2, containers (ECS/EKS)

✗ Complex file operations
- Solution: EC2 with local storage

✗ Machine learning training
- Solution: SageMaker

## Best Practices

✅ Use Lambda for discrete tasks (< 15 minutes)
✅ Keep functions small and focused
✅ Use triggers (don't run constantly)
✅ Implement error handling and retries
✅ Monitor with CloudWatch
✅ Version your functions
✅ Test before production
✅ Use environment variables for config

## Next Steps

→ [Triggers](./triggers.md) - Event sources
→ [First Lambda Function](./first-lambda-function.md) - Hands-on guide
→ [Pricing](./pricing.md) - Cost breakdown