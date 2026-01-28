# What is CloudWatch? 📊

Monitor, log, and visualize AWS infrastructure and applications.

## Core Concept

**CloudWatch** collects metrics, logs, and events from your AWS resources, giving you complete visibility.

```
Without CloudWatch:
├─ Server crashes → You don't know until users complain
├─ Performance degrades → No visibility
├─ Errors accumulate → Discover after data loss
└─ Problem: Flying blind!

With CloudWatch:
├─ Real-time metrics dashboard
├─ Automated alerts when problems occur
├─ Logs searchable and analyzable
└─ Solution: See everything happening!
```

## Three Pillars of CloudWatch

### 1. Metrics

Numerical measurements over time (CPU, memory, network, custom).

```
EC2 Instance Metrics:
├─ CPU Utilization (0-100%)
├─ Network bytes in/out
├─ Disk read/write operations
├─ Status checks (healthy/unhealthy)
└─ Storage space (EBS attached)

Database Metrics:
├─ Query latency
├─ Connections count
├─ Replication lag
└─ CPU/Memory usage

Custom Metrics:
├─ Application requests/second
├─ Cache hit rate
├─ Business metrics (sales, conversions)
└─ Any data you can send!
```

### 2. Logs

Text data from applications and infrastructure.

```
Log Sources:
├─ Application logs
│  ├─ Errors and warnings
│  ├─ Debug information
│  └─ Business events
├─ System logs
│  ├─ Security events
│  ├─ Access logs
│  └─ Performance data
└─ VPC Flow Logs
   └─ Network traffic capture
```

### 3. Events

Trigger-based notifications when things happen.

```
CloudWatch Events:
├─ EC2 instance launches/terminates
├─ RDS backup completes
├─ Lambda function fails
├─ Scheduled events (cron-like)
└─ Custom application events
```

## Metrics Deep Dive

### Built-in Metrics

All AWS services automatically send metrics:

```
Free Metrics (No cost):
├─ EC2: CPU, network (5-minute granularity)
├─ RDS: CPU, storage, connections
├─ S3: Number of objects, bucket size
├─ Lambda: Invocations, errors, duration
└─ Most AWS services

Detailed Metrics (Paid):
├─ EC2: 1-minute granularity
├─ Additional dimensions
└─ Cost: ~$0.10 per metric/month
```

### Metric Dashboard Example

```yaml
Dashboard: "Production Application"
├─ Widget 1: EC2 CPU
│  ├─ Instance 1: 45%
│  ├─ Instance 2: 32%
│  └─ Instance 3: 51%
├─ Widget 2: RDS Connections
│  └─ Active: 234 connections
├─ Widget 3: Lambda Errors
│  └─ Last hour: 3 errors
└─ Widget 4: S3 Bytes
   └─ Total stored: 2.5 TB
```

### Custom Metrics

Send application-specific data:

```python
import boto3

cloudwatch = boto3.client('cloudwatch')

# Send custom metric
cloudwatch.put_metric_data(
    Namespace='MyApp',
    MetricData=[
        {
            'MetricName': 'ProcessedOrders',
            'Value': 125,
            'Unit': 'Count',
            'Timestamp': datetime.utcnow()
        },
        {
            'MetricName': 'AvgOrderValue',
            'Value': 89.50,
            'Unit': 'None',
            'Timestamp': datetime.utcnow()
        }
    ]
)

# Query metric in dashboard
```

## Logs Management

### CloudWatch Logs

```
Log Group: Collection of log streams
└─ Log Stream: From single application instance
   ├─ 2024-01-15 10:00:01 INFO: Starting app
   ├─ 2024-01-15 10:00:02 INFO: Connected to DB
   ├─ 2024-01-15 10:05:23 ERROR: Query timeout
   └─ 2024-01-15 10:05:24 INFO: Retrying...
```

### Log Retention

