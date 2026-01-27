# AWS Security Checklist ✅

A practical checklist for securing your AWS account and resources. Start at the top and work your way down.

## 🔴 CRITICAL - Do First!

### Account Security
- [ ] **Enable MFA on root account**
  - Go to IAM → Users → root account → Security credentials
  - Use authenticator app (not SMS)
  - Store recovery codes safely

- [ ] **Create IAM users for daily work**
  - Never use root account for daily tasks
  - Each person gets their own user
  - Enable MFA for each user

- [ ] **Enable CloudTrail logging**
  - Logs all AWS API activity
  - Essential for compliance
  - Store logs in S3

- [ ] **Set up billing alerts**
  - Prevent surprise charges
  - Alert at $50, $100, $500

### Access Control
- [ ] **Use IAM groups**
  - Create "Developers", "DevOps" groups
  - Add users to groups
  - Manage permissions at group level

- [ ] **Apply least privilege principle**
  - Users get MINIMUM permissions needed
  - Start restrictive, add as needed
  - Audit quarterly

- [ ] **Rotate access keys every 90 days**
  - Create new key, update applications
  - Delete old key

## 🟠 HIGH PRIORITY

### Data Protection
- [ ] **Enable encryption at rest**
  - S3: Enable default encryption
  - RDS: Check "Encryption" checkbox
  - EBS: Enable encryption on volumes
  - KMS: Use for sensitive data

- [ ] **Enable encryption in transit**
  - Use HTTPS/TLS everywhere
  - SSL certificates on load balancers
  - RDS: Enable SSL connections

- [ ] **Enable S3 versioning**
  - Protects against deletion
  - Recover previous versions

- [ ] **Restrict S3 bucket access**
  - Block all public access by default
  - Use bucket policies for specific access

### Network Security
- [ ] **Configure Security Groups**
  - Deny all inbound by default
  - Allow only needed ports
  - Restrict to specific IPs

- [ ] **Use private subnets**
  - Public: Load balancer only
  - Private: App servers, databases

- [ ] **Enable VPC Flow Logs**
  - Troubleshoot network issues
  - Monitor traffic patterns

## 🟡 IMPORTANT

### Monitoring
- [ ] **Enable CloudWatch Logs**
  - EC2: Detailed monitoring
  - Lambda: Log groups
  - RDS: Slow query logs

- [ ] **Set CloudWatch Alarms**
  - High CPU usage
  - Failed logins
  - Unusual API calls

- [ ] **Enable AWS Config**
  - Track configuration changes
  - Compliance alerts

### Backup & Recovery
- [ ] **Automated backups**
  - RDS: Daily backups (7-35 day retention)
  - EBS: Regular snapshots
  - S3: Versioning

- [ ] **Test recovery**
  - Monthly: Restore from backup
  - Verify it actually works

- [ ] **Use AWS Backup**
  - Centralized backup management
  - Cross-region backups

## 🚨 If Compromised

**IMMEDIATE:**
1. Change root account password
2. Enable MFA
3. Check CloudTrail for suspicious activity
4. Revoke suspicious access keys
5. Look for unexpected resources
6. Review unexpected IAM users

## 📖 Related Resources

- [Core Concepts - Security](../core-concepts/security-best-practices.md)
- [IAM Best Practices](../tier-1-foundational/iam/README.md)
- [Troubleshooting IAM Issues](../troubleshooting/iam-issues.md)
- [Cost Optimization](cost-optimization.md)