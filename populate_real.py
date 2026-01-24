import os, glob

AWS = {
    's3': 'Object storage with 99.999999999% durability',
    'ec2': 'Virtual machines in cloud',
    'lambda': 'Serverless compute',
    'rds': 'Managed SQL database',
    'dynamodb': 'NoSQL database',
    'iam': 'Identity and access management',
    'vpc': 'Virtual private cloud',
    'cloudfront': 'Content delivery network',
    'ebs': 'Block storage volumes',
    'efs': 'Network file system',
    'glacier': 'Long-term cold storage',
    'elasticache': 'In-memory caching',
    'route53': 'Domain name service',
    'cloudwatch': 'Monitoring and logging',
    'logs': 'Log aggregation',
    'kms': 'Key management service',
    'secrets': 'Secrets manager',
    'sns': 'Simple notification',
    'sqs': 'Message queue',
    'kinesis': 'Stream processing',
    'opensearch': 'Search and analytics',
    'redshift': 'Data warehouse',
    'athena': 'Query S3 data',
    'emr': 'Elastic mapreduce',
    'batch': 'Batch processing',
    'apprunner': 'Container runtime',
    'ecs': 'Container orchestration',
    'eks': 'Kubernetes service',
    'elasticbeanstalk': 'Application platform',
}

count = 0
for md in sorted(glob.glob('**/*.md', recursive=True)):
    if any(x in md.lower() for x in ['readme', '.md~', 'all_services']):
        continue
    try:
        svc = os.path.basename(os.path.dirname(md)).replace('-', '').lower()
        name = os.path.basename(md).lower()
        title = os.path.basename(os.path.dirname(md)).replace('-', ' ').title()
        
        desc = AWS.get(svc, f'AWS {title} service')
        
        if 'what' in name:
            content = f'# What is {title}?\n\n{desc}\n\n## Key Info\n- AWS managed service\n- Auto-scaling capable\n- Enterprise security\n- Pay-as-you-go pricing'
        elif 'pricing' in name:
            content = f'# {title} Pricing\n\nVary by usage model\n\n## Cost Factors\n- Usage volume\n- Features used\n- Regional location'
        elif 'use' in name:
            content = f'# {title} Use Cases\n\n- Production workloads\n- Development/testing\n- Data processing\n- Application hosting'
        elif 'best' in name:
            content = f'# {title} Best Practices\n\n- Enable monitoring\n- Implement backups\n- Use encryption\n- Optimize costs\n- Regular audits'
        elif 'troubl' in name:
            content = f'# {title} Troubleshooting\n\n## Common Issues\n- Check IAM permissions\n- Verify security groups\n- Review CloudWatch logs\n- Confirm resource configuration'
        else:
            content = f'# {title}\n\n{desc}'
        
        with open(md, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
    except Exception as e:
        pass

print(f' Successfully updated {count} files')
