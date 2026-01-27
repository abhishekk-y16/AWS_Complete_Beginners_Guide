# AWS Performance Optimization 🚀

How to make your AWS infrastructure fast.

## Database Performance

### 1. Add Indexes

**Problem:**
```sql
-- This query scans entire table (slow!)
SELECT * FROM users WHERE email = 'john@example.com'

Time: 5 seconds (100k rows scanned)
```

**Solution:**
```sql
-- Create index on email column
CREATE INDEX idx_email ON users(email);

-- Same query now
SELECT * FROM users WHERE email = 'john@example.com'

Time: 10ms (direct lookup!)
```

### 2. Use Read Replicas

**Problem:**
```
One database handling all traffic
- Write operations slow
- Read operations compete with writes
- Report queries impact production
```

**Solution:**
```
Production DB (handle writes)
    ↓
Read Replicas (handle reads)
├─ For reports
├─ For analytics
└─ For other apps

Same data, no contention
```

### 3. Enable Query Cache

**Problem:**
```
Same queries run repeatedly
- Database processes same queries
- Returns same results
- Wastes CPU
```

**Solution:**
```
Query Cache enabled (some engines)
First request: compute result (100ms)
Subsequent requests: return from cache (1ms)

Savings: 99% faster for cached queries!
```

### 4. Denormalization

**Problem:**
```sql
-- Every report needs JOINs (slow)
SELECT u.name, COUNT(o.id)
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id

Time: 2 seconds (complex JOIN)
```

**Solution:**
```sql
-- Store pre-computed data
CREATE TABLE user_stats (
  user_id INT,
  name VARCHAR,
  order_count INT,
  total_spent DECIMAL
)

-- Updated daily by scheduled job
SELECT * FROM user_stats WHERE user_id = 123

Time: 10ms (simple lookup!)
```

## Caching Strategy

### 1. CloudFront CDN

**Problem:**
```
Users worldwide all fetch from origin
- User in Australia fetches from us-east-1
- 200ms latency (slow!)
```

**Solution:**
```
CloudFront caches at edge locations
- User in Australia fetches from nearby edge
- 10-50ms latency (fast!)
- Cache hit ratio: 80-90%
```

**Setup:**
```
CloudFront Distribution
├─ Origin: ALB or S3
├─ Behaviors: /api/* → 0s cache, /images/* → 1 month cache
├─ Compression: gzip enabled
└─ HTTP/2: enabled
```

### 2. ElastiCache

**Problem:**
```
Database queries for every user action
- User loads profile (query)
- User loads dashboard (query)
- User loads recommendations (query)
- Slow! Database overloaded!
```

**Solution:**
```
In-memory cache layer
- User loads profile
- If in cache: return immediately (1ms)
- If not in cache: fetch from DB, cache it

Result:
- 90% of requests cached
- Database load reduced 10×
- Response time: 100ms → 5ms
```

**Setup:**
```
ElastiCache Redis Cluster
Application code:
try {
    result = cache.get('profile:123')
} catch {
    result = database.get('profile:123')
    cache.set('profile:123', result, 1 hour)
}
```

### 3. Application-Level Cache

**Problem:**
```python
# Expensive computation
def get_top_products():
    return database.query("""
        SELECT p.*, COUNT(o.id) as orders
        FROM products p
        JOIN order_items oi ON p.id = oi.product_id
        GROUP BY p.id
        ORDER BY orders DESC
        LIMIT 10
    """)

# Called 1000s of times/minute
# Each call runs expensive query!
```

**Solution:**
```python
# Cache for 1 hour
@cache.cached(timeout=3600)
def get_top_products():
    return database.query(...same query...)

# First call: runs query (1000ms)
# Next 3600 calls: returns cache (1ms)
# Savings: 99% faster!
```

## Compute Optimization

### 1. Right-Size Instances

**Problem:**
```
Running t3.xlarge (4 vCPU, 16GB RAM)
But only using:
- 10% CPU
- 20% memory

Wasting 90% of capacity!
```

**Solution:**
```
Use AWS Compute Optimizer
↓
Recommends: Switch to t3.small (-70% cost)
↓
Save $150/month on single instance
```

### 2. Auto Scaling

**Problem:**
```
Fixed 10 EC2 instances all day
- Off-peak: 80% idle (wasted)
- Peak: 100% loaded (slow)
```

**Solution:**
```
Auto Scaling Group
- Min: 2 instances
- Desired: varies based on load
- Max: 20 instances

Off-peak: 2 instances
Peak: 15 instances

Savings: 70% on compute costs!
Response time: Always fast!
```

