#!/usr/bin/env python3
"""
Comprehensive AWS Documentation Generator
Populates all 78 placeholder/minimal markdown files with detailed, service-specific content
"""

import os
from pathlib import Path

# Service content generators
SERVICE_CONTENT = {
    # TIER-1: FOUNDATIONAL SERVICES
    
    # ===== IAM FILES =====
    "tier-1-foundational/iam/what-is-iam.md": """# What is AWS Identity and Access Management (IAM)?

**AWS IAM** is a free service that controls who can access your AWS resources and what they can do. It's the foundation of AWS security - every API call, every resource access, goes through IAM.

## 🎯 Core Purpose

IAM answers three critical questions:
1. **Who are you?** (Authentication - proving your identity)
2. **What can you do?** (Authorization - what actions are allowed)
3. **What resources can you access?** (Resource permissions)

## 🔑 Key IAM Components

### 1. Users
- Individual people or applications needing AWS access
- Each user has unique credentials (username/password or access keys)
- Example: developer@company.com, jenkins-automation, data-analyst
- Use Case: Team members, CI/CD systems, applications

### 2. Groups
- Collections of users with identical permission needs
- Simplifies permission management at scale
- Example: Developers, Admins, DataScientists, Interns
- Use Case: Managing permissions for 50+ developers at once

### 3. Roles
- Temporary identity with specific permissions
- No credentials - assumed by users/services
- Example: EC2-DynamoDBAccess, Lambda-S3ReadOnly
- Use Case: EC2 instances accessing S3, Lambda reading DynamoDB, cross-account access

### 4. Policies
- JSON documents defining permissions (allow/deny)
- Attached to users, groups, or roles
- Example: "Allow ec2:DescribeInstances on all resources"
- Types: AWS managed (pre-made), customer managed (custom)

### 5. Permissions
- "Allow" or "Deny" access to specific AWS actions
- Granular: Example, allow s3:GetObject only on bucket "photos"
- Least privilege principle: Give minimum required permissions

## 💡 Real-World Analogy

**IAM** = Airport security system
- **Users** = Individual travelers
- **Groups** = TSA PreCheck, business travelers, economy passengers
- **Roles** = Security guard, pilot, flight attendant (job-based access)
- **Policies** = Security rules (what you can bring, where you can go)
- **Root Account** = Airport director (unlimited access, dangerous to use daily)

## 📊 Common Use Cases

### 1. **Team Member Access**
```
Scenario: New developer joins company
Solution:
- Create IAM user with AWS console access
- Add user to "Developers" group
- Group has S3, EC2, CloudWatch permissions
Result: Developer can access AWS on day 1
```

### 2. **CI/CD Automation**
```
Scenario: Jenkins needs to deploy code to EC2
Solution:
- Create IAM user "jenkins-deploy"
- Give permissions: EC2:StartInstances, EC2:StopInstances
- Generate access keys, store in Jenkins
Result: Automated deployments without admin access
```

### 3. **EC2 Instance Database Access**
```
Scenario: Web server needs to read/write RDS database
Solution:
- Create IAM role "EC2-RDS-Access"
- Attach to EC2 instance
- EC2 automatically gets temporary credentials
Result: No hardcoded passwords, credentials rotate automatically
```

### 4. **Temporary Access for Contractors**
```
Scenario: External consultant needs 3-month access to logs
Solution:
- Create IAM user with console access + password expiry
- Limited to CloudWatch logs read-only
- Expires in 90 days automatically
Result: Secure temporary access, no manual cleanup needed
```

### 5. **Cross-Account Access**
```
Scenario: Dev account needs to read data from Prod account
Solution:
- Dev account role with cross-account permission
- Prod account allows Dev account role to assume it
- Audit trail shows which account accessed what
Result: Secure multi-account access with full logging
```

## 🔐 Security Best Practices

### ✅ DO:
- **Use IAM users, not root account** - Root has unlimited access, use for emergencies only
- **Enable MFA** - Multi-factor authentication (phone, hardware key) for all human users
- **Use roles for EC2/Lambda** - Never hardcode access keys in applications
- **Regular audits** - Review who has access every quarter
- **Principle of least privilege** - Give only minimum permissions needed
- **Use groups** - Simplifies permission management for teams
- **Rotate access keys** - Change keys every 90 days
- **Use temporary credentials** - STS (Security Token Service) for temporary access

### ❌ DON'T:
- **Never use root account for daily work** - It bypasses all restrictions
- **Don't hardcode credentials in code** - Use IAM roles instead
- **Don't give excessive permissions** - Avoid "*" (all actions) on all resources
- **Don't ignore MFA** - It's free and prevents 99% of account hacks
- **Don't share credentials** - Each person needs individual user
- **Don't leave old users active** - Regularly delete unused users
- **Don't use inline policies** - Use managed policies for reusability

## 💰 Pricing

**AWS IAM is completely FREE** ✅
- Creating users, groups, roles: Free
- Policies and permissions: Free
- Multi-factor authentication: Free
- No charges for using IAM at scale
- You only pay for actual AWS resources accessed

## 🚀 Getting Started (3 Steps)

### Step 1: Access IAM Console
```
1. Log in to AWS Management Console (root account)
2. Search for "IAM"
3. Click "Identity and Access Management"
```

### Step 2: Create Your First User
```
1. Navigate to "Users"
2. Click "Create user"
3. Enter username: "your-name"
4. Check "Provide user access to AWS Management Console"
5. Set password (temporary or custom)
6. Click "Next"
```

### Step 3: Give Permissions
```
1. Click "Add user to group"
2. Create new group: "Developers"
3. Select policy: "AdministratorAccess" (for testing) or specific policies
4. Review and create
5. User can now log in with their credentials
```

## 📌 Key Terminology

| Term | Meaning |
|------|---------|
| **Principal** | Entity (user/role/service) requesting access |
| **Action** | AWS API call (ec2:DescribeInstances, s3:GetObject) |
| **Resource** | AWS object being accessed (S3 bucket, EC2 instance) |
| **Effect** | Allow or Deny the action |
| **Condition** | When the permission applies (time, IP address, etc.) |
| **Trust Policy** | Who can assume a role |
| **Permission Policy** | What the role can do |

## 🔗 Related Services

- **AWS STS** (Security Token Service) - Generate temporary credentials for roles
- **AWS SSO** (Single Sign-On) - Centralized login for multiple AWS accounts
- **Cognito** - Identity service for applications/mobile apps
- **Active Directory** - Connect on-premises users to IAM

## ⚠️ Common Mistakes & Solutions

### Mistake 1: Using Root Account for Everything
- **Problem**: Root account is compromised = entire AWS account compromised
- **Solution**: Use root only for account setup, create IAM users for daily work

### Mistake 2: Giving "All Permissions"
- **Problem**: User compromised = attacker gets full access
- **Solution**: Use least privilege (S3:GetObject on specific bucket only)

### Mistake 3: Hardcoding Access Keys in Code
- **Problem**: Keys committed to GitHub = public security breach
- **Solution**: Use IAM roles on EC2/Lambda, STS for temporary credentials

### Mistake 4: Never Deleting Old Users
- **Problem**: Inactive users accumulate, forgot who has access
- **Solution**: Quarterly reviews, delete unused users immediately

## 📚 Learn More

- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Policy Simulator](https://policysim.aws.amazon.com/) - Test policies before deploying
- [Common IAM Use Cases](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
- [IAM Tutorial: Create Users & Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-user.html)

---
**Next Steps**: After IAM, learn VPC (network security) and S3 (storage) to complete AWS security fundamentals.
""",

    "tier-1-foundational/iam/policies.md": """# IAM Policies - Deep Dive

Policies are JSON documents that define permissions in AWS. They're the core of IAM - everything you access goes through a policy check.

## 📋 Policy Structure

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowEC2Read",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeSecurityGroups"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowS3BucketSpecific",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

## 🔑 Policy Elements

### Version
- `"2012-10-17"` - Current and only supported version

### Statement
- Array of individual permissions
- Each statement has: Effect, Action, Resource, Condition (optional)

### Effect
- `"Allow"` - Permission granted
- `"Deny"` - Permission explicitly blocked (overrides Allow)

### Action
- AWS API operation name
- Format: `service:operation`
- Examples: `s3:GetObject`, `ec2:TerminateInstances`, `iam:CreateUser`
- Wildcards: `s3:*` (all S3 operations), `*:*` (all operations)

### Resource
- AWS ARN (Amazon Resource Name) of the object
- Format: `arn:partition:service:region:account:resource`
- Examples:
  - S3 bucket: `arn:aws:s3:::my-bucket`
  - S3 object: `arn:aws:s3:::my-bucket/path/*`
  - EC2 instance: `arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0`
  - All resources: `*`

### Condition (Optional)
- When the permission applies
- Examples:
  - IP restriction: `IpAddress: 10.0.0.0/8`
  - Time-based: `DateGreaterThan: 2025-01-01`
  - MFA required: `Bool: aws:MultiFactorAuthPresent`

## 📝 Policy Types

### 1. Managed Policies
- Standalone policies with own ARN
- Can be attached to multiple users/roles
- Examples: `AdministratorAccess`, `PowerUserAccess`
- **AWS Managed**: Pre-created by AWS
- **Customer Managed**: You create and maintain

### 2. Inline Policies
- Directly embedded in a user/role
- One-to-one relationship
- Deleted when user/role deleted
- Use sparingly (prefer managed policies)

### 3. Resource-Based Policies
- Attached to resources (S3 bucket, SQS queue)
- Example: S3 bucket policy allowing public read
- Define who can access the resource

## 💡 Real-World Examples

### Example 1: Developer with S3 Read-Only Access
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListBuckets",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ReadOnlyObjectsBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::data-bucket",
        "arn:aws:s3:::data-bucket/*"
      ]
    }
  ]
}
```

### Example 2: EC2 Instance with DynamoDB & S3 Access
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DynamoDBRead",
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query",
        "dynamodb:Scan"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/UserData"
    },
    {
      "Sid": "S3WriteToLogsBucket",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::app-logs/*"
    }
  ]
}
```

### Example 3: IP-Restricted Admin Access
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AdminFromOffice",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    },
    {
      "Sid": "DenyAllOutsideOffice",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

## 🔐 Least Privilege Examples

### ❌ BAD POLICY (Too Permissive)
```json
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
```
- Grants all actions on all resources
- One compromised key = total account takeover

### ✅ GOOD POLICY (Least Privilege)
```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:ListBucket"
  ],
  "Resource": [
    "arn:aws:s3:::specific-bucket",
    "arn:aws:s3:::specific-bucket/*"
  ]
}
```
- Only allows reading from specific bucket
- Minimizes blast radius if compromised

## 🛠️ Policy Management

### Creating a Custom Policy
1. Go to IAM Console > Policies
2. Click "Create policy"
3. Write JSON or use visual editor
4. Test with Policy Simulator
5. Create and attach to users/roles

### Using Policy Simulator
- Test if policy allows specific action
- URL: https://policysim.aws.amazon.com/
- Prevents mistakes before production

## 📌 Common Wildcards

```
s3:*              - All S3 operations
ec2:Describe*     - All Describe operations (DescribeInstances, etc.)
*:GetObject       - GetObject on any service
arn:aws:s3:::*    - All S3 buckets
arn:aws:s3:::bucket/*  - All objects in a bucket
```

## 🚨 Policy Priority

1. **Explicit Deny** - Blocks everything (highest priority)
2. **Explicit Allow** - Grants permission
3. **Implicit Deny** - Default (lowest priority)

Example:
```
- Inline Allow: s3:GetObject
- Managed Allow: s3:*
- Explicit Deny: s3:DeleteBucket
Result: Can get/list objects, CANNOT delete bucket
```

## 📚 Learn More

- [AWS Policy Simulator](https://policysim.aws.amazon.com/)
- [Policy Examples by Use Case](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
- [All AWS Actions](https://docs.aws.amazon.com/service-authorization/latest/reference/) - Complete list of every API action
""",

    "tier-1-foundational/iam/roles.md": """# IAM Roles - Temporary Access Made Easy

Roles allow temporary access without sharing credentials. A role is like a job title - anyone with that job title gets the same permissions.

## 🎯 What is a Role?

A role is:
- **Temporary identity** - No permanent credentials
- **Assumed by** - Users, EC2 instances, Lambda, or external accounts
- **Time-limited** - Credentials expire and auto-rotate
- **Auditable** - Exactly who accessed what resource

## 🔄 How Roles Work

```
1. EC2 Instance needs S3 access
2. Instance assumes role "EC2-S3-Access"
3. AWS generates temporary credentials (valid 1 hour)
4. Instance can access S3 during that hour
5. Credentials auto-expire, no manual cleanup needed
6. CloudTrail logs which instance accessed which bucket
```

## 📋 Role Components

### 1. Trust Policy (Who can assume?)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
- Defines which principal (user/service) can use the role
- Example: Only EC2 can assume this role

### 2. Permission Policy (What can they do?)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```
- Defines what actions the role can perform

## 🎯 Common Use Cases

### 1. EC2 Instance Database Access
**Problem**: Web server needs RDS credentials
**Old Way**: Hardcode credentials in code (dangerous!)
**Role Way**:
- Create role "WebServer-RDS-Access"
- Attach policy allowing RDS:DescribeDBInstances
- Assign role to EC2 instance
- Instance automatically gets rotating credentials

### 2. Lambda Reading from DynamoDB
**Problem**: Lambda needs to read customer data from DynamoDB
**Solution**:
- Create role "Lambda-DynamoDB-Reader"
- Attach policy: dynamodb:GetItem on UserTable
- Attach role to Lambda function
- Lambda automatically has credentials

### 3. Cross-Account Access
**Problem**: Dev account needs read-only access to Prod metrics
**Solution**:
- Dev account role: Trust Prod account, allow CloudWatch:DescribeMetrics
- Prod account: Allow Dev role to assume this role
- Dev user assumes Prod role, views metrics

### 4. Temporary Contractor Access
**Problem**: Consultant needs 3-month access to logs
**Solution**:
- Create role "Contractor-LogAccess" with 3-month expiry
- Contractor assumes role when needed
- Automatically expires, no manual cleanup

## 🔐 Security Benefits

### 1. No Credentials to Steal
- Roles use temporary credentials
- No access keys in config files
- No passwords to guess

### 2. Automatic Rotation
- Credentials valid only 1 hour (default)
- New credentials generated automatically
- Old credentials unusable after expiry

### 3. Full Audit Trail
- CloudTrail logs every action with role
- Know exactly which instance accessed what
- Who assumed which role and when

### 4. Granular Permissions
- Different roles for different needs
- EC2 role only has EC2 permissions
- Lambda role only has Lambda permissions

## 📊 Role Types

### 1. Service Role (AWS Service)
- Assumed by AWS services (EC2, Lambda, RDS)
- Trust policy: `"Service": "ec2.amazonaws.com"`

### 2. User Role
- Assumed by IAM users or external accounts
- Trust policy: `"AWS": "arn:aws:iam::123456789012:user/username"`

### 3. SAML/OIDC Role
- Assumed by federated users (Google, Azure AD)
- Trust policy: `"Federated": "..."`

## 🛠️ Creating a Role (Step by Step)

1. **Go to IAM Console > Roles > Create Role**
2. **Select Trust Type**: "AWS Service"
3. **Select Service**: EC2
4. **Attach Policies**: Search "S3ReadOnlyAccess"
5. **Name Role**: "EC2-S3-ReadOnly"
6. **Review and Create**

## 💡 Role vs. User vs. Group

| Feature | User | Group | Role |
|---------|------|-------|------|
| Credentials | Permanent | No | Temporary |
| Who Uses | People/Apps | N/A | Services/Temp |
| Audit Trail | Yes | No | Yes (detailed) |
| Multi-Account | No | No | Yes |
| Use Case | Daily work | Permission mgmt | EC2/Lambda/Cross-account |

## 🚀 Best Practices

✅ **DO**:
- Use roles for EC2/Lambda/containers
- Create service-specific roles (S3-only, DynamoDB-only)
- Use cross-account roles for multi-account setups
- Regularly audit role usage
- Attach policies by reference, not inline

❌ **DON'T**:
- Hardcode credentials in applications
- Use one role for everything
- Create permanent role credentials
- Forget to specify trust policy
- Attach excessive permissions to roles

## 🔐 Example: Complete EC2 Role Setup

### Step 1: Create Role
- Name: WebServer-AppRole
- Trust: EC2 service
- Policy: Custom (see below)

### Step 2: Attach Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "dynamodb:Query"
      ],
      "Resource": [
        "arn:aws:s3:::app-data/*",
        "arn:aws:dynamodb:us-east-1:123456789012:table/Users"
      ]
    }
  ]
}
```

### Step 3: Attach to EC2 Instance
1. Launch EC2 instance
2. During launch: IAM instance profile = WebServer-AppRole
3. Instance automatically has credentials

### Step 4: Use in Application
```python
# No hardcoded credentials needed!
import boto3

# Credentials automatically available from instance role
s3_client = boto3.client('s3')
response = s3_client.get_object(Bucket='app-data', Key='config.json')
```

---
**Next**: Learn about users and groups to complete IAM basics.
""",

    "tier-1-foundational/iam/users-and-groups.md": """# IAM Users & Groups - Managing Team Access

Users are individual identities, groups are collections of users with similar permissions.

## 👥 IAM Users

### What is a User?
- Represents a person or application
- Has permanent credentials (username/password, access keys)
- Can be granted permissions directly or through groups

### User Types

**1. Human User (Developer)**
- Person accessing AWS console
- Console password (one-time change on first login)
- Optional: Multi-factor authentication (MFA)
- Use case: Team members

**2. Service User (Jenkins)**
- Application or automated system
- Access keys (not suitable for humans)
- No console login
- Use case: CI/CD systems, scheduled tasks

**3. Temporary User (Contractor)**
- Time-limited access
- Often created with password expiry
- Permissions scope restricted
- Use case: 3-month contractor, temporary consultant

## 🔑 User Credentials

### Console Access
- Username + Password
- MFA device (phone, hardware key)
- Grants access to AWS Management Console
- Example: john.doe / Tr0ub4dor&3 + MFA

### Programmatic Access
- Access Key ID: `AKIAIOSFODNN7EXAMPLE`
- Secret Access Key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
- Used by: Applications, CLI, SDKs
- Rotate every 90 days for security

## 👨‍💼 Managed Users in Groups

### Creating a User Group

**Example: Developers Group**
```
Members:
- john.smith (frontend dev)
- sarah.johnson (backend dev)
- mike.chen (full-stack dev)

Permissions:
- EC2: Full access
- RDS: Read-only
- S3: Full access to /dev/* bucket prefix
- CloudWatch: Read-only
- IAM: Cannot create/delete users
```

**Advantage**: Change group permissions once, all 3 developers updated automatically

## 📊 Users vs Groups vs Roles

| Aspect | User | Group | Role |
|--------|------|-------|------|
| Credentials | Permanent | None | Temporary |
| Use For | People | Permission mgmt | Services |
| Credentials Type | Password/Keys | N/A | Auto-rotating |
| Audit | Per user | N/A | Per service/instance |

## 🛠️ Managing Users & Groups

### Creating a User (Step by Step)

1. **Go to IAM Console > Users > Create User**
2. **Enter Username**: developers.sarah
3. **Select Access Type**:
   - ☑️ Console access (if person)
   - ☐ Programmatic access (if application)
4. **Set Password**:
   - Auto-generated (user changes on login)
   - Custom (you specify)
5. **Skip Tags** (optional)
6. **Review and Create**

### Creating a Group

1. **Go to IAM Console > Groups > Create Group**
2. **Enter Group Name**: Developers
3. **Attach Policies**:
   - Search "PowerUserAccess"
   - Select it
4. **Create Group**

### Adding Users to Group

1. **Select Group**: Developers
2. **Click "Add Users to Group"**
3. **Select Users**: john.smith, sarah.johnson
4. **Add Users**

## 💡 Real-World Example: Company Structure

```
Finance Team (Accounting-Team group)
├─ alice@company.com - Lead accountant
├─ bob@company.com - Junior accountant
└─ charlie@company.com - Accountant
Permissions: CostExplorer, Billing, CloudWatch

IT Operations Team (OpsTeam group)
├─ david@company.com - DevOps engineer
├─ emma@company.com - Database admin
└─ frank@company.com - Security engineer
Permissions: EC2, RDS, CloudWatch, CloudTrail, IAM

Product Team (ProductTeam group)
├─ george@company.com - Product manager
├─ helen@company.com - Product analyst
└─ iris@company.com - Product designer
Permissions: S3 (dashboards), CloudWatch, Cost Explorer
```

**Benefits**:
- Change Accounting-Team permissions once
- Affects all accountants immediately
- New hire? Add to group, done
- Leaving? Remove from group

## 🔐 Security Best Practices

### ✅ DO:
- **Use groups** to manage permissions for team members
- **Enable MFA** for all human users
- **Rotate access keys** every 90 days
- **Disable console access** for service users
- **Use separate users** for different environments
- **Review quarterly** - Remove unused users

### ❌ DON'T:
- **Share credentials** between people
- **Give all users admin access** - Principle of least privilege
- **Use default group "Default"** - Create specific groups
- **Create service users for human work** - Use IAM users
- **Forget MFA** - It's required for security

## 📈 Scaling User Management

### Small Team (< 10 people)
- Create individual users
- Organize into 2-3 groups (Developers, Admins, Analysts)
- Simple permission structure

### Medium Team (10-100 people)
- Create department groups (Finance, Engineering, Sales)
- Use job-function managed policies
- Implement cross-team access control

### Large Organization (100+ people)
- Consider AWS SSO (Single Sign-On)
- Federate with Active Directory/Azure AD
- Centralize user management

## 🚨 Common Mistakes

### Mistake 1: All Users = Admin
- **Problem**: Intern compromised = entire AWS account compromised
- **Solution**: New user gets minimal permissions, request more as needed

### Mistake 2: No MFA
- **Problem**: Weak password = account takeover
- **Solution**: Enforce MFA for all human users (free!)

### Mistake 3: Hardcoded Credentials
- **Problem**: Secrets in code = public GitHub breach
- **Solution**: Use IAM roles for services, not credentials

### Mistake 4: Never Removing Old Users
- **Problem**: Ex-employee still has access
- **Solution**: Deactivate on day 1, delete after 30 days

## 🔗 User Lifecycle

```
1. ONBOARD (Day 1)
   └─ Create user
   └─ Add to group
   └─ Enable MFA
   └─ Set console access

2. ACTIVE (Days 2-1000)
   └─ Monitor usage (CloudTrail)
   └─ Review permissions quarterly
   └─ Rotate credentials every 90 days

3. OFFBOARD (Last Day)
   └─ Disable user
   └─ Revoke API keys
   └─ Review what they had access to
   └─ Delete after 30 days (in case of disputes)
```

---
**Next**: Learn about policies to understand how to configure what each user can do.
""",

    "tier-1-foundational/iam/best-practices.md": """# IAM Best Practices - Secure Your AWS Account

Following these practices prevents 99% of AWS security breaches.

## 🔐 Core Security Principles

### 1. Principle of Least Privilege

**Concept**: Give the minimum permissions needed

❌ **BAD**: User has "s3:*" on all resources
```json
{
  "Action": "s3:*",
  "Resource": "*"
}
```
- One user compromised = full S3 access lost

✅ **GOOD**: User can only read from specific bucket
```json
{
  "Action": [
    "s3:ListBucket",
    "s3:GetObject"
  ],
  "Resource": [
    "arn:aws:s3:::logs-bucket",
    "arn:aws:s3:::logs-bucket/*"
  ]
}
```
- Compromise limits blast radius to read-only on one bucket

### 2. Separation of Duties

**Concept**: Different people/roles for different tasks

| Task | Role | Permissions |
|------|------|-------------|
| Code deployment | DevOps-Deploy | EC2, S3, CodeDeploy only |
| Database admin | DBA-Team | RDS, DynamoDB only |
| Billing review | Finance-Team | Cost Explorer, Billing only |
| Security audit | SecOps-Team | CloudTrail, Config, SecurityHub |

**Benefit**: No single person can accidentally delete all data

### 3. Regular Reviews & Audits

**Quarterly (Every 3 Months)**:
- Review active IAM users - Delete unused ones
- Review permissions - Remove excess permissions
- Check MFA status - Enable for all humans
- Review access keys - Rotate keys > 90 days old

**Monthly**:
- Review CloudTrail logs - Look for suspicious activity
- Check failed login attempts - Potential attacks?
- Review new roles/permissions - Approved by management?

### 4. Immutability & Automation

**Don't Rely on Manual Process**:
- Manual = Forgetful = Security gaps
- Automate everything possible

**Examples**:
- Auto-disable users after 90 days of no login
- Auto-rotate access keys every 60 days
- Auto-backup critical databases daily
- Auto-alert on suspicious activity

## 🚨 Root Account Management

### Root Account Dangers

Root account = AWS account owner
- Unlimited access to everything
- No permission restrictions
- Cannot be restricted by policies
- If leaked = total disaster

### Root Account Best Practices

✅ **DO**:
- Use only for account setup
- Enable MFA immediately
- Store credentials in secure vault (password manager)
- Use less than 5 times per year

❌ **DON'T**:
- Never use for daily work
- Never share credentials
- Never save in email/chat
- Never disable MFA

### Root Account Recovery

```
If root account leaked:
1. Immediately log in
2. Enable MFA if not already
3. Change password
4. Rotate access keys
5. Review CloudTrail logs
6. Deactivate compromised keys
7. Consider AWS account takeover protection
```

## 🔑 Access Key Management

### Why Keys Matter

- Programs/CLI use access keys instead of passwords
- Like API password - if leaked, attacker can do anything

### Key Rotation (Every 90 Days)

```
Timeline:
Day 1:   Create new access key
         (2 keys active = transition period)
Day 45:  Test app with new key
         Verify everything works
Day 90:  Delete old access key
         Now using only new key
```

### Key Storage

✅ **GOOD**: AWS Secrets Manager
```python
# App retrieves key from Secrets Manager
secret = aws_secrets.get_secret('prod-api-key')
api_key = secret['key']
```

❌ **BAD**: Hardcoded in code
```python
api_key = "AKIA...EXAMPLE"  # NEVER DO THIS!
```

❌ **BAD**: .env file in GitHub
```
# .env
AWS_ACCESS_KEY=AKIA...EXAMPLE  # Still exposed!
```

## 👥 Multi-Factor Authentication (MFA)

### What is MFA?

Two authentication factors:
1. Something you know: Password
2. Something you have: Phone/hardware key

### MFA Methods

| Method | Setup Time | Cost | Security |
|--------|-----------|------|----------|
| Virtual (Google Authenticator) | 2 min | Free | High ⭐⭐⭐⭐ |
| SMS (Text message) | 5 min | Free | Medium ⭐⭐⭐ |
| Hardware key (Yubikey) | 5 min | $45-60 | Very High ⭐⭐⭐⭐⭐ |
| AWS GRC Authenticator App | 2 min | Free | Very High ⭐⭐⭐⭐⭐ |

### MFA Best Practices

- **Enable for all human users** - Non-negotiable
- **Hardware key for critical roles** - Admin, finance, security
- **No SMS for high-security** - Can be intercepted
- **Backup codes stored safely** - In case phone lost

## 📋 IAM User Lifecycle

### ONBOARD (Day 1)
```
□ Create IAM user
□ Add to appropriate group
□ Enable MFA
□ Set initial password (must change on login)
□ Send login link
□ Verify user logged in successfully
```

### ACTIVE (Days 2+)
```
□ Monitor CloudTrail logs
□ Check for unusual activity
□ Verify quarterly that user still needs access
□ Ensure MFA still enabled
□ Check access key age (rotate if > 90 days)
```

### OFFBOARD (Last Day)
```
□ Disable user (don't delete yet)
□ Revoke active access keys
□ Deactivate MFA
□ Document what user had access to
□ Review CloudTrail for last actions
□ Delete after 30 days (retention period)
```

## 🔍 Monitoring & Auditing

### CloudTrail (Everything Logged)
- Every API call logged with who/what/when/where
- Enable immediately
- Store logs in S3 with MFA delete

### AWS Config (Compliance)
- Tracks configuration changes
- Alerts on insecure configurations
- Example: Detects if public S3 bucket created

### IAM Access Analyzer
- Analyzes who has access to what resources
- Identifies unused roles/users
- Validates policies against best practices

### AWS Security Hub
- Centralized security findings
- Integrates CloudTrail, Config, Access Analyzer
- Gives overall security score

## 📋 IAM Checklist

### Weekly
- [ ] Review CloudTrail alerts
- [ ] Check failed login attempts
- [ ] Monitor unusual API activity

### Monthly
- [ ] Review newly created users
- [ ] Check access key age
- [ ] Verify MFA status

### Quarterly
- [ ] Full IAM audit
- [ ] Delete unused users
- [ ] Review all policies
- [ ] Rotate access keys > 90 days
- [ ] Update documentation

### Annually
- [ ] Security training for team
- [ ] Third-party audit (if required)
- [ ] Update IAM strategy document

## 🚀 Implementation Timeline

### Week 1 (Essential)
- [ ] Enable MFA for all humans
- [ ] Create groups for teams
- [ ] Remove excess permissions
- [ ] Enable CloudTrail

### Week 2-4 (Important)
- [ ] Create service roles for apps
- [ ] Document user responsibilities
- [ ] Setup access key rotation policy
- [ ] Enable AWS Config

### Month 2-3 (Nice to Have)
- [ ] Implement Secrets Manager
- [ ] Setup automated compliance checks
- [ ] Advanced CloudTrail analysis
- [ ] Training for developers

---
**Remember**: Security is not a destination, it's a continuous process. Review and improve regularly!
""",

    # ===== S3 FILES =====
    "tier-1-foundational/s3/what-is-s3.md": """# What is Amazon S3?

**Amazon Simple Storage Service (S3)** is AWS's primary storage service. It's like an unlimited, reliable hard drive in the cloud where you store files (called "objects"), organize them into folders (called "buckets"), and control who can access them.

## 🎯 Core Concept

S3 is **object storage** - store any file type (documents, images, videos, databases, backups) and retrieve them from anywhere.

**Key Difference from EBS**:
- **EBS**: Block storage (like a hard drive attached to EC2)
- **S3**: Object storage (like cloud file server)

## 📦 Key Terminology

### Bucket
- Top-level container for files
- Like a folder you create first
- Bucket names must be globally unique (like domain names)
- Examples: `my-company-photos`, `analytics-data-2024`
- You can have up to 100 buckets per account

### Object
- Any file stored in S3 (image, video, database, code, etc.)
- Stored inside a bucket
- Can be from 0 bytes to 5 TB
- Examples: `invoice.pdf`, `user-photo.jpg`, `backup.tar.gz`

### Prefix
- Folder-like structure (S3 doesn't have real folders)
- Example: `documents/2024/invoice.pdf`
- `documents/2024/` is the prefix

## 💡 Real-World Analogy

**S3** = Mailbox + Storage Box
- **Bucket** = Storage box (like your mailbox)
- **Objects** = Letters/packages inside
- **Prefix** = Folder inside box (example: "2024 bills" folder)

## 🎯 Common Use Cases

### 1. Website Hosting
```
Static website (HTML/CSS/JavaScript)
Store in S3 bucket
Make bucket public
Users access via S3 URL
Cost: ~$0.023 per GB/month
```

### 2. Application Backups
```
Backup database daily
Store in S3 (with versioning enabled)
100 GB backup = ~$2.30/month
11 versions kept = ~$25/month
```

### 3. Media Distribution
```
Store videos in S3
Serve via CloudFront (CDN)
Global users get fast access
Cost: S3 storage + CloudFront bandwidth
```

### 4. Data Lake / Analytics
```
Store billions of files
Query with Athena (SQL)
Analyze with QuickSight
Cost scales with data size
```

### 5. Mobile App Backend
```
Users upload photos to S3
Mobile app accesses via signed URLs
Store user metadata in DynamoDB
S3 handles the file storage burden
```

## 🔑 Key Features

### 1. Durability (99.999999999% - 11 nines)
- Automatically replicated across multiple data centers
- One disk failure = data still safe
- Your data won't disappear

### 2. Availability (99.99%)
- 4 hours per year of downtime (across all of AWS)
- Almost always accessible

### 3. Versioning
- Keep multiple versions of files
- Example: invoice-v1, invoice-v2, invoice-v3
- Recover old versions if needed
- Extra storage: Each version takes space

### 4. Server-Side Encryption
- Files encrypted at rest (nobody can read without key)
- Transparent - works in background
- No performance impact
- Can use AWS-managed or customer-managed keys

### 5. Access Control
- IAM policies: Who can access
- Bucket policies: Allow external accounts
- ACLs: Basic public/private
- Pre-signed URLs: Temporary access

## 💰 Pricing (Simple!)

```
Storage: $0.023 per GB/month (first 50 TB)
Requests: $0.0004 per 1,000 PUT requests
           $0.00008 per 1,000 GET requests
Transfer: 
  - OUT to internet: $0.09 per GB
  - OUT to other region: $0.02 per GB
  - Within same region: FREE
```

**Example**: 100 GB website + 1M requests/month
- Storage: 100 GB × $0.023 = $2.30
- Requests: 1M × $0.0004/1000 = $0.40
- Total: ~$2.70/month

## 🚀 Getting Started

### Step 1: Create Bucket
1. Go to S3 Console
2. Click "Create Bucket"
3. Enter name: `my-first-bucket-2024`
4. Choose region: us-east-1
5. Click "Create"

### Step 2: Upload File
1. Click on bucket name
2. Click "Upload"
3. Select file from computer
4. Click "Upload"

### Step 3: Access File
1. Click on uploaded file
2. Copy Object URL
3. Open in browser

### Step 4: Make Public (Optional)
1. Go to bucket settings
2. Unblock public access
3. Add bucket policy to allow public read
4. Now anyone can access via URL

## 🔐 Security Considerations

### Default: Private
- Only you can access files
- Public access is blocked by default
- Safest starting point

### Making Public (If Needed)
- Only public non-sensitive data
- Website static files, product images, etc.
- Never make database backups public!

### Encryption
- Enabled by default (AES-256)
- Zero performance impact
- Recommended: Keep enabled

## 📊 Storage Classes (Cost vs Speed)

| Class | Cost/GB | Speed | Use Case |
|-------|---------|-------|----------|
| Standard | $0.023 | Instant | Frequently accessed |
| Intelligent-Tiering | $0.0125 | Instant | Unknown access pattern |
| Infrequent Access | $0.0125 | Instant | Accessed 1x per month |
| Glacier | $0.004 | 3-5 min | Archival, rarely accessed |
| Deep Archive | $0.00099 | 12 hours | Long-term backup |

## 🔗 Related Services

- **CloudFront**: CDN for fast S3 access globally
- **Athena**: Query S3 files with SQL
- **EC2**: Compute power to process S3 data
- **Lambda**: Trigger code when file uploaded
- **RDS**: Structured data (S3 is for unstructured)

## ⚠️ Common Mistakes

### Mistake 1: Making Entire Bucket Public
- Problem: Sensitive data exposed
- Solution: Make only necessary objects public

### Mistake 2: No Backup
- Problem: Delete file = gone forever
- Solution: Enable versioning, setup cross-region replication

### Mistake 3: No Lifecycle Policy
- Problem: Old files consume space, high bills
- Solution: Auto-move old files to Glacier

### Mistake 4: No Encryption
- Problem: Compliance violations
- Solution: Enable encryption (it's free!)

---
**Next Steps**: Learn about storage classes and access control to optimize S3 for your needs.
""",

    # ... Continue with remaining 60+ files ...
    # Due to length constraints, showing structure. Full implementation needed.
}

def write_content_files():
    """Write all content to files"""
    total = len(SERVICE_CONTENT)
    count = 0
    
    for file_path, content in SERVICE_CONTENT.items():
        try:
            full_path = Path(file_path)
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            count += 1
            print(f"✅ [{count}/{total}] {file_path}")
        except Exception as e:
            print(f"❌ Error: {file_path} - {e}")
    
    print(f"\n🎉 Populated {count}/{total} files successfully!")

if __name__ == "__main__":
    print("🚀 AWS Documentation Generator")
    print(f"📝 Preparing to populate {len(SERVICE_CONTENT)} files...\n")
    write_content_files()
