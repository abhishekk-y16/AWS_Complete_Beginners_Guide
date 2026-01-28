# EC2 Security Groups 🛡️

A virtual firewall that controls inbound and outbound traffic to EC2 instances.

## What is a Security Group?

**Security Group** = Instance-level firewall that defines what traffic can reach your EC2.

```
Request from internet
        ↓
Security Group Inbound Rules
(Does security group allow?)
        ↓
EC2 Instance
(If allowed, reaches instance)
        ↓
Instance Outbound Rules
(Can instance send response?)
        ↓
Response back to requester
```

## Key Characteristics

| Property | Details |
|----------|---------|
| Scope | Instance level |
| State | Stateful (remembers connections) |
| Default Inbound | DENY ALL (closed) |
| Default Outbound | ALLOW ALL (open) |
| Cost | FREE |
| Changes | Instant (no restart needed) |

## Common Inbound Rules

### Web Server

```
Port 80 (HTTP)    from 0.0.0.0/0 (public)
Port 443 (HTTPS)  from 0.0.0.0/0 (public)
Port 22 (SSH)     from 203.0.113.0/24 (admins)

Result:
✓ Public can access website
✓ Admins can SSH in
✗ Database ports blocked
```

### Database Server

```
Port 3306 (MySQL) from App SG only
Port 22 (SSH)     from DBA SG only

Result:
✓ Only app servers can query DB
✓ DBA can manage DB
✗ Internet cannot reach DB
```

### Default (No Custom Rules)

```
Inbound: ALL DENIED (most secure)
Outbound: ALL ALLOWED

You must explicitly allow what you need
```

## Creating Inbound Rules

```
Protocol: TCP
Port: 80
Source: 0.0.0.0/0 (anywhere)
Description: Allow HTTP traffic

Or reference another security group:
Protocol: TCP
Port: 8080
Source: web-server-sg (by security group)
```

## Stateful Firewall

```
Request: Client → Server on port 80
Inbound rule: Port 80 allowed? YES ✓

Response: Server → Client on random port (52341)
Outbound: Port 52341 allowed? YES auto-allowed ✓

Why: AWS tracks the connection (stateful)
No need to explicitly allow response ports
```

## Port Reference

| Port | Protocol | Use | Default |
|------|----------|-----|---------|
| 22 | SSH | Remote login | Restricted |
| 80 | HTTP | Web | Public |
| 443 | HTTPS | Secure web | Public |
| 3306 | MySQL | Database | Private |
| 5432 | PostgreSQL | Database | Private |
| 3389 | RDP | Windows remote | Admin only |

## Security Group Chaining

Reference other security groups:

```
Web SG:
  Inbound: 80, 443 from 0.0.0.0/0
  Outbound: App SG

App SG:
  Inbound: 8080 from Web SG ← KEY!
  Outbound: Database SG

Database SG:
  Inbound: 3306 from App SG ← KEY!

Benefit: When you add new app instance,
it automatically gets access. No updates needed.
```

## Best Practices

✅ **Least Privilege** - Only open ports you need
✅ **Be Specific** - Use CIDR ranges or SG references
✅ **Restrict SSH** - Port 22 from your IP only
✅ **Use SG References** - Instead of hardcoding IPs
✅ **Separate by Function** - Web, App, DB each have SG
✅ **Document Rules** - Add descriptions
✅ **Regular Audits** - Review rules quarterly

## Common Mistakes

### ✗ Too Permissive
```
Database port 3306 from 0.0.0.0/0 ✗

Risk: Internet can attack database

✅ Fix: Port 3306 from App SG only
```

### ✗ SSH from Anywhere
```
Port 22 from 0.0.0.0/0 ✗

Risk: Brute force SSH attacks

✅ Fix: Port 22 from your IP only (203.0.113.5/32)
        or use bastion host
```

### ✗ Forgot Outbound
```
Inbound: Open ✓
Outbound: Blocked ✗

Result: Responses can't get out, connections hang

✅ Fix: Default outbound is ALLOW ALL (usually fine)
```

## Creating a Security Group

```
AWS Console:
1. EC2 Dashboard → Security Groups
2. Create Security Group
3. Name: web-server-sg
4. Description: Allow HTTP/HTTPS for web servers
5. VPC: (select your VPC)

Add Inbound Rules:
Rule 1: Port 80, TCP, from 0.0.0.0/0
Rule 2: Port 443, TCP, from 0.0.0.0/0
Rule 3: Port 22, TCP, from 203.0.113.0/24

Outbound Rules: (default ALLOW ALL - usually fine)

Save → Use when launching EC2
```

## Troubleshooting

### Can't Connect to Web Server
```
Check security group:
1. Is port 80 in inbound rules?
2. Source: 0.0.0.0/0 or your IP?
3. Protocol: TCP?

Fix: Add rule for port 80
```

### Can't SSH
```
Check security group:
1. Is port 22 in inbound rules?
2. Source includes your IP?
3. Instance has public IP?

Fix: Add rule for port 22 from your IP
```

## Limits & Quotas

```
Per Account (Default):
- Security Groups per VPC: 500
- Rules per SG: 120 (60 in + 60 out)
- SGs per instance: 5

Can request increases via AWS Support
```

## Cost

✓ Security Groups: FREE
✓ Rule changes: FREE and instant
✓ No performance impact

## Next Steps

→ [VPC Security Groups](../vpc/security-groups.md) - Detailed guide
→ [Key Pairs](./key-pairs.md) - SSH access
→ [Launching Instances](./launching-first-instance.md) - Getting started