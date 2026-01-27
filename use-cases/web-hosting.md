# Web Hosting on AWS 🌐

Complete guide to hosting a website or web application on AWS.

## Architecture Overview

### Simple Static Website
```
Domain → Route 53 DNS
         ↓
     CloudFront CDN
         ↓
      S3 Bucket
      (website files)
```

**Cost:** ~$1/month  
**Maintenance:** None (AWS managed)  
**Best for:** Blogs, documentation, portfolios

### Dynamic Web Application
```
Domain → Route 53 DNS
         ↓
    Elastic Load Balancer
         ↓
    EC2 Web Servers (ASG)
         ↓
    RDS Database
         ↓
    S3 for uploads
```

**Cost:** ~$50-200/month  
**Maintenance:** Application updates, monitoring  
**Best for:** Web apps, e-commerce, SaaS

### Serverless Web Application
```
Domain → Route 53 DNS → API Gateway
         ↓
      Lambda Functions
         ↓
    DynamoDB + S3
```

**Cost:** ~$10-100/month  
**Maintenance:** Minimal (no servers)  
**Best for:** Microservices, APIs, low-traffic apps

## Step 1: Choose Your Domain

### Option A: New Domain
1. Route 53 → Register Domain
2. Search for domain name
3. Add to cart
4. Complete registration (~$12/year)
5. Route 53 automatically manages DNS

### Option B: Existing Domain
1. Transfer to Route 53 (optional)
2. Or use Route 53 with external registrar
3. Point nameservers to Route 53

## Step 2: Static Website Hosting (S3 + CloudFront)

### Step-by-Step

**1. Create S3 bucket**
```
S3 → Create Bucket
Name: my-website.com
Region: us-east-1
Block public access: ✓ Block all
```

**2. Enable static website hosting**
```
Bucket → Properties → Static Website Hosting
Enable
Index document: index.html
Error document: 404.html
```

**3. Upload files**
```
Bucket → Upload
- index.html
- about.html
- style.css
- images/
```

**4. Create CloudFront distribution**
```
CloudFront → Create Distribution
Origin domain: my-website.com.s3.amazonaws.com
Viewer protocol policy: Redirect HTTP to HTTPS
Cache policy: Caching optimized
```

**5. Point domain to CloudFront**
```
Route 53 → Hosted Zone → Create Record
Type: A
Name: my-website.com
Alias: CloudFront distribution
```

**6. Add SSL certificate**
```
ACM → Request Certificate
Domain: my-website.com, www.my-website.com
Validation: DNS
CloudFront → Edit → Add certificate
```

**Result:** Your website is live with HTTPS!

**Cost:**
- S3 storage: ~$0.50/month (for small site)
- CloudFront: ~$0.85/month (1GB/month)
- Route 53: $0.50/month
- Domain: $12/year
- **Total: ~$1.50/month**

## Step 3: Dynamic Web Application (EC2)

### Architecture Setup

**1. Create VPC and Security Groups**
```
VPC → Create VPC
CIDR: 10.0.0.0/16
Subnets: public (10.0.1.0/24), private (10.0.2.0/24)

Security Groups:
- Web: Allow 80, 443 from 0.0.0.0/0
- Database: Allow 3306 from Web SG
```

**2. Create RDS Database**
```
RDS → Create Database
Engine: MySQL or PostgreSQL
Instance type: db.t3.micro (free tier)
Storage: 20GB
Backup retention: 7 days
```

**3. Create EC2 Instance**
```
EC2 → Launch Instance
AMI: Ubuntu 22.04
Instance type: t3.micro
VPC: Your VPC
Security group: Web SG

Storage: 30GB gp3
```

**4. Install Application**
```bash
# SSH to instance
ssh -i key.pem ubuntu@instance-ip

# Install web server
sudo apt update
sudo apt install nginx php-fpm php-mysql -y

# Upload application files
scp -r myapp/* ubuntu@instance-ip:/var/www/

# Configure nginx
sudo systemctl start nginx
```

**5. Setup Elastic IP + Auto Scaling**
```
Elastic IP → Allocate
Attach to EC2 instance

Auto Scaling Group → Create
Min: 1, Desired: 1, Max: 3
Triggers: Scale when CPU > 70%
```

**6. Create Load Balancer**
```
Load Balancer → Create ALB
Listeners: 80 (HTTP), 443 (HTTPS)
Target group: EC2 instances
Health check: /health

Redirect HTTP → HTTPS
```

**7. Point domain**
```
Route 53 → Create Record
Type: A
Alias: Load Balancer
```

