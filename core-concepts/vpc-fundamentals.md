# VPC Fundamentals 🌐

Virtual Private Cloud - your own private network in AWS.

## What is a VPC?

**Think of it as:** Your own private data center in the cloud

```
VPC = Virtual Private Cloud

Your isolated network in AWS:
- Private IP addresses
- Controlled access
- Custom routing
- Security rules
```

**Analogy:** Your house with walls, doors, locks
- VPC = Your property boundary
- Subnets = Rooms in your house
- Security Groups = Door locks
- NACLs = Fence around property

## Why VPC?

### Without VPC
```
❌ All resources public
❌ No isolation
❌ Security nightmare
❌ Can't control network
```

### With VPC
```
✅ Resources isolated
✅ Private communication
✅ Controlled internet access
✅ Custom IP ranges
✅ Multi-tier architecture
```

## VPC Architecture

```
                     Internet
                        |
                 [Internet Gateway]
                        |
            ==========================
            |        VPC             |
            |   10.0.0.0/16          |
            |                        |
            |  +-----------------+   |
            |  | Public Subnet   |   |
            |  | 10.0.1.0/24     |   |
            |  |                 |   |
            |  | [Web Server]    |   |
            |  +-----------------+   |
            |          |             |
            |  [NAT Gateway]         |
            |          |             |
            |  +-----------------+   |
            |  | Private Subnet  |   |
            |  | 10.0.2.0/24     |   |
            |  |                 |   |
            |  | [Database]      |   |
            |  +-----------------+   |
            ==========================
```

## Core VPC Components

### 1. VPC (The Container)
```
Your private network

IP Range (CIDR):
- 10.0.0.0/16 (65,536 IPs)
- 172.16.0.0/16 (65,536 IPs)
- 192.168.0.0/16 (65,536 IPs)

Example:
- VPC: 10.0.0.0/16
- Can use: 10.0.0.0 to 10.0.255.255
```

### 2. Subnets (Rooms)
```
Subdivisions of VPC

Public Subnet:
- Has internet access
- Web servers
- Load balancers
- Example: 10.0.1.0/24

Private Subnet:
- No direct internet
- Databases
- App servers
- Example: 10.0.2.0/24
```

### 3. Internet Gateway (Front Door)
```
Allows VPC to access internet

One per VPC
Highly available
Free!

Required for:
- Public subnets
- Outbound internet
- Inbound internet
```

### 4. NAT Gateway (Private Exit)
```
Allows private subnets to access internet
(But internet can't access them)

Use cases:
- Software updates
- API calls
- Download files

Cost: $32/month + $0.045/GB
```

### 5. Route Tables (Directions)
```
Define where traffic goes

Public Route Table:
- 10.0.0.0/16 → local
- 0.0.0.0/0 → Internet Gateway

Private Route Table:
- 10.0.0.0/16 → local
- 0.0.0.0/0 → NAT Gateway
```

### 6. Security Groups (Door Locks)
```
Firewall for instances
Stateful (remembers connections)

Example:
- Inbound: Allow port 80 (HTTP)
- Inbound: Allow port 443 (HTTPS)
- Outbound: Allow all

Default: Deny all inbound
```

### 7. NACLs (Property Fence)
```
Network Access Control Lists
Firewall for subnets
Stateless (doesn't remember)

Example:
- Inbound: Allow HTTP (80)
- Outbound: Allow HTTP (80)

Default: Allow all
```

## Creating Your First VPC

### Option 1: Default VPC (Already Exists)
```
Every account has:
- Default VPC (172.31.0.0/16)
- In each region
- Public subnets
- Internet Gateway

✅ Good for learning
❌ Not for production
```

### Option 2: Custom VPC

**Step 1: Create VPC**
```
1. VPC Console → Create VPC

VPC settings:
- Name: my-app-vpc
- IPv4 CIDR: 10.0.0.0/16
- Tenancy: Default

2. Create VPC

✅ VPC created!
```

**Step 2: Create Subnets**
```
1. Subnets → Create subnet

Public Subnet:
- VPC: my-app-vpc
- Name: public-subnet
- AZ: us-east-1a
- CIDR: 10.0.1.0/24

Create subnet

Private Subnet:
- VPC: my-app-vpc
- Name: private-subnet
- AZ: us-east-1a
- CIDR: 10.0.2.0/24

Create subnet

✅ 2 subnets created!
```

