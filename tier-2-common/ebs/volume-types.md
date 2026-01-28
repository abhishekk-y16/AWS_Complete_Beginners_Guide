# EBS Volume Types 💾

Choosing the right EBS volume type for your workload.

## Overview

```
EBS Volume Types:

1. General Purpose (gp3, gp2)
   ├─ Balanced price and performance
   ├─ Good for: Most workloads
   └─ Cost: Moderate

2. Provisioned IOPS (io2, io1)
   ├─ High performance, predictable I/O
   ├─ Good for: Databases, high-transaction apps
   └─ Cost: Expensive

3. Throughput Optimized (st1)
   ├─ High throughput, sequential I/O
   ├─ Good for: Big data, data warehouses
   └─ Cost: Moderate

4. Cold Storage (sc1)
   ├─ Low cost, infrequent access
   ├─ Good for: Archives, backups
   └─ Cost: Very cheap
```

## General Purpose (gp3) - Most Common

### Specs

```
gp3: General Purpose SSD

Performance:
├─ Baseline: 3,000 IOPS, 125 MB/s
├─ Burstable: Up to 16,000 IOPS, 1,000 MB/s
├─ Latency: 1-3ms
└─ Max volume size: 16 TB

Cost:
├─ $0.08 per GB-month
├─ 100GB volume: $8/month
├─ 1TB volume: $80/month
└─ 10TB volume: $800/month

When to use:
✅ Web servers
✅ Application servers
✅ Small databases
✅ Development/testing
✅ Default choice (unless specific needs)

When NOT to use:
❌ Very high transaction databases
❌ Massive throughput (1000+ MB/s)
❌ Extremely low latency (<1ms) requirements
```

### Configuration

```
Create gp3 volume:

1. Size: 10-16,000 GB
   └─ Choose based on data size + growth

2. IOPS: 3,000-16,000
   ├─ 3,000: Default (free)
   ├─ 10,000: Cost = $0.05/IOPS-month
   └─ 16,000: Cost = $0.80/month extra

3. Throughput: 125-1,000 MB/s
   ├─ 125 MB/s: Default (free)
   ├─ 500 MB/s: Good for apps
   └─ 1,000 MB/s: Peak performance

Example: gp3 for web app
├─ Size: 100GB ($8/month)
├─ IOPS: 3,000 (default, free)
├─ Throughput: 125 MB/s (default, free)
└─ Total: $8/month
```

## General Purpose (gp2) - Legacy

### Specs

```
gp2: Older general purpose option

Performance:
├─ Baseline: 100 IOPS (varies by size)
├─ Burstable: Up to 3,000 IOPS
├─ Latency: 1-5ms
└─ Max volume size: 16 TB

Cost:
├─ $0.10 per GB-month (more expensive than gp3)
├─ 100GB volume: $10/month
└─ 1TB volume: $100/month

Comparison to gp3:
┌─────────────────┬────────────┬────────────┐
│ Feature         │ gp2        │ gp3        │
├─────────────────┼────────────┼────────────┤
│ Cost            │ $0.10/GB   │ $0.08/GB   │
│ Baseline IOPS   │ 100-160    │ 3,000      │
│ Max IOPS        │ 3,000      │ 16,000     │
│ Throughput      │ 125 MB/s   │ 1,000MB/s  │
└─────────────────┴────────────┴────────────┘

Why choose gp3:
✅ gp3 is cheaper and faster
✅ Recommendation: Migrate from gp2 to gp3
```

## Provisioned IOPS (io2, io1) - Databases

### Specs

```
io2: Latest high-performance
├─ IOPS: 100-64,000 (tunable)
├─ Throughput: 125-1,000 MB/s
├─ Latency: < 1ms
├─ Cost: $0.125/GB + $0.065/IOPS-month
└─ Best for: Mission-critical databases

io1: Previous high-performance
├─ IOPS: 100-32,000
├─ Throughput: 125-500 MB/s
├─ Latency: < 1ms
├─ Cost: $0.125/GB + $0.065/IOPS-month
└─ Legacy (io2 preferred)

When to use:
✅ Production MySQL/PostgreSQL
✅ Oracle databases
✅ SAP HANA
✅ High-transaction applications
✅ Financial systems (must not lose data)

When NOT to use:
❌ Development/testing
❌ Web servers
❌ Batch jobs
❌ Cost is prohibitive
```

### Cost Example

```
io2 volume for production database:

Configuration:
├─ Size: 500GB
├─ IOPS: 20,000
└─ Throughput: 500 MB/s

Monthly cost:
├─ Storage: 500GB × $0.125 = $62.50
├─ IOPS: 20,000 × $0.065 = $1,300
└─ Total: $1,362.50/month

Comparison to gp3:
├─ Same workload on gp3: 500GB @ 3,000 IOPS = $40/month
├─ io2 premium: $1,362.50
└─ Difference: 34x more expensive!

But io2 guarantees:
✅ Predictable latency (< 1ms)
✅ 64,000 IOPS available (gp3 max 16,000)
✅ Sub-millisecond random I/O
✅ Perfect for mission-critical databases
```

## Throughput Optimized (st1) - Big Data

### Specs

