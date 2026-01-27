# Redshift Quickstart

TL;DR
- Use Amazon Redshift for petabyte-scale data warehousing; start with RA3 nodes and the query editor.

Prerequisites
- VPC with private subnets and security groups allowing Redshift access.

Steps
1. Create a Redshift cluster with RA3 nodes and configure parameter groups.
2. Load data from S3 using `COPY` with IAM role access.
3. Analyze with Redshift Spectrum and set WLM queues for concurrency.

Cost notes
- Redshift can be expensive; use pause/resume and RA3 for managed storage separation.

Troubleshooting
- COPY failures: check IAM role, file formats, and network access to S3.

Checklist
- Cluster created, IAM role for S3 access, COPY completed.
