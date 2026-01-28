# RDS Use Cases 🎯

Real-world scenarios where AWS RDS is the right database choice.

## Use Case 1: Web Application with User Data

### Scenario

```
You're building: Social network app

Requirements:
├─ Store user profiles (name, bio, avatar)
├─ Store user connections/friendships
├─ Store posts and comments
├─ Query user feed (recent posts from friends)
├─ Update user information frequently
└─ Strong data consistency required

Why RDS is perfect:
├─ SQL: Easy to query relationships
├─ ACID transactions: Consistency guaranteed
├─ Indexes: Fast search by username
├─ Joins: Efficient queries across tables
└─ Backups: Protect user data
```

### Database Design

```sql
-- Users table
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Posts table
CREATE TABLE posts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Friendships (relationships)
CREATE TABLE friendships (
  user_id INT NOT NULL,
  friend_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, friend_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (friend_id) REFERENCES users(id)
);
```

### Cost & Scale

```
Small scale (10K users):
├─ Instance: db.t3.micro
├─ Storage: 10GB
├─ Monthly cost: ~$14
├─ Estimated users: 10,000
└─ Cost per user: $0.0014/month

Medium scale (1M users):
├─ Instance: db.m5.large
├─ Storage: 500GB
├─ Read replicas: 3
├─ Monthly cost: ~$1,000
├─ Estimated users: 1,000,000
└─ Cost per user: $0.001/month
```

## Use Case 2: E-Commerce Platform

### Scenario

```
You're building: Online store (Shopify-like)

Requirements:
├─ Store product catalog (SKU, price, inventory)
├─ Track orders and order items
├─ Inventory management (stock levels)
├─ Customer reviews and ratings
├─ Transaction history
├─ Payment information (encrypted)
└─ Must handle concurrent orders (transactions)

Why RDS is perfect:
├─ Transactions: Inventory can't go negative
├─ Consistency: Order total matches items + tax
├─ Relationships: Orders → Items → Products
├─ Indexes: Fast product search
└─ Reliability: Never lose sales data
```

### Database Design

```sql
-- Products
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  stock INT NOT NULL DEFAULT 0
);

-- Orders
CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  total_amount DECIMAL(12, 2),
  status ENUM('pending', 'completed', 'failed'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order Items
CREATE TABLE order_items (
  id INT PRIMARY KEY AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2),
  FOREIGN KEY (order_id) REFERENCES orders(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### Transaction Example

```javascript
// Process order with guarantee
const connection = await getConnection();

try {
  await connection.beginTransaction();
  
  // 1. Create order
  await connection.execute(
    'INSERT INTO orders (customer_id, total_amount, status) VALUES (?, ?, ?)',
    [customerId, totalAmount, 'pending']
  );
  
  // 2. Add order items
  for (const item of cartItems) {
    await connection.execute(
      'INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)',
      [orderId, item.productId, item.qty, item.price]
    );
  }
  
  // 3. Reduce inventory
  for (const item of cartItems) {
    await connection.execute(
      'UPDATE products SET stock = stock - ? WHERE id = ?',
      [item.qty, item.productId]
    );
  }
  
  // 4. Mark order complete
  await connection.execute(
    'UPDATE orders SET status = ? WHERE id = ?',
    ['completed', orderId]
  );
  
  // If all succeed → commit
  await connection.commit();
  
} catch (error) {
  // If ANY step fails → rollback all
  await connection.rollback();
  throw error;
}
```

### Cost & Scale

```
Small store (1K products, 100 orders/day):
├─ Instance: db.t3.micro
├─ Storage: 50GB
├─ Monthly cost: ~$18
└─ Revenue: $3,000/day = $90K/month

Large store (100K products, 1M orders/month):
├─ Instance: db.m5.2xlarge + replicas
├─ Storage: 2TB with provisioned IOPS
├─ Multi-AZ: Yes (must not go down!)
├─ Monthly cost: ~$5,000
└─ Revenue: $30M/month
└─ Cost as % of revenue: 0.017% (tiny!)
```

## Use Case 3: Financial Application

### Scenario

```
You're building: Personal finance app (like Mint)

Requirements:
├─ Store bank account information
├─ Transaction history (immutable)
├─ Budget tracking
├─ Category spending analysis
├─ Recurring bills
├─ Data encryption (PII sensitive)
└─ Audit trail (who changed what, when)

