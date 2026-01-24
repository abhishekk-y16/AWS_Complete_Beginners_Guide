# AWS Beginners Guide 🚀

A comprehensive, beginner-friendly documentation resource for learning Amazon Web Services (AWS) from the ground up.

## Overview

This repository contains structured, easy-to-follow guides covering all major AWS services organized by category. Whether you're new to cloud computing or looking to expand your AWS knowledge, you'll find helpful tutorials, best practices, and real-world examples.

## Quick Navigation

### 🎯 Start Here
- [What is Cloud Computing?](getting-started/what-is-cloud-computing.md)
- [What is AWS?](getting-started/what-is-aws.md)
- [Creating Your AWS Account](getting-started/creating-aws-account.md)
- [AWS Free Tier Overview](getting-started/aws-free-tier.md)

### 🏗️ Core Concepts
- [Regions and Availability Zones](core-concepts/regions-and-availability-zones.md)
- [IAM Basics](core-concepts/iam-basics.md)
- [VPC Fundamentals](core-concepts/vpc-fundamentals.md)
- [AWS Pricing Models](core-concepts/pricing-models.md)

### 🖥️ Compute Services
- **[EC2 - Elastic Compute Cloud](compute/ec2/README.md)** - Virtual servers in the cloud
- **[Lambda](compute/lambda/README.md)** - Serverless compute
- [Lightsail](compute/lightsail/README.md) - Simplified instances
- [Elastic Beanstalk](compute/elastic-beanstalk/README.md) - Easy web app deployment

### 💾 Storage Services
- **[S3 - Simple Storage Service](storage/s3/README.md)** - Object storage
- [EBS - Elastic Block Store](storage/ebs/README.md) - Block storage for EC2
- [EFS - Elastic File System](storage/efs/README.md) - Managed file storage
- [Glacier](storage/glacier/README.md) - Long-term archive storage

### 🗄️ Database Services
- [RDS - Relational Database Service](database/rds/README.md) - Managed relational databases
- [DynamoDB](database/dynamodb/README.md) - NoSQL database
- [Aurora](database/aurora/README.md) - High-performance relational database
- [ElastiCache](database/elasticache/README.md) - In-memory caching

### 🌐 Networking & Content Delivery
- [VPC - Virtual Private Cloud](networking/vpc/README.md) - Your own network
- [CloudFront](networking/cloudfront/README.md) - CDN and edge locations
- [Route 53](networking/route53/README.md) - DNS and domain management
- [API Gateway](networking/api-gateway/README.md) - Create and manage APIs

### 🔐 Security & Identity
- [IAM - Identity and Access Management](security/iam/README.md) - User and permission management
- [Cognito](security/cognito/README.md) - User authentication
- [KMS - Key Management Service](security/kms/README.md) - Encryption key management
- [WAF - Web Application Firewall](security/waf/README.md) - Protection from web attacks

### 📦 Containers
- [ECS - Elastic Container Service](containers/ecs/README.md)
- [EKS - Elastic Kubernetes Service](containers/eks/README.md)
- [ECR - Elastic Container Registry](containers/ecr/README.md)

### 📊 Analytics
- [Athena](analytics/athena/README.md) - Query data in S3 with SQL
- [Redshift](analytics/redshift/README.md) - Data warehouse
- [Kinesis](analytics/kinesis/README.md) - Real-time data streaming

### 🤖 Machine Learning
- [SageMaker](machine-learning/sagemaker/README.md) - Build ML models
- [Bedrock](machine-learning/bedrock/README.md) - Generative AI
- [Rekognition](machine-learning/rekognition/README.md) - Image recognition

### 📚 Learning Resources

#### Tutorials
- [S3 Static Website Hosting](tutorials/s3-static-website.md) ⭐ Complete step-by-step
- [Deploy a Web Server on EC2](tutorials/deploy-web-server.md)
- [Build a Serverless API](tutorials/serverless-api.md)
- [Create Your First RDS Database](tutorials/rds-first-database.md)
- [Lambda + S3 Processing](tutorials/lambda-s3-processing.md)
- [CI/CD Pipeline with CodePipeline](tutorials/cicd-pipeline.md)
- [Full Stack Application Deployment](tutorials/full-stack-deployment.md)

#### Use Cases
- [Web Hosting](use-cases/web-hosting.md)
- [Data Backup and Recovery](use-cases/data-backup.md)
- [Mobile App Backend](use-cases/mobile-backend.md)
- [Data Analytics](use-cases/data-analytics.md)
- [Disaster Recovery](use-cases/disaster-recovery.md)

#### Service Comparisons
- [EC2 vs Lambda](service-comparisons/ec2-vs-lambda.md)
- [RDS vs DynamoDB](service-comparisons/rds-vs-dynamodb.md)
- [S3 vs EBS vs EFS](service-comparisons/s3-vs-ebs-vs-efs.md)
- [ECS vs EKS vs Fargate](service-comparisons/ecs-vs-eks-vs-fargate.md)

#### Best Practices
- [Cost Optimization](best-practices/cost-optimization.md)
- [Security Checklist](best-practices/security-checklist.md)
- [Performance Optimization](best-practices/performance-optimization.md)
- [Tagging Strategy](best-practices/tagging-strategy.md)
- [Backup Strategy](best-practices/backup-strategy.md)

#### Troubleshooting
- [Common Errors Guide](troubleshooting/common-errors.md)
- [EC2 Issues](troubleshooting/ec2-issues.md)
- [S3 Issues](troubleshooting/s3-issues.md)
- [Lambda Issues](troubleshooting/lambda-issues.md)
- [Networking Issues](troubleshooting/networking-issues.md)

