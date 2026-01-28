# S3 Access Control 🔐

Control who can access S3 buckets and objects using IAM, bucket policies, and ACLs.

## Three Layers of S3 Security

```
┌─────────────────────────────────────┐
│ Layer 1: IAM Policies               │ Who can perform actions?
│ (AWS user/role level)               │
├─────────────────────────────────────┤
│ Layer 2: Bucket Policies            │ Public access rules?
│ (Bucket level)                      │
├─────────────────────────────────────┤
│ Layer 3: Object ACLs                │ Individual object access
│ (Object level - Legacy)             │
└─────────────────────────────────────┘
```

## IAM Policies

### What is IAM?

Identity and Access Management (IAM) controls who in your organization can access what.

```
IAM User: abhy4
Permissions:
├─ s3:GetObject (read)
├─ s3:PutObject (write)
└─ s3:DeleteObject (delete)

Scoped to: bucket "my-company-data"
Result: abhy4 can only access that bucket
```

### IAM Policy Example

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

Meaning:
- Effect: Allow or Deny
- Action: What can they do?
- Resource: Which bucket/objects?

### Common S3 Actions

```
s3:ListBucket           - List bucket contents
s3:GetObject            - Download objects
s3:PutObject            - Upload objects
s3:DeleteObject         - Delete objects
s3:GetObjectVersion     - Access versioned objects
s3:GetBucketPolicy      - Read bucket policy
s3:PutBucketPolicy      - Modify bucket policy
s3:DeleteBucket         - Delete bucket
s3:GetObjectAcl         - Read object permissions
s3:PutObjectAcl         - Modify object permissions
```

### IAM Policy: Limited Access

```json
{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::logs/*",
  "Condition": {
    "StringLike": {
      "s3:x-amz-server-side-encryption": "AES256"
    }
  }
}
```

Meaning:
- User can only read objects
- Only in "logs" folder
- Only if encrypted with AES256
- Maximum security!

## Bucket Policies

### What is a Bucket Policy?

Applied at bucket level, controls access from outside your organization (often public).

```
Scenario: Public website files
┌─────────────┐
│ S3 Bucket   │
├─ /index.html│ ← Bucket Policy: Allow public read
├─ /style.css │ ← Anyone can download
└─ /image.jpg │ ← No AWS credentials needed
```

