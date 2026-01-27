# SQS Queue Patterns

TL;DR
- Use SQS for decoupling; combine with SNS for fan-out and Lambda for event-driven processing.

Prerequisites
- IAM permissions to create SQS queues and SNS topics.

Steps
1. Create standard or FIFO queue depending on ordering needs.
```
aws sqs create-queue --queue-name MyQueue
```
2. Configure dead-letter queues for failed messages and set redrive policy.
3. Use long polling to reduce empty receives and lower costs.

Cost notes
- SQS costs are per request; long polling reduces unnecessary requests.

Troubleshooting
- Message visibility issues: adjust visibility timeout and ensure consumers delete messages after processing.

Checklist
- DLQ configured, long polling enabled, monitoring set.
