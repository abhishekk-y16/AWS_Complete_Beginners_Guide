# CloudWatch vs X-Ray

When to use
- **CloudWatch**: metrics, logs, alarms, dashboards, synthetics.
- **X-Ray**: distributed tracing, service maps, latency breakdown.

Quick compare
| Feature | CloudWatch | X-Ray |
|---------|------------|-------|
| Data | Metrics/logs | Traces/segments |
| Use case | Infra/app health | Request-level debugging |
| Cost driver | Metrics + log ingest | Trace sampling volume |
| Setup | Agents/SDK env vars | SDK/OTel instrumentation |

Guidance
- Use CloudWatch for dashboards/alarms; add X-Ray/OTel for tracing critical paths.
- Sample traces (5-10%) to control cost; keep logs indexed for errors.