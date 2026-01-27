# Database Setup

TL;DR
- Choose managed database services: RDS for relational, DynamoDB for key-value, and Aurora for high performance.

Prerequisites
- IAM permissions and VPC with appropriate subnets.

Steps
1. For RDS, create subnet groups and a parameter group; launch an instance with automated backups enabled.
2. For DynamoDB, create tables with appropriate primary keys and set autoscaling or provisioned capacity.
3. Secure databases with security groups and subnet isolation.

Cost notes
- Storage, I/O, and backup retention affect costs; DynamoDB costs depend on read/write capacity units.

Troubleshooting
- Connection issues: check security groups, public accessibility, and subnet route tables.

Checklist
- Backup retention set, monitoring enabled, maintenance windows configured.
