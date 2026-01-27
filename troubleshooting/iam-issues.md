# IAM Troubleshooting Guide 🔑

Common IAM issues and solutions.

## "Access Denied" or "User is not authorized"

### Symptom
```
Action: iam:CreateRole
Error: User: arn:aws:iam::123456:user/john is not authorized
```

### Root Causes

**1. Policy not attached to user**
- IAM → Users → Select user
- Permissions tab → No policy listed?
- Add policy!

**2. Wrong permission name**
- Policy says `s3:GetObjectXyz` (typo)
- Should be `s3:GetObject`
- Check AWS documentation for exact action names

**3. Explicit Deny overrides Allow**
- Even if policy says "Allow"
- If another policy says "Deny"
- Result = Deny wins!
- Check all policies

**4. Condition doesn't match**
```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "*",
  "Condition": {
    "IpAddress": {
      "aws:SourceIp": "192.168.1.0/24"
    }
  }
}
```
- This only works from that IP range
- Outside that IP? Denied!

### Solutions

**1. Check user policies**
```
IAM → Users → [user] → Permissions
View detailed policy → Check action names
```

**2. Add policy**
- Click "Add permission"
- Choose managed policy or inline policy
- Save

**3. Use Policy Simulator**
- IAM → Access Analyzer → Policy Simulator
- User: select user
- Action: type action
- Resource: specify resource
- Result: shows if allowed/denied and why!

**4. Check role trust policy**
- For roles: Role → Trust Relationships
- Make sure correct principal (user/service) listed

## Cannot Create User/Role/Policy

### Symptom
```
Permission Denied when trying to create IAM resources
```

### Solutions

**1. Check your own permissions**
- You need IAM policy allowing iam:CreateUser, iam:CreateRole, etc.
- Console → Click your name → Security Credentials
- Check policies attached

**2. Check limits**
- Account limits exist!
- IAM → Account Settings → Account Information
- IAM Users limit (default 5000)
- Roles per account limit (1000)
- Request increase if needed

**3. Check name conflicts**
- User/role with that name already exists?
- Try different name
- Delete old one first?

## Assumed Role Doesn't Have Permissions

### Symptom
```
I assumed role X, but can't access service Y
```

### Root Causes

**1. Role policy insufficient**
- Role → Permissions
- Missing required action
- Add policy to role

**2. Trust relationship wrong**
- Role → Trust Relationships
- Your identity not listed as principal?
- Add your ARN

**3. STS token expired**
- Temporary credentials expire
- Get new credentials
- Run `aws sts get-caller-identity` to check

### Solutions

```bash
# Check current identity
aws sts get-caller-identity
# Shows: UserArn, AccountId, UserId

# Assume role properly
aws sts assume-role --role-arn arn:aws:iam::123456:role/MyRole --role-session-name my-session

# Use returned credentials
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...

# Verify
aws sts get-caller-identity
# Should now show role ARN
```

## "arn:aws:iam::123456:user/john is not authorized to perform..."

### Solutions

**1. Identify what action is needed**
```
Error says: "iam:PutUserPolicy"
You need policy allowing: iam:PutUserPolicy
```

**2. Find exact action name**
- AWS docs for service
- Find action names
- Copy exact spelling

**3. Create or modify policy**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:PutUserPolicy",
        "iam:GetUserPolicy"
      ],
      "Resource": "arn:aws:iam::*:user/*"
    }
  ]
}
```

**4. Attach policy**
- Copy policy JSON
- IAM → Users → [user] → Add inline policy
- Paste JSON
- Save

## Users Can't See Each Other's Resources

### Symptom
```
User A created S3 bucket
User B cannot see it or access it
```

### Solutions

**1. Add bucket policy (for service permissions)**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456:user/userB"
      },
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**2. Add role policy (for service permissions)**
```json
{
  "Effect": "Allow",
  "Action": "s3:ListBucket",
  "Resource": "arn:aws:s3:::my-bucket"
}
```

**3. Enable cross-account access (if different accounts)**
- User A's account: Modify bucket policy
- Add User B's ARN as Principal

## Can't Assume Role from Console

### Symptom
```
Switch Role button doesn't work
Error when trying to assume role
```

### Solutions

**1. Check trust relationship**
- Role → Trust Relationships
- Find your user's ARN
- Should be listed as Principal

**2. Your user needs sts:AssumeRole**
```json
{
  "Effect": "Allow",
  "Action": "sts:AssumeRole",
  "Resource": "arn:aws:iam::123456:role/RoleName"
}
```

**3. Try from CLI**
```bash
aws sts assume-role \
  --role-arn arn:aws:iam::123456:role/MyRole \
  --role-session-name my-session
```

## MFA Not Working

### Symptom
```
Virtual MFA not accepting code
Hardware MFA token not working
```

### Solutions

**1. Check time sync (virtual MFA)**
- MFA token generates time-based codes
- Your device clock must be synchronized
- Sync device time with NTP

**2. Code already used**
- MFA codes valid for 30 seconds
- Try again in 30 seconds

**3. Try code from new authenticator app**
- Resynchronize or reinstall authenticator
- Get new code
- Try that code

**4. Reset MFA (if locked out)**
- Root account user can reset
- IAM → Users → [user]
- Security Credentials → Assigned MFA Device → Delete
- User re-adds MFA

**5. Using wrong account**
- MFA for Account A
- Trying to log into Account B
- Won't work! Add MFA to Account B

## Policy Becoming Invalid

### Symptom
```
Policy was working, now shows error
"Invalid policy"
```

### Solutions

**1. Check JSON syntax**
```
Missing comma? ✗
Missing quotes? ✗
Mismatched brackets? ✗
```

**2. Validate JSON**
- Use online JSON validator
- AWS Policy Simulator
- Both show exact error

**3. Policy version**
- Should start: `"Version": "2012-10-17"`
- Older versions may have deprecated actions
- Update to latest version

**4. Action name changed**
- AWS occasionally changes action names
- Check documentation for service
- Old actions deprecated
- Use new action names

## 📖 Related Resources

- [IAM Documentation](../tier-1-foundational/iam/README.md)
- [Policy Simulator](https://policysim.aws.amazon.com)
- [Common Errors Guide](common-errors.md)
- [Security Checklist](../best-practices/security-checklist.md)