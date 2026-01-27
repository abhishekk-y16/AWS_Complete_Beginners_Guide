# IAM Users and Groups

**IAM Users** and **Groups** are the foundation of team access management in AWS. Users represent individual people or applications, while groups make it easier to manage permissions for multiple users at once.

## 👥 IAM Users

### What is an IAM User?
An IAM user is a permanent identity with long-term credentials (username/password and/or access keys) that represents a person or application needing AWS access.

### When to Create IAM Users
✅ **Individual team members** need AWS console or CLI access  
✅ **Applications** running outside AWS need API access  
✅ **CI/CD systems** (Jenkins, GitLab) need deployment credentials  
❌ **AWS services** accessing other services (use IAM roles instead)  
❌ **Temporary contractors** (use federated access with expiration)

### User Authentication Methods

#### 1. **Console Access** (Web UI)
```
Credentials:
- Username (e.g., john.doe)
- Password (min 8 characters, follows password policy)
- MFA device (optional but strongly recommended)

Use Case: Developers, admins accessing AWS Console
```

#### 2. **Programmatic Access** (CLI/API)
```
Credentials:
- Access Key ID (e.g., AKIAIOSFODNN7EXAMPLE)
- Secret Access Key (e.g., wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY)

Use Case: AWS CLI, SDKs, automation scripts
```

#### 3. **Both**
```
Common for developers who need:
- Console access for visual management
- CLI/SDK access for development and automation
```

## 📦 IAM Groups

### What is an IAM Group?
A group is a collection of IAM users. Instead of attaching policies to each user individually, attach policies to groups and add users to appropriate groups.

### Why Use Groups?
```
Without Groups (BAD):
Attach S3FullAccess to: Alice, Bob, Carol, David, Eve
If policy changes: Update 5 users manually

With Groups (GOOD):
Create "Developers" group with S3FullAccess
Add: Alice, Bob, Carol, David, Eve
If policy changes: Update 1 group
```

### Common Group Patterns

#### 1. **By Job Function**
```
Admins Group:
- Policy: AdministratorAccess
- Members: Senior engineers, ops team

Developers Group:
- Policy: PowerUserAccess (everything except IAM)
- Members: Software engineers

Read-Only Group:
- Policy: ReadOnlyAccess
- Members: New hires, auditors, managers
```

#### 2. **By Project/Team**
```
Project-Alpha-Team:
- Policy: Access to project-alpha-* resources
- Members: Alpha project developers

Project-Beta-Team:
- Policy: Access to project-beta-* resources
- Members: Beta project developers
```

#### 3. **By Environment**
```
Production-Access:
- Policy: Read-only for prod, full access for dev/staging
- Members: Senior engineers only

Development-Access:
- Policy: Full access to dev environment
- Members: All developers
```

## 🔍 Real-World Setup Example

### Scenario: Tech Startup with 10 People

**Team Breakdown:**
- 2 DevOps Engineers (full admin)
- 5 Software Developers (deploy apps, access databases)
- 2 Data Analysts (read-only S3, Athena)
- 1 Manager (billing and cost visibility)

**Groups Setup:**

#### Group 1: Admins
```
Members: 2 DevOps engineers
Policies:
- AdministratorAccess

MFA Required: Yes (via policy condition)
```

#### Group 2: Developers
```
Members: 5 Software developers
Policies:
- AmazonEC2FullAccess
- AmazonS3FullAccess
- AmazonDynamoDBFullAccess
- AWSLambda_FullAccess
- CloudWatchLogsReadOnlyAccess

MFA Required: For production resources
```

#### Group 3: DataAnalysts
```
Members: 2 Data analysts
Policies:
- AmazonS3ReadOnlyAccess
- AmazonAthenaFullAccess
- AWSGlueConsoleFullAccess

MFA Required: No (read-only)
```

#### Group 4: Billing
```
Members: 1 Manager
Policies:
- Billing (custom policy for Cost Explorer, Budgets)

MFA Required: Yes
```

## 🛠️ Creating Users and Groups

### Method 1: AWS Console

**Create Group:**
```bash
1. IAM → User Groups → Create Group
2. Group Name: Developers
3. Attach Policies: Select policies (e.g., PowerUserAccess)
4. Create Group
```

**Create User:**
```bash
1. IAM → Users → Add User
2. User Name: john.doe
3. Access Type:
   [x] Console access (password)
   [x] Programmatic access (access key)
4. Add to Groups: Select "Developers"
5. Tags (optional): Department=Engineering
6. Review and Create
7. Download credentials CSV (IMPORTANT!)
```

### Method 2: AWS CLI

**Create Group:**
```bash
# Create group
aws iam create-group --group-name Developers

# Attach policy
aws iam attach-group-policy \
  --group-name Developers \
  --policy-arn arn:aws:iam::aws:policy/PowerUserAccess
```

**Create User:**
```bash
# Create user
aws iam create-user --user-name john.doe

# Create console password
aws iam create-login-profile \
  --user-name john.doe \
  --password 'TempPassword123!' \
  --password-reset-required

# Create access keys
aws iam create-access-key --user-name john.doe

# Add user to group
aws iam add-user-to-group \
  --group-name Developers \
  --user-name john.doe
```

