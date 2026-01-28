# Route 53 🌐

Scalable domain name system (DNS) service for domain registration and routing traffic to AWS resources.

## Overview

Route 53 translates domain names (example.com) to IP addresses. Also routes traffic based on health, geography, latency. Amazon's managed DNS + domain registrar.

## DNS Basics

```
You type: example.com
  ↓
Browser asks Route 53: What's the IP?
  ↓
Route 53 responds: 1.2.3.4
  ↓
Browser connects to 1.2.3.4
  ↓
Your website loads!
```

## DNS Records

**A Record**: Maps domain to IPv4
```
example.com  →  1.2.3.4
```

**CNAME Record**: Maps domain to another domain
```
www.example.com  →  example.com
```

**MX Record**: Mail server
```
example.com  →  mail.google.com (receive email)
```

**NS Record**: Name server
```
Delegates DNS to Route 53
```

**TXT Record**: Text data
```
google.com verification code
Sender Policy Framework (SPF)
Domain Keys (DKIM)
```

## Route 53 Features

**Health Checks**: Monitor endpoints
- Check if IP is responding
- Automatic failover if unhealthy
- SMS notifications

**Traffic Policies**: Route traffic intelligently
- Latency-based: Route to nearest region
- Geographic: Route by location
- Weighted: A/B testing (80% to v1, 20% to v2)
- Failover: Active-passive backup

**Domain Registration**: Buy/manage domains
- $9-12 per year
- Automatic renewal
- WHOIS privacy

## Example: Simple Setup

```
Domain: example.com (registered in Route 53)

DNS Record:
example.com  A  3.4.5.6

Website hosted on:
EC2 instance with IP 3.4.5.6

User types: example.com
Route 53 responds: 3.4.5.6
User connects to EC2 instance
```

## Example: Advanced Routing

```
Domain: api.example.com

Routing Policy: Latency-Based

North America users
  ↓
Route 53 checks latency
  ↓
Send to us-east-1 (3ms)

Europe users
  ↓
Route 53 checks latency
  ↓
Send to eu-west-1 (5ms)

Asia-Pacific users
  ↓
Route 53 checks latency
  ↓
Send to ap-southeast-1 (2ms)

Result: Users get closest server!
```

## Health Checks & Failover

```
Primary Server (us-east-1) - IP: 1.2.3.4
  ↓
Route 53 health check (every 30s)
  ↓
Server responding? YES
  ↓
Route traffic to primary

--- Server goes down ---

Health check fails
  ↓
Route 53 detects
  ↓
Automatically route to backup (1.2.3.5)
  ↓
No downtime!
```

## Pricing

```
Hosted Zone: $0.50/month per zone
- Stores DNS records
- Supports unlimited records

Queries:
- First 1B queries: $0.40/million
- Over 1B queries: $0.20/million

Health Checks:
- $0.50 each/month
- CloudWatch alarm: $0.10/alarm

Domain Registration:
- .com: ~$12/year
- .io: ~$45/year
- .net: ~$11/year
- Auto-renewal available

Example: Small company
├─ Hosted zone: $0.50/month
├─ 100M queries: $40/month
├─ 1 health check: $0.50/month
├─ Domain: $1/month (12/12)
└─ Total: ~$42/month
```

## Common Routing Patterns

**Simple Routing**: One resource
```
example.com → EC2 (1.2.3.4)
```

**Weighted Routing**: Distribute traffic
```
example.com
├─ 80% to v1 (1.2.3.4)
└─ 20% to v2 (5.6.7.8)

(A/B testing, gradual rollout)
```

**Latency-Based**: Route to nearest
```
example.com
├─ us-east-1 (1.2.3.4) - 3ms
├─ eu-west-1 (5.6.7.8) - 5ms
└─ ap-southeast-1 (9.10.11.12) - 2ms
```

**Geographic**: Route by location
```
example.com
├─ Europe visitors → CDN in Frankfurt
├─ Asia visitors → CDN in Singapore
└─ Americas visitors → CDN in Virginia
```

**Failover**: Primary + backup
```
Primary (us-east-1) - IP: 1.2.3.4
  OR
Backup (us-west-2) - IP: 5.6.7.8

If primary unhealthy → automatic failover
```

## Real-World Example

```
Global SaaS Platform

Setup:
├─ api.example.com
├─ Servers in: US, EU, Asia
├─ Health checks every 30s
├─ Traffic policy: Latency-based
└─ Auto-failover enabled

Cost: $42/month for DNS

Result:
├─ Fast for global users
├─ Automatic failover
├─ 99.99% uptime
└─ Customer confidence
```

## When to Use Route 53

✅ Need DNS service
✅ Domain registration
✅ Multi-region routing
✅ Health-check failover
✅ Global applications

## When NOT to Use

❌ Simple static DNS (use cheaper providers)
❌ No domain management needed

## Best Practices

✅ Use health checks for critical apps
✅ Enable CloudWatch monitoring
✅ Test failover scenarios
✅ Set TTL appropriately (300-900s)
✅ Use weighted routing for deployments
✅ Document routing policies
✅ Enable DNSSEC for security
✅ Use alias records for AWS resources

## Related Topics

- [What is Route 53](./what-is-route53.md)
- [CloudFront CDN](../cloudfront/what-is-cloudfront.md)
- [Elastic Load Balancer](../networking/elastic-load-balancing/what-is-elb.md)
- [EC2 Hosting](../compute/ec2/what-is-ec2.md)

## Resources

- [Route 53 Documentation](https://docs.aws.amazon.com/route53/)
- [Getting Started](https://docs.aws.amazon.com/route53/latest/developerguide/getting-started-dns.html)
- [Routing Policies](https://docs.aws.amazon.com/route53/latest/developerguide/routing-policy.html)