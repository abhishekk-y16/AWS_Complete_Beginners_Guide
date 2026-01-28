# S3 Storage Classes 💾

Choose the right storage class based on access patterns and cost.

## Storage Classes Overview

| Class | Cost | Retrieval | Best For |
|-------|------|-----------|----------|
| STANDARD | $0.023/GB | Instant | Frequent access |
| INTELLIGENT-TIERING | $0.0125-0.023/GB | Varies | Unknown patterns |
| STANDARD-IA | $0.0125/GB | Instant | Infrequent access |
| ONEZONE-IA | $0.01/GB | Instant | Infrequent, single AZ |
| GLACIER Flexible | $0.004/GB | Hours | Long-term backup |
| GLACIER Instant | $0.006/GB | Instant | Archive with fast retrieval |
| DEEP_ARCHIVE | $0.00099/GB | 12+ hours | 7+ year retention |

## STANDARD (Default)

**For**: Frequently accessed data (websites, applications)

```
Characteristics:
- Millisecond retrieval
- Multiple AZ redundancy
- 11 nines durability
- No retrieval fees

Cost Example:
100 GB/month: $2.30
1 TB/month: $23

When to use: Active data, databases, websites
```

## STANDARD-IA (Infrequent Access)

**For**: Data accessed < once per month

```
Characteristics:
- Lower storage cost
- Instant retrieval
- Minimum 30-day storage period
- Minimum 128 KB object size
- Retrieval fees ($0.01 per GB)

Cost Example (100 GB, 1 retrieval):
Storage: $1.25
Retrieval (100 GB): $1.00
Total: $2.25 (vs $2.30 STANDARD)

Break-even: Similar to STANDARD
When to use: Occasional access needed, instant retrieval
```

## INTELLIGENT-TIERING

**For**: Unknown or changing access patterns

```
How it works:
- Automatic tiering based on access
- Frequently accessed: STANDARD cost
- Infrequent access: IA cost (after 30 days)
- Archive: Cheap cost (after 90 days)
- Deep Archive: Cheapest (after 180-270 days)

Cost: Monitoring fee $0.0025/1,000 objects

Benefit: Automatic optimization (no manual moves)
When to use: Unpredictable access patterns
```

## ONEZONE-IA

**For**: Data you can reproduce if lost (backups, logs)

```
Characteristics:
- Single Availability Zone (risky!)
- Lowest cost of all classes
- Instant retrieval
- Minimum 30-day storage

Cost Example:
100 GB: $1.00/month (cheaper than IA)

Trade-off: Lose all data if AZ fails
When to use: Reproducible data, cost-sensitive
```

## GLACIER Flexible Retrieval

**For**: Long-term backup (3-5+ years)

```
Characteristics:
- Retrieval time: Hours (3-5+ hours)
- Instant (expedited): Minutes (expensive)
- Cheapest option for archive
- Minimum 90-day storage period

Cost Example (1 TB backup):
Storage: $4/month
Retrieval (1 TB, expedited): $50
Total: $54

When to use: Cold storage, disaster recovery, archives
```

## GLACIER Instant Retrieval

**For**: Archive needing occasional fast access (quarterly review)

```
Characteristics:
- Retrieval time: Milliseconds
- More expensive than Flexible
- Less than IA
- Minimum 90-day storage

Cost:
Storage: $6/month (between IA and Flexible)
Retrieval: Instant (no extra cost)
```

## DEEP_ARCHIVE

**For**: Extreme long-term retention (7-10+ years, compliance)

```
Characteristics:
- Retrieval time: 12+ hours
- Ultra-cheap storage
- Minimum 180-day storage
- Compliance archives

Cost Example (1 TB/year for 7 years):
STANDARD-IA: $126/year × 7 = $882 total
DEEP_ARCHIVE: $12/year × 7 = $84 total
Savings: $798!

When to use: Regulatory compliance, long-term archives
```

## Choosing Your Class

### Decision Tree

```
Access frequency?
├─ Multiple times per day/week
│  └─ STANDARD ($0.023/GB)
│
├─ Monthly or less
│  └─ Access speed critical?
│     ├─ Yes: STANDARD-IA ($0.0125/GB)
│     └─ No: GLACIER Flexible ($0.004/GB)
│
└─ Unknown pattern
   └─ INTELLIGENT-TIERING (auto-tiering)
```

## Cost Comparison Examples

### Scenario 1: Website Static Content

```
10 GB frequently accessed

STANDARD: $0.23/month
INTELLIGENT-TIERING: $0.23/month + monitoring fee

Choice: STANDARD (simpler)
```

### Scenario 2: Monthly Database Backup

```
500 GB, accessed 1x per month (restore test)

STANDARD-IA: $6.25 storage + $0 retrieval = $6.25
GLACIER: $2 storage + $5 retrieval = $7

Choice: STANDARD-IA (predictable access)
```

### Scenario 3: Archive 10 Years of Logs

```
500 TB total, never accessed

DEEP_ARCHIVE: $0.50/month × 120 = $60 total
GLACIER: $2.00/month × 120 = $240 total
STANDARD: $11.50/month × 120 = $1,380 total

Savings with DEEP_ARCHIVE: $1,320!
```

### Scenario 4: Mixed Access

```
1 TB total:
- 100 GB hot (weekly access): STANDARD
- 400 GB warm (monthly): INTELLIGENT-TIERING
- 500 GB cold (annual): GLACIER

Cost: $2.30 + $5 + $2 = $9.30/month
```

## Lifecycle Policies (Auto-tiering)

Automatically move objects between classes:

```
Day 0: Upload to STANDARD ($0.023/GB)
Day 30: Move to STANDARD-IA ($0.0125/GB)
Day 90: Move to GLACIER ($0.004/GB)
Day 365: Delete

Benefit: Optimal cost automatically
```

## Retrieval Costs by Class

| Class | Retrieval Time | Cost |
|-------|---|---|
| STANDARD | Instant | FREE |
| STANDARD-IA | Instant | $0.01/GB |
| GLACIER Flexible | Hours | $0.03/GB |
| GLACIER Instant | Instant | FREE |
| DEEP_ARCHIVE | 12+ hours | $0.02/GB |

## Best Practices

✅ Use STANDARD for active data
✅ Use STANDARD-IA for infrequent access
✅ Use GLACIER for backups
✅ Use DEEP_ARCHIVE for compliance
✅ Use INTELLIGENT-TIERING if unsure
✅ Set up lifecycle policies
✅ Monitor access patterns
✅ Review quarterly

## Next Steps

→ [Versioning](./versioning.md) - Keep file history
→ [Lifecycle Rules](./lifecycle-rules.md) - Auto-transition
→ [Access Control](./access-control.md) - Security