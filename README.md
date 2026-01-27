# AWS Beginners Guide - Top 30 Services Edition 🚀

A streamlined, beginner-friendly documentation resource covering the 30 most essential AWS services organized into three learning tiers for progressive mastery.

## Overview

This simplified guide focuses on the most important AWS services that cover 80% of real-world use cases. Services are organized into three learning tiers:
- **Tier 1: Foundational** - Core services everyone must learn
- **Tier 2: Very Common** - Widely-used services for most applications
- **Tier 3: Specializations** - Advanced services for specific use cases

## Quick Navigation

### 🎯 Start Here (Setup & Fundamentals)
- [What is Cloud Computing?](getting-started/what-is-cloud-computing.md)
- [What is AWS?](getting-started/what-is-aws.md)
- [Creating Your AWS Account](getting-started/creating-aws-account.md)
- [AWS Free Tier Overview](getting-started/aws-free-tier.md)

### 🏗️ Core Concepts (Must Know Before Services)
- [Regions and Availability Zones](core-concepts/regions-and-availability-zones.md)
- [IAM Basics](core-concepts/iam-basics.md)
- [VPC Fundamentals](core-concepts/vpc-fundamentals.md)
- [AWS Pricing Models](core-concepts/pricing-models.md)

---

## 📚 TIER 1: FOUNDATIONAL SERVICES (Start Here!)

These 7 services form the foundation of AWS. Learn these first before moving to other tiers.

| Service | What It Does | Best For |
|---------|-------------|----------|
| **[EC2](tier-1-foundational/ec2/README.md)** | Virtual servers in the cloud | Running applications, web servers, databases |
| **[S3](tier-1-foundational/s3/README.md)** | Object/file storage in the cloud | Storing files, backups, static websites |
| **[IAM](tier-1-foundational/iam/README.md)** | User & permission management | Security, access control, team management |
| **[VPC](tier-1-foundational/vpc/README.md)** | Your own private network on AWS | Network isolation, security, connectivity |
| **[Lambda](tier-1-foundational/lambda/README.md)** | Serverless code execution | Running code without managing servers |
| **[RDS](tier-1-foundational/rds/README.md)** | Managed relational databases | Storing structured data (SQL databases) |
| **[CloudFormation](tier-1-foundational/cloudformation/README.md)** | Infrastructure as code | Automating & replicating infrastructure |

---

## 🔧 TIER 2: VERY COMMON SERVICES (Learn After Tier 1)

These 10 services are essential for building real applications. Used in ~70% of AWS deployments.

| Service | What It Does | Best For |
|---------|-------------|----------|
| **[DynamoDB](tier-2-common/dynamodb/README.md)** | NoSQL database | Fast, scalable, flexible databases |
| **[EBS](tier-2-common/ebs/README.md)** | Block storage volumes for EC2 | Persistent storage for virtual servers |
| **[CloudFront](tier-2-common/cloudfront/README.md)** | Content delivery network (CDN) | Speeding up content delivery worldwide |
| **[Route 53](tier-2-common/route53/README.md)** | DNS & domain management | Routing traffic, registering domains |
| **[Elastic Beanstalk](tier-2-common/elastic-beanstalk/README.md)** | Easy web app deployment | Quick app deployment without managing infrastructure |
| **[KMS](tier-2-common/kms/README.md)** | Key management for encryption | Securing data with encryption keys |
| **[Cognito](tier-2-common/cognito/README.md)** | User authentication & management | Managing app users, login systems |
| **[CloudWatch](tier-2-common/cloudwatch/README.md)** | Monitoring & logging | Tracking application performance & health |
| **[Auto Scaling](tier-2-common/auto-scaling/README.md)** | Automatic capacity management | Scaling servers up/down based on demand |
| **[API Gateway](tier-2-common/api-gateway/README.md)** | Create & manage APIs | Building REST APIs for applications |

---

## 🎯 TIER 3: SPECIALIZATION SERVICES (Advanced Topics)

