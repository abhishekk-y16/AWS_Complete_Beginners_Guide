# What is IAM?

**AWS Identity and Access Management (IAM)** is a free service that controls who can access your AWS resources and what they can do with them. Think of it as the security guard and access card system for your entire AWS account.

## 🎯 Core Purpose

IAM answers three critical questions:
1. **Who are you?** (Authentication)
2. **What can you do?** (Authorization)
3. **What resources can you access?** (Permissions)

## 🔑 Key IAM Components

### 1. Users
- **What**: Individual people or applications
- **Example**: john@company.com, jenkins-ci-user
- **Use When**: Each person/system needs unique credentials

### 2. Groups
- **What**: Collections of users with similar access needs
- **Example**: Developers, Admins, Data-Scientists
- **Use When**: Managing permissions for multiple users

### 3. Roles
- **What**: Temporary permissions that can be assumed
- **Example**: EC2 instance accessing S3, Lambda reading DynamoDB
- **Use When**: Services need to access other services

### 4. Policies
- **What**: JSON documents defining permissions
- **Example**: "Allow read access to S3 bucket production-data"
- **Use When**: Specifying exactly what actions are allowed/denied

## 🏢 Real-World Analogy

Imagine IAM as a corporate office building:
- **Users** = Employees with ID badges
- **Groups** = Departments (Engineering, HR, Finance)
- **Roles** = Visitor badges (temporary access)
- **Policies** = Access rules ("Finance can enter accounting floor")

## 📋 Common Use Cases

### 1. **Multi-User Management**
```
Scenario: 5 developers need AWS access
Solution: Create IAM users, add to "Developers" group
Benefit: Don't share root account credentials
```

### 2. **Service-to-Service Access**
```
Scenario: EC2 instance needs to read S3 files
Solution: Create IAM role, attach to EC2
Benefit: No hardcoded credentials in code
```

### 3. **Temporary Access**
```
Scenario: Contractor needs 3-month access
Solution: Create IAM user with expiration
Benefit: Automatically revoke access
```

### 4. **Cross-Account Access**
```
Scenario: Partner needs access to specific resources
Solution: Create cross-account IAM role
Benefit: Secure, auditable access
```

## 🔒 Security Best Practices

### ✅ DO
- Enable MFA (Multi-Factor Authentication) for all users
- Use IAM roles for EC2/Lambda instead of access keys
- Follow principle of least privilege
- Rotate credentials regularly
- Use IAM Access Analyzer to identify overly permissive policies

### ❌ DON'T
- Share root account credentials
- Use root account for daily tasks
- Embed access keys in code
- Give full admin access unless absolutely necessary
- Ignore CloudTrail logs (audit trail)

## 💰 Pricing

**IAM is 100% FREE!**
- No charge for users, groups, roles, or policies
- No limits on number of IAM entities
- Only pay for resources your IAM users access

## 🚀 Getting Started

### Step 1: Enable MFA on Root Account
```bash
1. Sign in as root user
2. Go to IAM → Dashboard → Activate MFA
3. Use authenticator app (Google Authenticator, Authy)
```

### Step 2: Create Your First IAM User
```bash
1. IAM → Users → Add User
2. Enter username (e.g., your name)
3. Enable console access + programmatic access
4. Attach policies (start with PowerUserAccess)
5. Download credentials CSV
```

### Step 3: Create Admin Group
```bash
1. IAM → Groups → Create Group
2. Name: Administrators
3. Attach policy: AdministratorAccess
4. Add your IAM user to this group
```

## 🔗 Related Services

- **AWS Organizations**: Manage multiple AWS accounts
- **AWS STS**: Generate temporary security credentials
- **Amazon Cognito**: User authentication for applications
- **AWS SSO**: Single sign-on for AWS accounts
- **CloudTrail**: Audit IAM activity

## ⚠️ Common Mistakes

### 1. **Using Root Account Daily**
```
Problem: Root has unlimited access
Risk: Accidental deletion, security breach
Fix: Create IAM admin user, lock away root credentials
```

### 2. **Overly Permissive Policies**
```
Problem: Giving "*" (all) permissions
Risk: Security vulnerabilities
Fix: Grant only necessary permissions
```

### 3. **Hardcoded Credentials**
```
Problem: Access keys in application code
Risk: Keys leak to GitHub, get compromised
Fix: Use IAM roles for EC2/Lambda/ECS
```

### 4. **No MFA**
```
Problem: Password-only authentication
Risk: Account takeover if password stolen
Fix: Enable MFA for all users (especially admins)
```

## 📚 Learn More

- [IAM Policies →](policies.md)
- [IAM Roles →](roles.md)
- [Users and Groups →](users-and-groups.md)
- [IAM Best Practices →](best-practices.md)
- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)

---

**Next Step**: Learn about [IAM Policies](policies.md) to understand how permissions work.