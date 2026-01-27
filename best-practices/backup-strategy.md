# AWS Backup Strategy 🔄

How to protect your data and ensure business continuity.

## Backup Fundamentals

### What to Backup
- **Databases:** RDS, DynamoDB, MongoDB
- **Filesystems:** EBS volumes, EFS
- **Objects:** S3 buckets, archive to Glacier
- **Configuration:** CloudFormation templates, configs
- **Code:** GitHub repos, CodeCommit repositories

### The 3-2-1 Rule
- **3** copies of data (original + 2 backups)
- **2** different storage media (disk + cloud)
- **1** offsite copy (different region/account)

## RDS Backups

### Automated Backups
```
RDS → Database → Backup and restore
Backup retention: 7 days (default)
Backup window: 03:00 UTC (configure)
```

**Restore from automated backup:**
- Point-in-time recovery (5 minute precision)
- Instant restore (takes 1-5 minutes)
- New database created

### Manual Snapshots
```
RDS → Snapshots → Snapshot DB instance
- Copy snapshot to different region
- Long-term retention (years)
```

**Cost:** $0.095/GB/month (much cheaper than running DB)

### Best Practices
- ✅ Set retention to 30 days (1 week = too short)
- ✅ Copy snapshots to backup region monthly
- ✅ Test restore process quarterly
- ✅ Enable backup encryption
- ✅ Enable copy to secondary region for DR

## EBS Volume Backups

### Snapshots
```
EC2 → Snapshots → Create Snapshot
- Point-in-time copy of volume
- Incremental (only changed blocks)
- Store in S3 (behind scenes)
```

### Lifecycle Policy
```
Data Lifecycle Manager → Create lifecycle policy
Schedule: Daily at 2:00 AM
Retention: Keep 30 snapshots
Tags: Automatically tag snapshots
```

**Cost:** $0.05 per snapshot (incremental)

### Restore Volume
```
Snapshots → [Snapshot] → Create Volume
- Same or different region
- Attach to instance
- Restore takes 1-10 minutes
```

## S3 Backups

### Versioning
```
S3 Bucket → Properties → Versioning
Enable versioning
- Keep all file versions
- Recover deleted files
- Protects against accidental overwrites
```

### Cross-Region Replication
```
S3 Bucket → Replication rules
Destination: Bucket in different region
All objects replicated automatically
```

**Use for:**
- Disaster recovery
- Data residency requirements
- Lower latency for global users

**Cost:** Data transfer between regions (~$0.02/GB)

### Lifecycle Policies
```
S3 → Lifecycle rules
- 30 days → Move to Glacier ($0.004/GB)
- 90 days → Move to Deep Archive ($0.00099/GB)
- 1 year → Delete
```

**Cost Savings:** 99% reduction for old data

## DynamoDB Backups

### On-Demand Backups
```
DynamoDB → Backups → Create Backup
- Full backup of table
- Zero impact on performance
- Backup size = table size
```

### Point-in-Time Recovery
```
DynamoDB Table → Backup/Restore → Enable PITR
- Automatic backups every 5 minutes
- Recover to any point in last 35 days
- No cost for backup storage (included)
```

## Lambda Backup

### Source Code
```
# Use CodeCommit or GitHub
Git repository → Backup (free with GitHub)

# Or export from Lambda
AWS CLI: aws lambda get-function --function-name my-func
```

### Environment Variables
```
# Export configuration
Lambda Console → Copy environment variables
Store in secure file or Secrets Manager
```

## Backup Automation

### AWS Backup Service
```
AWS Backup → Create Backup Plan
Resources: Select services to backup
Schedule: Daily at 3 AM
Retention: 30 days
Copy to region: us-west-2
```

**Supports:**
- EC2 volumes (EBS)
- RDS databases
- DynamoDB tables
- EFS filesystems
- AWS Storage Gateway

**Cost:** $0.50/GB backed up + $0.10/recovery

### Example: Complete Backup Plan
```json
{
  "BackupPlanName": "CompanyBackup",
  "Rules": [
    {
      "RuleName": "DailyBackup",
      "TargetBackupVault": "daily",
      "ScheduleExpression": "cron(0 3 * * ? *)",
      "StartWindowMinutes": 60,
      "CompletionWindowMinutes": 180,
      "Lifecycle": {
        "DeleteAfterDays": 30,
        "MoveToColdStorageAfterDays": 7
      },
      "RecoveryCopyRegions": ["us-west-2"]
    }
  ]
}
```

## Testing Your Backups

### ✅ Monthly Backup Test
```
1. Restore backup to test environment
2. Verify data integrity
3. Check all critical records exist
4. Document restore time
5. Verify restore is in working state
```

### ✅ Disaster Recovery Drill
```
1. Simulate region failure
2. Switch to backup region
3. Verify service is running
4. Measure RTO (Recovery Time Objective)
5. Document any issues
```

## Cost Optimization

| Strategy | Savings | Implementation |
|----------|---------|-----------------|
| Incremental snapshots | 60% | Automatic in AWS |
| Tiered retention | 70% | 30d full + 1y archive |
| Regional compression | 50% | Glacier for old data |
| Deduplication | 40% | S3 versioning |

## Backup Checklist

🔴 **CRITICAL**
- ✅ Database automated backups enabled
- ✅ Cross-region backup copy
- ✅ Point-in-time recovery tested

🟠 **HIGH**
- ✅ EBS snapshots automated
- ✅ S3 versioning enabled
- ✅ Backup retention policy documented

🟡 **IMPORTANT**
- ✅ Lambda code in git repository
- ✅ Configuration backed up
- ✅ Monthly restore test scheduled

## 📖 Related Resources

- [AWS Backup Documentation](https://aws.amazon.com/backup/)
- [RDS Documentation](../tier-1-foundational/rds/README.md)
- [Disaster Recovery Guide](disaster-recovery.md)
- [Cost Optimization](cost-optimization.md)