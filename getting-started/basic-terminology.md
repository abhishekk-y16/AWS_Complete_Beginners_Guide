# Basic AWS Terminology 📚

Essential terms every AWS beginner should know.

## Core Concepts

### Region
```
Physical location with data centers

Examples:
- us-east-1 (N. Virginia)
- us-west-2 (Oregon)
- eu-west-1 (Ireland)
- ap-southeast-1 (Singapore)

🌍 AWS has 33 regions worldwide

Why it matters:
- Latency (choose close to users)
- Compliance (data residency)
- Pricing (varies by region)
- Service availability
```

### Availability Zone (AZ)
```
Data center within a region

Example:
- us-east-1a
- us-east-1b
- us-east-1c

Each region has 2-6 AZs

Why it matters:
- High availability
- Fault tolerance
- Run in multiple AZs for redundancy
```

### Account
```
Your AWS account
- Unique 12-digit ID: 123456789012
- Root user (don't use daily!)
- IAM users (use these!)
- Billing is per account
```

### Resource
```
Anything you create in AWS

Examples:
- EC2 instance
- S3 bucket
- RDS database
- Lambda function

Each resource has unique ID/ARN
```

### ARN (Amazon Resource Name)
```
Unique identifier for resources

Format:
arn:aws:service:region:account-id:resource-type/resource-name

Example:
arn:aws:s3:::my-bucket
arn:aws:ec2:us-east-1:123456789:instance/i-1234567890

Use for:
- IAM policies
- Cross-service access
- Uniquely identifying resources
```

## Compute Terms

### Instance
```
Virtual server (EC2)

Like: Renting a computer

Types:
- t3.micro (1 vCPU, 1GB RAM)
- t3.small (2 vCPU, 2GB RAM)
- m5.large (2 vCPU, 8GB RAM)

You choose:
- Instance type
- Operating system
- Storage size
```

### AMI (Amazon Machine Image)
```
Template for launching instances

Like: Operating system installer

Popular AMIs:
- Amazon Linux 2
- Ubuntu 22.04
- Windows Server 2022
- Custom AMIs (your own)

Contains:
- Operating system
- Pre-installed software
- Configuration
```

### Auto Scaling
```
Automatically adjust resources

Example:
- Normal: 2 instances
- Peak traffic: Scale to 10 instances
- Low traffic: Scale to 1 instance

Benefits:
- Handle traffic spikes
- Save money
- Always available
```

### Elastic IP
```
Static public IP address

Like: Your permanent phone number

Features:
- Doesn't change when instance stops
- Can move between instances
- Costs $0 when attached
- Costs $3.60/month when not attached

Use for:
- Production servers
- Consistent access
```

## Storage Terms

### EBS (Elastic Block Store)
```
Hard drive for EC2 instances

Like: External hard drive

Types:
- gp3 (General Purpose SSD)
- io2 (High Performance)
- st1 (Throughput Optimized)

Features:
- Attach to EC2 instances
- Persist after instance stops
- Can snapshot for backups

Cost: $0.08-0.10/GB/month
```

### Snapshot
```
Backup of EBS volume

Like: Photo of your hard drive

Use for:
- Backups
- Copy to other regions
- Create new volumes

Cost: $0.05/GB/month
Incremental (only changed data)
```

### Object
```
File in S3

Can be:
- Photo (image.jpg)
- Video (movie.mp4)
- Document (report.pdf)
- Any file type

Each object:
- Has unique key (filename + path)
- Stored in bucket
- Has metadata
```

### Bucket
```
Container for S3 objects

Like: Folder in cloud storage

Rules:
- Name must be globally unique
- Can store unlimited objects
- Created in specific region
- Can be public or private

Example names:
- my-company-backups
- website-images-2024
```

## Database Terms

### RDS Instance
```
Managed database server

Supports:
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- SQL Server

AWS handles:
- Backups
- Patches
- Updates
- Scaling

You handle:
- Database design
- Queries
- Application logic
```

### Multi-AZ
```
Database in multiple availability zones

How it works:
- Primary database in AZ 1
- Standby replica in AZ 2
- Automatic failover if AZ 1 fails

Benefits:
- High availability
- Automatic failover
- No downtime for backups

Cost: 2× (runs two databases)
```

### Read Replica
```
Read-only copy of database

Use for:
- Heavy read workloads
- Reports and analytics
- Reduce load on primary

Example:
- Primary: Handle writes
- Replica 1: Handle user reads
- Replica 2: Handle reports

Cost: Same as additional instance
```

## Networking Terms

### VPC (Virtual Private Cloud)
```
Your private network in AWS

Like: Your own internet

Contains:
- Subnets
- Route tables
- Internet gateway
- Security groups

Default VPC:
- Created automatically
- Good for getting started
- Can create custom VPCs
```

