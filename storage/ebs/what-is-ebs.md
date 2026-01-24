# Amazon EBS (Elastic Block Store)

## 🎯 What is EBS?

Amazon EBS is a block storage service that provides persistent storage volumes that attach to EC2 instances. Think of it as an external hard drive for your virtual computer in the cloud. Unlike instance storage (which disappears when you stop your instance), EBS volumes retain your data and can be backed up.

## 🔑 Key Concepts

- **Volume**: A block storage unit that attaches to EC2 instances (like a hard drive)
- **Snapshot**: A point-in-time backup of your EBS volume
- **IOPS**: Input/Output Operations Per Second (performance metric)
- **Throughput**: Data transfer speed (MB/s)
- **Multi-Attach**: Attach one volume to multiple EC2 instances
- **Encryption**: Automatically encrypt data at rest
- **Availability Zone**: Volumes exist in single AZ (must be same as instance)

## 💡 Real-World Analogy

EBS is like **a removable hard drive for your cloud computer**:
- **EBS Volume = External hard drive** that you plug into your EC2 instance
- **Snapshots = Backups** of your drive you can save
- **IOPS = Drive speed** (how many operations per second)
- **Instance Storage = Built-in drive** (gone when computer shut down)
- **Encryption = Hard drive lock** (protects data)

## 🚀 Common Use Cases

1. **Database Storage**: PostgreSQL, MySQL, Oracle databases need persistent storage
2. **Application Data**: Store application files, logs, configurations
3. **Boot Volumes**: Operating system installation for EC2 instances
4. **High-Performance Computing**: Applications needing fast I/O
5. **Backup & Recovery**: Create snapshots for disaster recovery
6. **Data Analytics**: Store large datasets for processing

## 💰 Pricing Overview

### Volume Storage
- **General Purpose (gp3)**: $0.10/GB/month
- **General Purpose (gp2)**: $0.10/GB/month
- **Provisioned IOPS (io1)**: $0.125/GB/month + $0.065 per provisioned IOPS
- **Throughput Optimized (st1)**: $0.045/GB/month
- **Cold HDD (sc1)**: $0.015/GB/month
- **Magnetic (standard)**: $0.05/GB/month

### Free Tier
- **30 GB** of EBS storage per month

## ⚠️ Important Things to Know

- **Single AZ**: EBS volumes exist in one Availability Zone only
- **Availability**: 99.999% uptime SLA for volumes
- **Encryption**: Can enable at volume creation (can't change after)
- **Snapshots**: Incremental backups (only changes stored)
- **Performance**: Depends on volume type and IOPS provisioned
- **Instance Attachment**: Can detach and reattach to different instance (in same AZ)

## 🔗 Related Services

- **EC2**: Uses EBS volumes for storage
- **S3**: Long-term backup of EBS snapshots
- **AWS Backup**: Automated EBS backup service
- **CloudWatch**: Monitor EBS performance metrics

## 🆘 Common Issues & Solutions

### Problem: "Insufficient capacity" error when creating volume
**Solution**: Try different AZ or volume type

### Problem: Poor performance on io1 volume
**Solution**: Verify provisioned IOPS is sufficient; check if volume is attached to right instance type

## 💡 Best Practices

- Use gp3 for most workloads (better price/performance than gp2)
- Enable encryption for sensitive data
- Create snapshots regularly for backup
- Tag volumes for cost tracking
- Monitor CloudWatch metrics for performance issues

## 📖 Additional Resources

- [EBS Documentation](https://docs.aws.amazon.com/ebs/)
- [EBS Volume Types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [EBS Best Practices](https://docs.aws.amazon.com/ebs/latest/userguide/best-practices.html)
