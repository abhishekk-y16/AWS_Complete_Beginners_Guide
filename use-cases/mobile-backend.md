# Mobile Backend

What it is
- Backend services for mobile apps with auth, APIs, storage, and push notifications.

Recommended stack
- Cognito for auth, API Gateway + Lambda for APIs, DynamoDB/S3 for data, SNS/Pinpoint for push.

Quick start
1. Set up Cognito User Pool + Identity Pool; configure hosted UI or SDKs.
2. Build APIs with API Gateway + Lambda; secure with Cognito authorizers.
3. Store user data in DynamoDB; files in S3; send push via SNS/Pinpoint.

Cost snapshot
- Largely pay-per-use; Cognito MAU-based, API GW/Lambda per request, DynamoDB on-demand.

Success metrics
- Signup/login success, P95 API latency, crash-free sessions, cost per MAU.