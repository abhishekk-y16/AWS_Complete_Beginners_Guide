# Tier 3: Specialization Services 🎯

Welcome to **Tier 3** - advanced services for specialized use cases!

## Overview

These 12 services address specific needs for advanced applications. **Complete Tier 1 & 2 first**, then choose services based on your project requirements.

### Services in This Tier

1. **[ECS](ecs/README.md)** - Docker container orchestration
2. **[EKS](eks/README.md)** - Kubernetes on AWS
3. **[ECR](ecr/README.md)** - Docker image registry
4. **[ElastiCache](elasticache/README.md)** - In-memory caching
5. **[Aurora](aurora/README.md)** - High-performance database
6. **[Glacier](glacier/README.md)** - Archival storage
7. **[Systems Manager](systems-manager/README.md)** - Server operations
8. **[CloudTrail](cloudtrail/README.md)** - Audit logging
9. **[Backup](backup/README.md)** - Centralized backups
10. **[Organizations](organizations/README.md)** - Multi-account management
11. **[Config](config/README.md)** - Compliance monitoring
12. **[CodePipeline](codepipeline/README.md)** - CI/CD automation

---

## 🎯 Choose Based on Your Needs

### Need Advanced Containers? (ECS, EKS, ECR)
- **ECS** - Docker containers without Kubernetes complexity
- **EKS** - Full Kubernetes management
- **ECR** - Private Docker image registry

### Need High Performance? (Aurora, ElastiCache)
- **Aurora** - Better than RDS, MySQL/PostgreSQL compatible
- **ElastiCache** - Speed up databases with caching

### Need Long-Term Storage? (Glacier)
- **Glacier** - Archive data for years at low cost

### Need Operations at Scale? (Systems Manager, CloudTrail)
- **Systems Manager** - Patch servers, run commands
- **CloudTrail** - Audit every AWS action

### Need Backup & Compliance? (Backup, Config, Organizations)
- **Backup** - Centrally backup all your resources
- **Config** - Ensure compliance with policies
- **Organizations** - Manage 10+ AWS accounts

### Need Automated Deployments? (CodePipeline)
- **CodePipeline** - Automate code → production

---

## 📚 When to Use Each Service

### Container Services

**Choose ECS when:**
- Using Docker but not Kubernetes
- Want AWS-managed simplicity
- Team is smaller
- **Tier 2 prerequisite:** API Gateway, CloudWatch

**Choose EKS when:**
- Need Kubernetes for cluster management
- Have Kubernetes expertise
- Running on multiple clouds
- **Tier 2 prerequisite:** All Tier 2 services

**Use ECR with both:**
- Store Docker images privately
- No need for public Docker Hub account
- Integrate with IAM permissions

---

### Database Services

**Choose Aurora when:**
- Current RDS is becoming bottleneck
- Need 3-5x better performance
- Want auto-scaling without effort
- **Prerequisites:** Master RDS (Tier 1)

**Use ElastiCache with any database:**
- Speed up frequently-accessed data
- Reduce database load
- Particularly good with DynamoDB
- **Prerequisites:** CloudWatch (Tier 2), DynamoDB (Tier 2)

---

### Backup & Compliance

**Use Backup when:**
- Need centralized backup management
- Managing 3+ different resource types
- Want point-in-time recovery
- **Prerequisites:** Multiple Tier 1 resources

**Use Config when:**
- Need compliance reporting
- Want infrastructure drift detection
- Regulatory requirements
- **Prerequisites:** IAM, CloudTrail

**Use CloudTrail when:**
- Need security audits
- Compliance requirement (SOC 2, HIPAA, PCI)
- Troubleshooting "who did what"
- **Prerequisites:** S3 (Tier 1), Cloud Formation (Tier 1)

---

### Multi-Account Management

**Use Organizations when:**
- Managing 10+ AWS accounts
- Organizing teams by department
- Centralized billing required
- **Prerequisites:** IAM (Tier 1) mastery

---

### Operations & Automation

