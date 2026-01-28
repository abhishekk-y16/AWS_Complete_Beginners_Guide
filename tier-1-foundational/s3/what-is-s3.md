# AWS S3 (Simple Storage Service) 📦

An object storage service offering 99.999999999% (11 nines) durability - industry leading reliability.

## What is S3?

**S3** = A massive, scalable cloud storage service where you store files (objects) in named containers (buckets). Like having unlimited cloud hard drives organized by folder name.

## Why You Need S3

### Unlimited Scale 📈
- Store from 1 byte to 5 TB per object
- Unlimited total storage
- Automatic scaling (no capacity planning)

### 11 Nines Durability 🔐
- 99.999999999% durability (only 1 file lost per 10 million annually)
- Data replicated across multiple facilities
- Designed to survive data center failures

### Cost Effective 💰
- Standard: $0.023/GB/month (cheaper than disks)
- Infrequent Access: $0.0125/GB/month
- Archival: $0.004/GB/month
- Pay only for what you use

### Enterprise Features ✨
- Versioning (keep all file versions)
- Access control (IAM, bucket policies)
- Encryption (data at rest and in transit)
- Lifecycle policies (auto-delete old files)
- Replication (across regions)
- Monitoring (CloudWatch, CloudTrail)

## Common Use Cases

### 1. Static Website Hosting
```
├─ index.html
├─ styles.css
├─ logo.png
└─ script.js

Served directly from S3 (super fast, cheap)
Cost: ~$0.50/month for small site
```

### 2. Backup & Archive
```
Daily backups → S3 Standard (first 30 days)
            → S3 Glacier (after 30 days)

Cost: Minimal (archival is cheap)
Durability: Protected against disasters
```

### 3. Data Lake
```
Raw data → S3 Standard
Analytics → Athena queries directly
Reports → Generated from S3 data

Cost: Query pricing, not storage
```

### 4. Application Assets
```
User uploads → S3
Images, videos → Served via CloudFront
Database → Smaller, faster

Cost: Storage + transfer costs
```

## S3 Basics

### Buckets (Containers)
```
Bucket Name: my-company-photos
Region: us-east-1

Properties:
- Globally unique name (can't duplicate)
- Tied to specific region
- Versioning (optional)
- Access control
```

### Objects (Files)
```
Bucket: my-company-photos
Key: /2024/01/photo-001.jpg
Content: Image bytes
Metadata: Permissions, encryption, etc.

Like file path but objects are flat
```

### Key Features
- **Versioning**: Keep old versions, restore if needed
- **Lifecycle**: Auto-move old files to cheaper storage
- **Encryption**: Encrypt data before storing
- **Access Control**: Who can read/write
- **Replication**: Copy to other regions
- **Events**: Trigger Lambda when files uploaded

## Pricing Example

```
Small Website:
- 100 GB storage: $2.30/month (Standard)
- 10 GB transfer out: $0.90/month
- 1000 PUT requests: $0.01/month
Total: ~$3.21/month

Large Dataset:
- 1 TB storage: $23/month (Standard)
- Move to Glacier after 90 days: $4/month
- 10 TB transfer out: $900/month
Total: ~$927/month
```

## Learning Path

1. **[What is S3](./what-is-s3.md)** ← You are here
2. **[Buckets and Objects](./buckets-and-objects.md)** - Core concepts
3. **[Storage Classes](./storage-classes.md)** - Cost optimization
4. **[Versioning](./versioning.md)** - Keep file history
5. **[Lifecycle Rules](./lifecycle-rules.md)** - Auto-archive
6. **[Access Control](./access-control.md)** - Security

## Key Takeaways

✅ S3 = Unlimited, durable, cheap cloud storage
✅ 11 nines durability = Extremely reliable
✅ Pay only for storage used
✅ Combine with Glacier for long-term backup
✅ Perfect for backups, data lakes, static websites

## Next Steps

→ [Buckets and Objects](./buckets-and-objects.md) - Get started
→ [Storage Classes](./storage-classes.md) - Cost optimization
→ [Creating First Bucket](./creating-first-bucket.md) - Hands-on