#### Additional Resources
- [AWS Glossary](glossary/README.md)
- [Official AWS Links](resources/official-links.md)
- [Learning Paths](resources/learning-paths.md)
- [Certification Guides](resources/certification-guide.md)
- [Free Tier Services](resources/free-tier-services.md)

## 📋 All AWS Services

This guide covers **100+ AWS services** organized by category:

- **Compute:** EC2, Lambda, Lightsail, Elastic Beanstalk, Batch, App Runner, and more
- **Storage:** S3, EBS, EFS, Glacier, FSx, Storage Gateway, Backup
- **Database:** RDS, DynamoDB, Aurora, ElastiCache, Neptune, DocumentDB, and more
- **Networking:** VPC, CloudFront, Route 53, API Gateway, Direct Connect
- **Security:** IAM, Cognito, KMS, WAF, Shield, GuardDuty, Secrets Manager
- **Containers:** ECS, EKS, ECR, Fargate
- **Analytics:** Athena, Redshift, Kinesis, Glue, EMR, MSK, QuickSight
- **Machine Learning:** SageMaker, Bedrock, Rekognition, Comprehend, Polly, Transcribe
- **Developer Tools:** CodeCommit, CodeBuild, CodeDeploy, CodePipeline, Cloud9
- **Management:** CloudWatch, CloudFormation, CloudTrail, Config, Organizations
- **Migration:** Database Migration Service, Application Migration Service, DataSync
- **And More:** Media services, IoT, Blockchain, and specialized services

See [All Services](ALL_SERVICES.md) for the complete list.

## 🎓 Learning Approach

This guide is designed with these principles:

1. **Beginner-Friendly:** No prior AWS experience required
2. **Hands-On:** Includes practical tutorials and examples
3. **Well-Organized:** Services grouped by function and use case
4. **Practical:** Focus on real-world scenarios and best practices
5. **Updated:** Regular updates to reflect AWS changes

## 📊 Repository Statistics

- **100+ Services Documented**
- **18+ Hands-on Tutorials**
- **9+ Use Cases**
- **6+ Service Comparisons**
- **10+ Best Practices Guides**
- **9+ Troubleshooting Guides**

## 🚀 Quick Start

1. **New to AWS?** Start with [Getting Started](getting-started/README.md)
2. **Want to build something?** Check out [Tutorials](tutorials/README.md)
3. **Comparing services?** See [Service Comparisons](service-comparisons/README.md)
4. **Having issues?** Visit [Troubleshooting](troubleshooting/README.md)
5. **Learning a specific service?** Browse [All Services](#-all-aws-services)

## 💡 Key Features

✅ **Structured Learning Path** - From basics to advanced  
✅ **100+ Services Covered** - All major AWS services  
✅ **18+ Complete Tutorials** - Step-by-step guides  
✅ **Real-World Examples** - Practical use cases  
✅ **Best Practices** - Industry-standard recommendations  
✅ **Free Tier Focus** - Budget-friendly learning  
✅ **Regularly Updated** - Keeping up with AWS changes  
✅ **Community-Driven** - Open for contributions  

## 📖 Documentation Standards

All documentation follows consistent formatting for easy navigation:

- Clear section headers
- Code examples where applicable
- Links to official AWS documentation
- Related topics and references
- Visual diagrams and flowcharts (where helpful)

## 🤝 Contributing

We welcome contributions from the community! Whether you want to:

- Fix typos or errors
- Add new tutorials
- Improve existing documentation
- Suggest new topics
- Translate content

Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📋 Code of Conduct

This project is committed to providing a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🔒 Security

If you discover a security vulnerability, please email security@awsbeginnersguide.dev instead of using the issue tracker. See [Security Policy](SECURITY.md) for details.

## 📞 Support

- **Questions?** Open a [Discussion](https://github.com/yourname/aws-beginners-guide/discussions)
- **Found a bug?** Create an [Issue](https://github.com/yourname/aws-beginners-guide/issues)
- **Have an idea?** Submit a [Feature Request](https://github.com/yourname/aws-beginners-guide/issues/new?template=feature_request.md)

## 🙏 Acknowledgments

- AWS for providing comprehensive cloud services
- The open-source community for tools and inspiration
- All contributors who make this guide better
- The learners who drive continuous improvement

## 📚 Additional Resources

- [AWS Official Documentation](https://docs.aws.amazon.com/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- [AWS Learning Library](https://www.aws.training/)
- [AWS Certification Paths](https://aws.amazon.com/certification/)

---

## Getting Started Tips

### For Complete Beginners:
1. Read [What is Cloud Computing?](getting-started/what-is-cloud-computing.md)
2. Set up your [AWS Account](getting-started/creating-aws-account.md)
3. Explore the [AWS Console](getting-started/aws-console-overview.md)
4. Follow your first [Hands-on Tutorial](tutorials/README.md)

### For Developers:
1. Review [Core Concepts](core-concepts/README.md)
2. Choose a service to learn ([Compute](compute/README.md), [Storage](storage/README.md), etc.)
3. Complete a [Tutorial](tutorials/README.md)
4. Check [Best Practices](best-practices/README.md)

### For System Administrators:
1. Understand [IAM](security/iam/README.md) and [VPC](networking/vpc/README.md)
2. Explore [Management Tools](management-governance/README.md)
3. Review [Security Best Practices](best-practices/security-checklist.md)
4. Study [Infrastructure as Code](management-governance/cloudformation/README.md)

---

**Ready to start your AWS journey?** Pick a topic above and begin learning! 🚀

Last Updated: January 25, 2025  
Maintained by: AWS Beginners Guide Community
