# Auto Scaling 📈

Automatically add/remove EC2 instances based on demand to keep performance consistent and costs optimized.

## Overview

Auto Scaling watches metrics (CPU, memory, connections) and adjusts instance count:
- High demand → Add instances
- Low demand → Remove instances
- Always right-sized
- No manual scaling needed

## Architecture

```
Users
  ↓ Load increases
  ↓
CloudWatch detects high CPU (>70%)
  ↓
Auto Scaling triggers
  ↓
Launches 2 new EC2 instances
  ↓
Load Balancer distributes traffic
  ↓
Load decreases
  ↓
Idle instances removed after 5 minutes
  ↓
Cost optimized!
```

## Core Components

**Launch Template**: How to create instances
- AMI (image)
- Instance type (t3.small)
- Security groups
- Storage
- IAM role

**Auto Scaling Group**: Container for instance management
- Min instances: 2
- Desired capacity: 3
- Max instances: 5

**Scaling Policies**: When to add/remove
- Scale up at 70% CPU
- Scale down at 20% CPU
- Cooldown period: 5 minutes

**Load Balancer**: Distribute traffic
- Health checks
- Route to healthy instances

## Real-World Example

```
Web Application Scaling:

Off-Peak (2am-6am):
├─ 1 instance running
├─ CPU: 5-10%
├─ Cost: $0.05/hour

Peak Hours (8am-6pm):
├─ Initial: 2 instances, CPU 85%
├─ Scale up: Add instance, CPU 75%
├─ Add another: 4 instances, CPU 60%
├─ Cost: $0.20/hour

Night (8pm-2am):
├─ Scale down: Remove instances
├─ Back to 1 instance
├─ Cost: $0.05/hour
```

## Scaling Policies

**Target Tracking**: Simplest
```
"Keep CPU at 70%"

Auto Scaling calculates:
├─ Current: 80% CPU
├─ Need more capacity
├─ Add instance
├─ New: 70% CPU ✓
```

**Step Scaling**: Granular control
```
CPU 70-80% → Add 1 instance
CPU 80-90% → Add 2 instances
CPU 90%+  → Add 3 instances

CPU <40%  → Remove 1 instance
```

**Scheduled Scaling**: Time-based
```
Every weekday at 7am:
  → Scale to 5 instances

Every weekday at 6pm:
  → Scale down to 2 instances

Every weekend:
  → Minimum 1 instance
```

## Metrics to Monitor

**CPU Utilization**:
- >70% → Scale up
- <30% → Scale down

**Memory**: Custom metric
- App sends memory % to CloudWatch
- >75% → Add instance

**Network I/O**: Data throughput
- Predict spikes

**Custom Metrics**: Your own
- Database connections
- Queue length
- User sessions

## Configuration Example

```bash
# Create launch template
aws ec2 create-launch-template \
  --launch-template-name web-app \
  --launch-template-data '{
    "ImageId": "ami-12345",
    "InstanceType": "t3.small",
    "SecurityGroupIds": ["sg-12345"]
  }'

# Create auto scaling group
aws autoscaling create-auto-scaling-group \
  --auto-scaling-group-name web-asg \
  --launch-template LaunchTemplateName=web-app \
  --min-size 2 \
  --desired-capacity 3 \
  --max-size 5 \
  --load-balancer-names my-alb

# Add scaling policy
aws autoscaling put-scaling-policy \
  --auto-scaling-group-name web-asg \
  --policy-name scale-up \
  --policy-type TargetTrackingScaling \
  --target-tracking-configuration '{
    "TargetValue": 70.0,
    "PredefinedMetricSpecification": {
      "PredefinedMetricType": "ASGAverageCPUUtilization"
    }
  }'
```

## Lifecycle

```
Instance Launch
  ↓
In Service (handling traffic)
  ↓
CloudWatch monitors
  ↓
--- Demand drops ---
  ↓
Cooldown period (5 mins)
  ↓
Still low usage?
  ↓
Terminate instance
  ↓
Instance Terminated
```

## Pricing

```
Auto Scaling itself: FREE

You pay for:
├─ EC2 instances: $0.0416/hour (t3.micro)
├─ Load Balancer: $0.0225/hour
└─ CloudWatch alarms: $0.10/month

Example: Web app
├─ 2-5 instances (avg 3): $60/month
├─ ALB: $15/month
├─ CloudWatch alarms: $1/month
└─ Total: ~$76/month
```

## Benefits

✅ **Cost Optimization**: Only pay for what you need
✅ **High Availability**: Automatic replacement of failed instances
✅ **Performance**: Always adequate capacity
✅ **Hands-off**: No manual scaling
✅ **Flexibility**: Works with any AWS service

## When to Use Auto Scaling

✅ Traffic varies (web apps)
✅ Batch processing
✅ Database read replicas
✅ Need high availability
✅ Predictable traffic patterns

## When NOT to Use

❌ Stateful applications (sticky sessions)
❌ Fixed capacity needed
❌ Serverless (use Lambda instead)

## Auto Scaling vs Load Balancing

```
Load Balancer: Distributes traffic across instances
Auto Scaling: Adds/removes instances based on demand

Both needed for scalable applications!
```

## Best Practices

✅ Set appropriate min/max instances
✅ Use health checks
✅ Monitor scaling events
✅ Test with load tools
✅ Set cooldown period (avoid thrashing)
✅ Use CloudWatch dashboard
✅ Document scaling policies
✅ Regular capacity reviews

## Related Topics

- [EC2 Instances](../compute/ec2/what-is-ec2.md)
- [Load Balancing](../networking/elastic-load-balancing/what-is-elb.md)
- [CloudWatch Monitoring](../cloudwatch/what-is-cloudwatch.md)
- [Elastic Beanstalk](../compute/elastic-beanstalk/what-is-elastic-beanstalk.md)

## Resources

- [Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/)
- [Getting Started](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)
- [Scaling Policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)