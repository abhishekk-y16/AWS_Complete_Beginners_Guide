# Host a Static Website on S3 + CloudFront 🌐

Quick, cheap, and highly available static website hosting using Amazon S3 and CloudFront.

Estimated cost (small site): ~$1–5/month (S3 + CloudFront request/transfer).

Prerequisites:
- A registered domain (optional for custom domain).
- AWS account with S3, CloudFront, and Route 53 (if using AWS DNS).

1) Create an S3 Bucket for the Website

Console:

- S3 → Create bucket
- Bucket name: must be globally unique (example: `my-site.example.com`)
- Region: choose nearest region
- Uncheck "Block all public access" (we will restrict via bucket policy)
- Create

CLI:

```bash
aws s3 mb s3://my-site.example.com --region us-east-1
```

2) Upload Website Files

Console: Upload `index.html`, `404.html`, assets/

CLI (sync folder):

```bash
aws s3 sync ./site/ s3://my-site.example.com --acl public-read
```

3) Configure Static Website Hosting

Console:

- S3 → Bucket → Properties → Static website hosting
- Host website: index document `index.html`, error document `404.html`
- Save

4) Set Bucket Policy (public read)

Example policy (adjust bucket name):

```json
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicReadGetObject",
    "Effect":"Allow",
    "Principal":"*",
    "Action":["s3:GetObject"],
    "Resource":["arn:aws:s3:::my-site.example.com/*"]
  }]
}
```

Apply in S3 Console → Permissions → Bucket policy.

5) Use CloudFront for CDN & HTTPS (recommended)

Why CloudFront:
- Global caching → lower latency
- Free TLS via ACM (when using CloudFront)
- Lower data transfer costs for high traffic

Steps (Console):

1. Go to CloudFront → Create distribution
2. Origin domain: `my-site.example.com.s3.amazonaws.com` (or bucket website endpoint for custom error handling)
3. Viewer protocol policy: Redirect HTTP to HTTPS
4. Cache behavior: Use default
5. Add Alternate Domain Name (CNAME): `www.example.com` and attach ACM certificate (request via ACM in us-east-1)
6. Create distribution (propagation 5–15 minutes)

CLI quick create (basic):

```bash
aws cloudfront create-distribution --origin-domain-name my-site.example.com.s3.amazonaws.com
```

6) Configure Route 53 (optional)

- Create an Alias record pointing your domain (e.g., `www.example.com`) to the CloudFront distribution.

7) Logging, Caching & Invalidations

- Enable CloudFront access logs for analytics.
- To update content immediately: create invalidation:

```bash
aws cloudfront create-invalidation --distribution-id <ID> --paths "/index.html" "/css/*"
```

8) Security Best Practices

- Use CloudFront with S3 OAI (Origin Access Identity) to keep the bucket private and serve only via CloudFront.
- Enable AWS WAF on CloudFront to block common attacks.
- Use S3 versioning and lifecycle policies for backups and cost control.

9) Cost Notes

- S3 storage: $0.023/GB-month (first 50TB) — tiny for static sites.
- CloudFront: requests and transfer vary; small sites often <$5/month.
- Route 53: $0.50/month for hosted zone + small per-query cost.

10) Troubleshooting

- 403 Access Denied: check bucket policy and OAI settings.
- 404 Not Found: ensure `index.html` exists and static hosting configured.
- Custom domain TLS: request ACM certificate in us-east-1 for CloudFront.

Checklist

- [ ] Bucket created and hosting enabled
- [ ] Files uploaded and visible
- [ ] CloudFront distribution created (optional)
- [ ] Custom domain DNS records set (optional)

Related tutorials:
- `cloudfront-cdn.md` (advanced caching and WAF)
- `route53-custom-domain.md` (domain + DNS)

Done — static website hosted with high performance and low cost.
# Tutorials

AWS Tutorials service