# Data Backup

What it is
- Protect data across databases, volumes, and file systems with automated backups and retention.

Recommended stack
- AWS Backup for policies
- S3/Glacier for archive
- Cross-region copy for DR

Quick start
1. Create AWS Backup vault and plan; assign RDS/EBS/EFS/DynamoDB resources.
2. Enable cross-region copy; define retention (e.g., 30/90/365 days).
3. Test restore quarterly.

Cost snapshot
- Backup storage + restore requests; Glacier Deep Archive cheapest for long retention.

Success metrics
- RPO met, restore success rate, backup job success, storage cost trend.