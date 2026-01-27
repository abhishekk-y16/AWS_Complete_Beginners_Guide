# IAM Best Practices

Implementing IAM correctly is the foundation of AWS security. Follow these proven best practices to protect your AWS account and resources from unauthorized access and potential breaches.

## 🔒 Top 10 IAM Security Rules

### 1. ⚠️ Never Use Root Account for Daily Tasks

**Why**: Root account has unlimited access to everything, including billing.

❌ **DON'T:**
```
- Use root for launching EC2 instances
- Share root credentials with team
- Use root access keys for applications
```

✅ **DO:**
```
1. Create IAM admin user on day 1
2. Enable MFA on root
3. Store root credentials in safe (physical or password manager)
4. Only use root for:
   - Account recovery
   - Changing billing/account settings
   - Closing account
```

### 2. 🔑 Enable MFA (Multi-Factor Authentication) for All Users

**Especially Important**: Root account, admin users, any user with production access

**MFA Options**:
- **Virtual MFA** (Recommended): Google Authenticator, Authy, Microsoft Authenticator
- **Hardware MFA**: YubiKey, Gemalto token
- **SMS** (Least secure, not recommended)

**How to Enable**:
```bash
1. IAM → Users → Select user
2. Security Credentials tab
3. Assigned MFA Device → Manage
4. Choose Virtual/Hardware device
5. Scan QR code with authenticator app
6. Enter two consecutive codes
```

**Enforce MFA via Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}
```

### 3. 🎯 Grant Least Privilege

**Principle**: Give only the permissions needed to do the job, nothing more.

❌ **BAD Example**:
```json
// Giving developer full admin access
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
```

✅ **GOOD Example**:
```json
// Giving developer only what they need
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "lambda:UpdateFunctionCode",
    "logs:CreateLogGroup",
    "logs:PutLogEvents"
  ],
  "Resource": [
    "arn:aws:s3:::my-app-bucket/*",
    "arn:aws:lambda:us-east-1:123456789012:function:my-app-*"
  ]
}
```

**Start Restrictive, Then Expand**:
```
1. Start with read-only access
2. User reports what they need
3. Add specific permissions
4. Repeat as needed
```

### 4. 📦 Use Groups to Assign Permissions

❌ **DON'T**: Attach policies directly to individual users
✅ **DO**: Create groups, attach policies to groups, add users to groups

**Why**: Easier to manage, audit, and scale

**Example Structure**:
```
Groups:
  ├─ Admins (AdministratorAccess)
  ├─ Developers (PowerUserAccess)
  ├─ Data-Analysts (S3 + Athena read)
  └─ Billing-Team (Billing read-only)

Users:
  Alice → Admins
  Bob → Developers
  Carol → Developers, Billing-Team
  David → Data-Analysts
```

### 5. 🔄 Rotate Credentials Regularly

**Access Keys**:
```
- Rotate every 90 days (set calendar reminder)
- Use IAM credential report to find old keys
- Automate rotation where possible
```

**Check Last Used**:
```bash
aws iam get-access-key-last-used \
  --access-key-id AKIAIOSFODNN7EXAMPLE
```

**Passwords**:
```
- Set password policy with 90-day expiration
- Require password change on first login
- Prevent password reuse (last 5 passwords)
```

### 6. 🚀 Use IAM Roles for Applications

❌ **NEVER**: Hardcode access keys in application code

```python
# TERRIBLE - Keys exposed in code!
aws_access_key_id = 'AKIAIOSFODNN7EXAMPLE'
aws_secret_access_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
```

✅ **DO**: Use IAM roles for AWS services

```python
# GOOD - No credentials in code!
import boto3

# For EC2/Lambda/ECS: Role credentials automatically provided
s3 = boto3.client('s3')
s3.list_buckets()
```

**Best Practices**:
- **EC2**: Attach IAM role via instance profile
- **Lambda**: Assign execution role
- **ECS/Fargate**: Use task roles
- **Outside AWS**: Use IAM roles with assume-role

### 7. 📋 Enable CloudTrail for Auditing

**What**: CloudTrail logs every API call made in your account

**Why**: 
- Investigate security incidents
- Audit who did what and when
- Compliance requirements
- Detect unusual activity

**Setup**:
```bash
1. CloudTrail → Create Trail
2. Trail Name: company-audit-trail
3. Apply to all regions: Yes
4. Storage: S3 bucket (company-cloudtrail-logs)
5. Enable log file validation
6. Enable CloudWatch Logs integration
```

**What to Monitor**:
```
- Failed login attempts
- Root account usage
- IAM policy changes
- Security group modifications
- S3 bucket policy changes
```

### 8. 🔍 Remove Unnecessary Credentials

**Regular Cleanup**:
```bash
# Run quarterly
1. Generate IAM credential report
2. Find users with:
   - No activity in 90+ days
   - Unused access keys
   - No MFA enabled
3. Disable inactive users
4. Delete after 180 days of inactivity
```

**IAM Credential Report**:
```bash
# Generate report
aws iam generate-credential-report