**Cost:**
- EC2 (t3.micro): ~$10/month
- RDS (db.t3.micro): ~$15/month
- Load Balancer: ~$16/month
- Domain + Route 53: ~$1/month
- **Total: ~$42/month**

## Step 4: Serverless Web Application

### Architecture Setup

**1. Create API Gateway**
```
API Gateway → Create API
Type: REST API
Name: my-api
```

**2. Create Lambda Functions**
```
Lambda → Create Function
Runtime: Python 3.11
Handler: index.handler

def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello from Lambda'})
    }
```

**3. Create DynamoDB Table**
```
DynamoDB → Create Table
Table name: users
Partition key: userId (String)
Billing: Pay-per-request
```

**4. Add IAM Role to Lambda**
```
IAM → Create Role
Trust: Lambda
Policies:
- dynamodb:PutItem
- dynamodb:GetItem
- dynamodb:Query
```

**5. Connect API Gateway to Lambda**
```
API Gateway → Resource → Create Resource
Method: POST
Integration: Lambda
Lambda Function: my-function
```

**6. Deploy API**
```
API Gateway → Deploy
Stage: prod
Domain: my-api.execute-api.us-east-1.amazonaws.com
```

**7. Add custom domain**
```
Route 53 → Create Record
Type: A
Alias: API Gateway
```

**Cost:**
- Lambda: 1M requests free/month, then $0.20 per million
- DynamoDB: Pay-per-request (~$1-2/month small)
- API Gateway: ~$3.50 per million requests
- **Total: ~$5-10/month** (for small app)

## Monitoring and Maintenance

### Setup CloudWatch Monitoring

**1. CloudWatch Dashboard**
```
CloudWatch → Dashboards → Create
Add widgets:
- EC2 CPU usage
- RDS database connections
- Lambda invocations
- Request count
```

**2. Set Alarms**
```
CloudWatch → Alarms → Create Alarm
Metric: EC2 CPU
Threshold: > 80%
Action: Send SNS notification
```

**3. View Logs**
```
CloudWatch → Logs
- /aws/lambda/function-name
- /aws/rds/instance-name
- Application logs from EC2
```

### Security Checklist

- ✅ Enable SSL/TLS (HTTPS)
- ✅ Enable CloudTrail logging
- ✅ Setup WAF on CloudFront
- ✅ Database backups enabled
- ✅ IAM roles least privilege
- ✅ Security groups minimal access
- ✅ MFA for console access
- ✅ VPC private subnets for database

### Cost Optimization

- **Use S3 lifecycle** for old logs (delete after 90 days)
- **Enable CloudFront** for caching (reduce bandwidth)
- **Use RDS Read Replicas** for reporting
- **Auto Scaling** for variable traffic
- **Reserved Instances** for predictable workloads (-30% savings)
- **Spot Instances** for non-critical tasks (-70% savings)

## Common Issues & Solutions

### Website Slow
1. Enable CloudFront caching
2. Optimize images (use compression)
3. Use CloudFront edge locations
4. Check database query performance

### Database Connection Errors
1. Check security group allows traffic
2. Verify database is running
3. Check credentials correct
4. Verify Lambda/EC2 in correct VPC

### High Bills
1. Check CloudFront data transfer costs
2. Review RDS instance type (may be oversized)
3. Check Lambda invocation count spikes
4. Review S3 data transfer (use CloudFront)

## Scaling as You Grow

**Phase 1: Prototype ($0-5/month)**
- Static S3 + CloudFront website
- Serverless Lambda + DynamoDB API

**Phase 2: Growing ($20-50/month)**
- Single t3.small EC2 + RDS micro
- CloudFront + Route 53 DNS

**Phase 3: Production ($50-200/month)**
- Multi-AZ EC2 Auto Scaling group
- RDS with read replicas
- ElastiCache for caching

**Phase 4: Enterprise ($200+/month)**
- Multi-region deployment
- Advanced caching strategies
- DynamoDB DAX for latency
- Enhanced monitoring and alerting

## 📖 Related Resources

- [S3 Documentation](../tier-1-foundational/s3/README.md)
- [EC2 Documentation](../tier-1-foundational/ec2/README.md)
- [Lambda Documentation](../tier-1-foundational/lambda/README.md)
- [RDS Documentation](../tier-1-foundational/rds/README.md)
- [CloudFront Documentation](../tier-2-common/cloudfront/README.md)
- [Route 53 Documentation](../tier-2-common/route-53/README.md)
- [Best Practices](../best-practices/README.md)
- [Troubleshooting](../troubleshooting/README.md) service