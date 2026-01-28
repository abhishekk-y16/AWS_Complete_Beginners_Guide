# Troubleshooting AWS Issues 🔧

Comprehensive guide to diagnosing and resolving common AWS problems across all services.

## Quick Start

**Problem-solving workflow:**

```
Problem occurs
    ↓
Check AWS Status page (Is AWS down?)
    ↓
Check service health (CloudWatch)
    ↓
Review error message (logs, metrics)
    ↓
Search this guide by service/error
    ↓
Follow specific troubleshooting steps
    ↓
Problem solved!
```

## Service-Specific Guides

### Compute Services

**EC2 Issues:**
- Instances won't start
- Connection timeout (SSH/RDP)
- High CPU/Memory usage
- Insufficient capacity errors
- EBS volume issues
- Security group blocking traffic

**Lambda Issues:**
- Function timeout (15 min limit)
- Memory exceeded
- Cold start performance
- Permission denied errors
- Code deploy failures
- Concurrent execution limits

**Elastic Beanstalk Issues:**
- Deployment failures
- Health checks failing
- Instance communication issues
- Environment scaling problems
- Auto Scaling not working

### Storage Services

**S3 Issues:**
- Access denied errors (403)
- Slow upload/download speeds
- Objects not appearing
- Versioning confusion
- Lifecycle rule problems
- Cross-region replication lag

**EBS Issues:**
- Volume attach failures
- Performance degradation
- Snapshot issues
- Encryption problems
- IOPS throttling

### Database Services

**RDS Issues:**
- Connection refused
- Too many connections
- Query timeouts
- Replication lag
- Backup failures
- Parameter group conflicts

**DynamoDB Issues:**
- Throttling (ProvisionedThroughputExceededException)
- Hot partitions
- Query timeout
- Global secondary index problems
- Stream issues

### Networking Services

**VPC Issues:**
- No internet connectivity
- Cross-subnet communication fails
- NAT Gateway not working
- Route table problems
- Peering not functioning

**Security Group Issues:**
- Inbound traffic blocked
- Outbound traffic blocked
- Rule precedence confusion
- Ephemeral port range issues

**Route 53 Issues:**
- DNS resolution failing
- Records not updating
- Health checks failing
- Routing policy not working

### IAM and Security

**Permission Issues:**
- Access Denied errors
- Missing permissions
- Role assumption failures
- Policy evaluation issues

**Encryption Issues:**
- KMS key access denied
- Encryption/decryption failures
- Key rotation problems

## Common Error Messages and Solutions

### EC2 Errors

**"ConnectTimeout: Unable to connect"**
```
Diagnosis:
├─ Check: Security group allows port 22 (SSH) or 3389 (RDP)
├─ Check: Network ACL allows traffic
├─ Check: Instance has public IP or NAT gateway
├─ Check: Your client IP isn't blocked
└─ Check: Instance is running (not stopped)

Solution steps:
1. aws ec2 describe-instances --instance-ids i-xxx
2. aws ec2 describe-security-groups --group-ids sg-xxx
3. Check inbound rule: 
   ├─ Port 22 (SSH)
   ├─ Protocol: TCP
   └─ Source: Your IP (0.0.0.0/0 if public)
4. If missing, add rule: 
   aws ec2 authorize-security-group-ingress \
     --group-id sg-xxx \
     --protocol tcp \
     --port 22 \
     --cidr YOUR_IP/32
```

**"InsufficientInstanceCapacity"**
```
Diagnosis:
├─ AWS doesn't have capacity in that AZ
├─ Often happens in popular AZs during peak
├─ Instance type unavailable in that zone
└─ Happens with spot instances too

Solution steps:
1. Stop and start instance (moves to different host)
2. Or terminate and launch in different AZ
3. Use different instance type (t3.medium instead of t3.large)
4. Wait 5-10 minutes and retry
5. Request capacity increase (for reserved instances)
```

