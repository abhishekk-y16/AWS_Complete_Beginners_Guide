# IAM Policies

**IAM Policies** are JSON documents that define permissions - what actions are allowed or denied on which AWS resources. Think of them as rule books that determine "who can do what."

## 🎯 What are IAM Policies?

Policies are the language IAM uses to grant or deny permissions. Every time someone or something tries to use an AWS resource, IAM checks the relevant policies to decide if the action is allowed.

## 📋 Policy Types

### 1. **Identity-Based Policies**
Attached to IAM users, groups, or roles

**Managed Policies** (Reusable)
- **AWS Managed**: Created by AWS (e.g., `AmazonS3ReadOnlyAccess`)
- **Customer Managed**: Created by you, reusable across users

**Inline Policies** (One-to-one)
- Embedded directly in a single user, group, or role
- Deleted when the identity is deleted

### 2. **Resource-Based Policies**
Attached directly to resources (S3 buckets, SQS queues, etc.)

### 3. **Permission Boundaries**
Set maximum permissions an identity can have

### 4. **Service Control Policies (SCPs)**
Used in AWS Organizations to restrict entire accounts

## 📝 Policy Structure

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadS3Bucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket",
        "arn:aws:s3:::my-bucket/*"
      ],
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "192.168.1.0/24"
        }
      }
    }
  ]
}
```

### Key Elements:

- **Version**: Policy language version (always `"2012-10-17"`)
- **Statement**: Array of permission statements
- **Sid**: (Optional) Statement ID for identification
- **Effect**: `"Allow"` or `"Deny"`
- **Action**: AWS service actions (e.g., `s3:GetObject`)
- **Resource**: ARN of resources the actions apply to
- **Condition**: (Optional) Conditions for when policy applies

## 🔍 Common Policy Examples

### Example 1: S3 Read-Only Access
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::prod-data-bucket",
        "arn:aws:s3:::prod-data-bucket/*"
      ]
    }
  ]
}
```

### Example 2: EC2 Start/Stop (No Delete)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": "ec2:TerminateInstances",
      "Resource": "*"
    }
  ]
}
```

### Example 3: DynamoDB Table Access
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query",
        "dynamodb:Scan"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Users"
    }
  ]
}
```

### Example 4: Multi-Service Developer Access
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:*",
        "s3:*",
        "dynamodb:*",
        "logs:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```

## 🔐 Policy Evaluation Logic

### Decision Process:
1. **Default**: Deny everything by default
2. **Explicit Deny**: Check for explicit deny (overrides everything)
3. **Organizations SCPs**: Check account-level restrictions
4. **Resource-Based Policies**: Check resource policies
5. **Identity-Based Policies**: Check user/group/role policies
6. **Permission Boundaries**: Check maximum permissions
7. **Final Decision**: Allow only if explicitly allowed and not denied

### Rule of Thumb:
```
Explicit DENY > Explicit ALLOW > Implicit DENY (default)
```

## 🎯 Best Practices

### ✅ DO
- **Grant Least Privilege**: Only permissions needed for the job
- **Use AWS Managed Policies**: Start with AWS-provided policies
- **Use Conditions**: Add IP restrictions, MFA requirements
- **Use Policy Simulator**: Test policies before applying
- **Document SIDs**: Add descriptive statement IDs

### ❌ DON'T
- **Use Wildcards Unnecessarily**: Avoid `"*"` in production
- **Grant Full Admin**: Use `AdministratorAccess` sparingly
- **Ignore Deny Statements**: They override allows
- **Hardcode Account IDs**: Use variables when possible

## 🛠️ Policy Tools

### 1. **IAM Policy Simulator**
```
Use: Test policies before applying
Access: IAM Console → Policy Simulator
Benefit: Avoid accidental lockouts
```

### 2. **Access Analyzer**
```
Use: Find overly permissive policies
Access: IAM Console → Access Analyzer
Benefit: Improve security posture
```

### 3. **Policy Generator**
```
Use: Create policies visually
Access: IAM Console → Create Policy → Visual Editor
Benefit: Easier for beginners
```

## 📊 Variables in Policies

### Policy Variables (Dynamic Values)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::company-data",
      "Condition": {
        "StringLike": {
          "s3:prefix": "home/${aws:username}/*"
        }
      }
    }
  ]
}
```

**Common Variables**:
- `${aws:username}` - IAM user name
- `${aws:userid}` - Unique user ID
- `${aws:SourceIp}` - IP address of requester
- `${aws:CurrentTime}` - Current date/time

## ⚠️ Common Mistakes

### 1. **NotAction vs Action**
```json
// DANGEROUS - Allows everything except S3
{
  "Effect": "Allow",
  "NotAction": "s3:*",
  "Resource": "*"
}

// BETTER - Explicitly list allowed services
{
  "Effect": "Allow",
  "Action": ["ec2:*", "lambda:*"],
  "Resource": "*"
}
```

### 2. **Resource ARN Mistakes**
```json
// WRONG - Missing /* for objects
"Resource": "arn:aws:s3:::my-bucket"

// CORRECT - Includes bucket and objects
"Resource": [
  "arn:aws:s3:::my-bucket",
  "arn:aws:s3:::my-bucket/*"
]
```

### 3. **Overly Permissive**
```json
// BAD - Full access to everything
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}

// GOOD - Specific actions and resources
{
  "Effect": "Allow",
  "Action": ["s3:GetObject"],
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

## 🚀 Getting Started

### Step 1: Use AWS Managed Policies First
```bash
Common AWS Managed Policies:
- ReadOnlyAccess
- PowerUserAccess
- AmazonS3ReadOnlyAccess
- AmazonEC2FullAccess
```

### Step 2: Test with Policy Simulator
```bash
1. IAM → Policies → Select policy
2. Click "Simulate"
3. Select user and actions to test
4. Review results
```

### Step 3: Create Custom Policy
```bash
1. IAM → Policies → Create Policy
2. Use Visual Editor or JSON
3. Add actions, resources, conditions
4. Review and create
5. Attach to users/groups/roles
```

## 🔗 Related Topics

- [IAM Roles →](roles.md)
- [Users and Groups →](users-and-groups.md)
- [IAM Best Practices →](best-practices.md)
- [What is IAM? →](what-is-iam.md)

## 📚 Learn More

- [AWS Policy Examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
- [Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
- [IAM Policy Simulator](https://policysim.aws.amazon.com/)

---

**Next Step**: Learn about [IAM Roles](roles.md) for service-to-service access.