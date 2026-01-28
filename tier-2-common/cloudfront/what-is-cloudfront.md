# What is CloudFront? 🚀

AWS's content delivery network (CDN) that caches content at edge locations worldwide.

## Core Concept

**CloudFront** delivers content from servers located around the world, reducing latency and improving performance.

```
Without CloudFront:
├─ User in Tokyo requests image
├─ Content fetched from US server
├─ 200ms latency (slow!)
└─ Users frustrated

With CloudFront:
├─ User in Tokyo requests image
├─ CloudFront serves from Tokyo edge
├─ 20ms latency (10x faster!)
└─ Users happy
```

## How CloudFront Works

```
First Request:
├─ User in Sydney requests image
├─ CloudFront edge in Sydney doesn't have it
├─ Fetches from origin (US S3 bucket)
├─ Returns to user (first time slower)
└─ Caches for future requests

Second Request:
├─ User in Sydney requests same image
├─ CloudFront edge has cached copy
├─ Returns instantly from Sydney
└─ Origin server not hit!

Third Request (different user Sydney):
├─ Another Sydney user requests same image
├─ CloudFront serves from cache
├─ No origin fetch needed
└─ Everyone benefits from cache!
```

## Key Components

### Distribution

```
Distribution: "Web App Content"
├─ Domain: d123.cloudfront.net
├─ Origin: S3 bucket, Load Balancer, EC2
├─ Behavior Rules: Route requests
├─ Cache Settings: TTL, compression
├─ Price Class: Edge locations to use
└─ SSL: HTTPS enabled
```

### Cache Behavior

```
Path /images/*:
├─ Origin: S3 bucket
├─ TTL: 1 day (86400 seconds)
├─ Compress: Yes (gzip)
└─ Headers cached: Authorization

Path /api/*:
├─ Origin: API Gateway
├─ TTL: 0 (no cache, always fresh)
└─ Forward: All headers

Default:
├─ Origin: Load Balancer
├─ TTL: 1 hour
└─ Compress: Yes
```

## Edge Locations

CloudFront has 400+ edge locations worldwide:

```
Used by users in:
├─ North America: 100+ edges
├─ Europe: 80+ edges
├─ Asia: 60+ edges
├─ South America: 20+ edges
└─ Africa: 15+ edges

Result: ~99% of internet users within 50ms
```

## Caching Behavior

### Object Caching

```
TTL (Time To Live): How long to cache

Static content (images, CSS):
├─ TTL: 1 year (31536000 seconds)
├─ Almost never changes
└─ Huge performance gain

Semi-dynamic content (HTML):
├─ TTL: 1 hour (3600 seconds)
├─ Changes occasionally
└─ Balance freshness + performance

Dynamic content (API responses):
├─ TTL: 0 (no cache)
├─ Always fresh
└─ Straight to origin
```

## Cost Analysis

```
Scenario: SaaS app with 10M page views/month

Average response: 500KB
Total data: 10M × 500KB = 5TB

Without CloudFront:
├─ Data from origin (S3): 5TB × $0.09/GB = $450
└─ No compression (uncompressed)

With CloudFront (80% hit ratio):
├─ Origin fetch (20%): 1TB × $0.09/GB = $90
├─ CloudFront requests: 10M × $0.0075 = $75
└─ Compression benefits: 85% reduction
```

## Real-World Example: Video Streaming

```
Setup: Netflix-like video streaming

Origin: S3 bucket (100TB videos)
├─ 200 Mbps bandwidth
├─ Located in us-east-1
└─ Cost: $0.085/GB data out

With CloudFront:
├─ User in Tokyo downloads video
├─ 50 Mbps from Tokyo edge (fast)
├─ Edge fetches from S3 (once)
├─ Hit ratio: 80%
└─ Massive bandwidth savings!
```

## Best Practices

✅ Enable compression for text
✅ Use S3 with Origin Access Identity
✅ Set appropriate TTL values
✅ Use signed URLs for sensitive content
✅ Enable HTTPS/TLS
✅ Monitor cache hit ratio
✅ Set Cache-Control headers
✅ Invalidate cache when needed
✅ Use appropriate price class
✅ Enable access logs

## Next Steps

→ [Distributions](./distributions.md) - Setup and configuration
→ [Caching Strategy](./caching.md) - Optimize hit ratio
→ [Performance Optimization](./performance.md) - Advanced tuning