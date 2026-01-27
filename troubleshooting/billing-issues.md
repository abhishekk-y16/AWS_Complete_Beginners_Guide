# Billing Issues 🔍

Symptoms
- Unexpected bill spike
- Free-tier overages
- Credits not applied

Quick checks
- Cost Explorer (daily view) and Top Services widget
- Bills → Previous months for anomalies
- AWS Budgets/Alerts status

Common causes & fixes
- **Idle resources**: stop orphaned EC2/RDS/ECS tasks; delete unattached EBS/EIP.
- **Data transfer**: high inter-AZ or NAT Gateway; add VPC endpoints or same-AZ placements.
- **S3/CloudFront**: hot objects or many small PUTs; add caching/compression and lifecycle policies.
- **Lambda/API GW**: sudden traffic; set throttles and WAF rules.
- **Free-tier expiry**: 12-month window ended; right-size or move to cheaper tiers.

Prevention
- Set budgets with email/SNS alerts.
- Tag resources with `owner`, `env`, `cost-center` and use cost allocation tags.
- Enable Cost Anomaly Detection.