# Full-Stack Deployment (Frontend + API + DB)

TL;DR
- Deploy a React/SPA frontend to S3 + CloudFront, an API on API Gateway + Lambda (or ECS), and a database on RDS/DynamoDB.

Prerequisites
- Built frontend assets, container or Lambda for API, AWS CLI configured, domain in Route 53 (optional).

Steps
1. Frontend: build and sync to S3 static bucket, enable static website hosting or set as CloudFront origin.
2. CDN: create CloudFront distribution pointing to S3 origin; attach ACM cert (us-east-1) for HTTPS.
3. API: deploy via API Gateway + Lambda (SAM/Serverless) or ECS/Fargate behind an ALB; expose `/api/*`.
4. Database: choose RDS (relational) or DynamoDB (key-value); enable backups/retention.
5. Wiring: configure CORS on API, set environment variables for DB endpoints/secrets via Secrets Manager.
6. Routing: add Route 53 records (A/AAAA + ALIAS) to CloudFront; optional subdomain `api.example.com` to API.

Cost notes
- S3+CloudFront low; API Gateway+Lambda pay-per-use; RDS costs hourly; watch NAT/data-transfer for private APIs.

Troubleshooting
- 403 on frontend: check S3 bucket policy/CloudFront OAC.
- CORS errors: align allowed origins/headers on API Gateway.
- Slow TTFB: enable CloudFront caching and keep-alive on API.

Checklist
- S3 + CloudFront deployed
- API reachable at `/api`
- DB backups enabled
- DNS + HTTPS live