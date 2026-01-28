# API Gateway 🌐

Managed service for creating, publishing, and managing RESTful APIs and WebSocket APIs.

## Overview

AWS API Gateway lets you create HTTP and REST APIs that act as a "front door" for applications. It handles infrastructure, authentication, caching, and scaling. Integrate with Lambda, EC2, RDS, or any HTTP endpoint.

## Key Features

- ✅ REST & HTTP APIs (different pricing, both auto-scale)
- ✅ WebSocket APIs (real-time bidirectional)
- ✅ Request validation & transformation
- ✅ Caching (reduce backend load)
- ✅ Rate limiting & throttling
- ✅ AWS IAM & custom authorizers
- ✅ CORS handling
- ✅ CloudFront integration (global delivery)

## Common Use Cases

**Mobile/Web Backend**: REST endpoints for apps
**Microservices**: Gateway pattern for routing
**Serverless**: Lambda + API Gateway (popular combo)
**Real-Time**: WebSocket for chat, notifications

## Pricing

```
REST API: $3.50 per 1M requests + $0.09/GB data
HTTP API: $0.90 per 1M requests (cheaper!)
WebSocket: $1.00 per 1M connections + $0.25 per 1M messages
```

Example: 10M API requests/month = $35/month (REST)

## Best Practices

✅ Use HTTP API if caching not needed (cheaper)
✅ Enable request validation
✅ Use API keys for rate limiting
✅ Enable X-Ray tracing
✅ Version APIs (/v1/, /v2/)
✅ Use CloudWatch logging
✅ Implement request throttling
✅ Cache responses when possible

## Related Topics

- [Full API Gateway Guide](./what-is-api-gateway.md)
- [Lambda Integration](../../compute/lambda/what-is-lambda.md)
- [Cognito Authentication](./cognito/README.md)

## Resources

- [API Gateway Docs](https://docs.aws.amazon.com/apigateway/)
- [REST API Best Practices](https://restfulapi.net/)