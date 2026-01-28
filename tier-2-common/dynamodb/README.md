# DynamoDB 🚀

Fully managed NoSQL database service with automatic scaling and flexible schema.

## Overview

DynamoDB stores data as JSON-like documents with flexible structure. No fixed schema needed. Auto-scales from 0 to millions of requests/second. Pay for throughput, not storage.

## Key Concepts

**Table**: Container (like SQL table)
**Item**: Single record (like SQL row)
**Partition Key**: Unique identifier (determines distribution)
**Sort Key**: Secondary ordering (optional)
**Attributes**: Key-value pairs (no fixed schema!)

## Example

```
Table: Users

Item 1:
├─ UserID: 1001 (Partition Key)
├─ Name: John Doe
├─ Email: john@example.com
├─ CreatedAt: 2024-01-01
└─ Preferences: {theme: dark}

Item 2:
├─ UserID: 1002 (Partition Key)
├─ Name: Jane Smith
├─ Email: jane@example.com
├─ Phone: 555-1234 (optional!)
└─ Preferences: {theme: light}

Flexibility: Each item can have different attributes!
```

## Scaling

**On-Demand**: Pay per request
- Perfect for unpredictable load
- $1.25 per 1M reads
- $6.25 per 1M writes

**Provisioned**: Reserve capacity
- $0.0098 per 100 RCU (read)
- $0.0488 per 100 WCU (write)
- Better for predictable load

**Auto-Scaling**: Watch metrics, adjust capacity

## Query Examples

```javascript
// Get user by ID (fast!)
const user = await dynamodb.get({
  TableName: 'Users',
  Key: { UserID: '1001' }
});

// Get all messages in chat (sorted by time)
const messages = await dynamodb.query({
  TableName: 'Messages',
  KeyConditionExpression: 'ChatRoomID = :id',
  ExpressionAttributeValues: { ':id': 'room-123' }
});
```

## Common Use Cases

- **User Sessions**: Fast lookup by SessionID
- **Chat Messages**: PartitionKey=ChatRoomID, SortKey=Timestamp
- **Analytics**: Write millions per minute
- **Product Catalog**: Fast lookups by ProductID

## When to Use DynamoDB

✅ Flexible/changing schema
✅ Simple key-value lookups
✅ Millions of requests/second
✅ Real-time data
✅ Mobile/web applications

## When NOT to Use DynamoDB

❌ Complex relationships (JOINs needed)
❌ Fixed schema with reporting
❌ Financial transactions (use RDS)

## DynamoDB vs RDS

```
DynamoDB: Flexible, NoSQL, auto-scales, simple queries
RDS: Fixed schema, SQL, complex relationships, manual scale
```

## Best Practices

✅ Choose partition key carefully (avoid hot keys!)
✅ Use on-demand for unpredictable load
✅ Enable point-in-time recovery
✅ Enable TTL for auto-deleting old items
✅ Cache frequently accessed items (ElastiCache)
✅ Monitor throttling (CloudWatch)
✅ Use batch operations
✅ Enable encryption at rest

## Pricing

```
On-Demand:
├─ Reads: $1.25 per 1M
├─ Writes: $6.25 per 1M
└─ Storage: $0.25 per GB/month

Provisioned:
├─ RCU: $0.0098 per 100/month
├─ WCU: $0.0488 per 100/month
└─ Storage: $0.25 per GB/month

Example: 1M reads + 100K writes = $1.25 + $0.63 = $1.88
```

## Related Topics

- [DynamoDB Guide](./what-is-dynamodb.md)
- [Tables & Items](./tables-and-items.md)
- [Use Cases](./use-cases.md)
- [RDS Database](../../database/rds/what-is-rds.md)

## Resources

- [DynamoDB Docs](https://docs.aws.amazon.com/dynamodb/)
- [Getting Started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)
- [Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)