### Public Read Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-website/*"
    }
  ]
}
```

Meaning:
- Principal: "*" = Anyone on internet
- Action: GetObject = Read only
- No write/delete permissions
- Perfect for: Static website hosting

### Conditional Public Read

```json
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::assets/*",
  "Condition": {
    "IpAddress": {
      "aws:SourceIp": [
        "203.0.113.0/24",
        "198.51.100.0/24"
      ]
    }
  }
}
```

Meaning:
- Anyone CAN read
- But ONLY from specific IP ranges
- Example: Company offices, data centers

### Deny Policy (Block All Public)

```json
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:*",
  "Resource": "arn:aws:s3:::private-data/*"
}
```

Meaning:
- Explicitly block: Nobody (not even root!)
- Prevents accidental public access
- Super secure

## Cross-Account Access

### Scenario: Company A Needs Company B's Data

```
Company B (Data Owner):
├─ Bucket: analytics-data
├─ Bucket Policy: Allow specific role from Company A
└─ Result: Company A can read data

Company A (Data Consumer):
├─ IAM Role: external-access
├─ Assumes: Role in Company B account
└─ Accesses: analytics-data bucket
```

### Bucket Policy for Cross-Account

```json
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::ACCOUNT-B:role/external-access"
  },
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::analytics-data/*"
}
```

Meaning:
- Account B's role can read
- No need to copy data
- Real-time access to source

## Presigned URLs

### What is a Presigned URL?

Time-limited URL that grants temporary access without AWS credentials.

```
Regular URL: https://s3.amazonaws.com/mybucket/file.pdf
❌ Blocked (no credentials)

Presigned URL: https://s3.amazonaws.com/mybucket/file.pdf?
X-Amz-Credential=...&X-Amz-Expires=3600
✅ Works for 1 hour (3600 seconds)
```

### Use Cases

```
1. Download Link
   User clicks → Temporary download link
   Expires → Link becomes invalid

2. Upload Link
   User has form → Presigned URL for upload
   Direct to S3 (no server middleman)

3. Mobile App
   App → Get presigned URL from backend
   App → Upload directly to S3
   Result: No need for server storage
```

### Generating Presigned URL (Python)

```python
import boto3

s3 = boto3.client('s3')

# Presigned download URL
url = s3.generate_presigned_url(
    'get_object',
    Params={
        'Bucket': 'my-bucket',
        'Key': 'report.pdf'
    },
    ExpiresIn=3600  # 1 hour
)

print(url)  # User clicks this link
```

### Time Expiration

```
URL created: 2024-01-15 14:00
ExpiresIn: 3600 (1 hour)
Valid until: 2024-01-15 15:00

After 15:01: ❌ Access Denied
Before 15:00: ✅ Download works
```

## Block Public Access Settings

### What is Block Public Access?

Extra layer preventing accidental public exposure.

```
├─ Block public ACLs
├─ Block public bucket policies
├─ Ignore existing public ACLs
└─ Ignore existing public bucket policies
```

### Scenario: Development vs Production

```
Development Bucket:
├─ Block Public Access: OFF
├─ Team can make things public quickly
└─ Faster testing

Production Bucket:
├─ Block Public Access: ON
├─ Even admin can't accidentally go public
└─ Maximum safety
```

## Object ACLs (Legacy)

### What is ACL?

Access Control List - old method, mostly replaced by IAM/bucket policies.

```
Object permissions:
├─ Private (default)
├─ Public-Read
├─ Public-Read-Write
├─ Authenticated-Read
└─ Bucket-Owner-Full-Control
```

### Why Avoid ACLs?

```
Problems:
❌ Limited control (only 6 options)
❌ Hard to audit
❌ Mixing IAM + ACL = confusing
❌ Not as flexible

Better: Use IAM + Bucket Policies
✅ Detailed control
✅ Easier to manage
✅ Clear inheritance
```

## Access Scenarios

### Scenario 1: Public Website

```
Bucket: my-website
├─ index.html (public)
├─ style.css (public)
├─ app.js (public)
└─ /data/ (private - not exposed)

Bucket Policy:
├─ Allow public: s3:GetObject on "/*"
└─ Deny: DeleteObject (no deletion)

Result: Visitors can view site, can't break it
```

### Scenario 2: Company Data Access

```
Bucket: company-reports
├─ Employees: s3:GetObject, s3:ListBucket
├─ Managers: + s3:PutObject (upload)
├─ Finance: + s3:DeleteObject (clean old)
└─ Interns: None (no access)

Setup: IAM policies per group
Result: Granular, role-based access
```

### Scenario 3: Third-Party Contractor

```
Contractor needs: Upload completed work

Solution:
├─ Generate presigned URL
├─ URL valid: 24 hours
├─ Action: PutObject only
└─ Result: Contractor uploads without AWS account

Revocation:
└─ Time expires → No more access
```

### Scenario 4: Application Upload

```
Architecture:
┌──────────┐
│ App      │
├──────────┤
│ Backend  │─→ Generate Presigned URL
└──────────┘
    ↓
┌──────────────┐
│ Mobile User  │ Upload directly to S3
└──────────────┘
    ↓
┌──────────┐
│ S3       │
└──────────┘

Benefits:
✅ No server bandwidth for file upload
✅ Direct to storage
✅ Scalable
```

## Common Security Mistakes

### ✗ Mistake 1: Using Bucket Policy + Overly Permissive IAM

```
Wrong:
├─ IAM: s3:* (all actions)
├─ Bucket Policy: Allow public
└─ Result: Bucket fully exposed!

Right:
├─ IAM: s3:GetObject only
├─ Bucket Policy: None (private)
└─ Result: Only internal access
```

### ✗ Mistake 2: Presigned URLs Without Expiration

```
Wrong:
url = s3.generate_presigned_url(
    'get_object',
    ExpiresIn=604800  # 7 days too long!
)

Right:
url = s3.generate_presigned_url(
    'get_object',
    ExpiresIn=3600  # 1 hour
)
```

### ✗ Mistake 3: Storing Credentials in Code

```
Wrong:
s3 = boto3.client('s3',
    aws_access_key_id='AKIA...',
    aws_secret_access_key='...'
)

Right:
# Use IAM Role (credentials auto-managed)
s3 = boto3.client('s3')
```

### ✗ Mistake 4: Not Using Block Public Access

```
Wrong:
├─ Bucket Policy: Public
├─ No Block Public Access
├─ Someone deletes policy by accident
└─ Result: EXPOSED!

Right:
├─ Bucket Policy: Public (intentional)
├─ Enable: Block Public Access
├─ Prevents: Accidental changes
└─ Result: Double-protected
```

## Audit & Monitoring

### CloudTrail

```
Logs all S3 API calls:
- Who accessed what?
- When did they access?
- Did access succeed?

Example:
2024-01-15 14:23:45 | abhy4 | GetObject | /file.pdf | SUCCESS
2024-01-15 14:24:10 | bot | PutObject | /data.csv | DENIED
```

### S3 Access Logs

```
Bucket logging:
- Enable S3 Access Logging
- Logs to another bucket
- Records all requests

Information:
├─ Requester IP
├─ Request time
├─ Action (GET, PUT, DELETE)
├─ Key name
├─ Response status
└─ Bytes sent/received
```

### Cost of Access Logs

```
1 million requests/day
= 30 million/month
Cost: ~$0.50/month
Benefit: Complete audit trail
```

## Best Practices

✅ Use IAM for employees
✅ Use bucket policies for public access
✅ Enable Block Public Access (production)
✅ Use presigned URLs for temporary access
✅ Set short expiration on presigned URLs
✅ Enable CloudTrail for audit
✅ Avoid ACLs (use IAM instead)
✅ Review permissions quarterly
✅ Principle of least privilege
✅ Never store credentials in code

## Encryption

### Server-Side Encryption

```
Upload unencrypted → S3 encrypts
├─ AES256 (default, free)
├─ KMS (more control, costs)
└─ Customer-provided key

Advantage: Data encrypted at rest
```

### Access Control + Encryption

```
Combination:
├─ IAM prevents unauthorized access
├─ Encryption secures data
└─ Result: Defense in depth
```

## Next Steps

→ [Buckets and Objects](./buckets-and-objects.md) - Core concepts
→ [Lifecycle Rules](./lifecycle-rules.md) - Auto-management
→ [Storage Classes](./storage-classes.md) - Cost optimization