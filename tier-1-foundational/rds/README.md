# AWS RDS (Relational Database Service) 🗄️

## 🎯 What is RDS?

RDS is a **managed database service** where AWS handles operations so you focus on data. AWS automatically handles backups, patches, scaling, and failover - you just create it and use it.

## 🔑 Database Options

- **MySQL**: Popular open-source, great for web apps
- **PostgreSQL**: Advanced open-source with more features  
- **MariaDB**: MySQL alternative, drop-in replacement
- **Oracle Database**: Enterprise-grade with most features
- **SQL Server**: Microsoft's database, Windows/.NET integration

## 💡 AWS Managed Benefits

**AWS Automatically Handles:**
- ✅ Daily automated backups
- ✅ Security patches and OS updates
- ✅ Database engine version upgrades
- ✅ High availability with Multi-AZ failover
- ✅ Read replicas for scaling reads
- ✅ Hardware provisioning and maintenance

**You Handle:**
- ✓ Writing SQL queries
- ✓ Database schema design
- ✓ Who can access (IAM/Security Groups)
- ✓ Application code

## 🚀 Quick Start

1. Go to RDS Console → Create Database
2. Choose engine (MySQL recommended for beginners)
3. Choose size: **db.t3.micro** (free tier eligible)
4. Set master username and password (strong password!)
5. Configure backup settings
6. Click "Create Database"
7. Wait 5 minutes for creation
8. Connect using SQL client (MySQL Workbench, pgAdmin, etc.)

## 💰 Free Tier Includes

- db.t3.micro or db.t2.micro instance (1 year)
- 20 GB storage
- Automated daily backups
- Multi-AZ for high availability

**Perfect for learning and testing!**

## ⭐ Best Practices

- ✓ Enable automated backups (minimum 7 days)
- ✓ Use Multi-AZ for production (automatic failover)
- ✓ Place in private subnet, not public
- ✓ Use Security Groups to allow only app servers
- ✓ Enable encryption at rest
- ✓ Use read replicas for read-heavy workloads

## 📖 Official Resources

- [RDS Documentation](https://docs.aws.amazon.com/rds/)
- [RDS Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)
- [RDS vs DynamoDB Comparison](../../service-comparisons/rds-vs-dynamodb.md)