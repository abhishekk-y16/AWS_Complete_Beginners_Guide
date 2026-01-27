# KMS & Encryption

TL;DR
- Use AWS KMS for key management, enable default encryption on supported services, and use IAM & KMS policies for access controls.

Prerequisites
- IAM permissions to create KMS keys and modify service encryption settings.

Steps
1. Create a symmetric KMS key and define key policy.
2. Enable service-side encryption using KMS (S3 SSE-KMS, EBS encryption, RDS KMS keys).
3. Rotate keys automatically or manually and audit key usage with CloudTrail.

Cost notes
- KMS has per-request charges for asymmetric keys and API usage; symmetric keys have lower cost.

Troubleshooting
- Access denied to encrypted resources: check KMS key policy, IAM policy, and any grants.

Checklist
- Keys created, services encrypted, rotation and audit enabled.