```
CloudWatch Logs retention:
├─ Default: Never expire
├─ Custom: 1 day, 7 days, 30 days, 1 year, etc.
├─ Older logs can be exported to S3

Cost:
├─ $0.50 per GB ingested
├─ $0.03 per GB stored per month
└─ Example: 100GB/month = $50 + $3/month storage
```

### Log Insights

Search and analyze logs efficiently:

```sql
# Find all errors in last hour
fields @timestamp, @message, @logStream
| filter @message like /ERROR/
| stats count() by @logStream

# Find slow API requests
fields @duration
| filter @message like /api/
| filter @duration > 1000
| stats avg(@duration), max(@duration) by @logStream

# Top error types
fields @message
| filter @message like /ERROR/
| stats count() as error_count by @message
| sort error_count desc
```

## Alarms

Trigger actions when thresholds are breached.

```
Alarm: "High CPU Alert"
├─ Metric: EC2 CPU Utilization
├─ Threshold: > 80%
├─ Duration: 5 minutes
├─ Action:
│  ├─ Send SNS email notification
│  ├─ Trigger Auto Scaling (add more instances)
│  └─ Create PagerDuty incident
└─ Result: Automatic response to problems!
```

### Setting Alarms

```python
cloudwatch = boto3.client('cloudwatch')

# Create alarm
cloudwatch.put_metric_alarm(
    AlarmName='HighCPU',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,  # 5 minutes
    EvaluationPeriods=2,  # Check twice
    Threshold=80,
    ComparisonOperator='GreaterThanThreshold',
    AlarmActions=['arn:aws:sns:us-east-1:123456789:my-topic']
)
```

### Alarm States

```
OK: Everything normal
├─ No alert necessary
└─ Green status

ALARM: Threshold breached
├─ Send notification
├─ Execute actions
└─ Red status

INSUFFICIENT_DATA: Not enough data
├─ Recently created alarm
├─ No action taken
└─ Gray status
```

## Real-World Example: E-commerce App

```
Production Stack:
├─ 5 EC2 web servers
├─ RDS MySQL database
├─ ElastiCache Redis
├─ S3 assets
└─ CloudFront CDN

CloudWatch Setup:
├─ Dashboard: Real-time visibility
│  ├─ EC2 CPU (alert if >75%)
│  ├─ RDS connections (alert if >500)
│  ├─ Cache hit rate (should >85%)
│  └─ HTTP response time (alert if >500ms)
├─ Logs: All application errors
│  ├─ Parse payment failures
│  ├─ Database timeouts
│  └─ User session issues
├─ Events: Triggered actions
│  ├─ Scale up if CPU >75%
│  ├─ Send alert if RDS connection timeout
│  └─ Scheduled backup verification
└─ Result: 99.9% uptime, instant problem detection!
```

## Cost Analysis

```
Scenario: Typical web application

Metrics:
├─ 10 EC2 instances (free tier)
├─ RDS database (free tier)
├─ 5 custom metrics (paid)
├─ Cost: 5 × $0.10 = $0.50/month

Logs:
├─ 50GB/month ingested: 50 × $0.50 = $25
├─ Storage (7-day retention): 50 × $0.03 = $1.50
└─ Subtotal: $26.50/month

Alarms:
├─ 20 alarms (free!)
└─ Cost: $0

Total: ~$27/month for complete monitoring!
(Usually covered by free tier for small apps)
```

## Anomaly Detection

CloudWatch automatically learns normal behavior:

```
Machine Learning Alarm:
├─ Monitors: Network traffic, CPU, latency
├─ Learns: Normal patterns over 2 weeks
├─ Detects: Unusual spikes automatically
└─ Alerts: When behavior deviates from normal

Example:
├─ Normal traffic: 1000 requests/min
├─ Anomaly: 5000 requests/min (5x spike)
└─ Alert: Possible DDoS attack! Investigate.
```

## Dashboards

Create custom monitoring views:

