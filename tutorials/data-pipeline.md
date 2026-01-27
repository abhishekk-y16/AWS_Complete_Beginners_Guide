# Data Pipeline

TL;DR
- Build a simple data pipeline: ingest -> transform -> store using AWS services (Kinesis/S3/Lambda/Glue/Redshift).
- Use S3 as a raw landing zone and Glue for ETL/cataloging.
- Use Lambda for lightweight transformations and Kinesis for streaming.
- Automate schema discovery with Glue Crawlers.
- Partition data to optimize queries and cost.
- Monitor failures and set up retries.

Prerequisites
- AWS CLI configured and IAM roles for data services.
- Sample data source (files, stream, or events).

Steps
1. Create an S3 bucket for raw and processed data:
```
aws s3 mb s3://my-data-bucket
```
2. If streaming, create a Kinesis Data Stream and a Lambda consumer to write to S3.
3. Create a Glue Crawler to catalog raw data and run it:
```
aws glue create-crawler --name raw-crawler --role MyGlueRole --database-name rawdb --targets S3Targets=[{"Path":"s3://my-data-bucket/raw/"}]
```
4. Create a Glue job or Athena/Redshift ETL to transform and write to `processed/` with partitioning.
5. Schedule Glue jobs with Workflows or EventBridge for periodic runs.
6. Validate data by running sample queries in Athena and set up monitoring/alarms.

Cost notes
- Costs from S3, Glue jobs, Kinesis throughput, Lambda invocations, and query engines like Athena/Redshift. Partition to reduce query costs.

Quick troubleshooting
- Glue job fails: inspect job logs in CloudWatch and check IAM access to S3.
- Missing partitions in Athena: run MSCK REPAIR TABLE or re-run crawler.
- Data duplication: ensure idempotent consumers and checkpointing.

Checklist
- Raw and processed S3 buckets exist.
- Glue catalog and jobs configured.
- Monitoring and retries established.
# Tutorials

AWS Tutorials service