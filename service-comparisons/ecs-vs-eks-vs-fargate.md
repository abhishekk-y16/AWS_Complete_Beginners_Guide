# ECS vs EKS vs Fargate

When to use
- **ECS**: simplest AWS-native orchestrator.
- **EKS**: full Kubernetes control/portability.
- **Fargate**: serverless compute for ECS/EKS tasks/pods.

Quick compare
| Feature | ECS | EKS | Fargate |
|---------|-----|-----|---------|
| Control plane | AWS managed | AWS managed (K8s API) | N/A (compute only) |
| Infra mgmt | EC2 or Fargate | EC2 or Fargate | No servers |
| Complexity | Low | Higher (K8s) | Low |
| Best for | Fast AWS-native | K8s workloads/portability | Ops-light workloads |

Guidance
- Choose ECS+Fargate for fastest path; EKS when you need Kubernetes ecosystem; use EC2 launch types for lower cost/daemon needs, Fargate for simplicity.