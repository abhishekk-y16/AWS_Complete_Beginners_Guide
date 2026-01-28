# CloudFront Distributions 🚀

How to create and configure CloudFront distributions for global content delivery.

## What is a Distribution?

```
CloudFront Distribution: Configuration for global delivery

├─ Origin: Where content lives
│  ├─ S3 bucket
│  ├─ EC2 instance
│  ├─ Load balancer
│  ├─ Custom origin (your server)
│  └─ API Gateway
│
├─ Delivery: How content reaches users
│  ├─ Edge locations (210+ worldwide)
│  ├─ Regional edge caches
│  └─ Origin
│
├─ Caching: How long to keep content
│  ├─ Images: 1 month
│  ├─ HTML: 1 day
│  ├─ API responses: 1 hour
│  └─ Custom: You decide
│
└─ Behavior: Rules for handling requests
   ├─ Path patterns (e.g., /api/* vs /static/*)
   ├─ Compression (gzip, brotli)
   ├─ HTTPS redirect
   └─ Custom headers
```

## Creating a Distribution

### Step 1: Access CloudFront

```
1. AWS Console → CloudFront
2. Click: "Create distribution"
3. Choose: "Web" or "RTMP"
   └─ (Web for most use cases)
```

### Step 2: Configure Origin

```
Origin Settings:

1. Origin Domain Name
   ├─ S3 bucket: mybucket.s3.amazonaws.com
   ├─ EC2 instance: ec2-1-2-3-4.compute.amazonaws.com
   ├─ Custom: api.example.com
   └─ Load Balancer: alb-1234.elb.amazonaws.com

2. Origin Type
   ├─ S3 origin
   │  └─ Uses: OAI (Origin Access Identity)
   │  └─ Restricts: Only CloudFront can access S3
   │
   ├─ Custom origin (HTTP/HTTPS)
   │  ├─ Protocol: HTTP or HTTPS
   │  ├─ Port: 80 (HTTP) or 443 (HTTPS)
   │  └─ Requires: Public endpoint
   │
   └─ Custom origin (TCP)
      ├─ Any TCP port
      └─ For: Non-HTTP protocols

3. Protocol Policy
   ├─ HTTP only
   │  └─ Faster (no SSL overhead)
   │
   ├─ HTTPS only
   │  └─ Secure (required for modern apps)
   │
   └─ Match viewer
      └─ HTTP ➜ HTTP, HTTPS ➜ HTTPS
```

### Step 3: Configure Caching

```
Cache Settings:

1. Default TTL (Time To Live)
   ├─ How long CloudFront caches content
   ├─ Examples:
   │  ├─ Images: 2592000 (30 days)
   │  ├─ CSS/JS: 86400 (1 day)
   │  ├─ HTML: 3600 (1 hour)
   │  └─ API: 0 (no caching)
   └─ HTTP headers override this

2. Maximum TTL
   ├─ Never cache longer than this
   └─ Safety limit (e.g., 31536000 = 1 year)

3. Cache Headers
   ├─ Respect origin headers
   │  └─ Use: Cache-Control from origin
   │
   └─ Custom headers
      ├─ Set: Custom Cache-Control
      └─ Ignore: Origin headers

4. Query Strings
   ├─ Include in cache key?
   ├─ Example: /api?user=100&type=json
   │  └─ Different queries = Different cache entries
   │
   └─ Forward all / None / Whitelist
```

### Step 4: Configure Behaviors

