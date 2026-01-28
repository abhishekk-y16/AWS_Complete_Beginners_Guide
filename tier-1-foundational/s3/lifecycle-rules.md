# S3 Lifecycle Rules ⏰

Automatically manage object lifecycle (transition, expire) to optimize costs.

## What is a Lifecycle Rule?

A **lifecycle rule** automatically transitions objects between storage classes or deletes them based on age.

## How Lifecycle Works

```
Day 0: Upload to STANDARD ($0.023/GB)
       ↓ (30 days later)
Day 30: Auto-move to STANDARD-IA ($0.0125/GB)
        ↓ (90 days later)
Day 120: Auto-move to GLACIER ($0.004/GB)
         ↓ (365 days later)
Day 485: Auto-delete (permanent)

Result: Optimal cost automatically!
```

## Key Lifecycle Actions

### Transition
```
Move object between storage classes:
- STANDARD → STANDARD-IA (after 30 days)
- STANDARD-IA → GLACIER (after 90 days)
- GLACIER → DEEP_ARCHIVE (after 180 days)
- Or delete

Minimum transition periods:
- To IA: 30 days
- To GLACIER: 90 days
- To DEEP_ARCHIVE: 180 days
```

### Expiration
```
Automatically delete objects:
- Delete after X days
- Delete incomplete multipart uploads

Example:
- Log files: Delete after 90 days
- Temp backups: Delete after 30 days
- Unfinished uploads: Clean after 7 days
```

## Creating a Lifecycle Rule

### Scenario: Application Logs

```
Requirement:
- Keep recent logs in STANDARD (instantly searchable)
- Move old logs to GLACIER (backup)
- Delete very old logs (90 days+)

Rule:
├─ Apply to: Objects with prefix "logs/"
├─ Transition to STANDARD-IA: 30 days
├─ Transition to GLACIER: 90 days
└─ Delete: 365 days
```

### Scenario: Database Backups

```
Requirement:
- Keep daily backups for 30 days
- Keep weekly backups for 1 year
- Keep yearly backups permanently

Rule 1 (daily):
├─ Apply to: prefix "backups/daily/"
├─ Transition to GLACIER: 30 days
└─ Delete: 31 days

Rule 2 (weekly):
├─ Apply to: prefix "backups/weekly/"
└─ Transition to GLACIER: 1 day
```

## Lifecycle Filter Options

### By Object Key Prefix
```
Prefix "logs/":
- logs/2024-01-01.log ✓
- logs/2024-01-02.log ✓
- archived/2024-01-01.log ✗

Applied to: All objects matching prefix
```

### By Tag
```
Tag "Retention: short":
- Only objects with this tag
- Exclude objects without tag

Useful: Mix retention policies in same bucket
```

### By Object Size
```
Size > 1 GB:
- Apply rule only to large objects
- Exclude smaller files

Example: Move large logs to archive, keep small recent files
```

### By Current Storage Class
```
Apply only if currently in: STANDARD
- Skip already archived objects
- Avoid unnecessary transitions

Efficient: Transitions only when needed
```

## Common Lifecycle Patterns

### Pattern 1: Short-Term + Archive

```
Rule:
├─ Transition to IA: 30 days
├─ Transition to GLACIER: 90 days
└─ Delete: 365 days

Cost: Cheap long-term storage
Use case: Backup retention policies
```

### Pattern 2: Hot + Cold Storage

```
Rule:
├─ Keep in STANDARD: 0-7 days
├─ Move to GLACIER: 7 days
└─ Delete: 2555 days (7 years)

Cost: Low for archives
Use case: Compliance storage
```

### Pattern 3: Intelligent Auto-tiering

```
Rule:
├─ Use INTELLIGENT-TIERING: Immediate
├─ Auto-archives after: 90 days
└─ Delete: 2555 days

Cost: Automatic optimization
Use case: Unknown access patterns
```

### Pattern 4: Development/Testing

```
Rule:
├─ Prefix: "dev/"
├─ Delete: 7 days

Cost: Minimal (short-lived)
Use case: Test artifacts, logs
```

## Combining with Versioning

### With Versioning Enabled

```
Lifecycle can target:
- Current version
- Non-current versions

Example:
├─ Current version: Keep 90 days
├─ Non-current versions: Keep 30 days
└─ Then delete

Benefit: Controlled version history
```

### Cost Example

```
File edited daily for 90 days:
Without lifecycle: 90 versions × 1MB = 90MB
Cost: 90MB × $0.023 = $2.07

With lifecycle:
├─ Current: Keep 90 days
├─ Old: Delete after 30 days
Result: ~35 versions × 1MB = 35MB
Cost: 35MB × $0.023 = $0.81

Savings: 60%
```

## Incomplete Multipart Upload Cleanup

```
Problem:
- Large uploads sometimes fail mid-transfer
- Partial uploads left in bucket
- Consume storage but are useless

Solution:
Lifecycle rule: Delete incomplete uploads after 7 days

Rule:
└─ Delete incomplete uploads: 7 days

Effect:
- Automatic cleanup
- Saves storage
- No manual intervention
```

## Common Mistakes

### ✗ Mistake 1: Can't Transition Backward
```
Wrong: GLACIER → STANDARD (not allowed)

Correct: Only forward transitions
STANDARD → IA → GLACIER → DEEP_ARCHIVE

If you need recent versions: Use versioning
```

### ✗ Mistake 2: Minimum Days Not Met
```
Wrong:
├─ Transition to IA: 15 days (minimum is 30)
└─ Result: Rule ignored!

Correct:
└─ Transition to IA: 30 days (minimum)
```

### ✗ Mistake 3: Over-aggressive Deletion
```
Wrong:
└─ Delete all objects: 7 days

Risk: Lost important backups!

Correct:
└─ Delete test files: 7 days
└─ Delete production backups: 365 days
```

## Lifecycle Configuration Example

```
Bucket: my-app-backups

Rule 1: Recent backups
├─ Prefix: "backups/"
├─ Transition to IA: 30 days
├─ Transition to GLACIER: 90 days
└─ Delete: 365 days

Rule 2: Test files
├─ Tag: environment=test
├─ Delete: 7 days

Rule 3: Cleanup uploads
└─ Delete incomplete: 7 days
```

## Monitoring Lifecycle

```
CloudWatch:
- Monitor transitions
- Track deleted objects
- Alert if rules fail

Cost Explorer:
- See savings from tiering
- Verify cost reduction

CLI:
aws s3api get-bucket-lifecycle-configuration \
  --bucket my-bucket
```

## Cost Estimation

### Without Lifecycle
```
1 TB uploaded daily, never deleted:
365 TB per year
Cost: 365 × $23 = $8,395/year
```

### With Lifecycle
```
Same scenario:
- Recent 30 days: 30 GB × $0.023 = $0.69
- Months 2-3: 60 GB × $0.0125 = $0.75
- Months 4+: 275 GB × $0.004 = $1.10
Total/month: ~$2.54
Annual: ~$30!

Savings: 99.6% (from $8,395 to ~$30)
```

## Best Practices

✅ Define clear retention policies
✅ Use lifecycle for cost optimization
✅ Clean up incomplete uploads
✅ Test rules in dev first
✅ Monitor transitions
✅ Combine with versioning
✅ Document policies
✅ Review annually

## Next Steps

→ [Storage Classes](./storage-classes.md) - Choose right class
→ [Versioning](./versioning.md) - Keep file history
→ [Access Control](./access-control.md) - Security