# What is DynamoDB? ⚡

Fully managed NoSQL database with millisecond latency at any scale.

## Core Concept

**DynamoDB** is AWS's fast, scalable NoSQL database - no servers to manage, automatic scaling.

```
Traditional Database (RDS):
├─ Fix server size upfront
├─ Traffic surge → Slow queries
├─ Need read replicas for scale
├─ Maintenance overhead
└─ Cost: Fixed + surge costs

DynamoDB:
├─ Automatic scaling
├─ Always fast (milliseconds)
├─ Built-in replication
├─ Serverless (no maintenance)
└─ Cost: Per request
```

## Relational vs NoSQL

### SQL Database (RDS)

```
Users Table:
┌──────┬─────────────┬──────────┐
│ ID   │ Name        │ Email    │
├──────┼─────────────┼──────────┤
│ 1    │ John        │ j@ex.com │
│ 2    │ Jane        │ j@ex.com │
│ 3    │ Bob         │ b@ex.com │
└──────┴─────────────┴──────────┘

Structured, rigid schema
```

### NoSQL (DynamoDB)

```
Users Collection:
{
  "user_1": {
    "name": "John",
    "email": "j@ex.com",
    "age": 30,
    "preferences": { "theme": "dark" },
    "tags": ["admin", "active"]
  },
  "user_2": {
    "name": "Jane",
    "email": "j@ex.com",
    "phone": "+1234567890",
    "notifications": ["email", "sms"]
  }
}

Flexible, schema-less
```

## Data Model: Tables & Items

```
Table: Users
├─ Partition Key: user_id
├─ Sort Key: timestamp
│
├─ Item 1:
│  ├─ user_id: "user_123" (partition key)
│  ├─ timestamp: 1234567890 (sort key)
│  ├─ name: "John"
│  ├─ email: "john@example.com"
│  └─ preferences: { theme: "dark" }
│
└─ Item 2:
   ├─ user_id: "user_456"
   ├─ timestamp: 1234567891
   └─ ...
```

## Two Capacity Modes

### On-Demand

```
Pricing: Per request

Configuration:
├─ Requests auto-scale automatically
├─ No capacity planning needed
├─ Predictable pricing

Cost Calculation:
├─ Write: $1.25 per million writes
├─ Read: $0.25 per million reads
├─ Example: 1M reads + 100K writes = $0.30

Use Case:
├─ Variable traffic
├─ New applications
├─ Testing/development
└─ Unpredictable workloads
```

### Provisioned

```
Pricing: Per capacity unit (hourly)

Configuration:
├─ Define: Read capacity units (RCUs)
├─ Define: Write capacity units (WCUs)
├─ Auto-scaling optional

1 RCU = 4KB read per second
1 WCU = 1KB write per second

Example:
├─ 100 RCU + 100 WCU
├─ Cost: ~$50/month (US East)
├─ Throughput: 400KB/s reads, 100KB/s writes

Use Case:
├─ Predictable traffic
├─ High traffic applications
├─ Cost optimization needed
└─ Consistent performance
```

## Query vs Scan

### Query (Fast)

```
Query: Find items by partition + sort key

Query Example:
├─ Find: All messages for user_123
├─ Partition key: user_id = "user_123"
├─ Sort key: timestamp > 1 hour ago
├─ Speed: Milliseconds
└─ Efficient: Only scans needed data

Performance:
├─ 100KB data size
├─ Returned: 2 items (4KB)
└─ Cost: 1 RCU (read 4KB)
```

### Scan (Slow)

```
Scan: Read every item in table

Scan Example:
├─ Find: All users with age > 30
├─ Must scan: Entire users table
├─ Speed: Seconds/minutes
└─ Inefficient: Reads all data

Performance:
├─ 100GB table size
├─ Returned: 1000 items (400KB)
└─ Cost: Reads all 100GB (inefficient!)

AVOID SCANS IN PRODUCTION!
```

## Global Secondary Indexes (GSI)

Add alternate query patterns:

```
Table: Users
├─ Partition Key: user_id
├─ Sort Key: timestamp
│
├─ GSI 1: email
│  └─ Query: Find user by email (alternative way)
│
├─ GSI 2: country
│  └─ Query: Find all users in country
│
└─ GSI 3: created_date
   └─ Query: Find users created in date range

With GSI:
├─ Query email (previously needed scan)
├─ Query country (previously needed scan)
└─ Query date (previously needed scan)
```

## Consistency Models

### Strong Consistency (Default)

```
Read after Write:

Write: Update user age to 30
    ↓
Read: Immediately read age
    ↓
Result: 30 (latest value)

Latency: ~10ms
Cost: 1 RCU
```

### Eventually Consistent

```
Read after Write (delayed):

Write: Update user age to 30
    ↓
Read: Immediately read age
    ↓
Result: 29 (old value - not propagated yet)
    ↓
Read again: 10ms later
    ↓
Result: 30 (now updated)

Latency: ~5ms (faster!)
Cost: 0.5 RCU (half cost!)

Use When:
├─ Slight staleness acceptable
├─ Need maximum performance
└─ Cost optimization critical
```

