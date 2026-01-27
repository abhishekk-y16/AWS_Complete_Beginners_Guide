# RDS: First Database

TL;DR
- Launch a managed relational DB (PostgreSQL/MySQL) on RDS with backups, security groups, and minimal tuning.

Prerequisites
- VPC with subnets, DB subnet group, security group allowing your IP/app, admin credentials planned.

Steps
1. Create DB subnet group covering two+ AZs.
2. Launch RDS instance (e.g., `db.t3.micro`, Postgres), set storage (gp3), enable auto minor version upgrades.
3. Set backups: automated backups (7–35 days), enable Multi-AZ if uptime is critical.
4. Networking: attach security group to allow app/your IP on port 5432/3306.
5. Connect using `psql`/`mysql` from bastion or client and create application user/db.
6. Monitor with Performance Insights and CloudWatch; set storage autoscaling.

Cost notes
- Instance hours + storage + I/O; Multi-AZ doubles compute/storage.

Troubleshooting
- Connection refused: check SG ingress and if instance is in public/private subnet; ensure correct endpoint/port.
- Slow queries: create indexes, enable Performance Insights, or resize instance/storage type.

Checklist
- Backups enabled, SG rules set, app user created, monitoring active.