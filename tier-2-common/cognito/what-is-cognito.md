# What is Cognito? 🔐

User authentication, authorization, and identity management without building your own auth system.

## Core Concept

**Cognito** handles user sign-up, sign-in, and access control for your applications.

```
Without Cognito:
├─ Build own user database
├─ Build login/signup forms
├─ Handle password hashing (security risk!)
├─ Implement password reset (complex)
├─ Manage sessions (security headache)
├─ Handle multi-factor auth (complicated)
└─ Result: Weeks of work, security vulnerabilities!

With Cognito:
├─ User pools (pre-built auth)
├─ Login/signup out-of-the-box
├─ Password security (AWS handles)
├─ MFA built-in
├─ Social login (Google, Facebook, etc.)
└─ Result: Deploy in hours, battle-tested security!
```

## Two Main Components

### 1. User Pools

Manage user authentication and user data.

```
User Pool: "MyApp Users"
├─ User Directory:
│  ├─ john@example.com (password)
│  ├─ jane@example.com (password)
│  └─ bob@example.com (Google login)
├─ Sign-up/Sign-in UI
├─ Password policy enforcement
├─ MFA options (SMS, email, authenticator)
├─ User attributes (email, phone, custom)
└─ Groups (Admin, User, Premium)
```

### 2. Identity Pools

Map authentication to AWS credentials and access resources.

```
Identity Pool: "AWS Access"
├─ Map: Cognito user → AWS credentials
├─ Permissions: What can user access?
│  ├─ S3 bucket for photos
│  ├─ DynamoDB table
│  └─ Lambda functions
└─ Session duration: 15 minutes
```

## User Pool Workflow

```
Step 1: User visits app
    ↓
Step 2: Click "Sign Up"
    ↓
Step 3: Cognito hosted UI appears
    ├─ Email: user@example.com
    ├─ Password: (meets requirements)
    └─ Confirm: Click link in email
    ↓
Step 4: User authenticated
    ├─ Get ID token (user info)
    ├─ Get Access token (permissions)
    └─ Get Refresh token (session)
    ↓
Step 5: Access app
    ├─ Token sent with every request
    └─ App verifies token
    ↓
Result: Secure authentication!
```

## Authentication Methods

### Username & Password

```
Traditional login:
├─ Email or username
├─ Password (encrypted transmission)
└─ Verified via email/SMS
```

### Social Login

```
Connect existing social accounts:
├─ Google
├─ Facebook
├─ Apple
└─ Automatically create user account
```

### Federated Identity

```
Use enterprise identity:
├─ Active Directory
├─ SAML providers
├─ OpenID Connect
└─ OAuth
```

### Passwordless

```
Eliminate passwords:
├─ Email verification code
├─ SMS verification code
├─ TOTP (Time-based One-Time Password)
└─ No password to remember!
```

## Multi-Factor Authentication (MFA)

Extra layer of security:

```
SMS MFA:
├─ User enters password
├─ Cognito sends SMS: "Your code: 123456"
├─ User enters code
└─ Authenticated!

TOTP MFA:
├─ User scans QR with authenticator app
├─ App generates 6-digit code every 30 seconds
└─ User enters code

Backup Codes:
├─ If phone lost, use backup codes
└─ Saved during setup
```

## Real-World Example: SaaS Application

```
App: Project Management Tool

User Journey:

1. Sign Up:
   ├─ Enter email
   ├─ Enter password
   ├─ Verify email
   └─ Account created (auto in Cognito)

2. First Login:
   ├─ Email + password
   ├─ Enable MFA (optional)
   ├─ Get JWT tokens
   └─ Access app

3. Every API Call:
   ├─ Send JWT token
   ├─ API verifies token with Cognito
   ├─ Token valid? Grant access
   └─ Token expired? Ask to refresh

4. Access Control:
   ├─ Admin group → Can delete projects
   ├─ User group → Can only edit own projects
   ├─ View-only group → Read-only access
   └─ Enforced by Cognito groups

5. Password Reset:
   ├─ User clicks "Forgot Password"
   ├─ Cognito sends email link
   ├─ User sets new password
   └─ Automatic update

Result: Professional authentication system!
```

## Security Features

### Password Policies

