# RDS vs DynamoDB Comparison

Choosing between relational database (RDS) and NoSQL database (DynamoDB).

## Quick Decision Matrix

| Feature | RDS | DynamoDB |
|---------|-----|----------|
| **Best For** | Complex queries, transactions | Real-time, massive scale |
| **Data Model** | Structured tables/rows | Key-value, JSON documents |
| **Query Language** | SQL | Key-based, scans |
| **Relationships** | JOINs, foreign keys | Denormalized data |
| **Transactions** | ACID guaranteed | Limited (within partition) |
| **Scaling** | Vertical (bigger server) | Horizontal (unlimited) |
| **Cost (small)** | $10-50/month | Pay per request (~$1/month) |
| **Cost (large)** | $100-1000/month | Can scale to millions |
| **Setup Time** | 5-10 minutes | 2 minutes |
| **Maintenance** | Backups, patches, updates | AWS handles it |
| **Latency** | 1-100ms | 1-10ms |
| **Max size** | Limited by server size | Unlimited (petabytes) |

## RDS Advantages ✓

**1. Complex queries**
```sql
-- Easy in RDS
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
```

**2. Transactions (ACID)**
- Multiple operations all succeed or all fail
- Perfect for payments, reservations
- Data consistency guaranteed

**3. Relationships**
- Foreign keys prevent bad data
- Normalize data (less duplication)
- Data integrity rules

**4. Familiar**
- SQL is standard
- Most developers know it
- Ecosystem of tools

**5. Complex data types**
- Dates, arrays, ranges
- Constraints and validation
- Column types

## DynamoDB Advantages ✓

**1. Unlimited scaling**
- Grows to millions of users
- No planning needed
- No maintenance

**2. Speed**
- Single-digit millisecond latency
- Fast reads/writes
- Great for real-time apps

**3. Simplicity**
- No schema changes hassle
- Add fields anytime
- Flexible structure

**4. Cost efficiency (unpredictable)**
- Pay per request
- Spiky usage = lower cost
- No paying for idle time

**5. Built for scale**
- Designed for AWS scale
- 24/7 availability
- Automatic replication

## Data Model Comparison

### RDS: Structured Tables
```
Users Table:
┌─────┬─────────┬────────────┐
│ ID  │  Name   │   Email    │
├─────┼─────────┼────────────┤
│ 1   │ Alice   │ alice@... │
│ 2   │ Bob     │ bob@...   │
└─────┴─────────┴────────────┘

Orders Table:
┌────────┬─────────┬────────────┐
│ OrderID│ UserID  │  Amount    │
├────────┼─────────┼────────────┤
│ 101    │ 1       │ $99.99    │
│ 102    │ 1       │ $49.99    │
└────────┴─────────┴────────────┘
```

### DynamoDB: Flexible Documents
```
{
  "userId": "user-123",
  "name": "Alice",
  "email": "alice@...",
  "orders": [
    {"orderId": "101", "amount": 99.99},
    {"orderId": "102", "amount": 49.99}
  ],
  "preferences": {
    "newsletter": true,
    "notifications": ["email", "sms"]
  }
}
```

## Cost Comparison

### Scenario 1: Small app (1,000 users, 10,000 requests/day)

**RDS (db.t3.micro):**
- Instance: ~$10/month
- Storage: ~$2/month
- Backups: ~$5/month
- Total: ~$17/month

**DynamoDB:**
- Write requests: 10,000/month × $1.25 per million = $0.0125
- Read requests: 10,000/month × $0.25 per million = $0.0025
- Storage: 10GB × $0.25 = $2.50
- Total: ~$2.52/month
- **DynamoDB wins: 6.7x cheaper**

### Scenario 2: Growing app (100,000 users, 10M requests/day)

**RDS (db.t3.large):**
- Instance: ~$150/month
- Storage: ~$50/month
- Backups: ~$100/month
- Total: ~$300/month

**DynamoDB:**
- Requests: 10M × 2 per request = 20M ops
- Write: 15M × $1.25 per million = $18.75
- Read: 5M × $0.25 per million = $1.25
- Storage: 100GB × $0.25 = $25
- Total: ~$45/month
- **DynamoDB wins: 6.7x cheaper**

## Use Cases

**Choose RDS if:**
- Complex queries (lots of JOINs)
- Transactions critical (payments)
- Relational data (users, orders, products)
- Regular schema (consistent structure)
- Reporting needed
- Example: E-commerce site, banking, CRM

**Choose DynamoDB if:**
- Simple lookups (by ID)
- Massive scale (millions)
- Real-time apps (gaming, chats)
- Flexible structure (schema changes often)
- High traffic spikes
- Example: Gaming leaderboards, IoT sensors, messaging

## Migration Example

### Before: RDS Structure
```sql
-- Users
id, name, email, created_at

-- User Preferences
id, user_id, theme, notifications_enabled

-- User Activity
id, user_id, last_login, login_count
```

### After: DynamoDB Document
```json
{
  "PK": "USER#123",
  "SK": "PROFILE",
  "name": "Alice",
  "email": "alice@...",
  "preferences": {
    "theme": "dark",
    "notifications": true
  },
  "activity": {
    "lastLogin": "2024-01-15T10:30:00Z",
    "loginCount": 42
  }
}
```

## Query Complexity

### RDS: Complex Query
```sql
-- Find top customers by spending
SELECT 
  u.id, u.name, SUM(o.amount) as total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01'
GROUP BY u.id
ORDER BY total_spent DESC
LIMIT 10;
```

### DynamoDB: Simpler Pattern
```python
# Can't do complex JOINs
# Must query: users by ID or by GSI (email, status)

# Get single user
user = table.get_item(Key={'userId': 'user-123'})

# Query all users with status='premium'
users = table.query(
    IndexName='statusIndex',
    KeyConditionExpression='#s = :status',
    ExpressionAttributeNames={'#s': 'status'},
    ExpressionAttributeValues={':status': 'premium'}
)
```

## Scaling Comparison

### RDS Scaling
```
Need more performance?
├─ Small load → db.t3.micro ($10/mo)
├─ Medium load → db.t3.small ($20/mo)
├─ Large load → db.m5.large ($150/mo)
└─ Massive load → Read replicas needed ($300+)
```

### DynamoDB Scaling
```
Need more performance?
├─ 100 requests/sec → $0.50/day
├─ 1,000 requests/sec → $5/day
├─ 10,000 requests/sec → $50/day
└─ 1M requests/sec → $5000/day
(Automatic, no action needed)
```

## Recommendation Decision Tree

```
Do you need complex queries with JOINs?
├─ YES → RDS
└─ NO → Continue...

Do you need transactions?
├─ YES → RDS
└─ NO → Continue...

Is your data highly relational?
├─ YES → RDS
└─ NO → DynamoDB

Is your scale massive (millions of users)?
├─ YES → DynamoDB
└─ RDS probably fine

Do you have spiky traffic?
├─ YES → DynamoDB (pay-per-request)
└─ RDS (predictable costs)
```

## Hybrid Approach

**Use both:**

```
Web App
├─ RDS (primary data)
│  └─ Users, orders, products
└─ DynamoDB (real-time cache)
   └─ Session data, leaderboards, activity feeds
```

- RDS for complex business logic
- DynamoDB for fast reads
- Best of both worlds

## 📖 Related Resources

- [RDS Documentation](../tier-1-foundational/rds/README.md)
- [DynamoDB Documentation](../tier-2-common/dynamodb/README.md)
- [Database Comparison](../service-comparisons/README.md)
- [Cost Optimization](../best-practices/cost-optimization.md)