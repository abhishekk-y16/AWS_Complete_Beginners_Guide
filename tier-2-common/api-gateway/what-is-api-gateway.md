# What is API Gateway? 🚪

Create, publish, and manage REST/HTTP APIs that connect to backend services.

## Core Concept

**API Gateway** acts as the "front door" for your applications, routing HTTP requests to backend services.

```
Without API Gateway:
├─ Client directly accesses Lambda
├─ Security exposed
├─ Rate limiting: none
├─ Logging: manual
└─ CORS, auth: manual implementation

With API Gateway:
├─ API Gateway → Lambda (secure)
├─ Built-in rate limiting
├─ Automatic logging
├─ CORS handling
├─ Authentication/authorization
└─ All managed automatically!
```

## Architecture

```
Client Requests:
    ↓
API Gateway (Front Door)
    ├─ Validate request
    ├─ Check authentication
    ├─ Apply rate limits
    ├─ Route to backend
    ↓
Backend Services:
    ├─ Lambda functions
    ├─ EC2/containers
    ├─ HTTP endpoints
    └─ On-premises systems
    ↓
API Gateway (Response)
    ├─ Format response
    ├─ Log request
    └─ Send to client
```

## API Types

### 1. REST API

Traditional RESTful API with resources and methods.

```
API Structure:
/api/
├─ /users
│  ├─ GET /users → List all users
│  ├─ POST /users → Create user
│  └─ /users/{id}
│     ├─ GET → Get user details
│     ├─ PUT → Update user
│     └─ DELETE → Delete user
├─ /orders
│  ├─ GET → List orders
│  └─ POST → Create order
└─ /products/{id}
   └─ GET → Product details
```

### 2. HTTP API

Modern, simpler alternative to REST API.

```
HTTP API:
├─ Faster (40% lower latency)
├─ Cheaper (cheaper pricing)
├─ Simpler configuration
├─ Best for: Simple APIs, mobile apps

vs REST API:
├─ REST: Full control, all features
├─ HTTP: Simpler, faster, cheaper
```

### 3. WebSocket API

Bidirectional communication for real-time apps.

```
WebSocket Use Cases:
├─ Chat applications (messages in real-time)
├─ Live notifications (stock prices, alerts)
├─ Gaming (multiplayer real-time)
├─ Collaborative tools (shared editing)
└─ IoT sensors (live data streaming)
```

## REST API Example

```
Scenario: Pet store API

Resources:
├─ /pets
│  ├─ GET /pets
│  │  ├─ Query: ?type=dog&breed=labrador
│  │  └─ Response: [{"id": 1, "name": "Max"}, ...]
│  └─ POST /pets
│     ├─ Body: {"name": "Bella", "type": "cat"}
│     └─ Response: {"id": 2, "name": "Bella", ...}
└─ /pets/{petId}
   ├─ GET /pets/1
   │  └─ Response: {"id": 1, "name": "Max", "type": "dog"}
   ├─ PUT /pets/1
   │  └─ Update pet details
   └─ DELETE /pets/1
      └─ Remove pet
```

## Integration Points

```
API Gateway can connect to:

1. Lambda (Serverless)
   └─ AWS managed, pay per invocation

2. HTTP Endpoints
   ├─ EC2 instances
   ├─ On-premises servers
   └─ External APIs

3. AWS Services
   ├─ Directly call DynamoDB
   ├─ Directly call SNS
   └─ Any AWS service with SDK

4. Mock Responses
   └─ Testing without backend

5. VPC Link
   └─ Private endpoints inside VPC
```

## Authentication & Authorization

### API Key

Simple key-based access:

```
Client Request:
    ↓
GET /api/users HTTP/1.1
X-API-Key: abc123xyz789

API Gateway validates:
├─ Key exists?
├─ Key not revoked?
└─ Route allowed for this key?
```

### AWS IAM

Control access with IAM roles:

```yaml
IAM Policy:
{
  "Effect": "Allow",
  "Action": "execute-api:Invoke",
  "Resource": "arn:aws:execute-api:us-east-1:123456789:api-id/stage/GET/users",
  "Principal": "arn:aws:iam::123456789:role/my-app-role"
}
```

### Lambda Authorizer (Custom)

Use Lambda function for custom logic:

```python
def lambda_handler(event, context):
    token = event['authorizationToken']
    method_arn = event['methodArn']
    
    # Validate token with your backend
    if is_valid_token(token):
        return generate_policy('user', 'Allow', method_arn)
    else:
        return generate_policy('user', 'Deny', method_arn)
```

### Cognito User Pools

Manage user authentication:

```
Flow:
1. User signs up in Cognito
2. Gets JWT token
3. Sends JWT in API request
4. API Gateway validates with Cognito
5. Request allowed/denied
```

## Rate Limiting & Throttling

```
Prevent abuse and control traffic:

Usage Plan:
├─ Throttle: 10,000 requests/second
├─ Burst: 5,000 requests (temporary spike)
├─ Monthly quota: 1,000,000 requests
└─ Error: 429 Too Many Requests

Per-Client:
├─ API Key: john@example.com
│  ├─ Daily limit: 10,000 calls
│  └─ Cost: $100/month
├─ API Key: startup@example.com
│  ├─ Daily limit: 1,000,000 calls
│  └─ Cost: $10,000/month
└─ Default: 10,000 requests/second
```

## Caching

Improve performance with caching:

```
Cache Configuration:
├─ TTL (Time To Live): 300 seconds
├─ Cache size: 0.5GB (default) to 237GB
├─ Key: {method, path, query, headers}
└─ Invalidate: Manual or automatic

Performance:
├─ Without cache: 500ms response time
├─ With cache: 50ms response time
└─ 10x faster for repeated requests!

Cost:
├─ Small cache (0.5GB): $0.02/hour
├─ Large cache (237GB): $1.95/hour
└─ Usually saves costs with reduced Lambda invocations
```

