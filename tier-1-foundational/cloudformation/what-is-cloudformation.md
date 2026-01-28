# What is CloudFormation? 📋

Infrastructure as Code (IaC) - Define AWS resources in JSON/YAML templates.

## Core Concept

**CloudFormation** lets you describe your entire AWS infrastructure in a template, then automatically creates all resources.

```
Traditional Way:
├─ Create EC2 (AWS Console)
├─ Create RDS (AWS Console)
├─ Create S3 (AWS Console)
├─ Create IAM roles (AWS Console)
├─ Manual configuration
└─ Time: 30+ minutes, error-prone

CloudFormation Way:
├─ Write template (YAML/JSON)
├─ Run: aws cloudformation create-stack
└─ Everything deployed automatically!
   Time: 5 minutes, reproducible
```

## Real-World Analogy

```
Traditional Construction:
├─ Call electrician
├─ Call plumber
├─ Call carpenter
└─ Coordinate, hope nothing breaks

CloudFormation (Blueprint):
├─ Have master blueprint
├─ Contractor builds from blueprint
├─ Everything is coordinated
└─ Can rebuild identical house anytime
```

## Template Structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'My first CloudFormation template'

Parameters:
  EnvironmentName:
    Type: String
    Default: Production

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-app-bucket-prod
  
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0c55b159cbfafe1f0
      InstanceType: t3.micro

Outputs:
  BucketName:
    Value: !Ref MyBucket
    Export:
      Name: MyAppBucket
```

## What CloudFormation Can Create

```
Compute:
├─ EC2 instances
├─ Lambda functions
├─ Auto Scaling groups
└─ Elastic Beanstalk environments

Storage:
├─ S3 buckets
├─ EBS volumes
└─ Backup vaults

Database:
├─ RDS databases
├─ DynamoDB tables
├─ ElastiCache
└─ Redshift clusters

Networking:
├─ VPC
├─ Subnets
├─ Security Groups
├─ Route 53 DNS
└─ Load Balancers

Everything AWS offers (~200+ resource types)
```

## Template Example: Web Application

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'Simple web application stack'

Resources:
  # Security Group
  WebServerSG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP/HTTPS
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0

  # EC2 Instance
  WebServer:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0c55b159cbfafe1f0
      InstanceType: t3.micro
      SecurityGroups:
        - !Ref WebServerSG
      UserData: |
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd

  # S3 Bucket for Assets
  AssetsBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: web-app-assets

  # RDS Database
  Database:
    Type: AWS::RDS::DBInstance
    Properties:
      DBInstanceIdentifier: app-db
      Engine: mysql
      DBInstanceClass: db.t3.micro
      MasterUsername: admin
      MasterUserPassword: ChangeMe123!
      AllocatedStorage: 20

Outputs:
  WebServerIP:
    Value: !GetAtt WebServer.PublicIp
    Export:
      Name: WebServerPublicIP

  DatabaseEndpoint:
    Value: !GetAtt Database.Endpoint.Address
    Export:
      Name: DatabaseEndpoint

  BucketName:
    Value: !Ref AssetsBucket
    Export:
      Name: AssetsBucketName
```

## How CloudFormation Works

```
Step 1: Create Template (YAML/JSON)
Step 2: Validate Template
Step 3: Create Stack
│  ├─ Parse resources
│  ├─ Validate dependencies
│  └─ Create in order
Step 4: Monitor Deployment
│  ├─ Watch events
│  ├─ See progress
│  └─ Alert on errors
Step 5: Stack Complete
└─ All resources ready!
```

## Key Concepts

### Stack

```
Stack = Collection of resources created from template

Example Stack: "web-app-prod"
├─ EC2 instance
├─ Security group
├─ S3 bucket
├─ RDS database
└─ All linked together

Update Stack:
└─ Modify template → Update stack
   CloudFormation figures out changes
```

### Parameters

```yaml
Parameters:
  InstanceType:
    Type: String
    Default: t3.micro
    AllowedValues:
      - t3.micro
      - t3.small
      - t3.medium

  EnvironmentName:
    Type: String
    Default: development
```

Usage:
```bash
aws cloudformation create-stack \
  --stack-name my-stack \
  --template-body file://template.yaml \
  --parameters \
    ParameterKey=InstanceType,ParameterValue=t3.small \
    ParameterKey=EnvironmentName,ParameterValue=production
```

### Outputs

```yaml
Outputs:
  WebsiteURL:
    Value: !Sub 'http://${WebServer.PublicDnsName}'
    Export:
      Name: WebsiteURL

  DatabaseConnection:
    Value: !GetAtt Database.Endpoint.Address
    Export:
      Name: DatabaseEndpoint
```

Returns:
```
Outputs:
  WebsiteURL: http://ec2-54-123-45-67.compute-1.amazonaws.com
  DatabaseConnection: mydb.c9akciq32.us-east-1.rds.amazonaws.com
```

