# AWS Beginners Guide - Quick Reference Card 🎯

## Where to Start?

### 👶 Complete Beginners
1. **Read:** [Main README](README.md) - Overview
2. **Learn:** [Getting Started](getting-started/README.md) - AWS basics
3. **Study:** [Core Concepts](core-concepts/README.md) - Fundamentals
4. **Follow:** [Tier 1 Learning Guide](tier-1-foundational/README.md) - Start here!

### 👨‍💻 Developers (Some AWS experience)
1. **Skim:** [README.md](README.md) - What's new
2. **Review:** [Tier 1](tier-1-foundational/README.md) quickly
3. **Focus:** [Tier 2](tier-2-common/README.md) - Common services
4. **Select:** [Tier 3](tier-3-specializations/README.md) as needed

### 🏢 Enterprises (Planning AWS)
1. **Review:** [ALL_SERVICES.md](ALL_SERVICES.md) - Full catalog
2. **Study:** [Best Practices](best-practices/) - Standards
3. **Check:** [Service Comparisons](service-comparisons/) - Choose tools
4. **Reference:** [Tier guides](tier-1-foundational/README.md) for team training

---

## 29 Services at a Glance

### 🟢 TIER 1: MUST LEARN FIRST (7 services)
| Service | Purpose | Prerequisite |
|---------|---------|--------------|
| **[IAM](tier-1-foundational/iam/)** | Security & access | None (learn first!) |
| **[VPC](tier-1-foundational/vpc/)** | Network infrastructure | IAM understanding |
| **[EC2](tier-1-foundational/ec2/)** | Virtual servers | IAM + VPC |
| **[S3](tier-1-foundational/s3/)** | File storage | IAM |
| **[RDS](tier-1-foundational/rds/)** | Databases | VPC + IAM |
| **[Lambda](tier-1-foundational/lambda/)** | Serverless code | IAM + VPC |
| **[CloudFormation](tier-1-foundational/cloudformation/)** | Infrastructure automation | All above |

### 🟡 TIER 2: VERY COMMON (10 services)
Used in ~70% of real applications. Learn after Tier 1.

| Service | When to Use | Pair With |
|---------|------------|-----------|
| **[DynamoDB](tier-2-common/dynamodb/)** | High-speed NoSQL DB | API Gateway |
| **[EBS](tier-2-common/ebs/)** | EC2 persistent storage | EC2 |
| **[CloudFront](tier-2-common/cloudfront/)** | Global content delivery | S3 or EC2 |
| **[Route 53](tier-2-common/route53/)** | Domain & DNS | CloudFront/EC2 |
| **[Elastic Beanstalk](tier-2-common/elastic-beanstalk/)** | Easy web app deployment | RDS/DynamoDB |
| **[KMS](tier-2-common/kms/)** | Encryption keys | Any service with data |
| **[Cognito](tier-2-common/cognito/)** | User authentication | Lambda/API Gateway |
| **[CloudWatch](tier-2-common/cloudwatch/)** | Monitoring & logging | All services |
| **[Auto Scaling](tier-2-common/auto-scaling/)** | Auto-scale servers | EC2/Beanstalk |
| **[API Gateway](tier-2-common/api-gateway/)** | Create & manage APIs | Lambda/EC2 |

### 🔵 TIER 3: SPECIALIZED (12 services)
Advanced services for specific use cases. Pick based on your needs.

| Category | Services |
|----------|----------|
| **Containers** | [ECS](tier-3-specializations/ecs/), [EKS](tier-3-specializations/eks/), [ECR](tier-3-specializations/ecr/) |
| **Advanced Databases** | [Aurora](tier-3-specializations/aurora/), [ElastiCache](tier-3-specializations/elasticache/) |
| **Storage** | [Glacier](tier-3-specializations/glacier/) |
| **Operations** | [Systems Manager](tier-3-specializations/systems-manager/), [CloudTrail](tier-3-specializations/cloudtrail/) |
| **Backup & Compliance** | [Backup](tier-3-specializations/backup/), [Config](tier-3-specializations/config/) |
| **Enterprise** | [Organizations](tier-3-specializations/organizations/) |
| **CI/CD** | [CodePipeline](tier-3-specializations/codepipeline/) |

---

## 🛣️ Recommended Learning Paths

### Path 1: Web Application Developer
**Learn in this order:**
1. EC2 → S3 → RDS (Tier 1 foundation)
2. CloudFront → Route 53 → API Gateway (Tier 2 connectivity)
3. CloudWatch → Auto Scaling → Elastic Beanstalk (Tier 2 operations)
4. CodePipeline (Tier 3 deployment)

**Result:** Deploy scalable web apps on AWS

### Path 2: Serverless Developer
**Learn in this order:**
1. Lambda → API Gateway (Tier 1-2)
2. DynamoDB (Tier 2 data)
3. Cognito (Tier 2 auth)
4. CloudWatch (Tier 2 monitoring)
5. CodePipeline (Tier 3 CI/CD)

**Result:** Build serverless APIs and apps

### Path 3: DevOps Engineer
**Learn in this order:**
1. EC2 → VPC → IAM (Tier 1 foundation)
2. CloudFormation (Tier 1 IaC)
3. CloudWatch → Auto Scaling (Tier 2 scaling)
4. Systems Manager → CloudTrail → Backup (Tier 3 operations)

**Result:** Manage and automate infrastructure

