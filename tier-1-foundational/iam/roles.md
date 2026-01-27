# IAM Roles

**IAM Roles** are like temporary visitor badges that AWS services or users can "wear" to gain specific permissions. Unlike IAM users (permanent identities), roles provide temporary security credentials that automatically rotate.

## 🎯 What are IAM Roles?

Roles solve the problem: **"How do I give AWS services or external users access to my resources without creating permanent credentials?"**

### Key Concept:
- **Users** = Permanent identity with long-term credentials
- **Roles** = Temporary identity with short-term credentials (15 min - 12 hours)

## 🔑 When to Use IAM Roles

### Use Case 1: Service-to-Service Access
```
Scenario: EC2 instance needs to read from S3
❌ BAD: Hardcode access keys in application code
✅ GOOD: Attach IAM role to EC2 instance
```

### Use Case 2: Cross-Account Access
```
Scenario: Partner company needs access to your resources
❌ BAD: Share IAM user credentials
✅ GOOD: Create cross-account role they can assume
```

### Use Case 3: Federated Users
```
Scenario: Corporate users need AWS access via existing login
❌ BAD: Create duplicate IAM users for everyone
✅ GOOD: Use roles with SAML/OIDC federation
```

### Use Case 4: Temporary Elevated Permissions
```
Scenario: Developer needs admin access for 1 hour
❌ BAD: Give permanent admin permissions
✅ GOOD: Let them assume admin role temporarily
```

## 📝 Role Components

### 1. **Trust Policy** (Who can assume this role?)
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

### 2. **Permission Policy** (What can the role do?)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

## 🔍 Common Role Types

### 1. **Service Roles**
Used by AWS services to access other AWS services

**Example: EC2 accessing S3**
```
Role Name: EC2-S3-Read-Role
Trust Policy: ec2.amazonaws.com
Permissions: s3:GetObject, s3:ListBucket
Attach To: EC2 instance
```

**Common Service Roles**:
- **Lambda Execution Role**: Lambda function accessing DynamoDB, S3
- **ECS Task Role**: Container accessing AWS services
- **EC2 Instance Profile**: EC2 accessing S3, DynamoDB, etc.

### 2. **Cross-Account Roles**
Allow users from another AWS account to access your resources

**Example: Partner Access**
```
Role Name: PartnerDataAccess
Trust Policy: arn:aws:iam::111111111111:root (partner account)
Permissions: s3:GetObject on specific bucket
Assume: Partner users switch to this role
```

### 3. **Federated Roles**
Allow external identity providers (Google, Active Directory) to access AWS

**Example: Corporate SSO**
```
Role Name: CorporateDevelopers
Trust Policy: SAML identity provider
Permissions: Developer access to specific resources
Assume: Users log in via corporate portal
```

### 4. **IAM User Assumable Roles**
Allow IAM users to temporarily elevate privileges

**Example: Admin Escalation**
```
Role Name: EmergencyAdmin
Trust Policy: Specific IAM users
Permissions: AdministratorAccess
Assume: User switches to role via console/CLI
```

## 🏢 Real-World Example: Lambda + DynamoDB

### Scenario: Lambda function needs to read from DynamoDB table

**Step 1: Create Role**
```
Role Name: LambdaDynamoDBReadRole
Trust Policy: lambda.amazonaws.com
```

**Step 2: Attach Permissions**
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
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

**Step 3: Attach Role to Lambda**
```bash
In Lambda console:
Configuration → Permissions → Execution Role → Select role
```

**Step 4: Lambda Code (No hardcoded credentials!)**
```python
import boto3

# Automatically uses attached role
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    response = table.get_item(Key={'userId': '123'})
    return response['Item']
```

## 🔐 Role Assumption Process

### How Roles Work:
1. **Request**: Entity (user/service) requests to assume role
2. **Verification**: AWS checks trust policy - is this entity allowed?
3. **Issue Credentials**: AWS STS issues temporary credentials (access key, secret key, session token)
4. **Use**: Entity uses credentials to access resources
5. **Expire**: Credentials automatically expire (15 min - 12 hours)

