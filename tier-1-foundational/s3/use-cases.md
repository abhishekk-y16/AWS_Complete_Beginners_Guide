# S3 Use Cases 🎯

Real-world scenarios where AWS S3 is the perfect storage solution.

## Use Case 1: Static Website Hosting

### Scenario

```
You're building: Portfolio website (HTML, CSS, JavaScript)

Requirements:
├─ Serve HTML pages, images, CSS
├─ Fast, reliable worldwide access
├─ Need HTTPS/SSL
├─ Low cost (no server needed)
└─ Auto-scale to traffic spikes

Why S3 is perfect:
├─ Static website hosting built-in
├─ CloudFront CDN integration (global delivery)
├─ HTTPS support with ACM certificates
├─ Pay only for what you store + bandwidth
└─ 11 9's durability (99.999999999%)
```

### Architecture

```
Your website files:
├─ index.html
├─ about.html
├─ css/style.css
├─ js/app.js
└─ images/logo.png

Upload to S3:
├─ Create bucket: my-portfolio-website
├─ Upload files
├─ Enable static website hosting
├─ Set index.html as default

Connect CloudFront CDN:
├─ Create distribution
├─ Point to S3 bucket
├─ Attach SSL certificate
├─ Enable caching

Result:
└─ Global access from any region
   ├─ US: 50ms
   ├─ Europe: 100ms
   ├─ Asia: 150ms
   └─ All auto-cached!
```

### Cost Example

```
Small portfolio site:

Data stored:
├─ HTML/CSS/JS: 2MB
├─ Images: 50MB
├─ Total: 52MB
└─ Monthly cost: 52MB × $0.023/GB = $0.001

Bandwidth:
├─ Monthly visitors: 10,000
├─ Avg page size: 500KB
├─ Monthly transfer: 5GB
├─ Cost: 5GB × $0.085/GB = $0.43

CDN (CloudFront):
├─ Same 5GB served globally
├─ Cost: 5GB × $0.085/GB = $0.43

Total monthly: ~$0.87
Annual: ~$10.40

Perfect for: Freelancers, portfolios, blogs
```

## Use Case 2: Mobile App Backend Storage

### Scenario

```
You're building: Photo sharing app (Instagram-like)

Requirements:
├─ Store user-uploaded photos
├─ Generate thumbnails automatically
├─ Serve images fast worldwide
├─ Handle millions of photos
├─ Create resized versions (mobile, web, high-res)
├─ Secure storage (users can't see others' photos)
└─ Archive old photos

Why S3 is perfect:
├─ Scales to petabytes automatically
├─ Lambda integration: Auto-thumbnail generation
├─ Pre-signed URLs: Secure access without secrets
├─ Lifecycle rules: Auto-archive old files
├─ CloudFront: Fast image delivery
├─ Storage classes: Glacier for archives
```

### Architecture

```
User uploads photo
        │
        ▼
  S3 bucket receives
        │
        ├─ Triggers Lambda
        │      │
        │      ├─ Resize to 200×200 (thumbnail)
        │      ├─ Resize to 800×600 (web)
        │      └─ Keep original (high-res)
        │
        ├─ Store metadata in DynamoDB
        │   (photo ID, user ID, timestamp)
        │
        └─ CloudFront caches for fast delivery
        
User views photo
        │
        ├─ App requests from CloudFront
        │  (fast, cached globally)
        │
        └─ If not cached:
           ├─ Fetch from S3
           ├─ Cache in CloudFront
           └─ 2nd request instant
```

### Cost Example

```
Growing photo app:

Users: 100,000
Monthly photos: 50,000
Avg photo: 3MB

Storage:
├─ Original: 50,000 × 3MB = 150GB
├─ Thumbnail: 50,000 × 0.3MB = 15GB
├─ Web: 50,000 × 1MB = 50GB
├─ Total: 215GB
├─ Cost: 215GB × $0.023/GB = $4.95

Requests:
├─ Upload requests: 50,000 × $0.0005 = $25
├─ Download requests: 500,000 × $0.0004 = $200
└─ Lambda (thumbnail generation): ~$10

CloudFront (image delivery):
├─ 500GB served monthly: 500GB × $0.085 = $42.50

Total monthly: ~$282.45
Annual: ~$3,389

Per user (100K users): $0.0282/month
Scales beautifully!
```

## Use Case 3: Data Lake for Analytics

### Scenario

```
You're building: Business data warehouse

Requirements:
├─ Store data from multiple sources:
│  ├─ App databases (via RDS)
│  ├─ Mobile analytics (logs)
│  ├─ Web server logs
│  ├─ CRM data
│  └─ External APIs
├─ Query data with SQL (AWS Athena)
├─ Create reports and dashboards
├─ Archive historical data (years)
├─ Keep 5 years of data
└─ Control costs

Why S3 is perfect:
├─ Data lake: Central repository
├─ Structured (CSV, Parquet) + unstructured (logs)
├─ Athena: Query S3 with SQL directly
├─ Partitioning: Organize by date, region, etc.
├─ Redshift Spectrum: Advanced analytics
├─ Lifecycle: Archive to Glacier (90% cheaper)
```

