# Debugging Guide 🧭

Workflow
1. **Reproduce** with clear inputs and timestamps.
2. **Logs**: CloudWatch Logs Insights query by `@logStream`, `@message`, `@timestamp`.
3. **Metrics**: check CloudWatch dashboards/alarms for spikes.
4. **Traces**: X-Ray/OTel for request path and latency.
5. **Config**: confirm IAM policies, env vars, network (SG/NACL/route tables).

Useful snippets (Logs Insights)
```
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

Network triage
- From EC2: `curl`, `dig`, `telnet <host> <port>`; check SG/NACL/route table.
- VPC Reachability Analyzer to trace path.

Permissions triage
- IAM Policy Simulator for denied actions; look for explicit denies or missing conditions.

Rollbacks
- For IaC changes, keep versions; prefer canary/linear deployments; enable automatic rollbacks on alarm.