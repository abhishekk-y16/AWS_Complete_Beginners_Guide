# Deploy a Simple Web Server 🚀

This tutorial shows how to deploy a simple, production-ready web server on AWS using an EC2 instance, a security group, and an Application Load Balancer (ALB). It includes CLI and Console steps, basic hardening, and cost notes.

Prerequisites:
- An AWS account with permissions for EC2, VPC, IAM, and ELB.
- AWS CLI configured locally (optional but recommended).

Estimated cost (small): ~$10–30/month depending on instance type and transfer.

1) Create a Key Pair (Console)

 - Console: EC2 → Key Pairs → Create key pair
 - Name: `web-server-key`
 - Download `web-server-key.pem` and secure it (chmod 400)

CLI:

```bash
aws ec2 create-key-pair --key-name web-server-key --query 'KeyMaterial' --output text > web-server-key.pem
chmod 400 web-server-key.pem
```

2) Create Security Group

- Purpose: allow HTTP/HTTPS from internet and SSH from your IP only.

Console:

- EC2 → Security Groups → Create security group
- Name: `web-sg`
- Inbound rules:
	- HTTP (80) Source: 0.0.0.0/0
	- HTTPS (443) Source: 0.0.0.0/0
	- SSH (22) Source: your.ip.address/32

CLI example (replace `MY_IP`):

```bash
MY_IP=$(curl -s http://checkip.amazonaws.com)/32
aws ec2 create-security-group --group-name web-sg --description "Web server SG" --vpc-id vpc-xxxx
aws ec2 authorize-security-group-ingress --group-name web-sg --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name web-sg --protocol tcp --port 443 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name web-sg --protocol tcp --port 22 --cidr $MY_IP
```

3) Launch an EC2 Instance

Recommended AMI: Amazon Linux 2 (small apps), Instance type: `t3.small` or `t3.micro` for testing.

Console steps:

- EC2 → Launch Instance
- Choose AMI: Amazon Linux 2
- Choose instance type: `t3.micro` (Free tier) or `t3.small` (recommended for production)
- Configure network: select your VPC and public subnet
- Add Storage: 8–20 GB (gp3)
- Add Tags: Name=web-server-1
- Configure Security Group: select `web-sg`
- Key pair: `web-server-key`
- Launch

4) Install Web Server (via SSH)

SSH into instance:

```bash
ssh -i web-server-key.pem ec2-user@<PUBLIC_IP>
```

On the instance (Amazon Linux 2):

```bash
sudo yum update -y
sudo yum install -y httpd
sudo systemctl enable httpd
sudo systemctl start httpd
echo "<h1>Hello from AWS EC2</h1>" | sudo tee /var/www/html/index.html
```

Test: open `http://<PUBLIC_IP>` in browser.

5) Add an Application Load Balancer (optional, recommended)

Benefits: health checks, SSL termination, high availability across AZs.

Console:

- EC2 → Load Balancers → Create Load Balancer → Application Load Balancer
- Scheme: internet-facing
- Listeners: HTTP (80) and/or HTTPS (443)
- Availability Zones: select at least two AZs and corresponding public subnets
- Security group: create/load balancer SG allowing HTTP/HTTPS
- Target group: create new target group (targets: instances)
- Register your `web-server-1` instance
- Create ALB

6) Health Checks & Auto Scaling (optional)

- Configure health check path `/` on target group.
- Create an Auto Scaling Group (ASG) with desired capacity 2, min 2, max 4 for resilience.

7) SSL (HTTPS)

- Use AWS Certificate Manager (ACM) to request a public certificate (requires domain validation via DNS or email).
- Attach certificate to ALB listener (443) for TLS termination.

8) Hardening Tips

- Remove SSH access for password-based login; use key-only.
- Configure automatic security updates where possible.
- Limit IAM permissions for any deployed application.
- Use CloudWatch for logs and alarms (CPU, 4xx/5xx rates).

9) Cost Notes

- EC2 t3.micro: free tier eligible; otherwise ~$8–12/month.
- ALB: ~$16/month + small per-LCU charge.
- EBS storage: ~$0.08/GB-month (gp3 pricing varies).

10) Troubleshooting

- If instance not reachable: check Security Group, public IP, subnet route to Internet Gateway.
- If ALB shows unhealthy: check instance health checks (security group must allow ALB health check traffic).

Checklist

- [ ] Key pair created and secured
- [ ] Security group restricted for SSH
- [ ] Web server running and responding
- [ ] ALB configured and healthy (if used)
- [ ] SSL certificate attached (if using HTTPS)

Related tutorials:
- `s3-static-website.md` (static hosting alternative)
- `cloudfront-cdn.md` (performance and caching)

Done — you now have a basic, resilient web server deployed on AWS. Scale and secure further as needed.
# Tutorials

AWS Tutorials service