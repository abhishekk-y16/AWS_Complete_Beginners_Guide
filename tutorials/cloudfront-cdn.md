# CloudFront CDN

TL;DR
- Use CloudFront to cache and accelerate content delivery from S3, ALB, or custom origins.
- Configure origins, behaviors, and cache TTLs for performance and cost control.
- Use HTTPS, custom domain, and an ACM certificate in us-east-1.
- Invalidate objects selectively to avoid high invalidation costs.
- Monitor cache-hit ratio and edge metrics in CloudWatch.
- Use signed URLs/cookies for private content.

Prerequisites
- Origin content hosted in S3, ALB, or a web server.
- AWS CLI configured and an ACM certificate for custom domain (us-east-1).

Steps
1. Create a distribution with an origin (example uses S3):
```
aws cloudfront create-distribution --origin-domain-name my-bucket.s3.amazonaws.com --default-root-object index.html
```
2. Configure behaviors: enable compression, set TTLs, and forward headers/cookies as needed.
3. Attach an ACM certificate for custom domain (certificate in us-east-1) and set `Aliases`.
4. Deploy and wait for distribution status to become `Deployed` (can take minutes).
5. Use invalidation to refresh cached content:
```
aws cloudfront create-invalidation --distribution-id EXXXXX --paths "/index.html"
```
6. Monitor metrics: `Requests`, `BytesDownloaded`, and `CacheHitRate` in CloudWatch.

Cost notes
- Costs include CloudFront bandwidth and requests plus origin charges (S3/ALB). Invalidation beyond free tier has costs.

Quick troubleshooting
- 403 from S3: ensure bucket policy allows CloudFront origin access or use OAC/OAI.
- Stale content: confirm TTLs and use invalidation.
- SSL issue: verify ACM cert in us-east-1 and domain DNS records.

Checklist
- Distribution deployed and serving from origin.
- Custom domain and ACM certificate configured.
- Cache behavior tuned and invalidation tested.
# Tutorials

AWS Tutorials service