### Architecture

```
Data Sources
├─ RDS Database
├─ Application Logs
├─ Mobile Analytics
├─ Web Server Logs
└─ Third-party APIs
        │
        ▼
    Lambda (ETL)
    ├─ Transform data
    ├─ Convert to Parquet (compress)
    └─ Partition by date/region
        │
        ▼
    S3 Data Lake
    ├─ Raw data/logs (30 days)
    ├─ Processed data (Parquet format)
    └─ Historical archive (Glacier)
        │
    ┌───┴───┬───────────┐
    │       │           │
    ▼       ▼           ▼
  Athena  Redshift   QuickSight
  (SQL)  (Analytics) (BI Dashboards)
```

### Partitioning Example

```
S3 bucket structure:

s3://my-data-lake/
├─ year=2024/
│  ├─ month=01/
│  │  ├─ day=01/
│  │  │  ├─ sales-2024-01-01.parquet
│  │  │  ├─ users-2024-01-01.parquet
│  │  │  └─ events-2024-01-01.parquet
│  │  ├─ day=02/
│  │  │  └─ ...
│  │  └─ ...
│  └─ month=02/
│     └─ ...
└─ year=2023/
   └─ ... (archived to Glacier)

Athena query:
SELECT SUM(revenue), region
FROM sales
WHERE year=2024 AND month=01
GROUP BY region;

Bonus: Only scans data in that partition!
Cost: Only charges for data scanned
```

### Cost Example

```
Data lake with 5 years of history:

Data stored:
├─ Year 1: 200GB (hot, S3 Standard)
├─ Year 2: 200GB (warm, S3-IA)
├─ Year 3: 200GB (warm, S3-IA)
├─ Year 4: 200GB (cold, Glacier)
└─ Year 5: 200GB (cold, Glacier)

Monthly storage cost:
├─ S3 Standard (200GB): 200 × $0.023 = $4.60
├─ S3-IA (400GB): 400 × $0.0125 = $5.00
├─ Glacier (400GB): 400 × $0.004 = $1.60
└─ Total storage: ~$11.20

Athena queries (assume 50 queries/month):
├─ Avg data scanned: 10GB per query
├─ Cost: 50 × 10GB × $5/TB = $2.50

Total monthly: ~$13.70
Annual: ~$164.40

Perfect for: Enterprise analytics, regulatory storage
```

## Use Case 4: Backup & Disaster Recovery

### Scenario

```
You're protecting: Database backups, application code

Requirements:
├─ Daily backups of production database
├─ Version control for code/configs
├─ Long-term retention (7 years for compliance)
├─ Fast recovery after disaster
├─ Encryption for security
├─ Geographic redundancy (backup in another region)
└─ Low cost (backups are accessed rarely)

Why S3 is perfect:
├─ Durability: 99.999999999% (11 9's)
├─ Encryption: Server-side encryption built-in
├─ Cross-region replication: Disaster recovery
├─ Versioning: Restore any previous version
├─ Lifecycle: Auto-archive old backups
└─ Cost: Cheapest long-term storage (Glacier)
```

### Backup Strategy

```
Daily backup process:

1. RDS automated backup
   └─ Snapshots kept for 35 days in AWS

2. Export to S3 (daily)
   ├─ Database dump: 50GB
   ├─ Compressed to Parquet: 10GB
   ├─ Upload to S3 Standard
   └─ Keep for 1 year

3. Weekly full backup
   └─ Keep for 5 years in Glacier

4. Monthly snapshots
   └─ Keep for 7 years in Glacier

Lifecycle rules:
├─ 0-30 days: S3 Standard (hot)
├─ 30-90 days: S3-IA (warm)
└─ 90+ days: Glacier (cold)

Recovery:
├─ Disaster in last 30 days?
│  └─ Restore from S3 Standard (5 min)
├─ Disaster in last year?
│  └─ Restore from S3-IA (30 min)
└─ Disaster long ago?
   └─ Restore from Glacier (4 hours)
```

### Cost Example

```
Backup for mid-size company:

Data backed up:
├─ RDS database: 500GB
├─ Application data: 100GB
├─ Code & configs: 10GB
└─ Total: 610GB

Monthly backups stored:

Current month (S3 Standard):
├─ 610GB × $0.023 = $14.03

Last 3 months (S3-IA):
├─ 3 × 610GB × $0.0125 = $22.88

Last year (Glacier):
├─ 9 × 610GB × $0.004 = $21.96

5-year archives (Glacier):
├─ 60 × 610GB × $0.004 = $146.40

Total monthly: ~$205.27
Annual: ~$2,463

Value: Can recover from any disaster
ROI: Worth every penny!
```

## Use Case 5: Content Distribution

### Scenario

