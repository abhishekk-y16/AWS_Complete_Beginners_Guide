# What is Elastic Beanstalk? 🌐

AWS Platform-as-a-Service for deploying, managing, and auto-scaling web applications.

## Core Concept

**Elastic Beanstalk** abstracts infrastructure complexity. Upload code → Beanstalk handles servers, databases, monitoring.

```
Traditional Deployment:
├─ Launch EC2 instances
├─ Configure Auto Scaling
├─ Setup Load Balancer
├─ Install runtime (Python, Node, etc)
├─ Deploy code manually
├─ Monitor CloudWatch
└─ 1-2 weeks to production

Elastic Beanstalk:
├─ Upload code
├─ Select environment
├─ Click deploy
└─ Live in minutes!
```

## How It Works

```
Beanstalk Architecture:
├─ Application: Your code
├─ Environment: Deployment instance
│  ├─ EC2 instances (2-10+)
│  ├─ Auto Scaling group
│  ├─ Elastic Load Balancer
│  ├─ RDS database (optional)
│  └─ CloudWatch monitoring
├─ Version: Specific code release
└─ Configuration: Settings (CPU, memory, etc)
```

## Supported Platforms

```
Languages:
├─ Node.js (12+, 14+, 16+, 18+)
├─ Python (3.7, 3.8, 3.9, 3.10, 3.11)
├─ Java (8, 11, 17)
├─ Ruby (2.6, 2.7, 3.0, 3.1)
├─ Go (1.18+)
├─ PHP (7.4, 8.0, 8.1)
├─ .NET (3.1, 6.0)
└─ Docker (custom containers)

Auto-selected runtime handles:
├─ OS updates
├─ Runtime patches
├─ Security fixes
└─ Performance optimization
```

## Deployment Strategies

### All-at-Once (0% uptime, fastest)

```
Deploy app v2.0:

Before:
└─ 4 instances running v1.0

Deploy all-at-once:
├─ Stop all 4 instances
├─ Deploy v2.0 to all
├─ Start all instances
└─ DOWNTIME: 2-3 minutes

Use case: Development, low traffic
```

### Rolling (100% uptime, balanced)

```
Deploy app v2.0 to 4 instances:

├─ Stop instance #1, deploy v2.0
│  └─ 3 instances serving, 25% capacity
├─ Stop instance #2, deploy v2.0
│  └─ 2 instances serving, 50% capacity
├─ Stop instance #3, deploy v2.0
│  └─ 1 instance serving, 75% capacity
└─ Stop instance #4, deploy v2.0
   └─ All on v2.0, 100% capacity

Downtime: 0 minutes
Duration: 5-10 minutes
Use case: Production with traffic
```

### Blue-Green (Safe, testable)

```
Setup:
├─ Blue environment (v1.0): 4 instances
└─ Green environment (empty)

Deployment:
├─ Launch green: Deploy v2.0 to 4 new instances
├─ Test green: All traffic still on blue
├─ Validate: Green passes smoke tests
├─ Switch: Redirect traffic to green
└─ Cleanup: Terminate blue later

Downtime: 0 minutes (traffic switches instantly)
Use case: Critical production (banking, healthcare)
Risk: Lowest (test before going live)
```

## Real-World Example: SaaS App

```
Deployment:

Step 1: Git push
├─ git commit -m "Fix homepage"
└─ git push origin main

Step 2: Deploy to Beanstalk
├─ AWS console → Upload code
├─ Select "Rolling" deployment
└─ Click "Deploy"

Step 3: Beanstalk handles
├─ Pull code from S3
├─ Update instances (rolling, no downtime)
├─ Run health checks
├─ Monitor with CloudWatch
└─ Auto-scale if traffic spikes

Result: Live in 3-5 minutes, zero downtime!
```

## Environment Configuration

```
Development Environment:
├─ Instance type: t3.micro (free tier eligible)
├─ Instances: 1 (cost-optimized)
├─ Auto Scaling: Disabled
├─ Database: None (use external)
└─ Cost: $0/month (free tier) or ~$5/month

Production Environment:
├─ Instance type: t3.small (2 CPU, 2GB RAM)
├─ Instances: 2 (high availability)
├─ Auto Scaling: 2-10 based on CPU
├─ Load Balancer: Application Load Balancer
├─ Database: Amazon RDS (Multi-AZ)
└─ Cost: ~$74/month

  Breakdown:
  ├─ 2× t3.small: $30.88/month
  ├─ ALB: $16.20/month (+ $0.006/LCU)
  └─ Data transfer: ~$1-3/month
```

## Configuration Management

```
Environment properties:

Application variables:
├─ DATABASE_URL=db.example.com
├─ API_KEY=secret123
├─ ENVIRONMENT=production
└─ DEBUG=false

Platform-specific:
├─ Node.js: npm start script
├─ Python: WSGI application path
├─ Java: JAR file location
└─ Ruby: Gemfile and Procfile

Health checks:
├─ Target: /health endpoint
├─ Interval: Every 30 seconds
├─ Threshold: 3 consecutive failures
└─ Action: Mark unhealthy, replace
```

## Scaling Behavior

```
Auto Scaling policy (production):

Current: 3 instances, 40% average CPU
├─ CPUUtilization > 70%: Add 1 instance
├─ Wait 5 minutes
├─ Check again, add if still high
└─ Max instances: 10

Example spike:
├─ T0: 3 instances, 40% CPU
├─ T3: Spike! 85% CPU
├─ T8: +1 instance (4 total), CPU → 65%
├─ T13: Still high, +1 instance (5 total)
├─ T18: CPU → 45%, stable
└─ T1800: No change 30 min, -1 instance → 4

No human intervention needed!
```

## Best Practices

✅ Use rolling deployment for zero downtime
✅ Test in dev before prod deployment
✅ Monitor CloudWatch metrics
✅ Set up database backups (RDS integrated)
✅ Use SSL/TLS certificates
✅ Configure auto scaling appropriately
✅ Version your environments
✅ Use environment variables for config
✅ Enable access logs
✅ Regular environment updates

## Common Mistakes

✗ Using all-at-once in production (causes downtime)
✗ Not testing before deployment
✗ Over-sizing instances (wastes money)
✗ Not configuring health checks
✗ Storing secrets in code (use environment variables)
✗ Not monitoring logs
✗ Single instance production (no HA)

## Next Steps

→ [Deployments](./deployments.md) - Detailed strategies
→ [Database Integration](./database.md) - RDS setup
→ [Monitoring](./monitoring.md) - CloudWatch integration