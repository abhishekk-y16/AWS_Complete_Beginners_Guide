# VPC Subnets 🏗️

A **subnet** is a subdivision of your VPC that spans a single Availability Zone (AZ). It's like dividing your office into separate floors.

## Subnet Types

### 🌍 Public Subnet

**Purpose**: Resources that need internet access

| Property | Details |
|----------|---------|
| Internet Access | YES - via Internet Gateway |
| Public IP | Can have Elastic IP |
| Use Cases | Web servers, load balancers |
| Security | Security groups + NACLs |

```
Route Table:
10.0.0.0/16 → Local (VPC traffic)
0.0.0.0/0   → IGW (Internet)
```

**Example**: Web server at 10.0.1.100 can reach google.com

### 🔐 Private Subnet

**Purpose**: Resources NOT accessible from internet

| Property | Details |
|----------|---------|
| Internet Access | Outbound only (via NAT) |
| Public IP | NO - no internet exposure |
| Use Cases | App servers, databases |
| Security | Maximum isolation |

```
Route Table:
10.0.0.0/16 → Local (VPC traffic)
0.0.0.0/0   → NAT (Outbound only)
```

**Example**: Database at 10.0.10.50 can download packages, but internet cannot reach it

## IP Addressing: CIDR Notation

```
10.0.1.0/24
  ↑      ↑
  │      └─ /24 = 256 total IPs
  └─ Network address

Common sizes:
/16 = 65,536 IPs (VPC)
/24 = 256 IPs    (Typical subnet)
/25 = 128 IPs    (Small subnet)
/32 = 1 IP       (Single host)
```

## Reserved IPs

In every subnet, 5 IPs are reserved:

```
Subnet: 10.0.1.0/24 (256 IPs total)

10.0.1.0       → Network address (reserved)
10.0.1.1       → VPC router (reserved)
10.0.1.2       → DNS server (reserved)
10.0.1.3       → Future use (reserved)
10.0.1.4-254   → 251 USABLE IPs ✓
10.0.1.255     → Broadcast (reserved)

Formula: 256 - 5 = 251 usable IPs
```

## Multi-AZ Deployment

### Single AZ (Not Recommended)
```
AZ: us-east-1a
├─ Public Subnet: 10.0.1.0/24 (Web)
└─ Private Subnet: 10.0.10.0/24 (DB)

Risk: If AZ fails → Everything down ✗
```

### Multi-AZ (High Availability)
```
AZ-A                    AZ-B
├─ 10.0.1.0/24         ├─ 10.0.2.0/24
│  └─ Web Server #1    │  └─ Web Server #2
└─ 10.0.10.0/24        └─ 10.0.11.0/24
   └─ App #1              └─ App #2

Benefit: If AZ-A fails, AZ-B handles traffic ✓
Cost: ~2x resources
```

## Common Configuration

```
VPC: 10.0.0.0/16

Tier 1 - Web (Public)
├─ AZ-A: 10.0.1.0/24 (251 IPs)
└─ AZ-B: 10.0.2.0/24 (251 IPs)

Tier 2 - App (Private)
├─ AZ-A: 10.0.10.0/24 (251 IPs)
└─ AZ-B: 10.0.11.0/24 (251 IPs)

Tier 3 - Database (Private)
├─ AZ-A: 10.0.20.0/24 (251 IPs)
└─ AZ-B: 10.0.21.0/24 (251 IPs)

Total: 6 subnets, 1,506 usable IPs
```

## Common Mistakes

### ✗ Mistake 1: No IGW Route
```
Public Subnet Route Table:
10.0.0.0/16 → Local ✓
0.0.0.0/0   → (missing!) ✗

Result: Web server can't reach internet
✅ Fix: Add route: 0.0.0.0/0 → IGW
```

### ✗ Mistake 2: Database in Public Subnet
```
Result: Database exposed to internet
✅ Fix: Move to private subnet
```

### ✗ Mistake 3: Wrong NAT Gateway AZ
```
Private Subnet (us-east-1a): 10.0.10.0/24
NAT Gateway in AZ-B ✗ (different AZ)

✅ Fix: NAT Gateway should be in SAME AZ public subnet
```

## Pricing

✓ VPC Subnets: FREE
✓ Route Tables: FREE (2 included)
✓ Data within VPC: FREE
✗ NAT Gateway: ~$32/month
✗ Data transfer: $0.01-0.02/GB

## Best Practices

✅ Plan CIDR blocks before creation
✅ Deploy across multiple AZs for HA
✅ Separate public/private by function
✅ Use descriptive subnet names
✅ Leave IP space for growth (don't use /30)

## Next Steps

→ [Security Groups](./security-groups.md) - Instance firewall
→ [Network ACLs](./nacls.md) - Subnet firewall
→ [What is VPC](./what-is-vpc.md) - Architecture overview