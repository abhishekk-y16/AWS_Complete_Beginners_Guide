# Creating Your First RDS Database 🚀

Step-by-step hands-on guide to create, configure, and connect to your first AWS RDS database.

## What You'll Learn

```
By the end of this guide:

├─ Create a managed MySQL database
├─ Connect from your application
├─ Take automated backups
├─ Monitor performance
└─ Cost ~$10-15/month for small workload
```

## Prerequisites

```
1. AWS Account
   ├─ Free tier eligible (750 hrs/month of db.t3.micro)
   └─ Create at: https://aws.amazon.com

2. Basic knowledge
   ├─ SQL queries (SELECT, INSERT)
   ├─ What is a database
   └─ Network basics (VPC, security groups)

3. Optional tools
   ├─ MySQL Workbench (GUI client)
   ├─ SQL CLI (command line)
   └─ Any application (Node.js, Python, etc.)
```

## Step 1: Create RDS Instance (Console)

### Navigate to RDS

```
1. Log into AWS Console
   └─ https://console.aws.amazon.com

2. Find RDS service
   ├─ Search bar: "RDS"
   ├─ Click: "RDS" service
   └─ Select region: us-east-1 (most free tier options)

3. Click "Create database"
   └─ Orange button on dashboard
```

### Choose Engine

```
Database creation page:

1. Engine options
   ├─ Select: MySQL (free tier eligible)
   ├─ Version: 8.0.35 (latest)
   └─ Edition: Community (free)

2. Templates
   ├─ Select: Free tier
   └─ This includes: db.t3.micro, 20GB storage, backups

3. DB instance identifier
   ├─ Name: my-first-database
   └─ Rules: Alphanumeric + hyphens
```

### Configure Settings

```
Credentials:

1. Master username
   ├─ Default: admin
   └─ Can't change after creation

2. Master password
   ├─ Create: Strong password (12+ chars)
   ├─ Example: MyDb#Pass2024!
   └─ Save this! (you'll need it to connect)

3. Confirm password
   └─ Re-enter the password
```

### DB Instance Size

```
Instance class:
├─ Selected: db.t3.micro (free tier)
├─ vCPU: 2
├─ Memory: 1 GB
└─ Perfect for development/learning!

Storage:
├─ Type: General Purpose (SSD)
├─ Size: 20 GB (free tier)
├─ Allocated: 20 GB
└─ Auto-scaling: Enable (optional)
```

### Network & Security

```
VPC & Security Group:

1. VPC
   ├─ Select: Default VPC (easiest)
   └─ Or: Your custom VPC

2. Public accessibility
   ├─ Select: Yes
   ├─ Allows: Connect from internet
   └─ Important: Restrict with security group

3. VPC Security Group
   ├─ Select: Create new
   ├─ Name: rds-mysql-sg
   └─ Later: Configure rules for your IP

4. Availability zone
   ├─ Select: No preference (auto-select)
   └─ Or: Specific zone (doesn't matter for learning)
```

### Backup & Maintenance

```
Backup settings:

1. Automated backups
   ├─ Enabled: Yes
   ├─ Retention: 7 days
   └─ Automatic recovery: Enabled

2. Backup window
   ├─ Preferred: 03:00-04:00 UTC
   └─ Choose off-peak hours

3. Maintenance window
   ├─ Preferred: Mon 04:00-05:00 UTC
   └─ AWS can patch/update during this time
```

### Final Step

```
1. Review all settings
   └─ Double-check:
      ├─ Engine: MySQL
      ├─ Instance: db.t3.micro
      ├─ Storage: 20GB
      └─ Public: Yes

2. Click: "Create database"
   └─ Creation takes 5-10 minutes

3. Wait for status
   ├─ Status: "Creating..."
   ├─ Then: "Modifying..."
   └─ Finally: "Available" (ready to connect!)
```

## Step 2: Configure Security Group

### Allow Your IP

```
1. RDS console → Databases → Your database
2. Scroll to: Connectivity & security
3. VPC Security Group: Click the group name
4. Inbound rules → Edit inbound rules
5. Add rule:
   ├─ Type: MySQL/Aurora
   ├─ Protocol: TCP
   ├─ Port: 3306
   ├─ Source: Your IP (find at: https://checkip.amazonaws.com)
   └─ Example: 192.0.2.1/32
6. Save rules
```

### Test Connection

```
After security group update:

1. Get endpoint
   └─ RDS console → Databases → Your DB
   └─ Copy: "Endpoint" (looks like: my-first-database.xxx.us-east-1.rds.amazonaws.com)

2. Try to connect
   └─ Command: mysql -h [endpoint] -u admin -p
   └─ Enter password when prompted
   └─ Success: mysql> prompt appears
```

## Step 3: Connect from Application

### Node.js Connection

```javascript
// 1. Install driver
// npm install mysql2

const mysql = require('mysql2/promise');

const connection = await mysql.createConnection({
  host: 'my-first-database.xxx.us-east-1.rds.amazonaws.com',
  user: 'admin',
  password: 'MyDb#Pass2024!',
  database: 'myapp' // create this first
});

// 2. Query database
const [rows] = await connection.execute(
  'SELECT * FROM users WHERE id = ?',
  [1]
);

console.log(rows);

// 3. Insert data
await connection.execute(
  'INSERT INTO users (name, email) VALUES (?, ?)',
  ['John Doe', 'john@example.com']
);

await connection.end();
```

