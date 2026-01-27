# AWS VPC (Virtual Private Cloud) 🌐

## 🎯 What is VPC?

VPC is your **private, isolated network on AWS** where you launch EC2, databases, and other resources. Like building a gated community - you control who enters and where traffic flows.

## 🔑 Key Concepts

- **VPC**: Your private network (isolated from others). Choose IP range when creating (CIDR block like 10.0.0.0/16)
- **Subnets**: Subdivisions of your VPC (can be public or private). One per Availability Zone typically
- **Internet Gateway**: Your VPC's connection to the internet. Needed for public websites
- **Route Tables**: Traffic rules (e.g., "All internet traffic goes to Internet Gateway")
- **Security Groups**: Virtual firewalls for individual resources. Port-level control
- **Network ACLs**: Optional stateless firewalls at subnet level (most use Security Groups)

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