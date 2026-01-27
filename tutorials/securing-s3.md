# Securing S3

TL;DR
- Use bucket policies, block public access, enable encryption at rest, and enforce least privilege.

Prerequisites
- IAM with permissions to modify S3 policies and encryption settings.

Steps
1. Enable Block Public Access at account and bucket levels.
2. Configure S3 Bucket Policy to restrict access to specific principals and VPC endpoints.
3. Enable default encryption (SSE-S3 or SSE-KMS).
4. Enable versioning and lifecycle rules for retention and archival.

Cost notes
- Versioning increases storage; lifecycle rules can reduce long-term cost by moving data to Glacier.

Troubleshooting
- Access denied: check bucket policy, IAM principal, and KMS key policy.

Checklist
- Public access blocked, encryption enabled, versioning set.
