# DynamoDB Use Cases 🎯

Real-world scenarios where DynamoDB excels.

## Use Case 1: Real-Time Web Application

### Scenario

```
You're building: E-commerce shopping cart

Requirements:
├─ Store shopping carts (temporary, 24-hour TTL)
├─ Update quantity instantly
├─ Get cart for specific user
├─ Handle 1000s of concurrent users
├─ Variable traffic (spikes on weekends)
└─ Must be fast (< 100ms)

Why DynamoDB:
├─ Partition by user_id (each user separate)
├─ TTL: Auto-delete abandoned carts (24h)
├─ On-demand pricing: Pay for actual usage
├─ Millisecond response times
└─ Handles traffic spikes automatically
```

### Data Model

```
Table: ShoppingCarts
├─ Partition Key: user_id
├─ Sort Key: session_id
├─ TTL: expires_at (auto-delete after 24h)
└─ Attributes:
   ├─ items (List)
   │  ├─ {product_id, qty, price}
   │  ├─ {product_id, qty, price}
   │  └─ {...}
   ├─ total: 199.99
   ├─ created_at: 1706461200
   └─ updated_at: 1706470000
```

### Operations

```javascript
// 1. Add item to cart
await dynamodb.updateItem({
  TableName: "ShoppingCarts",
  Key: { user_id: "user-100", session_id: "sess-xyz" },
  UpdateExpression: "SET items = list_append(items, :item), updated_at = :now",
  ExpressionAttributeValues: {
    ":item": [{product_id: "prod-123", qty: 1, price: 49.99}],
    ":now": Date.now()
  }
});

// 2. Get cart
const cart = await dynamodb.getItem({
  TableName: "ShoppingCarts",
  Key: { user_id: "user-100", session_id: "sess-xyz" }
});

// 3. TTL auto-deletes after 24h
// No manual cleanup needed!
```

## Use Case 2: User Sessions & Authentication

### Scenario

```
You're managing: Web app user sessions

Requirements:
├─ Store session info (JWT refresh tokens)
├─ Lookup session by token
├─ Auto-expire sessions (1 hour)
├─ Handle millions of sessions
├─ Lightning-fast lookups
└─ Secure (encrypted)

Why DynamoDB:
├─ TTL: Sessions auto-expire
├─ GSI: Lookup by token quickly
├─ Sub-millisecond performance
├─ Encryption at rest
└─ Scales to millions of sessions
```

### Data Model

```
Table: Sessions
├─ Partition Key: session_id
├─ GSI: SessionsByUserId (lookup by user)
├─ TTL: expires_at (1 hour)
└─ Attributes:
   ├─ session_id (String) - Primary key
   ├─ user_id (String) - For GSI
   ├─ token (String) - JWT refresh token
   ├─ ip_address (String) - For security
   ├─ device (String) - Device info
   ├─ created_at (Number) - Timestamp
   └─ expires_at (Number) - TTL attribute
```

### Operations

```javascript
// 1. Create session on login
await dynamodb.putItem({
  TableName: "Sessions",
  Item: {
    session_id: "sess-abc123",
    user_id: "user-100",
    token: "eyJhbGciOiJIUzI1NiIs...",
    ip_address: "192.0.2.1",
    created_at: Date.now(),
    expires_at: Math.floor(Date.now() / 1000) + 3600  // 1 hour from now
  }
});

// 2. Verify session (fast)
const session = await dynamodb.getItem({
  TableName: "Sessions",
  Key: { session_id: "sess-abc123" }
});

if (!session) {
  throw new Error("Session expired or invalid");
}

// 3. Sessions auto-delete after TTL
// No manual cleanup needed!
```

## Use Case 3: Real-Time Analytics & Metrics

### Scenario

```
You're tracking: Website analytics (page views, clicks)

Requirements:
├─ Track events in real-time
├─ Aggregate by page, country, device
├─ Query "views per page today"
├─ Handle 10K+ events/second
├─ Variable traffic (mobile vs desktop)
└─ Queries must be fast

Why DynamoDB:
├─ Partition by metric (page, country)
├─ Sort by timestamp (time-series)
├─ On-demand pricing (variable traffic)
├─ Can handle 10K+ writes/second
└─ Query by date range easily
```

### Data Model

```
Table: PageViews
├─ Partition Key: page_id
├─ Sort Key: timestamp
├─ Attributes:
   ├─ page_id: "/products"
   ├─ timestamp: 1706461200000
   ├─ country: "US"
   ├─ device: "mobile"
   ├─ session_id: "sess-xyz"
   └─ referrer: "google"

Queries:
1. Get page views for /products today
   ├─ Partition: page_id = "/products"
   ├─ Sort: timestamp >= today
   └─ Result: All views for that page today

2. Aggregate views by country
   ├─ Scan filtered by date range
   ├─ Group by country in application
   └─ Result: Views per country
```

### Cost Example

```
Analytics volume:
├─ Events: 10K per second = 864M per day
├─ Storage: 5TB per month
└─ On-demand: Pay per request

Monthly cost:
├─ Writes: 864M × $1.25/1M = $1,080
├─ Reads: 100M queries × $0.25/1M = $25
├─ Storage: 5TB × $0.25/GB = $1,280
└─ Total: ~$2,385/month

Alternative (Analytics DB):
├─ Would cost 3-5x more
└─ DynamoDB wins for this use case
```