These 12 services cover specific use cases. Choose based on your needs.

| Service | What It Does | Best For |
|---------|-------------|----------|
| **[ECS](tier-3-specializations/ecs/README.md)** | Container orchestration | Running Docker containers |
| **[EKS](tier-3-specializations/eks/README.md)** | Kubernetes on AWS | Production-grade container orchestration |
| **[ECR](tier-3-specializations/ecr/README.md)** | Container image registry | Storing & managing Docker images |
| **[ElastiCache](tier-3-specializations/elasticache/README.md)** | In-memory caching | Speeding up database queries |
| **[Aurora](tier-3-specializations/aurora/README.md)** | High-performance database | Enterprise-grade relational database |
| **[Glacier](tier-3-specializations/glacier/README.md)** | Long-term file archival | Archiving rarely-accessed data cheaply |
| **[Systems Manager](tier-3-specializations/systems-manager/README.md)** | Infrastructure operations | Managing & patching servers |
| **[CloudTrail](tier-3-specializations/cloudtrail/README.md)** | Audit logging | Tracking all AWS activity |
| **[Backup](tier-3-specializations/backup/README.md)** | Centralized backup management | Backing up resources across AWS |
| **[Organizations](tier-3-specializations/organizations/README.md)** | Multi-account management | Managing multiple AWS accounts |
| **[Config](tier-3-specializations/config/README.md)** | Configuration tracking | Monitoring infrastructure compliance |
| **[CodePipeline](tier-3-specializations/codepipeline/README.md)** | CI/CD automation | Automating deployment pipelines |

---

## 📚 Learning Resources

### 📖 Tutorials (Hands-On Practice)
- [S3 Static Website Hosting](tutorials/s3-static-website.md) ⭐ Best for Tier 1 beginners
- [Deploy a Web Server on EC2](tutorials/deploy-web-server.md)
- [Build a Serverless API](tutorials/serverless-api.md)
- [Create Your First RDS Database](tutorials/rds-first-database.md)
- [Lambda + S3 Processing](tutorials/lambda-s3-processing.md)

### 🎯 Use Cases (Real-World Scenarios)
- [Web Hosting](use-cases/web-hosting.md) - Host your website on AWS
- [Data Backup and Recovery](use-cases/data-backup.md) - Protect your data
- [Mobile App Backend](use-cases/mobile-backend.md) - APIs for mobile apps
- [Disaster Recovery](use-cases/disaster-recovery.md) - Business continuity

### 🔄 Service Comparisons (Choose the Right Tool)
- [EC2 vs Lambda](service-comparisons/ec2-vs-lambda.md) - When to use each
- [RDS vs DynamoDB](service-comparisons/rds-vs-dynamodb.md) - Database choice
- [S3 vs EBS](service-comparisons/s3-vs-ebs.md) - Storage options
- [ECS vs EKS](service-comparisons/ecs-vs-eks.md) - Container options

### ⭐ Best Practices (Industry Standards)
- [Cost Optimization](best-practices/cost-optimization.md)
- [Security Checklist](best-practices/security-checklist.md)
- [Performance Optimization](best-practices/performance-optimization.md)
- [Tagging Strategy](best-practices/tagging-strategy.md)

### 🔧 Troubleshooting (Fix Common Issues)
- [Common Errors Guide](troubleshooting/common-errors.md)
- [EC2 Issues](troubleshooting/ec2-issues.md)
- [S3 Issues](troubleshooting/s3-issues.md)
- [Lambda Issues](troubleshooting/lambda-issues.md)

### 📚 Additional Resources
- [AWS Glossary](glossary/README.md) - Key terms explained
- [Official AWS Links](resources/official-links.md)
- [Free Tier Services](resources/free-tier-services.md)

---

## 🎓 Recommended Learning Path