```
You're running: SaaS application with global users

Requirements:
├─ Software downloads (installers, updates)
├─ Documentation and help files
├─ API assets (icons, logos, images)
├─ User-generated content
├─ Serve from any location (global)
├─ Fast downloads (100+ Mbps)
├─ Version control (multiple versions available)
└─ Download analytics

Why S3 is perfect:
├─ CloudFront: Distributes globally
├─ Pre-signed URLs: Time-limited access
├─ Versioning: Multiple versions at once
├─ Access logs: Track downloads
├─ Bandwidth: Fast worldwide delivery
├─ Cost: Pay only for transfer
```

### Distribution Pattern

```
Users worldwide
├─ US: Download from edge in Virginia
├─ EU: Download from edge in Frankfurt
├─ Asia: Download from edge in Singapore
└─ All get: Original from S3 bucket

Speed improvement:
├─ Without CloudFront: 500ms (S3 latency)
├─ With CloudFront: 50ms (edge server)
└─ Improvement: 10x faster!

Cost:
├─ Without CloudFront: $0.09/GB (S3 egress)
├─ With CloudFront: $0.085/GB (cheaper!)
└─ Plus: Saves bandwidth costs
```

## Use Case 6: Machine Learning Training Data

### Scenario

```
You're training: ML models on large datasets

Requirements:
├─ Store raw data (images, videos, CSV)
├─ Organize training/validation/test sets
├─ Version datasets (experiment with different versions)
├─ Access from SageMaker training jobs
├─ Share data across team
├─ Keep data organized (1000s of files)
└─ High throughput reading

Why S3 is perfect:
├─ SageMaker: Direct integration
├─ Multipart upload: Fast uploads
├─ Batch operations: Organize 1000s of files
├─ Request rate: 3,500 PUTs/1,000 GETs per second
├─ Cost: Cheaper than alternatives
└─ Durability: Never lose training data
```

### Organization Example

```
s3://ml-training-data/
├─ datasets/
│  ├─ images-v1/
│  │  ├─ train/ (80% of data)
│  │  ├─ validation/ (10%)
│  │  └─ test/ (10%)
│  │
│  ├─ images-v2/ (improved version)
│  │  ├─ train/
│  │  ├─ validation/
│  │  └─ test/
│  │
│  └─ text-corpus/
│     ├─ raw/
│     ├─ cleaned/
│     └─ tokenized/
│
└─ models/
   ├─ model-v1-accuracy-92%.zip
   ├─ model-v2-accuracy-94%.zip
   └─ model-v3-accuracy-96%.zip

SageMaker can read directly:
├─ Training job references S3 path
├─ Auto-downloads to training instance
├─ Parallel reads across multiple instances
└─ High throughput to GPUs
```

## When NOT to Use S3

```
❌ Frequently changing data
   → Use: EBS for databases, DynamoDB for NoSQL

❌ Real-time transactional data
   → Use: RDS, DynamoDB, or Memcached

❌ High request rate (>1K/sec per object)
   → Use: DynamoDB with caching

❌ Search within data
   → Use: OpenSearch or Elasticsearch

❌ Small files with frequent access
   → Use: Database or cache

❌ Extremely low latency (microseconds)
   → Use: ElastiCache or local storage
```

## Best Practices by Use Case

### Website Hosting
✅ Enable versioning (rollback capability)
✅ Use CloudFront CDN (global speed)
✅ Enable compression (reduce bandwidth)
✅ Set cache headers (browser caching)
✅ Use HTTPS with ACM certificate

### Mobile Apps
✅ Use pre-signed URLs (secure without secrets)
✅ Generate thumbnails automatically (Lambda)
✅ Archive old uploads (lifecycle rules)
✅ Enable transfer acceleration (upload speed)
✅ Use S3 Intelligent-Tiering

### Data Lakes
✅ Partition by date/region (query efficiency)
✅ Use Parquet format (compression + speed)
✅ Archive old data (cost savings)
✅ Enable S3 Inventory (track files)
✅ Use Athena for querying (no servers)

### Backups
✅ Enable versioning
✅ Cross-region replication (disaster recovery)
✅ MFA delete (prevent accidents)
✅ Lifecycle to Glacier (cost optimization)
✅ Encryption mandatory

### Content Distribution
✅ CloudFront mandatory (global speed)
✅ Enable compression
✅ Set appropriate cache headers
✅ Monitor with CloudFront analytics
✅ Use S3 access logs

## Comparison: S3 vs Alternatives

```
Storage needs       → Best choice
─────────────────────────────────
Static website      → S3 + CloudFront
User files (photos) → S3 + CloudFront
Database backups    → S3 + Glacier
Real-time database  → RDS/DynamoDB
NoSQL JSON data     → DynamoDB
Cache layer         → ElastiCache
Search index        → OpenSearch
Machine learning    → S3 + SageMaker
Logs/time-series    → CloudWatch Logs
Fast disks (DB)     → EBS volumes
```

## Next Steps

→ [What is S3](./what-is-s3.md) - Full S3 overview
→ [Pricing](./pricing.md) - Cost breakdown
→ [Storage Classes](./storage-classes.md) - Choose the right tier
→ [Lifecycle Rules](./lifecycle-rules.md) - Automate cost savings