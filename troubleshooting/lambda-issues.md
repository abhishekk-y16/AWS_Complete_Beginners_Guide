# Lambda Troubleshooting Guide ⚡

Common Lambda issues and solutions.

## Lambda Function Timeout

### Symptom
```
Error: Task timed out after X seconds
Function runs too long
```

### Root Causes

**1. Function logic is slow**
- Inefficient code loops
- Database queries taking too long
- External API calls slow
- Large dataset processing

**2. Default timeout too low**
- Default: 3 seconds
- Some operations need more time
- Need to increase timeout

### Solutions

**1. Increase timeout**
- Lambda → Function → Configuration → General Configuration
- Timeout: Change to 15, 30, or 60 seconds
- (Maximum 15 minutes)

**2. Optimize code**
```python
# ✗ Slow - loops 1000 times
def handler(event, context):
    for i in range(1000):
        result = database.query("SELECT * FROM table")

# ✓ Fast - query once, loop results
def handler(event, context):
    results = database.query("SELECT * FROM table")
    for result in results:
        process(result)
```

**3. Use async operations**
```python
# ✗ Waits for each API call
for item in items:
    response = requests.get(f"https://api.example.com/{item}")

# ✓ Parallel requests (faster)
import asyncio
async def fetch_all(items):
    tasks = [fetch(item) for item in items]
    await asyncio.gather(*tasks)
```

**4. Cache results**
```python
# ✗ Queries every time
def handler(event, context):
    return database.query("SELECT COUNT(*) FROM users")

# ✓ Use caching - query once per 5 minutes
import time
last_result = None
last_time = 0

def handler(event, context):
    global last_result, last_time
    if time.time() - last_time > 300:  # 5 minutes
        last_result = database.query("SELECT COUNT(*) FROM users")
        last_time = time.time()
    return last_result
```

## Lambda Out of Memory

### Symptom
```
Error: An error occurred (ResourceLimitExceeded)
Java.lang.OutOfMemoryError
Process exited before completing request
```

### Solutions

**1. Increase memory**
- Lambda → Function → Configuration → General Configuration
- Memory: Increase from 128 MB → 256 MB → 512 MB
- Affects CPU and speed too!

**2. Check for memory leaks**
```python
# ✗ Memory leak - keeps growing
cache = {}

def handler(event, context):
    cache[uuid.uuid4()] = expensive_operation()
    return cache
```

**3. Don't store large objects**
```python
# ✗ Loads huge file every time
import json
with open('/tmp/huge-file.json') as f:
    data = json.load(f)

# ✓ Load once at module level
data = None
def initialize():
    global data
    with open('/tmp/huge-file.json') as f:
        data = json.load(f)

def handler(event, context):
    return data[event['key']]
```

**4. Check dependencies**
- Large libraries? Use Lambda Layers
- Import only what needed
- Check package size: Deployment package < 50MB

## Lambda Function Returns Wrong Output

### Symptom
```
Function executes but returns null/empty
Output doesn't match input
```

### Root Causes

**1. Not returning value**
```python
# ✗ Missing return
def handler(event, context):
    result = event['id'] * 2
    # No return!

# ✓ Has return
def handler(event, context):
    result = event['id'] * 2
    return result
```

**2. Wrong return format**
```python
# ✗ Wrong - string instead of dict
def handler(event, context):
    return "success"

# ✓ Correct - dict with statusCode
def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"result": "success"})
    }
```

**3. Exception not caught**
```python
# ✗ Exception fails
def handler(event, context):
    return event['missing_key']  # KeyError!

# ✓ Safe with error handling
def handler(event, context):
    try:
        return event.get('missing_key', 'default')
    except Exception as e:
        return {"error": str(e)}
```

### Solutions

**1. Use CloudWatch Logs**
- CloudWatch → Logs → /aws/lambda/function-name
- See actual output
- See errors

**2. Test locally**
```bash
# Test with AWS SAM
sam local invoke MyFunction -e event.json
```