## Use Case 4: Real-Time Notifications

### Scenario

```
You're managing: User notifications

Requirements:
├─ Store notifications per user
├─ Mark as read/unread
├─ Query unread count
├─ Delete old notifications (30 days)
├─ Handle 1M+ concurrent users
└─ Real-time updates

Why DynamoDB:
├─ Partition by user_id
├─ Sort by timestamp (newest first)
├─ TTL: Auto-delete 30+ day old
├─ Update in real-time
└─ Can handle 1M+ concurrent
```

### Data Model

```
Table: Notifications
├─ Partition Key: user_id
├─ Sort Key: notification_id
├─ TTL: created_at + 30 days
└─ Attributes:
   ├─ user_id: "user-100"
   ├─ notification_id: "notif-123"
   ├─ message: "Alice liked your post"
   ├─ type: "like" | "comment" | "follow"
   ├─ is_read: false
   ├─ created_at: 1706461200
   └─ link: "/posts/123"

Queries:
1. Get all unread notifications
   └─ Query user_id, filter is_read = false

2. Count unread
   └─ Query user_id with limit = 1000
   └─ Count filter results

3. Mark as read
   └─ UpdateItem on notification_id
```

## Use Case 5: Time-Series Data

### Scenario

```
You're tracking: IoT sensor data (temperature, humidity)

Requirements:
├─ Store readings from 1000s of sensors
├─ One reading per sensor per minute
├─ Query readings for specific sensor + date range
├─ Store years of historical data
├─ Archive old data (older than 1 year)
└─ Fast time-range queries

Why DynamoDB:
├─ Partition by sensor_id
├─ Sort by timestamp (time-series)
├─ Range queries: "Get sensor-1 readings from yesterday"
├─ TTL: Auto-archive to Glacier
└─ Can store years of data cost-effectively
```

### Data Model

```
Table: SensorReadings
├─ Partition Key: sensor_id
├─ Sort Key: timestamp
├─ TTL: auto-archive after 1 year
└─ Attributes:
   ├─ sensor_id: "sensor-temp-001"
   ├─ timestamp: 1706461200
   ├─ temperature: 22.5
   ├─ humidity: 45.2
   ├─ pressure: 1013.25
   └─ location: "warehouse-1"

Queries:
1. Get all readings for sensor-1 today
   ├─ Partition: sensor_id = "sensor-temp-001"
   ├─ Sort: timestamp >= today midnight
   └─ Result: All today's readings (fast!)

2. Get readings for specific hour
   ├─ Partition: sensor_id
   ├─ Sort: timestamp BETWEEN 14:00-15:00
   └─ Result: All readings in that hour
```

## Use Case 6: User Profiles & Preferences

### Scenario

```
You're storing: User profiles + preferences

Requirements:
├─ Store profile info (name, bio, settings)
├─ Variable attributes (some users have more data)
├─ Query by user_id (fast)
├─ Update preferences frequently
├─ Flexible schema (new features over time)
└─ Real-time updates

Why DynamoDB:
├─ Partition by user_id
├─ Flexible schema (add attributes anytime)
├─ Fast gets by user_id
├─ Update individual fields
└─ Scales to 100M+ users
```

### Data Model

```
Table: UserProfiles
├─ Partition Key: user_id
└─ Attributes:
   ├─ user_id: "user-100"
   ├─ email: "alice@example.com"
   ├─ username: "alice_j"
   ├─ profile_pic_url: "s3://bucket/pic.jpg"
   ├─ bio: "Software engineer, coffee lover"
   ├─ preferences: {
   │  ├─ theme: "dark"
   │  ├─ notifications: true
   │  ├─ newsletter: false
   │  └─ language: "en"
   │}
   ├─ social_accounts: {
   │  ├─ github: "alice_j"
   │  ├─ twitter: "alice_codes"
   │  └─ linkedin: "alice-j"
   │}
   ├─ stats: {
   │  ├─ followers: 1250
   │  ├─ posts: 87
   │  └─ joined_at: 1704067200
   │}
   └─ updated_at: 1706470000
```

## When NOT to Use DynamoDB

```
❌ Complex SQL queries
   → Use: RDS (MySQL, PostgreSQL)

❌ Complex joins across tables
   → Use: RDS with multi-table queries

❌ Strongly consistent reports
   → Use: RDS or Redshift

❌ Small datasets with infrequent access
   → Use: Database or S3

❌ Data analysis with SQL
   → Use: Redshift or Athena

❌ Full-text search
   → Use: OpenSearch or Elasticsearch
```

## Best Practices

✅ Design tables around access patterns
✅ Use partition key + sort key for scalability
✅ Use GSI for alternative access patterns
✅ Avoid scans in production (use Query)
✅ Use on-demand for unpredictable traffic
✅ Use provisioned for predictable traffic
✅ TTL for temporary data (auto-cleanup)
✅ DynamoDB Streams for change data capture
✅ Monitor with CloudWatch
✅ Archive old data to S3

## Next Steps

→ [What is DynamoDB](./what-is-dynamodb.md) - Full overview
→ [Tables & Items](./tables-and-items.md) - Core concepts