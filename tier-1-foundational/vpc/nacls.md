# Network Access Control Lists (NACLs) 📋

A **Network ACL** is a firewall at the **subnet level** that controls inbound and outbound traffic for ALL instances in that subnet. Like a security gate at the building entrance.

## Security Groups vs NACLs

| Property | Security Groups | NACLs |
|----------|---|---|
| Scope | Instance level | Subnet level |
| Applies To | Individual EC2 | All instances in subnet |
| State | STATEFUL | STATELESS |
| Default Inbound | DENY ALL | ALLOW ALL |
| Default Outbound | ALLOW ALL | ALLOW ALL |
| Rule Evaluation | All rules checked | Rule # order (first match wins) |
| Rule Limit | 60 rules | 20 rules |
| Cost | FREE | FREE |

## Key Difference: Stateful vs Stateless

### 🔄 Security Groups (Stateful)
```
Inbound Rule: Allow port 80

Request: Client → EC2 (port 80) ✓
Response: EC2 → Client (port 52341) ✓ Auto-allowed

Why: AWS remembers the connection
```

### 📋 NACLs (Stateless)
```
Inbound Rule: Allow port 80

Request: Client → Subnet (port 80) ✓ Inbound rule allows
Response: Subnet → Client (port 52341) ✗ No outbound rule!

Why: NACL must check BOTH directions

✅ Solution: Add outbound rule for ephemeral ports (1024-65535)
```

## NACL Rule Evaluation

Rules are checked by **rule number**, not alphabetically:

```
Inbound Rules (evaluated in order):

Rule 100: Allow port 80 (HTTP)
Rule 110: Allow port 443 (HTTPS)
Rule 120: Allow port 22 (SSH)
Rule 32767: DENY ALL (implicit, always last)

How traffic is evaluated:
1. Incoming request on port 80
2. Check rule 100: Is it port 80? YES → ALLOW (STOP)

3. Incoming request on port 3306
4. Check rule 100: Is it port 80? NO → Continue
5. Check rule 110: Is it port 443? NO → Continue
6. Check rule 120: Is it port 22? NO → Continue
7. Check rule 32767: DENY (default catch-all)

⚠️  Rule 32767 always exists and DENIES by default
```

## Default NACL

```
New VPC default NACL:

Inbound:
Rule 100: Allow ALL traffic

Outbound:
Rule 100: Allow ALL traffic

Effect: Everything allowed (permissive by default)
```

## Example: Web Server NACL

### Inbound Rules (Allow Web Traffic)

```
┌─────────┬──────────┬────────────┬─────────────┐
│ Rule #  │ Protocol │ Port Range │ Source      │
├─────────┼──────────┼────────────┼─────────────┤
│ 100     │ TCP      │ 80         │ 0.0.0.0/0   │
│ 110     │ TCP      │ 443        │ 0.0.0.0/0   │
│ 120     │ TCP      │ 22         │ 203.0.113/24│
│ 32767   │ ALL      │ ALL        │ 0.0.0.0/0   │ DENY
└─────────┴──────────┴────────────┴─────────────┘

Traffic Analysis:
- HTTP request on port 80 → Rule 100 ✓ ALLOW
- SSH from admin → Rule 120 ✓ ALLOW
- Port 3306 (MySQL) → Rule 32767 ✗ DENY
```

### Outbound Rules (Allow Responses)

```
┌─────────┬──────────┬────────────┬─────────────┐
│ Rule #  │ Protocol │ Port Range │ Destination │
├─────────┼──────────┼────────────┼─────────────┤
│ 100     │ TCP      │ 1024-65535 │ 0.0.0.0/0   │
│ 110     │ TCP      │ 80, 443    │ 0.0.0.0/0   │
│ 32767   │ ALL      │ ALL        │ 0.0.0.0/0   │ DENY
└─────────┴──────────┴────────────┴─────────────┘

Why Rule 100 (Ephemeral Ports)?
When client connects on port 80:
- Server responds on ephemeral port (1024-65535)
- Outbound rule 100 allows this ✓
```

