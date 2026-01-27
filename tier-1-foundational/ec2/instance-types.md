# EC2 Instance Types

EC2 offers **500+ instance types** optimized for different workloads. Choosing the right instance type is critical for performance and cost optimization.

## 📊 Instance Type Naming Convention

### Format: `t3.medium`
```
t        3        .     medium
│        │              │
Family   Generation     Size
```

- **Family**: Workload type (t=burstable, m=general, c=compute, r=memory, etc.)
- **Generation**: Newer = better performance/price (use latest when possible)
- **Size**: nano < micro < small < medium < large < xlarge < 2xlarge ... 24xlarge

## 🎯 Instance Family Types

### 1. **General Purpose** (T, M, Mac)

Best for: Web servers, small databases, development environments

#### **T-Series (Burstable Performance)**
```
Ideal for: Variable workloads (dev/test, web servers, microservices)
Feature: CPU Credits (burst above baseline when needed)

t3.micro:   2 vCPU, 1 GB RAM,  $0.0104/hr (~$7.50/month)
t3.small:   2 vCPU, 2 GB RAM,  $0.0208/hr (~$15/month)
t3.medium:  2 vCPU, 4 GB RAM,  $0.0416/hr (~$30/month)
t3.large:   2 vCPU, 8 GB RAM,  $0.0832/hr (~$60/month)

CPU Credits:
- Accrue credits when CPU < baseline (e.g., 20% for t3.micro)
- Spend credits when CPU > baseline
- Unlimited mode: Keep bursting but pay extra

When to Use:
✅ Development/test environments
✅ Code repositories, blogs, small websites
✅ Microservices with variable traffic
❌ Steady high-CPU workloads (use C or M series instead)
```

#### **M-Series (Balanced)**
```
Ideal for: Enterprise applications, SAP, SharePoint, general workloads

m5.large:    2 vCPU,  8 GB RAM,  $0.096/hr
m5.xlarge:   4 vCPU, 16 GB RAM,  $0.192/hr
m5.2xlarge:  8 vCPU, 32 GB RAM,  $0.384/hr
m5.4xlarge: 16 vCPU, 64 GB RAM,  $0.768/hr

When to Use:
✅ Applications with balanced CPU/memory needs
✅ Medium-traffic web servers
✅ Backend app servers
✅ Small-medium databases
```

### 2. **Compute Optimized** (C)

Best for: Batch processing, media transcoding, high-traffic web servers, scientific modeling

#### **C-Series**
```
Ideal for: CPU-intensive workloads

c5.large:     2 vCPU,  4 GB RAM,  $0.085/hr
c5.xlarge:    4 vCPU,  8 GB RAM,  $0.170/hr
c5.2xlarge:   8 vCPU, 16 GB RAM,  $0.340/hr
c5.4xlarge:  16 vCPU, 32 GB RAM,  $0.680/hr
c5.24xlarge: 96 vCPU, 192 GB RAM, $4.08/hr

Features:
- 3.6 GHz Intel Xeon Scalable processors
- Up to 25 Gbps network bandwidth
- EBS-optimized by default

Real-World Examples:
✅ Video encoding (convert 1080p to 720p)
✅ Batch data processing (ETL jobs)
✅ Web servers handling 10K+ requests/sec
✅ Scientific simulations
✅ Machine learning inference (prediction, not training)

Cost Comparison:
Scenario: Encode 100 hours of video
- t3.medium (slow): 200 hours = $8.32
- c5.2xlarge (fast): 20 hours = $6.80 ✅ Cheaper + 10x faster!
```

### 3. **Memory Optimized** (R, X, Z)

Best for: Databases, in-memory caches (Redis, Memcached), big data analytics

#### **R-Series (High Memory)**
```
Ideal for: Databases, in-memory analytics

r5.large:     2 vCPU,  16 GB RAM,  $0.126/hr (8 GB per vCPU)
r5.xlarge:    4 vCPU,  32 GB RAM,  $0.252/hr
r5.2xlarge:   8 vCPU,  64 GB RAM,  $0.504/hr
r5.4xlarge:  16 vCPU, 128 GB RAM,  $1.008/hr
r5.24xlarge: 96 vCPU, 768 GB RAM,  $6.048/hr

When to Use:
✅ MySQL, PostgreSQL databases (1M+ rows)
✅ Redis/Memcached caches
✅ SAP HANA
✅ Apache Spark, Hadoop
```

