# AWS Lambda

## 🎯 What is Lambda?

AWS Lambda is a "serverless" compute service where you write code without needing to manage servers. You upload your code, and AWS automatically runs it when triggered by events (like a file upload, API request, or scheduled time). You only pay for the compute time you actually use, down to the millisecond.

It's like having a personal assistant who waits for something to happen, then immediately runs a specific task and goes back to waiting - you only pay them when they're working.

## 🔑 Key Concepts

- **Function**: Your code packaged with configuration
- **Handler**: The entry point - the specific function AWS calls to run your code
- **Trigger**: What causes your Lambda function to execute (S3 upload, API call, schedule, etc.)
- **Event**: The data passed to your Lambda function (e.g., which file was uploaded)
- **Runtime**: The language/environment (Python, Node.js, Java, Go, .NET, etc.)
- **Execution Role**: IAM role that defines what AWS services your function can access
- **Cold Start**: The delay when Lambda first initializes your function (usually < 1 second)
- **Concurrent Execution**: How many function instances can run simultaneously

## 💡 Real-World Analogy

AWS Lambda is like **a vending machine with special abilities**:

- **Your Function = The vending machine's action** (dispense snack, take payment)
- **Trigger = Someone inserting money** (event that starts the action)
- **Event Data = How much money, which button** (parameters/context)
- **Handler = The specific mechanism** that runs
- **Execution Role = Permissions** (can access cash drawer, restock list, etc.)
- **Concurrent Executions = Multiple machines** running simultaneously
- **Cold Start = Machine warming up** first time
- **Serverless = No one manages the building** - just the machine exists

## 🚀 Common Use Cases

### 1. **Automatic File Processing**
- User uploads image to S3 → Lambda resizes it
- User uploads PDF → Lambda extracts text
- Video uploaded → Lambda creates thumbnail

### 2. **Real-time Data Processing**
- IoT device sends data → Lambda processes and stores
- Website events → Lambda updates database
- Log processing in real-time

### 3. **REST APIs**
- Build web APIs with API Gateway + Lambda
- No need to manage servers
- Scales automatically

### 4. **Scheduled Tasks**
- Every day at 9 AM → Lambda sends email report
- Every hour → Lambda backs up database
- Weekly → Lambda cleans up old files

### 5. **Chatbots & Voice**
- Alexa skill backed by Lambda
- Chatbot processing NLP
- Voice assistant commands

### 6. **Stream Processing**
- Process Kinesis streams in real-time
- DynamoDB streams triggering Lambda functions
- Real-time analytics

### 7. **Website Personalization**
- User visits site → Lambda fetches personalized content
- CloudFront + Lambda@Edge for edge computing
- Serve custom content per user

### 8. **Cost Optimization Automation**
- Automatic AWS resource cleanup
- Stop unused instances
- Right-sizing recommendations

## 🛠️ Getting Started

### Prerequisites
- [ ] AWS account
- [ ] Basic Python or JavaScript knowledge (we'll use Python)
- [ ] Comfortable with basic code concepts

### Step-by-Step: Create Your First Lambda Function

#### 1. Navigate to Lambda Console

- Sign into AWS Console
- Search for "Lambda" in services
- Click "Lambda"
- Click orange "Create function" button

#### 2. Configure Basic Settings

**Function name**: `my-first-function`

**Runtime**: Python 3.11

**Architecture**: x86_64 (default is fine)

**Execution role**:
- Keep default: "Create a new role with basic Lambda permissions"
- AWS will create: `lambda_basic_execution`

#### 3. Write Your Code

In the code editor, replace the default code with:

```python
import json

def lambda_handler(event, context):
    """
    This is your Lambda function handler.
    
    event: contains the event data (what triggered the function)
    context: contains function execution information
    """
    
    # Log something
    print("Lambda function executed!")
    print(f"Event received: {event}")
    
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

**Understanding the Code**:
- `lambda_handler`: Function that AWS calls (the handler)
- `event`: Contains data about what triggered the function
- `context`: Contains info about the execution (function name, request ID, etc.)
- `return`: The response sent back to whoever/whatever triggered the function

#### 4. Deploy

- Click orange "Deploy" button
- Your code is now live!

#### 5. Test Your Function

- Click "Test" button
- A test event popup appears
- For now, keep the default event (just `{}` - empty JSON)
- Click "Test"
- You should see:
  - **Execution result**: "succeeded"
  - **Function Logs**: Shows your print statements
  - **Response**: Returns `{'statusCode': 200, 'body': 'Hello from Lambda!'}`

🎉 **You just created and ran a Lambda function!**

### More Complex Example: Process Data

```python
import json
import math

def lambda_handler(event, context):
    """Process user data"""
    
    # Get data from the event
    name = event.get('name', 'Guest')
    age = event.get('age', 18)
    
    # Do something with it
    birth_year = 2025 - age
    
    # Return result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Hello {name}!',
            'birth_year': birth_year,
            'verification': age >= 18
        })
    }
