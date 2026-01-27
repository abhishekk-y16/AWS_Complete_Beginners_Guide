# Observability

TL;DR
- Combine CloudWatch metrics, logs, X-Ray traces, and OpenTelemetry for full-stack observability.

Prerequisites
- Services instrumented with SDKs or agents and correct IAM permissions.

Steps
1. Instrument application with X-Ray SDK and enable sampling.
2. Send logs to CloudWatch Logs and create Metric Filters.
3. Use CloudWatch ServiceLens or third-party APM tools for correlation.

Cost notes
- Additional tracing and high-cardinality metrics increase cost; sample traces where possible.

Troubleshooting
- Missing traces: confirm SDK initialization and IAM policies for X-Ray and CloudWatch.

Checklist
- Tracing enabled, logs centralized, dashboards created.
