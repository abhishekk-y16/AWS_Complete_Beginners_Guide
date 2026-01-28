# What is ECR? 📦

AWS's Elastic Container Registry for storing, managing, and deploying Docker container images.

## Core Concept

**ECR** is a fully managed Docker registry. Store, version, and deploy container images without managing infrastructure.

```
Manual Docker Registry:
├─ Run a registry server
├─ Manage storage
├─ Handle authentication
├─ Monitor registry uptime
├─ Scale storage
└─ Complex

ECR:
├─ AWS manages infrastructure
├─ Automatic replication
├─ Built-in security scanning
├─ Integration with ECS/EKS
└─ Simple, managed
```

## Repository Structure

```
Organization setup:

ECR Account:
├─ Repository 1: frontend
│  ├─ Tag: v1.0.0
│  ├─ Tag: v1.1.0
│  ├─ Tag: latest (most recent)
│  └─ Tag: dev (development build)
├─ Repository 2: api
│  ├─ Tag: v2.0.0
│  ├─ Tag: v2.1.0
│  └─ Tag: latest
└─ Repository 3: worker
   ├─ Tag: v1.2.0
   └─ Tag: latest

Image URI format:
├─ aws_account_id.dkr.ecr.region.amazonaws.com/repository:tag
├─ Example: 123456789.dkr.ecr.us-east-1.amazonaws.com/frontend:v1.0.0
└─ Used to pull images
```

## Image Lifecycle

### Build and Push

```
Developer workflow:

Step 1: Build locally
├─ docker build -t frontend:v1.2.0 .
└─ Creates image on local machine

Step 2: Authenticate with ECR
├─ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
└─ Credentials provided

Step 3: Tag for ECR
├─ docker tag frontend:v1.2.0 123456789.dkr.ecr.us-east-1.amazonaws.com/frontend:v1.2.0
└─ Rename to ECR format

Step 4: Push to ECR
├─ docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/frontend:v1.2.0
└─ Image uploaded (50MB example = few seconds)

Result: Image stored in ECR, accessible globally
```

### Security Scanning

```
Vulnerability scanning (automatic):

Image pushed: ubuntu:latest

Scan process:
├─ Break image into layers
├─ Compare against vulnerability database
├─ Identify known CVEs
└─ Generate report

Report shows:
├─ CRITICAL: 5 vulnerabilities
│  ├─ OpenSSL CVE-2021-1234 (exploitable)
│  ├─ Curl CVE-2021-5678 (DoS)
│  └─ Libc CVE-2021-9012 (buffer overflow)
├─ HIGH: 12 vulnerabilities
├─ MEDIUM: 25 vulnerabilities
└─ LOW: 50 vulnerabilities

Action: Update base image, rescan
```

## Pricing Model

```
Cost breakdown:

Storage:
├─ $0.10 per GB/month
├─ Example: 10 repositories, 50GB each = 500GB
├─ Cost: 500 × $0.10 = $50/month
└─ Images retained until deleted

Data transfer OUT:
├─ $0.02 per GB
├─ Pulling images (ECS, developers)
├─ Example: ECS pulls 10GB/day
├─ Monthly: 10 × 30 = 300GB
├─ Cost: 300 × $0.02 = $6/month
└─ Transfer within region: Free!

Image scans:
├─ $0.005 per image scanned
├─ Daily scanning: 30 repositories
├─ Monthly: 30 × 30 = 900 scans
├─ Cost: 900 × $0.005 = $4.50/month
└─ Optional (but recommended)

Total ECR cost: ~$60.50/month
Plus: ECS/EKS costs (separate)
```

## Real-World Example: Microservices

