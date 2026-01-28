# Cognito 🔐

Managed user authentication and authorization service for web and mobile applications.

## Overview

Cognito handles user sign-up, sign-in, and access control. Instead of building auth from scratch, get pre-built sign-up/login, MFA, social login (Google, Facebook, Apple), and password reset.

## Key Components

**User Pools**
- Store your users
- Password policies
- MFA enforcement
- Account lockout
- Custom attributes

**Identity Pools**
- Temporary AWS credentials
- Access S3, DynamoDB, Lambda
- For authenticated users & guests

**Hosted UI**
- Pre-built sign-in/sign-up page
- MFA setup
- Social login buttons
- Zero code needed!

## How It Works

```
User → Sign In Page → Cognito → Tokens → App Access
       (pre-built)              (JWT)
```

1. User enters email + password
2. Cognito validates
3. Issues tokens (Access, ID, Refresh)
4. Tokens stored in app
5. User makes API requests with token
6. Backend validates token with Cognito

## Features

✅ Password hashing (bcrypt)
✅ MFA (SMS, email, TOTP)
✅ Social login (Google, Facebook, Apple)
✅ Biometric login (mobile)
✅ Email verification
✅ Account lockout (brute force protection)
✅ Session management
✅ Audit logs

## Pricing

```
User Pools: First 50,000 MAU free, then $0.006/MAU
Example: 1M users = $5,700/month (cheaper than alternatives!)
```

## Common Use Cases

**Web Apps**: SaaS, dashboards, admin panels
**Mobile Apps**: Sign-up/login for iOS/Android
**Consumer Apps**: Millions of users with social login
**Enterprise**: Active Directory sync, SAML

## Authentication Flows

- **Sign Up**: Email + password → account created
- **Sign In**: Email + password + MFA
- **Social**: Click Google → auto-create account
- **Refresh**: Refresh token → new access token

## Best Practices

✅ Enable MFA for accounts
✅ Strong password policies
✅ Email verification
✅ Account lockout after 5 failures
✅ Use Identity Pools for AWS access
✅ Implement refresh token rotation
✅ Monitor sign-in attempts
✅ Log authentication events

## vs. Alternatives

```
Cognito: AWS-native, scales, integrated
Auth0: More features, easier start
Okta: Enterprise SSO
Manual: Full control, security risk
```

## Related Topics

- [Cognito Setup Guide](./what-is-cognito.md)
- [API Gateway Security](./api-gateway/README.md)
- [Lambda Authorizers](../../compute/lambda/what-is-lambda.md)

## Resources

- [Cognito Docs](https://docs.aws.amazon.com/cognito/)
- [Getting Started](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-getting-started.html)
- [Pricing](https://aws.amazon.com/cognito/pricing/)