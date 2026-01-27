# Observability with OpenTelemetry

TL;DR
- Use OpenTelemetry SDKs to emit traces/metrics to AWS Distro for OpenTelemetry or third-party backends.

Prerequisites
- Instrumented application and an OTel collector running (AWS Distro for OpenTelemetry recommended).

Steps
1. Add OTel SDK to your application and configure exporters (OTLP, X-Ray, CloudWatch).
2. Run the OTel Collector (as sidecar, DaemonSet, or service) and configure receivers/exporters.
3. Create dashboards and alerts from exported metrics and traces.

Cost notes
- Exporting high-cardinality metrics or full trace payloads can increase costs; sample and aggregate when needed.

Troubleshooting
- No traces: verify exporter endpoints and collector health.

Checklist
- SDK added, collector running, dashboards configured.
