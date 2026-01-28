# What is ElastiCache? ⚡

AWS's managed in-memory caching service for ultra-fast data access without querying databases.

## Core Concept

**ElastiCache** provides Redis or Memcached for caching. Speed up applications 100x by keeping hot data in memory.

```
Without caching:
├─ User requests profile
├─ Query database: 100ms
├─ Return to user
└─ Database hit for every request

With ElastiCache:
├─ User requests profile
├─ Check cache (Redis): 1ms
├─ Cache hit: Return instantly
├─ Cache miss (first time): Query DB, save to cache
└─ Database hit only on expiration
```

## Cache Engines

### Redis

```
Features:
├─ In-memory data structure store
├─ Data types: Strings, Lists, Sets, Hashes, Sorted Sets
├─ Advanced: HyperLogLog, Streams, Geospatial
├─ Persistence: Can save to disk (RDB/AOF)
├─ Replication: Multi-AZ replication
└─ Cluster: Horizontal scaling (Cluster mode)

Use cases:
├─ Session store
├─ Cache (with complex data)
├─ Real-time analytics
├─ Leaderboards (sorted sets)
├─ Message queues (streams)
└─ Pub/Sub messaging

Why choose: Advanced features, persistence
```

### Memcached

```
Features:
├─ Simple key-value in-memory store
├─ Data type: Only strings
├─ No persistence
├─ No replication
├─ Multi-threaded
└─ Simple, fast

Use cases:
├─ Session store
├─ Database result caching
├─ User profile caching
└─ Temporary data

Why choose: Simplicity, speed, horizontal scaling
```

## ElastiCache Redis Cluster

```
Single-Node Setup (simplest):
├─ 1 node: cache.t3.micro
├─ Memory: 1GB
├─ No replication
├─ No automatic failover
└─ Cost: $0.017/hour = $12/month

High Availability (Multi-AZ):
├─ Primary node: cache.r6g.xlarge (26GB)
├─ 2 Replica nodes (standby)
├─ Automatic failover: 30 seconds
├─ Data loss: 0 (full replication)
└─ Cost: $0.419/hour per node × 3 = ~$919/month

Cluster Mode (horizontal scaling):
├─ 3 shards (16GB each = 48GB total)
├─ 2 replicas per shard
├─ 9 nodes total
├─ Horizontal scaling: Just add shards
└─ Cost: ~$2,700/month
```

## Real-World Example: E-commerce

```
Application: Product catalog with 10M products

Without caching:
├─ Queries per second: 5,000
├─ Database: Aurora db.r6g.2xlarge
├─ Instance cost: $0.48/hour = $350/month
├─ Database connections: 1,000 max
└─ At 5K QPS: Approaching limit, need scale

With ElastiCache:
├─ ElastiCache (Redis cluster): 2 shards
├─ Cost: ~$300/month
├─ Cache hit ratio: 95% (hot products)
├─ Database queries: 5,000 × 5% = 250 QPS
├─ Database instance: db.r6g.large (smaller!)
├─ Database cost: $0.24/hour = $175/month
├─ Total: Cache $300 + DB $175 = $475
└─ Savings: $350 + $350 (could use smaller DB) = $175/month saved
```

## Caching Strategies

### Cache-Aside (Most Common)

```
Application flow:

1. User requests product details
2. Check Redis:
   ├─ If exists: Return from cache (1ms)
   └─ If not: Continue to step 3
3. Query database (100ms)
4. Save result to Redis with 1-hour TTL
5. Return to user

Code:
def get_product(id):
    cached = redis.get(f"product:{id}")
    if cached:
        return json.loads(cached)
    
    # Cache miss
    product = db.query(f"SELECT * FROM products WHERE id={id}")
    redis.setex(f"product:{id}", 3600, json.dumps(product))
    return product
```

### Write-Through

