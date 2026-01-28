# EC2 Use Cases 🚀

Real-world scenarios where EC2 solves specific problems.

## 1. Web Application Hosting

**Problem**: Need web app accessible 24/7

**Solution**: Multi-AZ deployment with load balancer
```
ALB (Load Balancer)
  ├─ EC2 (m5.large)
  └─ EC2 (m5.large)
     │
     └─ RDS Database

Cost: ~$150-200/month
Benefits: High availability, auto-scaling
```

## 2. Development/Testing

**Problem**: Developers need isolated test environments

**Solution**: Each dev gets personal t3.small instance
```
Can start/stop as needed
Cost: ~$15/month when running
Benefits: Safe to experiment, no conflicts
```

## 3. Batch Processing

**Problem**: Process 1TB data weekly (takes 4 hours)

**Solution**: Spin up 8x c5.xlarge instances
```
Monday 2am: Launch instances
2 hours: Process data
Write to S3
Terminate instances

Cost: 2h × 8 × $0.17/h = $2.72
Benefit: Parallelization, cost-effective
```

## 4. Machine Learning Training

**Problem**: Train neural network on GPU (24 hours)

**Solution**: p3.2xlarge with GPU using Spot
```
On-demand: $587/day
Spot: $176/day (70% discount!)

Best for: Research, non-critical training
```

## 5. Disaster Recovery

**Problem**: Need backup if primary region fails

**Solution**: Standby AMI in secondary region
```
Primary (running): us-east-1
DR (stopped): us-west-2
Database: Replicated

Failover time: 5-10 minutes
Cost: ~50% of primary
```

## 6. Media Encoding

**Problem**: Convert videos to 5 formats (4 hours each)

**Solution**: Auto-scale EC2 with ffmpeg
```
Single instance: 4 hours per video
4 instances parallel: 1 hour per video

Cost: Only during processing
```

## 7. CI/CD Build Servers

**Problem**: Jenkins needs build agents on demand

**Solution**: Auto-scale agents based on queue
```
10 pending builds
Auto-launch 10x t3.small agents
Parallel processing
Terminate when done

Benefits: Fast builds, cost-effective
```

## 8. VPN/Bastion Host

**Problem**: Secure access to private resources

**Solution**: t3.micro bastion in public subnet
```
You SSH to bastion
From bastion: SSH to private DB

Cost: ~$10/month
Alternative: AWS Systems Manager (no bastion)
```

## 9. IoT Backend

**Problem**: Thousands of sensors need data processing

**Solution**: Auto-scaling API backend
```
Baseline: 3 instances
Peak: 50 instances
Back to 3 after peak

Cost: Only for spike resources
```

## 10. HPC/Scientific Computing

**Problem**: Simulation needs 1000+ cores

**Solution**: Cluster of EC2 instances
```
100x c5.4xlarge = 400 cores
50x c5.9xlarge = 1800 cores
Using Spot: $2-3/hour

Benefit: Massively scalable compute
```

## Choosing by Type

```
Web/App:        m5, t3 (general)
Databases:      r5 (memory)
Computing:      c5 (CPU)
GPU/ML:         p3, g4 (GPU)
High I/O:       i3 (storage)
Budget:         t3.micro (cheap)
```

## Cost Optimization

```
Production (24/7):      1-year RI (40% discount)
Development (daily):    Stop/start (70% savings)
Testing:               Spot instances (90% discount)
Batch/Scheduled:        Spot instances (90% discount)
```

## Disaster Recovery Strategies

```
Pilot Light:      Minimal DR resources (~cheap, 1h RTO)
Warm Standby:     Half capacity (~moderate, 15min RTO)
Hot Standby:      Full capacity (~expensive, <1min RTO)

Choose based on business criticality
```

## Next Steps

→ [Instance Types](./instance-types.md) - Choosing size
→ [Pricing](./pricing.md) - Cost details
→ [What is EC2](./what-is-ec2.md) - Overview