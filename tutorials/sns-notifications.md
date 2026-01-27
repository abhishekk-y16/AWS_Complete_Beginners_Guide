# SNS Notifications

TL;DR
- Use SNS for pub/sub messaging and fan-out to multiple subscribers (email, Lambda, SQS, HTTP).

Prerequisites
- IAM permissions to create topics and subscriptions.

Steps
1. Create an SNS topic and subscribe endpoints:
```
aws sns create-topic --name my-topic
aws sns subscribe --topic-arn arn:aws:sns:... --protocol email --notification-endpoint user@example.com
```
2. Set topic policies for cross-account or cross-service publishing.
3. Integrate with CloudWatch Alarms or Lambda for notifications.

Cost notes
- SNS has per-request costs; SMS messages and mobile push have different pricing.

Troubleshooting
- Email subscriptions require confirmation; use `ListSubscriptionsByTopic` to check status.

Checklist
- Topic created, subscribers verified, policies set.