### Week 1-2: Tier 1 Foundations
1. Complete [Core Concepts](core-concepts/README.md)
2. Study [IAM](tier-1-foundational/iam/README.md) & [VPC](tier-1-foundational/vpc/README.md)
3. Try [EC2 tutorial](tutorials/deploy-web-server.md)

### Week 3-4: Storage & Databases (Tier 1)
4. Learn [S3](tier-1-foundational/s3/README.md)
5. Try [S3 Website Hosting](tutorials/s3-static-website.md)
6. Learn [RDS](tier-1-foundational/rds/README.md)

### Week 5-6: Serverless & Infrastructure (Tier 1)
7. Learn [Lambda](tier-1-foundational/lambda/README.md)
8. Try [Serverless API tutorial](tutorials/serverless-api.md)
9. Learn [CloudFormation](tier-1-foundational/cloudformation/README.md)

### Week 7+: Tier 2 & Tier 3 (Specializations)
10. Choose services based on your project needs
11. Review [Best Practices](best-practices/README.md)
12. Build real projects!

## 📊 This Guide Covers

**29 Most Important AWS Services** organized into 3 learning tiers:
- **Tier 1:** 7 foundational services (everyone needs these)
- **Tier 2:** 10 common services (used in most projects)
- **Tier 3:** 12 specialized services (choose based on your needs)

## 🎓 Learning Approach

This simplified guide focuses on **quality over quantity** with these principles:

1. **Top 30 Focus:** Only the most important AWS services
2. **Beginner-Friendly:** Clear explanations suitable for newcomers
3. **Tier-Based Learning:** Progress from foundational → common → specialized
4. **Hands-On:** Real tutorials and practical examples
5. **Up-to-Date:** Latest AWS best practices

## 💡 Key Principles

✅ **Simplified:** Only essential services (no overwhelming options)  
✅ **Structured:** Tier-based learning progression  
✅ **Practical:** Tutorials and real-world examples  
✅ **Focused:** Quality over quantity  
✅ **Beginner-Friendly:** Easy-to-understand explanations  
✅ **Best Practices:** Industry-standard recommendations  

## 🚀 Getting Started

### For Complete Beginners:
1. Start with [Getting Started](getting-started/README.md)
2. Learn [Core Concepts](core-concepts/README.md)
3. Follow the [Recommended Learning Path](#recommended-learning-path)
4. Complete Tier 1 tutorials first

### For Experienced Developers:
1. Review [Tier 1 Services](#-tier-1-foundational-services-start-here) quickly
2. Jump to Tier 2 & 3 as needed
3. Check [Best Practices](best-practices/README.md)
4. Use [Service Comparisons](service-comparisons/README.md) to choose tools  

## � What's New (Simplified Edition)

This is a **drastically simplified** version of the AWS Beginners Guide:
- ✂️ **Reduced from 100+ services to 29** - Eliminates overwhelm
- 🎯 **Tier-based learning** - Clear progression path
- 📚 **Focused content** - Quality over quantity
- 🚀 **Faster to learn** - Less time lost on niche services

---

## 📞 Support & Contributing

- **Questions?** Check [FAQs in Tutorials](tutorials/README.md)
- **Found an issue?** Create a GitHub Issue
- **Want to contribute?** See [Contributing Guidelines](CONTRIBUTING.md)

## 📄 License & Security

- **License:** MIT License - see [LICENSE](LICENSE)
- **Security:** See [Security Policy](SECURITY.md)
- **Code of Conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

---

**Happy learning! Start with Tier 1, progress at your own pace, and build amazing things on AWS.** 🚀

### For System Administrators:
1. Understand [IAM](security/iam/README.md) and [VPC](networking/vpc/README.md)
2. Explore [Management Tools](management-governance/README.md)
3. Review [Security Best Practices](best-practices/security-checklist.md)
4. Study [Infrastructure as Code](management-governance/cloudformation/README.md)

---

**Ready to start your AWS journey?** Pick a topic above and begin learning! 🚀

Last Updated: January 25, 2025  
Maintained by: AWS Beginners Guide Community
