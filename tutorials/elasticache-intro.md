# ElastiCache Introduction

TL;DR
- Use ElastiCache (Redis or Memcached) for in-memory caching to reduce database load and latency.

Prerequisites
- VPC with subnets and security groups configured for cache access.

Steps
1. Create a Redis or Memcached cluster with appropriate node types.
2. Configure parameter groups, snapshotting (for Redis), and shard/replica settings.
3. Use Redis for rich data structures and persistence; Memcached for simple caching workloads.

Cost notes
- Costs from node-hour usage and backup storage; pick instance sizes carefully.

Troubleshooting
- Connection errors: check security groups, engine version compatibility, and parameter group settings.

Checklist
- Cluster created, snapshots enabled (if needed), client config updated.
