# Setting Up Billing Alerts 🚨

Step-by-step guide to prevent surprise AWS bills.

## Why Billing Alerts?

**Horror stories:**
```
❌ Accidentally left 100 EC2 instances running
   Result: $500 bill in one day

❌ Lambda infinite loop
   Result: $2,000 bill in hours

❌ Forgot about old snapshots
   Result: $50/month wasted for months
```

**Solution:** Set up alerts!

## Method 1: Free Tier Alerts (Easiest)

### Step 1: Enable Alerts
```
1. Sign in to AWS Console
2. Click account name (top right)
3. Click "Billing and Cost Management"
4. Click "Billing Preferences" (left sidebar)
```

### Step 2: Configure
```
Check all boxes:

☑ Receive PDF Invoice By Email
☑ Receive Free Tier Usage Alerts
   Email: your-email@example.com

☑ Receive Billing Alerts

☑ Receive Cost Optimization Recommendations

Click "Save preferences"

✅ Done! (Takes 5 minutes)
```

### What You'll Get
```
Free Tier Alerts:
- When you reach 85% of free tier limit
- Example: "You've used 637 of 750 EC2 hours"

Billing Alerts:
- Enables CloudWatch billing metrics
- Set custom thresholds (next step)
```

## Method 2: CloudWatch Billing Alarm

### Step 1: Switch Region
```
🚨 IMPORTANT: Must use us-east-1!

1. Region selector (top right)
2. Select "US East (N. Virginia)"

Billing metrics only available in us-east-1
```

### Step 2: Go to CloudWatch
```
1. Search "CloudWatch" in console
2. Or Services → CloudWatch
```

### Step 3: Create Alarm
```
1. Click "Alarms" (left sidebar)
2. Click "Create alarm"
3. Click "Select metric"
```

### Step 4: Select Billing Metric
```
1. Click "Billing"
2. Click "Total Estimated Charge"
3. Check box next to "USD"
4. Click "Select metric"
```

### Step 5: Set Threshold
```
Metric:
- Statistic: Maximum
- Period: 6 hours

Conditions:
- Threshold type: Static
- Whenever EstimatedCharges is: Greater
- than: 10 (or your budget)

Example thresholds:
- Learning: $1
- Testing: $10
- Production: $100

Click "Next"
```

### Step 6: Configure Notification
```
Notification:
- Alarm state trigger: In alarm

Send notification to:
● Create new topic

Topic name: BillingAlerts

Email endpoints:
- your-email@example.com
- (Add more emails if needed)

Click "Create topic"

📧 Check your email!
Confirm subscription

Click "Next"
```

### Step 7: Name and Create
```
Alarm name: BillingAlert-$10

Description: Alert when bill exceeds $10

Click "Next"

Click "Create alarm"

✅ Alarm created!
```

## Method 3: AWS Budgets (Most Powerful)

### Step 1: Go to Budgets
```
1. Billing → Budgets
2. Click "Create budget"
```

### Step 2: Choose Budget Type
```
Select: Cost budget

Click "Next"
```

### Step 3: Set Budget Amount
```
Budget name: MonthlyBudget

Period: Monthly

Budget effective dates:
● Recurring budget

Start month: [Current month]

Budget amount:
● Fixed: $50 (or your monthly budget)

Budget scope:
● All AWS services

Click "Next"
```

### Step 4: Configure Alerts
```
Add alert threshold:

Threshold 1:
- Alert based on: Actual costs
- Threshold: 50% of budgeted amount ($25)
- Email: your-email@example.com

Click "Add alert threshold"

Threshold 2:
- Alert based on: Actual costs
- Threshold: 80% of budgeted amount ($40)
- Email: your-email@example.com

Threshold 3:
- Alert based on: Actual costs
- Threshold: 100% of budgeted amount ($50)
- Email: your-email@example.com

Click "Next"
```

### Step 5: Review and Create
```
Review settings:
- Budget: $50/month
- Alerts: 50%, 80%, 100%
- Email: your-email@example.com

Click "Create budget"

✅ Budget created!

You'll receive:
- Email at $25 (50%)
- Email at $40 (80%)
- Email at $50 (100%)
```

## Method 4: Cost Anomaly Detection

### Enable ML-Powered Alerts
```
1. Cost Management → Cost Anomaly Detection
2. Click "Get started"
3. Click "Enable now"
```

