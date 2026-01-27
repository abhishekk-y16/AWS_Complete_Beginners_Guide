# Application Development on AWS

What it is
- Build and run web/mobile apps using managed compute, databases, and CI/CD.

Recommended stack
- Frontend: S3 + CloudFront
- API: API Gateway + Lambda or ECS/Fargate
- Data: RDS or DynamoDB; S3 for assets
- CI/CD: CodePipeline/CodeBuild or GitHub Actions

Quick start
1. Create repo and pipeline (CodePipeline or GitHub Actions) to build and deploy.
2. Deploy API (Lambda/ECS) and database (RDS/DynamoDB) in a VPC.
3. Serve frontend from S3+CloudFront; wire domain via Route 53.

Cost snapshot
- Low traffic: ~$5–30/mo (S3/CloudFront/API GW/Lambda/DynamoDB on-demand). Higher for RDS/ALB.

Success metrics
- Latency <300 ms P95, error rate <1%, deploy time <10 min, cost per user tracked.