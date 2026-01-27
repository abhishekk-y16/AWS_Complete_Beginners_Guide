# Serverless Web App

TL;DR
- Host frontend on S3+CloudFront and backend on API Gateway + Lambda; optional DynamoDB for data.

Prerequisites
- Built frontend assets, Lambda backend, AWS CLI, domain (optional).

Steps
1. Upload frontend build to S3; enable OAC/Block Public Access and set index/error documents.
2. Create CloudFront distribution with S3 origin; cache static assets; add ACM cert (us-east-1) for HTTPS.
3. Build backend: API Gateway routes → Lambda functions; add CORS for CloudFront domain.
4. Persist data in DynamoDB; use IAM roles instead of static keys.
5. Wire domain via Route 53 A/AAAA alias to CloudFront; add environment configs via `env.js` or CloudFront headers.

Cost notes
- Low for light traffic: S3/CloudFront + API Gateway + Lambda + DynamoDB on-demand; watch NAT/data transfer if Lambdas in VPC.

Troubleshooting
- SPA routing 403/404: configure CloudFront custom error to serve `index.html` on 403/404.
- Mixed content: ensure HTTPS URLs for APIs and assets.

Checklist
- CloudFront working, API reachable, CORS correct, caching tuned, domain/SSL valid.