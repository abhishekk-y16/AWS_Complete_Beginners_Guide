# Migrate to AWS

TL;DR
- Plan migration by assessing workloads, selecting migration patterns (rehost, replatform, refactor), and testing.

Prerequisites
- Inventory of applications, dependencies, and data size.

Steps
1. Assess application using AWS Application Discovery Service.
2. Choose migration strategy: lift-and-shift (EC2), containerize for ECS/EKS, or refactor for serverless.
3. Migrate data using AWS DataSync, Snowball, or Database Migration Service (DMS).
4. Validate functionality and performance in staging.

Cost notes
- Migration tools may have costs; data transfer and temporary parallel run costs should be planned.

Troubleshooting
- Connectivity issues during data migration: check bandwidth, endpoint config, and IAM permissions.

Checklist
- Assessment completed, migration plan approved, DMS/DataSync configured, cutover scheduled.