#### **X-Series (Extreme Memory)**
```
Ideal for: Giant in-memory databases (SAP HANA, Redis)

x1e.xlarge:   4 vCPU,  122 GB RAM,  $0.834/hr
x1e.2xlarge:  8 vCPU,  244 GB RAM,  $1.668/hr
x1e.4xlarge: 16 vCPU,  488 GB RAM,  $3.336/hr
x1e.32xlarge: 128 vCPU, 3,904 GB RAM, $26.688/hr (nearly 4 TB RAM!)

When to Use:
✅ SAP HANA (in-memory database)
✅ Apache Spark (keep entire dataset in RAM)
❌ Overkill for most use cases (very expensive)
```

### 4. **Storage Optimized** (I, D, H)

Best for: NoSQL databases, data warehouses, distributed file systems, log processing

#### **I-Series (NVMe SSD)**
```
Ideal for: Low-latency, high IOPS workloads

i3.large:    2 vCPU,  15 GB RAM, 475 GB NVMe SSD,  $0.156/hr
i3.xlarge:   4 vCPU,  30 GB RAM, 950 GB NVMe SSD,  $0.312/hr
i3.2xlarge:  8 vCPU,  61 GB RAM, 1.9 TB NVMe SSD,  $0.624/hr

Performance:
- 3.3 million IOPS (read)
- 1.4 million IOPS (write)
- < 1ms latency

When to Use:
✅ Cassandra, MongoDB, Elasticsearch
✅ Real-time analytics
✅ Transactional databases (thousands of queries/sec)
```

#### **D-Series (Hard Disk)**
```
Ideal for: Massive sequential I/O (data warehouses)

d2.xlarge:   4 vCPU,  30 GB RAM, 6 TB HDD,   $0.690/hr
d2.2xlarge:  8 vCPU,  61 GB RAM, 12 TB HDD,  $1.380/hr
d2.8xlarge: 36 vCPU, 244 GB RAM, 48 TB HDD,  $5.520/hr

When to Use:
✅ Hadoop/HDFS clusters
✅ MapReduce, Apache Spark
✅ Log processing (TB of logs/day)
```

### 5. **Accelerated Computing** (P, G, F, Inf)

Best for: Machine learning, graphics rendering, video processing, scientific computing

#### **P-Series (GPU for ML Training)**
```
Ideal for: Deep learning model training

p3.2xlarge:  8 vCPU, 61 GB RAM, 1 V100 GPU,  $3.06/hr
p3.8xlarge: 32 vCPU, 244 GB RAM, 4 V100 GPUs, $12.24/hr
p4d.24xlarge: 96 vCPU, 1,152 GB RAM, 8 A100 GPUs, $32.77/hr

GPU Memory:
- V100: 16 GB (p3)
- A100: 40 GB (p4d)

When to Use:
✅ Training neural networks (TensorFlow, PyTorch)
✅ Natural language processing (GPT, BERT)
✅ Computer vision (image recognition)

Example:
Train ResNet-50 model:
- CPU (c5.9xlarge): 10 hours = $6.80
- GPU (p3.2xlarge): 1 hour = $3.06 ✅ 10x faster, cheaper!
```

#### **G-Series (GPU for Graphics/Inference)**
```
Ideal for: Graphics rendering, ML inference, video streaming

g4dn.xlarge:  4 vCPU, 16 GB RAM, 1 T4 GPU,  $0.526/hr
g4dn.2xlarge: 8 vCPU, 32 GB RAM, 1 T4 GPU,  $0.752/hr
g4dn.12xlarge: 48 vCPU, 192 GB RAM, 4 T4 GPUs, $3.912/hr

When to Use:
✅ ML inference (serving predictions)
✅ Video transcoding
✅ 3D rendering
✅ Game streaming
```

