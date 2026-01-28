# Glacier 🧊

Long-term archival storage for compliance, regulatory, and backup data retention.

## Overview

Glacier is ultra-low-cost storage for data accessed rarely (years apart). Automatic archival from S3 lifecycle policies. Compliance-grade: WORM (Write-Once-Read-Many), encryption, audit logging. Retrieval takes 1-12 hours.

## Key Features

- ✅ 99.999999999% durability (11 nines)
- ✅ Extremely low cost ($0.004/GB/month)
- ✅ Automatic archival from S3
- ✅ Lifecycle policies for data transitions
- ✅ MFA delete protection
- ✅ Encryption by default

## Storage Classes

- **Glacier Instant Retrieval**: 1-3 minutes retrieval
- **Glacier Flexible Retrieval**: 1 minute to 12 hours
- **Deep Archive**: 12 hours retrieval
- **Deep Archive (DIY)**: Manual retrieval

## Retrieval Tiers

| Tier | Speed | Cost Multiplier |
|------|-------|---|
| Expedited | 1-5 minutes | 10x |
| Standard | 3-5 hours | 1x (base) |
| Bulk | 5-12 hours | 0.5x |

## Use Cases

- **Compliance Storage**: Regulatory retention (7+ years)
- **Backup Archives**: Long-term disaster recovery
- **Media Archival**: Film, photos, legacy media
- **Log Retention**: Years of audit logs
- **Cold Data**: Rarely accessed datasets

## Pricing Breakdown

- **Storage**: $0.004/GB/month (Flexible Retrieval)
- **Deep Archive**: $0.00099/GB/month (cheapest)
- **Retrieval**: $0.01-$0.03/GB depending on tier
- **Minimum Storage Duration**: 90 days

Example: 10TB archive (Glacier) = ~$400/year storage

## S3 Lifecycle Integration

Automatic transition rules:
```
S3 Standard (0-30 days)
  ↓
S3 Intelligent-Tiering (30-90 days)
  ↓
Glacier (90+ days)
  ↓
Deep Archive (1+ years)
```

## Access & Retrieval

- **Initiate Retrieval**: Submit job to S3
- **Wait Period**: 1 minute to 12 hours
- **Download**: Retrieved to S3 temporary location
- **Cost**: Pay per GB retrieved

## Compliance Features

✅ HIPAA eligible
✅ GDPR compliant
✅ SOC 1/2/3 certified
✅ PCI-DSS compliant
✅ FedRAMP authorized

## Best Practices

✅ Use Deep Archive for 7+ year retention
✅ Set MFA delete on sensitive archives
✅ Enable Glacier Vault Lock for compliance
✅ Tag data with retention requirements
✅ Plan retrieval costs into budget
✅ Use bulk retrieval for cost savings

## Next Steps

→ [Glacier Documentation](https://docs.aws.amazon.com/glacier/)
→ [S3 Lifecycle Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
→ [Glacier Console](https://console.aws.amazon.com/glacier/)