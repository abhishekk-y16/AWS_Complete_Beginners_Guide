# What is ECS? 🐳

AWS's container orchestration service for running Docker containers at scale without managing Kubernetes.

## Core Concept

**ECS** (Elastic Container Service) simplifies Docker container management. Define tasks, set desired count, ECS handles deployment and scaling.

```
Manual Docker:
├─ Manage 50 servers
├─ Deploy containers manually
├─ Handle networking
├─ Monitor container health
├─ Scale manually
└─ Complex, error-prone

ECS:
├─ Define desired state (10 containers)
├─ ECS handles provisioning
├─ Auto-restart failed containers
├─ Auto-scaling built-in
└─ Managed service
```

## ECS Concepts

```
Application structure:

Task Definition:
├─ Image: docker:latest
├─ CPU: 256 (0.25 vCPU)
├─ Memory: 512MB
├─ Port mappings: 8080 → 80
├─ Environment variables
└─ Logging configuration

Service (High-level):
├─ Name: web-app-service
├─ Task definition: docker:1
├─ Desired count: 3 (3 containers running)
├─ Load balancer: ALB
├─ Auto-scaling: 3-10 containers based on CPU
└─ Deployment strategy: Rolling updates

Cluster:
├─ EC2 instances OR Fargate
├─ Networking (VPC, subnets)
├─ Security groups
└─ Monitoring (CloudWatch)
```

## Launch Types

### EC2 Launch Type (Manage instances)

```
You manage:
├─ EC2 instances
├─ OS patching
├─ Scaling (when to add more instances)
└─ Networking configuration

ECS manages:
├─ Bin-packing (which instance gets container)
├─ Container deployment
├─ Health checks
└─ Restart failed containers

Cost: EC2 instance charges only
├─ t3.small: $0.0231/hour = $17/month
├─ Run 4 instances: $68/month
├─ Plus 50GB EBS storage: +$5/month
└─ Total: ~$73/month base

Use case: High control needed, cost-sensitive
```

### Fargate Launch Type (Serverless)

```
You manage: Nothing!
├─ Just upload image
├─ Specify CPU/memory
├─ ECS handles everything else

AWS manages:
├─ Underlying infrastructure
├─ Scaling
├─ Patching
├─ High availability

Cost: Per CPU/memory combination
├─ 0.25 vCPU, 512MB: $0.0256/hour = $18.60/month per container
├─ Run 3 containers: $55.80/month
└─ No instance cost!

Use case: Simplicity, don't want ops overhead
```

## Task Definition Example

```yaml
{
  "family": "web-app",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {
      "name": "web",
      "image": "myrepo/web:latest",
      "portMappings": [
        {
          "containerPort": 8080,
          "hostPort": 8080
        }
      ],
      "environment": [
        {"name": "NODE_ENV", "value": "production"},
        {"name": "DEBUG", "value": "false"}
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/web",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

## Deployment Strategies

### Rolling Deployment (zero downtime)

```
Current: 4 containers running v1.0

Deploy v2.0:
├─ T0: Start container #5 (v2.0)
├─ T20s: Check health, ok
├─ T30s: Stop container #1 (v1.0)
├─ T40s: Start container #6 (v2.0)
├─ T50s: Stop container #2 (v1.0)
├─ T60s: Start container #7 (v2.0)
├─ T70s: Stop container #3 (v1.0)
├─ T80s: Start container #8 (v2.0)
├─ T90s: Stop container #4 (v1.0)
└─ Complete: 4 containers v2.0

Downtime: 0 minutes
Duration: ~90 seconds
Success rate: 100%
```

### Blue-Green Deployment (safest)

```
Blue (current): 4 containers v1.0
Green (new): Empty (will be v2.0)

Step 1: Create green service
├─ Deploy 4 containers v2.0
├─ All traffic still on blue
└─ Test green service

Step 2: Validation
├─ Run smoke tests
├─ Check metrics
└─ Verify success rate

Step 3: Switch traffic
├─ ALB switches to green
├─ Blue stays running (safety net)
└─ New users on v2.0

Step 4: Cleanup (optional)
├─ After 1 hour, delete blue
└─ Saves cost

Downtime: 0 seconds
Rollback: Instant (switch back to blue)
```

## Real-World Example: Microservices

```
E-commerce platform:

Service 1: User API
├─ Container: user-api:v3.2
├─ Desired count: 5
├─ CPU/Memory: 512MB/1GB
└─ Cost: 5 × $0.0256/hour = $110/month

Service 2: Product Catalog
├─ Container: catalog:v2.1
├─ Desired count: 10 (higher traffic)
├─ CPU/Memory: 256MB/512MB
└─ Cost: 10 × $0.0128/hour = $92/month

Service 3: Orders
├─ Container: orders:v1.8
├─ Desired count: 3
├─ CPU/Memory: 512MB/1GB
└─ Cost: 3 × $0.0256/hour = $66/month

Total Fargate cost: ~$268/month
Plus: ALB ($16), CloudWatch logs ($5)
Platform total: ~$290/month
Scaling: Auto-adds/removes containers based on CPU
```

## Auto-Scaling

```
Service configuration:

Current state: 5 containers, 45% CPU average

Scaling policy:
├─ Target CPU: 70%
├─ Scale up: Add 1 container when CPU > 70%
├─ Scale down: Remove 1 container when CPU < 20%
├─ Min containers: 3
├─ Max containers: 20

Traffic spike example:
├─ T0: 45% CPU (5 containers)
├─ T5min: 80% CPU (customers arriving)
├─ T10min: +1 container (6 total), CPU → 62%
├─ T15min: +2 containers (8 total), CPU → 50%
├─ T3000min: Traffic drops, -1 container/5min
└─ Back to 5 containers after 30 mins

Cost savings: Only pay for what you use!
```

## Best Practices

✅ Use Fargate for simplicity
✅ Use rolling deployments for safety
✅ Implement health checks
✅ Use CloudWatch for monitoring
✅ Store configs in environment variables
✅ Use container registries (ECR)
✅ Enable auto-scaling
✅ Monitor resource usage
✅ Use load balancing
✅ Version your task definitions

## Common Mistakes

✗ Not setting resource limits (OOM kills)
✗ Using :latest tag (unpredictable)
✗ Not configuring health checks
✗ Hardcoding config in images
✗ Not using load balancers
✗ Ignoring CloudWatch logs
✗ Over-provisioning capacity
✗ Manual scaling (use auto-scaling)

## Next Steps

→ [Task Definitions](./task-definitions.md) - Advanced configuration
→ [Service Auto-scaling](./auto-scaling.md) - Scaling strategies
→ [ECR Integration](./ecr.md) - Container registry setup