### Subnet
```
Section of VPC

Types:
- Public subnet (internet access)
- Private subnet (no internet)

Example:
- Public: Web servers
- Private: Databases

Each subnet in one AZ
```

### Security Group
```
Firewall rules for resources

Like: Bouncer at a club

Rules:
- Inbound (incoming traffic)
- Outbound (outgoing traffic)

Example:
- Allow port 22 (SSH) from your IP
- Allow port 80 (HTTP) from anywhere
- Allow port 443 (HTTPS) from anywhere

Default: Deny all inbound, allow all outbound
```

### Load Balancer
```
Distributes traffic across instances

Like: Traffic cop

Types:
- ALB (Application Load Balancer)
- NLB (Network Load Balancer)
- CLB (Classic Load Balancer)

Benefits:
- High availability
- Health checks
- Auto-scaling support
- SSL termination

Cost: ~$16/month + data processed
```

## Security Terms

### IAM (Identity & Access Management)
```
Control who can access what

Components:
- Users (people)
- Groups (collection of users)
- Roles (for services)
- Policies (permissions)

Example:
- User: john@company.com
- Group: Developers
- Policy: Can launch EC2
```

### Policy
```
Permissions document (JSON)

Defines:
- What actions allowed
- On which resources
- Under what conditions

Example:
Allow john to:
- List S3 buckets
- Upload to specific bucket
- Not delete anything
```

### Role
```
Temporary permissions for services

Like: Security badge

Use for:
- EC2 accessing S3
- Lambda accessing DynamoDB
- Cross-account access

Benefits:
- No credentials in code
- Automatic credential rotation
- Secure
```

### MFA (Multi-Factor Authentication)
```
Two-step verification

Requires:
1. Password (something you know)
2. Code from phone (something you have)

Apps:
- Google Authenticator
- Microsoft Authenticator
- Authy

🚨 ALWAYS enable on root account!
```

## Monitoring Terms

### CloudWatch
```
Monitoring and logging service

Collects:
- Metrics (CPU, memory)
- Logs (application logs)
- Events (state changes)

Use for:
- Monitor performance
- Set alarms
- Debug issues
- Track costs
```

### Metric
```
Time-series data point

Examples:
- CPU Utilization: 45%
- Network In: 1000 bytes/sec
- Disk Writes: 50 IOPS

Refreshes:
- Standard: Every 5 minutes (free)
- Detailed: Every 1 minute (paid)
```

### Alarm
```
Alert when metric threshold exceeded

Example:
- If CPU > 80% for 5 minutes
- Then send email alert
- And scale up instances

Use for:
- Performance alerts
- Billing alerts
- Auto-scaling triggers
```

## Pricing Terms

### On-Demand
```
Pay per hour/second used

Like: Taxi (pay per ride)

Benefits:
- No commitment
- Stop anytime
- Pay only when running

Best for:
- Testing
- Unpredictable workloads
- Short-term use
```

### Reserved Instances
```
Commit to 1-3 years, get discount

Like: Monthly gym membership

Discount:
- 1 year: ~30% off
- 3 years: ~60% off

Best for:
- Steady workloads
- Production servers
- Long-term use
```

### Spot Instances
```
Bid on unused capacity

Like: Standby airline tickets

Discount: Up to 90% off!

Catch:
- Can be terminated anytime
- When AWS needs capacity back

Best for:
- Batch processing
- Big data
- Non-critical workloads
```

### Free Tier
```
Free services for new accounts

Duration:
- 12 months for most services
- Forever for some (Lambda, DynamoDB)

Limits:
- EC2: 750 hours/month
- S3: 5GB storage
- RDS: 750 hours/month
```

## Common Acronyms

```
AMI - Amazon Machine Image
ARN - Amazon Resource Name
AWS - Amazon Web Services
AZ - Availability Zone
CDN - Content Delivery Network
CLI - Command Line Interface
DNS - Domain Name System
EBS - Elastic Block Store
EC2 - Elastic Compute Cloud
IAM - Identity & Access Management
RDS - Relational Database Service
S3 - Simple Storage Service
SDK - Software Development Kit
VPC - Virtual Private Cloud
```

## 📖 Next Steps

1. [Cost Management Basics](cost-management-basics.md)
2. [Core Concepts](../core-concepts/README.md)
3. [Launch First Instance](../tutorials/deploy-web-server.md)

## Related Resources

- [What is AWS?](what-is-aws.md)
- [AWS Glossary (Detailed)](../glossary/README.md)
- [IAM Basics](../core-concepts/iam-basics.md)