### CLI Example:
```bash
# Assume role
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/AdminRole \
  --role-session-name MySession

# Returns:
# - AccessKeyId
# - SecretAccessKey
# - SessionToken
# - Expiration time

# Use temporary credentials
export AWS_ACCESS_KEY_ID=<AccessKeyId>
export AWS_SECRET_ACCESS_KEY=<SecretAccessKey>
export AWS_SESSION_TOKEN=<SessionToken>
```

## 🎯 Best Practices

### ✅ DO
- **Use roles for EC2/Lambda/ECS**: Never hardcode credentials
- **Set maximum session duration**: Default 1 hour, max 12 hours
- **Use external ID for cross-account**: Prevents confused deputy problem
- **Require MFA to assume role**: Add condition for sensitive roles
- **Use specific trust policies**: Don't trust entire accounts unnecessarily

### ❌ DON'T
- **Hardcode credentials**: Use roles instead
- **Give overly broad permissions**: Least privilege principle
- **Trust unknown accounts**: Verify external account IDs
- **Skip external ID**: Required for third-party access
- **Use long session durations**: Shorter is more secure

## 🛠️ Creating Roles

### Method 1: AWS Console
```bash
1. IAM → Roles → Create Role
2. Select trusted entity:
   - AWS Service (EC2, Lambda, etc.)
   - Another AWS Account
   - Web Identity (Google, Facebook)
   - SAML 2.0 Federation
3. Attach permissions policies
4. Name and create role
```

### Method 2: AWS CLI
```bash
# Create role
aws iam create-role \
  --role-name MyEC2Role \
  --assume-role-policy-document file://trust-policy.json

# Attach policy
aws iam attach-role-policy \
  --role-name MyEC2Role \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

### Method 3: CloudFormation
```yaml
MyLambdaRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            Service: lambda.amazonaws.com
          Action: sts:AssumeRole
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    Policies:
      - PolicyName: DynamoDBAccess
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action:
                - dynamodb:GetItem
                - dynamodb:PutItem
              Resource: !GetAtt MyDynamoDBTable.Arn
```

## ⚠️ Common Mistakes

### 1. **Confused Deputy Problem**
```
Problem: Attacker tricks your service into accessing resources
Solution: Use external ID in trust policy

Trust Policy with External ID:
{
  "Condition": {
    "StringEquals": {
      "sts:ExternalId": "unique-identifier-12345"
    }
  }
}
```

### 2. **Overly Permissive Trust Policy**
```json
// BAD - Trusts entire account
{
  "Principal": {
    "AWS": "arn:aws:iam::111111111111:root"
  }
}

// GOOD - Trusts specific role
{
  "Principal": {
    "AWS": "arn:aws:iam::111111111111:role/SpecificRole"
  }
}
```

### 3. **Forgetting Instance Profile**
```
Problem: EC2 role created but not attached as instance profile
Symptom: EC2 can't find credentials
Solution: Create instance profile linking role to EC2

aws iam create-instance-profile --instance-profile-name MyProfile
aws iam add-role-to-instance-profile --instance-profile-name MyProfile --role-name MyRole
```

## 🚀 Getting Started

### Quick Start: EC2 Role for S3 Access

**Step 1: Create Role (Console)**
```bash
1. IAM → Roles → Create Role
2. Trusted Entity: AWS Service → EC2
3. Permissions: AmazonS3ReadOnlyAccess
4. Name: EC2-S3-Read-Role
5. Create
```

**Step 2: Attach to EC2 Instance**
```bash
1. EC2 Console → Select instance
2. Actions → Security → Modify IAM Role
3. Select: EC2-S3-Read-Role
4. Update IAM Role
```

**Step 3: Test (SSH into EC2)**
```bash
# No credentials needed in code!
aws s3 ls

# Boto3 Python example
import boto3
s3 = boto3.client('s3')
buckets = s3.list_buckets()
print(buckets)
```

## 🔗 Related Topics

- [IAM Policies →](policies.md)
- [Users and Groups →](users-and-groups.md)
- [IAM Best Practices →](best-practices.md)
- [What is IAM? →](what-is-iam.md)

## 📚 Learn More

- [AWS STS (Security Token Service)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [IAM Roles Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Cross-Account Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)

---

**Next Step**: Learn about [Users and Groups](users-and-groups.md) for managing team access.