# Tier 2: Common AWS Services 🔧

Welcome to **Tier 2** - widely-used services that complement the Tier 1 foundation!

## Overview

These 10 services are used in ~70% of AWS applications. They're essential for building real, production-grade systems. **Complete Tier 1 first** before diving into these.

### Services in This Tier

1. **[DynamoDB](dynamodb/README.md)** - NoSQL database
2. **[EBS](ebs/README.md)** - Persistent storage for EC2
3. **[CloudFront](cloudfront/README.md)** - Content delivery & performance
4. **[Route 53](route53/README.md)** - DNS & domain management
5. **[Elastic Beanstalk](elastic-beanstalk/README.md)** - Easy app deployment
6. **[KMS](kms/README.md)** - Encryption & key management
7. **[Cognito](cognito/README.md)** - User authentication
8. **[CloudWatch](cloudwatch/README.md)** - Monitoring & logging
9. **[Auto Scaling](auto-scaling/README.md)** - Dynamic scaling
10. **[API Gateway](api-gateway/README.md)** - Create APIs

---

## 📚 Recommended Learning Order

### Start with Infrastructure Improvements
1. **EBS** - Add persistent storage to your EC2 instances
2. **Route 53** - Set up proper domain management
3. **CloudFront** - Speed up your application globally

### Then Add Application Features
4. **API Gateway** - Create REST APIs for your app
5. **Cognito** - Add user login to your app
6. **DynamoDB** - Alternative to RDS for specific use cases

### Finally, Add Operations
7. **CloudWatch** - Monitor your systems
8. **Auto Scaling** - Handle traffic spikes automatically
9. **KMS** - Encrypt sensitive data
10. **Elastic Beanstalk** - Simplify deployments

---

## 🎯 Common Combinations

### Web Application Stack
- **EC2** (Tier 1) → Web server
- **EBS** (Tier 2) → Storage for EC2
- **RDS** (Tier 1) → Database
- **Route 53** (Tier 2) → Domain management
- **CloudFront** (Tier 2) → CDN for fast delivery

### User Authentication Stack
- **Lambda** (Tier 1) → Run code
- **API Gateway** (Tier 2) → Create API
- **Cognito** (Tier 2) → User login
- **DynamoDB** (Tier 2) → Store user data
- **KMS** (Tier 2) → Encrypt passwords

### Monitoring & Reliability Stack
- **CloudWatch** (Tier 2) → Monitoring
- **Auto Scaling** (Tier 2) → Handle demand
- **CloudFormation** (Tier 1) → Automate recovery
- **RDS** (Tier 1) → Reliable database

---

## ⚠️ Prerequisites

Before using Tier 2 services, ensure you understand:

✅ **From Tier 1:**
- EC2 basics and security groups
- S3 bucket structure and permissions
- IAM roles and policies
- VPC networking fundamentals
- Lambda function basics
- RDS database concepts
- CloudFormation templates

If you haven't mastered Tier 1, go back and review [Tier 1 Services](../tier-1-foundational/README.md).

---

## 💡 What Each Service Adds

| Service | Adds to Tier 1 | Real-World Need |
|---------|--------|---------|
| **EBS** | EC2 needs persistent storage | Long-running databases on EC2 |
| **Route 53** | Better domain/DNS control | Custom domain names |
| **CloudFront** | Global performance | Websites that load fast globally |
| **API Gateway** | Expose Lambda/services as APIs | Mobile apps, third-party integrations |
| **Cognito** | User management | Apps that need login systems |
| **DynamoDB** | Alternative to RDS | High-speed apps, real-time data |
| **CloudWatch** | System visibility | Know when things go wrong |
| **Auto Scaling** | Handle traffic spikes | Black Friday sales, viral content |
| **KMS** | Data encryption | HIPAA/PCI compliance |
| **Elastic Beanstalk** | Less infrastructure work | Get to coding faster |

---

## 🚀 Typical Learning Timeline

- **Days 1-3:** EBS + Route 53 (infrastructure improvements)
- **Days 4-7:** CloudFront + API Gateway (performance & APIs)
- **Days 8-12:** Cognito + DynamoDB (features)
- **Days 13-14:** CloudWatch + Auto Scaling (operations)
- **Days 15+:** KMS + Elastic Beanstalk (advanced features)

---

## 🔄 Example: Building a Scalable Web App

```
User in Brazil makes a request
        ↓
CloudFront (Tier 2) - Content delivered quickly globally
        ↓
Route 53 (Tier 2) - Routes to nearest server
        ↓
Auto Scaling (Tier 2) - Spins up more EC2 if needed
        ↓
EC2 (Tier 1) - Runs your app
        ↓
API Gateway (Tier 2) - Routes to Lambda for certain paths
        ↓
Lambda (Tier 1) - Processes data
        ↓
DynamoDB (Tier 2) - Stores results quickly
        ↓
KMS (Tier 2) - Encrypts sensitive fields
        ↓
CloudWatch (Tier 2) - Logs every step
        ↓
Result returned in milliseconds!
```

---

## ⭐ Key Best Practices

1. **Use CloudWatch from day 1** - Monitoring is essential
2. **Set up Auto Scaling early** - Handle unexpected traffic
3. **Enable encryption with KMS** - Security first
4. **Use Cognito for any user data** - Don't build auth yourself
5. **Enable CloudFront for static content** - Speed matters

---

## 📖 Documentation Structure

Each service guide includes:
- **What it does** - Purpose and capabilities
- **When to use** - Real-world scenarios
- **How it works** - Architecture and concepts
- **Pricing** - Cost calculations with examples
- **Comparisons** - When to choose this over alternatives
- **Tutorials** - Step-by-step setup guides
- **Best practices** - Production recommendations
- **Troubleshooting** - Common issues and fixes

---

## 🎯 Next Steps

1. **Choose your starting service** from the list above
2. **Read its documentation** thoroughly
3. **Try a hands-on tutorial**
4. **Integrate with your Tier 1 setup**
5. **Review best practices** before production

---

## 📚 Related Resources

- **[Tier 1 Foundational](../tier-1-foundational/)** - Prerequisites
- **[Tier 3 Specializations](../tier-3-specializations/)** - Advanced services
- **[Main README](../README.md)** - Overall guide
- **[Tutorials](../tutorials/)** - Hands-on practice
- **[Best Practices](../best-practices/)** - Industry standards
- **[Service Comparisons](../service-comparisons/)** - Choose the right tool

---

**Ready to level up?** Pick a service above and dive in! 🚀