### Method 3: CloudFormation
```yaml
DevelopersGroup:
  Type: AWS::IAM::Group
  Properties:
    GroupName: Developers
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/PowerUserAccess

JohnDoeUser:
  Type: AWS::IAM::User
  Properties:
    UserName: john.doe
    Groups:
      - !Ref DevelopersGroup
    LoginProfile:
      Password: TempPassword123!
      PasswordResetRequired: true
    Tags:
      - Key: Department
        Value: Engineering
```

## 🔐 Password Policies

### Set Account Password Policy
```bash
Requirements:
- Minimum length: 12 characters
- Require uppercase letters
- Require lowercase letters
- Require numbers
- Require symbols
- Password expiration: 90 days
- Prevent password reuse: Last 5 passwords
- Password reset: Self-service allowed

How to Set:
IAM → Account Settings → Set Password Policy
```

### Example Password Policy (CLI)
```bash
aws iam update-account-password-policy \
  --minimum-password-length 12 \
  --require-symbols \
  --require-numbers \
  --require-uppercase-characters \
  --require-lowercase-characters \
  --max-password-age 90 \
  --password-reuse-prevention 5 \
  --allow-users-to-change-password
```

## 🔑 Access Keys Management

### Best Practices
✅ **Rotate every 90 days** (set reminder)  
✅ **Never commit to Git** (use environment variables)  
✅ **Deactivate unused keys** (don't delete immediately)  
✅ **Use separate keys per environment** (dev, staging, prod)  
❌ **Don't share keys between users**  
❌ **Don't embed in code** (use IAM roles for EC2/Lambda)

### Rotate Access Keys
```bash
# Step 1: Create new key
aws iam create-access-key --user-name john.doe

# Step 2: Update applications with new key
# (Test thoroughly!)

# Step 3: Deactivate old key
aws iam update-access-key \
  --user-name john.doe \
  --access-key-id AKIAIOSFODNN7EXAMPLE \
  --status Inactive

# Step 4: Monitor for errors (1 week)

# Step 5: Delete old key
aws iam delete-access-key \
  --user-name john.doe \
  --access-key-id AKIAIOSFODNN7EXAMPLE
```

## 🎯 Best Practices

### ✅ DO
- **Use groups for permissions**: Never attach policies directly to users
- **Enable MFA for all users**: Especially admins
- **Set password policy**: Strong passwords, rotation
- **Tag users**: Department, project, cost center
- **Review permissions regularly**: Remove unused access
- **Use naming conventions**: firstname.lastname or service-name

### ❌ DON'T
- **Share user credentials**: Each person gets their own user
- **Use root account**: Create IAM admin instead
- **Give more permissions than needed**: Principle of least privilege
- **Forget to remove users**: Offboard promptly
- **Leave access keys in code**: Use environment variables or roles

## 📊 User and Group Limits

```
Per AWS Account:
- IAM Users: 5,000 (soft limit, can be increased)
- IAM Groups: 300
- Groups per User: 10
- Managed Policies per User: 10
- Managed Policies per Group: 10
- Inline Policy Size: 2,048 characters (per user/group/role)
```

## ⚠️ Common Mistakes

### 1. **Attaching Policies Directly to Users**
```
❌ BAD:
Attach S3FullAccess to each user individually

✅ GOOD:
Create "Developers" group with S3FullAccess
Add users to group
```

### 2. **Not Using MFA**
```
❌ BAD:
Password-only authentication

✅ GOOD:
Password + MFA (Google Authenticator, Authy)
```

### 3. **Hardcoding Access Keys**
```python
# BAD
aws_access_key_id = 'AKIAIOSFODNN7EXAMPLE'
aws_secret_access_key = 'wJalrXUtnFEMI/K7MDENG'

# GOOD
import os
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
```

### 4. **Not Removing Old Users**
```
Problem: Ex-employees still have AWS access
Risk: Security breach, unauthorized costs
Fix: Offboarding checklist:
  1. Disable console access
  2. Deactivate access keys
  3. Remove from all groups
  4. (Later) Delete user
```

## 🚀 Getting Started Checklist

### For New AWS Account:

**Week 1: Foundation**
- [ ] Set account password policy
- [ ] Enable MFA on root account
- [ ] Create "Admins" group with AdministratorAccess
- [ ] Create your first IAM admin user
- [ ] Add admin user to Admins group
- [ ] Test login with IAM admin
- [ ] Store root credentials securely (lock away)

**Week 2: Team Setup**
- [ ] Create groups by job function (Developers, Analysts, etc.)
- [ ] Attach appropriate policies to groups
- [ ] Create IAM users for team members
- [ ] Add users to appropriate groups
- [ ] Email credentials (securely) and require password change
- [ ] Help users set up MFA

**Week 3: Security Hardening**
- [ ] Review all user permissions (least privilege)
- [ ] Enable CloudTrail (audit logging)
- [ ] Set up billing alerts
- [ ] Document IAM structure and policies
- [ ] Schedule quarterly access reviews

## 🔗 Related Topics

- [IAM Policies →](policies.md)
- [IAM Roles →](roles.md)
- [IAM Best Practices →](best-practices.md)
- [What is IAM? →](what-is-iam.md)

## 📚 Learn More

- [IAM Users Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)
- [IAM Groups Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

---

**Next Step**: Review [IAM Best Practices](best-practices.md) for security hardening.