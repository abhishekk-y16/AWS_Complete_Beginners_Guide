# Amazon EC2 (Elastic Compute Cloud)

## 🎯 What is EC2?

Amazon EC2 is a service that lets you rent virtual computers (called "instances") in the cloud. Instead of buying a physical server, you can launch a computer in AWS, choose how powerful it should be, install software on it, and use it just like a regular computer - but you only pay for the time you use it.

It's like renting a car instead of buying one - you get the capability when you need it, and you don't pay when you're not using it.

## 🔑 Key Concepts

- **Instance**: A virtual computer running in AWS with CPU, memory, storage, and an operating system
- **Instance Type**: Different sizes and capabilities (t2.micro, t3.small, m5.large, etc.)
- **AMI**: Amazon Machine Image - a pre-configured template containing OS and software
- **Security Group**: Acts like a firewall - controls what traffic can reach your instance
- **Elastic IP**: A permanent IP address that stays with your instance
- **Key Pair**: SSH keys used to securely connect to your instance
- **Availability Zone**: The specific data center where your instance runs
- **EBS**: Elastic Block Store - storage volumes attached to your instances

## 💡 Real-World Analogy

EC2 is like **renting a computer from a shop**:

- **Instance = The computer** you rent
- **Instance Type = Different models** (basic budget PC, gaming PC, workstation)
- **AMI = Pre-installed software** (bare Windows, Ubuntu, software bundle)
- **Security Group = Locks and doors** controlling who can connect
- **Key Pair = Access cards** to unlock and use the computer
- **Elastic IP = Address** that stays the same even if you move
- **Availability Zone = Different branch locations** where you can rent
- **EBS = External storage drives** you can attach

## 🚀 Common Use Cases

1. **Web Servers**: Host websites and web applications
2. **Application Servers**: Run business applications
3. **Databases**: Database servers (though RDS is usually better)
4. **Development/Testing**: Build and test software
5. **Batch Processing**: Process large amounts of data
6. **Machine Learning**: Training and inference
7. **Game Servers**: Host multiplayer games
8. **Content Rendering**: Video encoding, 3D rendering

## 🛠️ Getting Started

### Prerequisites
- [ ] AWS account created
- [ ] Familiar with Linux/Windows command line (basic knowledge)
- [ ] SSH client (built-in on Mac/Linux, or PuTTY on Windows)

### Step-by-Step: Launch Your First Instance

#### 1. Navigate to EC2 Console

- Sign into AWS Console
- Search for "EC2" in services
- Click "EC2"
- Click "Instances" in the left menu

#### 2. Choose an AMI (Operating System)

- Click orange "Launch instances" button
- **Name**: Enter `my-first-instance`
- **AMI**: Search for "Ubuntu"
  - Click "Ubuntu Server 22.04 LTS free tier eligible"
  - This gives you a Linux computer with Ubuntu

#### 3. Choose Instance Type

- **Instance type**: Select `t2.micro` (free tier eligible)
- This is good enough for learning
- Click "Next: Configure Instance Details"

#### 4. Configure Instance

- Leave most settings as default
- **Monitoring**: You can enable CloudWatch monitoring (small cost)
- Click "Next: Add Storage"

#### 5. Add Storage

- **Size**: 20-30 GB (default is fine for learning)
- **Volume type**: General purpose SSD (gp2) - default is fine
- Click "Next: Add Tags"

#### 6. Add Tags (Optional but Helpful)

- Click "Add new tag"
- **Key**: `Name`
- **Value**: `my-first-instance`
- Helps you identify instances later
- Click "Next: Configure Security Group"

#### 7. Configure Security Group (IMPORTANT!)

This is your firewall. You're allowing traffic.

**Create a new security group** or use default:
- **Security group name**: `my-first-security-group`
- **Description**: "Allow SSH and HTTP traffic"

**Edit inbound rules** (what traffic is ALLOWED IN):

Default Rule (SSH):
- **Type**: SSH
- **Port**: 22
- **Source**: 0.0.0.0/0 (accessible from anywhere - OK for learning, not for production!)

Add Rule for Web Traffic:
- Click "Add Rule"
- **Type**: HTTP
- **Port**: 80
- **Source**: 0.0.0.0/0

Add Rule for HTTPS (Optional):
- Click "Add Rule"
- **Type**: HTTPS
- **Port**: 443
- **Source**: 0.0.0.0/0

⚠️ **Security Note**: In production, restrict SSH to only your IP address!

#### 8. Review and Launch

- Review all settings
- Click "Launch"

#### 9. Create or Use Key Pair (CRITICAL!)