**"UnauthorizedOperation"**
```
Diagnosis:
├─ User lacks IAM permissions
├─ Security token expired
├─ Role doesn't have action
└─ Resource policy denies access

Solution steps:
1. Check IAM user permissions:
   aws iam get-user-policy --user-name USERNAME --policy-name POLICYNAME
2. Check attached policies:
   aws iam list-attached-user-policies --user-name USERNAME
3. Verify permissions include ec2:DescribeInstances, ec2:RunInstances, etc.
4. Check resource-based policies (if applicable)
5. Add missing permissions to IAM policy
```

### Lambda Errors

**"Task timed out after 15.00 seconds"**
```
Diagnosis:
├─ Function execution exceeds timeout
├─ Default timeout: 3 seconds
├─ Maximum timeout: 15 minutes (900 seconds)
└─ Often caused by waiting for external service

Solution steps:
1. Increase timeout in Lambda console:
   ├─ Configuration → General configuration → Timeout
   ├─ Set to reasonable value (30 seconds for API, 5+ min for batch)
   └─ Maximum: 15 minutes
2. Optimize code performance:
   ├─ Cache connections (don't recreate per invocation)
   ├─ Use connection pooling
   ├─ Remove unnecessary processing
   ├─ Use async/parallel processing where possible
   └─ Move long tasks to separate function
3. Consider Step Functions for long workflows
```

**"AccessDenied: User is not authorized to perform lambda:InvokeFunction"**
```
Diagnosis:
├─ Lambda execution role lacks permissions
├─ Trigger service doesn't have invoke permission
├─ API Gateway/S3 can't invoke Lambda
└─ Cross-account invocation attempted

Solution steps:
1. Check Lambda execution role:
   aws lambda get-function --function-name FUNC_NAME
   Look for "Role": "arn:aws:iam::..."
2. Check role permissions:
   aws iam list-role-policies --role-name ROLE_NAME
3. Add missing permission:
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Action": "lambda:InvokeFunction",
       "Resource": "arn:aws:lambda:REGION:ACCOUNT:function:FUNC_NAME"
     }]
   }
4. If trigger can't invoke:
   - S3: Add bucket policy with lambda:InvokeFunction
   - API Gateway: Add policy to Lambda
   - SNS/SQS: Add policy to Lambda
```

**"RequestLimitExceeded: Rate exceeded"**
```
Diagnosis:
├─ Concurrent execution limit hit (default 1,000)
├─ Function invoked >1,000 times simultaneously
├─ Temporary throttling (can be transient)
└─ Reserved concurrency too low

Solution steps:
1. Increase concurrency limit:
   aws lambda put-function-concurrency \
     --function-name FUNC_NAME \
     --reserved-concurrent-executions 5000
2. Optimize function:
   ├─ Make it faster (reduce execution time)
   ├─ Reduce number of invocations
   ├─ Batch requests together
   └─ Use async processing
3. Monitor concurrency:
   aws cloudwatch get-metric-statistics \
     --namespace AWS/Lambda \
     --metric-name ConcurrentExecutions \
     --start-time 2024-01-01T00:00:00Z \
     --end-time 2024-01-02T00:00:00Z \
     --period 300 \
     --statistics Maximum
```

### S3 Errors

**"AccessDenied: Access Denied"**
```
Diagnosis:
├─ User lacks S3:GetObject permission
├─ Bucket policy blocks access
├─ Object ACL blocks access
├─ Bucket is private (no public access)
└─ Block Public Access enabled

Solution steps:
1. Check user permissions:
   aws iam get-user-policy --user-name USER --policy-name POLICY
2. Verify bucket policy:
   aws s3api get-bucket-policy --bucket BUCKET_NAME
3. Check object ACL:
   aws s3api get-object-acl --bucket BUCKET_NAME --key OBJECT_KEY
4. Add missing permission:
   {
     "Effect": "Allow",
     "Action": ["s3:GetObject", "s3:PutObject"],
     "Resource": "arn:aws:s3:::bucket/*"
   }
```

