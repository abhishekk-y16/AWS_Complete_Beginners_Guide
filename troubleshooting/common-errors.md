# AWS Common Errors Guide 🚨

Quick reference for most common AWS errors and solutions.

## Authentication & Authorization Errors

### Error: "User is not authorized"

**What it means:** You don't have permission to do this action.

**Quick Fix:**
1. Check your IAM user policies
2. Ask admin to add needed permission
3. Use Policy Simulator to test

**Example Error:**
```
Error: User: arn:aws:iam::123456789:user/john 
is not authorized to perform: s3:PutObject
```

**Solution:**
```json
{
  "Effect": "Allow",
  "Action": "s3:PutObject",
  "Resource": "*"
}
```

---

### Error: "InvalidClientTokenId"

**What it means:** Your AWS access keys are invalid or expired.

**Quick Fix:**
```bash
# Check which credentials you're using
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY

# Generate new keys
# AWS Console → IAM → Users → [Your User] → Security Credentials
# Delete old, create new
```

---

### Error: "Unauthorized operation"

**What it means:** Missing MFA or wrong credentials.

**Quick Fix:**
1. Enable MFA if required
2. Check credentials not expired
3. Verify using correct profile: `aws s3 ls --profile production`

---

## Service-Specific Errors

### Error: "NoSuchBucket"

**Service:** S3  
**What it means:** Bucket doesn't exist or you're in wrong region

**Quick Fix:**
```bash
# List your buckets
aws s3 ls

# Specify region
aws s3 ls s3://my-bucket --region us-west-2
```

---

### Error: "ValidationException"

**Common for:** DynamoDB, Lambda, API Gateway  
**What it means:** Invalid input or malformed request

**Examples & Fixes:**

```python
# ✗ Wrong - InvalidParameterException
table.get_item(Key={'id': 123})  # number instead of string

# ✓ Correct
table.get_item(Key={'id': '123'})  # string
```

---

### Error: "ThrottlingException"

**What it means:** You're making too many requests too fast

**Solutions:**
1. **Wait a moment** - Often fixes itself
2. **Exponential backoff:**
```python
import time
for attempt in range(5):
    try:
        result = make_request()
        break
    except ThrottlingException:
        wait_time = 2 ** attempt  # 1, 2, 4, 8, 16 seconds
        time.sleep(wait_time)
```

3. **Request limit increase:**
   - AWS Console → Service Quotas
   - Find service → Request quota increase
   - Usually approved in 15 minutes

---

### Error: "InsufficientCapacityException"

**What it means:** AWS doesn't have capacity for this resource in this location

**Solutions:**
1. Try different Availability Zone
2. Try different instance type
3. Wait a few minutes and retry
4. Contact AWS support if critical

---

### Error: "ResourceNotFoundException"

**What it means:** Resource doesn't exist

**Examples:**
```
Lambda function not found
RDS instance doesn't exist
EC2 security group not found
```

**Fix:**
```bash
# Find what actually exists
aws lambda list-functions
aws rds describe-db-instances
aws ec2 describe-security-groups
```

---

## Network & Connectivity Errors

### Error: "Connection timed out"

**Could be:**
1. Security group blocking traffic
2. Network ACL blocking traffic
3. Resource is not running
4. Public IP missing
5. Internet Gateway missing

**Diagnostic Steps:**
```bash
# 1. Check if running
aws ec2 describe-instances --instance-ids i-123456

# 2. Check security group
aws ec2 describe-security-groups --group-ids sg-123456

# 3. Check public IP
aws ec2 describe-instances --query 'Reservations[].Instances[].PublicIpAddress'

# 4. Try from same VPC
# Launch bastion host in VPC and SSH from there
```

---

### Error: "Network is unreachable"

**Could be:**
1. Wrong VPC selected
2. Route table missing internet gateway route
3. Subnet is private (no internet access)

**Fix:**
```bash
# Check route table
aws ec2 describe-route-tables --route-table-ids rtb-123456

# Should have route to Internet Gateway:
# Destination: 0.0.0.0/0
# Target: igw-xxxxx
```

---

## Cost & Billing Errors

