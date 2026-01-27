# ECS Quickstart

TL;DR
- Run containerized apps with ECS using Fargate or EC2 launch types; use Task Definitions and Services.

Prerequisites
- Docker image in ECR or another registry and IAM permissions for ECS/ECR.

Steps
1. Push container image to ECR.
2. Create a Task Definition and Service, choosing Fargate for serverless containers.
3. Configure load balancer and service autoscaling.

Cost notes
- Fargate charges per vCPU and memory; EC2 costs depend on instance types and EBS storage.

Troubleshooting
- Task fails to start: check task IAM role, container definitions, and subnet/security group configuration.

Checklist
- Image in ECR, task definition valid, service healthy.