### Python Connection

```python
# 1. Install driver
# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host='my-first-database.xxx.us-east-1.rds.amazonaws.com',
    user='admin',
    password='MyDb#Pass2024!',
    database='myapp'
)

cursor = connection.cursor()

# 2. Query database
cursor.execute('SELECT * FROM users WHERE id = %s', (1,))
result = cursor.fetchall()
print(result)

# 3. Insert data
cursor.execute(
    'INSERT INTO users (name, email) VALUES (%s, %s)',
    ('John Doe', 'john@example.com')
)
connection.commit()

cursor.close()
connection.close()
```

## Step 4: Create Database & Tables

### Create Database

```sql
-- Login first:
-- mysql -h [endpoint] -u admin -p

-- Create database
CREATE DATABASE myapp;

-- Use database
USE myapp;
```

### Create Table

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verify
SHOW TABLES;
DESC users;
```

### Insert Sample Data

```sql
INSERT INTO users (name, email) VALUES
  ('Alice Johnson', 'alice@example.com'),
  ('Bob Smith', 'bob@example.com'),
  ('Carol White', 'carol@example.com');

-- Verify
SELECT * FROM users;

-- Result:
-- | id | name           | email               | created_at          |
-- |----|----------------|---------------------|---------------------| 
-- | 1  | Alice Johnson  | alice@example.com   | 2024-01-28 15:30:45 |
-- | 2  | Bob Smith      | bob@example.com     | 2024-01-28 15:30:45 |
-- | 3  | Carol White    | carol@example.com   | 2024-01-28 15:30:45 |
```

## Step 5: Monitor Database

### CloudWatch Metrics

```
1. RDS console → Databases → Your DB
2. Monitoring tab
3. View metrics:
   ├─ CPU Utilization (%)
   ├─ Database Connections (count)
   ├─ Network Receive Throughput (bytes/sec)
   ├─ Storage Space (GB)
   └─ Read/Write Latency (ms)

Healthy values for development:
├─ CPU < 20%
├─ Connections < 10
└─ Latency < 10ms
```

### Check Backups

```
1. RDS console → Automated backups
2. View:
   ├─ Backup creation time
   ├─ Retention period (days)
   ├─ Size (GB)
   └─ Status (Creating/Available)

Automatically created:
├─ Daily backup
├─ Kept for 7 days
└─ Can restore to any point in time
```

## Common Tasks

### Increase Storage

```
1. RDS console → Databases → Your DB
2. Modify
3. Storage:
   ├─ Change: 20 GB → 30 GB
   └─ Applied immediately or during maintenance
4. Continue → Modify DB instance

No downtime!
```

### Change Master Password

```
1. RDS console → Databases → Your DB
2. Modify
3. Master password:
   ├─ Enter new password
   └─ Re-confirm
4. Continue → Modify DB instance

Note: This will break connections briefly!
```

### Enable Multi-AZ (High Availability)

```
1. RDS console → Databases → Your DB
2. Modify
3. Availability & durability:
   ├─ Multi-AZ deployment: Yes
   └─ Creates standby replica in another zone
4. Continue → Modify DB instance

If primary fails → Automatic failover
Downtime: 1-2 minutes
Cost: 2x instance price
```

### Scale Instance Size

```
Need more power?

1. RDS console → Modify
2. DB instance class:
   ├─ Current: db.t3.micro (1GB RAM)
   ├─ Change to: db.t3.small (2GB RAM)
   └─ Or: db.t3.medium (4GB RAM)
3. Continue → Modify DB instance

Downtime: Few minutes (if applied immediately)
Or: Schedule for maintenance window (no downtime)

Cost impact:
├─ db.t3.small: ~$0.017/hour ($12/month)
├─ db.t3.medium: ~$0.034/hour ($25/month)
└─ db.t4g.micro: ~$0.0095/hour ($7/month) - Newer, cheaper
```

## Best Practices

✅ Use strong passwords (12+ chars, mix of types)
✅ Enable Multi-AZ for production
✅ Automated backups enabled (minimum 7 days)
✅ Monitor with CloudWatch (set alarms)
✅ Use security groups (restrict to your IP)
✅ Update regularly (enable auto-minor-version-upgrade)
✅ Use connection pooling in applications
✅ Regular backups for critical data
✅ Test failover process
✅ Document connection strings
✅ Use secrets manager for passwords
✅ Performance Insights for monitoring

## Troubleshooting

### Can't Connect

```
Problem: Connection timeout

Check:
1. Security group inbound rule
   └─ Port 3306 open to your IP?

2. Database status
   └─ Status showing "Available"?

3. Endpoint is correct
   └─ Copy from RDS console

4. Username/password correct
   └─ admin / YourPassword

5. Database exists
   └─ SHOW DATABASES; (after connecting)
```

### Slow Queries

```
Problem: Database is slow

Solutions:
1. Check CPU/Memory usage
   └─ CloudWatch metrics

2. Upgrade instance size
   └─ db.t3.small or higher

3. Check slow query logs
   └─ Enable in parameter group
   └─ View in CloudWatch Logs

4. Add indexes
   └─ CREATE INDEX idx_email ON users(email);
```

## Next Steps

→ [What is RDS](./what-is-rds.md) - Full RDS overview
→ [Pricing](./pricing.md) - Cost breakdown
→ [Use Cases](./use-cases.md) - When to use RDS