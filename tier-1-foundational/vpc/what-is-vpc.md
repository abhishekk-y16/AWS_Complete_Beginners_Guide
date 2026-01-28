# AWS VPC (Virtual Private Cloud) 🌐

A **Virtual Private Cloud (VPC)** is a private, isolated network environment within AWS. It's like having your own private data center in the cloud.

## Why You Need a VPC

### Security & Isolation 🔐
- Resources isolated from other AWS customers
- Complete access control
- No shared data exposure

### Complete Control 🎮
- Custom IP addressing (CIDR blocks)
- Public/private subnets
- Custom security rules
- VPN and Direct Connect support

### Enterprise Support 🏢
- Multi-tier architectures
- Disaster recovery
- Compliance (PCI-DSS, HIPAA)
- Network segmentation

## Components

| Component | Purpose | Cost |
|-----------|---------|------|
| VPC | Network boundary | FREE |
| Subnet | Network segment | FREE |
| Security Group | Instance firewall | FREE |
| Internet Gateway | Internet access | FREE |
| NAT Gateway | Outbound access | $32-45/month |

## Learning Path

1. **[Subnets](./subnets.md)** - Public vs Private
2. **[Security Groups](./security-groups.md)** - Firewall
3. **[Network ACLs](./nacls.md)** - Advanced control

## Costs

- Simple app: ~$5-10/month
- HA app: ~$50-100/month
- Enterprise: $500+/month

## Key Facts

✅ VPC = Isolated cloud network
✅ Public Subnet = Internet accessible
✅ Private Subnet = Internal only
✅ VPC itself is FREE