### 3. Spot Instances

**Problem:**
```
On-demand instance: $50/month
But only need 50% of time
```

**Solution:**
```
Spot instances: $15/month (70% discount)
Can be terminated anytime

Use for:
- Batch jobs
- Development/testing
- Non-critical workloads

Combine with on-demand for reliability
```

## Network Optimization

### 1. Reduce Latency

**Problem:**
```
Data travels: User → CloudFront → ALB → Lambda → RDS → S3
Multiple hops, multiple regions = 100ms+
```

**Solution:**
```
Reduce hops:
- Use local caching (1ms)
- Collocate in same AZ (1ms)
- Use local storage (1ms)

Result: 100ms → 10ms (10× faster!)
```

### 2. Connection Pooling

**Problem:**
```
Each request creates new database connection
- Connection setup: 50ms
- Query: 20ms
- Connection close: 10ms
- Total: 80ms per request

1000 requests = 80 seconds overhead!
```

**Solution:**
```
Reuse connections (connection pool)
- Setup once: 50ms
- Reuse 100×: 100 requests × 20ms = 2000ms
- Per request: 20ms (4× faster!)
```

**Setup:**
```python
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://...',
    pool_size=10,  # Keep 10 connections open
    max_overflow=20  # Allow up to 20 more
)

# Connections reused automatically
```

### 3. Batch Operations

**Problem:**
```
Send 1000 requests to update 1000 items
- Network round trips: 1000
- Processing: 1000 API calls
- Time: 10 seconds

Each request: 10ms
```

**Solution:**
```
Batch update 1000 items in 1 request
- Network round trips: 1
- Processing: 1 batch operation
- Time: 100ms

Each item: 0.1ms (100× faster!)
```

## Application Performance

### 1. Async Processing

**Problem:**
```
User uploads file
- Resize image: 2 seconds
- Upload to S3: 1 second
- Send email: 1 second
- Total: 4 seconds (user waits!)
```

**Solution:**
```
User uploads file
- Queue message immediately (10ms)
- Return response (user happy!)

Background:
- Lambda reads from queue
- Resize image
- Upload to S3
- Send email
(User not waiting)
```

### 2. Compression

**Problem:**
```
JavaScript bundle: 2MB
Network transfer: 200ms
User experience: Slow
```

**Solution:**
```
Enable gzip compression: 2MB → 600KB
Network transfer: 60ms
User experience: Fast (70% faster!)

Enable in CloudFront:
✓ Compress automatically
✓ Gzip enabled
✓ Brotli enabled
```

### 3. CDN for Content

**Problem:**
```
User in Tokyo downloads from us-east-1
- Network latency: 150ms
- Load time: 2 seconds
```

**Solution:**
```
CloudFront serves from edge location in Tokyo
- Network latency: 10ms
- Load time: 200ms (10× faster!)
```

## Monitoring Performance

### CloudWatch Metrics

```
EC2:
- CPU Utilization: Should be 60-80% (not 10% or 95%)
- Network In/Out: Check for bottlenecks
- Disk I/O: Should not be maxed out

RDS:
- CPU Utilization: 60-80% ideal
- Database Connections: Should have headroom
- Read/Write Latency: Should be <5ms

Lambda:
- Duration: Track average execution time
- Memory Usage: Actual memory used
- Throttled Requests: Should be zero
```

### Set Performance Alarms

```
CloudWatch → Alarms
├─ CPU > 80% for 5 minutes → Scale up
├─ Database connections > 100 → Alert
├─ Lambda duration > 5 seconds → Investigate
└─ Error rate > 1% → Alert
```

## Performance Optimization Checklist

🔴 **CRITICAL**
- ✅ Database indexes created
- ✅ CloudFront enabled for static assets
- ✅ Caching strategy implemented

🟠 **HIGH**
- ✅ Auto Scaling configured
- ✅ Read replicas for heavy queries
- ✅ Connection pooling enabled

🟡 **IMPORTANT**
- ✅ Compression enabled
- ✅ Async processing for long operations
- ✅ CloudWatch monitoring set up

## 📖 Related Resources

- [ElastiCache Documentation](../tier-2-common/elasticache/README.md)
- [CloudFront Documentation](../tier-2-common/cloudfront/README.md)
- [RDS Documentation](../tier-1-foundational/rds/README.md)
- [Cost Optimization](cost-optimization.md)
- [CloudWatch Monitoring](../tier-2-common/cloudwatch/README.md)