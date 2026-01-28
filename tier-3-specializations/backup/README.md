# AWS Backup 🔐

Centralized, policy-based backup service for protecting data across AWS services.

## Overview

AWS Backup simplifies backup management. Instead of configuring backups separately for each service (RDS, EBS, DynamoDB, etc.), use one central service with unified policies. Automatic backups, compliance enforcement, and cross-region replication.

## Key Features

- ✅ Unified backup management across all AWS services
- ✅ Automated backup scheduling (daily, weekly, monthly)
- ✅ Lifecycle policies (move old backups to Glacier for cost savings)
- ✅ Point-in-time recovery capabilities
- ✅ Cross-region replication for disaster recovery
- ✅ Compliance and audit trail

## Supported Services

- RDS, Aurora, DynamoDB
- EBS volumes, EFS
- FSx, Storage Gateway
- AWS Backup Appliance (on-premises)

## How It Works

1. Create backup plan (schedule + retention)
2. Assign resources to plan
3. AWS Backup automatically takes snapshots
4. Manage retention with lifecycle policies
5. Restore from any backup when needed

## Pricing

- Storage: $0.05/GB/month
- Backup requests: $0.50 per request
- Example: 100GB database, daily backups = ~$150/month

## Best Practices

✅ Create backup plans per workload type
✅ Use lifecycle policies for cost optimization
✅ Test recovery regularly
✅ Enable cross-region replication for critical data
✅ Set retention policies based on compliance needs

## Next Steps

→ [AWS Backup Documentation](https://docs.aws.amazon.com/aws-backup/)
→ [Pricing Calculator](https://aws.amazon.com/backup/pricing/)
→ [Getting Started](https://console.aws.amazon.com/backup/)