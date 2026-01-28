# ECR - Elastic Container Registry 📦

Managed Docker container image registry with security scanning and IAM integration.

## Overview

ECR is Docker Hub for AWS. Store container images privately, manage versions, scan for vulnerabilities. Integrate with ECS, EKS, Lambda for deployment. Private by default with automatic encryption.

## Key Features

- ✅ Private container image repositories
- ✅ Image versioning and tagging
- ✅ Automatic encryption at rest
- ✅ ECR image scanning (CVE detection)
- ✅ IAM access control
- ✅ Lifecycle management policies

## Security

- ✅ ECR image scanning for vulnerabilities
- ✅ CVE detection from known databases
- ✅ Compliance with security standards
- ✅ IAM-based access control
- ✅ Encryption at rest and in transit

## Integration

- ✅ **ECS**: Auto-pull images for deployment
- ✅ **EKS**: Kubernetes pod image pulling
- ✅ **Lambda**: Container-based functions
- ✅ **CodeBuild**: Build and push images
- ✅ **CloudFormation**: IaC automation

## Lifecycle Management

- ✅ Retention policies (keep N images)
- ✅ Auto-delete old images
- ✅ Cost optimization rules
- ✅ Per-repository policies

## Use Cases

- **Containerized Applications**: Store application images
- **CI/CD Pipelines**: CodeBuild → ECR → ECS/EKS
- **Security Scanning**: Find vulnerabilities before deployment
- **Multi-Environment**: Different images per environment

## Pricing

- Storage: $0.10/GB/month
- Data push: $0.09/GB
- Data pull: Free

## Best Practices

✅ Scan all images for vulnerabilities
✅ Use image tags for versioning
✅ Implement lifecycle policies
✅ Use private repositories by default
✅ Implement IAM policies for access control

## Next Steps

→ [ECR Documentation](https://docs.aws.amazon.com/ecr/)
→ [Image Scanning Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
→ [ECR Console](https://console.aws.amazon.com/ecr/)