## Ephemeral Ports Explained

```
Well-Known Ports (1-1023):
80 = HTTP
443 = HTTPS
22 = SSH
3306 = MySQL

Ephemeral Ports (1024-65535):
- Clients get random port for each connection
- Client 203.0.113.5:52341 → Server 54.12.34.56:80
                 ↑ random high port

Server Response:
Server 54.12.34.56:80 → Client 203.0.113.5:52341
                                           ↑ same port

⚠️ NACLs must allow both sides!
```

## Common Mistakes

### ✗ Mistake 1: Wrong Rule Order
```
Rule 100: DENY ALL 0.0.0.0/0 ← Blocks everything!
Rule 110: Allow 80 0.0.0.0/0 ← Never reached!

Result: All traffic blocked

✅ Fix: Put ALLOW rules before DENY rules
Rule 100: Allow 80, 443, 22
Rule 200: DENY ALL
```

### ✗ Mistake 2: Forgot Ephemeral Ports
```
Inbound: Allow 80 ✓
Outbound: Allow 22 only ✗

Problem: Responses on port 80 use ephemeral (1024+)
         but outbound rule blocks them

✅ Fix: Outbound rule 100: Allow 1024-65535
```

### ✗ Mistake 3: Too Restrictive
```
Rule 100: Allow 80 from 203.0.113.1/32 (single IP)

Result: Works for one person, everyone else blocked

✅ Fix: Use broader CIDR or 0.0.0.0/0
```

### ✗ Mistake 4: Conflict with Security Group
```
NACL: Allow port 80 ✓
Security Group: DENY port 80 ✗

Result: BOTH must allow → Traffic BLOCKED
(Most restrictive rule wins)

✅ Fix: Ensure both allow
```

## When to Use NACLs

✓ Subnet-level blocking (entire subnet under attack)
✓ Deny specific IP ranges or ports
✓ Additional layer beyond security groups
✓ Compliance requirements

✗ Day-to-day access control (use Security Groups)
✗ High-frequency rule changes (use Security Groups)

## Numbering Best Practices

```
Rule Numbers (by 10s - leaves gaps):
Rule 100: High-priority allows
Rule 110: Secondary allows
Rule 120: Specific cases
Rule 200: More allows if needed
Rule 32767: Default DENY (built-in)

Benefits:
- Easy to insert new rules
- Clear priority
- No renumbering needed
```

## Real-World Example: Multi-Tier

```
PUBLIC SUBNET NACL (10.0.1.0/24):
Inbound:  Allow 80, 443, 22 from specific ranges
Outbound: Allow 1024-65535 (responses)
          Allow 3306 to private subnet
          Allow 443 to internet (APIs)

PRIVATE SUBNET NACL (10.0.10.0/24):
Inbound:  Allow 8080 from public subnet
          Allow 22 from bastion
Outbound: Allow 1024-65535 to public
          Allow 443 to internet (updates)

PRIVATE DB SUBNET NACL (10.0.20.0/24):
Inbound:  Allow 3306 from app subnet
          Allow 22 from bastion
Outbound: Allow 1024-65535 back to app
```

## Cost & Performance

✓ NACLs: FREE to create and use
✓ Rule changes: Instant
✓ No performance impact
✓ No data transfer charges

## Best Practices

✅ Start with default NACL (allows all)
✅ Number rules by 10s (leave gaps)
✅ Allow ephemeral ports (1024-65535)
✅ Rule 32767 always DENY (don't add)
✅ Combine with Security Groups (defense in depth)
✅ Document rule purposes
✅ Keep it simple - NACLs are a secondary tool

## Next Steps

→ [Security Groups](./security-groups.md) - Instance firewall
→ [Subnets](./subnets.md) - Network segmentation
→ [What is VPC](./what-is-vpc.md) - Architecture overview