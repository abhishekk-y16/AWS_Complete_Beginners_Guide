# IAM Best Practices

TL;DR
- Apply least privilege, prefer IAM Roles over long-lived keys, use MFA for sensitive operations.
- Use IAM Access Analyzer and AWS Organizations SCPs to constrain permissions.

Prerequisites
- AWS account with administrative access to configure IAM.

Steps
1. Create groups and roles instead of assigning permissions directly to users.
2. Enable MFA for console access and require it for privileged roles.
3. Rotate access keys regularly and use IAM Roles for service-to-service access.
4. Use AWS Managed Policies where appropriate; create fine-grained custom policies when needed.
5. Configure password policies and set session durations for roles.

Cost notes
- IAM is free, but misconfigurations can cause high costs due to over-privileged automation.

Troubleshooting
- Access denied errors: use IAM Policy Simulator to debug effective permissions.

Checklist
- MFA enabled, roles used, policies reviewed, keys rotated.