### Path 4: Enterprise Architect
**Learn in this order:**
1. All Tier 1 services (foundation)
2. All Tier 2 services (application layer)
3. Organizations → Config → CloudTrail (governance)
4. All Tier 3 as needed for specialization

**Result:** Design enterprise AWS solutions

---

## 📚 Quick Links by Topic

### Storage Solutions
- **Files:** [S3](tier-1-foundational/s3/) (hot) vs [Glacier](tier-3-specializations/glacier/) (cold)
- **Persistent:** [EBS](tier-2-common/ebs/) for EC2
- **Comparison:** [S3 vs EBS](service-comparisons/s3-vs-ebs.md)

### Compute Options
- **Servers:** [EC2](tier-1-foundational/ec2/)
- **Serverless:** [Lambda](tier-1-foundational/lambda/)
- **Managed:** [Elastic Beanstalk](tier-2-common/elastic-beanstalk/)
- **Containers:** [ECS/EKS](tier-3-specializations/) (Tier 3)
- **Comparison:** [EC2 vs Lambda](service-comparisons/ec2-vs-lambda.md)

### Database Options
- **Relational:** [RDS](tier-1-foundational/rds/) (managed) or [EC2](tier-1-foundational/ec2/) (DIY)
- **NoSQL:** [DynamoDB](tier-2-common/dynamodb/)
- **High-Performance:** [Aurora](tier-3-specializations/aurora/) (Tier 3)
- **Comparison:** [RDS vs DynamoDB](service-comparisons/rds-vs-dynamodb.md)

### Networking
- **VPC:** [VPC](tier-1-foundational/vpc/) - Your network
- **DNS:** [Route 53](tier-2-common/route53/) - Domain management
- **CDN:** [CloudFront](tier-2-common/cloudfront/) - Global delivery
- **APIs:** [API Gateway](tier-2-common/api-gateway/) - Create APIs

### Security
- **Access Control:** [IAM](tier-1-foundational/iam/) - Users & permissions
- **Encryption:** [KMS](tier-2-common/kms/) - Encryption keys
- **Users/Auth:** [Cognito](tier-2-common/cognito/) - User authentication
- **Auditing:** [CloudTrail](tier-3-specializations/cloudtrail/) - Audit logs

### Operations
- **Monitoring:** [CloudWatch](tier-2-common/cloudwatch/)
- **Scaling:** [Auto Scaling](tier-2-common/auto-scaling/)
- **Backup:** [Backup](tier-3-specializations/backup/)
- **Server Ops:** [Systems Manager](tier-3-specializations/systems-manager/)

---

## 💰 Free Tier Coverage

**Services included in AWS Free Tier (12 months free):**
- EC2: t2.micro instance
- S3: 5GB storage
- RDS: db.t2.micro instance
- DynamoDB: 25GB storage
- Lambda: 1 million requests/month
- CloudFront: 1TB data transfer
- API Gateway: 1 million requests
- And more...

**Perfect for learning without cost!**

---

## ⏱️ Estimated Learning Timeline

**Week 1-2:** Tier 1 Foundation  
- IAM, VPC, EC2 basics

**Week 3-4:** Tier 1 Storage & Data  
- S3, RDS, introduce Lambda

**Week 5-6:** Tier 1 Automation  
- CloudFormation, deeper Lambda

**Week 7-10:** Tier 2 Services  
- Pick 3-4 services most relevant to you
- DynamoDB, CloudFront, Route 53, API Gateway

**Week 11-12:** Operations  
- CloudWatch, Auto Scaling, basic monitoring

**Week 13+:** Tier 3 & Specialization  
- Choose services for your specific use case

---

## 🎯 Decision Tree: "What Service Should I Use?"

**I need to run code:**
- Continuously? → EC2
- On-demand? → Lambda
- Easy deployment? → Elastic Beanstalk

**I need to store data:**
- Files? → S3 (hot) or Glacier (cold)
- Databases? → RDS (relational) or DynamoDB (NoSQL)
- Volume for EC2? → EBS

**I need authentication:**
- App users? → Cognito
- API access? → IAM

**I need to scale:**
- EC2 servers? → Auto Scaling
- Database? → Read replicas or Aurora

**I need monitoring:**
- Everything → CloudWatch

---

## 📖 Finding Information

**By Service:** [Browse Tiers](tier-1-foundational/README.md)  
**All Services:** [ALL_SERVICES.md](ALL_SERVICES.md)  
**Getting Started:** [getting-started/](getting-started/)  
**Fundamentals:** [core-concepts/](core-concepts/)  
**Best Practices:** [best-practices/](best-practices/)  
**Tutorials:** [tutorials/](tutorials/)  
**Comparisons:** [service-comparisons/](service-comparisons/)  
**Troubleshooting:** [troubleshooting/](troubleshooting/)  

---

## 🚀 Ready to Start?

1. **New to AWS?** → Start with [Getting Started](getting-started/README.md)
2. **Know basics?** → Go to [Tier 1](tier-1-foundational/README.md)
3. **Some experience?** → Skip to [Tier 2](tier-2-common/README.md)
4. **Building something specific?** → Check [Tier 3](tier-3-specializations/README.md)

**Happy learning! The journey from cloud beginner to AWS expert starts here.** ☁️🚀

---

*For the full restructuring details, see [RESTRUCTURING_SUMMARY.md](RESTRUCTURING_SUMMARY.md)*
