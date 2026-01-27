# Monitoring Setup

TL;DR
- Use CloudWatch for metrics/logs and CloudWatch Alarms for thresholds.
- Aggregate logs with CloudWatch Logs, use Metric Filters and Dashboards.
- Use CloudWatch Agent on EC2 for system metrics and X-Ray for tracing.

Prerequisites
- IAM role with permissions to write logs/metrics.

Steps
1. Install CloudWatch Agent on EC2 instances or configure the agent in Systems Manager.
2. Create log groups and set retention policies:
```
aws logs create-log-group --log-group-name /my-app/logs
aws logs put-retention-policy --log-group-name /my-app/logs --retention-in-days 30
```
3. Create Metric Filters to emit metrics from logs.
4. Create Alarms for key metrics (CPU, errors, latency) and configure SNS notifications.
5. Build Dashboards to visualize service health and create automated runbooks.

Cost notes
- CloudWatch costs include Logs ingestion, custom metrics, dashboards, and alarms. Optimize retention and use metric filters sparingly.

Troubleshooting
- Missing logs: verify agent configuration and IAM permissions.
- High costs: reduce log retention, set filter limits, or use subscription filters to Kinesis/Firehose to archive cheaper.

Checklist
- Agents installed, log groups created, alarms configured, dashboards live.
