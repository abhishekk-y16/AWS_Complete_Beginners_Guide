# Auto Scaling setup

TL;DR
- Use Auto Scaling Groups (ASG) to adjust EC2 capacity automatically.
- Define a launch template, scaling policy, and health checks.
- Combine with Elastic Load Balancer for zero-downtime scaling.
- Start small, test scaling triggers with CloudWatch alarms.
- Use lifecycle hooks only when you need custom instance init/cleanup.
- Monitor costs and scale-in protections to avoid churn.

Prerequisites
- AWS CLI configured with an IAM user that can manage EC2/ASG/CloudWatch.
- A VPC and subnet(s) already created.
- A working EC2 AMI or launch template.

Steps
1. Create a launch template (example):
```
aws ec2 create-launch-template --launch-template-name my-template --version-description v1 --launch-template-data '{"ImageId":"ami-0123456789","InstanceType":"t3.micro"}'
```
2. Create ASG with min/max/desired capacity and subnets:
```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name my-asg --launch-template LaunchTemplateName=my-template,Version=1 --min-size 1 --max-size 4 --desired-capacity 1 --vpc-zone-identifier "subnet-abc,subnet-def"
```
3. Attach a target group/ALB for health checks (optional):
```
aws autoscaling attach-load-balancer-target-groups --auto-scaling-group-name my-asg --target-group-arns arn:aws:elasticloadbalancing:...
```
4. Create CloudWatch alarm and a scaling policy (simple step scaling):
```
aws cloudwatch put-metric-alarm --alarm-name HighCPU --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 70 --comparison-operator GreaterThanThreshold --dimensions Name=AutoScalingGroupName,Value=my-asg --evaluation-periods 2 --alarm-actions <policy-arn>
```
5. Test by increasing load or lowering threshold; observe instance launches.
6. Tweak cool-downs, instance types, and lifecycle hooks as needed.

Cost notes
- You pay for launched EC2 instances, ALB hours, and data transfer. Test with small instance types.

Quick troubleshooting
- Instances stuck: check launch template AMI/permissions and subnet reachability.
- Scaling not triggered: verify CloudWatch alarm dimensions and IAM permissions.
- Health-check failures: verify security groups and application listeners.

Checklist
- Confirm launch template and AMI.
- Verify CloudWatch alarms trigger scaling policies.
- Validate health checks through ALB or EC2 status checks.
# Tutorials

AWS Tutorials service