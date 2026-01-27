# Serverless Data Lake

TL;DR
- Build a lightweight data lake using S3 (storage), Glue (catalog/ETL), and Athena (query) without servers.

Prerequisites
- S3 buckets for raw/processed, IAM roles for Glue/Athena, sample data.

Steps
1. Create S3 folders: `raw/`, `processed/`, `analytics/`.
2. Create Glue Crawler to catalog `raw/`; store metadata in Glue Data Catalog.
3. Create Glue ETL job (Spark or Python shell) to cleanse and write to `processed/` with partitions (e.g., `dt=`).
4. Query with Athena using external tables pointing to `processed/` paths; enable workgroup and result location.
5. Add Lake Formation permissions if using fine-grained access; monitor with CloudWatch.

Cost notes
- S3 storage/requests, Glue DPUs for jobs, Athena per-TB scanned; partition and compress to lower cost.

Troubleshooting
- Crawler mis-detects schema: specify classifiers or manual schema.
- Athena query slow/expensive: add partitions, use columnar formats (Parquet/ORC).

Checklist
- Catalog created, ETL job succeeds, Athena queries return expected rows, retention/lifecycle set.