#### **Inf-Series (AWS Inferentia - Cheapest ML Inference)**
```
Ideal for: High-throughput ML inference

inf1.xlarge:  4 vCPU, 8 GB RAM, 1 Inferentia chip, $0.228/hr
inf1.6xlarge: 24 vCPU, 48 GB RAM, 4 Inferentia chips, $1.180/hr

When to Use:
✅ Image classification (1000s predictions/sec)
✅ Recommendation systems
✅ Natural language processing

Cost Comparison (1M inferences):
- CPU (c5.large): $5.00
- GPU (g4dn.xlarge): $2.50
- Inferentia (inf1.xlarge): $1.00 ✅ Cheapest!
```

## 🏆 How to Choose the Right Instance Type

### Step 1: Identify Workload Type

```
Web Server (moderate traffic):
→ General Purpose (T3, M5)

Batch Processing (CPU-heavy):
→ Compute Optimized (C5)

Database (lots of RAM needed):
→ Memory Optimized (R5)

NoSQL Database (disk-intensive):
→ Storage Optimized (I3)

ML Training:
→ GPU (P3, P4)

ML Inference (predictions):
→ Inferentia (Inf1) or GPU (G4)
```

### Step 2: Right-Size

Start with a guess, then monitor CloudWatch metrics:

```
CPU Utilization:
- < 20%: Downsize (save money)
- 20-70%: Just right ✅
- > 80%: Upsize (prevent slowness)

Memory Usage:
- < 50%: Consider smaller instance
- 50-80%: Good ✅
- > 90%: Risk of OOM (out of memory) - upsize!

Network:
- Check NetworkIn/NetworkOut metrics
- If hitting limits, use network-optimized instances
```

### Step 3: Consider Costs

```
Development: t3.micro (cheap, burstable)
Staging: t3.small or t3.medium
Production: m5.large or larger (stable performance)

Use Savings Plans or Reserved Instances for 40-70% discount!
```

## 🔄 Migration Path

### Typical Growth Pattern:
```
Stage 1: Startup/MVP
→ t3.micro or t3.small ($7-15/month)

Stage 2: First Customers
→ t3.medium ($30/month)

Stage 3: Growth
→ m5.large ($70/month)
→ Add Load Balancer + Auto Scaling (2-10 instances)

Stage 4: Scale
→ m5.xlarge or m5.2xlarge
→ Separate databases to r5 instances
→ Use Reserved Instances for 40% savings
```

## 💡 Pro Tips

### 1. **Start Small, Scale Up**
```
Don't guess big - start with t3.medium
Monitor for 1 week
Upsize if needed (takes 2 minutes)
```

### 2. **Free Tier**
```
t2.micro: 750 hours/month free for 12 months
= 1 instance running 24/7 for a year!
```

### 3. **Spot Instances for Batch Jobs**
```
Use c5.4xlarge spot: $0.20/hr instead of $0.68/hr
70% savings for fault-tolerant workloads!
```

### 4. **Use Latest Generation**
```
m6i > m5 > m4 (better performance/price)
Always use latest unless app requires specific hardware
```

## 📚 Quick Reference Table

| Use Case | Instance Family | Example | Monthly Cost (24/7) |
|----------|----------------|---------|---------------------|
| Small website | T3 | t3.micro | $7.50 |
| Dev/test server | T3 | t3.small | $15 |
| Production web app | M5 | m5.large | $70 |
| Batch processing | C5 | c5.2xlarge | $245 |
| MySQL database | R5 | r5.large | $91 |
| Redis cache | R5 | r5.xlarge | $182 |
| Cassandra node | I3 | i3.large | $113 |
| ML training | P3 | p3.2xlarge | $2,203 |
| ML inference | Inf1 | inf1.xlarge | $164 |

## 🔗 Related Topics

- [EC2 Pricing →](pricing.md)
- [Launching First Instance →](launching-first-instance.md)
- [Use Cases →](use-cases.md)
- [What is EC2? →](what-is-ec2.md)

---

**Next Step**: Understand [EC2 Pricing](pricing.md) to optimize costs.