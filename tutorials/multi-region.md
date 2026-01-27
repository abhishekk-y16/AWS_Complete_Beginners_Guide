# Multi-Region Architecture

TL;DR
- Design for resiliency by duplicating critical services across regions with DNS failover and data replication.

Prerequisites
- Two target regions selected, IaC templates, RTO/RPO defined.

Steps
1. Deploy baseline stack (VPC, security groups, services) in primary and secondary regions using IaC.
2. Data: enable cross-region replication (S3 CRR, DynamoDB global tables, Aurora Global Database, ECR replication).
3. Traffic: use Route 53 health checks + failover/latency records; consider Global Accelerator for TCP/UDP.
4. State: externalize session state (ElastiCache/DynamoDB) replicated where possible.
5. Observability: centralize logs/metrics per region and set cross-region alarms.
6. Drills: run failover tests and document runbooks.

Cost notes
- Doubled infrastructure and data transfer for replication; optimize secondary as warm/standby.

Troubleshooting
- Stale data after failover: check replication lag/status; enable point-in-time recovery.
- DNS not failing over: verify health check endpoints and TTLs.

Checklist
- Replication enabled, DNS failover configured, runbook tested, costs reviewed.