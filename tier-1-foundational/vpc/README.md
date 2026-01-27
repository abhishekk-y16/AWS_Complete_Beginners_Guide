# VPC - Virtual Private Cloud

Your private network in AWS. Isolate resources, control traffic, build secure architectures.

## 📚 Learning Path

1. **[What is VPC?](what-is-vpc.md)** - Networking fundamentals
2. **[Subnets](subnets.md)** - Breaking up your network
3. **[Security Groups](security-groups.md)** - Firewall rules
4. **[NACLs](nacls.md)** - Network-level access control

## 🎯 Quick Summary

VPC is your isolated network in AWS. Every resource (EC2, RDS, Lambda) runs in a VPC.

| Aspect | Value |
|--------|-------|
| **Cost** | FREE (NAT gateway: $0.045/hour) |
| **Max IPs** | 16,384 per VPC |
| **Isolation** | Complete from other accounts |
| **Control** | Full network customization |

## 🏗️ Architecture Layers

```
VPC (10.0.0.0/16)
├─ Public Subnet (10.0.1.0/24)
│  └─ Route: 0.0.0.0/0 → Internet Gateway
├─ Private Subnet (10.0.2.0/24)
│  └─ Route: 10.0.0.0/16 → Local only
├─ Route Tables (traffic rules)
├─ Security Groups (instance firewall)
├─ NACLs (subnet firewall)
└─ Internet Gateway (bridge to internet)
```

## 📊 Public vs Private

| Feature | Public | Private |
|---------|--------|---------|
| Internet | Yes | No/NAT |
| Public IP | Yes | No |
| Use | Websites, LBs | Databases, apps |
| Security | Lower | Higher |

## 💡 3-Tier Architecture Example

```
┌─────────────────────────────────────┐
│ VPC: 10.0.0.0/16                    │
├─────────────────────────────────────┤
│ Public Layer: Load Balancer         │
├─────────────────────────────────────┤
│ Private Layer: App Servers          │
├─────────────────────────────────────┤
│ Private Layer: Database             │
└─────────────────────────────────────┘
```

## 🚀 Common Scenarios

### Simple Website
- Public subnet with web servers
- Internet traffic to port 80/443

### Web + Database  
- Public subnet: Web servers
- Private subnet: Database (no internet access)

### High Availability
- Multiple AZs
- Auto Scaling Group
- Multi-AZ RDS

## ⚠️ Common Mistakes

1. Database in public subnet
2. Single subnet (no HA)
3. Missing security group rules
4. Overcomplicated design

## ✅ Best Practices

- Use multiple subnets across 2+ AZs
- Keep databases in private subnets
- Document CIDR ranges
- Use VPC Flow Logs for debugging
- Implement least-privilege access

---
**Start**: [What is VPC?](what-is-vpc.md)

## 💡 Real-World Architecture

```
Internet
   ↓
Internet Gateway (attached to VPC)
   ↓
VPC 10.0.0.0/16
├── Public Subnet 10.0.1.0/24
│   ├── Web server (EC2) - accessible from internet
│   └── Load balancer
├── Private Subnet 10.0.2.0/24
│   └── Database (RDS) - NOT accessible from internet
└── Private Subnet 10.0.3.0/24
    └── Application server - requires NAT to reach internet
```

## 🚀 Getting Started

1. Go to VPC Console → Create VPC
2. Set CIDR block (10.0.0.0/16 is common)
3. Create public subnet for web servers
4. Create private subnets for databases
5. Attach Internet Gateway
6. Create Route Table to route traffic
7. Create Security Groups to allow/block ports

## 📊 Default VPC

- AWS provides a default VPC already configured
- Good for testing and learning
- Can create multiple VPCs for different environments

## ⭐ Best Practices

- ✓ Use private subnets for databases (not internet-accessible)
- ✓ Use public subnets only for load balancers/bastion hosts
- ✓ One subnet per Availability Zone for high availability
- ✓ Use Security Groups at instance level
- ✓ Document your VPC topology

## 📖 Official Resources

- [VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-best-practices.html)
- [Core VPC Fundamentals](../../core-concepts/vpc-fundamentals.md)