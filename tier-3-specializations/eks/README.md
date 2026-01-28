# EKS - Elastic Kubernetes Service ⛵

Managed Kubernetes service for deploying, managing, and scaling containerized applications.

## Overview

EKS is AWS's managed Kubernetes. AWS manages control plane, you manage worker nodes. Deploy Kubernetes manifests, leverage full Kubernetes ecosystem. Ideal for organizations standardizing on Kubernetes.

## Key Features

- ✅ Managed Kubernetes control plane
- ✅ Multi-AZ by default for high availability
- ✅ Automatic upgrades and patching
- ✅ EC2 and Fargate worker node options
- ✅ VPC networking integration
- ✅ IAM authentication and authorization

## Managed Control Plane

AWS manages:
- API Server
- etcd (state database)
- Scheduler
- Controllers
- Multi-AZ redundancy

You manage:
- Worker nodes (EC2 instances or Fargate)
- Pod deployment
- Application scaling

## Worker Node Options

- **EC2 Nodes**: You patch, manage, and scale
- **Fargate**: Serverless container execution
- **Mixed**: Combine EC2 and Fargate

## Core Components

- **Clusters**: EKS cluster definition
- **Node Groups**: EC2 instances running kubelet
- **Pods**: Smallest deployable unit
- **Services**: Expose pods to network
- **Ingress**: External HTTP/HTTPS access

## Use Cases

- **Microservices**: Service-oriented architecture
- **Data Processing**: Parallel job execution
- **Kubernetes Migration**: Lift-and-shift from on-premises
- **Multi-cloud Strategy**: Portable Kubernetes

## Pricing

- **Control Plane**: $0.10/hour (~$73/month)
- **Worker Nodes**: EC2 or Fargate pricing
- **Data Transfer**: Standard AWS egress rates

Example: Control plane + 3 t3.medium = ~$157/month

## Advantages vs ECS

✅ Full Kubernetes ecosystem
✅ Portable across clouds
✅ Advanced orchestration features
✅ Larger community support
❌ More complex than ECS

## Best Practices

✅ Use node groups for organization
✅ Implement pod security policies
✅ Use network policies for security
✅ Enable CloudWatch Container Insights
✅ Auto-scale nodes based on demand

## Next Steps

→ [EKS Documentation](https://docs.aws.amazon.com/eks/)
→ [Kubernetes Basics](https://kubernetes.io/docs/tutorials/)
→ [EKS Console](https://console.aws.amazon.com/eks/)