```
Behaviors: Route patterns

1. Default Behavior
   ├─ Path: /* (everything)
   ├─ Origin: Select origin
   ├─ Viewer Protocol Policy
   │  ├─ Allow all: HTTP + HTTPS
   │  ├─ Redirect HTTP to HTTPS
   │  └─ HTTPS only
   └─ Caching: Settings above

2. Additional Behaviors
   ├─ Example 1: /api/*
   │  ├─ Origin: API endpoint
   │  ├─ Cache: 0 (no caching)
   │  └─ Forward headers: All
   │
   ├─ Example 2: /static/*
   │  ├─ Origin: S3 bucket
   │  ├─ Cache: 30 days
   │  └─ Compress: On
   │
   └─ Example 3: /admin/*
      ├─ Origin: Internal server
      ├─ Cache: 0 (no caching)
      └─ Restrict: Allowed IPs only

Path Pattern Priority:
├─ Specific patterns first
│  └─ /api/* ➜ /api/users matches here
│
└─ /* (default) last
   └─ Everything else ➜ Default behavior
```

### Step 5: Configure HTTPS

```
SSL Certificate:

1. Certificate Source
   ├─ CloudFront default
   │  └─ *.cloudfront.net (free)
   │  └─ Good for: CDN distribution
   │
   └─ Custom SSL Certificate
      ├─ From AWS Certificate Manager (ACM)
      ├─ Custom domain (example.com)
      └─ Requires: ACM certificate setup

2. Protocol Policy
   ├─ Allow all (HTTP + HTTPS)
   ├─ Redirect HTTP ➜ HTTPS
   └─ HTTPS only

Recommendation:
└─ Always use: "Redirect HTTP to HTTPS"
```

### Step 6: Configure Compression

```
Automatic Compression:

1. Enable Compression
   ├─ Compress: Yes
   ├─ File types: Automatically selected
   └─ Reduces: ~70% for text files

2. Compressible Types
   ├─ application/json
   ├─ application/xml
   ├─ text/html
   ├─ text/css
   ├─ text/javascript
   └─ text/plain

3. Benefits
   ├─ 100KB file ➜ 30KB compressed
   ├─ User gets: Faster download
   ├─ Bandwidth: 70% savings
   └─ CloudFront: Automatic gzip/brotli

Recommendation:
└─ Always: Enable compression
```

## Distribution Settings

### Custom Headers

```
Add custom headers to origin requests:

1. Origin Custom Headers
   ├─ Add: X-Custom-Header
   ├─ Value: my-secret-value
   └─ Use: Authentication to origin

2. Example: Restrict origin access
   ├─ Header: Authorization
   ├─ Value: Bearer token-123456
   └─ Origin validates: Only CloudFront requests

3. Viewer Response Headers
   ├─ Add: X-Cache-Status
   ├─ Value: Hit or Miss
   └─ Debugging: See cache status
```

### Geo-Restrictions

```
Restrict access by country:

1. Whitelist (Allow specific countries)
   ├─ Allowed: US, UK, CA
   ├─ Others: Blocked (403 Forbidden)
   └─ Use: License restrictions

2. Blacklist (Block specific countries)
   ├─ Blocked: CN, RU, KP
   ├─ Others: Allowed
   └─ Use: Compliance requirements

3. Implementation
   ├─ Geolocation based on IP
   └─ CloudFront: Automatic detection
```

### Logging

```
Enable logging:

1. Access Logs
   ├─ Destination: S3 bucket
   ├─ Prefix: cloudfront-logs/
   └─ Logs: Every request (1000+ per hour)

2. Log Contents
   ├─ timestamp
   ├─ client_ip
   ├─ bytes
   ├─ request_path
   ├─ status_code (200, 304, 404, etc.)
   ├─ referrer
   ├─ user_agent
   └─ cache_status (Hit, Miss, Error)

3. Cost
   ├─ Storage: S3 charges (minimal)
   ├─ Analysis: Athena queries (optional)
   └─ Usually < $1/month for small sites
```

## Cache Behaviors - Detailed Examples

### Example 1: Website with Static + API