**"ServiceUnavailable: Service is unavailable"**
```
Diagnosis:
├─ S3 experiencing issues (rare)
├─ Too many requests (rate limited)
├─ Bucket with high request rate (>3,500 PUT/COPY/POST/DELETE)
└─ Partition hotspot (all requests to few keys)

Solution steps:
1. Check AWS Status:
   https://status.aws.amazon.com/
2. Back off requests (exponential backoff):
   ├─ Wait 1 second, retry
   ├─ If fail, wait 2 seconds, retry
   ├─ If fail, wait 4 seconds, retry
   └─ Maximum: Don't exceed 100 retries
3. Distribute key names:
   ├─ Avoid: bucket/data.json (everyone writes here)
   ├─ Use: bucket/2024/01/28/12/34/data_HASH.json
   ├─ Spreads requests across partitions
   └─ Enables higher throughput
```

**"SlowDown: Please reduce your request rate"**
```
Diagnosis:
├─ Request rate > 100 TPS on bucket
├─ Partition throttling
├─ Often happens with batch operations
└─ Can be region-dependent

Solution steps:
1. Implement exponential backoff
2. Distribute key names (add date, uuid)
3. Use S3 Batch Operations (for bulk operations)
4. Use multi-part upload for large files
5. Consider CloudFront (for reads)
```

### RDS Errors

**"Communications link failure - Connection refused"**
```
Diagnosis:
├─ RDS instance not running
├─ Security group blocks traffic
├─ Subnet doesn't route to RDS
├─ RDS endpoint is wrong
├─ Wrong username/password
└─ Firewall on client side

Solution steps:
1. Check RDS status:
   aws rds describe-db-instances --db-instance-identifier INSTANCE_NAME
   Look for: DBInstanceStatus: available
2. Check security group:
   aws ec2 describe-security-groups --group-ids sg-xxx
   Verify: Port 3306 (MySQL), 5432 (PostgreSQL), etc.
3. Test connectivity:
   telnet RDS_ENDPOINT 3306
   curl -v mysql://user:pass@RDS_ENDPOINT
4. Check network:
   aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-xxx"
   Ensure route to RDS subnet exists
```

**"ERROR 1040 (HY000): Too many connections"**
```
Diagnosis:
├─ Max connections exceeded
├─ Connection pool exhausted
├─ Not closing connections
├─ Lambda creating new connections per invocation
└─ Application leak

Solution steps:
1. Check current connections:
   SHOW PROCESSLIST;
   SHOW STATUS LIKE 'Threads%';
2. Increase max connections:
   aws rds modify-db-parameter-group \
     --parameter-group-name PARAM_GROUP \
     --parameters "ParameterName=max_connections,ParameterValue=500,ApplyMethod=immediate"
3. Kill idle connections:
   SELECT CONCAT('KILL ',id,';') FROM INFORMATION_SCHEMA.PROCESSLIST WHERE TIME>300 AND INFO IS NULL;
4. Implement connection pooling:
   ├─ Aurora Proxy (serverless proxy)
   ├─ pgBouncer (PostgreSQL)
   ├─ ProxySQL (MySQL)
   └─ Application connection pool (HikariCP, etc.)
```

### DynamoDB Errors

**"ValidationException: One or more parameter values were invalid"**
```
Diagnosis:
├─ Query/scan syntax error
├─ Wrong attribute name
├─ Invalid key condition expression
├─ Type mismatch (string vs number)
└─ Missing required parameter

Solution steps:
1. Check KeyConditionExpression:
   ├─ Must use pk = value, sk > value format
   ├─ Can't use non-key attributes
   ├─ Correct: KeyConditionExpression="pk = :pk",
   ├─ Wrong: KeyConditionExpression="attribute = :val"
2. Check attribute types:
   ├─ Numbers in ExpressionAttributeValues must be strings: ":val": {"N": "123"}
   ├─ Strings: ":val": {"S": "value"}
3. Check attribute names:
   aws dynamodb describe-table --table-name TABLE_NAME
   Verify all attribute names match
```

