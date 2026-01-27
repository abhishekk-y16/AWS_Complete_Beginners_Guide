# Backup & Restore

TL;DR
- Use automated backups and cross-region replication for critical data.
- Use AWS Backup to centralize backup policies for EBS, RDS, DynamoDB, and EFS.

Prerequisites
- IAM role with backup permissions and target storage (S3 or backup vaults).

Steps
1. Configure AWS Backup plan and assign resource assignments for RDS/EBS/DynamoDB.
2. Enable point-in-time recovery for supported services (RDS, DynamoDB).
3. Configure cross-region/ cross-account copy for disaster recovery.
4. Test restores regularly and document RTO/RPO.

Cost notes
- Backup storage and cross-region copies incur S3/backup vault costs; balance frequency with RPO.

Troubleshooting
- Restore failures: check IAM permissions, restore target VPC/subnet availability.

Checklist
- Backup plans defined, cross-region copies enabled, restore tests passed.
