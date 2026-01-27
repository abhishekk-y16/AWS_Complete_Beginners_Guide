# DynamoDB Best Practices

TL;DR
- Use DynamoDB for key-value and document workloads; design single-table or multiple-table schemas based on access patterns.

Prerequisites
- IAM permissions and understanding of item size and throughput.

Steps
1. Model access patterns and choose partition/sort keys accordingly.
2. Use provisioned capacity with autoscaling or on-demand for unpredictable workloads.
3. Use Global Secondary Indexes (GSIs) sparingly and project only needed attributes.
4. Enable point-in-time recovery and backups.

Cost notes
- Costs are driven by read/write units and storage; GSIs add extra read/write costs.

Troubleshooting
- Hot partitions: design keys to distribute load and consider DAX or adaptive capacity.

Checklist
- Access patterns documented, autoscaling configured, backups enabled.