```
st1: Throughput Optimized

Performance:
├─ Throughput: 125-500 MB/s (sequential)
├─ IOPS: Up to 500 IOPS
├─ Latency: 5-15ms (acceptable for batch)
└─ Max volume size: 16 TB

Cost:
├─ $0.045 per GB-month (cheapest for high throughput)
├─ 1TB volume: $45/month
├─ 10TB volume: $450/month
└─ 100TB volume: $4,500/month

When to use:
✅ Hadoop / Spark clusters
✅ Data warehouses
✅ Log processing
✅ Big data analytics
✅ Sequential reads (not random)
✅ Large files (> 1MB)

When NOT to use:
❌ Random I/O workloads
❌ Databases with small transactions
❌ Web servers
❌ Any latency-sensitive app
```

### Use Case Example

```
Data warehouse on st1:

Workload:
├─ 50TB of data
├─ Hadoop processing
├─ MapReduce jobs
└─ Batch processing (not real-time)

Volume configuration:
├─ 10 × st1 volumes, 5TB each
├─ Cost: 10 × 5TB × $0.045 = $2,250/month
└─ Total: ~$27,000/year

Alternative: gp3
├─ 50TB on gp3
├─ Cost: 50TB × $0.08 = $4,000/month
└─ Total: ~$48,000/year

Savings with st1:
└─ 44% cheaper! ($21,000/year)
```

## Cold Storage (sc1) - Archives

### Specs

```
sc1: Cold storage (rarely accessed)

Performance:
├─ Throughput: 12.5-250 MB/s
├─ IOPS: Up to 250 IOPS
├─ Latency: 5-30ms (slow, but acceptable)
└─ Max volume size: 16 TB

Cost:
├─ $0.015 per GB-month (cheapest option!)
├─ 1TB volume: $15/month
├─ 10TB volume: $150/month
└─ 100TB volume: $1,500/month

When to use:
✅ Archive/backup storage
✅ Disaster recovery (rarely accessed)
✅ Compliance storage (7 years retention)
✅ Cold data (accessed < 1x per month)
✅ Cost is primary concern

When NOT to use:
❌ Production systems
❌ Databases
❌ Frequent access
❌ Performance-sensitive
```

### Cost Comparison

```
Storing 1TB for 3 years:

gp3 (general purpose):
├─ Cost: 36 months × $80/month = $2,880
└─ Good for: Frequent access

st1 (throughput optimized):
├─ Cost: 36 months × $45/month = $1,620
└─ Good for: Big data, sequential reads

sc1 (cold storage):
├─ Cost: 36 months × $15/month = $540
└─ Good for: Archive, rarely accessed

Savings: sc1 is 81% cheaper than gp3!
```

## Comparison Matrix

```
┌──────────────┬─────────────┬────────────┬──────────┬──────────┐
│ Feature      │ gp3         │ io2        │ st1      │ sc1      │
├──────────────┼─────────────┼────────────┼──────────┼──────────┤
│ Use case     │ General     │ Database   │ Big Data │ Archive  │
├──────────────┼─────────────┼────────────┼──────────┼──────────┤
│ IOPS         │ 16K         │ 64K        │ 500      │ 250      │
├──────────────┼─────────────┼────────────┼──────────┼──────────┤
│ Throughput   │ 1000 MB/s   │ 1000 MB/s  │ 500 MB/s │ 250 MB/s │
├──────────────┼─────────────┼────────────┼──────────┼──────────┤
│ Latency      │ 1-3ms       │ <1ms       │ 5-15ms   │ 5-30ms   │
├──────────────┼─────────────┼────────────┼──────────┼──────────┤
│ Cost (1TB)   │ $80/mo      │ $1,300/mo  │ $45/mo   │ $15/mo   │
├──────────────┼─────────────┼────────────┼──────────┼──────────┤
│ Best for     │ ✅ Most     │ ✅ Mission │ ✅ High  │ ✅ Low   │
│              │ workloads   │ critical   │ throughput│ cost     │
└──────────────┴─────────────┴────────────┴──────────┴──────────┘
```

## Choosing the Right Type

### Decision Tree

```
What's your workload?

├─ Web server, app server?
│  └─ ➜ Use: gp3
│     └─ Default, good performance, cheap
│
├─ Production database?
│  ├─ High transaction rate?
│  │  └─ ➜ Use: io2
│  │     └─ Mission-critical, consistent latency
│  └─ Medium transaction rate?
│     └─ ➜ Use: gp3
│        └─ Good balance of cost/performance
│
├─ Big data / Data warehouse?
│  ├─ Sequential reads (Hadoop, Spark)?
│  │  └─ ➜ Use: st1
│  │     └─ High throughput, cost-effective
│  └─ Random access database?
│     └─ ➜ Use: gp3 or io2 (depends on scale)
│
├─ Archive / Backup storage?
│  └─ ➜ Use: sc1
│     └─ Cheapest, acceptable latency
│
└─ Default (unsure)?
   └─ ➜ Use: gp3
      └─ Best all-around choice for 2024+
```

## Best Practices

✅ Start with gp3 for most workloads
✅ Right-size volumes (don't over-provision)
✅ Monitor actual IOPS usage
✅ Use st1 for sequential workloads
✅ Use io2 only for mission-critical databases
✅ Use sc1 for cost-critical archives
✅ Enable EBS encryption for security
✅ Take regular snapshots (backups)
✅ Monitor with CloudWatch
✅ Consider auto-scaling for variable workloads

## Next Steps

→ [What is EBS](./what-is-ebs.md) - Full EBS overview