## Logging & Monitoring

### Access Logs

```
GET /api/users HTTP/1.1
Host: api.example.com
X-API-Key: abc123

CloudWatch Log:
{
  "requestId": "abc123xyz",
  "ip": "192.168.1.1",
  "requestTime": "2024-01-15T10:00:00Z",
  "httpMethod": "GET",
  "resourcePath": "/users",
  "status": 200,
  "responseLength": 1024,
  "integrationLatency": 150
}
```

### CloudWatch Integration

```
Metrics automatically sent:
├─ 4XXError (invalid request)
├─ 5XXError (backend error)
├─ Count (total requests)
├─ Latency (response time)
└─ IntegrationLatency (backend time)

Alarms created automatically:
├─ Alert if 5XXErrors > 5
├─ Alert if Latency > 1000ms
├─ Alert if error rate > 1%
```

## CORS (Cross-Origin Resource Sharing)

Handle cross-origin requests:

```
Browser Request from example.com:
    ↓
API at api.other.com

Browser blocks (CORS policy!)
    ↓
API Gateway adds CORS headers:
├─ Access-Control-Allow-Origin: https://example.com
├─ Access-Control-Allow-Methods: GET, POST, PUT
├─ Access-Control-Allow-Headers: Content-Type
    ↓
Browser allows request ✅
```

## Cost Example

```
Scenario: Mobile app with 1M API calls/month

REST API Pricing:
├─ API calls: 1M × $0.0035 = $3.50
├─ Cache (if enabled): ~$0.50
└─ Monthly: ~$4

HTTP API Pricing (cheaper):
├─ API calls: 1M × $0.0015 = $1.50
├─ Cache: ~$0.50
└─ Monthly: ~$2

Backend (Lambda):
├─ 1M invocations
├─ 512MB for 500ms = 256GB-seconds
├─ $0.0000002 per GB-second × 256 = $0.05
└─ Total: ~$6

Total cost: ~$10/month for 1M API calls!
```

## Real-World Example: E-commerce

```
Product API:

GET /api/products
└─ Returns: 50,000 products
└─ Response: 5MB
└─ Cache: 300 seconds

First request:
├─ API Gateway routes to Lambda
├─ Lambda queries DynamoDB
├─ Response: 5MB (slow)
├─ Time: 500ms
└─ Cache stored

Second request (within 300s):
├─ API Gateway returns from cache
├─ Response: 5MB (instant)
├─ Time: 50ms
└─ No Lambda invocation (costs saved!)

Requests/min: 1000
├─ Uncached: 1000 Lambda invocations = $0.02
├─ Cached: ~20 Lambda invocations = $0.0004
└─ Daily savings: ~$0.40/day!
```

## Common Mistakes

### ✗ Mistake 1: No Rate Limiting

```
Wrong:
├─ API with no rate limits
├─ Attacker sends 1M requests/second
├─ Service crashes
└─ Huge Lambda bill!

Right:
├─ Rate limit: 10,000 requests/second
├─ Attacker blocked at 10K
└─ Service stable, low cost
```

### ✗ Mistake 2: No Authentication

```
Wrong:
├─ Public API, no auth required
├─ Anyone can access data
├─ GDPR violation, liability!

Right:
├─ API key required
├─ IAM roles checked
├─ Cognito for user auth
└─ Audit trail maintained
```

### ✗ Mistake 3: Disabled Logging

```
Wrong:
├─ API Gateway with no logs
├─ Problem occurs
├─ No visibility into what happened
└─ Can't debug!

Right:
├─ Access logs to CloudWatch
├─ Errors logged automatically
├─ CloudTrail for API changes
└─ Complete audit trail
```

### ✗ Mistake 4: Cache Invalidation Issues

```
Wrong:
├─ Cache everything forever
├─ User sees stale data
├─ Update never appears

Right:
├─ Short TTL for dynamic data (60s)
├─ Long TTL for static data (3600s)
├─ Manual invalidation for critical updates
└─ Users see accurate data
```

## Deployment Patterns

### Canary Deployment

Roll out new version gradually:

```
Stage: Production
├─ Canary: Route 5% traffic to new version
├─ Monitor: Check errors and latency
├─ If good: Increase to 25%, then 100%
└─ If bad: Rollback to previous version

Benefit: Catch bugs before full rollout
```

### Blue-Green Deployment

```
Blue Environment (Current):
└─ 100% traffic to v1.0

Green Environment (New):
└─ 0% traffic to v2.0
└─ Fully tested and ready

Switch:
└─ Flip route to v2.0
└─ If problem: Flip back to v1.0
```

## Best Practices

✅ Enable CloudWatch logging
✅ Set rate limits appropriately
✅ Use authentication and authorization
✅ Enable caching for static content
✅ Use API keys for tracking usage
✅ Document API with OpenAPI/Swagger
✅ Version API endpoints
✅ Use stages (dev, staging, prod)
✅ Enable access logs for debugging
✅ Implement error handling consistently

## CLI Examples

```bash
# Create REST API
aws apigateway create-rest-api \
  --name PetStore \
  --description "Pet store API"

# Create resource
aws apigateway create-resource \
  --rest-api-id abc123 \
  --parent-id xyz789 \
  --path-part pets

# Create method
aws apigateway put-method \
  --rest-api-id abc123 \
  --resource-id def456 \
  --http-method GET \
  --authorization-type NONE

# List APIs
aws apigateway get-rest-apis
```

## Next Steps

→ [API Gateway Integrations](./integrations.md) - Connect to backends
→ [Authentication](./auth.md) - Secure your API
→ [Deployment](./deployment.md) - Release strategies