# Lambda Triggers and Event Sources 🔔

Comprehensive guide to triggering Lambda functions from various AWS services and external sources.

## How Triggers Work

```
Trigger types:

1. Synchronous (blocking):
   ├─ Caller waits for response
   ├─ Error propagates to caller
   ├─ Used for: APIs, real-time processing
   └─ Example: API Gateway

2. Asynchronous (fire-and-forget):
   ├─ Caller doesn't wait
   ├─ AWS retries on failure (2 attempts)
   ├─ Used for: background jobs, cleanup
   └─ Example: S3 events

3. Event streaming (batched):
   ├─ Process events in batches
   ├─ Single function invocation per batch
   ├─ Used for: high-volume events
   └─ Example: DynamoDB Streams, SQS
```

## AWS Native Triggers

### API Gateway (HTTP Requests)

```
Setup:
├─ Create API Gateway REST API
├─ Create method: POST /users
├─ Integration type: Lambda Function
├─ Function: createUser
└─ Deploy

Flow:
├─ Client POST to /users with JSON
├─ API Gateway validates request
├─ Invokes Lambda: createUser
├─ Lambda processes (create in DynamoDB)
├─ Lambda returns response
└─ API Gateway returns HTTP response

Example invocation event:
{
  "httpMethod": "POST",
  "path": "/users",
  "body": "{\"name\":\"John\"}",
  "headers": {"Content-Type": "application/json"},
  "queryStringParameters": null
}

Example Lambda response:
{
  "statusCode": 201,
  "body": "{\"id\":\"123\",\"name\":\"John\"}",
  "headers": {"Content-Type": "application/json"}
}

Latency: ~100-500ms (depending on function)
Scaling: Automatically handles 1M requests/sec
```

### S3 (Object Changes)

```
Setup:
├─ S3 bucket: my-images
├─ Event: s3:ObjectCreated:*
├─ Destination: Lambda function
├─ Function: processImage
└─ Filters: *.jpg, *.png only (optional)

Flow:
├─ User uploads image.jpg
├─ S3 detects creation
├─ Invokes Lambda: processImage
├─ Lambda downloads image
├─ Lambda creates thumbnail
├─ Lambda uploads thumb to S3
└─ Original image remains

Example event:
{
  "Records": [{
    "s3": {
      "bucket": {"name": "my-images"},
      "object": {"key": "photos/vacation.jpg", "size": 5242880}
    },
    "eventName": "ObjectCreated:Put"
  }]
}

EventName types:
├─ s3:ObjectCreated:Put
├─ s3:ObjectCreated:Post
├─ s3:ObjectCreated:Copy
├─ s3:ObjectRemoved:Delete
└─ s3:ObjectRemoved:DeleteMarkerCreated (versioning)

Latency: Usually 1-10 seconds after upload
Reliability: At least once delivery (could invoke multiple times)
```

### DynamoDB Streams

```
Scenario: Sync DynamoDB to Elasticsearch

Setup:
├─ DynamoDB table: users
├─ Enable Streams: New and old images
├─ Stream destination: Lambda
├─ Function: syncToElasticsearch
└─ Batch size: 100 records

Flow:
├─ Item inserted/updated in DynamoDB
├─ Stream captures change
├─ Batches up to 100 changes
├─ Invokes Lambda once per batch
├─ Lambda sends to Elasticsearch
└─ Search index updated

Example event (new item):
{
  "Records": [{
    "dynamodb": {
      "Keys": {"id": {"N": "123"}},
      "NewImage": {
        "id": {"N": "123"},
        "name": {"S": "John"},
        "email": {"S": "john@example.com"}
      }
    },
    "eventName": "INSERT",
    "eventSource": "aws:dynamodb"
  }]
}

EventName:
├─ INSERT: New item created
├─ MODIFY: Item updated
└─ REMOVE: Item deleted

Latency: Usually <1 second
Ordering: Guaranteed per shard
```

### SQS (Queue Messages)

```
Scenario: Process orders from queue

Setup:
├─ SQS queue: order-queue
├─ Messages format: JSON
├─ Lambda trigger: SQS
├─ Function: processOrder
├─ Batch size: 10 messages
└─ Timeout: 5 minutes

Flow:
├─ Order service puts message to SQS
├─ Message waits in queue
├─ Lambda polls queue every second
├─ Gets up to 10 messages
├─ Invokes function once (all messages)
├─ Lambda processes each order
├─ Lambda deletes messages on success
└─ Failed messages go to DLQ (Dead Letter Queue)

Example event:
{
  "Records": [{
    "body": "{\"orderId\":\"12345\",\"amount\":99.99}",
    "messageAttributes": {
      "priority": {"stringValue": "high"}
    },
    "receiptHandle": "AQEBVzBgMkQQ..." // Use to delete
  }]
}

Benefits:
├─ Decoupling: Producer doesn't wait
├─ Retry: Messages stay in queue if failed
├─ Dead Letter Queue: Track failures
└─ Batching: Process multiple messages efficiently

Latency: <1 second typical
Reliability: Messages guaranteed delivery (at least once)
```

### CloudWatch Events (Scheduled)

