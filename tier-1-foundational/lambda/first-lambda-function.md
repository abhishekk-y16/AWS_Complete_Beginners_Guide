# Creating Your First Lambda Function 🚀

Step-by-step hands-on guide to create, deploy, and test your first AWS Lambda function.

## Prerequisites

Before you begin:

```
1. AWS Account
   ├─ Free tier eligible (1M invocations/month free)
   ├─ Create at: https://aws.amazon.com
   └─ Takes 10 minutes

2. IAM Permissions
   ├─ Lambda full access (AWSLambdaFullAccess)
   ├─ IAM role creation (IAMFullAccess)
   └─ Verify in IAM dashboard

3. Development Tools (optional)
   ├─ AWS CLI (for local development)
   ├─ Node.js 18+ OR Python 3.11+ (for local testing)
   └─ Text editor (VS Code recommended)

4. Basic knowledge
   ├─ JavaScript/Python basics
   ├─ JSON format
   └─ HTTP requests
```

## Method 1: AWS Console (Fastest - 5 minutes)

### Step 1: Navigate to Lambda

```
1. Log into AWS Console
   └─ URL: https://console.aws.amazon.com

2. Find Lambda service
   ├─ Search bar: "Lambda"
   ├─ Click: "Lambda" service
   └─ Region: Select us-east-1 (free tier eligible)

3. Dashboard
   ├─ Click: "Create function" (orange button)
   └─ You'll see: Function creation page
```

### Step 2: Configure Function

```
Basic settings:

1. Function name
   ├─ Name: my-first-function
   └─ Rules: Alphanumeric + hyphens only

2. Runtime
   ├─ Select: Node.js 18.x (or Python 3.11)
   └─ This is the language version

3. Execution role
   ├─ Select: Create new role
   ├─ Role name: lambda-basic-role
   ├─ Permissions: Basic Lambda@Edge trust policy
   └─ Click: Create function
```

### Step 3: Write Code

```
In the code editor:

Default code:
├─ exports.handler = async (event) => {
│  ├─ return {
│  │  ├─ statusCode: 200,
│  │  └─ body: JSON.stringify('Hello from Lambda!')
│  │ }
│  └─ };
└─ This is already there!

What it does:
├─ event: Input data from trigger
├─ handler: Main function that runs
├─ statusCode: HTTP response code (200 = success)
└─ return: Output back to caller
```

## Method 2: Node.js (With npm)

### Step 1: Create Project

```bash
# Create directory
mkdir my-lambda-function
cd my-lambda-function

# Initialize project
npm init -y

# Create main file
echo "exports.handler = async (event) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Hello from Lambda!' })
  };
};" > index.js
```

### Step 2: Package Function

```bash
# Create deployment package
zip -r function.zip index.js

# Result: function.zip (ready to upload)
```

### Step 3: Deploy via Console

```
1. Go to Lambda console
2. Create function (same as Method 1)
3. Code source → Upload from
4. Upload file: function.zip
5. Handler: index.handler
6. Click: Deploy
```

### Step 4: Test Function

```javascript
// Test with sample event:
{
  "name": "John",
  "action": "greet"
}

// Lambda will call handler(event)
// And return your response
```

## Method 3: Python

### Step 1: Create Project

```bash
# Create directory
mkdir my-lambda-python
cd my-lambda-python

# Create main file
cat > lambda_function.py << 'EOF'
import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Python Lambda!',
            'event': event
        })
    }
EOF
```

### Step 2: Package Function

```bash
# Create deployment package
zip function.zip lambda_function.py

# If you have dependencies:
# pip install -r requirements.txt -t .
# zip -r function.zip . 
```

### Step 3: Deploy

```
1. Lambda console → Create function
2. Runtime: Python 3.11
3. Upload function.zip
4. Handler: lambda_function.lambda_handler
5. Deploy
```

### Step 4: Test

```python
# Test event (JSON):
{
  "operation": "multiply",
  "operand1": 5,
  "operand2": 10
}

# Your function receives:
# event = {"operation": "multiply", ...}
# context = execution context (request ID, memory, etc.)
```

## Creating an API Endpoint

### Step 1: Create Function

```
Use Method 1 or 2 above to create function first
```

### Step 2: Add API Gateway Trigger

```
1. Lambda console → Your function
2. Add trigger → Select API Gateway
3. Create new API
   ├─ API type: REST
   ├─ Security: Open
   └─ Authorization: None (for demo)
4. Create
```

### Step 3: Test API

```
Your function now has a public URL!

Example:
└─ https://xxxxxxx.execute-api.us-east-1.amazonaws.com/default/my-first-function

Test it:
├─ Open in browser
├─ Or: curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/default/my-first-function
└─ You'll see: {"statusCode": 200, "body": "Hello from Lambda!"}
```

### Step 4: Add Query Parameters

```javascript
// Update your function:
exports.handler = async (event) => {
  // Get query parameter
  const name = event.queryStringParameters?.name || 'Guest';
  
  return {
    statusCode: 200,
    body: JSON.stringify({ 
      message: `Hello, ${name}!` 
    })
  };
};

// Now call:
// https://...../my-first-function?name=Alice
// Response: {"message": "Hello, Alice!"}
```

## Adding S3 Trigger

### Step 1: Create S3 Bucket

```
1. S3 console → Create bucket
2. Name: my-lambda-bucket-[random]
3. Click Create
```

### Step 2: Update Lambda Code

