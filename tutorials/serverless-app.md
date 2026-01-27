# Serverless App Deployment

TL;DR
- Build and deploy a simple serverless REST API with API Gateway + Lambda + DynamoDB.

Prerequisites
- AWS CLI, Node.js/Python runtime, and an S3 bucket for deployment artifacts.

Steps
1. Create a Lambda function and an IAM role with minimal permissions to access DynamoDB.
2. Create a DynamoDB table for persistence.
3. Create an API Gateway REST API and integrate it with Lambda.
4. Deploy and test endpoints; use SAM/Serverless Framework for repeatable deployments.

Cost notes
- Lambda and API Gateway costs are low for low-traffic apps; watch for large DynamoDB read/write capacity.

Troubleshooting
- 502/504 from API GW: check Lambda timeout and VPC configuration.

Checklist
- Lambda created, API Gateway routes configured, DynamoDB table healthy.