## Real-World Example: Social Media App

```
Tables:

1. Users:
   ├─ Partition Key: user_id
   ├─ Data: name, email, profile pic
   └─ GSI: email (find by email)

2. Posts:
   ├─ Partition Key: user_id
   ├─ Sort Key: timestamp
   ├─ Data: content, likes, comments
   └─ GSI: timestamp (latest posts globally)

3. Followers:
   ├─ Partition Key: follower_id
   ├─ Sort Key: following_id
   └─ Data: date followed

Queries:

Get user profile:
└─ Query Users by user_id (10ms, 1 RCU)

Get user's posts:
└─ Query Posts (user_id, last 7 days) (50ms, 2 RCU)

Get global timeline:
└─ Query Posts GSI (all recent posts) (100ms, 5 RCU)

Get followers:
└─ Query Followers (follower_id) (15ms, 1 RCU)

Performance: All sub-100ms! ⚡
```

## Streams & Triggers

React to data changes:

```
DynamoDB Stream:
├─ Captures: INSERT, UPDATE, DELETE
├─ Sends to: Lambda function automatically
├─ Example use cases:
│  ├─ Update search index
│  ├─ Send notification
│  ├─ Trigger workflow
│  └─ Audit logging

Flow:
User posts → DynamoDB INSERT
    ↓
DynamoDB Stream triggers Lambda
    ↓
Lambda sends notification: "New post!"
    ↓
Result: Real-time features!
```

## Cost Example

```
Scenario: Chat application (1M monthly active users)

Assumptions:
├─ 1M users
├─ 100 messages/user/month
├─ Total messages: 100M/month

On-Demand Mode:

Writes (100M messages):
├─ 100M × $1.25 / 1M = $125

Reads (5x per message):
├─ 500M reads
├─ 500M × $0.25 / 1M = $125

Storage:
├─ 100M messages × 1KB = 100GB
├─ 100GB × $0.25/month = $25

Total: ~$275/month

Provisioned Mode (on-demand equivalent):

Writes:
├─ 100M writes / (30 days × 86400 seconds) = 38 WCU
├─ With buffer: 50 WCU

Reads:
├─ 500M reads / (30 days × 86400 seconds) = 193 RCU
├─ With buffer: 250 RCU

Cost:
├─ 250 RCU: ~$120/month
├─ 50 WCU: ~$25/month
├─ Storage: $25/month
└─ Total: ~$170/month (saves $105!)
```

## Common Mistakes

### ✗ Mistake 1: Hot Partitions

```
Wrong:
├─ Partition key: country (USA heavily used)
├─ USA has 10M users
├─ EU has 1M users
├─ USA requests hit single partition
└─ Throttled! (exceeds partition limit)

Right:
├─ Partition key: user_id (distributed)
├─ Every user hash across partitions
├─ Load evenly distributed
└─ No throttling!
```

### ✗ Mistake 2: Using Scan Instead of Query

```
Wrong:
├─ Find user by email
├─ Scan entire table
├─ 10M table → 10M RCU read! 💸
└─ Slow and expensive

Right:
├─ Create GSI on email
├─ Query by email
├─ 1 RCU read
└─ Fast and cheap
```

### ✗ Mistake 3: Overly Large Items

```
Wrong:
├─ Store 5MB JSON per item
├─ Query returns 5MB each time
├─ RCU limit reached
└─ Throttled!

Right:
├─ Store small items (< 100KB)
├─ Reference large data in S3
├─ Fast queries + cheap
└─ Scale easily
```

### ✗ Mistake 4: Wrong Capacity Mode

```
Wrong:
├─ Provisioned for unpredictable traffic
├─ Traffic spike → Throttled
├─ Overprovision to be safe
└─ Wasting money on unused capacity

Right:
├─ Unpredictable: Use On-Demand
├─ Predictable: Use Provisioned
└─ Right tool for job
```

## Best Practices

✅ Design partition key for even distribution
✅ Use GSI for alternate access patterns
✅ Query instead of Scan
✅ Enable DynamoDB Streams for event handling
✅ Set TTL for automatic cleanup
✅ Enable point-in-time recovery
✅ Monitor throttling metrics
✅ Use batch operations
✅ Compress large data
✅ Archive old data to S3

## CLI Examples

```bash
# Create table
aws dynamodb create-table \
  --table-name Users \
  --attribute-definitions \
    AttributeName=user_id,AttributeType=S \
  --key-schema \
    AttributeName=user_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

# Put item
aws dynamodb put-item \
  --table-name Users \
  --item '{
    "user_id": {"S": "user_123"},
    "name": {"S": "John"},
    "email": {"S": "john@example.com"}
  }'

# Query items
aws dynamodb query \
  --table-name Users \
  --key-condition-expression "user_id = :uid" \
  --expression-attribute-values '{
    ":uid": {"S": "user_123"}
  }'
```

## Next Steps

→ [DynamoDB Queries & Scans](./queries.md) - Query optimization
→ [Indexes](./indexes.md) - GSI and LSI
→ [Global Tables](./global.md) - Multi-region replication