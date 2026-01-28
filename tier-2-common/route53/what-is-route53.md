# What is Route 53? 🌐

AWS's DNS and domain management service with health checks and traffic routing.

## Core Concept

**Route 53** manages domain names (DNS) and routes traffic to AWS resources based on various policies.

```
Without Route 53:
├─ Buy domain elsewhere (GoDaddy, etc.)
├─ Manage DNS elsewhere (manual, complex)
├─ No health checks (broken links serve traffic)
├─ No traffic policies (simple round-robin only)
└─ Result: Disconnected, manual, unreliable

With Route 53:
├─ Register domain here
├─ Manage DNS here
├─ Health checks integrated
├─ Intelligent traffic routing
└─ Result: Unified, automated, reliable!
```

## How DNS Works

```
Browser enters: www.example.com
    ↓
1. Looks up IP address (DNS lookup)
    ↓
2. Asks: "What IP for www.example.com?"
    ↓
3. Route 53 responds: "34.82.101.45"
    ↓
4. Browser connects to 34.82.101.45
    ↓
5. Website loads!

Route 53's job: Answer "What IP?" questions
```

## Route 53 Services

### 1. Domain Registration

Register new domains:

```
example.com
├─ Cost: $12/year
├─ Renewal: Automatic or manual
├─ WHOIS privacy: Available
└─ Auto-renewal: Included
```

### 2. DNS Management

Create DNS records:

```
DNS Records:
├─ A Record: example.com → 34.82.101.45 (IPv4)
├─ AAAA Record: example.com → 2001:... (IPv6)
├─ CNAME: www.example.com → example.com
├─ MX: Mail server for email
├─ TXT: Verification records
└─ NS: Name server records
```

### 3. Health Checks

Monitor resource availability:

```
Health Check Setup:
├─ Every 30 seconds: Test endpoint
├─ HTTP request to server
├─ If healthy (200 OK): Route traffic
├─ If unhealthy (timeout/5xx): Stop routing
└─ Result: No traffic to broken servers!
```

### 4. Traffic Management

Intelligent request routing:

```
Routing Policies:
├─ Simple: Round-robin (50/50)
├─ Weighted: Canary (10% new, 90% old)
├─ Latency-based: Route to nearest server
├─ Geolocation: Route by country
├─ Failover: Primary/secondary
└─ Multi-value: Multiple IPs, health-checked
```

## DNS Record Types

### A Record

Maps domain to IPv4 address:

```
example.com → 192.168.1.1

AWS:
├─ Alias to EC2: 192.168.1.1
├─ Alias to ALB: 192.168.1.1
└─ Alias to CloudFront: d123.cloudfront.net
```

### CNAME Record

Alias for domain names (not IP):

```
www.example.com → example.com
api.example.com → api-backend.example.com
cdn.example.com → d123.cloudfront.net
```

### MX Record

Mail server routing:

```
example.com MX:
├─ Priority 10: mail1.example.com
├─ Priority 20: mail2.example.com
└─ Priority 30: mail3.example.com

Lower priority = tried first
```

### TXT Record

Text records for verification:

```
SPF (anti-spam):
example.com TXT: v=spf1 include:_spf.google.com ~all

DKIM (email verification):
default._domainkey.example.com TXT: v=DKIM1; k=rsa; p=MIGfMA0...

DMARC (authentication):
_dmarc.example.com TXT: v=DMARC1; p=reject
```

## Routing Policies

### Simple Routing

```
One resource, one IP:

www.example.com → 192.168.1.1
└─ All traffic goes to same server

Use case: Single web server (not scalable)
```

### Weighted Routing

```
Distribute traffic by percentage:

www.example.com
├─ 90% → old-server (192.168.1.1)
├─ 10% → new-server (192.168.1.2)
└─ Gradually migrate traffic!

Use case: Canary deployments
```

### Latency-Based Routing

```
Route based on lowest latency:

User in New York:
└─ Route to US-East server (lowest latency)

User in Tokyo:
└─ Route to Asia-Pacific server (lowest latency)

AWS measures latency automatically
```

### Geolocation Routing

```
Route based on user location:

User in USA:
└─ Route to US server

User in EU:
└─ Route to EU server (GDPR compliance)

User in China:
└─ Route to Asia server

Use case: Data residency, localization
```

### Failover Routing

```
Primary/Secondary failover:

Primary: prod-lb.example.com
├─ Health check: Every 30 seconds
├─ If healthy: Route all traffic
└─ If unhealthy: Fail over

Secondary: backup-lb.example.com
├─ Takes over immediately
└─ Result: 99.99% availability!
```

### Multi-Value Answer Routing

```
Multiple IPs, all health-checked:

www.example.com returns up to 8 IPs:
├─ 192.168.1.1 (healthy)
├─ 192.168.1.2 (healthy)
├─ 192.168.1.3 (unhealthy - excluded!)
└─ 192.168.1.4 (healthy)

Browser randomly picks from healthy IPs
```

## Health Checks

### HTTP/HTTPS Health Check

```
Route 53 → Every 30 seconds
    ↓
GET http://server.example.com/health
    ↓
Response:
├─ 200 OK: Healthy ✅
├─ 500 Error: Unhealthy ❌
├─ Timeout (>4 seconds): Unhealthy ❌
└─ Connection refused: Unhealthy ❌
```

### CloudWatch Health Check

