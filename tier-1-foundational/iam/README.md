# AWS IAM (Identity and Access Management) 🔐

## 🎯 What is IAM?

IAM is the security system for AWS. It controls **who** can access **what** in your AWS account and **what** they're allowed to do. Think of it like a hotel key card system where the root account is the master key and IAM users are guest cards.

## ⚠️ Most Important Rule

**NEVER use your AWS root account for daily work!** Always create IAM users/roles. Root account should only be used for account recovery.

## 🔑 Key Concepts

- **Users**: Individual login accounts for people with specific permissions
- **Roles**: Like job titles - services can assume roles (e.g., EC2 reading from S3)
- **Policies**: JSON rules defining what you can/cannot do
- **Groups**: Collections of users with same permissions
- **Access Keys**: Like passwords for programmatic/API access (rotate every 90 days)
- **MFA**: Extra security layer - password + code from phone

## 🚀 Quick Start

1. ✅ Enable MFA on root account
2. ✅ Create your first IAM user
3. ✅ Attach AdministratorAccess policy for testing
4. ✅ Sign in with IAM user (not root!)
5. ✅ Review [Security Best Practices](../../best-practices/security-checklist.md)

## 💡 Common Setup

**For a development team:**
- Create "developers" group with EC2/S3/RDS permissions
- Add all developers to this group
- Create admin user for DevOps with full access
- Each service gets an IAM role (not a user!)

## ⭐ Best Practices

- ✓ Never share credentials
- ✓ Use strong passwords (16+ characters)
- ✓ Enable MFA for console access
- ✓ Rotate access keys every 90 days
- ✓ Use groups to manage permissions
- ✓ Apply least-privilege (minimum needed permissions)
- ✓ Review users/roles monthly

## 📖 Official Resources

- [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Core IAM Basics](../../core-concepts/iam-basics.md)