```
Setup: SaaS with 5 microservices

Service architecture:

Frontend:
├─ Image size: 150MB (Node.js, React build)
├─ Tags: v2.0.0, v1.9.5, v1.8.0, latest
├─ Total: 4 × 150MB = 600MB
└─ Deploy: Every 2 days (3 per month)

API:
├─ Image size: 300MB (Python, dependencies)
├─ Tags: v3.1.0, v3.0.5, v2.9.0, latest
├─ Total: 4 × 300MB = 1.2GB
└─ Deploy: Weekly (4 per month)

Worker:
├─ Image size: 250MB (Python, heavy libs)
├─ Tags: v1.5.0, v1.4.0, v1.3.0, latest
├─ Total: 4 × 250MB = 1GB
└─ Deploy: Bi-weekly (2 per month)

Database migrate:
├─ Image size: 100MB
├─ Tags: v2.1.0, v2.0.0, v1.9.0
├─ Total: 3 × 100MB = 300MB
└─ Deploy: Monthly (1 time)

Utility functions:
├─ Image size: 80MB
├─ Tags: v1.2.0, v1.1.0, v1.0.0
├─ Total: 3 × 80MB = 240MB
└─ Deploy: Quarterly

Total storage: 600MB + 1.2GB + 1GB + 300MB + 240MB = 3.34GB
Storage cost: 3.34 × $0.10 = $0.334/month (negligible)

Data pulls/month:
├─ Frontend: 30 ECS updates × 150MB = 4.5GB
├─ API: 50 ECS updates × 300MB = 15GB
├─ Worker: 20 ECS updates × 250MB = 5GB
├─ Database migrate: 1 deployment × 100MB = 0.1GB
├─ Utility: 0.5 deployments × 80MB = 0.04GB
└─ Total: ~24.64GB/month

Data transfer cost: 24.64 × $0.02 = $0.49/month
Image scanning: 5 services × 2 scans/week = 40/month
Scanning cost: 40 × $0.005 = $0.20/month

Total ECR cost: ~$1/month (very cheap!)
```

## Integration with ECS

```
ECS deployment workflow:

Step 1: Developer pushes code
├─ git push origin main
└─ GitHub webhook triggers

Step 2: Build pipeline
├─ CodeBuild: Compile and build Docker image
├─ Build output: Docker image, say 200MB
└─ Tagged: 123456789.dkr.ecr.us-east-1.amazonaws.com/api:v2.3.0

Step 3: Scan for vulnerabilities
├─ ECR automatically scans
├─ Reports: 2 HIGH, 15 MEDIUM vulnerabilities
├─ Decision: Deploy anyway (acceptable risk)
└─ Tag as "latest"

Step 4: Update task definition
├─ Update image URI to api:v2.3.0
└─ Create new task definition version

Step 5: Trigger ECS deployment
├─ ECS pulls image from ECR
├─ Starts new containers
├─ Health checks pass
├─ Old containers stopped (rolling deployment)
└─ Service updated

End result: Code changes live in 3-5 minutes!
```

## Best Practices

✅ Use semantic versioning for tags (v1.2.0)
✅ Always push images to ECR (not local only)
✅ Use specific tags, not just :latest
✅ Enable image scanning for all repos
✅ Implement tag immutability (prevent overwrites)
✅ Use lifecycle policies to clean old images
✅ Monitor storage size
✅ Integrate with CI/CD pipeline
✅ Use cross-account access for multi-account setups
✅ Regular cleanup of unused images

## Common Mistakes

✗ Using :latest tag exclusively (unpredictable)
✗ Not scanning for vulnerabilities (security risk)
✗ Storing large unnecessary files (costs money)
✗ Pushing images without versioning (can't rollback)
✗ Not cleaning old images (storage bloat)
✗ Manual image pushes (error-prone)
✗ Storing secrets in images (security issue)
✗ Not implementing lifecycle policies
✗ Large base images (slow deploys, high cost)

## ECR Features

### Lifecycle Policies

```
Delete old images automatically:

Rule 1: Delete images not used in 30 days
├─ Target: Development tags
├─ Condition: Untagged images
└─ Retention: Keep only last 10

Rule 2: Delete if > 50 images
├─ Target: All images
├─ Condition: Count-based
└─ Keep: Most recent 50 only

Result:
├─ Storage manageable
├─ No manual cleanup
└─ Cost controlled
```

### Cross-Region Replication

```
Setup:
├─ Source: us-east-1 ECR
├─ Destination: eu-west-1 ECR
└─ Trigger: Push to source

Effect:
├─ Image pushed to us-east-1
├─ Automatically copied to eu-west-1
├─ Same tag, both regions
└─ Deploy faster (local registry)
```

## Next Steps

→ [Building Images](./building.md) - Dockerfile best practices
→ [CI/CD Integration](./ci-cd.md) - Automated deployment
→ [Lifecycle Management](./lifecycle.md) - Image cleanup