**Step 3: Internet Gateway**
```
1. Internet Gateways → Create

Name: my-igw

2. Create

3. Select IGW → Actions → Attach to VPC

VPC: my-app-vpc

4. Attach

✅ IGW attached!
```

**Step 4: Route Tables**
```
Public Route Table:

1. Route Tables → Create
   Name: public-rt
   VPC: my-app-vpc

2. Select route table → Routes → Edit
   Add route:
   - Destination: 0.0.0.0/0
   - Target: [Internet Gateway]

3. Subnet Associations → Edit
   Associate: public-subnet

✅ Public subnet has internet!
```

**Step 5: NAT Gateway (Optional)**
```
1. NAT Gateways → Create

Subnet: public-subnet (must be public!)
Elastic IP: Allocate Elastic IP

2. Create

3. Create private route table:
   - Name: private-rt
   - Add route: 0.0.0.0/0 → NAT Gateway
   - Associate: private-subnet

✅ Private subnet has internet (outbound)

Cost: ~$32/month
```

## Security Groups Deep Dive

### How They Work
```
Stateful = Remembers connections

Example:
1. Allow inbound HTTP (port 80)
2. Request comes in on port 80
3. Response automatically allowed out

No need to add outbound rule!
```

### Common Security Group Rules

**Web Server:**
```
Inbound:
- HTTP: Port 80, Source: 0.0.0.0/0
- HTTPS: Port 443, Source: 0.0.0.0/0
- SSH: Port 22, Source: [Your IP]

Outbound:
- All traffic: All, Destination: 0.0.0.0/0
```

**Database:**
```
Inbound:
- MySQL: Port 3306, Source: [Web SG]
- PostgreSQL: Port 5432, Source: [Web SG]

Outbound:
- All traffic: All (for updates)

✅ Only web servers can access!
```

**Application Server:**
```
Inbound:
- Custom TCP: Port 8080, Source: [Load Balancer SG]

Outbound:
- HTTPS: Port 443 (API calls)
- MySQL: Port 3306 (to database)
```

### Security Group Best Practices

```
✅ Least privilege (minimum required)
✅ Reference other SGs (not IP addresses)
✅ Separate SGs per tier (web, app, db)
✅ Document rules (add descriptions)

❌ Don't allow 0.0.0.0/0 for SSH
❌ Don't use same SG for everything
❌ Don't forget to remove old rules
```

## NACLs vs Security Groups

```
+------------------+------------------+
| Security Groups  | NACLs            |
+------------------+------------------+
| Instance level   | Subnet level     |
| Stateful         | Stateless        |
| Allow rules only | Allow & Deny     |
| All rules eval   | Rules in order   |
| Default: deny    | Default: allow   |
+------------------+------------------+

Use Security Groups for 99% of cases
Use NACLs for subnet-wide blocking
```

## Common VPC Patterns

### 1. Simple Web App
```
VPC: 10.0.0.0/16

Public Subnet: 10.0.1.0/24
- Load Balancer
- Web Servers

Private Subnet: 10.0.2.0/24
- Database
- Cache

✅ Most common pattern
```

### 2. Multi-Tier
```
VPC: 10.0.0.0/16

Public Subnet: 10.0.1.0/24
- Load Balancer

App Subnet: 10.0.2.0/24
- Application Servers

Data Subnet: 10.0.3.0/24
- Databases

✅ Better isolation
```

### 3. Multi-AZ (High Availability)
```
VPC: 10.0.0.0/16

Availability Zone A:
- Public: 10.0.1.0/24
- Private: 10.0.2.0/24

Availability Zone B:
- Public: 10.0.3.0/24
- Private: 10.0.4.0/24

✅ Survives AZ failure
```

## VPC Connectivity

### 1. VPC Peering
```
Connect two VPCs

VPC A (10.0.0.0/16) <----> VPC B (172.16.0.0/16)

Use cases:
- Different projects
- Different accounts
- Shared services

Cost: $0 (data transfer charges apply)
```

### 2. VPN Connection
```
Connect on-premises to AWS

Your Office <--[VPN]--> AWS VPC

Setup:
- Virtual Private Gateway (AWS side)
- Customer Gateway (your side)
- VPN Connection

Cost: $0.05/hour ($36/month)
```

