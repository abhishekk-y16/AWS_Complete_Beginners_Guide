# Cognito vs IAM

When to use
- **Cognito**: end-user authentication (web/mobile), social login, hosted UI.
- **IAM**: permissions for AWS users/roles, service-to-service access.

Quick compare
| Feature | Cognito | IAM |
|---------|---------|-----|
| Audience | App end-users | Admins, workloads |
| Credentials | JWT tokens, SRP | Access keys, roles, STS |
| Federation | Social/OIDC/SAML | SAML/OIDC for workforce |
| Pricing | MAU-based | Free (ops driven) |

Guidance
- Use Cognito User Pools/Hosted UI for sign-up/sign-in; IAM roles for backend resources; connect via Cognito Identity Pools to issue AWS creds to users.