# IAM Basics 🔐

Identity and Access Management — controlling who can do what in AWS.

## What is IAM?

Think of IAM as your AWS security gate: it controls authentication (who), authorization (what), and resource scope (which).

IAM is free to use and is essential for secure AWS operations.

## Core Concepts

- Users: individual identities for people or applications.
- Groups: collections of users that inherit group policies.
- Roles: temporary credentials assumed by services or users for specific tasks.
- Policies: JSON documents that Allow or Deny actions on resources.

## Quick Examples

S3 read-only policy (conceptual):

```
Effect: Allow
Action: s3:GetObject, s3:ListBucket
Resource: arn:aws:s3:::my-bucket and arn:aws:s3:::my-bucket/*
```

Use Roles for applications (Lambda, EC2) instead of embedding access keys in code.

## Best Practices (short)

- Never use the root account for daily tasks; secure root with MFA.
- Create an admin IAM user and enable MFA.
- Follow least-privilege: start with no permissions and add as required.
- Use groups to manage permissions at scale.
- Rotate credentials and delete unused access keys.
- Enable CloudTrail for auditing and logging.

## Creating a User (summary)

1. Console → IAM → Users → Create user
2. Provide console access, set password policy
3. Attach least-privilege policies or add to groups
4. Record credentials securely and test login

## When to use which policy type

- AWS Managed: simple, maintained by AWS (use when suitable)
- Customer Managed: custom and reusable across accounts
- Inline: attached directly to a single identity — avoid when possible

## Troubleshooting tips

- If access is denied: check attached policies, group membership, SCPs (Organizations), and permission boundaries.
- Use IAM Access Analyzer to find overly permissive policies.

## Links

- Security checklist: ../best-practices/security-checklist.md
- IAM docs: https://docs.aws.amazon.com/iam/