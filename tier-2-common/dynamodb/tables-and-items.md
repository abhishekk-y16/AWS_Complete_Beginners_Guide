# DynamoDB Tables & Items 📊

Understanding the core building blocks of DynamoDB: tables, items, and attributes.

## Tables

### What is a Table?

```
DynamoDB table: Container for your data

Comparison:
├─ Relational DB: Table has rows and columns
├─ DynamoDB: Table has items and attributes
├─ Each item: Like a JSON document (flexible schema)
└─ No fixed columns (unlike relational)
```

### Creating a Table

```
Required settings:

1. Table Name
   ├─ Example: Users, Orders, Products
   ├─ Rules: Alphanumeric, hyphens, underscores
   └─ Cannot change after creation

2. Primary Key
   ├─ Partition Key (required)
   │  ├─ Example: user_id
   │  ├─ Determines: Which partition stores item
   │  └─ Must be unique or paired with sort key
   │
   └─ Sort Key (optional)
      ├─ Example: timestamp (for time-series)
      ├─ Allows: Multiple items with same partition key
      └─ Enables: Range queries (between dates)

3. Capacity Mode
   ├─ On-demand: Pay per request (variable cost)
   │  └─ Good for: Unpredictable traffic
   │
   └─ Provisioned: Reserve capacity upfront
      ├─ Read capacity: 4KB per read
      ├─ Write capacity: 1KB per write
      └─ Good for: Predictable traffic

4. TTL (Time to Live) - Optional
   ├─ Automatically delete items after X seconds
   └─ Example: Sessions expire after 1 hour
```

### Example Table Design

```sql
-- Users table
Table: Users
├─ Partition Key: user_id (STRING)
├─ Sort Key: None
└─ Attributes:
   ├─ user_id (String) - Primary key
   ├─ email (String) - User's email
   ├─ name (String) - User's full name
   ├─ created_at (Number) - Timestamp
   ├─ preferences (Map) - Settings object
   │  ├─ theme: "dark"
   │  ├─ notifications: true
   │  └─ language: "en"
   └─ tags (List) - Array of strings
      ├─ "premium"
      ├─ "verified"
      └─ "trial"

-- Orders table
Table: Orders
├─ Partition Key: user_id (STRING)
├─ Sort Key: order_id (STRING)
└─ Attributes:
   ├─ user_id (String) - Which user
   ├─ order_id (String) - Unique order ID
   ├─ amount (Number) - Order total
   ├─ status (String) - pending/complete/failed
   ├─ items (List) - Items in order
   │  ├─ [0] {product_id, qty, price}
   │  ├─ [1] {product_id, qty, price}
   │  └─ ...
   └─ created_at (Number) - Timestamp
```

## Items

### What is an Item?

```
Item: Single record/document in a table

Example item from Users table:
{
  "user_id": "user-123",           ← Partition key
  "email": "alice@example.com",
  "name": "Alice Johnson",
  "created_at": 1706461200,
  "preferences": {
    "theme": "dark",
    "notifications": true,
    "language": "en"
  },
  "tags": ["premium", "verified"]
}

Flexible schema:
├─ user_id is required (partition key)
├─ email, name, preferences are optional
├─ One item might have tags, another won't
└─ Can add attributes anytime
```

### Item Size Limits

```
Maximum item size: 400KB (400 kilobytes)

Common items:
├─ User profile: 5-20KB
├─ Product info: 10-50KB
├─ Order with items: 20-100KB
├─ Chat message: 1-5KB
└─ Large document: 100-400KB

What if item > 400KB?
├─ Split across multiple items
├─ Or: Store in S3 + reference in DynamoDB
├─ Or: Compress data
└─ Or: Use DynamoDB Streams + S3 export
```

## Attributes

### Data Types

```
DynamoDB supports 7 data types:

1. String (S)
   ├─ Text data
   ├─ Max: 400KB per attribute
   └─ Example: "Alice", "alice@example.com"

2. Number (N)
   ├─ Integers and decimals
   ├─ Range: ±10^38 precision
   └─ Example: 42, 3.14, -100

3. Binary (B)
   ├─ Encrypted data
   ├─ Base64 encoded
   └─ Example: Image bytes, encrypted secrets

4. String Set (SS)
   ├─ Set of unique strings
   ├─ No duplicates
   └─ Example: ["tag1", "tag2", "tag3"]

5. Number Set (NS)
   ├─ Set of unique numbers
   ├─ No duplicates
   └─ Example: [1, 2, 3, 5, 8]

6. Map (M)
   ├─ Nested object/JSON
   ├─ Can contain other data types
   └─ Example: {"name": "Alice", "age": 30}

7. List (L)
   ├─ Ordered array
   ├─ Can contain mixed types
   └─ Example: ["item1", 2, true, {"nested": "object"}]

8. Boolean (BOOL)
   ├─ True or False
   └─ Example: true, false

9. Null (NULL)
   ├─ Represents missing/null values
   └─ Example: null
```

### Working with Attributes

