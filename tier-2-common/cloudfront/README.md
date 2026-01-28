# CloudFront 🌍

Global Content Delivery Network (CDN) for fast, secure content delivery worldwide.

## Overview

CloudFront caches and serves content from 400+ edge locations near users globally. Instead of serving from origin, users fetch from nearest edge (5-10ms latency instead of 50-200ms).

## Key Features

- ✅ 400+ edge locations worldwide
- ✅ Automatic caching
- ✅ Compression (gzip, brotli)
- ✅ HTTPS/SSL support
- ✅ AWS WAF integration
- ✅ Origin access identity (S3 security)
- ✅ Signed URLs (time-limited access)
- ✅ Real-time logs

## Origins Supported

- S3 buckets
- EC2/ELB instances
- API Gateway
- HTTP endpoints
- AWS Media Store

## Caching

- **TTL** (Time To Live): Customize per path
  - /images/* → 1 year
  - /api/* → 1 minute
- **Invalidation**: Update cache on demand ($0.005 after first 3,000)
- **Cache keys**: URL, query strings, headers, cookies

## Pricing

```
Data transfer out: $0.085/GB (cheapest at scale)
HTTP requests: $0.0075 per 10,000 requests
Invalidations: $0.005 each (after 3,000 free/month)
```

Example: 100GB/month = $8.50/month

## Use Cases

**Static Websites**: HTML, CSS, JS (perfect with S3)
**Video Streaming**: Large files from edge
**API Caching**: Cache responses, reduce backend
**Software Distribution**: Global downloads

## Best Practices

✅ Always use for static assets
✅ Set appropriate cache TTLs
✅ Enable compression
✅ Use origin access identity for S3
✅ Enable HTTP/2
✅ Monitor with CloudWatch
✅ Use WAF for DDoS protection

## Related Topics

- [CloudFront Distributions](./distributions.md)
- [S3 Storage](../../storage/s3/what-is-s3.md)
- [Route 53 DNS](./route53/README.md)

## Resources

- [CloudFront Docs](https://docs.aws.amazon.com/cloudfront/)
- [Pricing Calculator](https://aws.amazon.com/cloudfront/pricing/)