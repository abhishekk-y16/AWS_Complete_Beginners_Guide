# Glue ETL Basics

TL;DR
- Use AWS Glue for serverless ETL and metadata cataloging; Glue jobs and crawlers automate schema discovery.

Prerequisites
- IAM role for Glue with S3 access and an S3 bucket for source/target.

Steps
1. Create a Glue Crawler to populate the Data Catalog from S3.
2. Create a Glue Job (Spark or Python shell) to transform data and write to a processed path.
3. Schedule jobs using triggers or EventBridge.

Cost notes
- Glue jobs are billed per Data Processing Units (DPUs); optimize job code and partitioning.

Troubleshooting
- Job failures: check job logs in CloudWatch and increase DPUs if needed.

Checklist
- Crawler created, job tested, catalog available in Athena.
