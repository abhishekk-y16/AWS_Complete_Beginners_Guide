# S3 Versioning 📚

Keep multiple versions of files. Restore deleted or corrupted objects instantly.

## What is Versioning?

**Versioning** = S3 keeps every version of every object you upload. Delete an object? You can restore it.

## How Versioning Works

```
Without Versioning:
Document.pdf (v1)
  ↓ (overwrite)
Document.pdf (v2) ← Original v1 lost
  ↓ (delete)
(File gone, can't recover)

With Versioning:
Document.pdf version-id-1 (v1)
Document.pdf version-id-2 (v2)
Document.pdf version-id-3 (deleted marker)

Result: Can restore any version anytime
```

## Enabling Versioning

```
AWS Console:
1. S3 → Select bucket
2. Properties → Versioning
3. Enable Versioning
4. Click Save

Cost: Applies immediately
Storage: All versions consume space
```

## Version States

### Enabled
```
Behavior:
- Each upload gets unique version ID
- Old versions kept automatically
- Delete creates delete marker
- Can restore any version

Storage: All versions count toward quota
Cost: Multiplied by number of versions
```

### Suspended
```
Behavior:
- New uploads get "null" version
- Old versions still exist
- Deletes work normally
- Can restore old versions, not new ones

Use case: Turn off versioning but keep history
```

## Storage Cost Impact

```
Without Versioning:
File uploaded 100 times, each 10 MB
Total storage: 10 MB (last version only)
Cost: 10 MB × $0.023/GB = $0.00023

With Versioning (100 versions):
Total storage: 1000 MB (all versions)
Cost: 1000 MB × $0.023/GB = $0.023

Increase: 100x more expensive!
But: Safety against accidental deletion
```

## Cost Optimization with Lifecycle

```
Day 0: Keep all versions (STANDARD)
Day 30: Move old versions to IA
Day 90: Move old versions to GLACIER
Day 365: Delete old versions

Benefit: History + low cost
```

## Common Use Cases

### Critical Application Config
```
app-config.json versioned:
- Upload new config
- Issue found
- Restore previous version instantly
- Disaster averted!

Cost: Worth paying for safety
```

### Database Backups
```
database-backup.sql
- Daily upload
- 30 versions kept
- Restore any day in last month

Security: Protection against corruption
```

## MFA Delete Protection

```
Extra security: Require MFA to delete versions

Benefit: Prevent accidental permanent deletion
Cost: Minimal (just MFA requirement)
```

## Best Practices

✅ Enable versioning for critical data
✅ Use lifecycle rules to manage costs
✅ Set version expiration
✅ Monitor storage usage
✅ Use MFA delete for safety
✅ Test restoration procedures
✅ Document retention policies

## Limitations

```
Versioning does NOT protect against:
- Malware/ransomware (encrypts all versions)
- Accidental bucket deletion
- AWS account compromise

Use with:
- Bucket replication (separate account)
- Regular off-site backups
- IAM policies (prevent deletion)
```

## Next Steps

→ [Lifecycle Rules](./lifecycle-rules.md) - Auto-manage versions
→ [Access Control](./access-control.md) - Prevent deletion
→ [Storage Classes](./storage-classes.md) - Cost optimization