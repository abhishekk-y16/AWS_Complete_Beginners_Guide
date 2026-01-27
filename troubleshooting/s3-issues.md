# S3 Troubleshooting Guide 🪣

Common S3 issues and solutions.

## Access Denied When Uploading to S3

### Symptom
```
Error: AccessDenied
Message: Access Denied (403)
```

### Solutions

**1. Check bucket policy**
- S3 → Bucket → Permissions → Bucket Policy
- User's ARN listed as Principal?
- Policy has s3:PutObject action?

**2. Check user IAM policy**
- IAM → Users → [user] → Permissions
- Should include s3:PutObject
- Resource should be: arn:aws:s3:::bucket-name/*

**3. Check bucket ownership**
- Are you uploading to the right bucket?
- Bucket shows in your account?
- Not someone else's bucket?

**4. Add policy to user**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**5. Check bucket ACL**
- S3 → Bucket → Permissions → Access Control List
- Your account listed?
- Has Write permission?

## Cannot Download File from S3

### Symptom
```
AccessDenied error
403 Forbidden
```

### Solutions

**1. Check object permissions**
- S3 → Bucket → [object] → Permissions
- Your user should have read access
- Or bucket policy allows it

**2. Check bucket policy**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456:user/myuser"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

**3. Check if file is public**
- S3 → Bucket → [object] → Object ACL
- If you want public access, set Public Read
- Generate public URL if needed

**4. Check bucket versioning status**
- If versioning enabled
- Make sure accessing correct version
- Specify VersionId in request

## Files Disappearing from S3

### Symptom
```
File was there yesterday
Now it's gone!
```

### Solutions

**1. Check if versioning enabled**
- S3 → Bucket → Properties → Versioning
- If enabled, file may be "deleted" but recoverable
- Show versions of the file

**2. Check lifecycle policies**
- S3 → Bucket → Lifecycle Rules
- Expiration rule might be deleting files?
- Wrong filter? (e.g., deleting all *.log files?)
- Edit or disable rule

**3. Check storage class transition**
- Lifecycle might move to Glacier (appears gone)
- Lifecycle Rules → Check "Transition" actions
- May need to restore from Glacier

**4. Recover from versioning**
```bash
# List all versions
aws s3api list-object-versions --bucket my-bucket

# Restore deleted file
aws s3api get-object \
  --bucket my-bucket \
  --key filename.txt \
  --version-id VERSION_ID \
  filename.txt
```

## S3 Bucket Name Already Exists

### Symptom
```
Error: The specified bucket already exists
```

### Solutions

**1. Bucket name is globally unique**
- S3 bucket names must be unique across ALL AWS accounts
- Someone may have already claimed that name
- Try different name: my-bucket-2024-[randomnumber]

**2. You created it previously**
- Already have bucket with that name
- Check your buckets: S3 → Buckets
- Use existing bucket or delete old one

**3. Check different regions**
- Bucket may exist in another region
- List all buckets: `aws s3 ls`
- Use the existing one or rename your bucket

## Files Not Transferring

### Symptom
```
Upload stuck or very slow
```

### Solutions

**1. Check file size**
- Files over 5GB need multipart upload
- Smaller files: direct upload
- Stuck? Cancel and retry

**2. Use multipart upload for large files**
```bash
# AWS CLI handles multipart automatically
aws s3 cp large-file.zip s3://my-bucket/ \
  --storage-class STANDARD
```

**3. Check network**
- Internet connection stable?
- Bandwidth sufficient?
- Try again with smaller file first

**4. Check request timing**
- Large uploads may timeout
- Increase timeout in boto3/SDK
- Use transfer manager

## High S3 Costs

### Symptom
```
S3 bill higher than expected
```

### Solutions

**1. Check storage usage**
- S3 → Metrics → Storage
- Bucket → Objects summary
- How much data stored?

**2. Check request volume**
- S3 Console → Metrics → All requests
- Unusually high GET/PUT requests?
- Someone making lots of requests?

**3. Check storage classes**
- S3 → Bucket → Storage Class
- Glacier is cheaper but slower
- Frequent access = Standard
- Infrequent access = Standard-IA

**4. Use lifecycle policies**
- Move old data to cheaper storage
- Delete very old data
- Example:
  - 30 days → Standard-IA ($0.0125/GB)
  - 90 days → Glacier ($0.004/GB)
  - 365 days → Deep Archive ($0.00099/GB)

**5. Enable request metrics**
- S3 → Request Metrics
- See who is accessing what
- Identify waste

## Bucket Policy Not Applying

### Symptom
```
Added bucket policy
Still getting Access Denied
```

### Solutions

**1. Policy syntax error**
- S3 → Bucket → Permissions → Bucket Policy
- Errors shown? Fix JSON syntax

**2. Principal ARN is wrong**
```json
// ✗ Wrong - not a valid format
"Principal": "user/john"

// ✓ Correct - full ARN
"Principal": "arn:aws:iam::123456789:user/john"

// ✓ Correct - all principals
"Principal": "*"
```

**3. Resource specification wrong**
```json
// ✗ Wrong - forgot /*
"Resource": "arn:aws:s3:::my-bucket"

// ✓ Correct - for all objects
"Resource": "arn:aws:s3:::my-bucket/*"

// ✓ Correct - for bucket and objects
"Resource": [
  "arn:aws:s3:::my-bucket",
  "arn:aws:s3:::my-bucket/*"
]
```

**4. Condition not matching**
```json
{
  "Effect": "Allow",
  "Condition": {
    "IpAddress": {
      "aws:SourceIp": "192.168.1.0/24"
    }
  }
}
```
- Request must come from that IP
- If you're on different IP, denied!

## Can't Enable Versioning

### Symptom
```
Versioning toggle not working
Can't enable version
```

### Solutions

**1. Check MFA Delete settings**
- S3 → Bucket → Properties → Versioning
- If MFA Delete enabled
- Root account required to disable
- Sign in as root and change

**2. Check bucket ownership**
- You own the bucket?
- In correct account?
- Sufficient permissions?

**3. Check if already enabled**
- Versioning → "Enabled"
- Already on!
- Just use it

## Cors Errors With S3

### Symptom
```
Cross-origin request blocked
Error: CORS policy

XMLHttpRequest from web page to S3 blocked
```

### Solutions

**1. Add CORS configuration**
```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
    "AllowedOrigins": ["https://example.com"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 3000
  }
]
```

**2. Add via console**
- S3 → Bucket → Permissions → CORS
- Paste configuration
- Save

**3. Allow all origins (for testing only)**
```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["*"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": ["*"]
  }
]
```

**WARNING**: Allow-all CORS is security risk! Use specific domains in production.

## 📖 Related Resources

- [S3 Documentation](../tier-1-foundational/s3/README.md)
- [S3 Pricing](../best-practices/cost-optimization.md)
- [Common Errors Guide](common-errors.md)
- [Security Best Practices](../best-practices/security-checklist.md)