- **Key pair name**: `my-first-keypair`
- Click "Create key pair"
- **File downloads** - SAVE THIS FILE IN A SAFE PLACE
- This is your password to access the instance
- Click "Launch Instances"

#### 10. Monitor Instance Launch

- You'll see "Your instances are launching"
- Click "View Instances"
- Wait for **Instance State** to show "running" (green)
- Wait for **Status Checks** to show "2/2 checks passed" (2-3 minutes)

### Connect to Your Instance

#### On Mac/Linux:

```bash
# Make key pair readable only by you
chmod 400 my-first-keypair.pem

# Connect to instance (replace IP with your instance's IP)
ssh -i my-first-keypair.pem ubuntu@54.123.45.67
```

#### On Windows (using PuTTY):

1. Download and open PuTTY
2. **Host Name**: paste your instance's public IP
3. In left menu → Connection → SSH → Auth
4. **Private key file**: browse to your .pem file
5. Click "Open"
6. Username: `ubuntu`

#### Get Your Instance's IP:

In EC2 Console:
- Click on your instance
- Look for **Public IPv4 address** (in the right panel)
- This is the IP you use to connect

### Once Connected - Run Commands!

```bash
# You're now inside your Linux instance!

# Check what's running
whoami  # Should show 'ubuntu'

# Check instance info
uname -a  # Linux kernel info

# Check storage
df -h  # Disk usage

# Update packages
sudo apt update
sudo apt upgrade -y

# Install a web server
sudo apt install apache2 -y

# Start the web server
sudo systemctl start apache2

# Enable to start on reboot
sudo systemctl enable apache2
```

#### Access Your Web Server:

