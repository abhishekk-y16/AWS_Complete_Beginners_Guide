# IAM - Identity & Access Management

Master identity and access control in AWS - the foundation of AWS security.

## 📚 Learning Path

1. **[What is IAM?](what-is-iam.md)** - Core concepts and overview
2. **[Users & Groups](users-and-groups.md)** - Managing team access
3. **[Roles](roles.md)** - Temporary access for services
4. **[Policies](policies.md)** - Permission definitions
5. **[Best Practices](best-practices.md)** - Security guidelines

## 🎯 Quick Summary

IAM controls **WHO** can access **WHAT** and **WHAT** they can do. It's the foundation of AWS security.

| Aspect | Details |
|--------|---------|
| **Cost** | FREE! |
| **Use Cases** | Team access, service permissions, multi-account |
| **Core Rule** | Never use root account for daily work |
| **Learning Time** | 2-3 hours to master |

## 🔑 Core Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Users** | Individual person or app | john@company.com |
| **Groups** | Collection of users | Developers, Admins |
| **Roles** | Temporary access for services | EC2-S3-Access |
| **Policies** | JSON defining permissions | "s3:GetObject" |
| **MFA** | Second authentication factor | Google Authenticator |

## 💡 Real-World Scenario

```
Your Company AWS Account
├─ Root Account (you)
│  └─ Use ONLY for emergencies
├─ Production (EC2, RDS)
│  └─ Accessed via roles (not users)
├─ Developers (5 people)
│  └─ All in "Developers" group
│     └─ Permissions: EC2, S3, CloudWatch
└─ Finance (2 accountants)
   └─ All in "Finance" group
      └─ Permissions: Cost Explorer, Billing
```

## 🚀 Common Use Cases

### Team Member Access
Create IAM user + add to group = instant access

### EC2 to Database  
Create role + attach to EC2 = automatic credentials

### Third-Party Integration
Create user + limit permissions = Slack can't delete EC2!

## ✅ Best Practices

- ✓ Enable MFA (free!)
- ✓ Use principle of least privilege
- ✓ Create groups for team permission management
- ✓ Use roles for services
- ✓ Never hardcode credentials
- ✓ Quarterly audits

## ❌ Never Forget

- ❌ Never use root account for daily work
- ❌ Never share credentials
- ❌ Never skip MFA
- ❌ Never hardcode passwords in code

---
**Start with**: [What is IAM?](what-is-iam.md)