# CloudTrail 🔍

Audit and compliance service that logs all AWS API calls and account activity.

## Overview

CloudTrail records every API call to AWS services. Who did what, when, from where. Essential for security, compliance (HIPAA, PCI-DSS), and troubleshooting. Every action in your AWS account leaves a trail.

## Key Features

- ✅ Complete API call logging (Management, Data, Insights events)
- ✅ Compliance auditing with immutable logs
- ✅ CloudTrail Insights detects unusual API activity
- ✅ Integration with CloudWatch and S3
- ✅ Log integrity validation and tamper-proof verification
- ✅ Security investigation and forensics

## What Gets Logged

**Management Events**: IAM changes, EC2 launches, RDS modifications, security group changes
**Data Events**: S3 object access, Lambda invocations, DynamoDB activity
**Insights Events**: Unusual API activity detection

## Use Cases

- **Compliance Audits**: Prove resources are compliant with standards
- **Security Investigations**: Trace unauthorized access and suspicious activity
- **Troubleshooting**: Find who changed what and when
- **Incident Response**: Forensic analysis of security events

## How It Works

AWS Action → CloudTrail records details → Stored in S3 (encrypted) → Query with Athena/CloudWatch

## Pricing

- Management Events: $2/100,000 events
- Data Events: $0.10/100,000 events
- Insights: $0.35/100,000 events
- Example: 5M API calls/month = ~$100/month

## Best Practices

✅ Enable CloudTrail on all accounts
✅ Validate log file integrity
✅ Archive logs to Glacier for long-term retention
✅ Use CloudTrail Insights for anomaly detection
✅ Integrate with SIEM solutions

## Next Steps

→ [CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
→ [Security Best Practices](https://docs.aws.amazon.com/security/)
→ [CloudTrail Console](https://console.aws.amazon.com/cloudtrail/)