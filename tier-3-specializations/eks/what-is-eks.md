# What is EKS? ☸️

AWS's managed Kubernetes service for orchestrating containerized applications at enterprise scale.

## Core Concept

**EKS** (Elastic Kubernetes Service) manages the Kubernetes control plane for you. Focus on applications, not cluster management.

```
Self-Managed Kubernetes:
├─ Setup etcd (distributed database)
├─ Setup API server
├─ Setup scheduler
├─ Setup controller manager
├─ Monitor control plane
├─ Patch Kubernetes
├─ HA setup (3+ masters)
└─ Complex, requires k8s expertise

EKS:
├─ AWS manages control plane
├─ 99.95% uptime SLA
├─ Automatic patching
├─ Multi-AZ by default
├─ You only manage worker nodes
└─ Simpler, AWS responsible
```

## Architecture

```
EKS Cluster structure:

Control Plane (AWS Managed):
├─ API Server
├─ etcd (distributed database)
├─ Scheduler
├─ Controller Manager
├─ Cloud Controller Manager
└─ High availability (across AZs)

Worker Nodes (You manage):
├─ Node group 1 (t3.large × 2)
├─ Node group 2 (c5.xlarge × 3)
├─ Node group 3 (Fargate spot)
└─ Kubelet (agent on each node)

Add-ons (Integrated):
├─ VPC CNI (networking)
├─ CoreDNS (service discovery)
├─ kube-proxy (networking)
└─ aws-node (AWS integration)
```

## Node Group Types

### EC2 Managed Node Groups

```
You specify:
├─ Instance type: t3.large
├─ Desired count: 3
├─ Min/Max: 2-10
└─ Subnet/security groups

EKS manages:
├─ Launch configuration
├─ Auto Scaling Group
├─ AMI patching
├─ OS updates
└─ Health checks

Cost: Instance charges only
├─ 3× t3.large: $0.1104/hour each
├─ Total: 3 × $0.1104 × 730 = $242/month
└─ Control plane: $0.10/hour = $73/month

Total EKS cluster: ~$315/month base
```

### Fargate Nodes (Serverless)

```
You specify:
├─ Pod specs
├─ CPU/Memory
├─ Don't think about instances

AWS manages:
├─ Infrastructure
├─ Scaling
├─ Patching
└─ High availability

Cost: Per pod per hour
├─ 0.25 vCPU, 512MB: $0.0256/hour
├─ Run 5 pods continuously: $93/month
├─ Control plane: $0.10/hour = $73/month

Total Fargate setup: ~$166/month
```

## Kubernetes Basics on EKS

### Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: app
        image: myrepo/web:v2.1
        ports:
        - containerPort: 8080
        env:
        - name: ENVIRONMENT
          value: production
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
```

### Service Definition

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: web
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
  
  # This creates an AWS Network Load Balancer
  # External users access via NLB DNS name
```

## Pod Auto-Scaling

```
Horizontal Pod Autoscaler (HPA):

Current state:
├─ 3 pods, 50% CPU average
└─ Each pod: 0.5 vCPU, 256MB RAM

HPA policy:
├─ Target CPU: 70%
├─ Min pods: 2
├─ Max pods: 20

Traffic spike (Black Friday):
├─ T0: 50% CPU (3 pods)
├─ T2: 75% CPU → Add pods
├─ T4: 4 pods × 70% = running at capacity
├─ T6: 80% CPU → Add more pods
├─ T8: 6 pods × 60% CPU → balanced
├─ Users happy, no requests failing
└─ T7200: Traffic drops, -1 pod every 5 min
```

## Real-World Example: Microservices Platform

```
Setup: Kubernetes platform with 3 services

Namespace: production

Service 1: Frontend
├─ Replicas: 5
├─ Image: frontend:v3.2
├─ CPU: 0.25 vCPU
├─ Memory: 256MB
└─ Auto-scaling: 3-10 on CPU 70%

Service 2: API
├─ Replicas: 10
├─ Image: api:v2.1
├─ CPU: 0.5 vCPU
├─ Memory: 512MB
└─ Auto-scaling: 5-30 on CPU 75%

Service 3: Database
├─ StatefulSet: 1 primary + 2 replicas
├─ Image: postgres:14
├─ CPU: 2 vCPU
├─ Memory: 4GB
└─ No auto-scaling (stateful)

Infrastructure:
├─ 2 node groups: t3.2xlarge nodes
├─ 4 nodes total, can scale to 10
├─ EC2 cost: ~$600/month
├─ EKS control plane: ~$73/month
└─ Total: ~$673/month
```

## Networking

```
EKS networking model:

Pods communicate:
├─ Pod-to-pod: Direct, same/different nodes
├─ Pod-to-service: Via Kubernetes DNS
├─ Pod-to-external: Via NAT/security groups
└─ External-to-pod: Via LoadBalancer service

External access:
├─ LoadBalancer service creates AWS NLB/ALB
├─ DNS: External users resolve NLB DNS
├─ Ports: 80/443 exposed
└─ Cost: NLB ~$16/month + data charges

Internal services:
├─ ClusterIP: Only internal access
├─ Service DNS: api.default.svc.cluster.local
├─ No external cost
└─ Microservices communicate efficiently
```

## Best Practices

✅ Use Managed Node Groups (easier)
✅ Enable logging (CloudWatch)
✅ Use Fargate for variable workloads
✅ Implement resource requests/limits
✅ Use Auto Scaling
✅ Monitor with CloudWatch Container Insights
✅ Use Kubernetes RBAC
✅ Implement network policies
✅ Use persistent volumes for data
✅ Regular cluster updates

## Common Mistakes

✗ Not setting resource requests (node overfull)
✗ Using :latest tags (unpredictable)
✗ No auto-scaling (manual scaling slow)
✗ Not monitoring cluster
✗ Ignoring security (RBAC, network policies)
✗ Not backing up persistent data
✗ Over-provisioning nodes (cost waste)
✗ Not updating Kubernetes (security)

## EKS vs ECS

```
Comparison:

Kubernetes expertise needed:
├─ ECS: No (AWS-specific)
└─ EKS: Yes (standard Kubernetes)

Complexity:
├─ ECS: Lower (simpler model)
└─ EKS: Higher (more powerful)

Flexibility:
├─ ECS: Less (AWS-specific)
└─ EKS: More (industry standard)

When to use ECS:
├─ AWS-only shop
├─ Simple microservices
└─ Want to avoid ops

When to use EKS:
├─ Multi-cloud strategy
├─ Complex orchestration needs
├─ Already using Kubernetes
└─ Portability important
```

## Next Steps

→ [Deployments & Services](./deployments.md) - Advanced k8s
→ [Auto Scaling](./scaling.md) - HPA and cluster scaling
→ [Monitoring](./monitoring.md) - CloudWatch Container Insights