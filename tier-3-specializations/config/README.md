# AWS Config ⚙️

Continuous monitoring and compliance service that tracks AWS resource configuration changes.

## Overview

AWS Config records configuration of every AWS resource. Detects non-compliance (wrong security group, unencrypted database). Tracks changes over time with complete audit trail. Essential for compliance audits and security investigations.

## Key Features

- ✅ Configuration tracking for all resources
- ✅ Compliance rules (400+ pre-built rules)
- ✅ Auto-remediation capabilities
- ✅ Configuration change timeline
- ✅ Relationship and dependency mapping
- ✅ Compliance dashboard

## What Gets Tracked

- **EC2**: Security groups, instance types, public IPs
- **RDS**: Parameter groups, encryption, backups, Multi-AZ status
- **S3**: Versioning, public access settings, encryption
- **IAM**: User/role creation, permission changes
- **Plus**: 100+ other AWS services

## Pre-Built Compliance Rules

- ✅ Encryption enabled?
- ✅ Backup configured?
- ✅ Public access blocked?
- ✅ Logging enabled?
- ✅ MFA required?
- ✅ 400+ compliance rules available

## How It Works

Resource Change → Config detects → Compliance evaluation → Alert/Auto-fix → Timeline recorded

## Use Cases

- **Compliance Audits**: Prove resources meet standards
- **Security Monitoring**: Detect unauthorized changes
- **Change Management**: Track configuration timeline
- **Risk Assessment**: Identify non-compliant resources

## Pricing

- Configuration items: $0.003 per item/month
- Conformance packs: $15/month
- Example: 115 resources = $0.35/month + packs

## Best Practices

✅ Enable Config for all resources
✅ Use conformance packs for compliance frameworks
✅ Configure auto-remediation for common issues
✅ Regular review of non-compliant resources
✅ Archive old data for long-term compliance

## Next Steps

→ [AWS Config Documentation](https://docs.aws.amazon.com/config/)
→ [Compliance Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
→ [Config Console](https://console.aws.amazon.com/config/)