```

**Test with:**
```json
{
  "name": "Alice",
  "age": 25
}
```

### Common Triggers (Connect Lambda to Services)

**From Lambda Console:**

#### 1. **S3 Trigger** (Run when file uploaded)

- Click "Add trigger"
- Select "S3"
- **Bucket**: Choose your bucket (or create one)
- **Event type**: s3:ObjectCreated:*
- Click "Add"

Now whenever someone uploads a file to that S3 bucket, your Lambda runs automatically!

#### 2. **API Gateway Trigger** (Run via HTTP request)

- Click "Add trigger"
- Select "API Gateway"
- Create new API
- Select "REST API"
- Click "Add"

Copy the API endpoint URL and visit it in browser - your Lambda runs!

#### 3. **CloudWatch Event Trigger** (Run on schedule)

- Click "Add trigger"
- Select "EventBridge (CloudWatch Events)"
- Create new rule
- **Rule type**: Schedule expression
- **Schedule expression**: `rate(1 hour)` (runs every hour)
- Click "Add"

#### 4. **DynamoDB Trigger** (Run when database changes)

- Click "Add trigger"
- Select "DynamoDB"
- Choose your table
- This is an event stream trigger

## 💰 Pricing Overview

Lambda pricing is based on:

### 1. **Request Charges** (per 1,000,000 requests)
- **Price**: $0.20 per 1,000,000 requests
- **Example**: 10 million requests = $2.00

### 2. **Compute Time** (per GB-second)

Charged in increments of 1 millisecond.

- **Price**: $0.0000166667 per GB-second
- **GB-second**: How much memory × how long it ran

**Examples**:
- Function with 128 MB memory running for 3 seconds:
  - 0.125 GB × 3 seconds = 0.375 GB-seconds
  - Cost: 0.375 × $0.0000166667 = **$0.000006 (less than 1 cent!)**

- Function with 1024 MB (1 GB) memory running for 10 seconds:
  - 1 GB × 10 seconds = 10 GB-seconds
  - Cost: 10 × $0.0000166667 = **$0.00017 (very cheap)**

### 3. **Memory Options**

More memory = faster execution (and higher cost)

- 128 MB: $0.0000000021 per second
- 256 MB: $0.0000000042 per second
- 512 MB: $0.0000000083 per second
- 1024 MB (1 GB): $0.0000000167 per second
- 3008 MB: $0.0000000501 per second (max)

### Free Tier (Always)

**1,000,000 requests** per month - FREE  
**3,600,000 GB-seconds** per month - FREE

This is enough for:
- 1 million API calls/month, or
- Processing 1000 S3 uploads/day, or
- Running 4 functions constantly

💰 **Cost Tips**:

1. **You're almost always in free tier** - Lambda is incredibly cheap
2. **Only pay for what you use** - not for idle time
3. **More memory = shorter execution = sometimes cheaper total**
   - 256 MB function taking 10 seconds: more expensive
   - 1024 MB function taking 2 seconds: might be cheaper!
4. **Monitor with CloudWatch** - see your actual spending
5. **Use Provisioned Concurrency** only if you need instant response (has cost)

## ⚠️ Important Limitations to Know

### Execution Environment Limits

- **Timeout**: Maximum 15 minutes (900 seconds)
  - Perfect for: Processing files, API requests, data analysis
  - NOT good for: Long-running batch jobs (use EC2/Batch instead)

- **Memory**: 128 MB - 10,240 MB (10 GB)
  - Choose based on your code needs
  - Default is 128 MB (usually sufficient)
  - More memory = faster CPU = potentially faster execution

- **Disk Space** (/tmp): 512 MB
  - Temporary storage during execution
  - Cleaned up after function completes
  - Good for: Processing files, caching

- **Concurrent Executions**: 1,000 by default
  - Each trigger creates a new execution
  - If you hit limit, functions queue up
  - Can request AWS to increase limit

### Code Limits

- **Deployment package size**: 50 MB (zipped), 250 MB (unzipped)
  - If larger: upload to S3 and reference from Lambda
  - Or use container images (up to 10 GB)

- **Environment variables**: 4 KB total
  - Store configuration here (not in code!)

- **Layer size**: 256 MB total
  - Use for shared libraries/dependencies

### Cold Starts

**What**: When Lambda hasn't run recently, AWS has to initialize your function

**Typical times**:
- Python: 100-200 ms
- Node.js: 50-100 ms
- Java/Go: 500+ ms

**Solutions**:
- Keep functions warm with scheduled triggers
- Use Provisioned Concurrency (costs money)
- Optimize code and dependencies

## 🔗 Related Services

- **API Gateway**: Create REST APIs backed by Lambda
- **S3**: Trigger Lambda on file uploads
- **DynamoDB**: Serverless database often paired with Lambda
- **SNS/SQS**: Async processing with Lambda
- **CloudWatch Events**: Schedule Lambda functions
- **CloudWatch Logs**: View Lambda function logs
- **X-Ray**: Debug and analyze Lambda performance
- **SAM (Serverless Application Model)**: Deploy Lambda functions locally and to AWS

## 📚 Next Steps

- [ ] Try: [Trigger Lambda from S3](../../tutorials/deploy-web-server.md)
- [ ] Learn: [Environment Variables](../../compute/lambda/what-is-lambda.md)
- [ ] Explore: [Lambda Layers](../../compute/lambda/use-cases.md) for dependencies
- [ ] Build: [Create a REST API](../../tutorials/serverless-api.md)
- [ ] Deep dive: [IAM Execution Roles](../../security/iam/README.md)

## 🆘 Common Issues & Solutions

**Problem**: "Timeout - Task timed out after 60 seconds"
**Solution**:
- Function taking too long
- Increase timeout: Configuration → General configuration → Timeout
- If > 15 minutes needed: use EC2 or Batch instead
- Optimize code to run faster

**Problem**: "Permission denied" error
**Solution**:
- Execution role needs more permissions
- Go to Configuration → Permissions
- Click execution role name
- Add policy granting needed permissions (e.g., S3FullAccess, DynamoDBAccess)

**Problem**: Lambda can't access database/service
**Solution**:
1. **Check network**: Is Lambda in same VPC? (usually not needed unless in VPC)
2. **Check security groups**: Does security group allow Lambda?
3. **Check IAM role**: Does execution role have permissions?
4. **Check service**: Is the service publicly accessible or requires credentials?

**Problem**: "Payload too large" error
**Solution**:
- API response too big
- Return only needed data
- For large responses: save to S3, return S3 URL

**Problem**: Cold start too slow
**Solution**:
- Use Provisioned Concurrency (costs money)
- Keep function "warm" with scheduled trigger
- Minimize dependencies and code size
- Use faster runtime (Node.js vs Java)

## 💡 Best Practices

1. **Keep Functions Small**: Do one thing well
2. **Use Environment Variables**: Store config outside code
3. **Log Everything**: Use print() or logger for debugging
4. **Handle Errors Gracefully**: Always return proper responses
5. **Optimize Memory**: Right-size for your needs
6. **Use VPC Only If Needed**: No VPC = faster cold starts
7. **Monitoring**: Set up CloudWatch alarms for errors
8. **Use Layers**: Share code across multiple functions
9. **Test Locally**: Use SAM CLI to test before deploying
10. **Clean Up Old Versions**: Lambda keeps all versions (minimal cost but adds up)

## 🎓 Hands-On Exercise: Image Thumbnail Generator

**Goal**: Create Lambda function that creates thumbnails when images uploaded to S3

```python
import json
import boto3
import os
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Create thumbnail from uploaded image"""
    
    try:
        # Get bucket and key from S3 event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Download original image
        response = s3.get_object(Bucket=bucket, Key=key)
        image_data = response['Body'].read()
        
        # Open and process image
        image = Image.open(BytesIO(image_data))
        image.thumbnail((100, 100))  # Create 100x100 thumbnail
        
        # Save thumbnail
        thumbnail_key = f"thumbnails/{key}"
        buffer = BytesIO()
        image.save(buffer, format='JPEG')
        buffer.seek(0)
        
        # Upload thumbnail
        s3.put_object(
            Bucket=bucket,
            Key=thumbnail_key,
            Body=buffer.getvalue(),
            ContentType='image/jpeg'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Thumbnail created: {thumbnail_key}')
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
```

**Setup**:
1. Create Lambda function with this code
2. Add layer for Pillow dependency
3. Add S3 trigger for s3:ObjectCreated:*
4. Give execution role S3 permissions
5. Upload image to S3 - thumbnail created automatically!

## 📊 Monitoring Your Functions

**CloudWatch Metrics**:
- Invocations (how many times called)
- Errors (failed executions)
- Duration (how long functions take)
- Throttles (hitting concurrency limit)

**View Logs**:
1. Click function in Lambda console
2. "Monitor" tab
3. Click "View CloudWatch logs"
4. See all print() output from your function

**Set Up Alarms**:
1. CloudWatch → Alarms
2. Create alarm for high error rate
3. Get notified if errors > 1% of invocations

## 📖 Additional Resources

- [Official Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [AWS Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Lambda Pricing Calculator](https://calculator.aws/)
- [AWS SAM (Serverless Application Model)](https://aws.amazon.com/serverless/sam/)
- [Serverless Framework](https://www.serverless.com/)
- [Lambda Deployment Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/deployment-package-v2.html)

---

**Last Updated**: January 2025  
**Difficulty Level**: ⭐⭐ Intermediate  
**Estimated Learning Time**: 3-4 hours
