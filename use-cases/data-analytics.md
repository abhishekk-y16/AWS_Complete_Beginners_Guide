# Data Analytics on AWS

What it is
- Ingest, store, and analyze data with a serverless lakehouse stack.

Recommended stack
- Ingest: Kinesis Data Streams/Firehose
- Storage: S3 data lake (raw/curated)
- Catalog/ETL: Glue + Lake Formation
- Query: Athena or Redshift Serverless

Quick start
1. Land data in S3 `raw/`; crawl with Glue to build schema.
2. Transform with Glue jobs into partitioned Parquet in `curated/`.
3. Query with Athena; visualize in QuickSight.

Cost snapshot
- S3 + Glue + Athena pay-per-use; Redshift Serverless for heavier workloads.

Success metrics
- TB scanned per query, data freshness, query latency, cost per query.