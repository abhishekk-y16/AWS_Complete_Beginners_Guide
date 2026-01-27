# SageMaker Quickstart

TL;DR
- Use SageMaker for managed ML training and hosting, start with built-in algorithms or bring-your-own container.

Prerequisites
- IAM role for SageMaker with S3 access and sufficient quotas for notebook/instances.

Steps
1. Upload training data to S3 and create a SageMaker training job using built-in algorithms.
2. Use SageMaker Studio or Notebook instances for experimentation.
3. Deploy models to real-time endpoints or Batch Transform for offline inference.

Cost notes
- Training and hosting instances can be expensive; use spot instances for training where possible.

Troubleshooting
- Failed training jobs: check IAM permissions, data format, and container logs in CloudWatch.

Checklist
- Data in S3, training job runs, endpoint deployed.
