# S3 Buckets and Objects 🗂️

Understand S3's fundamental building blocks.

## Buckets (Containers)

A **bucket** is a top-level container for storing objects. Like a folder that can hold unlimited files.

### Bucket Properties

| Property | Details |
|----------|---------|
| Name | Globally unique (worldwide unique) |
| Region | Where data is stored (us-east-1, etc.) |
| Version Control | Enable/disable versioning |
| Encryption | Default encryption method |
| Access Control | Who can read/write |

### Bucket Naming Rules

```
Valid:
- my-bucket
- my-bucket-2024
- company-data-prod
- 2024-backups

Invalid:
- MyBucket (no uppercase)
- my bucket (no spaces)
- my_bucket (underscores risky)
- my-bucket- (can't end with dash)
- -my-bucket (can't start with dash)
- mb (too short - min 3 chars)
- my-bucket (if already exists globally)

Rule: Lowercase, dashes, 3-63 characters, globally unique
```

### Creating a Bucket

```
AWS Console:
1. S3 Dashboard → Create Bucket
2. Bucket name: my-app-backups
3. Region: us-east-1
4. Block Public Access: ON (for security)
5. Versioning: Enable (optional)
6. Encryption: Enable (default recommended)
7. Create Bucket

Cost: FREE to create, pay only for storage
```

## Objects (Files)

An **object** is a file stored in S3. Each object has content + metadata.

### Object Properties

```
Object:
├─ Key (path/name): backups/2024-01-28/database.sql
├─ Content: Binary data (file contents)
├─ Size: 2.5 GB
├─ Metadata: 
│  ├─ Content-Type: application/sql
│  ├─ Last-Modified: 2024-01-28T15:30:00Z
│  ├─ ETag: "d41d8cd98f00b204e9800998ecf8427e"
│  └─ Storage Class: STANDARD
├─ Encryption: AES-256
├─ Permissions:
│  ├─ Owner: read/write
│  └─ Public: (none)
└─ Tags: env=prod, project=backup
```

### Maximum Object Size

```
Single PUT: Max 5 GB
Multipart Upload: Max 5 TB per object

Multipart used automatically for large files:
- Faster (parallel uploads)
- Reliable (retry only failed parts)
- Resumable (pause and continue)
```

### Flat Structure (No Folders)

```
Important: S3 has NO folders!

Appearance (console shows folders):
my-bucket/
├─ documents/
│  └─ report.pdf
├─ images/
│  └─ logo.png
└─ videos/
   └─ intro.mp4

Actually (flat storage):
- documents/report.pdf (object key)
- images/logo.png (object key)
- videos/intro.mp4 (object key)

The "/" is just part of the object name!
```

## Bucket Policies vs ACLs

### Bucket Policy (Recommended)

```
Applies to: Entire bucket and all objects
Syntax: JSON
Examples:
- Allow public read access
- Allow CloudFront access
- Allow cross-account access
- Deny unencrypted uploads

Applied at: Bucket level
```

### Access Control Lists (ACLs)

```
Applies to: Individual objects
Older method: Less common now
Examples: public-read, private, etc.

Recommendation: Use bucket policies instead
(More flexible, easier to manage)
```

## Object Metadata

### System Metadata

```
Set by S3 automatically:
- Content-Length: 2500000 (size in bytes)
- Last-Modified: 2024-01-28T15:30:00Z
- ETag: "d41d8cd98f00b204e9800998ecf8427e"
- x-amz-version-id: (if versioning enabled)
- x-amz-storage-class: STANDARD
```

### Custom Metadata

```
You can add:
- x-amz-meta-project: analytics
- x-amz-meta-author: john-smith
- x-amz-meta-version: 2.1
- x-amz-meta-created: 2024-01-28

Searchable and retrievable later
```

## Object Tags

```
Key-value pairs for organization:

Tags:
- env: production
- project: backup
- cost-center: 1234
- retention: 90days

Uses:
- S3 lifecycle policies (tag-based)
- Access control (deny if tag=sensitive)
- Cost allocation (track by tag)
```

## Common Operations

### Upload

```
Console: Drag & drop or click upload
CLI: aws s3 cp file.txt s3://my-bucket/
SDK: Put request to /bucket/key

For 5GB+ files: Use multipart upload
```

### Download

```
Console: Click object → Download
CLI: aws s3 cp s3://my-bucket/file.txt ./
URL: https://my-bucket.s3.amazonaws.com/file.txt
     (if publicly readable)
```

### Delete

```
Console: Select object → Delete
CLI: aws s3 rm s3://my-bucket/file.txt
Permanently deleted (unless versioning enabled)
```

### Copy/Move

```
Same bucket: aws s3 cp s3://bucket/file1.txt s3://bucket/file2.txt
Different bucket: aws s3 cp s3://bucket1/file.txt s3://bucket2/
Moving: Copy then delete source
```

## Bucket Limits

```
Per AWS Account (Soft Limits):
- Buckets: 100 (can request increase)
- Objects per bucket: Unlimited
- Bucket size: Unlimited
- Object size: 5 TB max

Most applications never hit these
```

## Pricing

```
Storage:
- First 50 TB/month: $0.023/GB
- Next 450 TB/month: $0.022/GB
- Over 500 TB/month: $0.021/GB

Requests:
- PUT/COPY/POST/LIST: $0.005 per 1,000
- GET/HEAD: $0.0004 per 1,000

Data Transfer:
- Within region: FREE
- To internet: $0.09/GB
- CloudFront: $0.085/GB
```

## Best Practices

✅ Enable versioning for important data
✅ Enable encryption (default: AES-256)
✅ Use bucket policies for access control
✅ Block public access by default
✅ Enable logging/monitoring
✅ Use lifecycle policies to archive old data
✅ Tag objects for organization
✅ Use CloudFront for frequent access

## Next Steps

→ [Storage Classes](./storage-classes.md) - Cost optimization
→ [Versioning](./versioning.md) - Keep file history
→ [Lifecycle Rules](./lifecycle-rules.md) - Auto-archive