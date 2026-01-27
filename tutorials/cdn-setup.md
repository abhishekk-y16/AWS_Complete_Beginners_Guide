# CDN Setup with CloudFront

TL;DR
- Use CloudFront to cache and deliver content globally with S3 or custom origins.

Prerequisites
- S3 bucket or web origin and SSL/TLS certificate in ACM (us-east-1 for CloudFront).

Steps
1. Create an S3 bucket and upload content.
2. Request an ACM certificate in `us-east-1` and validate it.
3. Create a CloudFront distribution and set origin to the S3 bucket.
4. Configure caching behavior, error pages, and compressions.

Cost notes
- CloudFront billing includes requests, data transfer, and invalidation fees; set TTLs wisely.

Troubleshooting
- 403 from CloudFront: check bucket policy and origin access identity.

Checklist
- Origin ready, ACM cert issued, distribution deployed.