```
Enforce strong passwords:
├─ Minimum length: 8 characters
├─ Uppercase: At least 1 (A-Z)
├─ Lowercase: At least 1 (a-z)
├─ Numbers: At least 1 (0-9)
├─ Special characters: At least 1 (!@#$%^&*)
└─ Not previous passwords (configurable)
```

### Account Lockout

```
After failed login attempts:
├─ 1-5 failed attempts: No action
├─ 5+ failed attempts: Lock account
├─ Lock duration: 15 minutes
├─ User receives notification
└─ Auto-unlock or admin unlock
```

### Compromised Credentials

```
Automatic detection:
├─ Cognito detects leaked passwords
├─ User forced to change password
├─ SMS/email sent to user
└─ Account re-secured
```

### Session Management

```
Token expiration:
├─ ID token: 1 hour
├─ Access token: 1 hour
├─ Refresh token: 30 days
└─ Can refresh before expiration

Token revocation:
├─ User logout
├─ All tokens invalidated
└─ Sign-out across all devices
```

## Pricing

```
Monthly costs (10,000 active users):

User Pool:
├─ MAU (Monthly Active Users): 10,000
├─ Cost: $0.015 per MAU
└─ Total: 10,000 × $0.015 = $150

Identity Pool:
├─ Unauthenticated logins: Free tier
├─ Authenticated: Included in User Pool
└─ Cost: $0

MFA (SMS):
├─ 100,000 SMS sent
├─ Cost: $0.00075 per SMS
└─ Total: $75

Advanced Threats Protection:
├─ Cost: $0.02 per MAU
└─ Total: $200

Total: ~$425/month
```

## Common Mistakes

### ✗ Mistake 1: Exposing Client Secrets

```
Wrong:
├─ Store AWS credentials in mobile app
├─ Embed API keys in code
└─ Credentials leaked!

Right:
├─ Use Cognito Identity Pool
├─ Request temporary AWS credentials
├─ Credentials auto-rotate every hour
└─ No secrets in code!
```

### ✗ Mistake 2: Disabled MFA

```
Wrong:
├─ Users opt-in for MFA
├─ Few users enable it
├─ Accounts easily hacked

Right:
├─ Make MFA required
├─ Users must set up during signup
└─ Strong security default
```

### ✗ Mistake 3: Not Validating Tokens

```
Wrong:
├─ Trust tokens without verification
├─ Attacker creates fake token
├─ Access granted incorrectly

Right:
├─ Validate token signature
├─ Check token expiration
├─ Verify claims
└─ Use AWS SDK (handles automatically)
```

### ✗ Mistake 4: Storing Passwords Yourself

```
Wrong:
├─ Build own user authentication
├─ Store password hashes
├─ Security breach likely
└─ GDPR/HIPAA liability!

Right:
├─ Use Cognito User Pools
├─ Let AWS handle security
└─ Compliance included
```

## Best Practices

✅ Enable MFA for all users
✅ Use identity pools for AWS access
✅ Enforce strong password policies
✅ Enable compromised credentials detection
✅ Use social login options
✅ Implement account lockout
✅ Log authentication events
✅ Monitor for suspicious activity
✅ Use IAM roles with identity pools
✅ Test passwordless options

## Integration Examples

```python
# Sign in user
import boto3

cognito = boto3.client('cognito-idp')

response = cognito.admin_initiate_auth(
    UserPoolId='us-east-1_abc123',
    ClientId='xyz789',
    AuthFlow='ADMIN_NO_SRP_AUTH',
    AuthParameters={
        'USERNAME': 'user@example.com',
        'PASSWORD': 'Password123!'
    }
)

id_token = response['AuthenticationResult']['IdToken']
```

## CLI Examples

```bash
# Create user pool
aws cognito-idp create-user-pool \
  --pool-name MyAppUsers \
  --policies PasswordPolicy={MinimumLength=8,RequireUppercase=true}

# Create user
aws cognito-idp admin-create-user \
  --user-pool-id us-east-1_abc123 \
  --username user@example.com \
  --message-action SUPPRESS

# Set password
aws cognito-idp admin-set-user-password \
  --user-pool-id us-east-1_abc123 \
  --username user@example.com \
  --password Password123! \
  --permanent
```

## Next Steps

→ [User Pools Deep Dive](./user-pools.md) - Advanced configuration
→ [Identity Pools](./identity-pools.md) - AWS resource access
→ [Custom Auth Flows](./custom-auth.md) - Advanced scenarios