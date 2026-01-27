# Lambda Best Practices

TL;DR
- Keep Lambdas small, use layers for dependencies, set appropriate timeouts/memory, and use provisioned concurrency for low-latency workloads.

Prerequisites
- Functions packaged and IAM roles for execution and resource access.

Steps
1. Package dependencies in Lambda Layers to reduce cold start sizes.
2. Set environment variables and avoid storing secrets directly; use Secrets Manager or Parameter Store.
3. Monitor cold starts via tracing and consider provisioned concurrency for critical endpoints.

Cost notes
- Lambda costs are per-invocation and per-duration; optimizing memory/time reduces costs.

Troubleshooting
- Timeouts: increase function timeout or optimize code; check VPC ENI limits for VPC-enabled Lambdas.

Checklist
- Layers used, secrets stored properly, monitoring enabled.
