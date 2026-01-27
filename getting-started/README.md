# Getting Started with AWS ☁️

Your first steps into the AWS cloud! This section guides you from zero knowledge to creating your first AWS account and understanding the basics.

---

## 🌟 Start Here (In Order)

### Step 1: Understanding the Basics

#### [What is Cloud Computing?](what-is-cloud-computing.md)
**Understand the cloud before AWS**
- What is cloud computing?
- Benefits of the cloud
- Cloud service models (IaaS, PaaS, SaaS)
- Public vs Private vs Hybrid cloud
- Why businesses move to the cloud

#### [What is AWS?](what-is-aws.md)
**Introduction to Amazon Web Services**
- AWS overview and history
- AWS market position
- Core AWS services overview
- AWS vs other cloud providers
- Who uses AWS?

---

### Step 2: Setting Up Your Account ⚙️

#### [Creating AWS Account](creating-aws-account.md)
**Set up your AWS account (10 minutes)**
- Account creation process
- Email and password setup
- Payment method requirements
- Identity verification
- Initial account configuration

#### [AWS Free Tier](aws-free-tier.md)
**Learn for free (12 months!)**
- What's included in Free Tier?
- 12-month free services
- Always-free services
- Free tier limits and quotas
- How to avoid unexpected charges
- Monitoring Free Tier usage

---

### Step 3: Essential Setup Tasks 🔒

#### [AWS Console Overview](aws-console-overview.md)
**Navigate the AWS Management Console**
- Console layout and navigation
- Service search and favorites
- Region selector
- Account menu and settings
- CloudShell introduction
- Mobile app overview

#### [Cost Management Basics](cost-management-basics.md)
**Understand and control AWS costs**
- AWS billing dashboard
- Cost Explorer introduction
- Understanding your bill
- Cost allocation tags
- Budgets and forecasts
- Common cost pitfalls

#### [Setting Up Billing Alerts](setting-up-billing-alerts.md)
**Get notified before overspending (Set this up immediately!)**
- Creating billing alarms
- Setting budget thresholds
- Email notifications
- SNS alerts
- Best practices for alerts
- Example alert configurations

---

### Step 4: Learning AWS Terminology 📖

#### [Basic Terminology](basic-terminology.md)
**Essential AWS vocabulary**
- Common AWS terms
- Service naming conventions
- Understanding resource identifiers
- ARN (Amazon Resource Name)
- Tags and metadata
- AWS-specific acronyms

---

## 🎯 Quick Start Checklist

### Day 1: Account Setup (1 hour)
- [ ] Read [What is Cloud Computing?](what-is-cloud-computing.md)
- [ ] Read [What is AWS?](what-is-aws.md)
- [ ] Create AWS account → [Guide](creating-aws-account.md)
- [ ] Set up MFA on root account ⚠️ **Critical!**
- [ ] Review [AWS Free Tier](aws-free-tier.md) limits

### Day 2: Security & Cost Controls (1 hour)
- [ ] Set up [billing alerts](setting-up-billing-alerts.md) ⚠️ **Do this today!**
- [ ] Create first IAM user (don't use root!) → [IAM Basics](../core-concepts/iam-basics.md)
- [ ] Enable MFA on IAM user
- [ ] Review [Cost Management Basics](cost-management-basics.md)

### Day 3: Console Familiarization (30 minutes)
- [ ] Explore [AWS Console](aws-console-overview.md)
- [ ] Review [Basic Terminology](basic-terminology.md)
- [ ] Bookmark frequently used services
- [ ] Set your default region

### Day 4-7: Core Concepts
- [ ] Study [Core Concepts](../core-concepts/README.md) (IAM, VPC, Regions)
- [ ] Review [Security Best Practices](../core-concepts/security-best-practices.md)

---

## 🚦 Learning Paths by Goal

### 👶 Complete Beginner ("I know nothing about cloud")
**Start here →**
1. [What is Cloud Computing?](what-is-cloud-computing.md)
2. [What is AWS?](what-is-aws.md)
3. [Creating AWS Account](creating-aws-account.md)
4. [AWS Free Tier](aws-free-tier.md)
5. [AWS Console Overview](aws-console-overview.md)
6. **Next:** [Core Concepts](../core-concepts/README.md)

### 👨‍💻 Developer ("I know coding but not cloud")
**Quick path →**
1. [What is AWS?](what-is-aws.md) (skim)
2. [Creating AWS Account](creating-aws-account.md)
3. [Setting Up Billing Alerts](setting-up-billing-alerts.md) ⚠️
4. [Basic Terminology](basic-terminology.md)
5. **Next:** [Tier 1 Services](../tier-1-foundational/README.md)

### 🏢 Enterprise Evaluation ("Should we use AWS?")
**Business focus →**
1. [What is AWS?](what-is-aws.md)
2. [AWS Free Tier](aws-free-tier.md)
3. [Cost Management Basics](cost-management-basics.md)
4. Review [Pricing Models](../core-concepts/pricing-models.md)
5. **Next:** [Best Practices](../best-practices/README.md)

---

## ⚠️ Critical First Steps (Don't Skip!)

### 🔴 Must Do Immediately:
1. **Enable MFA on root account** - Protects your entire AWS account
2. **Set up billing alerts** - Prevents surprise charges
3. **Create IAM user** - Never use root account for daily work
4. **Review Free Tier limits** - Stay within free usage

### 🟡 Do Within First Week:
5. Understand [IAM Basics](../core-concepts/iam-basics.md)
6. Learn [VPC Fundamentals](../core-concepts/vpc-fundamentals.md)
7. Review [Security Best Practices](../core-concepts/security-best-practices.md)
8. Set up AWS CLI (optional but recommended)

---

## 💰 Staying Within Free Tier

**Free for 12 months:**
- **EC2:** 750 hours/month (t2.micro)
- **S3:** 5GB storage + 20,000 GET requests
- **RDS:** 750 hours/month (db.t2.micro)
- **Lambda:** 1 million requests/month
- **DynamoDB:** 25GB storage

**Always free:**
- **CloudWatch:** 10 custom metrics
- **Lambda:** 1 million requests/month (forever!)
- **DynamoDB:** 25GB storage (forever!)

**Tips to avoid charges:**
- Set billing alarms at $1, $5, $10
- Terminate unused EC2 instances
- Delete unnecessary S3 objects
- Monitor Free Tier usage in billing dashboard

---

## 📚 Recommended Reading Order

1. **This folder** (Getting Started) - Foundation
2. [Core Concepts](../core-concepts/README.md) - Essential knowledge
3. [Tier 1 Services](../tier-1-foundational/README.md) - Start building
4. [Tutorials](../tutorials/README.md) - Hands-on practice
5. [Best Practices](../best-practices/README.md) - Production-ready

---

## 🎓 Next Steps

After completing this section:

✅ **You have:** Active AWS account with security configured  
✅ **You understand:** Cloud basics and AWS terminology  
✅ **You know:** How to navigate the console and manage costs  

**Ready to learn services?** → Start with [Core Concepts](../core-concepts/README.md)

---

**Welcome to AWS! Let's build something amazing.** ☁️🚀
