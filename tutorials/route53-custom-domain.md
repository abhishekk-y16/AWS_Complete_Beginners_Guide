# Route 53 Custom Domain

TL;DR
- Register or import a domain, create hosted zone, and point records (A/AAAA/CNAME) to CloudFront, ALB, or API Gateway.

Prerequisites
- Domain owned/transferable, access to registrar, AWS account.

Steps
1. Create/Import Hosted Zone in Route 53; update registrar nameservers to the NS values provided.
2. For S3/CloudFront site: create A/AAAA alias to CloudFront distribution.
3. For ALB/API Gateway: create A alias to ALB or regional API endpoint; add ACM certificate in region/us-east-1 for CloudFront.
4. Add CNAMEs for subdomains (e.g., `api.example.com` → API endpoint) and TXT for verification.
5. Set TTLs (300s typical); wait for DNS propagation.

Cost notes
- Route 53 hosted zone (~$0.50/month) + queries; minimal.

Troubleshooting
- DNS not resolving: verify registrar NS updated; check propagation with `nslookup`.
- SSL errors: ensure correct ACM cert in region and domain SAN matches.

Checklist
- Hosted zone active, A/AAAA records set, SSL valid, propagation verified.