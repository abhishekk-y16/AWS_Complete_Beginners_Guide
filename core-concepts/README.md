# AWS Core Concepts 🎓

Fundamental AWS concepts every beginner must understand before diving into services. Master these concepts to build a solid foundation for your AWS journey.

---

## 🔐 Security Fundamentals

### [IAM Basics](iam-basics.md)
**Identity and Access Management - Control who can do what**
- Users, Groups, and Roles
- Policies and permissions
- Multi-Factor Authentication (MFA)
- Best practices for access control
- Root account protection

**Start here first!** IAM is the foundation of AWS security.

### [Security Best Practices](security-best-practices.md)
**Build secure AWS infrastructure from day one**
- Principle of least privilege
- Encryption strategies
- Network security
- Monitoring and logging
- Compliance considerations
- Security automation

---

## 🌍 Infrastructure Concepts

### [Regions and Availability Zones](regions-and-availability-zones.md)
**Understand AWS global infrastructure**
- What are AWS Regions?
- What are Availability Zones (AZs)?
- How to choose the right region
- Multi-AZ for high availability
- Edge locations and CloudFront
- Latency and compliance considerations

### [VPC Fundamentals](vpc-fundamentals.md)
**Your private network on AWS**
- Virtual Private Cloud (VPC) overview
- Subnets (public vs private)
- Internet Gateways and NAT Gateways
- Security Groups vs NACLs
- Route tables
- VPC peering and connectivity

---

## 💰 Cost & Limits

### [Pricing Models](pricing-models.md)
**Understand how AWS charges work**
- Pay-as-you-go pricing
- Reserved Instances (1-year, 3-year)
- Savings Plans
- Spot Instances
- Free Tier explained
- Cost optimization strategies

### [Service Limits & Quotas](service-limits-quotas.md)
**Know your boundaries and how to expand them**
- Default service limits
- Soft limits vs hard limits
- How to request limit increases
- Common limits by service
- Planning for scale
- Monitoring quota usage

---

## 📚 Recommended Learning Order

### Week 1: Security First 🔒
1. [IAM Basics](iam-basics.md) - **Must read first!**
2. [Security Best Practices](security-best-practices.md)

**Why?** Secure your AWS account before creating any resources.

### Week 2: Infrastructure 🌍
3. [Regions and Availability Zones](regions-and-availability-zones.md)
4. [VPC Fundamentals](vpc-fundamentals.md)

**Why?** Understand where and how your resources are deployed.

### Week 3: Cost Management 💰
5. [Pricing Models](pricing-models.md)
6. [Service Limits & Quotas](service-limits-quotas.md)

**Why?** Avoid surprises and plan for growth.

---

## 🎯 Quick Reference

### Essential IAM Concepts
- **Users:** Individual people with AWS access
- **Groups:** Collections of users with shared permissions
- **Roles:** Temporary credentials for services or users
- **Policies:** JSON documents defining permissions

### Essential Networking Concepts
- **Region:** Geographic location (e.g., us-east-1)
- **AZ:** Isolated data center within a region
- **VPC:** Your private network in AWS
- **Subnet:** Subdivision of VPC IP range
- **Security Group:** Virtual firewall for instances

### Essential Cost Concepts
- **On-Demand:** Pay per hour/second (most expensive)
- **Reserved:** 1-3 year commitment (up to 72% savings)
- **Spot:** Unused capacity (up to 90% savings, can be interrupted)
- **Free Tier:** Limited free usage for 12 months

---

## 💡 Key Principles

✅ **Security first** - Always start with IAM and MFA  
✅ **Think global** - Understand regions and AZs for reliability  
✅ **Design for failure** - Use multiple AZs  
✅ **Monitor costs** - Set billing alarms early  
✅ **Start small** - Use Free Tier to learn  

---

## 🚀 Next Steps

After mastering these core concepts:

1. **Tier 1 Services:** Start with [EC2](../tier-1-foundational/ec2/), [S3](../tier-1-foundational/s3/), and [Lambda](../tier-1-foundational/lambda/)
2. **Hands-On Practice:** Try [tutorials](../tutorials/) to apply concepts
3. **Best Practices:** Review [security checklist](../best-practices/security-checklist.md)

---

**Master these concepts before building anything on AWS!** 🎓