### 3. Direct Connect
```
Dedicated network connection

Your Data Center <--[Fiber]--> AWS

Benefits:
- Lower latency
- More bandwidth
- More reliable

Cost: $0.30/hour + port fees ($216/month+)
```

### 4. Transit Gateway
```
Hub connecting multiple VPCs

     [Transit Gateway]
      /    |    |    \
   VPC1  VPC2  VPC3  VPN

Manage connectivity centrally
Cost: $0.05/hour per attachment
```

## VPC Costs

### Free:
```
✅ VPC itself
✅ Subnets
✅ Route tables
✅ Internet Gateway
✅ Security Groups
✅ NACLs
```

### Paid:
```
💰 NAT Gateway: $32/month + $0.045/GB
💰 VPN: $36/month
💰 Direct Connect: $216+/month
💰 Transit Gateway: $36/month per attachment
💰 Elastic IPs (if unused): $3.60/month
```

## Troubleshooting VPC Issues

### Can't Connect to Instance
```
1. Check Security Group:
   - Is port allowed?
   - Is your IP allowed?

2. Check NACL:
   - Inbound rule exists?
   - Outbound rule exists?

3. Check Route Table:
   - Route to IGW?
   - Subnet associated?

4. Check Instance:
   - Public IP assigned?
   - Service running?
```

### No Internet in Private Subnet
```
1. NAT Gateway exists?
2. NAT in public subnet?
3. Route table has NAT route?
4. Subnet associated with route table?
```

### VPC Peering Not Working
```
1. Route tables updated (both sides)?
2. Security groups allow traffic?
3. NACLs allow traffic?
4. CIDR ranges don't overlap?
```

## VPC Best Practices

### 1. Plan IP Ranges
```
✅ Use RFC 1918 ranges:
   - 10.0.0.0/8
   - 172.16.0.0/12
   - 192.168.0.0/16

✅ Leave room to grow:
   - Start: 10.0.0.0/16 (65k IPs)
   - Not: 10.0.0.0/24 (256 IPs)

❌ Don't overlap with:
   - On-premises network
   - Other VPCs
```

### 2. Multiple Availability Zones
```
✅ Spread across AZs:
   - Public: AZ-a, AZ-b
   - Private: AZ-a, AZ-b

✅ High availability
✅ Fault tolerance
```

### 3. Subnet Sizing
```
Small app:
- Public: /24 (256 IPs)
- Private: /24 (256 IPs)

Medium app:
- Public: /22 (1024 IPs)
- Private: /21 (2048 IPs)

Large app:
- Public: /20 (4096 IPs)
- Private: /19 (8192 IPs)
```

### 4. Use VPC Flow Logs
```
Monitor network traffic:
- Accepted connections
- Rejected connections
- Source/destination IPs

Debugging & security!
```

## VPC Checklist

🔴 **Essential:**
- ✅ VPC created (10.0.0.0/16)
- ✅ Public subnet (10.0.1.0/24)
- ✅ Private subnet (10.0.2.0/24)
- ✅ Internet Gateway attached
- ✅ Route tables configured

🟠 **Recommended:**
- ✅ Multi-AZ setup
- ✅ NAT Gateway (if needed)
- ✅ Security groups per tier
- ✅ VPC Flow Logs

🟡 **Advanced:**
- ✅ VPC endpoints (S3, DynamoDB)
- ✅ VPN/Direct Connect
- ✅ Transit Gateway

## Quick Reference

### VPC Limits
```
VPCs per region: 5 (default)
Subnets per VPC: 200
Security Groups per VPC: 2,500
Rules per Security Group: 60
NACLs per VPC: 200
Routes per Route Table: 200
```

### CIDR Cheat Sheet
```
/16 = 65,536 IPs (recommended VPC)
/20 = 4,096 IPs
/24 = 256 IPs (recommended subnet)
/28 = 16 IPs

Smaller number = more IPs
```

## 📖 Next Steps

1. [Security Best Practices](security-best-practices.md)
2. [IAM Basics](iam-basics.md)
3. [Regions and Availability Zones](regions-and-availability-zones.md)

## Related Resources

- [Networking Issues](../troubleshooting/networking-issues.md)
- [Security Checklist](../best-practices/security-checklist.md)
- [AWS VPC Documentation](https://docs.aws.amazon.com/vpc/)