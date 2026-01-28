# ElastiCache 🚀

Managed in-memory data store for caching and sessions. Redis and Memcached engines.

## Overview

ElastiCache accelerates applications by caching data in-memory. Supports Redis and Memcached. Reduces database load, improves response times. Fully managed: AWS handles patching, backups, failover.

## Key Features

- ✅ Redis and Memcached support
- ✅ Automatic backups and snapshots (Redis)
- ✅ Multi-AZ replication (Redis)
- ✅ Redis Cluster mode for sharding
- ✅ Automatic failover
- ✅ Parameter groups for configuration

## Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| Data Persistence | ✅ Yes | ❌ No |
| Replication | ✅ Multi-AZ | ❌ No |
| Data Structures | Complex | Simple (strings) |
| Use Case | Sessions, cache, queues | Cache only |
| Price | Slightly higher | Lower cost |

## Use Cases

- **Web Sessions**: Store user session data
- **Database Caching**: Cache frequently accessed data
- **Real-time Analytics**: Fast data aggregation
- **Leaderboards**: Sorted sets for rankings
- **Message Queues**: Pub/sub with Redis

## Cluster Modes

- **Disabled**: Single master + replicas
- **Enabled**: Multiple shards for horizontal scaling

## Pricing

- **Node Types**: cache.t3.micro ($0.017/hour) to cache.r6g.xlarge
- **Redis**: $0.017-$0.50/hour depending on type
- **Memcached**: Generally $0.03-$0.40/hour
- **Data Transfer**: Standard AWS rates

Example: 3 cache.t3.small Redis nodes = ~$36/month

## Best Practices

✅ Use Redis for persistence needs
✅ Enable automatic backups
✅ Monitor CPU and memory usage
✅ Use connection pooling
✅ Implement cache invalidation strategy
✅ Enable encryption at rest and in transit

## Connection Methods

From EC2 or ECS:
```
redis-cli -h endpoint -p 6379
```

From application code:
- Python: redis-py library
- Node.js: redis package
- Java: Jedis or Lettuce
- Go: go-redis

## Failover & Availability

- **Redis Single-AZ**: Data loss on failure
- **Redis Multi-AZ**: Automatic failover, no data loss
- **Memcached**: Data loss always (no persistence)

## Next Steps

→ [ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/)
→ [Redis Cheatsheet](https://redis.io/docs/)
→ [ElastiCache Console](https://console.aws.amazon.com/elasticache/)