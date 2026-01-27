# Networking Basics

TL;DR
- Understand VPCs, subnets, routing, security groups, and NACLs.
- Use private subnets for databases and public subnets for internet-facing services.

Prerequisites
- VPC and basic IAM permissions.

Steps
1. Create a VPC with public and private subnets:
```
aws ec2 create-vpc --cidr-block 10.0.0.0/16
```
2. Create an Internet Gateway and attach it to the VPC.
3. Create route tables for public/private subnets and configure NAT Gateway for outbound internet from private subnets.
4. Apply security groups and NACLs for fine-grained access control.

Cost notes
- NAT Gateway and data transfer costs can add up; prefer NAT instances for extremely low-cost, low-throughput needs.

Troubleshooting
- Instance cannot reach internet: check route tables, IGW attachment, and subnet association.

Checklist
- VPC, subnets, IGW, route tables, and security groups configured.
