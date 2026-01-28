# AWS Systems Manager 🔧

Operations hub for managing, monitoring, and automating AWS resources and on-premises infrastructure.

## Overview

Systems Manager provides unified interface to manage EC2 instances, RDS databases, and on-premises servers. Run commands, automate patching, manage parameters, and monitor infrastructure. Reduces operational overhead and improves compliance.

## Key Features

- ✅ Run Command for remote execution
- ✅ Automation documents for workflows
- ✅ Session Manager for secure shell access
- ✅ Patch Manager for automated patching
- ✅ Parameter Store for configuration management
- ✅ Maintenance Windows for scheduled operations

## Core Capabilities

**Run Command**:
- Execute commands on instances (Linux/Windows)
- No SSH keys or bastion hosts needed
- Output visible in console

**Session Manager**:
- Web-based shell access
- Secure, audited sessions
- No inbound security group rules
- IAM-based access control

**Automation**:
- Workflow automation documents
- Remediation runbooks
- Event-based triggers

**Patch Manager**:
- Automated OS patching
- Compliance reporting
- Patch baselines per OS

**Parameter Store**:
- Store configuration values
- Encrypt sensitive data
- Secrets rotation

## Managed Nodes

Requires:
- **EC2**: Systems Manager Agent (pre-installed on many AMIs)
- **On-Premises**: Hybrid Activation (EC2 key pair needed)
- **RDS**: Native Systems Manager integration

## IAM Permissions

Required role policy:
```json
{
  "Effect": "Allow",
  "Action": [
    "ssm:SendCommand",
    "ssm:GetCommandInvocation",
    "ec2:DescribeInstances"
  ],
  "Resource": "*"
}
```

## Use Cases

- **Automated Patching**: Apply OS updates across fleet
- **Configuration Management**: Manage system settings
- **Inventory Management**: Track software and hardware
- **Compliance Monitoring**: Audit security settings
- **Troubleshooting**: Remote access without SSH
- **Bulk Operations**: Commands on 100s of instances

## Pricing

- **Run Command**: $0.00125 per command invocation
- **Automation**: $0.00025 per automation invocation
- **Session Manager**: Free
- **Parameter Store**: Free (standard), $0.04/month (advanced)

Example: 1000 monthly commands = $1.25/month

## Advantages

✅ No SSH key management
✅ Full audit trail via CloudTrail
✅ Works across AWS and on-premises
✅ IAM-based access control
✅ No security group modifications
✅ Parameter encryption options

## Automation Documents

Predefined runbooks for:
- AWS Systems Manager Automation
- EC2 instance management
- RDS operations
- ECS updates
- Lambda function management

## Maintenance Windows

Schedule operations during low-traffic periods:
- Patching
- Script execution
- Database updates
- Instance refreshes

## Next Steps

→ [Systems Manager Documentation](https://docs.aws.amazon.com/systems-manager/)
→ [Session Manager Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
→ [Automation Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation.html)
→ [Systems Manager Console](https://console.aws.amazon.com/systems-manager/)