**3. Add debugging**
```python
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def handler(event, context):
    logger.debug(f"Received event: {json.dumps(event)}")
    result = process(event)
    logger.debug(f"Returning: {json.dumps(result)}")
    return result
```

## Lambda Can't Access Resources

### Symptom
```
Error accessing S3, RDS, or other AWS service
Connection refused to database
```

### Solutions

**1. Check Lambda execution role**
- Lambda → Function → Configuration → Permissions
- Execution role shown?
- Has required permissions?

**2. Add policy to role**
```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject"
  ],
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

**3. Check VPC configuration**
- If Lambda needs database access
- Lambda → Configuration → VPC
- VPC selected?
- Subnets selected?
- Security group allows Lambda?

**4. Check security groups**
- If RDS/database in VPC
- Database security group
- Inbound rule for Lambda security group
- Port 3306 (MySQL) or correct port

**5. Check database credentials**
- Using Secrets Manager for credentials?
- Secret ARN correct?
- Lambda role has secrets:GetSecretValue permission?

## Lambda Environment Variables Not Loading

### Symptom
```
Environment variable undefined
process.env.API_KEY is null
os.environ['DB_HOST'] is None
```

### Solutions

**1. Check environment variables are set**
- Lambda → Function → Configuration → Environment Variables
- Variables listed?
- Not empty?

**2. Use correct variable name**
```python
# ✗ Wrong name
import os
api_key = os.environ['API_KEY']

# ✓ Correct - matches what's set
api_key = os.environ.get('API_KEY', 'default_value')
```

**3. Redeploy after changing**
- Change environment variable
- Deploy function
- Take ~10 seconds to apply

**4. Check function hasn't been reverted**
- Uploaded new version?
- Check $LATEST or specific version
- Make sure running latest

## Lambda Cold Starts Too Slow

### Symptom
```
First invocation slow (5+ seconds)
Subsequent invocations fast
```

### Causes

**1. Cold start is normal**
- Lambda starts new container first time
- Initialization code runs
- Libraries load
- This is expected

### Solutions

**1. Reduce deployment package size**
- Remove unnecessary dependencies
- Use Lambda Layers for shared code
- Smaller = faster cold start

**2. Optimize initialization code**
```python
# ✗ Connection in handler (slower)
def handler(event, context):
    db = psycopg2.connect(database="mydb")
    return db.query("SELECT * FROM users")

# ✓ Connection at module level (caches between invocations)
db = psycopg2.connect(database="mydb")

def handler(event, context):
    return db.query("SELECT * FROM users")
```

**3. Use Lambda Provisioned Concurrency**
- Lambda → Function → Aliases or Versions
- Provisioned Concurrency: Enable
- Sets aside reserved capacity
- Eliminates cold starts
- Costs more though!

**4. Use memory optimization**
- More memory = more CPU
- Faster execution
- Fast enough to offset cold start

## Lambda Permission Denied on Event Source

### Symptom
```
Cannot connect Lambda to S3/SQS/DynamoDB trigger
Error: Principal does not have permission
```

### Solutions

**1. Add Lambda permission**
```bash
aws lambda add-permission \
  --function-name my-function \
  --statement-id AllowS3Invoke \
  --action 'lambda:InvokeFunction' \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::my-bucket
```

**2. Or use console**
- Lambda → Function → Add Trigger
- Select service (S3, SQS, etc.)
- Grant permission when asked

**3. Check execution role**
- Function must have permission to read event source
- S3: s3:GetObject
- SQS: sqs:ReceiveMessage
- DynamoDB: dynamodb:GetRecords

## 📖 Related Resources

- [Lambda Documentation](../tier-1-foundational/lambda/README.md)
- [Serverless Best Practices](../best-practices/performance-optimization.md)
- [Common Errors Guide](common-errors.md)
- [Cost Optimization](../best-practices/cost-optimization.md)