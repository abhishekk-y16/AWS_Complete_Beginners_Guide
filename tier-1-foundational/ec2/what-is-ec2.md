# What is Amazon EC2?

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

**Next Step**: Learn about [EC2 Instance Types](instance-types.md) to choose the right size for your workload.