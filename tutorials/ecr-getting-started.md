# ECR Getting Started

TL;DR
- Use Amazon ECR to store container images securely and integrate with IAM and scanning.

Prerequisites
- Docker and AWS CLI configured.

Steps
1. Create a repository:
```
aws ecr create-repository --repository-name my-app
```
2. Authenticate Docker and push an image:
```
aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
docker tag my-image:latest <account>.dkr.ecr.<region>.amazonaws.com/my-app:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/my-app:latest
```
3. Enable image scanning on push and lifecycle policies for cleanup.

Cost notes
- ECR charges for storage and data transfer; use lifecycle policies to limit unused images.

Troubleshooting
- Push fails: check auth token, repository name, and IAM permissions.

Checklist
- Repo created, image pushed, scanning enabled.