## Cost Comparison

```
Manual Deployment (Time-based):
├─ Setup: 2 hours @ $50/hour = $100
├─ Testing: 1 hour = $50
├─ Redeploy: 1 hour = $50
└─ Total: $200 (labor only)

CloudFormation (One-time):
├─ Template creation: 1 hour = $50
├─ Deployment: 5 minutes = $4
├─ Redeploy: Automatic = $0
└─ Total: $54

Savings: $146 per deployment
With 10 deployments: $1,460 savings!
```

## Benefits

### 1. Infrastructure as Code

```
Version Control:
├─ Store template in Git
├─ Track all changes
├─ Review infrastructure changes
└─ Rollback if needed

Code Review:
├─ Team reviews template
├─ Approve before deployment
└─ Prevents mistakes
```

### 2. Consistency & Repeatability

```
Deploy identical infrastructure:
├─ Dev environment
├─ Staging environment
├─ Production environment

All identical, built from same template
No manual setup differences
```

### 3. Automation

```
Scenario: Need 5 new environments

Without CloudFormation:
├─ Manual setup for each (5 hours each)
└─ Total: 25 hours

With CloudFormation:
├─ Create 5 stacks (2 minutes each)
└─ Total: 10 minutes!
```

### 4. Disaster Recovery

```
Original Stack Corrupted:
├─ Delete stack (clean up)
├─ Re-create from template
└─ Identical infrastructure in 5 minutes

vs. Manual rebuild (hours or days)
```

## Change Sets

```
Scenario: Update production stack safely

Without Change Sets:
└─ Update stack → Resources changed immediately
   Risk: Unintended changes, downtime

With Change Sets:
├─ Create change set → See what will change
├─ Review changes → Verify safe
└─ Execute → Apply changes
   Safe, controlled updates
```

## Drift Detection

```
Stack Created:
├─ EC2 instance: t3.micro
├─ Security group: 80, 443 open
└─ S3 bucket: Encrypted

Manual Change (someone changes console):
├─ EC2 resized to t3.large
├─ Security group: Only 80 open
└─ S3 bucket: Encryption removed

Drift Detection:
└─ Finds differences between template and reality
   Alerts: "Your stack drifted!"
```

## Common Use Cases

### Use Case 1: Environment Parity

```
Need: Dev, Staging, Prod with same setup

Solution:
├─ Create single template
├─ Deploy with different parameters:
│  ├─ DevEnv: t3.micro, 1 replica
│  ├─ StagingEnv: t3.small, 2 replicas
│  └─ ProdEnv: t3.medium, 3 replicas
└─ All from same template!
```

### Use Case 2: Multi-Region Deployment

```
Deploy same infrastructure globally:
├─ US-East template stack
├─ EU-West template stack
├─ Asia-Pacific template stack

Create template once, deploy to 3 regions
Automatic failover ready
```

### Use Case 3: Rapid Scaling

```
Traffic surge → Need more resources

Manually:
├─ Add EC2 instances (manual)
├─ Add RDS read replicas (manual)
├─ Update load balancer (manual)
└─ Time: 1 hour

CloudFormation:
├─ Update template (increase count: 5)
├─ Update stack
└─ 10 new instances deployed: 10 minutes
```

## Best Practices

✅ Version control all templates
✅ Use parameters for reusability
✅ Create modular templates
✅ Use change sets before updating
✅ Enable termination protection
✅ Enable stack policy
✅ Document outputs
✅ Use meaningful names
✅ Test in dev first
✅ Monitor stack events

## Limitations

```
What CloudFormation CAN'T do:
├─ Some manual configuration steps
├─ Custom resources require Lambda
├─ Limited to AWS services
└─ Complex multi-account setup needs StackSets
```

## CLI Commands

```bash
# Create stack
aws cloudformation create-stack \
  --stack-name my-stack \
  --template-body file://template.yaml

# List stacks
aws cloudformation list-stacks

# Describe stack
aws cloudformation describe-stacks \
  --stack-name my-stack

# Update stack
aws cloudformation update-stack \
  --stack-name my-stack \
  --template-body file://template.yaml

# Delete stack
aws cloudformation delete-stack \
  --stack-name my-stack
```

## Getting Started

1. **Write Template** (YAML or JSON)
2. **Validate** (aws cloudformation validate-template)
3. **Create Stack** (AWS Console or CLI)
4. **Monitor** (Watch CloudFormation Events)
5. **Update** (Change template, update stack)

## Next Steps

→ [VPC Fundamentals](../vpc/what-is-vpc.md) - Create VPC with CloudFormation
→ [EC2 Basics](../ec2/what-is-ec2.md) - Launch EC2 with CloudFormation
→ [CloudFormation Best Practices](../../best-practices/) - Advanced patterns