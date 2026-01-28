# KMS - Key Management Service 🔐

Managed encryption key service for protecting data at rest and in transit.

## Overview

KMS manages cryptographic keys for encrypting/decrypting data. Create keys, control who uses them, audit access. AWS handles key storage, rotation, and security.

## Key Concepts

**Master Key**: Main encryption key (lives in KMS, never exported)
**Data Key**: Generated from Master Key, used to encrypt/decrypt data
**Encryption**: Convert plaintext → ciphertext (protect data)
**Decryption**: Convert ciphertext → plaintext (with correct key)

## How Encryption Works

```
Plaintext Data (confidential)
    ↓
Request Master Key (from KMS)
    ↓
KMS checks permissions
    ↓
Returns Data Key
    ↓
App encrypts with Data Key
    ↓
Ciphertext (protected!)
```

## Key Types

**AWS Managed Keys**: Free
- Automatically created by AWS services
- AWS manages rotation
- Limited control
- Example: s3/default

**Customer Managed Keys**: Pay-per-use
- Full control over rotation
- Custom key policies
- Enable/disable at will
- Audit all usage
- ~$1/month per key

**KMS Imported Keys**: Bring your own key
- Import key material
- You manage rotation
- $1/month

## Example: Encrypt an S3 Object

```bash
# Create KMS key
aws kms create-key --description "S3 encryption"

# Get key ID
KEY_ID="arn:aws:kms:us-east-1:123456789:key/abc123"

# Upload encrypted file to S3
aws s3 cp secret.txt s3://my-bucket/ \
  --sse aws:kms \
  --sse-kms-key-id $KEY_ID

# S3 automatically encrypts with KMS key!
# Only users with KMS decrypt permission can read
```

## Encryption in AWS Services

```
S3 Objects
    ↓ Use KMS
    ↓
EBS Volumes
    ↓ Use KMS
    ↓
RDS Databases
    ↓ Use KMS
    ↓
CloudTrail Logs
    ↓ Use KMS
    ↓
Lambda Environment Variables
    ↓ Use KMS
```

## Key Policies & IAM

KMS uses two layers:
1. **Key Policy**: Who can use key
2. **IAM Permissions**: Who can call KMS API

```
User wants to decrypt data:

✅ Has IAM permission to call kms:Decrypt
  AND
✅ Key policy allows their principal
  
= User can decrypt

❌ Only IAM permission
= Can't decrypt (Key policy denies)

❌ Only Key policy allows
= Can't decrypt (No IAM permission)
```

## Example Key Policy

```json
{
  "Sid": "Allow account root",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::123456789:root"
  },
  "Action": "kms:*",
  "Resource": "*"
}
```

## Key Rotation

**Automatic**: AWS manages
- Every 365 days
- Free for AWS managed keys
- For customer managed: $1/rotation

**Manual**: You can rotate anytime
- Create new key version
- Old versions still work (decrypt)
- New data uses new version

## Real-World Example

```
SaaS Application: Customer Data Storage

Requirements:
├─ Encrypt customer data at rest
├─ Each customer has their own key
├─ Audit who accesses keys
└─ Comply with regulations

Setup:
├─ Create 100s of customer-specific keys
├─ S3 stores data encrypted with customer key
├─ App has IAM role to call kms:Decrypt
├─ KMS logs to CloudTrail (who decrypted what)
├─ If customer data breached: Disable their key!

Cost: 100 keys × $1/month = $100/month
```

## Pricing

```
Customer Managed Keys:
├─ Key storage: $1.00/month per key
├─ API requests: $0.03 per 10K requests
└─ Key rotation: $1.00 per rotation

AWS Managed Keys:
├─ No charge!
└─ Automatic rotation included

Example:
├─ 5 customer keys: $5/month
├─ 100K encrypt requests: $0.30/month
├─ 100K decrypt requests: $0.30/month
└─ Total: ~$5.60/month
```

## Common Use Cases

- **S3 Encryption**: KMS encrypts objects
- **RDS Encryption**: Encrypt database at rest
- **Secrets Manager**: Encrypt secrets (uses KMS internally)
- **EBS Snapshots**: Encrypted backups
- **Application Encryption**: App calls KMS to encrypt sensitive data

## When to Use KMS

✅ Need encryption at rest
✅ Require key management/rotation
✅ Audit trail requirements
✅ Regulatory compliance (HIPAA, PCI-DSS)
✅ Multi-tenant application

## When NOT to Use KMS

❌ Simple passwords (use Secrets Manager instead)
❌ TLS certificates (use ACM)
❌ Not encrypting sensitive data
❌ Performance-critical decryption (latency)

## Best Practices

✅ Use customer managed keys for sensitive data
✅ Enable CloudTrail logging
✅ Separate keys by application/environment
✅ Use key policies + IAM for defense in depth
✅ Enable automatic key rotation
✅ Regularly audit key usage
✅ Use envelope encryption (encrypt data key with master key)
✅ Don't hardcode key IDs

## Related Topics

- [What is KMS](./what-is-kms.md)
- [Secrets Manager](./secrets-manager/what-is-secrets-manager.md)
- [S3 Encryption](../storage/s3/encryption.md)
- [RDS Encryption](../database/rds/security.md)

## Resources

- [KMS Documentation](https://docs.aws.amazon.com/kms/)
- [KMS Best Practices](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html)
- [Key Policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)