# Tier 1: Foundational AWS Services 🏗️

Welcome to **Tier 1** - the essential foundation of AWS! These 7 services form the core of almost every AWS application.

## Overview

These services must be understood before moving to any other tier. They appear in ~95% of all AWS deployments.

### Services in This Tier

1. **[EC2](ec2/README.md)** - Virtual servers (compute)
2. **[S3](s3/README.md)** - File storage
3. **[IAM](iam/README.md)** - User & security
4. **[VPC](vpc/README.md)** - Network infrastructure
5. **[Lambda](lambda/README.md)** - Serverless compute
6. **[RDS](rds/README.md)** - Relational databases
7. **[CloudFormation](cloudformation/README.md)** - Infrastructure automation

---

## 📚 Recommended Learning Order

### Week 1-2: Security & Networking First
1. **IAM** - Start here! You need to understand security before building anything
2. **VPC** - Build your network foundation

### Week 3-4: Compute
3. **EC2** - The most important compute service
4. **Lambda** - Modern serverless approach

### Week 5-6: Storage & Databases
5. **S3** - The most used service in AWS
6. **RDS** - Structured data storage

### Week 7: Automation
7. **CloudFormation** - Automate infrastructure creation

---

## 🎯 Quick Decision Guide

**Need to run code?**
- Use **Lambda** if it runs periodically or on-demand
- Use **EC2** if it needs to run continuously

**Need to store files?**
- Use **S3** for any unstructured data

**Need a database?**
- Use **RDS** for structured, relational data

**Need to manage users/permissions?**
- Use **IAM** for all access control

**Need a network?**
- Use **VPC** to isolate your infrastructure

---

## 💡 Real-World Example

A simple web application uses all 7 Tier 1 services:

```
┌─────────────────────────────────────────────────────────┐
│                  Your AWS Application                   │
├─────────────────────────────────────────────────────────┤
│ Users access your website through CloudFront (Tier 2)   │
│                         ↓                               │
│ Traffic routes to EC2 instances (Tier 1)                │
│                         ↓                               │
│ Apps store files in S3 (Tier 1)                        │
│ Apps store data in RDS (Tier 1)                        │
│                         ↓                               │
│ VPC (Tier 1) isolates all resources                    │
│ IAM (Tier 1) controls who can access what              │
│ CloudFormation (Tier 1) automates it all               │
└─────────────────────────────────────────────────────────┘
```

---

## ✅ Your First Steps

1. **Create an AWS Account** - If you haven't already
2. **Set up IAM** - Don't use root account for daily work!
3. **Create a VPC** - Your private network
4. **Launch an EC2 instance** - Your first virtual server
5. **Create an S3 bucket** - Store some files
6. **Try RDS** - Set up a test database
7. **Use CloudFormation** - Automate what you just built

---

## 📖 Documentation Structure

Each service has:
- **What it is** - Simple explanation
- **When to use it** - Real-world scenarios
- **How it works** - Key concepts
- **Pricing** - Cost breakdown with examples
- **Best practices** - Industry standards
- **Getting started** - Hands-on tutorials
- **Troubleshooting** - Fix common issues

---

## 🚀 Next Steps

- **Master all 7 services** here in Tier 1
- **Review best practices** in each service guide
- **Complete tutorials** to build real projects
- Then move to **[Tier 2 - Common Services](../tier-2-common/)**

---

## 📚 Related Resources

- **[Main README](../README.md)** - Overall guide structure
- **[All Services](../ALL_SERVICES.md)** - Complete service list
- **[Getting Started](../getting-started/)** - AWS basics
- **[Core Concepts](../core-concepts/)** - Fundamental knowledge
- **[Tutorials](../tutorials/)** - Hands-on practice

---

**Ready?** Start with **[IAM](iam/README.md)** to understand security first! 🔐
