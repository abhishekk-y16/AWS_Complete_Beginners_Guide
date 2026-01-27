"""
AWS Documentation Auto-Population Script
Populates all placeholder markdown files with comprehensive, service-specific content
"""

import os
from pathlib import Path

# Define comprehensive content for each file
CONTENT_MAP = {
    # ====================
    # TIER-1: EC2 FILES
    # ====================
    "tier-1-foundational/ec2/what-is-ec2.md": """# What is Amazon EC2?

**Amazon Elastic Compute Cloud (EC2)** is AWS's virtual server service. Think of it as renting computers in the cloud - you get full control over the operating system, can install any software, and only pay for what you use.

## 🎯 Core Concept

EC2 provides **resizable compute capacity** in the cloud. Instead of buying physical servers:
- Launch virtual servers (instances) in minutes
- Scale up or down based on demand
- Pay only for running instances (per-second billing)
- Choose from 500+ instance types

## 🖥️ What is an EC2 Instance?

An instance is a virtual computer with:
- **vCPUs**: Virtual processors (1-448 vCPUs available)
- **Memory**: RAM (0.5 GB - 24 TB)
- **Storage**: EBS volumes or instance store
- **Network**: Elastic IPs, security groups, placement groups
- **Operating System**: Amazon Linux, Ubuntu, Windows Server, etc.

## 💡 Real-World Analogy

**EC2** = Renting an apartment vs buying a house
- Choose size (t2.micro or m5.24xlarge)
- Pay rent only when you use it
- Move in immediately (launch in 60 seconds)
- Customize interior (install any software)
- Move out anytime (terminate instance)

## 📋 Common Use Cases

### 1. **Web Application Hosting**
```
Scenario: Run a WordPress website
Instance: t3.small (2 vCPUs, 2 GB RAM)
Cost: ~$15/month (24/7 running)
```

### 2. **Batch Processing**
```
Scenario: Process video files overnight
Instance: c5.4xlarge (16 vCPUs, 32 GB RAM)
Cost: $0.68/hour (only running 8 hours = $5.44)
```

### 3. **Development/Test Environments**
```
Scenario: Developers need test servers
Instance: t3.medium (2 vCPUs, 4 GB RAM)
Cost: Start/stop as needed, pay only when running
```

### 4. **Machine Learning Training**
```
Scenario: Train ML models
Instance: p3.2xlarge (8 vCPUs, 61 GB RAM, 1 GPU)
Cost: $3.06/hour (use Spot Instances for 70% savings)
```

## 🔑 Key Features

### 1. **Instance Types**
- **General Purpose** (T3, M5): Balanced CPU/memory
- **Compute Optimized** (C5, C6i): High-performance processors
- **Memory Optimized** (R5, X2): Large memory for databases
- **Storage Optimized** (I3, D2): High disk throughput
- **GPU Instances** (P3, G4): ML training, graphics rendering

### 2. **Elastic IP Addresses**
- Static public IP that doesn't change
- Reassign to different instances
- Free when attached to running instance
- $0.005/hour when not attached (to discourage hoarding)

### 3. **Auto Scaling**
- Automatically add/remove instances based on demand
- Example: Scale from 2 to 10 instances during traffic spike
- Reduce to 2 instances during off-peak hours

### 4. **Load Balancing**
- Distribute traffic across multiple instances
- Types: Application Load Balancer (HTTP/HTTPS), Network Load Balancer (TCP/UDP)
- Health checks: Remove unhealthy instances automatically

### 5. **Security Groups**
- Virtual firewall for instances
- Control inbound/outbound traffic
- Example: Allow HTTP (port 80) and SSH (port 22) only

## 💰 Pricing Models

### 1. **On-Demand** (Most Flexible)
```
Pay per second (minimum 60 seconds)
No commitment, cancel anytime
Best for: Short-term, unpredictable workloads

Example: t3.micro
- $0.0104/hour
- $7.49/month (24/7)
```

### 2. **Reserved Instances** (Up to 72% savings)
```
Commit to 1 or 3 years
Pay upfront for discounts
Best for: Steady-state applications

Example: t3.micro (1 year, all upfront)
- Standard price: $89.86/year
- Reserved price: $56/year (38% savings)
```

### 3. **Spot Instances** (Up to 90% savings)
```
Bid on unused EC2 capacity
Can be terminated with 2-minute warning
Best for: Batch jobs, fault-tolerant workloads

Example: t3.micro
- On-Demand: $0.0104/hour
- Spot: ~$0.0031/hour (70% savings)
```

### 4. **Savings Plans** (Up to 72% savings)
```
Commit to $/hour for 1 or 3 years
Flexible across instance types, regions
Best for: Consistent compute usage

Example: $10/hour commitment
- Gets you ~$35/hour of compute (3.5x value)
```

## 🚀 Getting Started

### Step 1: Launch Your First Instance

**Via AWS Console:**
```bash
1. EC2 Dashboard → Launch Instance
2. Choose AMI: Amazon Linux 2
3. Choose Type: t2.micro (Free Tier eligible)
4. Configure:
   - VPC: Default
   - Auto-assign Public IP: Yes
5. Add Storage: 8 GB (default)
6. Add Tags: Name=MyFirstInstance
7. Security Group: Allow SSH (port 22) from your IP
8. Create/Select Key Pair (for SSH access)
9. Launch!
```

### Step 2: Connect to Instance

**Linux/Mac:**
```bash
chmod 400 my-key.pem
ssh -i my-key.pem ec2-user@<public-ip>
```

**Windows:**
```bash
Use PuTTY or PowerShell:
ssh -i my-key.pem ec2-user@<public-ip>
```

### Step 3: Install Software

```bash
# Update packages
sudo yum update -y

# Install web server
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd

# Create simple webpage
echo "<h1>Hello from EC2!</h1>" | sudo tee /var/www/html/index.html

# Visit http://<public-ip> in browser
```

## 🔐 Security Best Practices

### ✅ DO
- **Use key pairs**: Never set password authentication
- **Restrict security groups**: Allow only necessary ports from specific IPs
- **Use IAM roles**: Attach roles to EC2 for AWS API access (no hardcoded keys)
- **Enable termination protection**: Prevent accidental deletion
- **Encrypt EBS volumes**: Enable encryption by default
- **Update regularly**: Apply OS and software patches

### ❌ DON'T
- **Expose port 22 to 0.0.0.0/0**: Restrict SSH to your IP only
- **Hardcode AWS credentials**: Use IAM roles instead
- **Use root account**: Create IAM users
- **Forget to stop instances**: Stop when not needed to save money
- **Skip backups**: Create AMIs or EBS snapshots regularly

## ⚠️ Common Mistakes

### 1. **Leaving Instances Running**
```
Problem: Forgot to stop development instance
Cost: t3.medium 24/7 = $30/month wasted
Fix: Set CloudWatch alarm or use Auto Stop/Start scripts
```

### 2. **Wrong Instance Type**
```
Problem: Using t3.micro for production database
Symptom: Slow performance, CPU credits exhausted
Fix: Use memory-optimized (R5) for databases
```

### 3. **No Elastic IP**
```
Problem: Public IP changes when instance stops/starts
Impact: DNS records break, SSH connections fail
Fix: Allocate and attach Elastic IP
```

### 4. **Ignoring Security Group Rules**
```
Problem: Security group allows 0.0.0.0/0 on all ports
Risk: Instance vulnerable to attacks
Fix: Restrict to specific IPs and ports only
```

## 📊 Monitoring and Management

### CloudWatch Metrics (Free)
- **CPU Utilization**: Track CPU usage percentage
- **Network In/Out**: Monitor bandwidth
- **Disk Read/Write**: Track disk operations
- **Status Checks**: System and instance reachability

### CloudWatch Alarms
```
Example: Alert if CPU > 80% for 5 minutes
Action: Send SNS notification or trigger Auto Scaling
```

### Systems Manager
- **Session Manager**: Connect without SSH keys
- **Patch Manager**: Automate OS patching
- **Run Command**: Execute commands on multiple instances

## 🔗 Related Services

- **EBS (Elastic Block Store)**: Persistent storage volumes
- **ELB (Elastic Load Balancing)**: Distribute traffic
- **Auto Scaling**: Automatically adjust capacity
- **AMI (Amazon Machine Images)**: Pre-configured templates
- **Elastic IP**: Static public IP addresses
- **CloudWatch**: Monitoring and logging

## 📚 Learn More

- [Instance Types →](instance-types.md)
- [Pricing Models →](pricing.md)
- [Security Groups →](security-groups.md)
- [Key Pairs →](key-pairs.md)
- [Connecting to Instances →](connecting-to-instances.md)
- [Launching First Instance →](launching-first-instance.md)
- [EC2 Use Cases →](use-cases.md)

---

**Next Step**: Learn about [EC2 Instance Types](instance-types.md) to choose the right size for your workload.""",

    "tier-1-foundational/ec2/instance-types.md": """# EC2 Instance Types

EC2 offers **500+ instance types** optimized for different workloads. Choosing the right instance type is critical for performance and cost optimization.

## 📊 Instance Type Naming Convention

### Format: `t3.medium`
```
t        3        .     medium
│        │              │
Family   Generation     Size
```

- **Family**: Workload type (t=burstable, m=general, c=compute, r=memory, etc.)
- **Generation**: Newer = better performance/price (use latest when possible)
- **Size**: nano < micro < small < medium < large < xlarge < 2xlarge ... 24xlarge

## 🎯 Instance Family Types

### 1. **General Purpose** (T, M, Mac)

Best for: Web servers, small databases, development environments

#### **T-Series (Burstable Performance)**
```
Ideal for: Variable workloads (dev/test, web servers, microservices)
Feature: CPU Credits (burst above baseline when needed)

t3.micro:   2 vCPU, 1 GB RAM,  $0.0104/hr (~$7.50/month)
t3.small:   2 vCPU, 2 GB RAM,  $0.0208/hr (~$15/month)
t3.medium:  2 vCPU, 4 GB RAM,  $0.0416/hr (~$30/month)
t3.large:   2 vCPU, 8 GB RAM,  $0.0832/hr (~$60/month)

CPU Credits:
- Accrue credits when CPU < baseline (e.g., 20% for t3.micro)
- Spend credits when CPU > baseline
- Unlimited mode: Keep bursting but pay extra

When to Use:
✅ Development/test environments
✅ Code repositories, blogs, small websites
✅ Microservices with variable traffic
❌ Steady high-CPU workloads (use C or M series instead)
```

#### **M-Series (Balanced)**
```
Ideal for: Enterprise applications, SAP, SharePoint, general workloads

m5.large:    2 vCPU,  8 GB RAM,  $0.096/hr
m5.xlarge:   4 vCPU, 16 GB RAM,  $0.192/hr
m5.2xlarge:  8 vCPU, 32 GB RAM,  $0.384/hr
m5.4xlarge: 16 vCPU, 64 GB RAM,  $0.768/hr

When to Use:
✅ Applications with balanced CPU/memory needs
✅ Medium-traffic web servers
✅ Backend app servers
✅ Small-medium databases
```

### 2. **Compute Optimized** (C)

Best for: Batch processing, media transcoding, high-traffic web servers, scientific modeling

#### **C-Series**
```
Ideal for: CPU-intensive workloads

c5.large:     2 vCPU,  4 GB RAM,  $0.085/hr
c5.xlarge:    4 vCPU,  8 GB RAM,  $0.170/hr
c5.2xlarge:   8 vCPU, 16 GB RAM,  $0.340/hr
c5.4xlarge:  16 vCPU, 32 GB RAM,  $0.680/hr
c5.24xlarge: 96 vCPU, 192 GB RAM, $4.08/hr

Features:
- 3.6 GHz Intel Xeon Scalable processors
- Up to 25 Gbps network bandwidth
- EBS-optimized by default

Real-World Examples:
✅ Video encoding (convert 1080p to 720p)
✅ Batch data processing (ETL jobs)
✅ Web servers handling 10K+ requests/sec
✅ Scientific simulations
✅ Machine learning inference (prediction, not training)

Cost Comparison:
Scenario: Encode 100 hours of video
- t3.medium (slow): 200 hours = $8.32
- c5.2xlarge (fast): 20 hours = $6.80 ✅ Cheaper + 10x faster!
```

### 3. **Memory Optimized** (R, X, Z)

Best for: Databases, in-memory caches (Redis, Memcached), big data analytics

#### **R-Series (High Memory)**
```
Ideal for: Databases, in-memory analytics

r5.large:     2 vCPU,  16 GB RAM,  $0.126/hr (8 GB per vCPU)
r5.xlarge:    4 vCPU,  32 GB RAM,  $0.252/hr
r5.2xlarge:   8 vCPU,  64 GB RAM,  $0.504/hr
r5.4xlarge:  16 vCPU, 128 GB RAM,  $1.008/hr
r5.24xlarge: 96 vCPU, 768 GB RAM,  $6.048/hr

When to Use:
✅ MySQL, PostgreSQL databases (1M+ rows)
✅ Redis/Memcached caches
✅ SAP HANA
✅ Apache Spark, Hadoop
```

#### **X-Series (Extreme Memory)**
```
Ideal for: Giant in-memory databases (SAP HANA, Redis)

x1e.xlarge:   4 vCPU,  122 GB RAM,  $0.834/hr
x1e.2xlarge:  8 vCPU,  244 GB RAM,  $1.668/hr
x1e.4xlarge: 16 vCPU,  488 GB RAM,  $3.336/hr
x1e.32xlarge: 128 vCPU, 3,904 GB RAM, $26.688/hr (nearly 4 TB RAM!)

When to Use:
✅ SAP HANA (in-memory database)
✅ Apache Spark (keep entire dataset in RAM)
❌ Overkill for most use cases (very expensive)
```

### 4. **Storage Optimized** (I, D, H)

Best for: NoSQL databases, data warehouses, distributed file systems, log processing

#### **I-Series (NVMe SSD)**
```
Ideal for: Low-latency, high IOPS workloads

i3.large:    2 vCPU,  15 GB RAM, 475 GB NVMe SSD,  $0.156/hr
i3.xlarge:   4 vCPU,  30 GB RAM, 950 GB NVMe SSD,  $0.312/hr
i3.2xlarge:  8 vCPU,  61 GB RAM, 1.9 TB NVMe SSD,  $0.624/hr

Performance:
- 3.3 million IOPS (read)
- 1.4 million IOPS (write)
- < 1ms latency

When to Use:
✅ Cassandra, MongoDB, Elasticsearch
✅ Real-time analytics
✅ Transactional databases (thousands of queries/sec)
```

#### **D-Series (Hard Disk)**
```
Ideal for: Massive sequential I/O (data warehouses)

d2.xlarge:   4 vCPU,  30 GB RAM, 6 TB HDD,   $0.690/hr
d2.2xlarge:  8 vCPU,  61 GB RAM, 12 TB HDD,  $1.380/hr
d2.8xlarge: 36 vCPU, 244 GB RAM, 48 TB HDD,  $5.520/hr

When to Use:
✅ Hadoop/HDFS clusters
✅ MapReduce, Apache Spark
✅ Log processing (TB of logs/day)
```

### 5. **Accelerated Computing** (P, G, F, Inf)

Best for: Machine learning, graphics rendering, video processing, scientific computing

#### **P-Series (GPU for ML Training)**
```
Ideal for: Deep learning model training

p3.2xlarge:  8 vCPU, 61 GB RAM, 1 V100 GPU,  $3.06/hr
p3.8xlarge: 32 vCPU, 244 GB RAM, 4 V100 GPUs, $12.24/hr
p4d.24xlarge: 96 vCPU, 1,152 GB RAM, 8 A100 GPUs, $32.77/hr

GPU Memory:
- V100: 16 GB (p3)
- A100: 40 GB (p4d)

When to Use:
✅ Training neural networks (TensorFlow, PyTorch)
✅ Natural language processing (GPT, BERT)
✅ Computer vision (image recognition)

Example:
Train ResNet-50 model:
- CPU (c5.9xlarge): 10 hours = $6.80
- GPU (p3.2xlarge): 1 hour = $3.06 ✅ 10x faster, cheaper!
```

#### **G-Series (GPU for Graphics/Inference)**
```
Ideal for: Graphics rendering, ML inference, video streaming

g4dn.xlarge:  4 vCPU, 16 GB RAM, 1 T4 GPU,  $0.526/hr
g4dn.2xlarge: 8 vCPU, 32 GB RAM, 1 T4 GPU,  $0.752/hr
g4dn.12xlarge: 48 vCPU, 192 GB RAM, 4 T4 GPUs, $3.912/hr

When to Use:
✅ ML inference (serving predictions)
✅ Video transcoding
✅ 3D rendering
✅ Game streaming
```

#### **Inf-Series (AWS Inferentia - Cheapest ML Inference)**
```
Ideal for: High-throughput ML inference

inf1.xlarge:  4 vCPU, 8 GB RAM, 1 Inferentia chip, $0.228/hr
inf1.6xlarge: 24 vCPU, 48 GB RAM, 4 Inferentia chips, $1.180/hr

When to Use:
✅ Image classification (1000s predictions/sec)
✅ Recommendation systems
✅ Natural language processing

Cost Comparison (1M inferences):
- CPU (c5.large): $5.00
- GPU (g4dn.xlarge): $2.50
- Inferentia (inf1.xlarge): $1.00 ✅ Cheapest!
```

## 🏆 How to Choose the Right Instance Type

### Step 1: Identify Workload Type

```
Web Server (moderate traffic):
→ General Purpose (T3, M5)

Batch Processing (CPU-heavy):
→ Compute Optimized (C5)

Database (lots of RAM needed):
→ Memory Optimized (R5)

NoSQL Database (disk-intensive):
→ Storage Optimized (I3)

ML Training:
→ GPU (P3, P4)

ML Inference (predictions):
→ Inferentia (Inf1) or GPU (G4)
```

### Step 2: Right-Size

Start with a guess, then monitor CloudWatch metrics:

```
CPU Utilization:
- < 20%: Downsize (save money)
- 20-70%: Just right ✅
- > 80%: Upsize (prevent slowness)

Memory Usage:
- < 50%: Consider smaller instance
- 50-80%: Good ✅
- > 90%: Risk of OOM (out of memory) - upsize!

Network:
- Check NetworkIn/NetworkOut metrics
- If hitting limits, use network-optimized instances
```

### Step 3: Consider Costs

```
Development: t3.micro (cheap, burstable)
Staging: t3.small or t3.medium
Production: m5.large or larger (stable performance)

Use Savings Plans or Reserved Instances for 40-70% discount!
```

## 🔄 Migration Path

### Typical Growth Pattern:
```
Stage 1: Startup/MVP
→ t3.micro or t3.small ($7-15/month)

Stage 2: First Customers
→ t3.medium ($30/month)

Stage 3: Growth
→ m5.large ($70/month)
→ Add Load Balancer + Auto Scaling (2-10 instances)

Stage 4: Scale
→ m5.xlarge or m5.2xlarge
→ Separate databases to r5 instances
→ Use Reserved Instances for 40% savings
```

## 💡 Pro Tips

### 1. **Start Small, Scale Up**
```
Don't guess big - start with t3.medium
Monitor for 1 week
Upsize if needed (takes 2 minutes)
```

### 2. **Free Tier**
```
t2.micro: 750 hours/month free for 12 months
= 1 instance running 24/7 for a year!
```

### 3. **Spot Instances for Batch Jobs**
```
Use c5.4xlarge spot: $0.20/hr instead of $0.68/hr
70% savings for fault-tolerant workloads!
```

### 4. **Use Latest Generation**
```
m6i > m5 > m4 (better performance/price)
Always use latest unless app requires specific hardware
```

## 📚 Quick Reference Table

| Use Case | Instance Family | Example | Monthly Cost (24/7) |
|----------|----------------|---------|---------------------|
| Small website | T3 | t3.micro | $7.50 |
| Dev/test server | T3 | t3.small | $15 |
| Production web app | M5 | m5.large | $70 |
| Batch processing | C5 | c5.2xlarge | $245 |
| MySQL database | R5 | r5.large | $91 |
| Redis cache | R5 | r5.xlarge | $182 |
| Cassandra node | I3 | i3.large | $113 |
| ML training | P3 | p3.2xlarge | $2,203 |
| ML inference | Inf1 | inf1.xlarge | $164 |

## 🔗 Related Topics

- [EC2 Pricing →](pricing.md)
- [Launching First Instance →](launching-first-instance.md)
- [Use Cases →](use-cases.md)
- [What is EC2? →](what-is-ec2.md)

---

**Next Step**: Understand [EC2 Pricing](pricing.md) to optimize costs.""",

    # Continue with remaining EC2 files... (truncated for brevity)
    # The script would contain comprehensive content for ALL files
}

def populate_file(file_path, content):
    """Write content to file, creating directories if needed"""
    try:
        # Convert relative path to absolute
        base_dir = Path(__file__).parent
        full_path = base_dir / file_path
        
        # Create parent directories
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write content
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Populated: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error populating {file_path}: {e}")
        return False

def main():
    """Main execution"""
    print("🚀 Starting AWS Documentation Population...")
    print(f"📝 Found {len(CONTENT_MAP)} files to populate\n")
    
    success_count = 0
    fail_count = 0
    
    for file_path, content in CONTENT_MAP.items():
        if populate_file(file_path, content):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n✅ Successfully populated: {success_count} files")
    print(f"❌ Failed: {fail_count} files")
    print("\n🎉 Done!")

if __name__ == "__main__":
    main()

# ============== EXTENDED CONTENT FOR ALL FILES ==============
# This script will be expanded with all 78 files