**Use Systems Manager when:**
- Patching 50+ EC2 instances
- Running commands across fleet
- Parameter Store for config management
- **Prerequisites:** EC2, IAM (Tier 1)

**Use CodePipeline when:**
- Want automated deployments
- Every code push should test/deploy
- Multiple environments
- **Prerequisites:** Lambda or EC2 (Tier 1)

---

## ⚠️ Prerequisites by Service

### ECS/EKS/ECR
- ✅ EC2 or Lambda
- ✅ API Gateway
- ✅ CloudWatch
- ✅ VPC networking

### Aurora/ElastiCache
- ✅ RDS (Tier 1)
- ✅ DynamoDB (Tier 2)
- ✅ CloudWatch (Tier 2)

### Glacier
- ✅ S3 (Tier 1)
- ✅ CloudFormation (Tier 1)

### Backup/CloudTrail/Config
- ✅ Multiple resources to backup
- ✅ S3 (Tier 1)
- ✅ CloudFormation (Tier 1)
- ✅ CloudWatch (Tier 2)

### Organizations
- ✅ Multiple AWS accounts
- ✅ Deep IAM understanding

### Systems Manager
- ✅ EC2 fleet
- ✅ IAM roles configured

### CodePipeline
- ✅ Lambda or EC2
- ✅ Code repository (GitHub, etc.)
- ✅ CloudFormation or similar deployment

---

## 🚀 Typical Implementation Timeline

### Week 1-2: Performance & Compliance
- Evaluate if **Aurora** needed
- Set up **CloudTrail** for audits
- Consider **Backup** strategy

### Week 3-4: Operations
- Implement **Systems Manager** for patching
- Add **Config** for compliance

### Week 5-6: Container Strategy (If Applicable)
- Choose between **ECS** vs **EKS**
- Set up **ECR** for images
- Configure monitoring

### Week 7+: Scaling & Enterprise
- Implement **ElastiCache** if needed
- Migrate cold data to **Glacier**
- Set up **Organizations** if needed
- Automate with **CodePipeline**

---

## 💡 Real-World Scenario

**Startup growing to enterprise scale:**

```
Year 1: Use only Tier 1 + basic Tier 2
        ↓
Year 2: Add Aurora (faster DB), Backup (data safety)
        ↓
Year 3: Add ECS (containerize), CloudTrail (compliance)
        ↓
Year 4: Add Organizations, Config (multi-account)
        ↓
Year 5: Add ElastiCache, Systems Manager (scale ops)
```

---

## 📖 Documentation Structure

Each service guide includes:
- **What problem does it solve?** - Use cases
- **When not to use** - Anti-patterns
- **How it works** - Architecture
- **Pricing model** - Cost examples
- **Comparison** - vs alternatives
- **Setup guide** - Step-by-step
- **Best practices** - Production ready
- **Troubleshooting** - Common issues

---

## 🎯 Getting Started

1. **Identify your specific need** from list above
2. **Check prerequisites** - Have you mastered them?
3. **Read the service guide** thoroughly
4. **Try the tutorials** hands-on
5. **Review best practices** before production

---

## 📚 Related Resources

- **[Tier 1 Foundational](../tier-1-foundational/)** - Essential services
- **[Tier 2 Common](../tier-2-common/)** - Widely-used services
- **[Main README](../README.md)** - Overall guide
- **[All Services](../ALL_SERVICES.md)** - Service list
- **[Tutorials](../tutorials/)** - Hands-on practice
- **[Best Practices](../best-practices/)** - Production standards
- **[Service Comparisons](../service-comparisons/)** - Choose tools

---

## 🏆 Pro Tips

1. **Don't use all Tier 3 services** - Choose what you need
2. **Master Tier 1 & 2 first** - They're simpler but essential
3. **Read the "When NOT to use" sections** - Avoid over-engineering
4. **Start with simplest option** - Upgrade if needed
5. **Cost check before implementing** - Some services are expensive!

---

**Ready to specialize?** Pick a service that solves your specific problem! 🎯
