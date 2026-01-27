# S3 vs EBS vs EFS

When to use
- **S3**: object storage, durable, cheap, static sites, data lakes.
- **EBS**: block storage for a single EC2 instance.
- **EFS**: shared POSIX file system across instances.

Quick compare
| Feature | S3 | EBS | EFS |
|---------|----|-----|-----|
| Access | HTTP APIs | Block device to one instance | NFS multi-AZ |
| Durability | 11 9s | 99.8%-99.99% | 11 9s |
| Throughput | Scales with objects | Tied to volume type/size | Scales with size |
| Use cases | Backups, media, data lake | DB disks, boot volumes | Shared content, ML features |

Guidance
- Pick S3 for most unstructured data; EBS for low-latency block; EFS for shared Linux file systems.