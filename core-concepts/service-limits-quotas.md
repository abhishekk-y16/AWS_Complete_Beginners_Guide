# Service Limits & Quotas ⚖️

AWS enforces default limits (quotas) to protect customers and the platform. This guide explains where to find limits, common limits to watch, and how to request increases.

## Where to view quotas

- AWS Service Quotas console: Services → Service Quotas
- Billing & Cost Management → Limits summary for some services
- Individual service consoles (e.g., EC2 console shows instance limits)

## Common default limits

- EC2: Varies by instance family and region. Default vCPU quotas per family (e.g., t3, m5) typically start small.
- EBS: Volume size up to 16 TiB; snapshots and throughput limits per account.
- VPC: Default VPCs per region (1), subnets per VPC (200), route table entries, etc.
- Elastic IPs: 5 per region (unused EIPs billed).
- Load Balancers: ALB/NLB quotas per region (varies).
- Lambda: Concurrent executions default 1,000 (account-wide).
- RDS: DB instances per region and total storage limits vary by engine.
- S3: Practically unlimited for objects, but request rate limits and per-object size rules apply.

## How to check your current usage (CLI)

Example: check EC2 vCPU quotas with AWS CLI

```powershell
aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A
```

Or list quotas:

```powershell
aws service-quotas list-service-quotas --service-code ec2
```

## Requesting a quota increase

1. Go to Service Quotas → Select service → Find quota → Request quota increase.
2. Provide desired value, justification, and expected timeframe.
3. AWS reviews and responds (often within 24–72 hours for common increases).

For large changes or enterprise needs, open a Support ticket (Business/Enterprise plans) with details.

## Typical quota increase examples

- Increase Lambda concurrency for bursty workloads.
- Increase EC2 vCPUs for high-scale compute clusters.
- Increase EFS throughput or performance mode quotas.

## Best practices

- Plan ahead: request quota increases before planned launches.
- Use separate accounts for dev/test/prod to avoid hitting shared account limits.
- Monitor usage programmatically via CloudWatch or the Service Quotas API.
- Automate alerts when utilization reaches 80% of a quota.

## Troubleshooting quota errors

- Error: "Instance limit exceeded" → Check vCPU usage, stop unused instances or request increase.
- Error: "Too many buckets" → S3 has a global limit for buckets per account (100 by default); request increase if needed.
- Error: API throttling → Implement exponential backoff and consider Request Rate quotas.

## Links and tools

- Service Quotas console: https://console.aws.amazon.com/servicequotas/
- Quotas API docs: https://docs.aws.amazon.com/service-quotas/
- Support Center: https://console.aws.amazon.com/support/

## Quick checklist

- [ ] Review Service Quotas for critical services
- [ ] Monitor quota usage and set alerts
- [ ] Request increases well before major launches
- [ ] Use multiple accounts for separation of quotas
