#!/usr/bin/env python3
"""
Generate comprehensive README files for all Tier-1 services
This script creates professional documentation structure
"""

import os
from pathlib import Path

# All README content for Tier-1 services
README_CONTENT = {
    'tier-1-foundational/vpc/README.md': """# VPC - Virtual Private Cloud

Your private network in AWS. Isolate resources, control traffic flow, build secure architectures.

## 📚 Learning Path

1. **[What is VPC?](what-is-vpc.md)** - Networking fundamentals and core concepts
2. **[Subnets](subnets.md)** - Breaking up your network into segments
3. **[Security Groups](security-groups.md)** - Instance-level firewall rules
4. **[NACLs](nacls.md)** - Network-level access control lists

## 🎯 Quick Summary

VPC is your isolated network in AWS. Every resource (EC2, RDS, Lambda) runs inside a VPC.

| Aspect | Details |
|--------|---------|
| **Cost** | FREE (pay for NAT gateways, VPN) |
| **Scalability** | Up to 16,384 IP addresses per VPC |
| **Isolation** | Complete isolation from other accounts |
| **Control** | Full network control |

## 🏗️ Architecture Layers

```
VPC (IP range: 10.0.0.0/16)
├─ Subnets (Public, Private)
│  ├─ Public: 10.0.1.0/24 (route to internet)
│  └─ Private: 10.0.2.0/24 (no internet)
├─ Route Tables (traffic rules)
├─ Security Groups (instance-level firewall)
├─ NACLs (subnet-level firewall)
└─ Internet Gateway (bridge to internet)
```

## 📊 Public vs Private Subnets

| Feature | Public | Private |
|---------|--------|---------|
| Internet Access | Yes | No (or via NAT) |
| Public IPs | Yes | No |
| Use For | Web servers, load balancers | Databases, app servers |
| Security | Lower (exposed) | Higher (hidden) |
| Data Cost | $0.09/GB out | None (internal) |

## 💡 Typical 3-Tier Architecture

```
┌──────────────────────────────────────────┐
│ VPC: 10.0.0.0/16                         │
├────────────────────────────────────────┤
│ Tier 1: Public (Web Layer)              │
│  EC2 Web Servers (10.0.1.0/24)          │
│  └─ Load Balancer                       │
│                                         │
│ Tier 2: Private (App Layer)             │
│  EC2 App Servers (10.0.2.0/24)          │
│  └─ Only accessible from Tier 1        │
│                                         │
│ Tier 3: Private (Database Layer)        │
│  RDS Database (10.0.3.0/24)             │
│  └─ Only accessible from Tier 2        │
│                                         │
│ Internet Gateway (IGW)                  │
│  └─ Allows public tier to reach internet│
└──────────────────────────────────────────┘
```

## 🔐 Network Security Layers

**Layer 1: VPC Level**
- IP address ranges
- Isolated from other accounts

**Layer 2: Subnet Level**
- Public (internet route) vs Private (no internet)
- Network ACLs (optional, stateless)

**Layer 3: Instance Level**
- Security Groups (stateful firewall)
- Who can connect on what ports

## 🚀 Common Scenarios

### Scenario 1: Simple Website
- Single public subnet
- Web servers in public subnet
- Traffic from internet to port 80/443
- No database (or external DB)

### Scenario 2: Web App with Database
- 2 subnets (public, private)
- Web servers in public (port 80/443)
- Database in private (port 3306)
- Web servers can access database
- Internet can't access database

### Scenario 3: High Availability
- Multiple AZs (at least 2)
- Subnets in each AZ
- Auto Scaling Group across AZs
- RDS Multi-AZ across AZs
- Load Balancer distributes traffic

## 💰 VPC Pricing

VPC itself: **FREE**

Pay for:
- **NAT Gateway**: $0.045/hour + $0.045/GB (private subnet internet access)
- **VPN Gateway**: $0.05/hour (connect on-premises to AWS)
- **Elastic IP**: $0.005/hour when not attached (static IP)

## ⚠️ Common Mistakes

1. **Making everything public** - Databases in public subnet (security risk)
2. **Single subnet** - No high availability across zones
3. **No firewall rules** - Forgetting security group rules
4. **Overcomplicated** - Start simple, scale up as needed

## ✅ Best Practices

- Use multiple subnets across 2+ AZs
- Keep databases in private subnets
- Use security groups (not NACLs unless needed)
- Document your CIDR ranges
- Use VPC Flow Logs for debugging
- Implement least-privilege access

---
**Start with**: [What is VPC?](what-is-vpc.md)""",

    'tier-1-foundational/s3/README.md': """# S3 - Simple Storage Service

AWS's primary cloud storage. Store unlimited files with 11 nines of durability.

## 📚 Learning Path

1. **[What is S3?](what-is-s3.md)** - Overview and core concepts
2. **[Buckets & Objects](buckets-and-objects.md)** - Core storage units
3. **[Storage Classes](storage-classes.md)** - Optimize by access pattern
4. **[Versioning](versioning.md)** - Keep file history
5. **[Lifecycle Rules](lifecycle-rules.md)** - Auto-archive old files
6. **[Access Control](access-control.md)** - Who can access what
7. **[Pricing](pricing.md)** - Cost calculator
8. **[Use Cases](use-cases.md)** - Real-world applications

## 🎯 Quick Summary

S3 is object storage - store any file (documents, images, videos, databases, backups) in buckets and access from anywhere.

| Aspect | Details |
|--------|---------|
| **Durability** | 99.999999999% (11 nines!) |
| **Availability** | 99.99% |
| **Scalability** | Unlimited storage |
| **Cost** | $0.023/GB/month (first 50 TB) |
| **Access** | Web API, CLI, SDKs |

## 📦 Core Concepts

### Bucket
- Container for objects (like top-level folder)
- Bucket names globally unique (like domain names)
- Example: "my-company-photos-2024"
- Can have 100 per account (can increase)

### Object
- Any file stored in S3
- Size: 0 bytes to 5 TB
- Types: Documents, images, videos, code, backups, databases
- Example: "documents/2024/invoice.pdf"

### Prefix
- Folder-like path (S3 doesn't have real folders)
- Example: "documents/2024/" is the prefix
- Used for organization and permissions

## 💡 Real-World Use Cases

### 1. Website Hosting ($5-20/month)
```
Static website (HTML/CSS/JS)
Store in S3 bucket
Enable public read
CloudFront for global caching
Cost: S3 storage + CloudFront bandwidth
```

### 2. Backup Service (Storage + Lifecycle)
```
Backup database daily
Store in S3
Versioning enabled (keep old versions)
Lifecycle: Move old to Glacier after 90 days
Cost: Decreases over time as files archive
```

### 3. Data Lake (Analytics)
```
Store billions of files
Query with Athena (SQL)
Analyze with QuickSight
Cost scales with data size
```

### 4. Mobile App Backend
```
Users upload photos
Mobile app reads via signed URLs
DynamoDB for metadata
S3 for actual files
```

## 🔐 Security & Compliance

**Default**: Private (only you access)

**Access Control**:
- IAM policies (who in your account)
- Bucket policies (allow external access)
- ACLs (public/private, legacy)
- Pre-signed URLs (temporary access)

**Encryption**:
- At-rest: AES-256 (automatic)
- In-transit: HTTPS/SSL
- Customer-managed keys: Optional

**Versioning**:
- Keep multiple versions
- Recover deleted files
- Audit trail of changes

## 📊 Storage Classes (Speed vs Cost)

| Class | Cost/GB | Speed | Use Case |
|-------|---------|-------|----------|
| Standard | $0.023 | Instant | Frequently accessed |
| Intelligent-Tiering | $0.0125 | Instant | Unknown patterns |
| Standard-IA | $0.0125 | Instant | Monthly access |
| Glacier | $0.004 | 3-5 min | Archival, <1x/month |
| Deep Archive | $0.001 | 12 hrs | Long-term backups |

**Tip**: Use lifecycle rules to auto-move old files to cheaper tiers!

## 💰 Pricing Quick Reference

```
Storage:
- First 50 TB: $0.023/GB/month
- Next 450 TB: $0.022/GB/month
- Over 500 TB: $0.021/GB/month

Requests:
- PUT: $0.0004 per 1000
- GET: $0.00008 per 1000

Data Transfer:
- OUT to Internet: $0.09/GB
- OUT to CloudFront: $0.085/GB  
- OUT to Same Region: FREE
```

## 🚀 Common Operations

### Create Bucket
```
1. S3 Console
2. "Create Bucket"
3. Unique name (e.g., my-app-data-2024)
4. Choose region (closest to you)
5. Block public access (recommended)
```

### Upload File
```
1. Click bucket
2. "Upload" or drag-and-drop
3. Set permissions (private recommended)
4. "Upload"
```

### Make Website Public
```
1. Bucket > Permissions
2. "Unblock public access"
3. Add bucket policy to allow public read
4. Static website hosting: enable
```

## ⚠️ Common Mistakes

1. **Bucket fully public** - Exposes sensitive data (private by default!)
2. **No versioning** - Delete file = lost forever (enable versioning!)
3. **No lifecycle** - Old files consume space forever (create lifecycle rules!)
4. **No MFA delete** - Can be deleted accidentally (MFA delete for production!)
5. **Wrong region** - High latency/cost (choose close to users!)

## ✅ Best Practices

- Keep buckets private (default)
- Enable versioning for critical data
- Use lifecycle rules to archive old data
- Enable MFA delete for production buckets
- Use CloudFront for global distribution
- Enable S3 Block Public Access
- Monitor costs with S3 analytics

---
**Start with**: [What is S3?](what-is-s3.md)""",

    'tier-1-foundational/lambda/README.md': """# Lambda - Serverless Computing

Run code without servers. Pay only for execution time.

## 📚 Learning Path

1. **[What is Lambda?](what-is-lambda.md)** - Serverless concepts
2. **[Triggers](triggers.md)** - What causes Lambda to run
3. **[Layers](layers.md)** - Sharing code and libraries
4. **[Pricing](pricing.md)** - Cost calculator and optimization
5. **[Use Cases](use-cases.md)** - Real-world applications
6. **[Create Function](first-lambda-function.md)** - Hands-on guide

## 🎯 Quick Summary

Lambda = "Functions as a Service". Write code, upload, trigger, pay for runtime.

| Aspect | Details |
|--------|---------|
| **Cost** | $0.20 per 1M requests + $0.0000166667/GB-second |
| **Free Tier** | 1M requests + 400,000 GB-seconds per month |
| **Languages** | Python, Node.js, Java, Go, C#, Ruby, Custom |
| **Scaling** | Automatic (1 to 1000s concurrent) |
| **Cold Start** | ~100ms first invocation |

## ⚡ Why Serverless?

### Traditional Server (EC2)
```
Cost: $100+/month (always running)
Scaling: Manual or Auto Scaling Group (complex)
Maintenance: Patches, OS updates, monitoring
```

### Lambda
```
Cost: $1-5/month for typical app (pay per execution)
Scaling: Automatic
Maintenance: None - AWS handles it
```

## 🔧 Supported Languages

| Language | Best For | Runtime |
|----------|----------|---------|
| Python | Quick development | 3.9, 3.10, 3.11 |
| Node.js | Web APIs | 14, 16, 18 |
| Java | Enterprise | 11, 17 |
| Go | Performance | Custom |
| C# | .NET | net6.0, net7.0 |
| Ruby | Scripting | 2.7, 3.2 |

## 💡 How Lambda Works

```
1. Write function (my_function.py)
2. Upload to Lambda
3. Set trigger (API, S3, schedule, etc.)
4. User triggers event
5. Lambda executes function
6. Returns response
7. Pay for execution time
```

## 🎯 Common Triggers

| Trigger | Example | Use Case |
|---------|---------|----------|
| **API Gateway** | HTTP request | REST API |
| **S3** | File upload | Image processing |
| **DynamoDB** | Database change | Stream processing |
| **SNS** | Notification | Email triggers |
| **SQS** | Message queue | Async processing |
| **CloudWatch** | Schedule (cron) | Nightly tasks |
| **EventBridge** | Any event | Complex workflows |

## 📋 Lambda Configuration

### Memory & CPU
- 128 MB - 10,240 MB
- CPU scales proportionally with memory
- Higher memory = faster execution

### Timeout
- Default: 3 seconds
- Maximum: 900 seconds (15 minutes)
- Long jobs → Use EC2/ECS instead

### Environment
- Runtime: Language version
- Layers: Shared dependencies
- VPC: Network access (if needed)

## 💰 Pricing Example

### Scenario: API with 1M requests/month

```
Each request:
- 100ms duration
- 256 MB memory
- Per month:
  - Requests: 1M × $0.20/1M = $0.20
  - Duration: 1M × 0.1s × 0.256 GB = 25,600 GB-seconds
  - Cost: 25,600 × $0.0000166667 = $0.43
  
Total: ~$0.63/month

vs EC2 m5.large: $70/month (always running)

Savings: 99% cheaper with Lambda!
```

## 🔐 Limitations to Know

| Limit | Value | Workaround |
|-------|-------|-----------|
| Execution time | 15 minutes max | Use EC2/ECS |
| Disk space | 512 MB (/tmp) | Use S3/DynamoDB |
| Memory | Max 10 GB | Use EC2 |
| Package size | 250 MB | Use layers |
| Concurrency | 1000 by default | Request increase |

## 🚀 Common Use Cases

### 1. REST API
```
API Gateway → Lambda → DynamoDB
Client requests → HTTP → Lambda executes → Returns JSON
Perfect for: Microservices, mobile backends
```

### 2. File Processing
```
S3 upload → Lambda triggers → Process file → Save result
Perfect for: Image resizing, video transcoding
```

### 3. Scheduled Tasks
```
CloudWatch Events (cron) → Lambda
Perfect for: Backups, reports, cleanup jobs
```

### 4. Real-time Stream Processing
```
Kinesis → Lambda → Store results
Perfect for: Analytics, aggregation, filtering
```

## ❌ When NOT to Use Lambda

- Long-running jobs (>15 min) → Use EC2/ECS
- Constant load (>10 GB/s) → Use EC2
- Complex dependencies → Use container (ECS)
- Legacy applications → Use EC2

## ✅ Best Practices

- Keep functions small and focused
- Use environment variables (not hardcoding)
- Handle cold starts in critical paths
- Use layers for shared code
- Monitor with CloudWatch
- Set appropriate timeouts
- Use IAM roles (not access keys)

---
**Start with**: [What is Lambda?](what-is-lambda.md)""",

    'tier-1-foundational/rds/README.md': """# RDS - Relational Database Service

Managed SQL databases. AWS handles backups, patches, scaling.

## 📚 Learning Path

1. **[What is RDS?](what-is-rds.md)** - Overview and benefits
2. **[Database Engines](database-engines.md)** - Choosing MySQL vs PostgreSQL
3. **[Pricing](pricing.md)** - Cost estimation
4. **[Use Cases](use-cases.md)** - Real-world applications
5. **[Create Database](creating-first-database.md)** - Hands-on guide

## 🎯 Quick Summary

RDS = Database with no management overhead. AWS handles backups, patches, replication, scaling.

| Aspect | Details |
|--------|---------|
| **Engines** | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora |
| **Cost** | $12-200+/month depending on size |
| **Backups** | Automatic, 35-day retention |
| **High Availability** | Multi-AZ with automatic failover |
| **Scaling** | Vertical (bigger instance) or read replicas |

## 🔄 Management Comparison

### Traditional Database (EC2)

**You Do**:
- Install database software
- Apply security patches
- Create backups
- Monitor performance
- Handle failover
- Manage storage

**Time**: 40% of your effort

### RDS

**AWS Does**:
- Installation ✓
- Patches ✓
- Backups ✓
- Monitoring ✓
- Failover ✓
- Storage ✓

**You Do**: Just use the database

## 📊 Supported Engines

| Engine | Best For | Cost | Complexity |
|--------|----------|------|-----------|
| MySQL | General web apps | Cheapest | Low |
| PostgreSQL | Advanced SQL, JSON | Medium | Medium |
| MariaDB | MySQL drop-in | Cheapest | Low |
| Aurora | Speed + scale | Premium | Medium |
| Oracle | Enterprise | Expensive | High |
| SQL Server | Windows/.NET | Expensive | High |

## 🏗️ Deployment Options

### Single-AZ (Cheap)
```
Single EC2 instance
Pros:
- Cheapest
- Sufficient for dev/test

Cons:
- No redundancy
- Downtime if instance fails
- No automatic failover
```

### Multi-AZ (Recommended for Production)
```
Primary instance + Standby replica
Pros:
- 99.95% SLA
- Automatic failover
- No data loss
- Synchronous replication

Cons:
- ~50% more expensive
```

### Read Replicas (Scale Reads)
```
Primary instance + read-only replicas
Pros:
- Scale read queries
- Different regions
- Can promote to primary

Cons:
- Eventual consistency
- Extra cost
```

## 💡 Architecture Example

```
Web Application Servers
├─ Primary RDS Instance (us-east-1a)
│  └─ Write queries here
├─ Standby Replica (us-east-1b)
│  └─ Automatic failover if primary down
└─ Read Replicas (multiple regions)
   └─ Distribute read queries
```

## 💰 Pricing Example

### db.t3.micro (Small Database)

**On-Demand**:
```
Instance: $0.017/hour × 730 hours = $12.41/month
Storage (20 GB): $20 × $0.115 = $2.30/month
Backup (20 GB): $20 × $0.095 = $1.90/month
Total: ~$17/month
```

**Multi-AZ** (add 50%):
```
Total: ~$25/month
```

**Reserved Instance** (save 45%):
```
1-year upfront: $72
Monthly: $6/month
Total year 1: $78
```

## 🔐 Security Features

- **Encryption at-rest**: AES-256 (all engines)
- **Encryption in-transit**: SSL/TLS (automatically)
- **Network isolation**: Runs in VPC (private by default)
- **IAM authentication**: Alternative to passwords
- **Automated patching**: Security updates
- **Audit logging**: CloudTrail integration

## 🚀 Common Scenarios

### Scenario 1: Small Website (WordPress, etc.)
```
db.t3.micro (2 vCPU, 1 GB RAM)
Single-AZ
20 GB storage
Cost: ~$17/month
```

### Scenario 2: Production Web App
```
db.m5.large (2 vCPU, 8 GB RAM)
Multi-AZ (high availability)
100 GB storage + read replicas
Cost: ~$300/month
```

### Scenario 3: Analytics Database
```
db.r5.xlarge (4 vCPU, 32 GB RAM)
Multi-AZ for reliability
1 TB storage
Read replicas for distributed queries
Cost: ~$800/month
```

## ⚠️ Common Mistakes

1. **Single-AZ production** - One failure = downtime
2. **Too small instance** - Slow queries, max connections reached
3. **No backups configured** - Data loss if disaster
4. **Outdated patches** - Security vulnerabilities
5. **No monitoring** - Performance issues unnoticed

## ✅ Best Practices

- Use Multi-AZ for production
- Enable automated backups (35 days)
- Use read replicas for scale
- Monitor with CloudWatch
- Apply patches in maintenance window
- Use IAM authentication
- Enable encryption at-rest
- Regular restore tests

## 🔗 Comparison: RDS vs Aurora

| Feature | RDS | Aurora |
|---------|-----|--------|
| Speed | Standard | 5-15x faster |
| Cost | Standard | +25-50% |
| Scaling | Manual | Auto-scaling |
| Replication | 6-way | 6-way |
| Backups | 35 days | Automatic |

---
**Start with**: [What is RDS?](what-is-rds.md)""",

    'tier-1-foundational/cloudformation/README.md': """# CloudFormation - Infrastructure as Code

Define AWS infrastructure in code. Repeatable, versionable, automated.

## 📚 Learning Path

1. **[What is CloudFormation?](what-is-cloudformation.md)** - Overview
2. **Template Basics** - YAML/JSON structure
3. **Resources** - Creating AWS services
4. **Parameters** - Input variables
5. **Outputs** - Return values
6. **AWS SAM** - Serverless applications
7. **Best Practices** - Patterns and anti-patterns

## 🎯 Quick Summary

CloudFormation = Infrastructure as Code. Write YAML → Create entire AWS infrastructure automatically.

| Aspect | Details |
|--------|---------|
| **Format** | YAML or JSON |
| **Units** | Templates (code) → Stacks (resources) |
| **Cost** | FREE (pay for created resources) |
| **Purpose** | Repeatable infrastructure |
| **Benefit** | Version control, disaster recovery, consistency |

## 🚀 Why CloudFormation?

### Manual (AWS Console)
```
1. Click VPC
2. Create subnet
3. Create security group
4. Launch EC2
5. Configure RDS
6. Create load balancer
...

Problems:
- Forget what you did
- Can't reproduce easily
- Disaster recovery is hard
- Takes 30 minutes per environment
```

### CloudFormation
```
1. Write template (YAML)
2. Create stack
3. Everything deployed automatically
4. Can recreate in 2 minutes
5. Stored in Git with history

Benefits:
- Repeatable
- Versionable
- Fast
- Disaster recovery easy
```

## 📋 Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: My application infrastructure

Parameters:
  InstanceType:
    Type: String
    Default: t3.micro
    Description: EC2 instance type

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-app-bucket
  
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType
      ImageId: ami-12345678

Outputs:
  BucketName:
    Value: !Ref MyBucket
    Description: Name of S3 bucket
```

## 🔄 Stack Lifecycle

```
1. CREATE
   └─ CloudFormation creates all resources

2. UPDATE  
   └─ Modify template
   └─ CloudFormation updates stack
   └─ Only changes applied (smart!)

3. ROLLBACK
   └─ If error during create/update
   └─ Automatically reverts

4. DELETE
   └─ Delete stack = delete all resources
   └─ Except S3 buckets (have data)
```

## 💡 Real-World Example

### Template: Simple Web App

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple web app with S3 + Lambda

Parameters:
  BucketName:
    Type: String
    Description: S3 bucket name

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName
  
  MyLambdaRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AWSLambdaFullAccess

  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Runtime: python3.9
      Role: !GetAtt MyLambdaRole.Arn
      Code:
        ZipFile: |
          def handler(event, context):
              return {'statusCode': 200, 'body': 'Hello'}

Outputs:
  BucketName:
    Value: !Ref MyBucket
  FunctionArn:
    Value: !GetAtt MyFunction.Arn
```

## 🛠️ Common Resources

| Service | Resource Type | Example |
|---------|---------------|---------|
| EC2 | AWS::EC2::Instance | Virtual server |
| S3 | AWS::S3::Bucket | Storage bucket |
| RDS | AWS::RDS::DBInstance | Database |
| Lambda | AWS::Lambda::Function | Function |
| VPC | AWS::EC2::VPC | Network |
| IAM | AWS::IAM::Role | Access control |
| DynamoDB | AWS::DynamoDB::Table | NoSQL DB |

## 📚 CloudFormation Functions

| Function | Purpose | Example |
|----------|---------|---------|
| !Ref | Reference resource | !Ref MyBucket |
| !GetAtt | Get attribute | !GetAtt MyInstance.PublicIp |
| !Sub | Substitute variables | !Sub "arn:aws:s3:::${BucketName}" |
| !Join | Join strings | !Join ['-', [prod, web, bucket]] |
| !If | Conditional | !If [IsProd, true, false] |

## 🎯 Best Practices

### DO:
- Use parameters for variables
- Use meaningful resource names
- Add descriptions to all parameters
- Version control your templates
- Create outputs for important values
- Use IAM roles, not access keys
- Enable termination protection

### DON'T:
- Hardcode values
- Put credentials in templates
- Create one huge template
- Forget to document parameters
- Manually modify created resources
- Ignore error messages

## 🔀 AWS SAM (Serverless Application Model)

Simplified syntax for serverless apps:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: python3.9
      Events:
        MyApi:
          Type: Api
          Properties:
            Path: /
            Method: GET

  MyTable:
    Type: AWS::Serverless::SimpleTable
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
```

## 🔗 CloudFormation vs Terraform

| Feature | CloudFormation | Terraform |
|---------|----------------|-----------|
| AWS only | Yes | No (multi-cloud) |
| Learning curve | Medium | Medium |
| Free/Cost | Free | Free (Cloud extra) |
| Syntax | YAML/JSON | HCL |
| State file | AWS (native) | Local/Cloud |

For AWS only → Use CloudFormation
For multi-cloud → Use Terraform

---
**Start with**: [What is CloudFormation?](what-is-cloudformation.md)"""
}

# Write all README files
total = len(README_CONTENT)
count = 0

for path, content in README_CONTENT.items():
    p = Path(path)
    p.write_text(content, encoding='utf-8')
    count += 1
    print(f"✅ [{count}/{total}] {path}")

print(f"\n🎉 Successfully populated {count} README files!")