```
Scenario 1: Daily report generation

Setup:
├─ Rule: "cron(0 2 * * ? *)" (2 AM daily)
├─ Target: Lambda function
├─ Function: generateDailyReport
└─ Timezone: UTC

Example event:
{
  "detail-type": "Scheduled Event",
  "source": "aws.events",
  "time": "2024-01-28T02:00:00Z"
}

Cron syntax examples:
├─ "cron(0 2 * * ? *)" = 2 AM UTC daily
├─ "cron(0 */6 * * ? *)" = Every 6 hours
├─ "cron(0 12 ? * MON *)" = Noon every Monday
├─ "cron(*/15 * * * ? *)" = Every 15 minutes
└─ "rate(5 minutes)" = Every 5 minutes

Latency: Usually within 1 minute of schedule
Reliability: Guaranteed delivery

Scenario 2: AWS Service State Change

Setup:
├─ Event source: EC2
├─ Event: Instance state-change
├─ Target: Lambda function
├─ Function: notifyOnEC2Stop
└─ Filter: state = "stopped"

Example event:
{
  "source": "aws.ec2",
  "detail-type": "EC2 Instance State-change Notification",
  "detail": {
    "instance-id": "i-0123456789abcdef",
    "state": "stopped"
  }
}

Common events:
├─ EC2 instance state change
├─ RDS instance event
├─ S3 bucket event
├─ IAM user creation
├─ Security group change
└─ And hundreds more!
```

### SNS (Topic Messages)

```
Scenario: Send email on alarm

Setup:
├─ CloudWatch Alarm: CPU > 80%
├─ Action: Publish to SNS topic
├─ SNS subscribers: Lambda + Email
├─ Function: createTicket
└─ Action: Create support ticket

Flow:
├─ EC2 CPU exceeds threshold
├─ CloudWatch creates alarm
├─ Publishes to SNS topic
├─ Topic delivers to:
│  ├─ Lambda function (automatic)
│  └─ Email subscribers (manual action)
├─ Lambda creates support ticket
└─ Email goes to ops team

Example event:
{
  "Records": [{
    "Sns": {
      "Message": "EC2 CPU alarm triggered",
      "Subject": "High CPU Alert",
      "TopicArn": "arn:aws:sns:us-east-1:123456789:alerts"
    }
  }]
}

Benefits:
├─ Pub/Sub pattern (loose coupling)
├─ Multiple subscribers (Email + Lambda + SQS)
├─ Fan-out (one message to many targets)
└─ Easy notification patterns
```

### EventBridge (Advanced Routing)

```
Scenario: Complex multi-service workflow

Setup:
├─ Rule 1: S3 object uploaded
│  └─ Target: Lambda processImage
├─ Rule 2: Processing complete
│  ├─ Target: SNS (notify user)
│  ├─ Target: SQS (async work)
│  └─ Target: DynamoDB (log event)
└─ Rule 3: Manual trigger
   └─ Target: Step Functions (complex workflow)

Example:
When S3 event arrives:
├─ Check file extension (Rule filter)
├─ If .jpg → processImage Lambda
├─ If .pdf → extractText Lambda
├─ If .csv → importData Lambda
└─ All async, all tracked

Benefits over native services:
├─ Content-based filtering
├─ Multiple targets per rule
├─ Cross-account/region routing
└─ Complex event transformation
```

## External Triggers

### GitHub Webhooks

```
Scenario: Deploy on code push

Setup:
├─ GitHub repo settings
├─ Add webhook → API Gateway endpoint
├─ Events: push, pull_request, release
├─ Target: Lambda function
└─ Function: handleGitHubWebhook

Flow:
├─ Developer git push
├─ GitHub sends webhook
├─ API Gateway validates (IP whitelist, signature)
├─ Invokes Lambda
├─ Lambda clones repo
├─ Lambda builds and tests
├─ Lambda deploys to production
└─ Lambda posts status to GitHub

Webhook signature verification:
├─ GitHub sends X-Hub-Signature header
├─ Contains HMAC SHA256 of payload
├─ Lambda verifies signature (security!)
├─ Prevents spoofed webhooks
└─ Only legitimate GitHub events processed
```

### Slack Events

```
Scenario: Slash command integration

Setup:
├─ Slack app → Slash Commands
├─ Command: /aws-status
├─ Request URL: API Gateway endpoint
├─ Target: Lambda function
└─ Function: getAWSServiceStatus

Flow:
├─ User types /aws-status in Slack
├─ Slack sends POST request
├─ Lambda checks AWS Service Health
├─ Lambda returns formatted response
├─ Response appears in Slack immediately
└─ User gets status without leaving Slack

Example Lambda response:
{
  "response_type": "in_channel",
  "text": "EC2: Operational ✅ | RDS: Issues 🔴"
}
```

## Best Practices for Triggers

✅ Use async triggers for background work (S3, SNS, SQS)
✅ Use sync triggers for real-time (API Gateway, ALB)
✅ Implement error handling and retries
✅ Use dead letter queues (SQS, Lambda)
✅ Monitor trigger latency (CloudWatch)
✅ Test trigger locally before production
✅ Verify event format in function code
✅ Set appropriate timeouts
✅ Use event filtering (S3, EventBridge)
✅ Implement idempotency (handle duplicates)

## Next Steps

→ [First Lambda Function](./first-lambda-function.md) - Hands-on guide
→ [Pricing](./pricing.md) - Cost breakdown
→ [Use Cases](./use-cases.md) - Real-world scenarios