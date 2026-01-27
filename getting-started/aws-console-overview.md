# AWS Console Overview 🖥️

Navigating the AWS Management Console.

## What is the Console?

**URL:** console.aws.amazon.com

**Your cloud control panel:**
- Visual interface
- No coding required
- Access all AWS services

## Top Navigation

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ AWS  🔍 Search  Services ▼  US East ▼  Account ▼ ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### 1. Search Bar 🔍 (Most Important!)

```
Type:
- "EC2" → Go to EC2
- "S3" → Go to S3
- "billing" → Cost dashboard

Shortcut: Ctrl+K (Cmd+K on Mac)
```

### 2. Services Menu

```
Click "Services":

💻 Compute: EC2, Lambda
💾 Storage: S3, EBS
📊 Database: RDS, DynamoDB
🌐 Networking: VPC, Route 53
🔒 Security: IAM, KMS
```

### 3. Region Selector (CRITICAL!)

```
Current: US East (N. Virginia)
         ↓ Click to change

Regions:
- us-east-1 (N. Virginia) ← Most services
- us-west-2 (Oregon)
- eu-west-1 (Ireland)
- ap-southeast-1 (Singapore)

🚨 Resources are region-specific!
EC2 in us-east-1 ≠ EC2 in us-west-2

Always check your region!
```

### 4. Account Menu

```
Click account name:

👤 My Account
💳 Billing Dashboard
🔒 Security Credentials
🚪 Sign Out
```

## Finding Services

### Tier 1 (Learn First)

**EC2:** Services → Compute → EC2
**S3:** Services → Storage → S3
**RDS:** Services → Database → RDS
**Lambda:** Services → Compute → Lambda
**IAM:** Services → Security → IAM
**VPC:** Services → Networking → VPC

### Monitoring & Billing

**CloudWatch:** Search "CloudWatch"
**Billing:** Account menu → Billing
**Cost Explorer:** Billing → Cost Explorer

## Console Tips

### Pin Favorites ⭐

```
1. Click Services
2. Find service
3. Click star icon
4. Appears in top bar

Recommend pinning:
⭐ EC2
⭐ S3
⭐ RDS
⭐ CloudWatch
```

### Keyboard Shortcuts

```
Ctrl+K / Cmd+K - Quick search
Alt+S - Services menu
Alt+R - Region selector
```

### CloudShell

```
Click >_ icon (top right)

✅ AWS CLI pre-installed
✅ Free to use
✅ No setup

Example:
aws s3 ls
aws ec2 describe-instances
```

## Common Navigation

### Launch EC2 Instance
```
1. Search "EC2"
2. Instances (left sidebar)
3. Launch Instance (orange button)
4. Follow wizard
```

### Create S3 Bucket
```
1. Search "S3"
2. Create bucket (orange button)
3. Enter name
4. Create
```

### Check Bill
```
1. Account name → Billing
2. See month-to-date spend
3. Click "Bills" for details
```

## Mobile App

**AWS Console Mobile:**
- iOS / Android
- View resources
- Start/stop instances
- Monitor billing
- Get alerts

## Common Issues

### Can't Find Service
```
Solution:
1. Use search bar
2. Check region
3. Check Services menu
```

### Resources Disappeared
```
"Where's my EC2?"

Solution:
1. Check region selector
2. Probably wrong region
3. Switch back
```

### Console Slow
```
Solutions:
- Clear browser cache
- Try different browser
- Disable extensions
```

## Customization

### Dark Mode
```
Settings ⚙️ → Theme → Dark mode
```

### Language
```
Settings ⚙️ → Language → Choose
```

## 📖 Next Steps

1. [Basic Terminology](basic-terminology.md)
2. [AWS Free Tier](aws-free-tier.md)
3. [First EC2 Instance](../tutorials/deploy-web-server.md)