```javascript
// Create item with various attributes
const item = {
  user_id: "user-123",              // String (S)
  balance: 1000.50,                 // Number (N)
  is_active: true,                  // Boolean
  tags: ["vip", "beta-tester"],    // String Set (SS)
  scores: [100, 95, 88, 92],        // Number Set (NS)
  profile: {                         // Map (M)
    name: "Alice Johnson",
    age: 30,
    preferences: {
      theme: "dark",
      notifications: true
    }
  },
  orders: [                          // List (L)
    {
      order_id: "ord-1",
      amount: 99.99
    },
    {
      order_id: "ord-2",
      amount: 49.99
    }
  ]
};

// Put item to DynamoDB
await dynamodb.putItem({
  TableName: "Users",
  Item: item
});
```

## Primary Key Design

### Partition Key Only

```
Structure:
├─ Partition Key: Unique identifier
├─ Example: user_id
└─ Each item: Unique partition key

Table: Users
├─ user-100
├─ user-101
├─ user-102
└─ user-103

Query: Get single user
const user = await dynamodb.getItem({
  TableName: "Users",
  Key: { user_id: "user-100" }
});

Limitation:
└─ Can only query by exact user_id
```

### Partition Key + Sort Key

```
Structure:
├─ Partition Key: Groups items
├─ Sort Key: Orders items within group
└─ Together: Create composite primary key

Example: Orders table
├─ Partition Key: user_id
├─ Sort Key: order_id
│
├─ user-100
│  ├─ ord-001
│  ├─ ord-002
│  └─ ord-003
│
├─ user-101
│  ├─ ord-001
│  ├─ ord-002
│  └─ ord-003
│
└─ user-102
   ├─ ord-001
   └─ ord-002

Queries:
1. Get all orders for user-100
const orders = await dynamodb.query({
  TableName: "Orders",
  KeyConditionExpression: "user_id = :uid",
  ExpressionAttributeValues: {
    ":uid": "user-100"
  }
});
// Returns: ord-001, ord-002, ord-003

2. Get orders after specific date
const recentOrders = await dynamodb.query({
  TableName: "Orders",
  KeyConditionExpression: "user_id = :uid AND order_id >= :oid",
  ExpressionAttributeValues: {
    ":uid": "user-100",
    ":oid": "ord-002"
  }
});
// Returns: ord-002, ord-003
```

## Global Secondary Indexes

### What is a GSI?

```
Global Secondary Index: Alternative way to query data

Example problem:
├─ Table: Orders (partition key: user_id)
├─ Can query: "Get all orders by user-100"
├─ Cannot query: "Get all orders from today"
└─ Solution: Create GSI on created_at

GSI: Orders_by_Date
├─ Partition Key: created_at (date)
├─ Sort Key: order_id
└─ Now can query: "Get orders from 2024-01-28"
```

### Creating GSI

```
Table: Orders
├─ Primary Key: user_id + order_id
│
├─ GSI-1: Orders_by_Date
│  ├─ Partition Key: created_at
│  ├─ Sort Key: order_id
│  └─ Use: Find orders by date
│
└─ GSI-2: Orders_by_Status
   ├─ Partition Key: status
   ├─ Sort Key: created_at
   └─ Use: Find orders by status

Queries enabled:
1. Query primary: user_id = "user-100"
2. Query GSI-1: created_at = "2024-01-28"
3. Query GSI-2: status = "completed"

Cost:
├─ Primary table: 4 write units (1 item)
├─ GSI-1: 4 write units (replicated)
├─ GSI-2: 4 write units (replicated)
└─ Total: 12 write units (3x cost!)
```

## Querying vs Scanning

### Query (Fast & Efficient)

```
Query: Use primary key or GSI

Example:
├─ Get all orders for user-100
├─ DynamoDB knows: Exact partition
├─ Scans: Only partition for user-100
└─ Speed: Usually < 10ms

Query always returns:
├─ Items matching partition key
├─ Can filter with sort key range
└─ Sorted by sort key
```

### Scan (Slow, Use Carefully)

```
Scan: Read all items in table

Example:
├─ "Find all orders with status=completed"
├─ DynamoDB: Must read EVERY item
├─ If table has 1M items: Reads all 1M
└─ Speed: Can be minutes (expensive!)

When to use Scan:
✅ Small tables (< 100K items)
✅ Rare operations (daily reports)
✅ Background jobs

When NOT to use Scan:
❌ Frequent queries (use GSI instead)
❌ Large tables
❌ Real-time requests
❌ High-traffic applications
```

## Best Practices

✅ Keep items < 100KB (unless necessary)
✅ Use partition key + sort key (enables range queries)
✅ Design GSIs for common access patterns
✅ Avoid scans in production (use Query + GSI)
✅ Use on-demand pricing for unpredictable traffic
✅ Monitor item count and sizes
✅ Use TTL for temporary data
✅ Normalize similar data types
✅ Archive old data to S3
✅ Test query patterns before designing

## Next Steps

→ [What is DynamoDB](./what-is-dynamodb.md) - Full overview
→ [Use Cases](./use-cases.md) - Real-world scenarios