```
Monitor with CloudWatch alarm:

CloudWatch Alarm:
├─ EC2 Status Check
├─ RDS Status Check
├─ Lambda errors
└─ Custom metric

Route 53 uses alarm state to route traffic
```

### Real-World Example: E-commerce

```
Health Check Setup:

Primary Servers (US-East):
├─ Server A: /health → 200 OK ✅
├─ Server B: /health → 200 OK ✅
├─ Server C: /health → 500 Error ❌

Route 53 Decision:
├─ Server C: Exclude from routing
├─ A + B: Split traffic 50/50
└─ No users hit broken Server C!

User Impact:
└─ Seamless experience (don't notice problem)
```

## Traffic Flow (Visual Policy Creation)

Create complex routing without code:

```
Traffic Flow Policy:

┌─ Geolocation Check
│  ├─ USA → Route to US-East
│  ├─ EU → Route to EU-West
│  └─ Default → Route to US-East
│
├─ Latency Check
│  ├─ Check US-East latency
│  ├─ Check EU-West latency
│  └─ Route to lowest latency
│
├─ Health Check
│  ├─ Is endpoint healthy?
│  ├─ Yes → Route traffic
│  └─ No → Failover
│
└─ Weighted Check
   ├─ 95% primary
   └─ 5% secondary (canary)
```

## Cost Example

```
Monthly costs:

Domain Registration:
├─ .com: $12/year = $1/month
└─ .io: $35/year = $3/month

Hosted Zone:
├─ One zone: $0.50/month
└─ 10 zones: $5/month

Queries:
├─ 1M queries/month: $0.50
├─ 10M queries/month: $5
└─ 100M queries/month: $50

Health Checks:
├─ One check: $0.50/month
├─ 10 checks: $5/month
└─ 50 checks: $25/month

Total (typical): ~$1-15/month
```

## Real-World Example: Disaster Recovery

```
Architecture:

Primary Region (US-East):
├─ Web servers
├─ Database
└─ Everything production

Secondary Region (US-West):
├─ Standby servers
├─ Standby database (RDS read replica)
└─ Hot standby (synced in real-time)

Route 53 Setup:

Primary Health Check → US-East ✅
└─ All traffic routes here normally

Primary Fails:
├─ Primary Health Check → ❌ Fails
├─ Route 53 detects failure
├─ Switches to Secondary Health Check
├─ Traffic now routes to US-West
└─ Result: Service continues (users don't notice!)

RTO (Recovery Time Objective): < 1 minute
RPO (Recovery Point Objective): Seconds

Benefit: 99.99% uptime guarantee!
```

## Common Mistakes

### ✗ Mistake 1: No Health Checks

```
Wrong:
├─ Server crashes
├─ Route 53 still routes traffic there
├─ Users get 503 errors
└─ No automatic failover

Right:
├─ Health check every 30 seconds
├─ Server fails → Excluded immediately
├─ Traffic routes to healthy server
└─ Users experience no downtime
```

### ✗ Mistake 2: Wrong DNS Propagation

```
Wrong:
├─ Change DNS record
├─ Forget TTL (time to live)
├─ Old cached DNS might serve for 24 hours
└─ Users see old site

Right:
├─ Lower TTL before change (300 seconds)
├─ Make DNS change
├─ Wait for propagation (5 minutes)
├─ Increase TTL after change
└─ Instant updates
```

### ✗ Mistake 3: Health Check Misconfiguration

```
Wrong:
├─ Health check points to wrong port
├─ Always returns timeout
├─ Healthy servers marked unhealthy
└─ Traffic never routes!

Right:
├─ Test endpoint before configuring
├─ Verify port and path
├─ Check response code expected
└─ Test failover in staging
```

### ✗ Mistake 4: Ignoring SSL Certificates

```
Wrong:
├─ Health check to HTTPS endpoint
├─ SSL certificate expired
├─ Health check fails
└─ Servers marked unhealthy

Right:
├─ Renew SSL certificates
├─ Test health check with valid cert
├─ Monitor certificate expiration
└─ Alert 30 days before expiry
```

## Best Practices

✅ Enable health checks on all production
✅ Use failover routing for high availability
✅ Set appropriate TTL values (300-3600 seconds)
✅ Monitor DNS query patterns
✅ Test failover regularly
✅ Use traffic flow for complex policies
✅ Enable logging for audit trail
✅ Document routing policies
✅ Set up DNS DNSSEC
✅ Plan for DNS DDoS protection

## CLI Examples

```bash
# Create hosted zone
aws route53 create-hosted-zone \
  --name example.com \
  --caller-reference $(date +%s)

# Create A record
aws route53 change-resource-record-sets \
  --hosted-zone-id Z123456 \
  --change-batch '{
    "Changes": [{
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "www.example.com",
        "Type": "A",
        "TTL": 300,
        "ResourceRecords": [{"Value": "192.168.1.1"}]
      }
    }]
  }'

# Create health check
aws route53 create-health-check \
  --health-check-config IPAddress=192.168.1.1,Port=80,Type=HTTP

# List records
aws route53 list-resource-record-sets \
  --hosted-zone-id Z123456
```

## Next Steps

→ [Advanced Routing Policies](./routing.md) - Complex traffic management
→ [Health Checks Deep Dive](./health-checks.md) - Reliability
→ [DNSSEC & Security](./security.md) - Protect your DNS