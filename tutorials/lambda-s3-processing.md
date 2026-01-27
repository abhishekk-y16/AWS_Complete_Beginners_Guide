# Lambda + S3 Processing

TL;DR
- Trigger Lambda from S3 uploads to process images, documents, or events without servers.

Prerequisites
- S3 bucket, Lambda execution role with `s3:GetObject` and destination permissions, AWS CLI.

Steps
1. Create S3 bucket (e.g., `incoming-bucket`).
2. Create Lambda function (Python/Node) with handler reading `event['Records']` for S3 object info.
3. Add S3 trigger: Event type `PUT`, prefix/suffix filters as needed.
4. In code, download object via `boto3`/SDK, process, and write results to another bucket/prefix.
5. Set timeout/memory based on processing; add DLQ (SQS) for failures.

Cost notes
- Pay per Lambda execution + duration; S3 storage/requests. Keep objects small or batch.

Troubleshooting
- Trigger not firing: verify event notification enabled and correct suffix/prefix.
- Access denied: ensure bucket policy allows Lambda role or use OAI/OAC where needed.

Checklist
- Trigger active, role permissions set, DLQ configured, test event succeeds.