# Kubernetes on AWS (EKS)

TL;DR
- Use EKS to run Kubernetes clusters; use managed nodegroups or Fargate for worker nodes.

Prerequisites
- `kubectl`, `eksctl`, and IAM permissions for EKS and EC2.

Steps
1. Create an EKS cluster with `eksctl`:
```
eksctl create cluster --name my-cluster --region us-east-1 --nodes 3
```
2. Configure IAM Roles for Service Accounts (IRSA) to grant pods specific AWS permissions.
3. Use managed nodegroups or Fargate profiles to run workloads.
4. Configure autoscaling with Cluster Autoscaler and HorizontalPodAutoscaler.

Cost notes
- Costs from EC2 nodes, load balancers, EBS volumes, and data transfer; use spot instances for cost savings.

Troubleshooting
- Node joining issues: check VPC subnet size, security groups, and IAM permissions.

Checklist
- Cluster created, nodes healthy, IRSA configured.
