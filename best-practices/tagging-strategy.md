# AWS Tagging Strategy 🏷️

How to organize and track your AWS resources with tags.

## Why Tags Matter

**Problem without tags:**
```
You have 50 EC2 instances
- Which are for production?
- Which are development?
- Which project do they belong to?
- Who created them?
- How much does each project cost?

Answer: No idea!
```

**Solution with tags:**
```
Tag every resource:
- Environment: production, development, testing
- Project: web-app, mobile-app, analytics
- Owner: john@company.com
- CostCenter: marketing, engineering

Now you can:
✓ Find resources quickly
✓ Track costs by project
✓ Identify who created what
✓ Automate based on tags
```

## Standard Tagging Schema

### Essential Tags (Always Use)

```
Environment: production | development | testing | staging
- Indicates which environment

Project: web-app | mobile-backend | analytics-pipeline
- Which project/application

Owner: john@company.com | team-backend
- Who is responsible

CostCenter: engineering | marketing | ops
- Who pays for it

CreatedBy: automation | manual | terraform
- How it was created

CreatedDate: 2024-01-15
- When it was created
```

### Optional Tags (Recommended)

```
Name: web-server-01 | db-production-primary
- Human-readable name

BackupRequired: true | false
- Should be backed up?

Compliance: pci-dss | hipaa | gdpr
- Compliance requirements

DataClassification: public | internal | confidential
- Data sensitivity

Patch-Group: critical | standard | deferred
- Patching schedule

DeleteAfter: 2024-12-31
- Auto-delete date (for test resources)

Terraform: true | false
- Managed by Infrastructure as Code?
```

## How to Apply Tags

### Manual (Console)

```
EC2 → Instances → [Instance] → Tags → Add/Edit Tags
Key: Environment
Value: production

Save
```

### AWS CLI

```bash
# Tag EC2 instance
aws ec2 create-tags \
  --resources i-1234567890abcdef0 \
  --tags Key=Environment,Value=production \
         Key=Project,Value=web-app \
         Key=Owner,Value=john@company.com

# Tag S3 bucket
aws s3api put-bucket-tagging \
  --bucket my-bucket \
  --tagging 'TagSet=[{Key=Environment,Value=production},{Key=Project,Value=web-app}]'

# Tag RDS instance
aws rds add-tags-to-resource \
  --resource-name arn:aws:rds:us-east-1:123456789:db:mydb \
  --tags Key=Environment,Value=production Key=Project,Value=web-app
```

### Terraform

```hcl
resource "aws_instance" "web_server" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  tags = {
    Name        = "web-server-01"
    Environment = "production"
    Project     = "web-app"
    Owner       = "john@company.com"
    CostCenter  = "engineering"
    CreatedBy   = "terraform"
  }
}
```

## Cost Tracking with Tags

### Enable Cost Allocation Tags

```
Billing → Cost Allocation Tags
Activate tags:
✓ Environment
✓ Project
✓ Owner
✓ CostCenter

(Takes 24 hours to apply)
```

### View Costs by Tag

```
Cost Management → Cost Explorer

Filter by:
- Tag: Project
- Value: web-app

Result:
Shows all costs for "web-app" project
- EC2: $150/month
- RDS: $50/month
- S3: $10/month
- Total: $210/month
```

### Example Cost Report

```
By Project:
- web-app: $500/month
- mobile-backend: $300/month
- analytics-pipeline: $1200/month

By Environment:
- production: $1500/month
- development: $300/month
- testing: $200/month

By Owner:
- john@company.com: $600/month
- team-backend: $900/month
- team-frontend: $500/month
```

## Automation with Tags

### Example 1: Auto-Stop Development Instances

```python
import boto3

ec2 = boto3.client('ec2')

# Find all development instances
instances = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Environment', 'Values': ['development']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)

# Stop them at night (save 50% on costs)
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        ec2.stop_instances(InstanceIds=[instance['InstanceId']])
        print(f"Stopped {instance['InstanceId']}")
```

### Example 2: Auto-Backup Tagged Resources

```python
# Find all resources tagged with BackupRequired=true
resources = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:BackupRequired', 'Values': ['true']}
    ]
)

# Create backup/snapshot
for instance in resources:
    create_snapshot(instance['InstanceId'])
```

