# VPC Security Groups 🛡️

A **Security Group** is a virtual firewall at the **instance level** that controls inbound and outbound traffic to EC2 instances. Like a bouncer at a nightclub - allowing certain traffic in and out.

## How Security Groups Work

### ⬇️ Inbound Rules (Incoming Traffic)

**What can connect TO your instance?**

```
Example Inbound Rules:
┌──────────────────────────────────────────┐
│ Port 80 (HTTP)     from 0.0.0.0/0 (all)  │
│ Port 443 (HTTPS)   from 0.0.0.0/0 (all)  │
│ Port 22 (SSH)      from 203.0.113.0/24   │
│ Port 3306 (MySQL)  from App SG only      │
│ Else: DENY (default)                     │
└──────────────────────────────────────────┘
```

### ⬆️ Outbound Rules (Outgoing Traffic)

**What can your instance connect TO?**

```
Example Outbound Rules (Default: ALLOW ALL):
┌────────────────────────────────────────┐
│ All traffic allowed outbound (default)  │
│ Can call APIs, download packages, etc   │
└────────────────────────────────────────┘
```

## Security Group Properties

| Property | Details |
|----------|---------|
| Scope | Instance level |
| State | STATEFUL (remembers connections) |
| Default Inbound | DENY ALL (secure) |
| Default Outbound | ALLOW ALL |
| Cost | FREE |
| Changes | Take effect immediately |

## Common Inbound Rules

### Web Server Security Group

```
Inbound Rules:
┌─────────┬──────────┬─────────────────┐
│ Port 80 │ HTTP     │ from 0.0.0.0/0  │
│ Port 443│ HTTPS    │ from 0.0.0.0/0  │
│ Port 22 │ SSH      │ from admin IPs  │
│ Else    │ DENY     │                 │
└─────────┴──────────┴─────────────────┘

Result:
✓ Public can access web server
✓ Admins can SSH in
✗ Database ports blocked
```

### Database Security Group

```
Inbound Rules:
┌────────┬─────────┬──────────────────┐
│ Port   │ Protocol│ Source           │
├────────┼─────────┼──────────────────┤
│ 3306   │ MySQL   │ App SG only      │
│ 22     │ SSH     │ DBA SG only      │
│ Else   │ DENY    │                  │
└────────┴─────────┴──────────────────┘

Result:
✓ Only app servers can query DB
✓ DBA can manage DB
✗ Internet cannot reach DB
```

## Stateful Firewall

Security Groups remember connections:

```
Request: Client → Server on port 80
         ✓ Inbound rule allows port 80

Response: Server → Client on random port (52341)
          ✓ Auto-allowed (stateful)
          No outbound rule needed

Why: AWS tracks "connection state" automatically
```

## Common Port Reference

| Port | Protocol | Use | Default Allow |
|------|----------|-----|---|
| 22 | SSH | Remote login | Admin only |
| 80 | HTTP | Web | Public |
| 443 | HTTPS | Secure web | Public |
| 3306 | MySQL | Database | App tier only |
| 5432 | PostgreSQL | Database | App tier only |
| 6379 | Redis | Cache | App tier only |
| 3389 | RDP | Windows remote | Admin only |

## Security Group Chaining

Reference other security groups:

```
Web SG:
├─ Inbound: 80, 443 from 0.0.0.0/0
└─ Outbound: App SG (all ports)

App SG:
├─ Inbound: 8080 from Web SG ← KEY!
└─ Outbound: Database SG (port 3306)

Database SG:
├─ Inbound: 3306 from App SG ← KEY!
└─ Outbound: None

Benefit: When you add new App instance,
it automatically gets access. No rule updates needed.
```

## 3-Tier Architecture Example

```
User → Internet → IGW → Web SG (port 80)
                          ↓
                       App SG (port 8080)
                          ↓
                    Database SG (port 3306)

Security Layers:
✓ Users see only ports 80/443
✓ App only reaches Database
✓ Database never exposed to internet
✓ Defense in depth
```

## Common Mistakes

### ✗ Mistake 1: Too Permissive
```
Port: 3306 (MySQL)
Source: 0.0.0.0/0 ← Entire internet! ✗

Risk: Database hacked

✅ Fix: Source: 10.0.10.0/24 (App subnet only)
```

### ✗ Mistake 2: Forgot Outbound
```
Inbound: Open ✓
Outbound: DENY ALL ✗

Result: Responses blocked, connections hang

✅ Fix: Default outbound is ALLOW ALL (usually fine)
```

### ✗ Mistake 3: SSH from Anywhere
```
Port 22: Source 0.0.0.0/0 ✗

Risk: SSH brute force attacks

✅ Fix: Source: 203.0.113.0/24 (your office only)
        or use Bastion host
```

## Best Practices

✅ Principle of Least Privilege - Only open what you need
✅ Be Specific - Use CIDR ranges or SG references
✅ Use SG References - Don't hardcode IP addresses
✅ Separate by Function - Web, App, DB get separate SGs
✅ Document Rules - Add descriptions
✅ Regular Audits - Review quarterly

## Limits & Quotas

```
Per Account (Default):
- Security Groups per VPC: 500
- Rules per SG: 120 (60 in + 60 out)
- SGs per instance: 5

Can request increases via AWS Support
```

## Cost

✓ Security Groups: FREE to create and use
✓ Rule changes: FREE and instant
✓ No performance impact
✓ No data transfer charges

## Next Steps

→ [Network ACLs](./nacls.md) - Subnet-level firewall
→ [Subnets](./subnets.md) - Network segmentation
→ [What is VPC](./what-is-vpc.md) - Architecture overview