### Error: "LimitExceeded" or "PricingException"

**What it means:** You've hit a limit or service quota

**Solutions:**
1. **Request limit increase:**
```
AWS Console → Service Quotas
Find service → Click quota → Request quota increase
```

2. **Check what's at limit:**
```bash
# EC2 instances
aws ec2 describe-account-attributes --attribute-names instance-quota

# IAM users
aws iam get-credential-report
```

3. **Cleanup unneeded resources:**
   - Delete old snapshots
   - Terminate unused instances
   - Remove old keys

---

### Error: "InsufficientBillingData"

**What it means:** Billing data not available yet (new account)

**Solution:** Wait 24 hours for first billing period data

---

## Common Error Messages by Service

### Lambda Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Task timed out` | Function too slow | Increase timeout or optimize code |
| `Out of memory` | Needs more RAM | Increase memory allocation |
| `Permission Denied` | Wrong IAM role | Add required permissions |
| `ResourceLimitExceeded` | Too many concurrent | Request higher concurrency quota |

### EC2 Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `UnauthorizedOperation` | Wrong security group | Check inbound rules |
| `Insufficient capacity` | No room in AZ | Try different AZ |
| `InstanceLimitExceeded` | Hit account limit | Request limit increase |
| `Cannot attach volume` | Wrong AZ | Volume and instance same AZ |

### S3 Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `NoSuchBucket` | Bucket doesn't exist | Check bucket name & region |
| `AccessDenied` | Wrong permissions | Add bucket policy |
| `SlowDown` | Too many requests | Add exponential backoff |
| `AllAccessDisabled` | Public access blocked | Disable "Block all public access" |

### RDS Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `DBInstanceNotFound` | DB doesn't exist | Check DB name & region |
| `DBSecurityGroupNotFound` | Security group deleted | Create new one |
| `DBInstanceAlreadyExists` | Name taken | Use different name |
| `MultiAZNotSupported` | Instance type too small | Use db.t3.small+ |

### DynamoDB Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `ValidationException` | Bad input format | Check key types |
| `ItemCollectionSizeLimitExceededException` | Partition key too hot | Distribute load |
| `ProvisionedThroughputExceededException` | Too many requests | Increase capacity |
| `ResourceInUseException` | Already exists | Use different name |

## Debugging Techniques

### 1. Check CloudWatch Logs
```bash
# List log groups
aws logs describe-log-groups

# View logs
aws logs tail /aws/lambda/my-function --follow
aws logs tail /aws/ec2/ --follow
```

### 2. Enable Detailed Monitoring
```bash
# EC2
aws ec2 monitor-instances --instance-ids i-123456

# RDS
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --enable-cloudwatch-logs-exports postgresql \
  --apply-immediately
```

### 3. Use AWS CLI Debug Mode
```bash
# Verbose output
aws s3 ls --debug

# Show request being made
aws s3 ls --debug | head -50
```

### 4. Test with Minimal Example
```python
# Instead of complex code, test simple example
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()
print(response)

# If this works, issue is in your logic
# If this fails, issue is IAM/credentials
```

### 5. Use IAM Policy Simulator
```
AWS Console → IAM → Access Analyzer → Policy Simulator
User: Select your user
Action: Type action you want to test
Resource: Specify resource
Result: Shows if allowed/denied and why
```

## Prevention Tips

### ✅ Before You Hit an Error

1. **Test with least privilege first**
   - Start with specific permissions
   - Add more only if needed

2. **Enable CloudTrail logging**
   - Tracks all API calls
   - Helps debug issues

3. **Use tags**
   - Tag resources by project
   - Easy to track and manage

4. **Monitor costs**
   - Enable billing alerts
   - Check every week

5. **Read error messages carefully**
   - AWS errors are specific
   - They often tell you exact fix

### 📖 Related Resources

- [IAM Troubleshooting](iam-issues.md)
- [EC2 Troubleshooting](ec2-issues.md)
- [S3 Troubleshooting](s3-issues.md)
- [Lambda Troubleshooting](lambda-issues.md)
- [Security Best Practices](../best-practices/security-checklist.md)
- [AWS Support](https://console.aws.amazon.com/support/)