### Example 3: Compliance Reporting

```bash
# Find all resources with sensitive data
aws resourcegroupstaggingapi get-resources \
  --tag-filters Key=DataClassification,Values=confidential \
  --resource-type-filters ec2 rds s3

# Verify encryption enabled
for resource in $(aws ...); do
  check_encryption_enabled $resource
done
```

## Tag Enforcement Policies

### Require Tags on Resource Creation

**AWS Config Rule:**
```
Config → Rules → Add Rule
Rule: required-tags
Parameters:
  tag1Key: Environment
  tag2Key: Project
  tag3Key: Owner

Action: Flag non-compliant resources
```

### IAM Policy to Require Tags

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:RunInstances",
        "ec2:CreateVolume"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestTag/Environment": [
            "production",
            "development",
            "testing"
          ]
        }
      }
    }
  ]
}
```

This prevents launching EC2 without Environment tag!

## Tag Best Practices

### 1. Be Consistent

**Bad:**
```
Environment: prod, production, PROD, prd
Project: webapp, web-app, WebApp, web_app
```

**Good:**
```
Environment: production | development | testing
Project: web-app | mobile-backend | analytics
(Standardized values)
```

### 2. Document Your Schema

```markdown
# Company Tagging Standard

## Required Tags (All Resources)
- Environment: production | development | testing
- Project: [project-name]
- Owner: [email]
- CostCenter: [department]

## Tag Naming Convention
- Use lowercase
- Use hyphens for spaces
- Max 255 characters
```

### 3. Review Tags Regularly

```
Monthly:
- Find untagged resources
- Tag them or delete them
- Update owner if changed

Quarterly:
- Review tag schema
- Update documentation
- Train team on changes
```

### 4. Automate Tagging

```python
# Lambda function to auto-tag new resources
def lambda_handler(event, context):
    # Get resource from CloudWatch Events
    resource_id = event['detail']['resource-id']
    
    # Auto-apply default tags
    default_tags = {
        'CreatedBy': 'automation',
        'CreatedDate': datetime.now().isoformat(),
        'ManagedBy': 'aws-auto-tagger'
    }
    
    apply_tags(resource_id, default_tags)
```

## Finding Untagged Resources

### AWS CLI

```bash
# Find untagged EC2 instances
aws ec2 describe-instances \
  --query 'Reservations[].Instances[?Tags==`null` || !contains(Tags[].Key, `Environment`)].[InstanceId]' \
  --output text

# Find untagged S3 buckets
aws s3api list-buckets --query 'Buckets[].Name' | while read bucket; do
  tags=$(aws s3api get-bucket-tagging --bucket $bucket 2>/dev/null)
  if [ -z "$tags" ]; then
    echo "Untagged: $bucket"
  fi
done
```

### Tag Compliance Report

```python
import boto3

def get_untagged_resources():
    required_tags = ['Environment', 'Project', 'Owner']
    
    # Check EC2
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    
    untagged = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            
            missing = [t for t in required_tags if t not in tags]
            if missing:
                untagged.append({
                    'ResourceId': instance['InstanceId'],
                    'Type': 'EC2',
                    'MissingTags': missing
                })
    
    return untagged

# Generate report
print("Untagged Resources Report")
for resource in get_untagged_resources():
    print(f"{resource['Type']} {resource['ResourceId']}: Missing {resource['MissingTags']}")
```

## Tagging Checklist

🔴 **CRITICAL**
- ✅ Required tags defined (Environment, Project, Owner, CostCenter)
- ✅ Cost allocation tags enabled
- ✅ Tag enforcement policy in place

🟠 **HIGH**
- ✅ All production resources tagged
- ✅ Tagging documented
- ✅ Monthly tag review scheduled

🟡 **IMPORTANT**
- ✅ Automation for tagging new resources
- ✅ Compliance reporting set up
- ✅ Team trained on tagging standards

## 📖 Related Resources

- [AWS Tagging Best Practices](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
- [Cost Optimization](cost-optimization.md)
- [Billing Alerts](billing-alerts.md)
- [AWS Config](https://aws.amazon.com/config/)