```
When saving data:

1. Save to database
2. Update cache
3. Return to user

Benefit: Cache always up-to-date
Cost: Slower writes (must write to both)

Code:
def update_product(id, data):
    db.update(f"UPDATE products SET ... WHERE id={id}", data)
    redis.setex(f"product:{id}", 3600, json.dumps(data))
    return data
```

### Write-Behind

```
When saving data:

1. Update cache only
2. Return to user immediately
3. Eventually save to database (async)

Benefit: Fast writes
Risk: Data loss if cache fails before DB write

Use case: Non-critical data (analytics, counters)
```

## Performance Improvements

```
Scenario: User session store

Application: Web app with 100K concurrent users
Each user: 5 session requests per session

Traditional (Database):
├─ Session store: PostgreSQL
├─ Queries: 100K users × 5 requests = 500K queries/min
├─ Latency per query: 50ms
├─ Total time: 500K × 50ms = 25,000 seconds (!)
└─ Database instance: db.r5.4xlarge = $1.344/hour

With Redis:
├─ Session store: ElastiCache Redis
├─ Queries: 100K users × 5 requests = 500K queries/min
├─ Latency per query: 1ms
├─ Total time: 500K × 1ms = 500 seconds (50x faster!)
├─ ElastiCache instance: cache.r6g.xlarge = $0.419/hour
└─ Savings: $1.344 - $0.419 = $0.925/hour = $674/month saved!
```

## Data Persistence

### Redis Persistence Options

```
RDB (Snapshots):
├─ Frequency: Every 15 minutes (configurable)
├─ Snapshot size: Database size (compressed)
├─ Recovery time: Few seconds
├─ Data loss: Up to 15 minutes
└─ Cost: Backup storage

AOF (Append-Only File):
├─ Frequency: Every write or every second
├─ File size: Larger (every operation logged)
├─ Recovery time: Minutes (replays operations)
├─ Data loss: Seconds or less
└─ Cost: More disk I/O

Recommendation:
├─ RDB: Good for non-critical caching
├─ AOF: Good for semi-critical data
└─ Both: Maximum durability, some performance hit
```

## Eviction Policies

```
When memory full, what to delete?

LRU (Least Recently Used):
├─ Remove least recently accessed keys
├─ Good for cache-aside pattern
└─ Most common choice

LFU (Least Frequently Used):
├─ Remove least frequently accessed keys
├─ Good when some data always hot
└─ Newer, less common

TTL (Time To Live):
├─ Remove expired keys only
├─ Memory waits for expiration
└─ Good when keys expire naturally

No Eviction:
├─ Return error when memory full
├─ Force application to delete manually
└─ Use: Critical data, scale instead
```

## Best Practices

✅ Use Redis for sessions and complex data
✅ Use Memcached for simple key-value caching
✅ Implement cache-aside pattern
✅ Set appropriate TTLs
✅ Monitor cache hit ratio (target: >80%)
✅ Use Cluster Mode for horizontal scaling
✅ Enable Multi-AZ for high availability
✅ Implement exponential backoff on cache misses
✅ Regular backup testing
✅ Monitor CPU and memory usage

## Common Mistakes

✗ Not setting TTL (stale data forever)
✗ Cache-stampede problem (all request DB on expiry)
✗ Caching too large objects (memory waste)
✗ No cache invalidation strategy (stale data)
✗ Single node (no failover, downtime)
✗ Not monitoring hit ratio (slow performance)
✗ Over-provisioning cache size (cost waste)
✗ Treating cache as persistent (data loss)

## ElastiCache vs DynamoDB

```
When to use each:

ElastiCache (Redis):
├─ Speed critical (sub-millisecond)
├─ Session storage
├─ Real-time leaderboards
├─ Message queues
└─ Temporary data

DynamoDB:
├─ Persistent key-value storage
├─ Complex queries needed
├─ Multi-AZ by default
└─ Managed backups
```

## Next Steps

→ [Redis Cluster Mode](./cluster.md) - Scaling strategies
→ [Cache Patterns](./patterns.md) - Advanced caching
→ [Monitoring](./monitoring.md) - CloudWatch metrics