# Amazon S3 (Simple Storage Service)

## 🎯 What is S3?

Amazon S3 is a cloud storage service where you can store and retrieve any amount of data from anywhere on the internet. It's designed to store files (called "objects") like photos, videos, backups, website files, or any type of data you need to keep safe and accessible.

Unlike your computer's hard drive, S3 is virtually unlimited in size, highly durable (your data won't get lost), and accessible from anywhere with an internet connection.

## 🔑 Key Concepts

- **Bucket**: A container for storing objects. Think of it as a top-level folder with a unique name across all of AWS.
- **Object**: Any file you store in S3 - could be an image, video, document, or any data. Maximum size: 5 TB per object.
- **Key**: The unique name/path for an object within a bucket (like a file path: `photos/2024/vacation.jpg`)
- **Region**: The geographic location where your bucket's data is physically stored
- **Storage Class**: Different pricing tiers based on how frequently you access your data
- **Versioning**: Keeps multiple versions of an object so you can recover from accidental deletions

## 💡 Real-World Analogy

S3 is like **a massive, magical storage warehouse**:

- **Bucket = Your personal storage unit** in the warehouse
- **Objects = Boxes/items** you put in your unit
- **Key = Label** on each box telling you what's inside
- **Storage Classes = Different sections** (climate-controlled vs regular, based on how often you access items)
- **Access Control = Locks and permissions** on who can open your unit
- **Versioning = Keeping old versions** of items even when you replace them
- **Durability = Warehouse copies** your items to 11 different locations automatically

## 🚀 Common Use Cases

1. **Website Hosting**: Store and serve static website files (HTML, CSS, images)
2. **Backup & Archive**: Keep backups of databases, files, or entire systems
3. **Media Storage**: Store photos, videos for applications (like Instagram or YouTube do)
4. **Data Lakes**: Store massive amounts of data for analytics and machine learning
5. **Software Distribution**: Host files for download (installers, updates, patches)
6. **Disaster Recovery**: Keep critical data safe in case of emergencies
7. **Content Delivery**: Serve files to users worldwide via CloudFront CDN

## 🛠️ Getting Started

### Prerequisites
- [ ] AWS account created
- [ ] Some files ready to upload (photos, documents, etc.)
- [ ] Basic understanding of files and folders

### Step-by-Step: Create Your First S3 Bucket

1. **Navigate to S3 Console**
   - Sign in to AWS Console
   - Search for "S3" in the services search bar
   - Click on "S3"

2. **Create a Bucket**
   - Click the orange "Create bucket" button

3. **Choose a Bucket Name** (IMPORTANT!)
   ```
   Bucket name: my-first-bucket-20250125
   ```
   - Must be globally unique across ALL AWS accounts
   - Must be lowercase, no spaces
   - Can use numbers and hyphens
   - Tip: Add date or random numbers to ensure uniqueness

4. **Select AWS Region**
   - Choose region closest to you or your users
   - Example: `US East (N. Virginia)` or `Asia Pacific (Mumbai)`
   - Affects latency and costs

5. **Object Ownership**
   - Leave default: "ACLs disabled (recommended)"

6. **Block Public Access Settings**
   - **Keep all boxes CHECKED** (block all public access)
   - For learning, you want private buckets
   - You can change this later if needed

7. **Bucket Versioning**
   - Leave "Disable" for now
   - You can enable later when you understand it

8. **Default Encryption**
   - Leave default: "Server-side encryption with Amazon S3 managed keys (SSE-S3)"
   - Your data will be automatically encrypted

9. **Click "Create bucket"**
   - Your bucket is ready!

### Upload Your First File

1. **Click on your bucket name** to open it

2. **Click "Upload"** button

3. **Add files**
   - Click "Add files" or drag-and-drop
   - Select a file from your computer

4. **Review settings**
   - Storage class: Standard (default)
   - Leave other settings as default

5. **Click "Upload"**
   - Wait for upload to complete
   - Click "Close"

