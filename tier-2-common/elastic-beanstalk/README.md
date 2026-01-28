# Elastic Beanstalk 🚀

Platform-as-a-Service (PaaS) for deploying and managing web applications without managing infrastructure.

## Overview

Elastic Beanstalk is like having a deployment butler. Upload your code (Node.js, Python, Java, Go, PHP, .NET, Ruby), it handles:
- EC2 instance creation
- Load balancing
- Auto-scaling
- Health monitoring
- Logging
- Database setup

You just push code. That's it.

## Supported Platforms

```
Node.js    → npm install, npm start
Python     → pip install, Flask/Django app
Java       → JAR/WAR files
Go         → Binary executable
PHP        → PHP code
.NET       → .NET Framework/Core
Ruby       → Ruby on Rails
Docker     → Your own container
```

## How It Works

```
Your Code
    ↓
Upload ZIP file
    ↓
Beanstalk creates:
├─ EC2 instance
├─ Load balancer
├─ Auto-scaling group
├─ RDS database (optional)
└─ CloudWatch monitoring
    ↓
Running Application
```

## Deployment Example

```bash
# Create environment
eb create my-app-env --instance-type t3.micro

# Deploy new version
eb deploy

# View logs
eb logs

# Monitor health
eb status

# Scale to 5 instances
eb scale 5
```

## Environments

**Development**:
- Single t3.micro instance
- No load balancer
- No auto-scaling
- ~$10-15/month

**Production**:
- Multiple instances (ALB)
- Auto-scaling group
- RDS database
- ~$100-200/month

## Application Example

**Node.js App**:
```javascript
// app.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(8080, () => {
  console.log('Server running on port 8080');
});
```

**package.json**:
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": {
    "start": "node app.js"
  }
}
```

Just zip both files → Upload to Beanstalk → Running!

## Architecture

```
Users
  ↓
Route 53 (DNS)
  ↓
Elastic Load Balancer (ALB)
  ↓
Auto-Scaling Group
├─ EC2 instance 1 (Node.js app)
├─ EC2 instance 2 (Node.js app)
└─ EC2 instance 3 (Node.js app)
  ↓
RDS (database)

CloudWatch monitors all
```

## Real-World Example

```
Web App: Personal Blog

Setup:
├─ Platform: Python (Flask)
├─ Instance Type: t3.small
├─ Instances: 2-4 (auto-scaling)
├─ Load Balancer: ALB
└─ Database: MySQL RDS

Monthly Cost:
├─ EC2 (avg 3 instances): $60
├─ ALB: $20
├─ RDS t3.small: $50
└─ Total: ~$130/month

Scale: 1000s of monthly users
```

## Pricing

```
Beanstalk itself: FREE (pay for resources)

You pay for:
├─ EC2 instances: $0.0416/hour (t3.micro)
├─ Load Balancer: $0.0225/hour
├─ RDS database: $0.0698/hour (t3.micro)
└─ Data transfer: $0.02/GB

Example:
├─ 2 t3.micro: $60/month
├─ ALB: $15/month
├─ t3.micro RDS: $50/month
└─ Total: ~$125/month
```

## Deployment Strategies

**All at Once**: Fastest but risky
- All instances replaced
- Brief downtime
- 1-2 minutes

**Rolling**: No downtime
- Replace 1/4 instances at a time
- 4-5 minutes
- Safer for production

**Blue/Green**: Zero downtime
- Create new environment
- Switch traffic
- 5-10 minutes
- Rollback easy

## Common Use Cases

- **Web Applications**: Traditional apps
- **APIs**: REST/GraphQL backends
- **Microservices**: Containerized apps
- **Worker Applications**: Processing queues

## When to Use Elastic Beanstalk

✅ Want to deploy without managing servers
✅ Traditional web applications
✅ Simple scaling requirements
✅ Team wants fast time-to-market

## When NOT to Use

❌ Complex infrastructure (use CloudFormation/CDK)
❌ Need full control (use EC2 directly)
❌ Serverless (use Lambda)
❌ High-performance computing

## Elastic Beanstalk vs Lambda

```
Beanstalk: Long-running apps, traditional deployment
Lambda: Event-driven, serverless, pay-per-execution
```

## Best Practices

✅ Use environment-specific configs
✅ Enable auto-scaling
✅ Regular backups of RDS
✅ Monitor with CloudWatch
✅ Use rolling deployments
✅ Test in dev environment
✅ Set up CI/CD pipeline
✅ Use .ebextensions for configuration

## Related Topics

- [What is Elastic Beanstalk](./what-is-elastic-beanstalk.md)
- [EC2 Instances](../compute/ec2/what-is-ec2.md)
- [Load Balancing](../networking/elastic-load-balancing/what-is-elb.md)
- [Lambda Functions](../compute/lambda/what-is-lambda.md)

## Resources

- [Elastic Beanstalk Docs](https://docs.aws.amazon.com/elasticbeanstalk/)
- [Getting Started](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html)
- [Deployment Options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy.overview.html)