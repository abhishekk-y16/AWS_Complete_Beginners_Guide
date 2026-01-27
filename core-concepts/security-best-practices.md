# Security Best Practices 🔐

Essential security controls and practical steps for AWS beginners.

## Shared Responsibility Model

AWS: security OF the cloud — physical hosts, networking, and hypervisor.
You: security IN the cloud — IAM, data, OS, applications, and network config.

## Day 1 Actions (Critical)

- Enable root account MFA and store root credentials securely.
- Create an admin IAM user and enable MFA for it.
- Enable CloudTrail for all regions and send logs to a central S3 bucket.
- Turn on AWS Config to track resource changes.
- Set up billing alerts and budgets.

## Identity & Access

- Enforce least privilege and use groups for role management.
- Use IAM roles for EC2/Lambda — avoid long-lived access keys.
- Enforce a strong password policy and rotate credentials regularly.

## Network & Data Protection

- Use VPC private subnets for databases and internal services.
- Use Security Groups (stateful) and NACLs (stateless) for layered defense.
- Enable encryption at rest (S3, EBS, RDS) and encryption in transit (TLS).

## Monitoring & Detection

- Enable GuardDuty for threat detection.
- Configure VPC Flow Logs and CloudWatch Alarms for suspicious activity.
- Centralize logs and monitor with automated alerts.

## Backups & Recovery

- Enable automated RDS backups and EBS snapshots.
- Use S3 versioning and lifecycle rules; consider cross-region replication.
- Test restore procedures regularly.

## Patch Management

- Patch EC2 instances using AWS Systems Manager Patch Manager.
- Rebuild and redeploy containers with updated base images.

## Cost-Aware Security

- GuardDuty and Config have low baseline costs; enable in production.
- Use sampling and retention policies for long-term logs to control costs.

## Common Pitfalls

- Leaving S3 buckets public by accident — enable Block Public Access and default encryption.
- Allowing 0.0.0.0/0 for SSH — restrict to admin IPs or use SSM Session Manager.
- Not enabling MFA on privileged accounts.

## Quick Checklist

- [ ] Root MFA enabled
- [ ] Admin IAM user created and MFA enabled
- [ ] CloudTrail + Config enabled (all regions)
- [ ] GuardDuty enabled
- [ ] S3 default encryption on
- [ ] Security groups documented and least-privilege enforced

## Links

- Security checklist: ../best-practices/security-checklist.md
- AWS security best practices: https://aws.amazon.com/security/best-practices/
- Optimize costs
- Regular audits