# Download report (CSV format)
aws iam get-credential-report --output text --query Content \
  | base64 -d > iam-credential-report.csv
```

**What to Look For**:
```
- password_last_used: >90 days
- access_key_1_active: true, access_key_1_last_used: >90 days
- mfa_active: false (for admins)
```

### 9. 🛡️ Use Permission Boundaries

**What**: Maximum permissions a user/role can have (even if policy allows more)

**Use Case**: Allow developers to create roles, but limit what those roles can do

**Example**:
```json
// Permission boundary: No IAM or billing access
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "ec2:*",
        "lambda:*",
        "dynamodb:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "iam:*",
        "aws-portal:*"
      ],
      "Resource": "*"
    }
  ]
}
```

### 10. 📊 Monitor with IAM Access Analyzer

**What**: Identifies resources shared with external accounts

**Detects**:
- S3 buckets accessible by other accounts
- IAM roles assumable externally
- KMS keys shared outside organization
- Lambda functions with public access

**Setup**:
```bash
1. IAM → Access Analyzer
2. Create Analyzer
3. Review findings
4. Remediate unintended public/external access
```

## 🛠️ Additional Best Practices

### Use AWS Organizations for Multi-Account Management

**Benefits**:
- Centralized billing
- Service Control Policies (SCPs) to restrict accounts
- Consolidated CloudTrail logging
- Resource sharing

**Example SCP** (Deny all regions except us-east-1):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

### Set Strong Password Policy

```bash
Requirements:
- Minimum 14 characters
- Uppercase + lowercase + numbers + symbols
- Password expiration: 90 days
- Prevent reuse: Last 10 passwords
- Account lockout: 5 failed attempts

IAM → Account Settings → Password Policy
```

### Tag IAM Resources

**Why**: Easier to manage, track costs, enforce policies

```bash
Common Tags:
- Department: Engineering, Marketing, Finance
- Project: Alpha, Beta, Gamma
- Environment: Production, Staging, Development
- Owner: alice@company.com
- CostCenter: CC-1234
```

### Use AWS SSO for Large Organizations

**When to Use**: 50+ users, need centralized access management

**Benefits**:
- Single sign-on across multiple AWS accounts
- Integration with existing identity providers (Okta, Azure AD)
- Centralized user management
- Automatic credential rotation

## ⚠️ Common Security Mistakes

### 1. **Overly Permissive Policies**
```json
// DANGEROUS
{
  "Effect": "Allow",
  "Action": "*",  // All actions
  "Resource": "*"  // All resources
}
```

### 2. **Sharing Access Keys**
```
Problem: Multiple people using same access key
Risk: Can't attribute actions, key compromise affects everyone
Fix: Each person gets their own IAM user
```

### 3. **Committing Credentials to Git**
```bash
# Check for exposed keys
git secrets --scan-history

# If found:
1. Rotate credentials immediately
2. Add .env to .gitignore
3. Use git-secrets to prevent future commits
```

### 4. **No Monitoring/Alerting**
```
Set up alerts for:
- Root account login
- Failed login attempts (>5 in 5 minutes)
- IAM policy changes
- New access keys created
- Security group changes
```

### 5. **Not Reviewing Permissions Regularly**
```
Schedule quarterly reviews:
- Remove unused users
- Audit group memberships
- Check for overly permissive policies
- Review external access (Access Analyzer)
```

## 🚀 Quick Security Audit Checklist

### Run This Monthly:

**Root Account**:
- [ ] MFA enabled?
- [ ] No access keys exist?
- [ ] Last used: >30 days ago?

**IAM Users**:
- [ ] All active users have MFA?
- [ ] No unused access keys (>90 days)?
- [ ] No inactive users (>90 days)?
- [ ] Password policy enforced?

**Policies**:
- [ ] No inline policies (use managed policies)?
- [ ] No overly permissive policies (Action: "*")?
- [ ] All policies follow least privilege?

**Monitoring**:
- [ ] CloudTrail enabled and logging?
- [ ] IAM Access Analyzer running?
- [ ] CloudWatch alarms set for suspicious activity?

**Groups and Roles**:
- [ ] Users added to groups (not direct policy attachment)?
- [ ] Roles used for EC2/Lambda (not hardcoded keys)?
- [ ] Cross-account roles use external ID?

## 📚 Resources

- [AWS IAM Best Practices (Official)](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Security Best Practices Whitepaper](https://aws.amazon.com/architecture/security-identity-compliance/)
- [IAM Policy Simulator](https://policysim.aws.amazon.com/)
- [AWS Trusted Advisor](https://console.aws.amazon.com/trustedadvisor) - Free security checks

## 🔗 Related Topics

- [What is IAM? →](what-is-iam.md)
- [IAM Policies →](policies.md)
- [IAM Roles →](roles.md)
- [Users and Groups →](users-and-groups.md)

---

**Next Step**: Implement these practices systematically. Start with MFA and root account security, then expand to policies and monitoring.