**"ProvisionedThroughputExceededException: Rate exceeded"**
```
Diagnosis:
├─ Request rate > provisioned capacity
├─ Hot partition (uneven key distribution)
├─ Spike in traffic
└─ Insufficient capacity mode

Solution steps:
1. Switch to on-demand capacity:
   aws dynamodb update-table \
     --table-name TABLE_NAME \
     --billing-mode PAY_PER_REQUEST
   (Good for variable load)
2. Or increase provisioned capacity:
   aws dynamodb update-table \
     --table-name TABLE_NAME \
     --provisioned-throughput ReadCapacityUnits=1000,WriteCapacityUnits=1000
3. Optimize queries:
   ├─ Use GetItem instead of Scan
   ├─ Use Query with key condition
   ├─ Filter after retrieval (if needed)
4. Check distribution:
   - Ensure partition key values distributed evenly
   - Avoid timestamp as partition key (all go to one partition)
```

## Monitoring and Diagnostics

### CloudWatch Metrics to Check

```
For each service, check:

EC2:
├─ CPU Utilization (high = scaling needed)
├─ Network In/Out (indicates traffic)
├─ Disk Read/Write (storage bottleneck)
└─ Status Check (failed = instance issues)

Lambda:
├─ Invocations (how many executions)
├─ Errors (failed executions)
├─ Duration (execution time)
├─ Throttles (concurrency exceeded)
└─ ConcurrentExecutions (current load)

RDS:
├─ CPU Utilization
├─ Database Connections
├─ Read/Write Latency
├─ IOPS Used
└─ Free Storage Space

DynamoDB:
├─ ConsumedReadCapacityUnits
├─ ConsumedWriteCapacityUnits
├─ UserErrors (bad requests)
├─ SystemErrors (AWS issues)
└─ SuccessfulRequestLatency
```

### CloudWatch Logs Insights Queries

```
Find errors in Lambda logs:
fields @timestamp, @message, @duration
| filter @message like /ERROR/
| stats count() as error_count by @message

Find slow requests:
fields @timestamp, @duration
| stats avg(@duration) as avg_ms, max(@duration) as max_ms

Find 4xx vs 5xx errors:
fields @timestamp, status
| filter status >= 400
| stats count() by status

Find requests by user:
fields @timestamp, user, action
| filter user = "john@example.com"
```

## Best Practices for Troubleshooting

✅ Check AWS Status page first (is the service down?)
✅ Review CloudWatch metrics (trending up/down?)
✅ Check logs (error messages, stack traces)
✅ Verify IAM permissions (can the user do this?)
✅ Test connectivity (network reachable?)
✅ Check security groups/NACLs (traffic allowed?)
✅ Use CloudWatch Logs Insights (pattern search)
✅ Review recent changes (what changed before error?)
✅ Test in isolation (reproduce the issue)
✅ Document findings (for future reference)

## When to Escalate

Contact AWS Support if:
- AWS service is actually down (Status page shows incident)
- You suspect hardware failure (EBS issue, instance crash)
- Billing looks wrong (unexpected charges)
- Need emergency capacity increase
- DDoS attack suspected
- Security issue (possible breach)
- Quota limit needs increase (contact support)

## Useful Commands

```bash
# Check instance status
aws ec2 describe-instance-status --instance-ids i-xxx

# Check function logs
aws logs tail /aws/lambda/function-name --follow

# Get RDS endpoint
aws rds describe-db-instances --query 'DBInstances[0].Endpoint.Address'

# List recent errors
aws cloudwatch get-metric-statistics --namespace AWS/Lambda \
  --metric-name Errors --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-02T00:00:00Z --period 3600 --statistics Sum

# Check security group rules
aws ec2 describe-security-groups --group-ids sg-xxx

# Verify IAM permissions
aws iam simulate-custom-policy --policy-input-list file://policy.json \
  --action-names ec2:RunInstances --resource-arns arn:aws:ec2:*:*:*
```

## Additional Resources

- [AWS Troubleshooting Guide](https://docs.aws.amazon.com/troubleshooting/)
- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [AWS Status Dashboard](https://status.aws.amazon.com/)
- [AWS Support Center](https://console.aws.amazon.com/support/)
- [AWS Forums](https://forums.aws.amazon.com/)