6. **View your file**
   - You'll see it listed in the bucket
   - Click on it to see details

### Access Your File

**Via AWS Console:**
- Click on object → Click "Open" button

**Via URL (if public):**
```
https://my-first-bucket-20250125.s3.amazonaws.com/myfile.jpg
```

**Via AWS CLI:**
```bash
# Download file from S3
aws s3 cp s3://my-first-bucket-20250125/myfile.jpg ./myfile.jpg

# Upload file to S3
aws s3 cp myfile.jpg s3://my-first-bucket-20250125/
```

## 📊 Pricing Overview

S3 pricing is based on three main factors:

### Storage Costs (per GB per month)

1. **S3 Standard** - ~$0.023/GB
   - Frequently accessed data
   - Most expensive but fastest access

2. **S3 Intelligent-Tiering** - ~$0.023/GB + small monitoring fee
   - Automatically moves data between tiers
   - Good for unpredictable access patterns

3. **S3 Standard-IA** (Infrequent Access) - ~$0.0125/GB
   - Accessed less than once a month
   - Retrieval fee applies

4. **S3 Glacier Instant Retrieval** - ~$0.004/GB
   - Rarely accessed (quarterly)
   - Instant access when needed

5. **S3 Glacier Flexible Retrieval** - ~$0.0036/GB
   - Long-term archive
   - Minutes to hours retrieval

6. **S3 Glacier Deep Archive** - ~$0.00099/GB
   - Cheapest option for archival
   - 12-48 hours retrieval time

### Request Costs (per 1,000 requests)
- **PUT/COPY/POST/LIST**: ~$0.005 per 1,000 requests
- **GET/SELECT**: ~$0.0004 per 1,000 requests

### Data Transfer Costs
- **Data IN**: FREE
- **Data OUT to internet**: $0.09/GB (after first 1 GB free)
- **Data OUT to CloudFront**: FREE
- **Data OUT to AWS services in same region**: FREE

### Free Tier (First 12 months)
- **5 GB** of S3 Standard storage
- **20,000 GET** requests
- **2,000 PUT** requests
- **100 GB** data transfer out

💰 **Cost Tips**: 
- Use Intelligent-Tiering for data with unknown access patterns
- Enable S3 Lifecycle policies to automatically move old data to cheaper storage
- Delete incomplete multipart uploads (hidden cost!)
- Use S3 Storage Class Analysis to optimize storage classes

## ⚠️ Important Things to Know

- **Bucket Names are Global**: You can't use a name someone else has taken anywhere in the world
- **Eventual Consistency**: New objects are immediately readable, but updates might take a moment to propagate
- **No Folders**: S3 doesn't have real folders - it uses object keys that look like paths
- **Delete Carefully**: No "trash bin" - deleted objects are gone (unless versioning is enabled)
- **Region-Specific**: Buckets exist in one region, but names are global
- **99.999999999% Durability**: AWS stores your data in multiple facilities automatically
- **Public Access is Blocked by Default**: You must explicitly allow public access

## 🔗 Related Services

- **CloudFront**: CDN for fast content delivery worldwide (works seamlessly with S3)
- **AWS Backup**: Automated backup service for S3
- **S3 Transfer Acceleration**: Faster uploads over long distances
- **Athena**: Query S3 data using SQL without loading it anywhere
- **Glue**: ETL service for processing data in S3
- **Lambda**: Run code automatically when S3 objects are created/modified
- **IAM**: Control who can access your buckets and objects

## 📚 Next Steps

- [ ] Try tutorial: [Host a Static Website on S3](../../tutorials/s3-static-website.md)
- [ ] Learn about [S3 Storage Classes](storage-classes.md) in detail
- [ ] Understand [S3 Bucket Policies](buckets-and-objects.md)
- [ ] Explore [S3 Lifecycle Rules](lifecycle-rules.md)
- [ ] Set up [S3 Versioning](versioning.md)

