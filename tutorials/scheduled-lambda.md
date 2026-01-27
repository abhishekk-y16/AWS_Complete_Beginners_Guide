# Scheduled Lambda (Cron)

TL;DR
- Run Lambda on a schedule using EventBridge cron/rate expressions for maintenance jobs, reports, or cleanup.

Prerequisites
- Lambda function created; IAM permissions for target actions.

Steps
1. Create or pick Lambda function; set timeout/memory appropriately.
2. In EventBridge → Rules, create a schedule rule (e.g., `rate(5 minutes)` or `cron(0 6 * * ? *)`).
3. Add the Lambda as target; enable dead-letter queue (SQS) and retry policy.
4. Add environment variables for parameters (dates, bucket names).
5. Monitor executions in CloudWatch Logs and Metrics; add alarms on errors.

Cost notes
- Pay for Lambda duration and EventBridge invocations (very low for cron).

Troubleshooting
- Function not triggering: ensure rule is enabled and correct region; check permissions on Lambda invoke.
- Multiple executions: avoid overlapping runs; add concurrency limit or idempotency checks.

Checklist
- Rule enabled, DLQ set, alarms configured, idempotency handled.