# CloudWatch 📊

Monitoring and observability service for AWS resources and applications.

## Overview

CloudWatch collects metrics from AWS services, stores application logs, and triggers alarms. Think of it as your central dashboard for everything happening in AWS.

## Three Core Features

1. **Metrics**: CPU, network, requests, connections
   - 15-month retention
   - 1-second to 1-minute granularity
   - Free for basic metrics

2. **Logs**: Application/system logs
   - Real-time streaming
   - Log Insights (SQL-like queries)
   - 5+ years retention

3. **Alarms**: "Alert me if X happens"
   - SNS notifications (email, SMS)
   - Lambda automation (auto-remediate)
   - Auto Scaling integration

## Key Metrics by Service

**EC2**: CPUUtilization, NetworkIn, DiskOps, StatusCheck
**RDS**: DatabaseConnections, FreeStorage, ReadLatency
**Lambda**: Invocations, Errors, Duration, ConcurrentExecutions
**API Gateway**: Count, 4XXError, 5XXError, Latency

## CloudWatch Logs Insights

SQL-like queries on logs:

```sql
fields @timestamp, @message | filter @message like /ERROR/ | stats count()
fields @duration | filter @duration > 1000 | stats avg(@duration)
fields @statusCode | stats count() by @statusCode
```

## Alarms Example

```
High CPU Alert:
├─ If CPUUtilization > 80% for 2 minutes
├─ Send email notification
└─ Auto-scale EC2 (add instance)

Disk Full Alert:
├─ If DiskSpace > 90%
├─ Run Lambda (cleanup)
└─ Page oncall engineer
```

## Pricing

```
Metrics: $0.10 per metric/month (detailed 1-min)
Logs: $0.50/GB ingestion + $0.03/GB storage/month
Alarms: $0.10 per alarm/month
```

Example: 10 EC2 instances + 100GB logs = ~$60/month

## Dashboards

Create custom dashboards visualizing:
- Real-time metrics
- Historical trends
- Alert status
- Share with team

## Best Practices

✅ Set up alarms for critical metrics
✅ Use CloudWatch Logs for debugging
✅ Create dashboards for common views
✅ Enable retention policies (save costs)
✅ Use Log Insights for troubleshooting
✅ Integrate with SNS for alerts
✅ Monitor costs with Cost Anomaly Detection
✅ Set up X-Ray for detailed tracing

## Related Topics

- [CloudWatch Guide](./what-is-cloudwatch.md)
- [EC2 Monitoring](../../compute/ec2/what-is-ec2.md)
- [Lambda Monitoring](../../compute/lambda/what-is-lambda.md)
- [Auto Scaling](./auto-scaling/README.md)

## Resources

- [CloudWatch Docs](https://docs.aws.amazon.com/cloudwatch/)
- [Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)