Why RDS is perfect:
├─ Data integrity: Can't lose transactions
├─ ACID: Balance calculations always correct
├─ Encryption: Built-in encryption at rest
├─ Backups: Automated daily backups
└─ Compliance: Audit logs/triggers for changes
```

### Database Design

```sql
-- Accounts
CREATE TABLE accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  bank_name VARCHAR(100),
  account_type ENUM('checking', 'savings', 'credit'),
  balance DECIMAL(15, 2) NOT NULL
);

-- Transactions (immutable)
CREATE TABLE transactions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  account_id INT NOT NULL,
  amount DECIMAL(12, 2) NOT NULL,
  type ENUM('debit', 'credit') NOT NULL,
  category VARCHAR(50),
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  -- Prevent updates/deletes
  CONSTRAINT immutable CHECK (created_at = created_at),
  FOREIGN KEY (account_id) REFERENCES accounts(id)
);

-- Audit log (compliance)
CREATE TABLE audit_log (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  action VARCHAR(100) NOT NULL,
  changed_data JSON,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Triggers for Audit

```sql
-- Auto-log when transaction added
DELIMITER //
CREATE TRIGGER transaction_audit
AFTER INSERT ON transactions
FOR EACH ROW
BEGIN
  INSERT INTO audit_log (user_id, action, changed_data)
  VALUES (
    (SELECT user_id FROM accounts WHERE id = NEW.account_id),
    'TRANSACTION_ADDED',
    JSON_OBJECT('amount', NEW.amount, 'category', NEW.category)
  );
END//
DELIMITER ;
```

### Cost & Compliance

```
Small app (10K users, conservative data):
├─ Instance: db.t3.small
├─ Storage: 100GB
├─ Encryption: At rest + in transit
├─ Backup retention: 30 days
├─ Monthly cost: ~$30
└─ Compliance: HIPAA/PCI if needed (extra cost)

Big financial platform:
├─ Multi-region for disaster recovery
├─ Multi-AZ for high availability
├─ Enhanced monitoring for compliance
├─ Encryption: Hardware-backed (AWS CloudHSM)
└─ Monthly cost: $10,000+
└─ Trade-off: Acceptable for financial data safety
```

## Use Case 4: Reporting & Analytics

### Scenario

```
You're building: Business intelligence dashboard

Requirements:
├─ Historical data (years of records)
├─ Complex SQL queries (joins, aggregations)
├─ Daily report generation
├─ Ad-hoc analysis queries
├─ Quarterly business reviews
└─ Don't need real-time data (1 hour lag acceptable)

Why RDS is good:
├─ SQL: Complex aggregations and grouping
├─ Indexes: Fast queries on large datasets
├─ Scheduled backups: Keep historical data
└─ Cost-effective compared to data warehouses

Why NOT RDS:
└─ If need petabyte-scale data → Use Redshift instead
```

### Reporting Queries

```sql
-- Daily revenue by region
SELECT
  DATE(orders.created_at) as date,
  users.region,
  COUNT(*) as order_count,
  SUM(orders.total_amount) as total_revenue
FROM orders
JOIN users ON orders.user_id = users.id
WHERE orders.created_at >= DATE_SUB(NOW(), INTERVAL 90 DAY)
GROUP BY DATE(orders.created_at), users.region
ORDER BY date DESC, total_revenue DESC;

-- Customer lifetime value
SELECT
  users.id,
  users.name,
  COUNT(orders.id) as total_orders,
  SUM(orders.total_amount) as lifetime_value,
  AVG(orders.total_amount) as avg_order_value
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
HAVING lifetime_value > 1000
ORDER BY lifetime_value DESC;
```

### Architecture

```
Production System          Read-Only Replica
┌─────────────────────────────┐   ┌──────────────────────┐
│ Primary RDS MySQL   │─────│ Read Replica     │
│ (Online app)        │   │ (Analytics)      │
│ - Write traffic     │   │ - Reporting      │
│ - Real-time data    │   │ - Complex queries│
│ - High performance  │   │ - Scheduled jobs │
└─────────────────────────────┘   └──────────────────────┘
          │
    (Auto-backup)
          │
    (S3 long-term)
```

### Cost & Performance

```
Small analytics (10M records):
├─ Read replica: db.t3.small
├─ Storage: 200GB
├─ Queries: < 5 min each
├─ Monthly cost: ~$30
└─ Perfect for: Quarterly reports

Medium analytics (1B records):
├─ Primary: db.m5.2xlarge
├─ Read replica: db.m5.2xlarge
├─ Storage: 5TB provisioned IOPS
├─ Queries: < 30 sec each
├─ Monthly cost: ~$2,000
└─ Perfect for: Daily dashboards + ad-hoc queries
```

## Use Case 5: SaaS Application

### Scenario

```
You're building: Project management tool (Asana-like)

Multi-tenant requirements:
├─ Each customer has separate workspace
├─ Data isolation (one tenant can't see another's data)
├─ Usage tracking (per-tenant metrics)
├─ Scalable to thousands of customers
└─ Per-customer backups

Why RDS is perfect:
├─ Database per tenant (isolation)
├─ Or: Schema per tenant (cost-efficient)
├─ Row-level security: Tenant filters
├─ Scaling: Just add more read replicas
└─ Backups: Automated per database
```

### Row-Level Security Example

```sql
-- Single database, multiple tenants
CREATE TABLE workspaces (
  id INT PRIMARY KEY AUTO_INCREMENT,
  tenant_id INT NOT NULL,
  name VARCHAR(100)
);

CREATE TABLE tasks (
  id INT PRIMARY KEY AUTO_INCREMENT,
  workspace_id INT NOT NULL,
  title VARCHAR(200),
  FOREIGN KEY (workspace_id) REFERENCES workspaces(id)
);

-- Add tenant ID to session/JWT
-- Always filter by tenant_id:
SELECT * FROM tasks
WHERE workspace_id IN (
  SELECT id FROM workspaces
  WHERE tenant_id = :current_tenant_id  -- Always enforced
);
```

### Scaling Strategy

```
Stage 1: Single database (all customers)
├─ Database: db.t3.micro
├─ Cost: $12/month
├─ Customers: < 100
└─ Issues: Noisy neighbor problem

Stage 2: Database per customer
├─ Database: 100 × db.t3.micro
├─ Cost: 100 × $12 = $1,200/month
├─ Customers: 100+
├─ Benefit: Complete isolation
└─ Issues: Management overhead

Stage 3: Hybrid approach
├─ Small customers: Shared database
├─ Large customers: Dedicated database
├─ Cost: Optimized per tier
└─ Benefit: Best of both worlds
```

## When NOT to Use RDS

```
❌ Unstructured data (photos, videos)
   → Use: S3 instead

❌ NoSQL data (flexible schema, JSON)
   → Use: DynamoDB or MongoDB

❌ Real-time logs (write-heavy, time-series)
   → Use: CloudWatch Logs or Elasticsearch

❌ Graph data (relationships are primary)
   → Use: Neptune

❌ Very large datasets (PB scale)
   → Use: Redshift or BigQuery

❌ Full-text search (Elasticsearch-like)
   → Use: OpenSearch or Elasticsearch

❌ Cache layer (high-speed reads)
   → Use: ElastiCache or Memcached
```

## Best Practices by Use Case

### Web Applications
✅ Use connection pooling
✅ Implement query timeouts
✅ Add indexes on frequently searched columns
✅ Cache frequently accessed data
✅ Monitor slow queries

### E-Commerce
✅ Use transactions for orders
✅ Separate read replicas for reports
✅ Keep inventory as separate table (for locking)
✅ Archive old orders to S3
✅ Monitor stock levels

### Financial Systems
✅ Immutable transaction table
✅ Audit logs for compliance
✅ Double-entry accounting (debit/credit)
✅ Multi-AZ mandatory
✅ Encryption at rest + in transit

### Analytics
✅ Use read replica to separate from production
✅ Indexes on dimension tables
✅ Periodically vacuum/optimize tables
✅ Archive old data to S3
✅ Use scheduler for heavy reports (off-peak)

### SaaS
✅ Tenant isolation (separate databases or rows)
✅ Usage tracking per tenant
✅ Per-tenant backups
✅ Monitor noisy neighbors
✅ Implement rate limiting

## Next Steps

→ [What is RDS](./what-is-rds.md) - Full overview
→ [Pricing](./pricing.md) - Cost breakdown
→ [Creating First Database](./creating-first-database.md) - Hands-on guide