1. Open browser
2. Go to: `http://54.123.45.67` (use your instance's public IP)
3. You should see Apache welcome page!

### Stop, Start, Terminate

**Stop Instance** (keep for later, don't pay for compute):
- Select instance → Instance State → Stop

**Start Instance** (restart, same IP if Elastic IP):
- Select instance → Instance State → Start

**Terminate Instance** (delete - can't recover!):
- Select instance → Instance State → Terminate
- ⚠️ **WARNING**: This deletes the instance and its data!

## 💰 Pricing Overview

EC2 pricing depends on several factors:

### Instance Type & Size

**On-Demand Pricing** (pay per hour, no commitment):
- `t2.micro`: ~$0.0116/hour (eligible for free tier)
- `t3.small`: ~$0.0208/hour
- `t3.medium`: ~$0.0416/hour
- `m5.large`: ~$0.096/hour
- `m5.xlarge`: ~$0.192/hour
- `c5.large`: ~$0.085/hour (optimized for compute)

### Pricing Tiers

1. **On-Demand**: Pay as you go
   - Most expensive
   - Good for learning, development, sporadic use
   - No commitment

2. **Reserved Instances**: Buy 1-3 year commitment
   - 40-50% discount vs On-Demand
   - Good for servers you'll run continuously

3. **Spot Instances**: Bid for unused capacity
   - 70-90% discount
   - Can be interrupted with 2-minute notice
   - Good for batch processing

4. **Savings Plans**: Flexible commitment (hourly spend)
   - Similar to Reserved
   - More flexibility on instance type changes

### Additional Costs

- **EBS Storage**: $0.10/GB/month (20 GB = $2/month)
- **Data Transfer OUT**: $0.09/GB (first 1 GB free)
- **Elastic IP**: FREE if attached to running instance
- **Elastic IP**: $0.005/hour if NOT attached (sitting unused)

### Free Tier (First 12 Months)

- **750 hours** of `t2.micro` per month
- **30 GB** EBS storage
- **1 GB** data transfer out per month

💰 **Cost Tips**:
- Use t2.micro for learning (free tier)
- Stop instances when not using (don't terminate!)
- Use Reserved Instances for always-on servers
- Use Spot Instances for batch jobs
- Delete unused Elastic IPs
- Terminate instances when completely done (not just stopping)

## ⚠️ Important Things to Know

- **Free Tier**: One t2.micro instance free for 12 months (must be new AWS account)
- **Key Pairs are Critical**: Lose your .pem file = can't access instance
- **Linux vs Windows**: Linux (Ubuntu) is free tier eligible; Windows costs extra
- **Regions**: Instance exists in only one region
- **Availability**: High availability requires multiple instances in different AZs
- **IP Addresses**: Public IP changes if you stop/start (use Elastic IP to keep same IP)
- **Stop vs Terminate**: Stop = pause (still pay for storage); Terminate = delete
- **Security Groups**: Default denies all traffic - you must allow what you need
- **Monitoring**: CloudWatch is built-in for monitoring metrics

## 🔗 Related Services

- **ECS/EKS**: Container orchestration (run many applications on EC2)
- **Lambda**: Serverless compute (don't manage instances)
- **RDS**: Managed databases (don't need to manage database EC2 instances)
- **Elastic Load Balancer**: Distribute traffic across multiple EC2 instances
- **Auto Scaling**: Automatically add/remove instances based on demand
- **Elastic Beanstalk**: Deploy applications without managing EC2 details
- **AMI**: Save your configured instance as a template
- **Snapshot**: Backup your EBS volumes

## 📚 Next Steps

- [ ] [Install a web server](launching-first-instance.md) on your instance
- [ ] Learn about [Instance Types](instance-types.md) to choose right size
- [ ] Understand [Security Groups](security-groups.md) better
- [ ] Explore [Key Pairs](key-pairs.md) and SSH access
- [ ] Create an [AMI from your instance](../../tutorials/deploy-web-server.md)

## 🆘 Common Issues & Solutions

**Problem**: "Connection timeout" when trying SSH
**Solution**:
- Instance might still be starting (wait 2-3 min)
- Security Group might not allow SSH (port 22)
- Check Security Group inbound rules
- Try: `ssh -v` to see detailed connection info

**Problem**: "Permission denied" when connecting
**Solution**:
- Key pair file permissions wrong: `chmod 400 my-first-keypair.pem`
- Using wrong username (usually `ubuntu` for Ubuntu AMI)
- Using wrong IP address - get it from console

**Problem**: Instance keeps stopping automatically
**Solution**:
- Might be shutdown inside the OS
- Check CloudWatch metrics for errors
- Look at system log: Instance → Monitor → System Log

**Problem**: Can't SSH but HTTP works
**Solution**:
- SSH (port 22) not allowed in Security Group
- Add inbound rule for SSH, port 22, source 0.0.0.0/0

**Problem**: Instance stuck in "pending" state
**Solution**:
- Usually resolves in 1-2 minutes
- If longer: try stopping/starting
- Last resort: terminate and launch new instance

## 💡 Best Practices

1. **Always Use Security Groups**: Restrict traffic to only what you need
2. **Enable CloudWatch Detailed Monitoring**: Track CPU, disk, network
3. **Backup Important Data**: Use EBS snapshots regularly
4. **Use Elastic IPs**: If you need permanent IP addresses
5. **Tag Everything**: Use tags for cost tracking and organization
6. **Create AMIs**: Save your configuration as a template for future instances
7. **Use Auto Scaling**: For production, not manual scaling
8. **Monitor Costs**: Set CloudWatch billing alerts
9. **Stop Don't Terminate**: For learning, stop instances to save money
10. **Use IAM Roles**: Don't put AWS credentials on instances (use IAM roles instead)

## 🎓 Hands-On Exercise: Host a Simple Website

**Goal**: Create a web server on EC2 and serve a website

1. **Launch t2.micro Ubuntu instance** (as shown above)

2. **Connect via SSH**
```bash
ssh -i my-first-keypair.pem ubuntu@YOUR_PUBLIC_IP
```

3. **Install web server**
```bash
sudo apt update
sudo apt install apache2 -y
```

4. **Create simple website**
```bash
sudo nano /var/www/html/index.html
```

5. **Paste this HTML**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My AWS Website</title>
    <style>
        body { font-family: Arial; margin: 50px; background: #f0f0f0; }
        .container { background: white; padding: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Welcome to My AWS Website!</h1>
        <p>This is running on EC2 instance in AWS.</p>
        <p>Instance ID: Check your console</p>
    </div>
</body>
</html>
```

6. **Press Ctrl+O, Enter, Ctrl+X to save**

7. **Visit your site**
   - Open browser
   - Go to: `http://YOUR_PUBLIC_IP`
   - See your website!

## 📊 Monitoring Your Instance

**Basic CloudWatch Metrics:**
- CPU Utilization
- Network In/Out
- Disk operations
- Status checks

**View in Console:**
1. Click on instance
2. "Monitor" tab
3. See graphs of metrics

**Set Up Alarms:**
1. CloudWatch → Alarms
2. Create alarm for high CPU
3. Get notified when CPU > 80%

## 📖 Additional Resources

- [Official EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [EC2 Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
- [AWS Free Tier EC2](https://aws.amazon.com/free/)
- [EC2 Security Best Practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html)
- [EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/)

---

**Last Updated**: January 2025  
**Difficulty Level**: ⭐ Beginner  
**Estimated Learning Time**: 3-4 hours