```javascript
// This processes uploaded files
const AWS = require('aws-sdk');
const s3 = new AWS.S3();

exports.handler = async (event) => {
  // Get bucket and key from S3 event
  const bucket = event.Records[0].s3.bucket.name;
  const key = event.Records[0].s3.object.key;
  
  console.log(`File uploaded: ${key} in ${bucket}`);
  
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'File processed!' })
  };
};
```

### Step 3: Add S3 Trigger

```
1. Lambda console → Add trigger
2. Source: S3
3. Bucket: my-lambda-bucket
4. Event: s3:ObjectCreated:*
5. Add
```

### Step 4: Test

```
1. Go to S3 console
2. Upload any file
3. Check CloudWatch Logs
4. You'll see: "File uploaded: filename in bucket-name"
```

## Environment Variables

### Set Variables

```
Lambda console → Configuration → Environment variables

Add:
├─ Key: DB_HOST
├─ Value: database.example.com
└─ Click Save
```

### Access in Code

```javascript
// Node.js
const dbHost = process.env.DB_HOST;
const apiKey = process.env.API_KEY;

console.log(`Connecting to ${dbHost}`);

exports.handler = async (event) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ host: dbHost })
  };
};
```

```python
# Python
import os

db_host = os.environ.get('DB_HOST')
api_key = os.environ.get('API_KEY')

print(f'Connecting to {db_host}')

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'host': db_host})
    }
```

## Using Lambda Layers

### Step 1: Create Layer

```
Scenario: You need npm packages (axios, lodash, etc.)

Create layer:
1. Lambda console → Layers
2. Create layer
3. Name: my-dependencies
4. Upload .zip file (see Step 2)
```

### Step 2: Package Dependencies

```bash
# Create directory structure
mkdir -p nodejs
cd nodejs

# Install packages
npm install axios lodash

# Package layer
cd ..
zip -r layer.zip nodejs

# Upload in Lambda console
```

### Step 3: Attach to Function

```
1. Lambda console → Your function
2. Code → Layers
3. Add layer → Custom layer
4. Select: my-dependencies
5. Add
```

### Step 4: Use in Code

```javascript
// Now available!
const axios = require('axios');
const _ = require('lodash');

exports.handler = async (event) => {
  const data = await axios.get('https://api.example.com');
  const processed = _.groupBy(data, 'type');
  
  return {
    statusCode: 200,
    body: JSON.stringify(processed)
  };
};
```

## Monitoring and Debugging

### CloudWatch Logs

```
Auto created for each function:

1. Lambda console → Your function
2. Click Monitor tab
3. View CloudWatch logs

Logs show:
├─ START RequestId: ...
├─ Your console.log() output
├─ END RequestId: ...
├─ REPORT Duration: 245ms, Memory: 128MB
└─ Any errors that occurred
```

### Adding Logs

```javascript
// Node.js
exports.handler = async (event) => {
  console.log('Event received:', JSON.stringify(event));
  
  const result = doSomething();
  console.log('Processing result:', result);
  
  return { statusCode: 200, body: JSON.stringify(result) };
};

// Each console.log shows in CloudWatch
```

### CloudWatch Metrics

```
View in Monitor tab:

├─ Invocations (how many times called)
├─ Duration (how long executions take)
├─ Errors (failed executions)
├─ Throttles (exceeding concurrency)
└─ ConcurrentExecutions (running right now)

Alert if:
├─ Error rate > 1%
├─ Duration > 5 seconds
├─ Throttles > 0
```

## Common Errors and Fixes

### Error 1: "Function is not permitted to..."

```
Problem: Lambda can't access RDS/S3/etc

Solution:
1. Lambda console → Configuration → Execution role
2. Click the role name (opens IAM)
3. Add inline policy
4. Grant permission for service
5. Save and retry

Example policy for S3:
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "*"
}
```

### Error 2: "Timeout (30 seconds)"

```
Problem: Function takes too long

Solutions:
1. Increase memory (higher memory = faster CPU)
   └─ Lambda console → Memory
   
2. Optimize code
   ├─ Remove unnecessary loops
   ├─ Use async/await properly
   └─ Cache expensive operations
   
3. Increase timeout
   └─ Configuration → General config → Timeout
```

### Error 3: "Module not found"

```
Problem: Can't find imported package (axios, etc.)

Solution 1: Add to code directory
└─ npm install [package]
└─ Include in deployment .zip
└─ Make sure package.json is uploaded

Solution 2: Use layers
└─ Create layer with dependencies
└─ Attach to function
└─ Now package available
```

### Error 4: "Cold Start (Slow First Invocation)"

```
Problem: First request takes 5 seconds, rest take 0.5s

Cause: AWS loading runtime

Solutions:
├─ Reduce code size (remove unused packages)
├─ Use smaller dependencies (lodash-es vs lodash)
├─ Pre-compile code (TypeScript → JavaScript)
├─ Use provisioned concurrency (costs extra)
└─ Just accept it (cold starts are normal!)

Typical cold start duration:
├─ Node.js: 0.5-1.5 seconds
├─ Python: 0.3-1 second
└─ Java: 1-3 seconds
```

## Best Practices

✅ Keep functions small (single responsibility)
✅ Use environment variables for secrets
✅ Add comprehensive logging
✅ Monitor with CloudWatch
✅ Test locally before deploying
✅ Version your functions
✅ Use layers for dependencies
✅ Handle errors gracefully
✅ Set appropriate memory
✅ Clean up old versions
✅ Use async appropriately
✅ Connection pooling for databases

## Next Steps

→ [Use Cases](./use-cases.md) - Where to use Lambda
→ [Triggers](./triggers.md) - Connect to AWS services
→ [Pricing](./pricing.md) - Cost optimization