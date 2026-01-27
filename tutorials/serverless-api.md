# Serverless API (API Gateway + Lambda)

TL;DR
- Build a REST/HTTP API with API Gateway + Lambda, no servers to manage.

Prerequisites
- Lambda function code, IAM execution role, AWS CLI/SAM/Serverless Framework.

Steps
1. Author Lambda handler; package with dependencies (or use Lambda layers).
2. Create API Gateway (HTTP API for simpler/cheaper, REST API for full features).
3. Integrate routes to Lambda; enable CORS for your domain.
4. Deploy stage; obtain invoke URL.
5. Add custom domain via ACM + Route 53 if needed; set throttling and WAF if exposed publicly.

Cost notes
- Pay per request and duration; HTTP API cheaper than REST API. Watch data transfer.

Troubleshooting
- 5xx responses: check Lambda logs; increase timeout/integration settings.
- CORS issues: ensure allowed origins/headers/methods on API.

Checklist
- Routes mapped, CORS set, logging enabled, custom domain (optional) live.