## 🆘 Common Issues & Solutions

**Problem**: Can't access object via URL - "Access Denied"
**Solution**: 
- Bucket is private by default
- Either: Make bucket public (not recommended for learning)
- Or: Generate a pre-signed URL for temporary access
- Or: Use AWS Console to access

**Problem**: "Bucket name already exists" error
**Solution**:
- Bucket names are globally unique
- Try adding numbers or date: `my-bucket-20250125`
- Or use a more unique name

**Problem**: Accidentally deleted important file
**Solution**:
- If versioning was enabled: Restore previous version
- If not: File is gone permanently
- Prevention: Enable versioning on important buckets

**Problem**: Unexpected high costs
**Solution**:
- Check for incomplete multipart uploads (they cost money!)
- Review S3 Storage Class Analysis in console
- Check data transfer out costs
- Use S3 Lifecycle policies to move old data to cheaper storage

## 💡 Best Practices

1. **Enable Versioning**: For important data to protect against accidental deletion
2. **Use Lifecycle Policies**: Automatically move old data to cheaper storage tiers
3. **Encrypt Everything**: Use default encryption (it's free!)
4. **Tag Buckets**: Add tags for cost tracking and organization
5. **Block Public Access**: Unless you specifically need public buckets
6. **Use IAM Policies**: Control access at user/role level
7. **Enable MFA Delete**: Require multi-factor auth to delete objects (for critical buckets)
8. **Monitor with CloudWatch**: Track metrics like bucket size, request counts
9. **Use S3 Inventory**: Get regular reports on all objects
10. **Clean Up Regularly**: Delete unnecessary files and incomplete uploads

## 🎓 Hands-On Exercise

**Build a Photo Gallery Storage System**

1. **Create a bucket**
```bash
aws s3 mb s3://my-photo-gallery-20250125
```

2. **Create folder structure** (using prefixes)
```bash
aws s3 cp family.jpg s3://my-photo-gallery-20250125/2024/family.jpg
aws s3 cp vacation.jpg s3://my-photo-gallery-20250125/2024/vacation.jpg
aws s3 cp pet.jpg s3://my-photo-gallery-20250125/2025/pet.jpg
```

3. **List all objects**
```bash
aws s3 ls s3://my-photo-gallery-20250125/ --recursive
```

4. **Download entire folder**
```bash
aws s3 sync s3://my-photo-gallery-20250125/2024/ ./2024-photos/
```

5. **Set up lifecycle rule** (via console)
- Move files older than 90 days to S3 Glacier
- Delete files older than 365 days

## 🔐 Security Best Practices

**Making Objects Public (When Needed)**

If you need to share files publicly:

1. Unblock public access at bucket level
2. Add bucket policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-bucket-name/*"
  }]
}
```

**Better Alternative: Pre-signed URLs**

Generate temporary URLs that expire:
```bash
aws s3 presign s3://my-bucket/myfile.jpg --expires-in 3600
```
This creates a URL valid for 1 hour (3600 seconds)

## 📊 Monitoring Your S3 Usage

**Enable CloudWatch Metrics:**
- Go to bucket → Metrics tab
- Enable "Request metrics"
- View graphs for:
  - Total bucket size
  - Number of objects
  - Request counts
  - Data transfer

**Set Up Billing Alerts:**
1. Go to CloudWatch → Alarms
2. Create alarm for S3 costs
3. Get notified if costs exceed threshold

## 📖 Additional Resources

- [Official S3 Documentation](https://docs.aws.amazon.com/s3/)
- [S3 FAQs](https://aws.amazon.com/s3/faqs/)
- [S3 Pricing Calculator](https://calculator.aws/)
- [S3 Best Practices Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html)
- [Video: S3 Masterclass](https://www.aws.training/)

---

**Last Updated**: January 2025  
**Difficulty Level**: ⭐ Beginner  
**Estimated Learning Time**: 2-3 hours
