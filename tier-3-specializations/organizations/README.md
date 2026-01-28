# AWS Organizations 🏢

Centralized management of multiple AWS accounts for large enterprises and organizations.

## Overview

Organizations consolidates billing, enforces policies, and manages multiple AWS accounts. Create organizational units (OUs), apply service control policies (SCPs), centralize logging. Ideal for enterprises with 10+ accounts.

## Key Features

- ✅ Consolidated billing across accounts
- ✅ Service Control Policies (SCPs)
- ✅ Organizational Units (OUs)
- ✅ AWS SSO integration
- ✅ Central audit logging (CloudTrail)
- ✅ Backup and recovery policies

## Organization Structure

```
Root
├─ Production OU
│  ├─ Account: Web Tier
│  ├─ Account: Database Tier
│  └─ Account: Analytics
├─ Development OU
│  ├─ Account: Dev Team A
│  └─ Account: Dev Team B
└─ Security OU
   └─ Account: Logging & Audit
```

## Service Control Policies (SCPs)

Policies that restrict what members can do:
- Prevent services usage by region
- Enforce encryption requirements
- Restrict root user actions
- Deny specific APIs globally
- Require MFA for actions

Example: Deny all actions except in US-East-1:
```json
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": "us-east-1"
    }
  }
}
```

## Use Cases

- **Multi-Account Strategy**: Separate prod/dev/test
- **Cost Allocation**: Billing per team or project
- **Compliance Enforcement**: Organization-wide policies
- **Security Isolation**: Separate security boundary per account
- **Partner Integration**: Secure multi-party deployments

## Consolidated Billing Benefits

✅ Volume discounts applied across accounts
✅ Reserved Instances shared automatically
✅ Savings Plans aggregated
✅ One bill for entire organization

## AWS SSO (Single Sign-On)

- Centralized user management
- One login for all accounts
- MFA enforcement
- Temporary credentials (no long-term access keys)
- Federate with Active Directory

## Policies & Compliance

- **Service Control Policies**: Restrict actions
- **Tag Policies**: Enforce tagging
- **Backup Policies**: Centralized backup requirements
- **AI Services Opt-Out**: Manage data usage

## Cross-Account Access

- Assume roles across accounts
- Delegate permissions via STS
- Secure service-to-service communication
- Audit cross-account access

## Pricing

- **Organization**: Free
- **Consolidated Billing**: Free
- **SSO**: Free tier (up to 2 MB stored users)

## Best Practices

✅ Use separate accounts for prod/dev/test
✅ Implement SCPs for guardrails
✅ Enable CloudTrail in central account
✅ Use AWS SSO instead of IAM users
✅ Enforce MFA at root and human users
✅ Regular SCP review and updates
✅ Implement least-privilege SCPs

## Next Steps

→ [AWS Organizations Documentation](https://docs.aws.amazon.com/organizations/)
→ [SCP Examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html)
→ [Organizations Console](https://console.aws.amazon.com/organizations/)