# Microservices on AWS

TL;DR
- Run microservices with ECS/Fargate or EKS, API Gateway/ALB for ingress, service discovery with Cloud Map, and central observability.

Prerequisites
- Containerized services, VPC with private subnets, CI/CD pipeline to build images.

Steps
1. Registry: push images to ECR with lifecycle policies.
2. Orchestrator: choose ECS (simpler) or EKS (Kubernetes). Create cluster + Fargate profiles or node groups.
3. Networking: one VPC, per-service security groups, use Cloud Map or Kubernetes services for discovery.
4. Ingress: use ALB (path-based) or API Gateway + VPC Link to route to services.
5. Resilience: enable autoscaling (CPU/requests), retries/timeouts, circuit breakers.
6. Observability: emit logs to CloudWatch, traces via X-Ray/OTel, metrics for SLIs.

Cost notes
- ECS/EKS control plane (EKS $), compute (Fargate/EC2), load balancers, data transfer. Right-size and use Spot where safe.

Troubleshooting
- Tasks not starting: check IAM task role and subnet/SNAT reachability.
- 5xx at ALB: inspect target health, security groups, app logs.

Checklist
- Images in ECR
- Cluster + services running
- Ingress routing working
- Logs/metrics/traces enabled