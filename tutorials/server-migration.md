# Server Migration

TL;DR
- Plan lift-and-shift migrations using AWS Migration Hub, Server Migration Service, or create AMIs.

Prerequisites
- Inventory of servers, credentials for source environment, and network connectivity.

Steps
1. Discover servers with AWS Application Discovery Service.
2. Use AWS Server Migration Service (SMS) or AMS agents to replicate VM images.
3. Convert and launch in EC2 and validate networking/security.

Cost notes
- Temporary replication and storage costs; plan for redundant snapshots.

Troubleshooting
- Replication failures: check network, agent versions, and permissions.

Checklist
- Servers inventoried, replication configured, tests passed.
