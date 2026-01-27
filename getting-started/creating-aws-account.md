# Creating Your AWS Account 🆕

Step-by-step guide to create your free AWS account in 10 minutes.

## What You'll Need

☑ Email address
☑ Credit/debit card (free tier won't charge you)
☑ Phone number
☑ 10 minutes

## Step 1: Go to AWS

```
1. Visit: aws.amazon.com
2. Click "Create an AWS Account"
```

## Step 2: Email & Password

```
Root user email: your-email@example.com
AWS account name: YourCompany

Password requirements:
✅ 8+ characters
✅ Uppercase + lowercase
✅ Number + special character

Example: MyAWS2024!Pass
```

## Step 3: Contact Info

```
Account Type:
● Personal (learning)
○ Professional (business)

Full Name: John Smith
Phone: +1-555-0123
Country: United States
Address: 123 Main St
City: Seattle
State: Washington
Zip: 98101

☑ Agree to AWS Customer Agreement
```

## Step 4: Payment Info

```
💳 Credit Card

🚨 IMPORTANT:
- Card for verification only
- Won't charge for free tier
- May see $1 temporary charge (refunded)
- Set billing alerts after!
```

## Step 5: Phone Verification

```
📞 Verify Identity

Method:
● SMS text message
○ Voice call

Enter code: 1234
```

## Step 6: Support Plan

```
● Basic Support - FREE ← Choose this!
  - Documentation
  - Forums
  - $0/month

○ Developer - $29/month
○ Business - $100/month
```

## Step 7: Wait for Activation

```
"Account being activated..."
Usually < 5 minutes

Check email:
"Welcome to AWS"

✅ Account ready!
```

## CRITICAL: Immediate Security Setup

### Enable MFA (Do Now!)

```
1. Sign in to console
2. Click account name (top right)
3. Security Credentials
4. Multi-factor authentication
5. Assign MFA device
6. Use Google Authenticator app
7. Scan QR code
8. Enter two codes
9. ✅ MFA enabled!
```

### Create Admin User (Don't Use Root!)

```
1. Search "IAM"
2. Users → Create user
3. Name: admin
4. Console access: Yes
5. Permissions: AdministratorAccess
6. Create user
7. Download credentials!

✅ Use admin user daily, not root
```

### Set Billing Alerts

```
1. Billing Dashboard
2. Billing Preferences
3. ☑ Receive Free Tier Alerts
4. ☑ Receive Billing Alerts
5. Save

6. CloudWatch (us-east-1 only!)
7. Create Alarm
8. Billing → Total Estimated Charge
9. Threshold: $10
10. Email: your-email@example.com
11. ✅ Alert created!
```

## Security Checklist

🔴 **Do Immediately:**
- ✅ MFA on root account
- ✅ Create IAM admin user
- ✅ Billing alerts enabled
- ✅ Sign out of root

## Common Issues

**Card Declined?**
- Try different card
- Contact bank
- Use debit instead

**SMS Not Received?**
- Try voice call
- Wait 2 minutes
- Check phone number format

**Still Activating?**
- Wait 24 hours
- Check spam folder
- Contact AWS Support

## 📖 Next Steps

1. [AWS Console Overview](aws-console-overview.md)
2. [AWS Free Tier](aws-free-tier.md)
3. [Launch First Server](../tutorials/deploy-web-server.md)