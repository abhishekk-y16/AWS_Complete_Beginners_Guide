# Connecting to EC2 Instances 🖥️

How to remotely access your EC2 instances to manage them.

## Connection Methods

### 1. SSH (Linux/Mac/Windows 10+)

**Best for**: Linux instances (Amazon Linux, Ubuntu, CentOS)

```
Prerequisites:
- EC2 instance with Linux AMI
- Key pair (.pem file)
- Security group allowing port 22
- Instance has public IP or bastion access

SSH from terminal:
$ ssh -i my-key.pem ec2-user@54.12.34.56
```

### 2. EC2 Instance Connect

**Best for**: Quick access without key pairs

```
Steps:
1. AWS Console → EC2 Instances
2. Select instance → Connect button
3. Choose "EC2 Instance Connect" tab
4. Click "Connect"
5. Browser-based terminal opens
```

### 3. AWS Systems Manager Session Manager

**Best for**: Secure remote access without public IP

```
Advantages:
✓ No SSH key needed
✓ Works through NAT/private subnet
✓ Audit all commands in CloudTrail
```

### 4. RDP (Windows Instances)

**Best for**: Windows Server instances

```
1. Get Windows password from EC2 console
2. Use Remote Desktop Connection
3. Port: 3389
```

### 5. Bastion Host (Jump Server)

**Best for**: Accessing private instances

```
Your PC → SSH to Bastion (Public)
       → SSH to Private Instance
```

## Typical Workflow

```
1. Launch instance
2. Wait for running status
3. Check security group (port 22)
4. Get public IP
5. SSH: ssh -i key.pem ec2-user@ip
6. Connected!
7. Run commands
8. Exit: exit or logout
```

## First Commands

```
$ uname -a              (System info)
$ df -h                 (Disk space)
$ sudo yum update -y    (Update packages)
$ sudo systemctl status (Check services)
```

## Common Issues

### Can't Connect
```
Check:
1. Instance running?
2. Has public IP?
3. Security group allows port 22?
4. Using correct username?
   - Amazon Linux: ec2-user
   - Ubuntu: ubuntu
   - CentOS: centos
```

### Permission Denied
```
Fix: chmod 600 key.pem
     ssh -i key.pem ec2-user@public-ip
```

### Connection Timeout
```
Try: EC2 Instance Connect (no port 22)
or:  Use bastion host
```

## Best Practices

✅ Use SSH key pairs (not passwords)
✅ Restrict port 22 to your IP only
✅ Use bastion for private instances
✅ Enable CloudTrail auditing
✅ Rotate keys periodically
✅ Use Session Manager when possible

## Next Steps

→ [Key Pairs](./key-pairs.md) - Key management
→ [Security Groups](./security-groups.md) - Network access
→ [What is EC2](./what-is-ec2.md) - Overview