```
Website structure:

/                     ➜ HTML (cache 1 hour)
/css/*                ➜ Stylesheets (cache 1 month)
/js/*                 ➜ JavaScript (cache 1 month)
/images/*             ➜ Images (cache 1 month)
/api/*                ➜ API (no cache, forward cookies)

Behaviors configuration:

Behavior 1: /api/*
├─ Origin: API endpoint
├─ Cache: 0 (no caching)
├─ Forward headers: All
├─ Forward cookies: All
└─ Compress: Off (APIs typically pre-compressed)

Behavior 2: /images/*
├─ Origin: S3 bucket
├─ Cache: 2592000 (30 days)
├─ Compress: On
└─ Query strings: Ignored

Behavior 3: /css/* or /js/*
├─ Origin: S3 bucket
├─ Cache: 2592000 (30 days)
├─ Compress: On
└─ Query strings: Ignored

Behavior 4: /* (default)
├─ Origin: Web server
├─ Cache: 3600 (1 hour)
├─ Compress: On
├─ Forward headers: Host, CloudFront-Viewer-*
└─ Forward cookies: Session cookie
```

### Example 2: API with Cache Busting

```
API versioning:

/v1/api/*             ➜ Cache: 0 (no cache)
/v2/api/*             ➜ Cache: 0 (no cache)
/static/v1/*          ➜ Cache: 1 month (versioned)

Cache busting:

Static file:
├─ /static/v1/app.js (hashed version)
├─ CloudFront: Cache 1 month
├─ Update? New version: /static/v2/app.js
└─ No cache invalidation needed!

Dynamic API:
├─ /v2/api/users -> Cache: 0
├─ Response headers: Cache-Control: max-age=0
└─ Origin: Always fetched fresh
```

## Invalidation

### When to Invalidate Cache

```
Invalidation: Force CloudFront to fetch fresh content

1. Update website content
   ├─ Change: index.html
   ├─ Invalidate: /index.html
   └─ CloudFront: Fetches fresh immediately

2. Cost
   ├─ First 3,000 invalidations/month: Free
   ├─ After: $0.005 per invalidation
   └─ Daily updates: Still free!

3. Path patterns
   ├─ /* (all paths): Clear everything
   ├─ /images/* (specific path): Clear just images
   └─ /index.html (specific file): Clear one file
```

### Invalidation Example

```
Updated product image:

1. Upload new image to S3
   └─ /images/products/123.jpg

2. Invalidate CloudFront
   └─ Path: /images/products/123.jpg

3. Wait: < 1 minute for invalidation
   └─ Users: Now get latest image

Without invalidation:
└─ Users: See old image for 30 days (until TTL)
```

## Cost Optimization

### Reducing CloudFront Costs

```
1. Increase Cache TTL
   ├─ More cache hits = Lower bandwidth
   ├─ 30 days cache: More hits
   ├─ 1 hour cache: More origin requests
   └─ Impact: 50%+ cost reduction

2. Enable Compression
   ├─ Reduces: Data transfer by 70%
   ├─ HTML/CSS/JS: 30KB instead of 100KB
   └─ Impact: Saves ~$5 per 1GB daily traffic

3. Use Cache Keys
   ├─ Forward only necessary headers
   ├─ Avoid: Unnecessary query strings
   └─ Impact: Better cache hit ratio

4. Price Classes
   ├─ All edge locations: Most expensive
   ├─ 200 locations: ~30% cheaper
   └─ 100 locations: ~60% cheaper

5. Examples
   ├─ Typical website: ~$0.10-0.50/month
   ├─ Video distribution: ~$1-10/month
   ├─ Large SaaS: ~$100-1,000/month
   └─ Global platform: ~$10,000+/month
```

## Best Practices

✅ Enable compression
✅ Use appropriate cache TTLs
✅ Set up proper cache headers (Cache-Control)
✅ Use versioning for cache busting (v1/, v2/)
✅ Forward only necessary headers
✅ Enable logging for debugging
✅ Monitor cache hit ratio
✅ Use HTTPS for security
✅ Set geo-restrictions if needed
✅ Regular performance monitoring

## Next Steps

→ [What is CloudFront](./what-is-cloudfront.md) - Full overview