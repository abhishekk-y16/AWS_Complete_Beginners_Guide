# OpenSearch Quickstart

TL;DR
- Use Amazon OpenSearch Service for search and analytics workloads; provision domains with appropriate instance types and storage.

Prerequisites
- IAM permissions and VPC settings for OpenSearch domain.

Steps
1. Create an OpenSearch domain and configure access policies.
2. Ingest data using Logstash, Fluent Bit, or Kinesis Firehose.
3. Use Kibana/OpenSearch Dashboards for visualization and alerts.

Cost notes
- OpenSearch costs include instance hours, EBS storage, and optional UltraWarm for infrequent access.

Troubleshooting
- Cluster health issues: check shard allocation, memory pressure, and indices mapping.

Checklist
- Domain provisioned, ingest pipeline configured, dashboards created.
