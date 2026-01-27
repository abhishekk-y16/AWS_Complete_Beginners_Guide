# Cost Optimization

TL;DR
- Right-size resources, use Savings Plans/Reserved Instances, schedule on/off for non-prod, and use cost allocation tags.

Prerequisites
- Billing access and Cost Explorer enabled.

Steps
1. Enable Cost Explorer and set budgets and alerts.
2. Identify idle/underutilized resources and right-size them.
3. Use Savings Plans or RI for stable workloads.
4. Automate start/stop for dev resources with Instance Scheduler or Lambda.
5. Use S3 lifecycle policies and Glacier for infrequent data.

Cost notes
- Main costs come from compute, storage, and data transfer; monitor and adjust regularly.

Troubleshooting
- Unexpected bills: analyze Cost Explorer, check for untagged resources, or rogue accounts in org.

Checklist
- Budgets set, tags applied, RI/Savings Plans reviewed.
