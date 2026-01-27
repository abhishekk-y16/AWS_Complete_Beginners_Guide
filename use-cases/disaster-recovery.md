# Disaster Recovery

What it is
- Keep services running during region or AZ failures with backups and replication.

Strategies
- Backup/restore (hours+), pilot light (minimal standby), warm standby, active-active.

Recommended stack
- S3/Glacier + AWS Backup, RDS/Aurora cross-region replicas, DynamoDB global tables, Route 53 failover.

Quick start
1. Choose RTO/RPO; map workloads to strategy (pilot light vs active-active).
2. Enable cross-region replication and backups; script infra via IaC.
3. Configure Route 53 health checks and failover records; run failover drills.

Cost snapshot
- Increases with standby duplication; start with pilot light to control cost.

Success metrics
- RTO/RPO achieved in drills, failover time, data loss window.