### Configure Detection
```
Anomaly detection settings:

Monitor type: AWS services

Threshold: $100 (minimum anomaly amount)

Frequency: Individual alerts (immediate)

Email: your-email@example.com

Click "Save"

✅ ML monitors spending patterns!
```

### What It Does
```
Learns your normal spending:
- Week 1: $50
- Week 2: $48
- Week 3: $52
- Week 4: $500 ← ALERT!

"Unusual spending detected in EC2"
```

## Setting Multiple Alerts

### Recommended Setup
```
🟢 Warning ($10):
- CloudWatch alarm
- Early warning
- "You're spending money"

🟡 Caution ($25):
- Budget alert (50%)
- "Getting close to budget"

🟠 Alert ($40):
- Budget alert (80%)
- "Almost at budget!"

🔴 Critical ($50):
- Budget alert (100%)
- "Budget exceeded!"

🔮 Anomaly:
- ML-powered
- "Unusual spike detected"
```

## Testing Your Alerts

### Verify Email
```
1. Check inbox
2. Look for AWS emails:
   - "AWS Budgets Notification"
   - "SNS Subscription Confirmation"
3. Click confirmation links
4. ✅ Alerts active
```

### Test CloudWatch Alarm
```
Wait for charges:
- Launch t3.micro instance
- Run for few hours
- Charges appear
- If over threshold → email!

Or set very low threshold ($0.01) to test
```

## What to Do When Alert Fires

### Step 1: Don't Panic
```
You got alert!
Email says: "Bill is $15"

This is good - alerts working!
```

### Step 2: Check Billing Dashboard
```
1. Billing Dashboard
2. See current charges
3. Identify culprit:
   - EC2: $12
   - S3: $2
   - Data transfer: $1
```

### Step 3: Investigate
```
If unexpected:

1. Cost Explorer
2. Filter by service
3. See what's expensive
4. Check:
   - Running instances?
   - Large data transfer?
   - Forgot to delete something?
```

### Step 4: Take Action
```
Stop unnecessary resources:
- Stop EC2 instances
- Delete unused volumes
- Delete old snapshots
- Remove unused Elastic IPs

Costs drop immediately!
```

## Alert Best Practices

### 1. Multiple Thresholds
```
✅ Set 3-4 alerts
❌ Don't set just one

Early warnings help!
```

### 2. Right Thresholds
```
✅ Start low ($1-10)
✅ Adjust as you learn
❌ Don't set too high initially
```

### 3. Check Weekly
```
✅ Review billing dashboard
✅ Even without alerts
❌ Don't wait for alerts only
```

### 4. Act Immediately
```
✅ Investigate same day
✅ Stop unnecessary resources
❌ Don't ignore alerts
```

## Common Alert Issues

### Not Receiving Emails?
```
Check:
1. Spam folder
2. Email confirmed? (click confirmation link)
3. Correct email address?
4. Alarm state: "In alarm" or "OK"?
```

### Alarm Not Triggering?
```
Check:
1. Region: us-east-1?
2. Threshold correct?
3. Billing preferences enabled?
4. Wait 24 hours for first data
```

### Too Many Alerts?
```
Solution:
1. Increase thresholds
2. Delete unnecessary alarms
3. Consolidate into budgets
```

## Alert Checklist

🔴 **Must Have:**
- ✅ Free tier alerts enabled
- ✅ CloudWatch billing alarm ($10)
- ✅ Budget with 3 thresholds
- ✅ Email confirmed

🟠 **Recommended:**
- ✅ Cost anomaly detection
- ✅ Multiple email recipients
- ✅ SMS for critical alerts

🟡 **Nice to Have:**
- ✅ Slack/Teams integration
- ✅ PagerDuty integration
- ✅ Lambda auto-remediation

## Sample Alert Email

```
Subject: AWS Billing Alert

You have a billing alert!

Your charges for February 2026:

Current: $42.30
Forecast: $55.00
Budget: $50.00

You're at 85% of your budget.

Top services:
1. EC2: $25.00
2. RDS: $12.00
3. S3: $3.30
4. Other: $2.00

View details: [Link to Billing Dashboard]
```

## 📖 Next Steps

1. [Cost Management Basics](cost-management-basics.md)
2. [Cost Optimization](../best-practices/cost-optimization.md)
3. [Hidden Costs](../best-practices/hidden-costs.md)

## Related Resources

- [AWS Free Tier](aws-free-tier.md)
- [Billing Best Practices](../best-practices/billing-alerts.md)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)