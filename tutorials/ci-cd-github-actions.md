# CI/CD with GitHub Actions

TL;DR
- Use GitHub Actions to build, test, and deploy to AWS using the `aws-actions/configure-aws-credentials` action.

Prerequisites
- GitHub repo, AWS IAM user or role for GitHub OIDC, and secrets configured for credentials.

Steps
1. Create `.github/workflows/ci.yml` with build and test steps.
2. Use `aws-actions/configure-aws-credentials` to set AWS credentials or configure OIDC.
3. Deploy artifacts to S3/CloudFormation/ECS from the workflow.

Cost notes
- GitHub Actions minutes and AWS deployment costs (ECR, S3, ECS/EKS) may apply.

Troubleshooting
- Permission errors: ensure proper IAM trust policy for OIDC or correct secrets for credentials.

Checklist
- Workflow runs green, artifacts deployed, secrets set.