```
Sales Dashboard:
├─ Orders processed (custom metric)
├─ Revenue (custom metric)
├─ Failed transactions (custom metric)
└─ Real-time updates

Operations Dashboard:
├─ EC2 CPU and memory
├─ Database connections and lag
├─ Error rates across all services
└─ Auto-refresh every 1 minute
```

## Integration with Other Services

```
CloudWatch → SNS: Email/SMS alerts
CloudWatch → Auto Scaling: Add/remove instances
CloudWatch → Lambda: Trigger functions
CloudWatch → EventBridge: Route to any service
CloudWatch → Third-party: Datadog, New Relic, etc.

Example Flow:
1. EC2 CPU > 80%
2. CloudWatch detects
3. Triggers Auto Scaling Group
4. Adds 2 new instances
5. Sends SNS alert to ops team
6. Logs event for audit
```

## Common Mistakes

### ✗ Mistake 1: Not Setting Alarms

```
Wrong:
├─ Collect metrics but no alarms
├─ Problems occur
└─ Discover much later (users complain!)

Right:
├─ Alert when CPU > 80%
├─ Alert when errors > 10/minute
├─ Alert when database lag > 30 seconds
└─ Instant notification of problems!
```

### ✗ Mistake 2: Alert Fatigue

```
Wrong:
├─ Set alarms too sensitive
├─ Receive 100 alerts/day
├─ Everyone ignores alerts
└─ Missing real problems!

Right:
├─ Carefully tuned thresholds
├─ Only critical issues alert
├─ Alert baselines reviewed weekly
└─ Alarms actually useful!
```

### ✗ Mistake 3: No Retention Policy

```
Wrong:
├─ Keep all logs indefinitely
├─ Storage cost increases monthly
└─ Searching becomes slow

Right:
├─ Retention policy based on needs
│  ├─ Recent logs: 30 days
│  ├─ Archive: Export to S3
│  └─ Delete very old logs
└─ Controlled costs, fast queries
```

### ✗ Mistake 4: Alert Without Action

```
Wrong:
├─ Alarm triggers
├─ Email sent
├─ No automatic response
└─ Manual investigation (slow!)

Right:
├─ Alarm triggers
├─ Auto Scaling adds instances
├─ PagerDuty alerts on-call engineer
├─ Logs captured for investigation
└─ Problem handled automatically!
```

## Best Practices

✅ Create comprehensive dashboards
✅ Set meaningful alarms with thresholds
✅ Establish log retention policies
✅ Use CloudWatch Insights for analysis
✅ Automate responses to common issues
✅ Review alarms monthly
✅ Enable detailed monitoring for critical services
✅ Archive old logs to S3
✅ Use custom metrics for business visibility
✅ Document alarm purposes

## CLI Examples

```bash
# Create alarm
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU \
  --alarm-description "Alert when CPU high" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold

# List alarms
aws cloudwatch describe-alarms

# Get metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --start-time 2024-01-15T00:00:00Z \
  --end-time 2024-01-15T01:00:00Z \
  --period 300 \
  --statistics Average

# Put log events
aws logs put-log-events \
  --log-group-name /aws/lambda/my-function \
  --log-stream-name 2024/01/15/[$LATEST]abc123
```

## Pricing Summary

```
Monthly bill (typical app):
├─ Metrics: $0.50 (5 custom)
├─ Logs ingestion: $25 (50GB)
├─ Logs storage: $1.50 (7-day retention)
├─ Alarms: Free (20 alarms)
└─ Total: ~$27/month

Free tier includes:
├─ Standard metrics from all AWS services
├─ 3 dashboards
├─ 10 alarms
└─ Some log storage
```

## Next Steps

→ [CloudWatch Metrics Deep Dive](./metrics.md) - Advanced metrics
→ [CloudWatch Logs & Insights](./logs.md) - Log analysis
→ [Alarms & Events](./alarms.md) - Automation setup