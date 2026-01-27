# EC2 Troubleshooting Guide 🔧

Common EC2 issues and solutions.

## Can't Connect to EC2 Instance

### Symptom
```
Connection refused / Connection timeout
Cannot SSH to instance
```

### Solutions

**1. Check instance is running**
- Console → EC2 → Instances
- Status should be "Running"
- If "Stopped", click "Start Instance"

**2. Check Security Group**
- Instance → Security Groups
- Inbound Rules should allow SSH (port 22)
- Rule should be: TCP, Port 22, Source: Your IP (or 0.0.0.0/0)
- If missing, add it!

**3. Check SSH key file**
- Permissions should be 400: `chmod 400 key.pem`
- Correct key for this instance?
- Not corrupted/empty?

**4. Check public IP**
- Instance → Details → Public IPv4
- Should not be empty
- If empty, allocate Elastic IP

**5. Check VPC routing**
- Instance → VPC → VPC ID
- VPC should have Internet Gateway
- Route table should route 0.0.0.0/0 to IGW

**6. Wait a moment**
- Instance takes 30-60 seconds to fully boot
- Security groups take 10 seconds to apply

## Instance Keeps Stopping

### Symptom
```
Instance stops automatically
Not due to manual stop
```

### Solutions

**1. Check Auto Scaling**
- Auto Scaling → Auto Scaling Groups
- Is instance part of ASG?
- Min/Desired/Max settings correct?

**2. Check CloudWatch Alarms**
- CloudWatch → Alarms
- Any alarms stopping the instance?

**3. Check Instance Health**
- Instance → Details → Instance State
- State Transition Reason
- Shows why it stopped

**4. Check EBS volume**
- Instance → Storage
- EBS volume full? (Disk space issues)
- Volume failures? Check CloudWatch

**5. Check EC2 capacity**
- If "Capacity Exceeded" error
- Availability Zone out of capacity
- Try different AZ: Terminate + Launch in different AZ

## High CPU Usage

### Symptom
```
CPU usage constantly 80-100%
Instance slow/unresponsive
```

### Solutions

**1. Check CloudWatch metrics**
- CloudWatch → Metrics → EC2 → CPU Utilization
- Is it actually high? (Not spike?)
- How long has it been high?

**2. SSH to instance, check processes**
```bash
# See running processes
top

# See CPU hogs
ps aux --sort=-%cpu

# See disk usage
df -h

# See memory usage
free -h
```

**3. Common causes & fixes**
- Web server misconfigured → Check config
- Database query slow → Optimize query
- Backup running → Wait for completion
- Memory swapping → Increase instance size or RAM

**4. Scale up**
- Stop instance
- Change instance type (t3.medium → t3.large)
- Start instance
- Restart application

**5. Auto Scaling**
- Set up Auto Scaling group
- Launches more instances when CPU > 70%
- Automatic scaling

## Out of Disk Space

### Symptom
```
"No space left on device" error
Cannot write files
```

### Solutions

**1. Check disk usage**
```bash
df -h
```

**2. Find large files**
```bash
du -sh /*
find / -type f -size +1G
```

**3. Clean up**
```bash
# Old logs
rm /var/log/*.old

# Package manager cache
apt-get clean

# Temp files
rm -rf /tmp/*
```

**4. Expand volume**
- Stop instance (if EBS backed)
- Create snapshot of volume
- Create new larger volume from snapshot
- Attach new volume
- Reboot and use new volume

## Instance Launches but No Traffic

### Symptom
```
Instance running and healthy
But application not responding
Website shows "connection refused"
```

### Solutions

**1. Check application is running**
```bash
ssh to instance
ps aux | grep application-name
```

**2. Check application listening on correct port**
```bash
sudo netstat -tlnp | grep LISTEN
```

**3. Check Security Group inbound rules**
- Instance → Security Groups
- HTTP should allow port 80
- HTTPS should allow port 443
- Custom port should allow correct port number

**4. Check application logs**
```bash
tail -f /var/log/application.log
```

**5. Check if service is running**
```bash
sudo systemctl status application-name
sudo systemctl start application-name
```

## Instance Won't Start

### Symptom
```
Cannot launch instance
Error message appears
```

### Solutions

**1. Check limits**
- EC2 → Limits
- Running instances limit exceeded?
- Request limit increase (1-5 minutes)

**2. Check capacity**
- Error: "Insufficient capacity"
- Try different Availability Zone
- Different instance type

**3. Check IAM permissions**
- User has EC2 launch permissions?
- Check IAM policy

**4. Check key pair exists**
- EC2 → Key Pairs
- Selected key pair exists?
- Not deleted accidentally?

## Network Performance Issues

### Symptom
```
Instance slow
Network throughput low
```

### Solutions

**1. Check instance type**
- Different instance types have different network limits
- t3.small = limited network
- m5.large = better network
- Upgrade if needed

**2. Check ENI metrics**
- CloudWatch → Metrics → EC2 → Network
- Bytes sent/received normal?
- Packets dropped?

**3. Use enhanced networking**
- Some instance types support: ena
- Better performance with ena
- Check instance type capabilities

**4. Use placement groups**
- For low-latency, high-bandwidth
- EC2 → Placement Groups
- Create and use for related instances

## 📖 Related Resources

- [EC2 Documentation](../tier-1-foundational/ec2/README.md)
- [Security Groups](../tier-1-foundational/vpc/README.md)
- [CloudWatch Monitoring](../tier-2-common/cloudwatch/README.md)
- [Common Errors Guide](common-errors.md)